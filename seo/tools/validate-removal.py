"""Validate the explicitly authorized removals and remaining site functionality."""
from pathlib import Path
import json,csv,re,hashlib,subprocess,datetime,urllib.request,urllib.error
from bs4 import BeautifulSoup
O=Path(__file__).resolve().parents[1];R=O.parent
E=json.loads((O/'evidence.json').read_text('utf8'));policy=json.loads((O/'business-policy.json').read_text('utf8'))
old=json.loads((O/'history/before-chiptuning-removal/functional-baseline.json').read_text('utf8'));errors=[]
removed=set(policy['removed_urls'].values());pages=E['pages'];paths={p['url'] for p in pages};titles=[];scripts=[]
for rel,baseline in old.items():
 f=R/rel
 if rel in removed:
  if f.exists():errors.append('Retired file still exists: '+rel)
  continue
 if not f.exists():errors.append('Unexpected deletion: '+rel);continue
 raw=f.read_text('utf8');s=BeautifulSoup(raw,'html.parser')
 current={'scripts':[str(x) for x in s.find_all('script') if x.get('type')!='application/ld+json'],'forms':[str(x) for x in s.find_all('form')],'contact':[str(x) for x in s.select('a[href]') if x['href'].startswith(('tel:','mailto:','https://wa.me'))]}
 if current!=baseline:errors.append('Protected functionality changed: '+rel)
 if re.search(r'chiptuning|chip-tuning|kennfeldoptimierung|stage [12]',raw,re.I):errors.append('Retired offer remains: '+rel)
 scripts += [x.get_text() for x in s.find_all('script') if not x.get('src') and x.get('type')!='application/ld+json']
for p in pages:
 if p['verification']:continue
 titles.append(p['title'])
 if len(p['headings']['h1'])!=1:errors.append('H1 count: '+p['path'])
 if len(p['canonical'])!=1 or p['canonical'][0] not in paths:errors.append('Canonical: '+p['path'])
 if any('parse_error' in x for x in p['schema']):errors.append('Schema: '+p['path'])
 for l in p['links']:
  if not l['resolved'] and not l['asset'] or l['missing_fragment']:errors.append('Broken link: '+p['path']+' '+l['href'])
 if p['sitemap'] and ('noindex' in ' '.join(p['robots']) or p['canonical']!=[p['url']]):errors.append('Sitemap: '+p['path'])
if len(set(titles))!=len(titles):errors.append('Duplicate titles')
for source in E['sources']:
 actual=hashlib.sha256((R/'Datei Manager'/source['name']).read_bytes()).hexdigest()
 original=next(x for x in json.loads((O/'history/before-chiptuning-removal/evidence.json').read_text('utf8'))['sources'] if x['name']==source['name'])
 if actual!=original['sha256']:errors.append('Original export changed')
for k,rules in policy['removed_routing_rules'].items():
 if any(r in E['config'][k] for r in rules):errors.append('Retired routing still present')
oldE=json.loads((O/'history/before-chiptuning-removal/evidence.json').read_text('utf8'))
for k in ['redirects','rewrites']:
 expected=[r for r in oldE['config'][k] if r not in policy['removed_routing_rules'][k]]
 if E['config'][k]!=expected:errors.append('Unrelated routing changed')
for a in oldE['assets']:
 if a['file'].endswith(('.js','.css')) or a['file'] in ['package.json','package-lock.json']:
  if hashlib.sha256((R/a['file']).read_bytes()).hexdigest()!=a['sha256']:errors.append('Protected asset changed: '+a['file'])
r=subprocess.run(['node','-e','const fs=require("fs"),vm=require("vm");for(const s of JSON.parse(fs.readFileSync(0,"utf8")))new vm.Script(s);'],input=json.dumps(scripts),text=True,capture_output=True)
if r.returncode:errors.append(r.stderr)
def rows(n):return list(csv.DictReader((O/n).open(encoding='utf-8-sig'),delimiter=';'))
if {r['URL'] for r in rows('seo-map.csv') if r['Dateipfad']}!=paths:errors.append('SEO map differs')
for r in rows('keyword-map.csv'):
 if re.search('chiptuning|softwareoptimierung',r['bestehende Zielseite'],re.I):errors.append('Retired keyword target')
compiled=json.loads((O/'routing-compiled.json').read_text('utf8'))
if compiled.get('error'):errors.append('Routing compilation failed')
http=[]
targets=[p['path'] for p in pages]+list(policy['removed_urls'])+[r['source'].replace('(.*)','test') for r in policy['removed_routing_rules']['redirects']]+['/sitemap.xml','/robots.txt']
for path in targets:
 try:
  with urllib.request.urlopen('http://127.0.0.1:4174'+path,timeout=10) as resp:code=resp.status
 except urllib.error.HTTPError as ex:code=ex.code
 except Exception as ex:code=str(ex)
 expected=404 if re.search('chiptuning|softwareoptimierung',path) else 200
 http.append({'path':path,'status':code,'expected':expected})
 if code!=expected:errors.append('HTTP: '+path+' '+str(code))
result={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'local authorized business correction','result':'passed' if not errors else 'failed','errors':errors,'html_checked':len(pages),'authorized_deletions':len(removed),'http_checks':http,'inline_js_parsed':len(scripts),'forms_submitted':0,'functional_baseline':'history/before-chiptuning-removal/functional-baseline.json'}
(O/'validation-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({k:v for k,v in result.items() if k!='http_checks'},ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
