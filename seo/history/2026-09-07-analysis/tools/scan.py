"""Read-only site/source inventory; writes only seo/evidence.json. Python + beautifulsoup4."""
from pathlib import Path
import csv,json,re,hashlib,collections,urllib.parse as U,xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'seo'
BASE='https://powertech-performance.com'
def txt(x): return ' '.join(x.get_text(' ',strip=True).split()) if x else ''
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
cfg=json.loads((ROOT/'vercel.json').read_text('utf-8'))
rewrites={r['destination'].lstrip('/'):r['source'] for r in cfg['rewrites']}
redirects={r['source']:r['destination'] for r in cfg['redirects'] if '(.*)' not in r['source']}
sources=[]
for f in sorted((ROOT/'Datei Manager').iterdir()):
    if f.suffix.lower()!='.csv': continue
    content=f.read_text('utf-8-sig'); delim=csv.Sniffer().sniff(content[:4096],delimiters=',;\t').delimiter
    reader=csv.DictReader(content.splitlines(),delimiter=delim); rows=list(reader)
    sources.append(dict(name=f.name,delimiter=delim,columns=reader.fieldnames,rows=rows,sha256=digest(f),replacement_chars=content.count('\ufffd')))
index=next(s for s in sources if 'Dateipfad' in s['columns'])
perf=next(s for s in sources if 'Impressionen' in s['columns'])
byfile={r['Dateipfad']:r for r in index['rows']}
sitemap=[e.text for e in ET.parse(ROOT/'sitemap.xml').iter() if e.tag.endswith('}loc')]
blocked=[l.split(':',1)[1].strip() for l in (ROOT/'robots.txt').read_text().splitlines() if l.startswith('Disallow:')]
pages=[]
for f in sorted(ROOT.rglob('*.html')):
    if any(x in f.relative_to(ROOT).parts for x in ('node_modules','.git','seo')): continue
    rel=f.relative_to(ROOT).as_posix(); raw=f.read_text('utf-8'); s=BeautifulSoup(raw,'html.parser')
    route=rewrites.get(rel,'/'+rel)
    if route.endswith('/index.html'): route=route[:-10]
    url=BASE+route
    can=[x.get('href','') for x in s.select('link[rel~=canonical]')]
    main=s.select_one('.article-body') or s.find('main') or s.body or s
    heads={h:[txt(x) for x in s.find_all(h)] for h in ['h1','h2','h3']}
    metas=[x.get('content','') for x in s.select('meta[name=description]')]
    robots=[x.get('content','') for x in s.select('meta[name=robots],meta[name=googlebot]')]
    links=[]
    for a in s.select('a[href],area[href]'):
        href=a['href']; absolute=U.urljoin(url,href); u=U.urlsplit(absolute)
        if u.hostname not in ('powertech-performance.com','www.powertech-performance.com'): continue
        context='Inhalt'
        for parent in [a]+list(a.parents):
            if not getattr(parent,'attrs',None): continue
            cls=' '.join(parent.get('class',[]))
            if 'breadcrumb' in cls: context='Breadcrumb';break
            if parent.name=='footer': context='Footer';break
            if parent.name=='nav': context='Navigation';break
            if parent.name=='header': context='Header';break
            if parent.name=='aside': context='Sidebar';break
        links.append(dict(href=href,url=U.urlunsplit((u.scheme,u.netloc,u.path or '/',u.query,'')),path=u.path or '/',fragment=u.fragment,anchor=txt(a) or a.get('aria-label','') or ' | '.join(x.get('alt','') for x in a.find_all('img')),context=context,rel=a.get('rel',[])))
    images=[dict(src=x.get('src',''),alt=x.get('alt'),loading=x.get('loading',''),width=x.get('width',''),height=x.get('height','')) for x in s.find_all('img')]
    schema=[]
    for x in s.select('script[type="application/ld+json"]'):
        try: schema.append(json.loads(x.string or x.get_text()))
        except Exception as e: schema.append({'parse_error':str(e),'raw':x.get_text()})
    for x in main.select('script,style,noscript'): x.decompose()
    content=txt(main)
    pages.append(dict(file=rel,url=url,path=route,canonical=can,title=txt(s.title),description=metas,robots=robots,blocked=any(route.startswith(b) for b in blocked),headings=heads,links=links,images=images,aria_images=[dict(label=x.get('aria-label',''),classes=x.get('class',[])) for x in s.select('[role=img]')],schema=schema,microdata=[x.get('itemtype') for x in s.select('[itemscope]')],content=content,words=len(content.split()),sections=[dict(id=x.get('id',''),heading=txt(x.find(['h1','h2','h3']))) for x in s.find_all('section')],ids=[x['id'] for x in s.select('[id]')],source_index=byfile.get(rel,{}),sitemap=url in sitemap,verification=rel.startswith('google'),replacement_chars=raw.count('\ufffd')))
paths={p['path']:p for p in pages}
aliases={'/'+p['file']:p['path'] for p in pages}
def resolve(path):
    if path in redirects: path=redirects[path]
    if path in paths:return path
    if path in aliases:return aliases[path]
    return None
for p in pages:
    for l in p['links']:
        l['resolved']=resolve(l['path'])
        l['missing_fragment']=bool(l['fragment'] and l['resolved'] and l['fragment'] not in paths[l['resolved']]['ids'])
        l['asset']=bool((ROOT/l['path'].lstrip('/')).is_file() and not l['path'].endswith('.html'))
for p in pages:
    p['incoming']=sorted({q['url'] for q in pages if q!=p and any(l['resolved']==p['path'] for l in q['links'])})
    p['outgoing']=sorted({BASE+l['resolved'] for l in p['links'] if l['resolved'] and l['resolved']!=p['path']})
    p['body_incoming']=sorted({q['url'] for q in pages if q!=p and any(l['resolved']==p['path'] and l['context']=='Inhalt' for l in q['links'])})
matches=[]
for r in perf['rows']:
    url=r['Die häufigsten Seiten']; path=U.urlsplit(url).path
    exact=next((p for p in pages if p['url']==url),None)
    candidate=paths.get(path) or (paths.get(path.rstrip('/')) if path!='/' else None)
    method='exakt' if exact else 'Host/Slash-Variante; technisch unbestätigt' if candidate else 'kein lokaler Pfad'
    thematic=None
    if not candidate:
        thematic=paths.get('/blog/'+path.strip('/')+'/')
        if path.strip('/')=='adblue-deaktivieren': thematic=paths.get('/adblue-service')
    matches.append(dict(source_url=url,impressions=int(r['Impressionen']),method=method,candidate=(exact or candidate or {}).get('url',''),thematic=(thematic or {}).get('url','')))
assets=[]
for f in ROOT.rglob('*'):
    if not f.is_file() or any(x in f.relative_to(ROOT).parts for x in ('node_modules','.git','seo','Datei Manager')):continue
    assets.append(dict(file=f.relative_to(ROOT).as_posix(),bytes=f.stat().st_size,sha256=digest(f)))
evidence=dict(sources=sources,pages=pages,sitemap=sitemap,robots=(ROOT/'robots.txt').read_text(),config=cfg,performance=matches,assets=assets)
(OUT/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(html=len(pages),content_pages=sum(not p['verification'] for p in pages),sitemap=len(sitemap),links=sum(len(p['links']) for p in pages),impressions=sum(m['impressions'] for m in matches),matches=collections.Counter(m['method'] for m in matches),orphans=[p['path'] for p in pages if not p['incoming']],missing_targets=collections.Counter(l['path'] for p in pages for l in p['links'] if not l['resolved'] and not l['asset']),missing_fragments=collections.Counter(l['path']+'#'+l['fragment'] for p in pages for l in p['links'] if l['missing_fragment']),jsonld=sum(bool(p['schema']) for p in pages),source_replacement_chars=[(s['name'],s['replacement_chars']) for s in sources]),ensure_ascii=False,indent=2))
