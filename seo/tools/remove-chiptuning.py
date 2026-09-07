"""One-time implementation of the explicit business-scope correction."""
from pathlib import Path
import re,json,shutil,datetime
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[2];O=R/'seo'
removed={'/chiptuning':'chiptuning.html',**{'/blog/'+slug+'/':'blog/'+slug+'/index.html' for slug in ['chiptuning-raum-erfurt','chiptuning-raumerfurt','softwareoptimierung-erfurt','softwareoptimierung-dpf-off-erfurt']}}
archive=O/'history'/'before-chiptuning-removal'
if archive.exists():raise SystemExit('Already applied')
archive.mkdir()
for f in O.iterdir():
 if f.is_file():shutil.copy2(f,archive/f.name)
snapshot={}
for f in R.rglob('*.html'):
 if any(x in f.relative_to(R).parts for x in ['seo','node_modules','.git']):continue
 raw=f.read_text('utf8');s=BeautifulSoup(raw,'html.parser')
 snapshot[f.relative_to(R).as_posix()]={'scripts':[str(x) for x in s.find_all('script') if x.get('type')!='application/ld+json'],'forms':[str(x) for x in s.find_all('form')],'contact':[str(x) for x in s.select('a[href]') if x['href'].startswith(('tel:','mailto:','https://wa.me'))]}
(archive/'functional-baseline.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=2),'utf8')
cfg=json.loads((R/'vercel.json').read_text('utf8'))
removed_rules={k:[r for r in cfg[k] if any(t in r['source'] or t in r['destination'] for t in ['chiptuning','softwareoptimierung'])] for k in ['redirects','rewrites']}
for k in removed_rules:cfg[k]=[r for r in cfg[k] if r not in removed_rules[k]]
(R/'vercel.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n','utf8')
for rel in removed.values():
 f=(R/rel).resolve()
 assert f.is_relative_to(R.resolve()) and f.is_file()
 f.unlink()
for f in R.rglob('*.html'):
 if any(x in f.relative_to(R).parts for x in ['seo','node_modules','.git']):continue
 raw=f.read_text('utf8');s=raw
 # Remove complete cards and list entries; remove paragraphs linking a retired article.
 s=re.sub(r'<a\b[^>]*href="/(?:blog/)?(?:chiptuning|softwareoptimierung)[^"]*"[^>]*>.*?</a>',lambda m:'' if 'blog-card' in m.group() else m.group(),s,flags=re.S)
 s=re.sub(r'<li\b[^>]*>(?:(?!</li>).)*href="/(?:blog/)?(?:chiptuning|softwareoptimierung)[^"]*"(?:(?!</li>).)*</li>','',s,flags=re.S)
 s=re.sub(r'<p\b[^>]*>(?:(?!</p>).)*href="/(?:blog/)?(?:chiptuning|softwareoptimierung)[^"]*"(?:(?!</p>).)*</p>',lambda m: '<p>Unser Angebot im Bereich Fahrzeugsoftware: <a href="/adblue-service">AdBlue-Deaktivierung und AGR On-Off</a>. Informationen zur Fahrzeugpflege finden Sie im <a href="/glosar">Glossar</a>.</p>' if f.name=='index.html' and f.parent==R else '',s,flags=re.S)
 s=s.replace('Chiptuning &amp; Software','AdBlue &amp; AGR').replace('und Chiptuning','und AdBlue').replace(', Chiptuning',', AdBlue')
 s=s.replace('<h3>Softwareoptimierung</h3>','<h3>AdBlue-Deaktivierung und AGR On-Off</h3>').replace('Individuelles Chiptuning für mehr Leistung und Effizienz – abgestimmt auf Ihr Fahrzeug in Erfurt.','Unser Angebot im Bereich Fahrzeugsoftware umfasst AdBlue-Deaktivierung und AGR On-Off. Fahrzeug und Einsatzzweck werden vorab geklärt.')
 if f.name=='adblue-service.html':
  s=s.replace('AdBlue-Service Erfurt – Diagnose &amp; Reparatur | Powertech Performance','AdBlue-Deaktivierung &amp; AGR On-Off Erfurt | Powertech Performance')
  s=s.replace('AdBlue-Warnmeldung oder Start-Countdown? Powertech Performance in Erfurt prüft Diagnose, Reparatur und Rückrüstung. Fahrzeugdaten zur Beratung senden.','AdBlue-Deaktivierung und AGR On-Off bei Powertech Performance in Erfurt. Fahrzeugdaten und Einsatzzweck senden und die Möglichkeiten vorab klären.')
  s=s.replace('AdBlue-Service in Erfurt: Fehler klären lassen','AdBlue-Deaktivierung und AGR On-Off in Erfurt')
  s=s.replace('AdBlue-Service in Erfurt | Powertech Performance','AdBlue-Deaktivierung &amp; AGR On-Off | Powertech Performance')
  s=s.replace('AdBlue-Diagnose, Softwareprüfung, Reparatur, Rückrüstung und zulässige Sonderanwendungen für Diesel-Fahrzeuge bis Baujahr 2021.','AdBlue-Deaktivierung und AGR On-Off: Fahrzeug und Einsatzzweck vorab klären. Bestehende Hinweise zur Nutzung im Straßenverkehr beachten.')
  s=s.replace('<h3>Reparatur- und Rückrüstungsberatung</h3>','<h3>AGR On-Off</h3>')
  s=re.sub(r'(<h3>AGR On-Off</h3>\s*)<p>.*?</p>',r'\1<p>Für Anfragen zu AGR On-Off benötigen wir Fahrzeugdaten, den aktuellen Zustand und den vorgesehenen Einsatzzweck. Die technischen Möglichkeiten und Voraussetzungen werden vorab geklärt.</p>',s,flags=re.S)
  s=s.replace('<h3>Zulässige Sonderanwendungen</h3>','<h3>AdBlue-Deaktivierung</h3>')
  s=s.replace('"name": "AdBlue-Diagnose und Softwareprüfung"','"name": "AdBlue-Deaktivierung – Voraussetzungen vorab klären"').replace('"name": "Prüfung zulässiger Sonderanwendungen"','"name": "AGR On-Off – Voraussetzungen vorab klären"')
 if s!=raw:f.write_text(s,'utf8')
p=R/'sitemap.xml';s=p.read_text('utf8');s=re.sub(r'\s*<url>\s*<loc>[^<]*(?:chiptuning|softwareoptimierung)[^<]*</loc>.*?</url>','',s,flags=re.S);p.write_text(s,'utf8')
policy={'date':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Fahrzeugsoftware; Autoaufbereitung bleibt bestehen','allowed_software_services':['AdBlue-Deaktivierung','AGR On-Off'],'not_offered':['Chiptuning','Stage 1/2','Leistungssteigerung','allgemeine Kennfeldoptimierung','DPF-Off'],'removed_urls':removed,'removed_routing_rules':removed_rules,'publication':'lokal umgesetzt; noch nicht gepusht','instruction':'Explizite Nutzeranweisung: alle Chiptuning-Seiten löschen; nicht wieder anlegen oder bewerben.'}
(O/'business-policy.json').write_text(json.dumps(policy,ensure_ascii=False,indent=2)+'\n','utf8')
p=R/'AGENTS.md';s=p.read_text('utf8');s+='\n## Verbindlicher Leistungsumfang\n\nPowertech bietet KEIN Chiptuning, keine Stage-1/2-Leistungssteigerung und keine allgemeine Kennfeldoptimierung an. Im Bereich Fahrzeugsoftware sind ausschließlich AdBlue-Deaktivierung und AGR On-Off bestätigt. Autoaufbereitung und Fahrzeugpflege bleiben bestehen. Keine Chiptuning-Seiten, Links, Keywords oder Angebote wieder anlegen, auch nicht aufgrund historischer SEO-Dateien. DPF-Off ist kein bestätigtes Angebot. Maßgeblich: `seo/business-policy.json`. Die fünf dort dokumentierten Seiten wurden ausdrücklich zur Löschung freigegeben. Originalexporte und historische Audits sind nur Belege, keine aktuellen Leistungsangaben. Bestehende rechtliche Hinweise, Tracking und Formulare erhalten.\n';p.write_text(s,'utf8')
p=O/'implementation.json';d=json.loads(p.read_text('utf8'))
for path,rel in removed.items():d['metadata'].pop(path,None);d['changed_pages'].pop(rel,None)
d['metadata']['/adblue-service'].update(keyword='AdBlue-Deaktivierung Erfurt',cluster='AdBlue / AGR')
d['redirect_repairs']=[r for r in d['redirect_repairs'] if not any(x in json.dumps(r) for x in ['chiptuning','softwareoptimierung'])]
d['business_policy']='business-policy.json';p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf8')
print('Removed',len(removed),'pages; preserved original exports and functional baseline.')
