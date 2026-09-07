from pathlib import Path as _Path
import runpy as _runpy
if (_Path(__file__).resolve().parents[1]/"business-policy.json").exists():
    _runpy.run_path(str(_Path(__file__).with_name("validate-removal.py")))
    raise SystemExit(0)

"""Meaningful release checks; run with the local read-only preview on port 4173."""
from pathlib import Path
import json,csv,re,hashlib,collections,urllib.request,urllib.error,urllib.parse as U,concurrent.futures,datetime,subprocess
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[2];O=R/'seo'
E=json.loads((O/'evidence.json').read_text('utf8'));P=E['pages'];B=E['pages'][0]['url'].split('/',3)[:3];B='/'.join(B)
baseline=json.loads((O/'protection-baseline.json').read_text('utf8'));I=json.loads((O/'implementation.json').read_text('utf8'));errors=[]
def sha(v):return hashlib.sha256(v.encode('utf8')).hexdigest()
def protected(raw):
    s=BeautifulSoup(raw,'html.parser')
    return {'scripts':[sha(m.group()) for m in re.finditer(r'<script\b(?![^>]*application/ld\+json)[^>]*>.*?</script>',raw,re.S|re.I)],'forms':[sha(m.group()) for m in re.finditer(r'<form\b[^>]*>.*?</form>',raw,re.S|re.I)],'noscript':[sha(m.group()) for m in re.finditer(r'<noscript\b[^>]*>.*?</noscript>',raw,re.S|re.I)],'contacts':sorted(x['href'] for x in s.select('a[href]') if x['href'].startswith(('tel:','mailto:','https://wa.me/'))),'buttons':sorted((x.get('id',''),x.get('type',''),x.get_text(' ',strip=True)) for x in s.find_all('button'))}
for f,v in baseline['pages'].items():
    if not (R/f).exists():errors.append('Removed page: '+f);continue
    if json.loads(json.dumps(protected((R/f).read_text('utf8'))))!=v:errors.append('Protected HTML changed: '+f)
css_additions={
'css/style.css':'''/* Readable editorial links on the existing dark surfaces; CTA styles stay intact. */
main p a:not(.btn), .article-body a:not(.btn) {
  color: var(--color-brand-light);
  text-decoration: underline;
  text-underline-offset: 0.18em;
}
''',
'css/home2.css':'''\n/* Make the linked service headings and editorial entrances discoverable. */
body.home2-page .service-tile h3 a,
body.home2-page #leistungen p a,
body.home2-page .contact-intro p a {
  text-decoration: underline;
  text-underline-offset: 0.18em;
}
'''}
for f,h in baseline['files'].items():
    raw=(R/f).read_bytes()
    if f in css_additions:
        text=raw.decode('utf8');assert text.count(css_additions[f])==1
        raw=text.replace(css_additions[f],'').encode('utf8')
    if hashlib.sha256(raw).hexdigest()!=h:errors.append('Protected file changed beyond approved addition: '+f)
for f,h in baseline['source_hashes'].items():
    if hashlib.sha256((R/'Datei Manager'/f).read_bytes()).hexdigest()!=h:errors.append('Source changed: '+f)
paths={p['path']:p for p in P}
for p in P:
    if p['verification']:continue
    if len(p['headings']['h1'])!=1:errors.append('H1 count: '+p['path'])
    if len(p['canonical'])!=1 or not p['canonical'][0].startswith('https://www.powertech-performance.com/'):errors.append('Canonical host/count: '+p['path'])
    elif U.urlsplit(p['canonical'][0]).path not in paths:errors.append('Missing canonical target: '+p['path'])
    if any('parse_error' in s for s in p['schema']):errors.append('Invalid JSON-LD: '+p['path'])
    if any(not h.strip() for level in p['headings'].values() for h in level):errors.append('Empty heading: '+p['path'])
    for l in p['links']:
        if not l['resolved'] and not l['asset']:errors.append('Broken internal target: '+p['path']+' -> '+l['href'])
        if l['missing_fragment']:errors.append('Missing fragment: '+p['path']+' -> '+l['href'])
    for img in p['images']:
        u=U.urlsplit(U.urljoin(p['url'],img['src']))
        if u.hostname in ['www.powertech-performance.com','powertech-performance.com'] and not (R/u.path.lstrip('/')).is_file():errors.append('Missing image: '+img['src'])
    if p['sitemap'] and ('noindex' in ' '.join(p['robots']) or p['canonical']!=[p['url']]):errors.append('Non-primary sitemap entry: '+p['path'])
titles=collections.defaultdict(list)
for p in P:
    if not p['verification']:titles[p['title']].append(p['path'])
for title,v in titles.items():
    if len(v)>1:errors.append('Duplicate title: '+' | '.join(v))
old=json.loads((O/'history/2026-09-07-analysis/evidence.json').read_text('utf8'))
for rule in old['config']['redirects']:
    if rule not in E['config']['redirects']:errors.append('Existing redirect changed: '+rule['source'])
for rule in old['config']['rewrites']:
    if rule not in E['config']['rewrites']:errors.append('Existing rewrite changed: '+rule['source'])
compiled=json.loads((O/'routing-compiled.json').read_text('utf8'))
if compiled.get('error'):errors.append('Vercel routing compiler error')

# Real local HTTP GETs, no SMTP/API invocation. urllib here follows 308 explicitly.
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):return None
def check(path):
    initial='http://127.0.0.1:4173'+path;url=initial;chain=[]
    try:
        op=urllib.request.build_opener(NoRedirect)
        for _ in range(8):
            try:
                with op.open(url,timeout=10) as r:return {'path':path,'status':r.status,'end':r.url,'chain':chain}
            except urllib.error.HTTPError as ex:
                if ex.code in [301,302,303,307,308]:
                    nxt=U.urljoin(url,ex.headers['Location']);chain.append({'status':ex.code,'location':nxt});url=nxt
                else:return {'path':path,'status':ex.code,'end':url,'chain':chain}
        return {'path':path,'error':'redirect loop','chain':chain}
    except Exception as ex:return {'path':path,'error':str(ex)}
urls=set(p['path'] for p in P)
urls.update(r['source']+'?gclid=seo-preview&test=1' for r in I['redirect_repairs'])
urls.update(['/trockeneisreinigung.html?test=1','/trockeneisreinigung/?test=1','/robots.txt','/sitemap.xml','/adblue-deaktivieren/'])
urls.update(r['source'].replace('(.*)','qa-sample') for r in old['config']['redirects'])
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:http=list(pool.map(check,sorted(urls)))
for r in http:
    expected=404 if r['path']=='/adblue-deaktivieren/' else 200
    if r.get('status')!=expected:errors.append('HTTP: '+str(r))
    if '?' in r['path'] and U.urlsplit(r.get('end','')).query!=U.urlsplit(r['path']).query:errors.append('Query parameters lost: '+r['path'])

# Parse every executable inline JS block with Node without executing it.
inline=[{'file':p['file'],'scripts':[m[1] for m in re.finditer(r'<script\b(?![^>]*application/ld\+json)[^>]*>(.*?)</script>',(R/p['file']).read_text('utf8'),re.S|re.I)]} for p in P]
nodecode="let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{for(const p of JSON.parse(s)){for(const x of p.scripts){try{new (require('node:vm').Script)(x,{filename:p.file})}catch(e){console.error(e.message);process.exitCode=1;}}}});"
parsed=subprocess.run(['node','-e',nodecode],input=json.dumps(inline),encoding='utf8',capture_output=True)
if parsed.returncode:errors.append('Inline JS parse: '+parsed.stderr)
for f in ['js/main.js','js/home2.js','api/send-lead.js','api/_lib/lead-email.js']:
    r=subprocess.run(['node','--check',str(R/f)],capture_output=True,text=True)
    if r.returncode:errors.append('JS parse '+f+': '+r.stderr)

def readcsv(name):return list(csv.DictReader((O/name).open(encoding='utf-8-sig',newline=''),delimiter=';'))
maps=readcsv('seo-map.csv');kw=readcsv('keyword-map.csv');links=readcsv('internal-links.csv')
if {p['url'] for p in P}!={r['URL'] for r in maps if r['Dateipfad']}:errors.append('SEO map does not cover current site')
if sum(int(r['Impressionen'] or 0) for r in maps)!=6493:errors.append('Impression reconciliation failed')
if any(r[k] for r in kw for k in ['Klicks','Impressionen','CTR','Position','Suchvolumen','CPC']):errors.append('Invented keyword measurement')
if len([r for r in links if r['Link-Typ'].startswith('Bestand')])!=sum(len(p['links']) for p in P):errors.append('Link count mismatch')
owners=collections.defaultdict(set)
for r in kw:
    if r['Hauptkeyword oder Nebenkeyword']=='Hauptkeyword (redaktionell)':owners[(r['Keyword / Suchanfrage'].casefold(),r['Suchintention'])].add(r['passende bestehende Seite'])
for k,v in owners.items():
    if len(v)>1:errors.append('Conflicting primary keyword: '+str(k))
report={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'lokal; nicht veröffentlicht','result':'passed' if not errors else 'failed','errors':errors,'html_checked':len(P),'http_checks':len(http),'http_results':http,'protected_original_html':len(baseline['pages']),'source_hashes_unchanged':not any('Source changed' in e for e in errors),'forms_submitted':0,'external_tracking_in_preview':'blocked by local response CSP, not a production change','build_lint_test_scripts':json.loads((R/'package.json').read_text('utf8')).get('scripts',{}),'inline_js_parsed':sum(len(p['scripts']) for p in inline),'known_open_url':'/adblue-deaktivieren/ (404, decision required)'}
(O/'validation-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k!='http_results'},ensure_ascii=False,indent=2))
raise SystemExit(1 if errors else 0)
