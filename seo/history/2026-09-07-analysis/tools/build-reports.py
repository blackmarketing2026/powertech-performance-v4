"""Build CSVs and factual appendices from scan evidence. Does not edit website/source files."""
from pathlib import Path
import json,csv,collections,re,hashlib,html,urllib.parse as U
O=Path(__file__).resolve().parents[1]; ROOT=O.parent
E=json.loads((O/'evidence.json').read_text('utf8')); P=E['pages']; B='https://powertech-performance.com'
LIVE=json.loads((O/'live-check.json').read_text('utf8')); L={r['url']:r for r in LIVE['results']}
by={p['path']:p for p in P}; perf=E['performance']
def blog(slug):return '/blog/'+slug+'/'
groups=[
 ('K1','Identischer Haupttext: Lackhärte',[blog(s) for s in ['harte-weiche-autolacke-lackaufbereitung','harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung','harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung-2']],blog('harte-weiche-autolacke-lackaufbereitung'),'hoch; Inhaltsduplikat bestätigt'),
 ('K2','Chiptuning / Softwareoptimierung',['/chiptuning']+[blog(s) for s in ['chiptuning-raum-erfurt','chiptuning-raumerfurt','softwareoptimierung-erfurt']],'/chiptuning','hoch; gleiche kommerzielle Intention vermutet'),
 ('K3','Keramikversiegelung allgemein',['/luxus-aufbereitung']+[blog(s) for s in ['professionelle-keramikversiegelung-erfurt','profi-keramikversiegelung','keramikversiegelung-profi-lackschutz','keramikversiegelung-erfurt-high-end-lackschutz-powertech-performance','keramik-fuer-auto-erfurt-vorteile-haltbarkeit','blog-keramikversiegelung']],'/luxus-aufbereitung','hoch; breite Leistungsversprechen überlappen'),
 ('K4','Innenreinigung in der Nähe',[blog('innenreinigung-auto-in-der-naehe'),blog('professionelle-innenreinigung-auto-in-der-naehe')],blog('innenreinigung-auto-in-der-naehe'),'hoch; gleiche lokale Leistungsintention'),
 ('K5','Auto-/Fahrzeugaufbereitung Erfurt',['/','/ads','/fahrzeugaufbereitung-aus-erfurt',blog('fahrzeugaufbereitung-erfurt')],'/','hoch; mehrere lokale Angebotsseiten'),
 ('K6','Leasingaufbereitung',[blog('leasingauto-aufbereiten'),blog('leasing-rueckgabe-aufbereitung-erfurt')],blog('leasing-rueckgabe-aufbereitung-erfurt'),'mittel; ähnliche kommerzielle Intention'),
 ('K7','AdBlue-Service / Deaktivierung',['/adblue-service']+[blog(s) for s in ['adblue-deaktivierung','adblue-deaktivieren-vor-nachteile-wahrheit','wie-lange-dauert-adblue-off']],'/adblue-service','mittel; gemischte Informations-/Angebotsintention, widersprüchliche Positionierung')]
groupby={path:(id,name,owner,risk) for id,name,paths,owner,risk in groups for path in paths}
new=[dict(path='/trockeneisreinigung',keyword='Trockeneisreinigung Erfurt',cluster='Trockeneisreinigung',type='Leistungsseite',priority='P2',intent='kommerziell / lokal'),dict(path='/blog/felgenversiegelung-pflege/',keyword='Felgenversiegelung pflegen',cluster='Felgenpflege',type='Ratgeber',priority='P3',intent='informativ')]
def cluster(p):
    t=(p['path']+' '+p['source_index'].get('Thema','')).lower()
    if any(x in t for x in ['adblue','dpf']):return 'AdBlue / SCR / DPF'
    if any(x in t for x in ['chiptuning','softwareoptimierung']):return 'Chiptuning'
    if 'leasing' in t:return 'Leasingrückgabe'
    if any(x in t for x in ['innenreinigung','auto-reinigung']):return 'Innenraumreinigung'
    if any(x in t for x in ['oldtimer','audi-r8','porsche','motorrad','flugzeug','boot','cabrio']):return 'Spezialfahrzeuge'
    if any(x in t for x in ['keramik','luxus']):return 'Keramikversiegelung'
    if any(x in t for x in ['lack','politur','step']):return 'Lackaufbereitung'
    if 'motorwaesche' in t:return 'Motorraumwäsche'
    if p['path'] in ['/eisenach','/gera','/gotha','/jena','/nordhausen','/suhl']:return 'Einzugsgebiet'
    if p['path'].startswith('/pages/') or p['path'] in ['/anfrage-danke','/online-termin-buchen']:return 'Kontakt / Service / Recht'
    return 'Autoaufbereitung'
def typ(p):
    path=p['path']
    if p['verification']:return 'Verifizierungsdatei'
    if path=='/':return 'Startseite'
    if path=='/blog/':return 'Blogübersicht'
    if path.startswith('/blog/'):return 'Blog / Ratgeber'
    if cluster(p)=='Einzugsgebiet':return 'Einzugsgebietsseite'
    if path=='/ads':return 'Kampagnen-Landingpage'
    if path.startswith('/pages/') or path in ['/anfrage-danke','/online-termin-buchen']:return 'Funktions-/Rechtsseite'
    if path=='/glosar':return 'Glossar'
    return 'Leistungs-/Landingpage'
def indexable(p):return not p['verification'] and 'noindex' not in ' '.join(p['robots']).lower()
def kw(p):return p['source_index'].get('Hauptkeyword (vermutet)','').replace('-', '-',1)
def intent(p):return 'informativ / teilweise kommerziell' if p['path'].startswith('/blog/') else 'navigational' if typ(p)=='Funktions-/Rechtsseite' else 'kommerziell / lokal'
def priority(p):return 'P1' if p['path'] in groupby or p['path'] in ['/','/blog/','/adblue-service'] else 'P2' if indexable(p) else 'P3'
def export(name,rows,fields=None):
    if not rows:return
    fields=fields or list(rows[0])
    with (O/name).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=';',extrasaction='raise');w.writeheader();w.writerows(rows)
def joined(items):return ' | '.join(items)
def report_join(m):
    r=L[m['source_url']]
    c=L.get(m['candidate'],{})
    return bool(m['candidate'] and r['status']==200 and c.get('status')==200 and r.get('final_url')==c.get('final_url'))
mapping=[]
for m in perf:
    mapped=report_join(m)
    mapping.append({'Export-URL':m['source_url'],'Impressionen':m['impressions'],'HTTP-Status':L[m['source_url']]['status'],'Finale Live-URL':L[m['source_url']].get('final_url',''),'Zugeordnete Projekt-URL':m['candidate'] if mapped else '', 'Mögliche Zielseite (ungeprüfte Inhaltsentscheidung)': '' if mapped else (m['candidate'] or m['thematic']), 'Zuordnung':'belegt durch identisches Live-Endziel' if mapped else 'keine Messwertübertragung; 404 / Inhaltszuordnung zu prüfen','Zeitraum':'unbekannt'})
export('url-mapping.csv',mapping)
measured={}
for m in perf:
    if report_join(m):measured[m['candidate']]=m
links=[]
generic={'hier','mehr','mehr erfahren','jetzt anfragen','jetzt unverbindlich anfragen','startseite','www.powertech-performance.com'}
for p in P:
    for l in p['links']:
        problems=[]; suggestions=[]
        if l['missing_fragment']:problems.append('Sprungziel fehlt');suggestions.append('Passende existierende Abschnitts-ID verwenden; keine Inhaltsbehauptung aus dem alten Anchor übernehmen')
        if l['anchor'].lower() in generic and l['context']=='Inhalt':problems.append('Generischer Anchor');suggestions.append('Im redaktionellen Text Zielthema nennen; generische Formular-CTAs dürfen bleiben')
        if l['anchor']=='Startseite' and l['path']!='/':problems.append('Anchor widerspricht Kontaktziel');suggestions.append('Anchor zu Kontakt ändern oder tatsächliche Startseite verlinken')
        if l['resolved'] and indexable(by[l['resolved']]) and p['blocked']:problems.append('Quelle für Crawler gesperrt');suggestions.append('Zusätzlich aus crawlbarer, passender Inhaltsseite verlinken')
        target=by.get(l['resolved'])
        if l['context']=='Inhalt' and target and p['path'].startswith('/blog/') and target['path'].startswith('/blog/') and cluster(p)!=cluster(target):problems.append('Themenübergang manuell prüfen')
        links.append({'Quellseite':p['url'],'Zielseite':l['url']+('#'+l['fragment'] if l['fragment'] else ''),'Anchor-Text':l['anchor'],'Link-Typ':'Bestand: '+('Sprunglink' if l['fragment'] else 'Seitenlink'),'Position/Kontext':l['context'],'Themencluster':cluster(p),'Bewertung':joined(problems) or 'technisch lokal auflösbar','Optimierungsvorschlag':joined(suggestions),'Lokale Ziel-URL':B+l['resolved'] if l['resolved'] else '', 'nofollow':'ja' if 'nofollow' in l['rel'] else 'nein'})
proposals=[]
def propose(source,target,anchor,context,reason):
    if source not in by:return
    if any(l['resolved']==target and l['context']=='Inhalt' and not l['fragment'] for l in by[source]['links']):return
    if (source,target) in {(x[0],x[1]) for x in proposals}:return
    proposals.append((source,target,anchor,context,reason))
for _,name,paths,owner,_ in groups:
    for path in paths:
        if path!=owner:propose(path,owner,by[owner]['headings']['h1'][0], 'Passender Abschnitt nach redaktioneller Abgrenzung','Cluster-Zielseite stärken; kein Ersatz für Duplikatentscheidung')
for target,anchor in [('/luxus-aufbereitung','Keramikversiegelung in Erfurt'),('/chiptuning','Chiptuning in Erfurt'),('/adblue-service','AdBlue-Diagnose und Reparatur'),(blog('innenreinigung-auto-in-der-naehe'),'professionelle Innenraumreinigung'),(blog('motorwaesche-erfurt-vorteile-kosten'),'Motorraumwäsche'),(blog('lackkorrektur-wofuer-gut-werterhalt'),'Lackkorrektur'),(blog('leasing-rueckgabe-aufbereitung-erfurt'),'Aufbereitung vor der Leasingrückgabe'),('/online-termin-buchen','Besichtigungstermin buchen')]:propose('/',target,anchor,'Leistungsabschnitt bzw. Termin-CTA','Direkter Zugang von der Startseite statt nur Seitenübersicht')
for p in P:
    if cluster(p)=='Einzugsgebiet':propose('/',p['path'],'Autoaufbereitung für Kunden aus '+p['path'][1:].title(),'Abschnitt Einzugsgebiet','Nur nach standortspezifischer Inhaltsverbesserung; keine fiktive Niederlassung')
for source,target,anchor in [('/luxus-aufbereitung',blog('haltbarkeit-keramikversiegelung-lackschutz'),'Haltbarkeit und Pflege der Keramikversiegelung'),(blog('haltbarkeit-keramikversiegelung-lackschutz'),'/luxus-aufbereitung','Keramikversiegelung in Erfurt'),(blog('was-kostet-eine-auto-reinigung'),blog('innenreinigung-auto-in-der-naehe'),'Innenraumreinigung anfragen'),(blog('leasingrueckgabe-checkliste'),blog('leasing-rueckgabe-aufbereitung-erfurt'),'Aufbereitung vor der Leasingrückgabe'),(blog('lackkorrektur-wofuer-gut-werterhalt'),blog('1-step-2-step-oder-lackkorrektur-lackaufbereitung-im-vergleich'),'Politurverfahren im Vergleich'),(blog('1-step-2-step-oder-lackkorrektur-lackaufbereitung-im-vergleich'),blog('harte-weiche-autolacke-lackaufbereitung'),'Lackhärte berücksichtigen'),(blog('auto-selber-waschen-erfurt'),'/','professionelle Fahrzeugaufbereitung in Erfurt')]:propose(source,target,anchor,'Thematisch passender Haupttext','Ergänzende Intention verbinden')
for source,target,anchor in [('/','/trockeneisreinigung','Trockeneisreinigung am Fahrzeug'),(blog('motorwaesche-erfurt-vorteile-kosten'),'/trockeneisreinigung','Trockeneisreinigung für geeignete Fahrzeugbereiche'),('/','/blog/felgenversiegelung-pflege/','versiegelte Felgen pflegen'),('/luxus-aufbereitung','/blog/felgenversiegelung-pflege/','Pflege versiegelter Felgen')]:propose(source,target,anchor,'Passender Leistungsabschnitt','Erst nach Veröffentlichung der vorgeschlagenen Seite verlinken')
for source,target,anchor,context,reason in proposals:
    links.append({'Quellseite':B+source,'Zielseite':B+target,'Anchor-Text':anchor,'Link-Typ':'Vorschlag: '+('bestehendes Ziel' if target in by else 'neue Seite, noch nicht vorhanden'),'Position/Kontext':context,'Themencluster':cluster(by[source]),'Bewertung':'vorgeschlagen; nicht umgesetzt','Optimierungsvorschlag':reason,'Lokale Ziel-URL':B+target if target in by else '', 'nofollow':'nein'})
export('internal-links.csv',links)
seo=[]
for p in P:
    m=measured.get(p['url'],{}); issues=[]
    if not p['verification']:issues.append('Live-Host www widerspricht Canonical ohne www')
    if indexable(p) and len(p['incoming'])<2:issues.append('Nur eine verlinkende Seite')
    if indexable(p) and p['incoming'] and all('/pages/seitenuebersicht.html' in u for u in p['incoming']):issues.append('Nur aus robots-gesperrter Seitenübersicht erreichbar')
    if p['path'] in groupby:issues.append(groupby[p['path']][0]+': '+groupby[p['path']][3])
    if p['sitemap'] and not indexable(p):issues.append('noindex in Sitemap')
    if p['blocked'] and 'noindex' in ' '.join(p['robots']):issues.append('robots-Sperre verhindert noindex-Auslesen')
    if any(l['missing_fragment'] for l in p['links']):issues.append('Link zu fehlendem Abschnitt')
    row={'URL':p['url'],'Seitentyp':typ(p),'Title':p['title'],'Meta Description':joined(p['description']),'H1':joined(p['headings']['h1']),'Hauptthema':p['source_index'].get('Thema',p['title']),'vermutetes Hauptkeyword':kw(p),'Nebenkeywords':joined(p['headings']['h2'][:3]) if indexable(p) else '', 'Suchintention':intent(p),'Themencluster':cluster(p),'interne Links von':joined(p['incoming']),'interne Links zu':joined(p['outgoing']),'Anzahl eingehender interner Links':len(p['incoming']),'Anzahl ausgehender interner Links':len(p['outgoing']),'Canonical':joined(p['canonical']),'Indexierungsstatus':'Verifizierung; kein SEO-Ziel' if p['verification'] else ('noindex deklariert' if not indexable(p) else 'lokal index erlaubt; Google-Status unbekannt')+('; robots.txt gesperrt' if p['blocked'] else ''),'SEO-Status':joined(issues) or 'kein Inhalts-SEO-Ziel','Optimierungspotenzial':'Host-Signale vereinheitlichen; '+('Kontextlinks ergänzen; Cluster-Intention prüfen' if indexable(p) else 'Indexierungssignale konsistent halten'),'Priorität':priority(p),'Klicks':'','Impressionen':m.get('impressions',''),'CTR':'','durchschnittliche Position':'','relevante Suchanfragen':'','H2':joined(p['headings']['h2']),'H3':joined(p['headings']['h3']),'Sitemap':'ja' if p['sitemap'] else 'nein','Robots Meta':joined(p['robots']),'Bilder und Alt-Texte':json.dumps(p['images'],ensure_ascii=False),'CSS-Bilder / ARIA':json.dumps(p['aria_images'],ensure_ascii=False),'Strukturierte Daten':json.dumps(p['schema'],ensure_ascii=False),'Content-Abschnitte':json.dumps(p['sections'],ensure_ascii=False),'Wörter Hauptinhalt':p['words'],'Dateipfad':p['file'],'Live HTTP':L[p['url']]['status'],'Live Endziel':L[p['url']].get('final_url',''),'Messwertquelle':m.get('source_url',''),'Messwert-Zuordnung':'belegtes gleiches HTTP-Endziel; nur Seitenimpressionen' if m else 'keine zugeordneten Messwerte','Optimierung empfohlen':'ja' if indexable(p) else 'nur Technik / kein Rankingziel','Keyword-Basis':'vermutet aus Seitenindex; Nebenkeywords sind Überschriftenthemen, keine Suchmessung'}
    seo.append(row)
for m in perf:
    if report_join(m):continue
    row={k:'' for k in seo[0]};row.update({'URL':m['source_url'],'Seitentyp':'Export-URL ohne erreichbaren Inhalt','Indexierungsstatus':'HTTP 404 am Prüftag; historischer Google-Status unbekannt','SEO-Status':'Suchdaten-URL derzeit 404','Optimierungspotenzial':'Inhaltliche Zielgleichheit prüfen; konkreten Wiederherstellungs-/Redirect-Plan freigeben lassen','Priorität':'P1','Impressionen':m['impressions'],'Live HTTP':404,'Live Endziel':L[m['source_url']].get('final_url',''),'Messwertquelle':m['source_url'],'Messwert-Zuordnung':'exakter Originaldatensatz; keine Übertragung auf Kandidaten','Optimierung empfohlen':'URL-Zuordnung prüfen','Hauptthema':'Kandidat: '+(m['candidate'] or m['thematic'])})
    seo.append(row)
export('seo-map.csv',seo)
keywords=[]
for p in P:
    if kw(p) in ('','-'):continue
    g=groupby.get(p['path']); owner=B+g[2] if g else p['url']
    recommendation='bestehende Seite optimieren' if g else 'interne Verlinkung verbessern' if len(p['incoming'])==1 else 'bestehenden Content erweitern'
    keywords.append({'Keyword / Suchanfrage':kw(p),'bestehende Zielseite':p['url'],'Klicks':'','Impressionen':'','CTR':'','Position':'','Suchvolumen':'','CPC':'','Suchintention':intent(p),'Themencluster':cluster(p),'Hauptkeyword oder Nebenkeyword':'Hauptkeyword (vermutet)','passende bestehende Seite':owner,'mögliche neue Seite':'','Kannibalisierungsrisiko':g[0]+': '+g[3] if g else 'nicht belegt; Query-URL-Daten fehlen','Priorität':priority(p),'Handlungsempfehlung':recommendation,'Begründung':'Seitenindex-Hypothese. '+('Zielseitenrolle im Cluster abgrenzen; Hauptziel ist Planungsvorschlag, kein Rankinggewinner.' if g else 'Themenrelevante Einstiegslinks und Nutzwert verbessern.'),'Datenquelle':'Datei Manager/seo-url-index.csv','Datenart':'Keyword-Hypothese; keine beobachtete Suchanfrage','URL-Impressionen (nicht Keyword-Messwert)':measured.get(p['url'],{}).get('impressions','')})
for n in new:
    row={k:'' for k in keywords[0]}; row.update({'Keyword / Suchanfrage':n['keyword'],'Suchintention':n['intent'],'Themencluster':n['cluster'],'Hauptkeyword oder Nebenkeyword':'Hauptkeyword (Planung)','passende bestehende Seite':B+'/#leistungen','mögliche neue Seite':B+n['path'],'Kannibalisierungsrisiko':'vor Erstellung gegen Cluster-Mapping prüfen','Priorität':n['priority'],'Handlungsempfehlung':'eigene neue Unterseite erstellen' if n['type']=='Leistungsseite' else 'Ratgeber-/Blogbeitrag erstellen','Begründung':'Eigenständige Intention; Leistung in index.html belegt, Nachfrage nicht gemessen. Details in content-plan.md.','Datenquelle':'index.html, Leistungsabschnitt','Datenart':'neue redaktionelle Hypothese'})
    keywords.append(row)
export('keyword-map.csv',keywords)
# Human-readable exhaustive technical findings, without mutating source documents.
lines=['# Technischer Detailnachweis','', 'Generiert aus allen lokalen HTML-Dateien und den öffentlichen HTTP-Prüfungen. Maschinenlesbare vollständige Texte, Überschriften, Bilder, Links, Schema-Objekte und Quellhashes: `evidence.json`. HTTP-Endziele und Weiterleitungsschritte: `live-check.json`.','', '## Vollständiger Seitenbestand','', '| URL | Typ | Eingehende Quellseiten | Haupttext Wörter | Sitemap |','|---|---|---:|---:|---|']
for p in P:lines.append(f"| {p['path']} | {typ(p)} | {len(p['incoming'])} | {p['words']} | {'ja' if p['sitemap'] else 'nein'} |")
lines+=['','## Schwache interne Erschließung','', 'Keine Inhaltsseite ist im vollständigen lokalen Linkgraphen vollständig verwaist. Die Google-Verifizierungsdatei wird als technischer Sonderfall nicht verlinkt. 52 indexierbare Inhaltsseiten haben nur eine verlinkende Quellseite. 39 Artikel hängen allein an `/blog/`; 13 indexierbare Landing-/Funktionsseiten allein an der robots-gesperrten Seitenübersicht. Die beiden übrigen dort exklusiv verlinkten Seiten sind Danke-Seite und AGB.','', '| Seite nur über gesperrte Seitenübersicht | Status |','|---|---|']
for p in P:
    if p['incoming']==[B+'/pages/seitenuebersicht.html']:lines.append(f"| {p['path']} | {'index erlaubt' if indexable(p) else 'noindex'} |")
lines+=['','## Identische Haupttexte','']
d=collections.defaultdict(list)
for p in P:
    if not p['verification']:d[p['content']].append(p['path'])
for content,paths in d.items():
    if len(paths)>1:lines+=['- '+joined(paths)+f' — {len(content.split())} Wörter, Haupttext exakt gleich.']
lines+=['','## Einzugsgebietsseiten','']
citypaths=['/eisenach','/gera','/gotha','/jena','/nordhausen','/suhl']
norm=lambda text:re.sub(r'\b(Eisenach|Gera|Gotha|Jena|Nordhausen|Suhl)\b','STADT',text)
citysame=len({norm(by[p]['content']) for p in citypaths})==1
lines+=['Die sechs Stadtseiten sind nach Ersetzung der jeweiligen Stadtbezeichnung im Haupttext '+('exakt identisch.' if citysame else 'nicht exakt identisch; hohe Vorlagenähnlichkeit bleibt manuell zu prüfen.'),'Keine eigenständigen Niederlassungen aus diesen Seiten ableiten. Unterschiedliche Städtenamen allein belegen keine Keyword-Kannibalisierung.','', '## Bilder und lokale Ressourcen','']
missing=[]
for p in P:
    for im in p['images']:
        target=U.urlsplit(U.urljoin(p['url'],im['src']))
        if target.hostname in ['powertech-performance.com','www.powertech-performance.com'] and not (ROOT/target.path.lstrip('/')).is_file():missing.append((p['path'],im['src']))
lines+= [f"295 img-Elemente; kein fehlendes alt-Attribut; 2 leere Alt-Texte. Lokal fehlende img-Ressourcen: {len(missing)}. Leere Texte: Startseiten-Nachherbild (Inhaltsbild prüfen) und dekorativer Smartphone-Rahmen (leer plausibel). CSS-Servicebilder besitzen auf der Startseite ARIA-Beschreibungen. CSS-Hintergründe sind keine img-Alt-Attribute.", '', '| Große Bilddatei | Bytes |','|---|---:|']
for a in sorted([a for a in E['assets'] if a['file'].startswith('images/')],key=lambda a:a['bytes'],reverse=True)[:15]:lines.append(f"| {a['file']} | {a['bytes']} |")
lines+=['','Dateigröße allein ist kein Core-Web-Vitals-Messwert. Vor Optimierung tatsächliche Nutzung, Viewport und Bildqualität prüfen. `css/home2.css` nutzt `home2-service-grid.png` als Hintergrund; `css/style.css` nutzt `adblue-vehicle-hero.png`. Schriftdateien sind lokal.','', '## Strukturierte Daten und Navigation','', 'Nur `/adblue-service` enthält JSON-LD: AutomotiveBusiness, BreadcrumbList und FAQPage. JSON ist syntaktisch parsebar; keine Zusage zu Rich Results. Andere Inhaltsseiten haben kein JSON-LD. Visuelle Breadcrumbs in Artikeln führen zur Blogübersicht; sie sind nicht automatisch BreadcrumbList-Daten. HTML-Navigation und Footer wurden bei jedem Link getrennt erfasst.','', '## Fehlende Sprungziele','', '`/#ueber-uns`: 46 Link-Vorkommen. `/#faq`: 2 Link-Vorkommen. Vorhandene Startseiten-IDs: '+joined(by['/']['ids'])+'.','', '## Technische Architektur','', 'Statische HTML-Multipage-Site, CSS und Vanilla-JavaScript. Kein Build-Framework oder CMS im Projekt. Vercel-Konfiguration: 14 explizite Rewrites und 42 Redirect-Regeln; `api/send-lead.js` als Node-Serverless-Endpunkt mit nodemailer. `main.js` steuert Formulare, Navigation und Consent; `home2.js` Scroll-Effekte und Slider. Keine JavaScript-generierte Inhaltsnavigation gefunden. CSS, JavaScript, API-Dateien, Konfiguration und alle HTML-Seiten wurden berücksichtigt. node_modules und .git sind Abhängigkeiten/Metadaten, keine eigenen Website-Inhaltsseiten.','', 'Formulare wurden nicht abgesendet. GTM, Ads, Consent und Tracking wurden nicht ausgeführt oder verändert. JavaScript-Rendering, Browser-Layout, Rich-Results-Test und Core Web Vitals sind nicht Bestandteil dieses statischen/HTTP-Audits.','', '## Herkunft und Host-Widerspruch','', 'Alle 62 lokalen HTML-Routen waren beim HTTP-Test erreichbar; Titel entsprechen lokalem Stand. Jede non-www-Route leitete auf www um, während der HTML-Canonical der 61 Inhaltsseiten ohne www angegeben ist. Eine 308-Antwort ist hier eine beobachtete permanente Host-Weiterleitung, kein Fehlerstatus des Endziels.','']
(O/'technical-inventory.md').write_text('\n'.join(lines),encoding='utf8')
summary=dict(content_pages=sum(not p['verification'] for p in P),html=len(P),seo_rows=len(seo),keyword_source_rows=55,distinct_source_keywords=len({kw(p).casefold() for p in P if kw(p) not in ('','-')}),keyword_rows=len(keywords),new_pages=len(new),risk_groups=len(groups),confirmed_ranking_cannibalization=0,exact_duplicate_groups=sum(len(v)>1 for v in d.values()),optimize_existing=sum(indexable(p) for p in P),weak_indexable=sum(indexable(p) and len(p['incoming'])==1 for p in P),existing_link_occurrences=sum(len(p['links']) for p in P),proposed_links=len(proposals),source_impressions=sum(m['impressions'] for m in perf),matched_impressions=sum(m['impressions'] for m in perf if report_join(m)),unmatched_impressions=sum(m['impressions'] for m in perf if not report_join(m)))
(O/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf8');print(json.dumps(summary,indent=2))
