"""Optional read-only HTTP checks of all inventory and performance URLs. No forms or tracking executed."""
from pathlib import Path
import json,urllib.request,urllib.error,urllib.parse,concurrent.futures,datetime
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[1]
e=json.loads((root/'evidence.json').read_text('utf8'))
urls=sorted(set([p['url'] for p in e['pages']]+[p['source_url'] for p in e['performance']]+['https://powertech-performance.com/robots.txt','https://powertech-performance.com/sitemap.xml']))
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl): return None
def check(url):
    chain=[]; current=url
    try:
        opener=urllib.request.build_opener(NoRedirect)
        for i in range(10):
            req=urllib.request.Request(current,headers={'User-Agent':'Powertech-SEO-Audit/1.0'})
            try: r=opener.open(req,timeout=18); break
            except urllib.error.HTTPError as ex:
                if ex.code in (301,302,303,307,308) and ex.headers.get('Location'):
                    target=urllib.parse.urljoin(current,ex.headers['Location'])
                    chain.append(dict(url=current,status=ex.code,location=target)); current=target
                else: raise
        else:return dict(url=url,status=None,error='Redirect limit',chain=chain)
        with r:
            data=r.read(2000000); s=BeautifulSoup(data,'html.parser')
            return dict(url=url,status=r.status,final_url=r.url,chain=chain,canonical=[x.get('href') for x in s.select('link[rel~=canonical]')],title=s.title.get_text(' ',strip=True) if s.title else '',h1=[x.get_text(' ',strip=True) for x in s.find_all('h1')],robots=[x.get('content') for x in s.select('meta[name=robots]')],x_robots=r.headers.get('X-Robots-Tag',''))
    except urllib.error.HTTPError as ex:return dict(url=url,status=ex.code,final_url=ex.url,error=str(ex),chain=chain)
    except Exception as ex:return dict(url=url,status=None,error=str(ex),chain=chain)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(check,urls))
(root/'live-check.json').write_text(json.dumps(dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),results=results),ensure_ascii=False,indent=2),encoding='utf8')
from collections import Counter
print(Counter(r['status'] for r in results))
