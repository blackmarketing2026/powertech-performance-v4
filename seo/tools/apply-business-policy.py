"""Apply permanent business exclusions to generated SEO outputs."""
from pathlib import Path
import csv,json,re
from urllib.parse import urlsplit
O=Path(__file__).resolve().parents[1]
policy=json.loads((O/'business-policy.json').read_text('utf8'));E=json.loads((O/'evidence.json').read_text('utf8'))
def retired(s):return any(x in s.lower() for x in ['chiptuning','softwareoptimierung'])
def read(n):return list(csv.DictReader((O/n).open(encoding='utf-8-sig',newline=''),delimiter=';'))
def write(n,rows):
 with (O/n).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter=';');w.writeheader();w.writerows(rows)
for name in ['seo-map.csv','url-mapping.csv']:
 rows=read(name)
 for r in rows:
  if retired(r.get('URL',r.get('Export-URL',''))):
   for k in ['Hauptthema','Optimierungspotenzial','Mögliche Zielseite','Lokale Zuordnung']:
    if k in r:r[k]=''
   for k,v in {'Status':'umgesetzt – ausdrücklich entfernt','SEO-Status':'Kein Angebot; nicht wiederherstellen','Indexierungsstatus':'Entfernt; 404 nach Veröffentlichung erwartet','Lokaler Status':'404 (beabsichtigt)','Umgesetzte Maßnahmen':'Seite und Routing auf Nutzeranweisung entfernt; keine Ersatzweiterleitung','Zuordnungstyp':'Historischer Messwert; kein aktuelles Leistungsziel'}.items():
    if k in r:r[k]=v
 write(name,rows)
for name in ['internal-links.csv','link-plan-status.csv']:
 rows=read(name)
 if name=='internal-links.csv':rows=[r for r in rows if not retired(r['Quellseite']+' '+r['Zielseite'])]
 else:
  for r in rows:
   if retired(r['Quellseite']+' '+r['Zielseite']):r.update(Status='nicht umgesetzt – dauerhaft verworfen',Begründung='Chiptuning wird nicht angeboten; Seiten ausdrücklich gelöscht.')
 write(name,rows)
s=json.loads((O/'summary.json').read_text('utf8'));s.update(removed_content_pages=5,retired_software_cluster=True,deferred_link_proposals=2,cancelled_link_proposals=4)
(O/'summary.json').write_text(json.dumps(s,ensure_ascii=False,indent=2),'utf8')
urls='\n'.join('- `'+x+'`' for x in policy['removed_urls'])
notice=f'''# Aktueller Leistungsumfang und Entfernung von Chiptuning

Die aktuelle Nutzeranweisung ersetzt alle früheren Chiptuning-Empfehlungen. Powertech bietet **kein Chiptuning**, keine Stage-1/2-Leistungssteigerung und keine allgemeine Kennfeldoptimierung an. Im Bereich Fahrzeugsoftware sind **AdBlue-Deaktivierung und AGR On-Off** bestätigt. Fahrzeugpflege und Autoaufbereitung bleiben bestehen. DPF-Off wird nicht als Angebot übernommen. Historische Exporte bleiben unverändert und begründen keine Wiederherstellung dieser Angebote.

## Umgesetzt

Fünf Seiten einschließlich interner Verweise, Blogkarten, Sitemap-Einträge und zugehöriger Routing-Regeln entfernt:

{urls}

Keine Ersatzweiterleitung auf eine thematisch abweichende Leistung. Die alten URLs sollen nach Veröffentlichung 404 liefern. Startseite, Glossar, Blogkategorien und AdBlue-Service benennen AdBlue/AGR. Metadaten und Angebotsdaten des Service wurden angepasst; vorhandene Hinweise zur Nutzung und Zulässigkeit bleiben erhalten. Formulare, Kontaktwege und ausführbare Skripte auf den verbleibenden Seiten bleiben unverändert.

## Aktueller Bestand

57 Inhaltsseiten plus eine Verifizierungsdatei, 49 Sitemap-Ziele, 969 interne Link-Vorkommen. Kein kaputtes internes Ziel und kein fehlendes Sprungziel. 38 ursprüngliche Linkvorschläge bleiben umgesetzt, vier sind durch die Leistungsentscheidung hinfällig, zwei Felgenpflege-Vorschläge bleiben zurückgestellt. Die Chiptuning-Gruppe K2 entfällt als aktives Kannibalisierungsthema. Keine bestätigte Ranking-Kannibalisierung mangels Query-URL-Zeitreihen.

## Weiteres Vorgehen

- Chiptuning nicht erneut anlegen, optimieren, verlinken oder in Search Console zur Indexierung anmelden.
- AdBlue-Deaktivierung und AGR On-Off auf `/adblue-service` bündeln; keine zusätzliche nahezu identische Leistungsseite erforderlich.
- Nach Veröffentlichung Sitemap erneut lesen lassen; die entfernten URLs aus bisherigen Beobachtungslisten streichen.
- Beobachten: `/adblue-service`, `/`, `/luxus-aufbereitung`, `/trockeneisreinigung`, `/blog/adblue-deaktivieren-vor-nachteile-wahrheit/`.
- `/ads`-Indexierung und das separate alte Ziel `/adblue-deaktivieren/` bleiben offen. Die Entfernung von Chiptuning ändert diese Entscheidungen nicht.
- Keyword-/Klick-/CTR-/Positionsdaten fehlen weiterhin. Historische Impressionen bleiben an ihrer ursprünglichen URL, auch bei bewusst entfernten Seiten.

Vorheriger Umsetzungsstand: `history/before-chiptuning-removal/`. Aktuelle technische Details und Zuordnungen: `evidence.json`, `seo-map.csv`, `keyword-map.csv`, `internal-links.csv`. Status der Veröffentlichung: siehe `business-policy.json`.
'''
for name in ['SEO-AUDIT.md','content-plan.md','changes.md']:(O/name).write_text(notice,'utf8')
p=O/'SEO-RULES.md';t=p.read_text('utf8')
if '## Verbindliche Leistungskorrektur' not in t:t=t.replace('\n\nStand:', '\n\n## Verbindliche Leistungskorrektur\n\nKein Chiptuning, keine Stage-1/2-Leistungssteigerung, keine allgemeine Kennfeldoptimierung. Fahrzeugsoftware ausschließlich AdBlue-Deaktivierung und AGR On-Off; Autoaufbereitung bleibt bestehen. `business-policy.json` hat Vorrang vor historischen Empfehlungen. Die fünf dokumentierten Seiten sind ausdrücklich gelöscht und dürfen nicht wiederhergestellt werden.\n\nStand:',1)
t=t.replace('62 Inhaltsseiten','57 Inhaltsseiten').replace('39 Blogartikel','35 Blogartikel').replace('`/adblue-service`, `/chiptuning`,','`/adblue-service`,').replace('15 explizite Rewrites','14 explizite Rewrites').replace('67 Redirects und 15 Rewrites',f"{len(E['config']['redirects'])} Redirects und 14 Rewrites")
t=re.sub(r'^\| Chiptuning \|.*$','| Fahrzeugsoftware | `/adblue-service` | Ausschließlich AdBlue-Deaktivierung und AGR On-Off; kein Chiptuning. |',t,flags=re.M)
t=t.replace('Tatsächlich belegtes Diagnose-/Reparaturangebot; fachlich abgestimmte Ratgeber separat.','Bestätigtes Angebot: AdBlue-Deaktivierung und AGR On-Off; Voraussetzungen und bestehende Nutzungshinweise beachten.')
t+='\n' if not t.endswith('\n') else ''
if 'apply-business-policy.py' not in t:t+='\nBei vorhandenem `business-policy.json` wendet der Reportgenerator abschließend `apply-business-policy.py` an. Es verwirft alte Chiptuning-Empfehlungen. Aktuelle Prüfung: `python seo/tools/validate.py` delegiert auf die Entfernungskontrolle. Der alte Statusgenerator darf den neuen Stand nicht überschreiben.\n'
p.write_text(t,'utf8')
for name in ['technical-inventory.md','data-analysis.md']:
 p=O/name;t=p.read_text('utf8');head='Aktuelle Leistungskorrektur: 5 Chiptuning-/Leistungsoptimierungsseiten ausdrücklich entfernt. 57 Inhaltsseiten, 49 Sitemap-Ziele. Historische Angaben unten beschreiben den vorherigen Stand, sofern abweichend. Maßgeblich: business-policy.json und evidence.json.\n\n'
 if not t.startswith('Aktuelle Leistungskorrektur:'):p.write_text(head+t,'utf8')
rows=read('implementation-status.csv')
for r in rows:
 if retired(' '.join(r.values())):
  for k in r:
   if k.lower()=='status':r[k]='ersetzt durch Leistungsentscheidung; siehe business-policy.json'
write('implementation-status.csv',rows)
print('Business policy applied to current reports.')
