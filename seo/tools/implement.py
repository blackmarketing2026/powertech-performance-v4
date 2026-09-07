"""One-time, narrowly scoped implementation of the approved SEO work.
Preserves raw script/form markup. Refuses to rerun after a successful application.
"""
from pathlib import Path
import csv,json,re,html,hashlib,shutil
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[2]; O=R/'seo'; B='https://www.powertech-performance.com'
assert not (O/'implementation.json').exists(), 'Already applied; edit current files, do not replay.'
old=json.loads((O/'evidence.json').read_text('utf8'))
history=O/'history'/'2026-09-07-analysis'; history.mkdir(parents=True,exist_ok=True)
for f in O.iterdir():
    if f.is_file():shutil.copy2(f,history/f.name)
(history/'tools').mkdir(exist_ok=True)
for f in (O/'tools').glob('*.py'):
    if f.name!='implement.py':shutil.copy2(f,history/'tools'/f.name)
original={p['file']:(R/p['file']).read_text('utf8') for p in old['pages']}
site=dict(original); records={}; metadata={}
def sha(x):return hashlib.sha256(x.encode('utf8')).hexdigest()
def protected(raw):
    soup=BeautifulSoup(raw,'html.parser')
    return {'scripts':[sha(m.group()) for m in re.finditer(r'<script\b(?![^>]*application/ld\+json)[^>]*>.*?</script>',raw,re.S|re.I)],'forms':[sha(m.group()) for m in re.finditer(r'<form\b[^>]*>.*?</form>',raw,re.S|re.I)],'noscript':[sha(m.group()) for m in re.finditer(r'<noscript\b[^>]*>.*?</noscript>',raw,re.S|re.I)],'contacts':sorted(x['href'] for x in soup.select('a[href]') if x['href'].startswith(('tel:','mailto:','https://wa.me/'))),'buttons':sorted((x.get('id',''),x.get('type',''),x.get_text(' ',strip=True)) for x in soup.find_all('button'))}
baseline={'pages':{f:protected(raw) for f,raw in original.items()},'files':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['js/main.js','js/home2.js','api/send-lead.js','api/_lib/lead-email.js','package.json','package-lock.json','css/style.css','css/home2.css']},'source_hashes':{s['name']:s['sha256'] for s in old['sources']}}
(O/'protection-baseline.json').write_text(json.dumps(baseline,ensure_ascii=False,indent=2),encoding='utf8')
paths={p['path']:p['file'] for p in old['pages']}
def note(f,what):records.setdefault(f,[]).append(what) if what not in records.get(f,[]) else None
def span(raw,node):
    start=sum(len(l) for l in raw.splitlines(keepends=True)[:node.sourceline-1])+node.sourcepos
    first=re.match(r'<[^>]+>',raw[start:]); assert first
    if node.name in ['meta','link','img','input','br','hr']:return start,start+first.end()
    depth=0
    for m in re.finditer(r'</?'+re.escape(node.name)+r'\b[^>]*>',raw[start:],re.I):
        depth+=-1 if m.group().startswith('</') else 1
        if depth==0:return start,start+m.end()
    raise ValueError((node.name,start))
def replace(f,selector,new,inner=False):
    raw=site[f]; n=BeautifulSoup(raw,'html.parser').select_one(selector);assert n is not None,(f,selector)
    a,b=span(raw,n)
    if inner:
        a=raw.index('>',a)+1;b=raw.rfind('</',a,b)
    site[f]=raw[:a]+new+raw[b:]
def append(f,selector,new):
    raw=site[f];n=BeautifulSoup(raw,'html.parser').select_one(selector);assert n is not None,(f,selector)
    a,b=span(raw,n);end=raw.rfind('</',a,b)
    site[f]=raw[:end]+new+'\n'+raw[end:]
def meta(path,title,desc,h1=None,keyword=None,intent='informativ',cluster=None):
    f=paths[path];replace(f,'title',html.escape(title)+' | Powertech Performance',True)
    replace(f,'meta[name=description]','<meta name="description" content="'+html.escape(desc,quote=True)+'">')
    if h1:replace(f,'h1',html.escape(h1),True)
    metadata[path]={'keyword':keyword or title,'intent':intent,'cluster':cluster,'title':title,'description':desc}
    note(f,'Title, Description und Themenausrichtung gezielt optimiert'+('; H1 präzisiert' if h1 else ''))
def body(path,text):
    f=paths[path];replace(f,'.article-body','\n'+text.strip()+'\n',True);note(f,'Artikelinhalt auf eigenständige, sachliche Nutzerfrage ausgerichtet')
def extra(path,text):
    f=paths[path];append(f,'.article-body','\n'+text.strip()+'\n');note(f,'Konkrete Information und thematische Inhaltslinks ergänzt')
def section(path,title,text):
    f=paths[path];append(f,'main','\n<section class="section"><div class="container"><h2>'+html.escape(title)+'</h2>'+text+'</div></section>\n');note(f,'Ergänzenden Beratungs-/Clusterabschnitt eingefügt')
def a(path,label):return '<a href="'+path+'">'+html.escape(label)+'</a>'
def blog(slug):return '/blog/'+slug+'/'
law='https://www.gesetze-im-internet.de/stvzo_2012/__19.html'
adac='https://www.adac.de/rund-ums-fahrzeug/ausstattung-technik-zubehoer/zubehoer/chip-tuning-und-eco-tuning/'

# All host changes are confined to URL attributes / structured data, never runtime scripts.
for f,raw in list(site.items()):
    if f.startswith('google'):continue
    raw=re.sub(r'((?:href|content)=["\'])https://powertech-performance\.com',r'\1https://www.powertech-performance.com',raw)
    raw=re.sub(r'<script\b[^>]*type="application/ld\+json"[^>]*>.*?</script>',lambda m:m.group().replace('https://powertech-performance.com','https://www.powertech-performance.com'),raw,flags=re.S)
    raw=raw.replace('href="/#ueber-uns"','href="/#standort"')
    raw=re.sub(r'(href="/#standort"[^>]*>)Über uns(</a>)',r'\1Standort &amp; Kontakt\2',raw)
    raw=raw.replace('href="/#faq"','href="/glosar"')
    raw=re.sub(r'(href="/glosar"[^>]*>)(?:FAQ|Häufige Fragen)(</a>)',r'\1Fragen zur Aufbereitung\2',raw)
    raw=re.sub(r'<h([23])[^>]*>\s*</h\1>','',raw)
    site[f]=raw;note(f,'Canonical-/Metadaten-Host an das bestehende www-Live-Endziel angepasst')
    if 'href="/#ueber-uns"' in original[f] or 'href="/#faq"' in original[f]:note(f,'Defekte Startseiten-Sprunglinks auf vorhandene Ziele korrigiert')

# Startseite: keep design, forms, imagery and controls; make existing tiles useful entrances.
meta('/','Autoaufbereitung Erfurt – Pflege & Werterhalt','Autoaufbereitung in Erfurt: Lackkorrektur, Keramikversiegelung, Innenraum- und Trockeneisreinigung. Fahrzeug und Wunschleistung anfragen.','Autoaufbereitung in Erfurt mit Tiefenglanz.','Autoaufbereitung Erfurt','kommerziell / lokal','Autoaufbereitung')
f='index.html'
tiles=[('Lackkorrektur',blog('lackkorrektur-wofuer-gut-werterhalt')),('Keramikversiegelung','/luxus-aufbereitung'),('Innenraumreinigung',blog('innenreinigung-auto-in-der-naehe')),('Lederpflege & Pinselarbeit',blog('innenreinigung-auto-in-der-naehe')),('Cockpit & Leasing',blog('leasing-rueckgabe-aufbereitung-erfurt')),('Trockeneisreinigung','/trockeneisreinigung'),('Motorraumwäsche',blog('motorwaesche-erfurt-vorteile-kosten')),('Mehrstufiges Finish',blog('1-step-2-step-oder-lackkorrektur-lackaufbereitung-im-vergleich'))]
for label,target in tiles:
    nodes=BeautifulSoup(site[f],'html.parser').select('.service-tile h3');n=next(x for x in nodes if x.get_text()==label);start,end=span(site[f],n)
    site[f]=site[f][:start]+'<h3>'+a(target,label)+'</h3>'+site[f][end:]
append(f,'#leistungen .intro-head' if BeautifulSoup(site[f],'html.parser').select_one('#leistungen .intro-head') else '#leistungen .section-heading','') if False else None
append(f,'#leistungen','<div class="home2-shell"><p>Auch bei Fragen zur Fahrzeugtechnik beraten wir Sie: '+a('/chiptuning','Chiptuning und Softwareoptimierung')+' sowie '+a('/adblue-service','AdBlue-Diagnose und Reparatur')+'. Fachbegriffe erläutert unser '+a('/glosar','Glossar zur Fahrzeugaufbereitung')+'.</p></div>')
replace(f,'.compare-copy h2','Lackzustand und Finish im Vergleich',True)
replace(f,'.compare-copy p:not(.kicker)','<p>Die KI-generierten Beispielbilder veranschaulichen den Unterschied zwischen matter und glänzender Lackoberfläche. Sie zeigen kein dokumentiertes Kundenergebnis. Welches Finish an Ihrem Fahrzeug möglich ist, klären wir anhand seines tatsächlichen Zustands.</p>')
site[f]=site[f].replace('optimal f&uuml;r schnelle mobile Vergleichsmomente','beispielhafte Darstellung, kein Ergebnisversprechen')
site[f]=site[f].replace('src="/images/home2-slider-after.png" alt=""','src="/images/home2-slider-after.png" alt="KI-generierte Illustration einer glänzenden Lackoberfläche"')
append(f,'#kontakt .contact-intro' if BeautifulSoup(site[f],'html.parser').select_one('#kontakt .contact-intro') else '#ablauf','<div class="home2-shell"><p>Sie möchten den Fahrzeugzustand gemeinsam besprechen? '+a('/online-termin-buchen','Besichtigungstermin in Erfurt anfragen')+'. Informationen zur Vorbereitung finden Sie unter '+a('/fahrzeugaufbereitung-aus-erfurt','Fahrzeugaufbereitung vor Ort')+'.</p></div>')
note(f,'Leistungsraster intern verlinkt; KI-Bildvergleich klar gekennzeichnet; Termin-/Glossarzugänge ergänzt')

# Primary commercial pages.
meta('/adblue-service','AdBlue-Service Erfurt – Diagnose & Reparatur','AdBlue-Warnmeldung oder Start-Countdown? Powertech Performance in Erfurt prüft Diagnose, Reparatur und Rückrüstung. Fahrzeugdaten zur Beratung senden.','AdBlue-Service in Erfurt: Fehler klären lassen','AdBlue Service Erfurt','kommerziell / lokal','AdBlue / SCR / DPF')
meta('/chiptuning','Chiptuning Erfurt – Fahrzeugbezogene Beratung','Chiptuning und Softwareoptimierung in Erfurt: Möglichkeiten, Fahrzeugzustand und Voraussetzungen besprechen. Modell und Motorisierung zur Beratung senden.','Chiptuning und Softwareoptimierung in Erfurt','Chiptuning Erfurt','kommerziell / lokal','Chiptuning')
sf=paths['/chiptuning']
site[sf]=site[sf].replace('AdBlue- und AGR','AdBlue- und SCR-Service').replace('Oildruck','Öldruck')
site[sf]=site[sf].replace('Probleme mit AdBlue oder der Abgasrückführung? Wir bieten Lösungen zur Deaktivierung dieser Systeme – für weniger Wartungsaufwand und mehr Fahrkomfort.','Bei AdBlue-Warnmeldungen steht die Klärung der Fehlerursache im Vordergrund. Informieren Sie sich über unseren <a href="/adblue-service">AdBlue-Service mit Diagnose und Reparaturprüfung</a>.')
site[sf]=site[sf].replace('Verlieren Sie keinen Tropfen zu viel: Unsere Lösung optimiert den Öldruck – für mehr Leistung, weniger Verschleiß und ein längeres Motorleben.','Fragen zu Öldruck und Softwarestand müssen anhand des konkreten Fahrzeugs eingeordnet werden. Teilen Sie uns Modell, Motorisierung und das beobachtete Problem mit.')
soup=BeautifulSoup(site[sf],'html.parser')
faq_answers={
'Warum ist Chiptuning überhaupt sinnvoll?':'Eine Softwareanpassung kann das Ansprechverhalten und die Leistungsentfaltung verändern. Ob sie zum Fahrzeug und zum Nutzungsziel passt, muss im Einzelfall geklärt werden. Mehrleistung und Verbrauchsvorteile lassen sich nicht pauschal zusagen.',
'Ist das Tuning sicher für meinen Motor?':'Zusätzliche Leistung kann Motor und Antriebsstrang stärker belasten. Fahrzeugzustand, vorhandene Änderungen und die erforderlichen Nachweise gehören deshalb in die Beratung. Eine risikofreie Leistungssteigerung oder unveränderte Herstellergarantie lässt sich nicht pauschal versprechen.',
'Wie lange dauert das Chiptuning?':'Der Zeitbedarf hängt von Fahrzeug, Steuergerät und vereinbartem Umfang ab. Senden Sie uns die Fahrzeugdaten; den möglichen Ablauf und Zeitrahmen klären wir vor dem Termin.',
'Wie viel PS und Drehmoment bekomme ich mehr?':'Ohne genaue Fahrzeugdaten und Prüfung gibt es keine belastbare Angabe. Hersteller, Modell, Baujahr, Motorisierung und bisherige Umbauten bilden die Grundlage der Beratung.'}
for i,n in enumerate(soup.select('.faq-item')):
    question=n.select_one('summary').get_text(' ',strip=True)
    if question in faq_answers:replace(sf,f'.faq-item:nth-of-type({i+1}) p',html.escape(faq_answers[question]),True)
section('/chiptuning','Vor der Softwareoptimierung klären','<p>Bringen Sie vorhandene Unterlagen zu Umbauten und Genehmigungen in die Beratung ein. Fragen zu Versicherung und Herstellergarantie gehören ebenfalls vor eine Änderung. Der '+a(adac,'ADAC erläutert mögliche Folgen von Chiptuning')+'.</p><p>Zur Vorbereitung: '+a(blog('chiptuning-raumerfurt'),'Fahrzeugdaten für die Chiptuning-Beratung')+' und '+a(blog('chiptuning-raum-erfurt'),'Fragen zu Leistung, Risiken und Nachweisen')+'.</p>')
meta('/luxus-aufbereitung','Keramikversiegelung Erfurt – Lackschutz & Pflege','Keramikversiegelung in Erfurt: Lackzustand, Vorbereitung und Pflege passend zum Fahrzeug abstimmen. Informationen zum Leistungsumfang und persönliche Beratung.','Keramikversiegelung in Erfurt: Schutz für gepflegten Lack','Keramikversiegelung Erfurt','kommerziell / lokal','Keramikversiegelung')
section('/luxus-aufbereitung','Vorbereitung und Pflege gehören zusammen','<p>Eine Versiegelung baut auf dem vorhandenen Lackzustand auf. Besprechen Sie vorab, welche '+a(blog('lackkorrektur-wofuer-gut-werterhalt'),'Lackkorrektur')+' sinnvoll ist und welche Spuren bleiben können. Für die spätere Pflege hilft unser Beitrag zur '+a(blog('haltbarkeit-keramikversiegelung-lackschutz'),'Haltbarkeit einer Keramikversiegelung')+'.</p><p>Welche Leistungen und Garantiebedingungen für Ihr Angebot gelten, klären Sie bitte bei der Beratung. Lassen Sie sich Umfang, Voraussetzungen und Pflegehinweise für Ihr Fahrzeug erläutern.</p>')

# High-impression AdBlue content: replace unsupported sales claims, keep shell/CTAs intact.
meta(blog('adblue-deaktivieren-vor-nachteile-wahrheit'),'AdBlue deaktivieren: Risiken und Alternativen','AdBlue deaktivieren oder die Ursache reparieren? Rechtliche Grenzen, Fehlermeldungen und sinnvolle nächste Schritte bei AdBlue-Problemen verständlich erklärt.','AdBlue deaktivieren: Risiken, Grenzen und Alternativen','AdBlue deaktivieren Risiken','informativ','AdBlue / SCR / DPF')
body(blog('adblue-deaktivieren-vor-nachteile-wahrheit'),f'''
<p>AdBlue-Warnmeldungen, wiederkehrende Fehler oder ein Start-Countdown können verunsichern. Wer nach „AdBlue deaktivieren“ sucht, möchte häufig vor allem ein zuverlässiges Fahrzeug. Entscheidend ist deshalb zuerst, ob lediglich nachgefüllt werden muss oder eine Störung des Systems vorliegt.</p>
<h2>Was bedeutet AdBlue deaktivieren?</h2>
<p>AdBlue gehört zur SCR-Abgasnachbehandlung eines dafür ausgerüsteten Dieselfahrzeugs. Eine Deaktivierung verändert die Funktion dieses Systems. Sie beseitigt nicht automatisch einen Defekt an Sensoren, Leitungen oder anderen Bauteilen. Eine unterdrückte Warnmeldung ist daher nicht mit einer behobenen Fehlerursache gleichzusetzen.</p>
<h2>Welche Risiken und Grenzen sind wichtig?</h2>
<p>Für Fahrzeuge im öffentlichen Straßenverkehr ist eine Deaktivierung keine reguläre Reparaturlösung. Nach <a href="{law}">§ 19 Absatz 2 StVZO</a> kann die Betriebserlaubnis erlöschen, wenn eine Änderung das Abgasverhalten verschlechtert. Ein pauschaler Hinweis auf Export oder Motorsport ersetzt keine Prüfung der konkret zulässigen Verwendung.</p>
<p>Auch Versprechen wie „dauerhaft fehlerfrei“, „ohne Risiko“ oder „garantiert weniger Verbrauch“ helfen bei der Diagnose nicht weiter. Für eine belastbare Entscheidung müssen Fahrzeugzustand, Fehlerbild und vorgesehene Nutzung betrachtet werden.</p>
<h2>Welche Alternativen gibt es bei einer Warnmeldung?</h2>
<p>Bei einer Nachfüllmeldung richtet sich das Vorgehen nach der Betriebsanleitung. Bleibt eine Meldung trotz korrektem Füllstand bestehen, sollte die Ursache geprüft werden. Auf unserer <a href="/adblue-service">Seite zum AdBlue-Service in Erfurt</a> sind Diagnose, Reparaturprüfung und die Prüfung einer Rückrüstung beschrieben.</p>
<h3>Füllstand und Fehlermeldung unterscheiden</h3>
<p>Notieren Sie die genaue Anzeige und eine gegebenenfalls genannte Restreichweite. Angaben zum letzten Nachfüllen und bereits vorgenommenen Arbeiten helfen, den Verlauf einzuordnen. Weitere Hinweise zum Nachfüllen bietet der <a href="https://www.adac.de/verkehr/tanken-kraftstoff-antrieb/benzin-und-diesel/adblue-nachfuellen/">ADAC</a>.</p>
<h3>Vorhandene Veränderungen offen angeben</h3>
<p>Falls die Fahrzeugsoftware bereits verändert wurde, erwähnen Sie dies bei der Anfrage. Serienstand, vorhandene Komponenten und bisherige Eingriffe sind für die Prüfung einer Rückrüstung relevant.</p>
<h2>So bereiten Sie die Beratung vor</h2>
<ul><li>Hersteller, Modell, Baujahr und Motorisierung nennen.</li><li>Die Warnmeldung möglichst wörtlich wiedergeben oder ein Foto bereithalten.</li><li>Beschreiben, seit wann der Fehler auftritt und ob er wiederkehrt.</li><li>Vorliegende Diagnoseberichte und bisherige Arbeiten angeben.</li></ul>
<p>Eine pauschale Dauer lässt sich daraus noch nicht ableiten. Unser Beitrag <a href="/blog/wie-lange-dauert-adblue-off/">AdBlue-Probleme: Ablauf und Zeitbedarf</a> erklärt, welche Informationen für die Terminplanung wichtig sind.</p>
<h2>AdBlue-Probleme in Erfurt besprechen</h2>
<p>Powertech Performance prüft auf Grundlage der Fahrzeugdaten den passenden nächsten Schritt. <a href="/pages/kontakt.html">Senden Sie Ihre Anfrage zur AdBlue-Diagnose</a>. Eine Änderung am Fahrzeug wird nicht allein aufgrund einer allgemeinen Online-Beschreibung festgelegt.</p>
''')
meta(blog('adblue-deaktivierung'),'AdBlue-Deaktivierung rückgängig machen: Prüfbedarf','Bereits veränderte AdBlue-Software? Welche Angaben und Unterlagen bei der Prüfung von Serienstand, vorhandenen Komponenten und einer Rückrüstung helfen.','AdBlue-Deaktivierung: Rückrüstung prüfen lassen','AdBlue Deaktivierung rückgängig machen','informativ','AdBlue / SCR / DPF')
body(blog('adblue-deaktivierung'),'''
<p>Wurde das AdBlue-System eines Fahrzeugs bereits deaktiviert, ist vor einer Rückrüstung mehr zu klären als die sichtbare Fehlermeldung. Wichtig sind der Softwarestand, die noch vorhandenen Komponenten und die Dokumentation der bisherigen Arbeiten.</p>
<h2>Welche Informationen sind für die Prüfung wichtig?</h2>
<p>Nennen Sie Hersteller, Modell, Baujahr und Motorisierung. Beschreiben Sie bekannte Eingriffe an der Software sowie ausgetauschte oder entfernte Teile. Rechnungen, Diagnoseberichte und Informationen zum ursprünglichen Zustand können die Einordnung unterstützen.</p>
<h2>Software und Hardware gemeinsam betrachten</h2>
<p>Die Rückkehr zu einem Serienstand ist nicht automatisch eine vollständige Reparatur. Ob die vorhandenen Komponenten funktionsfähig sind und welche weiteren Schritte nötig werden, muss am konkreten Fahrzeug geprüft werden. Ohne diese Prüfung lässt sich weder die Machbarkeit noch der Aufwand seriös zusagen.</p>
<h2>Welche Nutzung ist vorgesehen?</h2>
<p>Teilen Sie mit, wie das Fahrzeug eingesetzt werden soll. Für ein Straßenfahrzeug müssen die vorgesehenen Arbeiten zu den geltenden Anforderungen passen. Hintergründe zu den Grenzen einer Deaktivierung erläutert der Beitrag <a href="/blog/adblue-deaktivieren-vor-nachteile-wahrheit/">AdBlue deaktivieren: Risiken und Alternativen</a>.</p>
<h2>Rückrüstung in Erfurt anfragen</h2>
<p>Der <a href="/adblue-service">AdBlue-Service von Powertech Performance</a> umfasst die Prüfung von Diagnose, Reparatur und Rückrüstung. <a href="/pages/kontakt.html">Senden Sie die Fahrzeugdaten und vorhandene Unterlagen zur Beratung</a>. Ein Angebot richtet sich nach dem tatsächlich erforderlichen Prüfumfang.</p>
''')
meta(blog('wie-lange-dauert-adblue-off'),'AdBlue-Probleme: Ablauf und Zeitbedarf der Prüfung','Wie lange dauert die Prüfung eines AdBlue-Problems? Welche Fahrzeugdaten, Fehlerangaben und Vorarbeiten für eine verlässliche Terminplanung benötigt werden.','AdBlue-Probleme: Ablauf und Zeitbedarf klären','AdBlue Diagnose Dauer','informativ','AdBlue / SCR / DPF')
body(blog('wie-lange-dauert-adblue-off'),'''
<p>Wer nach der Dauer von „AdBlue Off“ sucht, hat oft eine akute Warnmeldung und braucht einen planbaren nächsten Schritt. Eine feste Zeitangabe für jedes Fahrzeug wäre jedoch irreführend. Fehlerursache, vorhandene Veränderungen und der erforderliche Arbeitsumfang können sich deutlich unterscheiden.</p>
<h2>Was lässt sich vor dem Termin klären?</h2>
<p>Hersteller, Modell, Baujahr und Motorisierung bilden die Grundlage. Ergänzen Sie die genaue Fehlermeldung, eine angezeigte Restreichweite und Informationen zu bisherigen Arbeiten. So lässt sich besprechen, welche Prüfung sinnvoll ist und welche Unterlagen Sie mitbringen sollten.</p>
<h2>Warum Diagnose und Reparatur unterschiedlich lange dauern</h2>
<p>Eine erste Einordnung ist nicht dasselbe wie eine abgeschlossene Reparatur. Ergibt sich weiterer Prüfbedarf oder werden Bauteile benötigt, verändert sich der Zeitrahmen. Eine allgemeine Aussage wie „immer in ein bis zwei Stunden erledigt“ passt deshalb nicht zu jedem Fehlerbild.</p>
<h2>Was gilt bei bereits veränderter Software?</h2>
<p>Bekannte Eingriffe müssen in die Planung einbezogen werden. Lesen Sie dazu, welche Angaben bei der <a href="/blog/adblue-deaktivierung/">Prüfung einer AdBlue-Rückrüstung</a> helfen. Eine Deaktivierung wird auf dieser Seite nicht als pauschale Reparaturlösung für Straßenfahrzeuge angeboten.</p>
<h2>Termin und nächsten Schritt abstimmen</h2>
<p>Beschreiben Sie Ihr Anliegen über die <a href="/pages/kontakt.html">Kontaktseite</a>. Informationen zum angebotenen <a href="/adblue-service">AdBlue-Service in Erfurt</a> helfen bei der Vorbereitung. Den konkreten Zeitbedarf stimmen Sie anhand Ihres Fahrzeugs und des vereinbarten Umfangs ab.</p>
''')

# Useful additions; the existing checklists and instructional content remain.
meta(blog('auto-selber-waschen-erfurt'),'Auto selber waschen in Erfurt: SB-Wäsche & Pflege','Auto selbst waschen in Erfurt: Hinweise zur Wahl einer SB-Waschbox, zur Vorbereitung und zur Abgrenzung von Autowäsche und professioneller Aufbereitung.','Auto selber waschen in Erfurt: SB-Wäsche und Pflege','Auto selber waschen Erfurt','informativ','Autoaufbereitung')
extra(blog('auto-selber-waschen-erfurt'),'''<h2>Vor der Fahrt zur Waschbox prüfen</h2><p>Prüfen Sie beim jeweiligen Betreiber die aktuellen Öffnungszeiten, Zahlungsarten und Regeln zur Nutzung eigener Waschmittel. Die oben verlinkten Standorte dienen der Orientierung; das vorhandene Angebot kann sich ändern. Entscheidend sind die Angaben vor Ort.</p><h2>Wäsche und Lackkorrektur unterscheiden</h2><p>Eine Wäsche entfernt Verschmutzungen. Sichtbare Swirls oder matte Stellen können eine andere Behandlung erfordern. Unser Beitrag zur <a href="/blog/lackkorrektur-wofuer-gut-werterhalt/">Lackkorrektur</a> erklärt die Abgrenzung. Für Pflege über die regelmäßige Wäsche hinaus finden Sie die <a href="/">Autoaufbereitung in Erfurt</a> in unserer Leistungsübersicht.</p><h2>Schonend arbeiten</h2><p>Beachten Sie die Hinweise des Anlagenbetreibers, entfernen Sie groben Schmutz vor der Kontaktwäsche und lassen Sie Reinigungsmittel nicht auf heißen Oberflächen antrocknen. Weitere allgemeine Hinweise finden Sie bei <a href="https://www.kaercher.com/de/de/home-and-garden/know-how/auto-waschen-c887">Kärcher zur Autowäsche</a>.</p>''')
meta(blog('motorwaesche-erfurt-vorteile-kosten'),'Motorraumwäsche Erfurt: Eignung, Ablauf & Aufwand','Motorraumwäsche in Erfurt: Fahrzeugzustand, sensible Komponenten und Reinigungsumfang besprechen. Informationen zur Vorbereitung und individuellen Anfrage.','Motorraumwäsche in Erfurt: Eignung und Ablauf','Motorraumwäsche Erfurt','informativ / kommerziell','Motorraumwäsche')
mf=paths[blog('motorwaesche-erfurt-vorteile-kosten')]
site[mf]=site[mf].replace('Motorwäsche: Warum sie für Ihr Fahrzeug überlebenswichtig ist','Wann eine Motorraumwäsche sinnvoll sein kann').replace('als essenzielle Wartungsmaßnahme','als gezielte Pflege des Motorraums')
site[mf]=site[mf].replace('Nein, solange die Arbeit fachgerecht ausgeführt wird. Im Gegenteil: Viele Werkstätten bevorzugen einen sauberen Motorraum für präzise Wartungsarbeiten.','Garantiebedingungen hängen vom Fahrzeug und vom Hersteller ab. Klären Sie vor einer Behandlung, welche Vorgaben für Ihr Fahrzeug gelten.')
extra(blog('motorwaesche-erfurt-vorteile-kosten'),'<h2>Motorraumwäsche oder Trockeneisreinigung?</h2><p>Eine nasse Reinigung und eine trockene Behandlung sind unterschiedliche Verfahren. Welche Methode für die betroffenen Bereiche passt, richtet sich nach Zustand und Material. Informieren Sie sich über die '+a('/trockeneisreinigung','Trockeneisreinigung am Fahrzeug')+' und beschreiben Sie bei der '+a('/pages/kontakt.html','Anfrage zur Motorraumreinigung')+' den gewünschten Bereich. Eine Reinigung ersetzt keine Reparatur vorhandener Defekte.</p>')
meta(blog('leasingrueckgabe-checkliste'),'Leasingrückgabe-Checkliste: Fahrzeug vorbereiten','Checkliste für die Leasingrückgabe: Unterlagen, Fahrzeugzustand, Zubehör und Übergabeprotokoll vorbereiten. Aufbereitung und Reparaturbedarf unterscheiden.','Leasingrückgabe-Checkliste: Vorbereitung und Übergabe','Leasingrückgabe Checkliste','informativ','Leasingrückgabe')
lf=paths[blog('leasingrueckgabe-checkliste')];site[lf]=site[lf].replace('Mit der richtigen Vorbereitung vermeiden Sie Nachzahlungen und Stress.','Mit guter Vorbereitung behalten Sie Unterlagen, Fahrzeugzustand und offene Fragen im Blick.')
extra(blog('leasingrueckgabe-checkliste'),'<h2>Aufbereitung rechtzeitig einordnen</h2><p>Die Reinigung erleichtert die Sicht auf den tatsächlichen Zustand. Ob Gebrauchsspuren akzeptiert werden, richtet sich nach dem vereinbarten Rückgabemaßstab. Eine Aufbereitung ersetzt weder erforderliche Reparaturen noch die Bewertung durch den Leasinggeber.</p><p>Bei sichtbaren Pflegespuren hilft die '+a(blog('leasing-rueckgabe-aufbereitung-erfurt'),'Beratung zur Aufbereitung vor der Leasingrückgabe')+'. Dokumentieren Sie den Zustand und klären Sie offene Punkte vor der Übergabe. Versprechen, sämtliche Nachzahlungen zu vermeiden, wären ohne Einzelfallprüfung nicht belastbar.</p>')
meta(blog('leasing-rueckgabe-aufbereitung-erfurt'),'Leasingrückgabe-Aufbereitung in Erfurt','Fahrzeug vor der Leasingrückgabe aufbereiten lassen: Lack, Innenraum und Pflegebedarf in Erfurt besprechen. Zustand und Rückgabeanforderungen berücksichtigen.','Aufbereitung vor der Leasingrückgabe in Erfurt','Leasingrückgabe Aufbereitung Erfurt','kommerziell / lokal','Leasingrückgabe')
extra(blog('leasing-rueckgabe-aufbereitung-erfurt'),'<h2>Rückgabe vorbereiten und Grenzen klären</h2><p>Was durch Pflege verbessert werden kann und was eine Reparatur erfordert, sollte vorab unterschieden werden. Die Entscheidung über Nachzahlungen trifft nicht der Aufbereiter. Nutzen Sie unsere '+a(blog('leasingrueckgabe-checkliste'),'Checkliste zur Leasingrückgabe')+' für Unterlagen, Zubehör und Zustandserfassung.</p>')
meta(blog('wie-oft-auto-aufbereiten-lassen') if blog('wie-oft-auto-aufbereiten-lassen') in paths else '/blog/wie-oft-auto-aufbereiten-lassen.html','Wie oft das Auto aufbereiten lassen?','Wie oft ist eine Autoaufbereitung sinnvoll? Nutzung, Lackzustand und Innenraum berücksichtigen und regelmäßige Wäsche von intensiver Pflege unterscheiden.',None,'wie oft Auto aufbereiten lassen','informativ','Autoaufbereitung')
extra('/blog/wie-oft-auto-aufbereiten-lassen.html','<h2>Den Pflegebedarf am Fahrzeug erkennen</h2><p>Ein fester Kalender ersetzt nicht den Blick auf Lack und Innenraum. Prüfen Sie nach der Wäsche, ob Flecken, matte Stellen oder andere Spuren bleiben. Bei einer geplanten Rückgabe oder einem Verkauf kann eine zusätzliche Bestandsaufnahme sinnvoll sein. Die '+a(blog('innenreinigung-auto-in-der-naehe'),'Innenraumreinigung')+' und die '+a(blog('1-step-2-step-oder-lackkorrektur-lackaufbereitung-im-vergleich'),'verschiedenen Stufen der Lackaufbereitung')+' verfolgen unterschiedliche Ziele.</p>')

# Tighten repeated commercial intents, retain useful existing paragraphs.
meta(blog('innenreinigung-auto-in-der-naehe'),'Innenreinigung Auto Erfurt – Umfang & Anfrage','Innenraumreinigung in Erfurt: Sitze, Teppiche und Verkleidungen passend zum Fahrzeugzustand pflegen lassen. Umfang besprechen und individuelles Angebot anfragen.','Professionelle Auto-Innenreinigung in Erfurt','Innenreinigung Auto Erfurt','kommerziell / lokal','Innenraumreinigung')
inf=paths[blog('innenreinigung-auto-in-der-naehe')];site[inf]=re.sub(r'(<a href="/pages/kontakt.html"[^>]*>)Startseite(</a>)',r'\1Kontakt zur Innenraumreinigung\2',site[inf])
extra(blog('innenreinigung-auto-in-der-naehe'),'<h2>Was gehört in die Anfrage?</h2><p>Nennen Sie Fahrzeugmodell, betroffene Flächen und auffällige Flecken oder Gerüche. Beschreiben Sie auch empfindliche Materialien und bisherige Reinigungsversuche. Fotos helfen, das Anliegen einzuordnen; ein konkretes Ergebnis hängt vom Zustand ab. Mehr zu den '+a(blog('was-kostet-eine-auto-reinigung'),'Kostenfaktoren einer Innenreinigung')+' und zur '+a('/pages/kontakt.html','persönlichen Anfrage')+'.</p>')
meta(blog('professionelle-innenreinigung-auto-in-der-naehe'),'Auto-Innenreinigung: Termin richtig vorbereiten','Was vor einer professionellen Auto-Innenreinigung wichtig ist: persönliche Gegenstände, betroffene Materialien und bekannte Flecken für die Beratung vorbereiten.','Auto-Innenreinigung: So bereiten Sie den Termin vor','Auto Innenreinigung vorbereiten','informativ','Innenraumreinigung')
extra(blog('professionelle-innenreinigung-auto-in-der-naehe'),'<h2>Vorbereitung in drei Schritten</h2><ol><li>Persönliche Gegenstände, Dokumente und Wertsachen aus dem Fahrzeug nehmen.</li><li>Betroffene Flächen benennen und bekannte Ursachen von Flecken oder Gerüchen notieren.</li><li>Empfindliche Materialien, nachgerüstete Ausstattung und bisher verwendete Mittel in der Beratung ansprechen.</li></ol><p>Der eigentliche Leistungsumfang wird auf der Seite zur '+a(blog('innenreinigung-auto-in-der-naehe'),'Innenraumreinigung in Erfurt')+' beschrieben.</p>')
meta(blog('chiptuning-raumerfurt'),'Chiptuning-Beratung: Fahrzeugdaten vorbereiten','Chiptuning-Beratung vorbereiten: Modell, Motorisierung, Softwarestand und bisherige Umbauten zusammenstellen. Technische und formale Voraussetzungen klären.','Chiptuning-Beratung: Welche Fahrzeugdaten werden benötigt?','Chiptuning Beratung Fahrzeugdaten','informativ','Chiptuning')
body(blog('chiptuning-raumerfurt'),f'''<p>Eine Anfrage zur Softwareoptimierung wird konkreter, wenn die wichtigsten Fahrzeugdaten bereits vorliegen. Eine pauschale Leistungszahl ohne diese Angaben sagt wenig darüber aus, was für Ihr Fahrzeug sinnvoll ist.</p><h2>Die wichtigsten Angaben zusammenstellen</h2><ul><li>Hersteller, Modell, Baujahr und Motorisierung.</li><li>Getriebevariante und Kilometerstand, soweit bekannt.</li><li>Vorhandene Umbauten und bisherige Softwareänderungen.</li><li>Aktuelle Auffälligkeiten oder Warnmeldungen.</li><li>Das Ziel der Beratung und die vorgesehene Nutzung.</li></ul><h2>Vorhandene Unterlagen bereithalten</h2><p>Informationen zu Reparaturen, Wartung und genehmigten Umbauten können für die Einordnung wichtig sein. Versenden Sie zunächst die nötigen Fahrzeugangaben und keine unnötigen personenbezogenen Dokumente.</p><h2>Welche Fragen gehören ins Gespräch?</h2><p>Fragen Sie nach Voraussetzungen, möglichen Belastungen und erforderlichen Nachweisen. Klären Sie außerdem, wie vorhandene Änderungen berücksichtigt werden. Der <a href="{adac}">ADAC beschreibt die möglichen Folgen einer Leistungssteigerung</a>.</p><h2>Beratung in Erfurt anfragen</h2><p>Das Angebot finden Sie unter <a href="/chiptuning">Chiptuning und Softwareoptimierung in Erfurt</a>. Nutzen Sie die <a href="/pages/kontakt.html">Kontaktseite</a>, um Fahrzeug und Anliegen zu beschreiben. Eine technische Zusage oder ein verbindlicher Zeitrahmen folgt nicht automatisch aus einem allgemeinen Beispiel.</p>''')
meta(blog('chiptuning-raum-erfurt'),'Chiptuning: Leistung, Risiken und Nachweise','Chiptuning einordnen: Leistungswünsche, Fahrzeugzustand, mögliche Risiken und Nachweise vor einer Softwareänderung besprechen. Beratung in Erfurt finden.','Chiptuning: Leistung, Risiken und Nachweise einordnen','Chiptuning Risiken und Voraussetzungen','informativ','Chiptuning')
extra(blog('chiptuning-raum-erfurt'),f'<h2>Leistungsbeispiele ersetzen keine Fahrzeugprüfung</h2><p>Die genannten Beispiele sind keine Zusage für Ihr Fahrzeug. Technischer Zustand, bestehende Änderungen und formale Voraussetzungen müssen zusammen betrachtet werden. Hinweise zu Belastung, Garantie und Versicherung bietet der <a href="{adac}">ADAC zum Chiptuning</a>.</p><p>Das Leistungsangebot finden Sie unter <a href="/chiptuning">Chiptuning in Erfurt</a>; zur Vorbereitung hilft die <a href="/blog/chiptuning-raumerfurt/">Checkliste der Fahrzeugdaten</a>.</p>')
meta(blog('softwareoptimierung-erfurt'),'Softwareoptimierung: Fragen vor einer Änderung','Softwareoptimierung am Fahrzeug: Ziel, vorhandene Änderungen und Wartungszustand besprechen. Fragen für die Beratung und zum weiteren Vorgehen in Erfurt.','Softwareoptimierung: Fragen vor einer Änderung','Softwareoptimierung Fahrzeug Beratung','informativ','Chiptuning')

keramik=[('professionelle-keramikversiegelung-erfurt','Keramikversiegelung: Leistungsumfang verstehen','Keramikversiegelung Leistungsumfang'),('profi-keramikversiegelung','Keramikversiegelung: Vorbereitung und Verarbeitung','Keramikversiegelung Vorbereitung'),('keramikversiegelung-profi-lackschutz','Keramikversiegelung: Profi oder selbst auftragen?','Keramikversiegelung Profi oder selber'),('keramikversiegelung-erfurt-high-end-lackschutz-powertech-performance','Keramikversiegelung: Lackzustand und Glanz','Keramikversiegelung Lackzustand'),('keramik-fuer-auto-erfurt-vorteile-haltbarkeit','Keramik fürs Auto: Nutzen und Pflegebedarf','Keramik Auto Vorteile'),('blog-keramikversiegelung','Keramikversiegelung fürs Auto einfach erklärt','Was ist Keramikversiegelung')]
for slug,title,key in keramik:
    meta(blog(slug),title,title+'. Grundlagen einordnen, Leistungsversprechen prüfen und die passende Beratung zur Keramikversiegelung in Erfurt finden.',title,key,'informativ','Keramikversiegelung')
    extra(blog(slug),'<h2>Vom Ratgeber zur passenden Leistung</h2><p>Welche Vorbereitung für Ihren Lack sinnvoll ist und welcher Umfang vereinbart wird, klären Sie bei der '+a('/luxus-aufbereitung','Beratung zur Keramikversiegelung in Erfurt')+'. Allgemeine Beispiele ersetzen keine Prüfung des konkreten Zustands. Pflege und Nutzung beeinflussen das Ergebnis; lesen Sie dazu den Beitrag zur '+a(blog('haltbarkeit-keramikversiegelung-lackschutz'),'Haltbarkeit der Versiegelung')+'.</p>')

# Verified duplicates: preserve URLs and full content, signal one canonical representative.
primary=blog('harte-weiche-autolacke-lackaufbereitung')
meta(primary,'Harte und weiche Autolacke: Lackhärte verstehen','Harte und weiche Autolacke: Warum der Lackzustand die Auswahl einer Politur beeinflusst und was bei einer professionellen Lackaufbereitung zu beachten ist.','Harte und weiche Autolacke: Was die Lackhärte bedeutet','harte und weiche Autolacke','informativ','Lackaufbereitung')
for slug in ['harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung','harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung-2']:
    path=blog(slug);f=paths[path]
    replace(f,'link[rel=canonical]','<link rel="canonical" href="'+B+primary+'">')
    # Retain each duplicate's body; distinct labels avoid indistinguishable document titles.
    label='Harte und weiche Autolacke – ältere Artikelfassung' if not slug.endswith('-2') else 'Harte und weiche Autolacke – zweite Artikelfassung'
    meta(path,label,'Diese frühere Artikelfassung bleibt erreichbar. Der zentrale Ratgeber erklärt Lackhärte und die Auswahl passender Verfahren für die Lackaufbereitung.',None,'harte und weiche Autolacke','informativ','Lackaufbereitung')
    extra(path,'<p>Die zentrale Fassung dieses Ratgebers finden Sie unter '+a(primary,'Harte und weiche Autolacke: Lackhärte verstehen')+'.</p>')
    note(f,'Identisches Inhaltsduplikat kanonisch der zentralen Fassung zugeordnet; URL bleibt erreichbar')

# No fictitious branch offices: correct existing city claims and link real appointment process.
for city in ['Eisenach','Gera','Gotha','Jena','Nordhausen','Suhl']:
    path='/'+city.lower();f=paths[path]
    meta(path,'Autoaufbereitung für '+city+' – Termin in Erfurt','Sie kommen aus '+city+'? Powertech Performance bietet Fahrzeugaufbereitung in Erfurt. Fahrzeugzustand und Wunschleistung vor Ihrer Anreise abstimmen.','Autoaufbereitung für Kunden aus '+city+' – in Erfurt','Autoaufbereitung '+city,'kommerziell / Einzugsgebiet','Einzugsgebiet')
    replace(f,'.hero-sub','Sie kommen aus '+city+' und möchten Lack oder Innenraum aufbereiten lassen? Unser Standort ist An der Klinge 10 in Erfurt. Beschreiben Sie vor Ihrer Anreise das Fahrzeug und die gewünschte Leistung, damit wir den passenden nächsten Schritt abstimmen können.',True)
    section(path,'Termin am Standort Erfurt vorbereiten','<p>Diese Seite richtet sich an Kunden aus '+city+'; sie beschreibt keine Niederlassung vor Ort. Für die Anfrage helfen Fahrzeugmodell, Zustand und Ihr Ziel: regelmäßige Pflege, Verkauf oder Rückgabe. Einen Hol- oder Bringservice setzen Sie bitte nicht voraus; besprechen Sie Abgabe und Abholung individuell.</p><p>'+a('/online-termin-buchen','Besichtigungstermin anfragen')+' oder '+a('/pages/kontakt.html','Kontakt zu Powertech Performance')+'. Die '+a('/','Leistungsübersicht der Autoaufbereitung in Erfurt')+' hilft bei der Auswahl.</p>')
    # Existing regional chips keep their component styling.
    site['index.html']=site['index.html'].replace('<span>'+city+'</span>','<span>'+a(path,city)+'</span>')
    note(f,'Fiktiven Vor-Ort-Eindruck korrigiert; eigenständiger lokaler Mehrwert bleibt mangels Ortsdaten offen')

meta('/fahrzeugaufbereitung-aus-erfurt','Fahrzeugaufbereitung Erfurt: Termin vorbereiten','Fahrzeugaufbereitung in Erfurt planen: Zustand, Wunschleistung und Ziel der Pflege vorab besprechen. Hinweise zur Anfrage, Besichtigung und Abholung.','Fahrzeugaufbereitung in Erfurt: Den Termin vorbereiten','Fahrzeugaufbereitung Termin vorbereiten','informativ / kommerziell','Autoaufbereitung')
section('/fahrzeugaufbereitung-aus-erfurt','Die passende Aufbereitung abstimmen','<p>Welche Behandlung sinnvoll ist, hängt vom Zustand und vom Ziel ab. Die '+a('/','Leistungsübersicht für Autoaufbereitung in Erfurt')+' ist der Einstieg. Nennen Sie bei der Anfrage Fahrzeug, auffällige Stellen und die geplante Nutzung nach der Pflege. Für eine gemeinsame Bestandsaufnahme können Sie einen '+a('/online-termin-buchen','Besichtigungstermin anfragen')+'.</p>')

# Minor heading/brand hygiene; do not change existing campaign configuration or forms.
for f,raw in list(site.items()):
    if f.startswith('google'):continue
    soup=BeautifulSoup(raw,'html.parser')
    if soup.title:
        title=soup.title.get_text()
        cleaned=re.sub(r'\s*\|\s*PowerTech Performance\s*\|\s*Powertech Performance$', ' | Powertech Performance',title,flags=re.I)
        if cleaned!=title:replace(f,'title',html.escape(cleaned),True);note(f,'Doppelten Markennamen im Title entfernt')
    if f.startswith('blog/') and f!='blog/index.html':
        soup=BeautifulSoup(site[f],'html.parser');h=soup.h1
        if h and re.search(r'\s*\|\s*PowerTech Performance(?: Benjamin)?$',h.get_text(),re.I):
            replace(f,'h1',html.escape(re.sub(r'\s*\|\s*PowerTech Performance(?: Benjamin)?$','',h.get_text(),flags=re.I)),True);note(f,'Markensuffix aus der H1 entfernt')

# Remaining original link-plan entries: use descriptive anchors in existing content.
plan=list(csv.DictReader((history/'internal-links.csv').open(encoding='utf-8-sig'),delimiter=';'))
from urllib.parse import urlsplit
for row in plan:
    if not row['Link-Typ'].startswith('Vorschlag'):continue
    source=urlsplit(row['Quellseite']).path;target=urlsplit(row['Zielseite']).path
    if target=='/blog/felgenversiegelung-pflege/' or source not in paths:continue
    f=paths[source];s=BeautifulSoup(site[f],'html.parser')
    if any(urlsplit(x['href']).path==target for x in (s.select_one('.article-body') or s.main).select('a[href]')):continue
    label={'/':'Autoaufbereitung in Erfurt','/adblue-service':'AdBlue-Diagnose und Reparatur','/chiptuning':'Chiptuning-Beratung in Erfurt','/luxus-aufbereitung':'Keramikversiegelung in Erfurt',primary:'Lackhärte und Politurverfahren'}.get(target,row['Anchor-Text'])
    text='<p>Passend zum Thema: '+a(target,label)+'.</p>'
    if s.select_one('.article-body'):extra(source,text)
    else:section(source,'Weiterführende Informationen',text)

# Broad but relevant links: every article gets a small related-reading block, no link carousel.
clusters={}
for p in old['pages']:
    if not p['path'].startswith('/blog/') or p['path']=='/blog/':continue
    f=p['file'];s=BeautifulSoup(site[f],'html.parser');cat=s.select_one('.article-category-tag')
    clusters.setdefault(cat.get_text(' ',strip=True) if cat else 'Fahrzeugpflege',[]).append(p['path'])
for cluster,items in clusters.items():
    # Do not route topical support through duplicate variants.
    items=[x for x in items if 'harte-und-weiche-autolacke' not in x]
    for i,path in enumerate(items):
        target=items[(i+1)%len(items)]
        if target==path:continue
        f=paths[path];s=BeautifulSoup(site[f],'html.parser');content=s.select_one('.article-body')
        if any(urlsplit(x['href']).path==target for x in content.select('a[href]')):continue
        heading=BeautifulSoup(site[paths[target]],'html.parser').h1.get_text(' ',strip=True)
        extra(path,'<p>Weiterlesen im Themenbereich '+html.escape(cluster)+': '+a(target,heading)+'.</p>')

# New commercial page: actual existing service, no assumed prices/equipment/guarantees.
newfile='trockeneisreinigung.html';paths['/trockeneisreinigung']=newfile
site[newfile]=site[paths[blog('1-step-politur-erklaert')]]
replace(newfile,'.article-meta','')
replace(newfile,'.article-tags','')
replace(newfile,'.author-box','')
replace(newfile,'.article-breadcrumb','<p class="article-breadcrumb"><a href="/">Autoaufbereitung</a> / Trockeneisreinigung</p>')
replace(newfile,'.article-category-tag','Fahrzeugreinigung',True)
replace(newfile,'link[rel=canonical]','<link rel="canonical" href="'+B+'/trockeneisreinigung">')
meta('/trockeneisreinigung','Trockeneisreinigung Erfurt – Fahrzeug & Unterboden','Trockeneisreinigung am Fahrzeug in Erfurt: Unterboden und sensible Bereiche nach Zustandsprüfung reinigen lassen. Fahrzeug und gewünschte Bereiche anfragen.','Trockeneisreinigung am Fahrzeug in Erfurt','Trockeneisreinigung Erfurt','kommerziell / lokal','Trockeneisreinigung')
body('/trockeneisreinigung','''
<p>Powertech Performance bietet Trockeneisreinigung am Fahrzeug in Erfurt an. Im Mittelpunkt stehen Unterboden, sensible Technikbereiche und hartnäckige Rückstände. Welche Behandlung zum Fahrzeug passt, richtet sich nach dem Zustand und den Flächen, die gereinigt werden sollen.</p>
<h2>Trocken reinigen statt klassisch nass waschen</h2>
<p>Beim Trockeneisstrahlen wird festes Kohlendioxid als Strahlmittel eingesetzt. Es geht anschließend in den gasförmigen Zustand über. Dadurch bleibt kein Strahlgranulat zurück und es wird kein Waschwasser aufgebracht. Der gelöste Schmutz muss trotzdem aufgenommen werden. Das Verfahren ist nicht automatisch für jede Oberfläche geeignet.</p>
<p>Eine allgemeine Beschreibung der Methode bietet <a href="https://www.kaercher.com/int/professional/know-how/dry-ice-blasting-in-car-workshops.html">Kärcher zur Trockeneisreinigung in Kfz-Werkstätten</a>. Daraus folgt keine Aussage darüber, welches Gerät an Ihrem Fahrzeug verwendet wird oder welches Ergebnis möglich ist.</p>
<h2>Unterboden und sensible Fahrzeugbereiche</h2>
<p>Am Unterboden sind Zugänglichkeit, vorhandene Beschichtungen und der Zustand der Bauteile wichtig. Beschreiben Sie möglichst genau, welche Rückstände Sie entfernen lassen möchten. Bekannte Schäden, lose Beschichtungen oder bereits bearbeitete Stellen sollten Sie in der Anfrage nennen. Die konkrete Behandlung wird passend zum Fahrzeug abgestimmt.</p>
<h3>Was eine Reinigung nicht ersetzt</h3>
<p>Ein sauberer Bereich ist nicht automatisch instand gesetzt. Wenn unter Verschmutzungen Schäden sichtbar werden, müssen diese gesondert beurteilt werden. Eine pauschale Rostbeseitigung, Reparatur oder anschließende Versiegelung ist mit der Anfrage zur Trockeneisreinigung nicht zugesagt.</p>
<h2>Trockeneisreinigung oder Motorraumwäsche?</h2>
<p>Die <a href="/blog/motorwaesche-erfurt-vorteile-kosten/">Motorraumwäsche</a> und die Trockeneisreinigung verfolgen unterschiedliche Vorgehensweisen. Entscheidend sind die betroffenen Materialien, vorhandene Verschmutzung und das Ziel der Pflege. Nennen Sie bei Ihrer Anfrage deshalb den Bereich, statt bereits eine bestimmte Behandlung vorauszusetzen.</p>
<h2>Diese Angaben helfen bei der Anfrage</h2>
<ul><li>Hersteller, Modell und Baujahr des Fahrzeugs.</li><li>Gewünschter Bereich, zum Beispiel Unterboden oder ein bestimmter Technikbereich.</li><li>Art der Verschmutzung und bekannte Vorarbeiten.</li><li>Fotos der betroffenen Stellen, soweit ohne Risiko zugänglich.</li><li>Ihr Ziel und ein möglicher Terminwunsch.</li></ul>
<p>Für Fotos müssen Sie sich nicht unter ein ungesichertes Fahrzeug begeben. Ist eine Stelle nicht zugänglich, beschreiben Sie das Anliegen zunächst. Eine <a href="/online-termin-buchen">Besichtigung in Erfurt</a> kann helfen, den Zustand gemeinsam zu besprechen.</p>
<h2>Aufwand und Termin individuell abstimmen</h2>
<p>Ohne Kenntnis des Fahrzeugs und des gewünschten Umfangs nennen wir hier keinen Pauschalpreis und keine feste Dauer. Klären Sie bei der Beratung auch die Vorbereitung des Fahrzeugs sowie Abgabe und Abholung. Zusätzliche Arbeiten sind getrennt zu besprechen.</p>
<h2>Trockeneisreinigung in Erfurt anfragen</h2>
<p>Unser Standort ist An der Klinge 10, 99095 Erfurt. <a href="/pages/kontakt.html">Senden Sie Ihre Fahrzeugdaten und den gewünschten Reinigungsbereich</a>. Weitere Pflegeangebote finden Sie in der <a href="/#leistungen">Leistungsübersicht der Autoaufbereitung</a>.</p>
''')
note(newfile,'Neue eigenständige Leistungsseite aus belegtem Bestandsangebot und kommerzieller Suchintention erstellt')

# Keep editorial previews consistent with the pages, remove duplicate cards only (URLs stay).
f='blog/index.html'
for path in list(metadata):
    if not path.startswith('/blog/'):continue
    s=BeautifulSoup(site[f],'html.parser');card=next((n for n in s.select('.blog-card') if n.get('href')==path),None)
    if not card:continue
    start,end=span(site[f],card);raw=site[f][start:end];ps=BeautifulSoup(site[paths[path]],'html.parser')
    raw=re.sub(r'(<h3[^>]*>).*?(</h3>)',lambda m:m[1]+html.escape(ps.h1.get_text(' ',strip=True))+m[2],raw,flags=re.S)
    raw=re.sub(r'(<p[^>]*>).*?(</p>)',lambda m:m[1]+html.escape(ps.select_one('meta[name=description]')['content'])+m[2],raw,count=1,flags=re.S)
    site[f]=site[f][:start]+raw+site[f][end:]
append(f,'.blog-intro' if BeautifulSoup(site[f],'html.parser').select_one('.blog-intro') else 'main','<section class="section"><div class="container"><h2>Passende Leistungen zu den Ratgebern</h2><p>'+a('/','Autoaufbereitung')+' · '+a('/luxus-aufbereitung','Keramikversiegelung')+' · '+a('/adblue-service','AdBlue-Service')+' · '+a('/chiptuning','Chiptuning')+' · '+a('/trockeneisreinigung','Trockeneisreinigung')+' · '+a('/glosar','Fachbegriffe im Glossar')+'</p></div></section>')
note(f,'Artikelteaser an überarbeitete Inhalte angepasst; Leistungscluster zugänglich gemacht')
append('pages/seitenuebersicht.html','.sitemap-list','<li>'+a('/trockeneisreinigung','Trockeneisreinigung am Fahrzeug')+'<span>Unterboden und geeignete Technikbereiche</span></li>')
site['pages/seitenuebersicht.html']=site['pages/seitenuebersicht.html'].replace('>Standorte<','>Einzugsgebiet<').replace('Standort-Landingpage','Kunden aus der Region; Standort Erfurt')

# Breadcrumbs: matches actual visible trail; no fictitious review/author/date data.
for path,f in paths.items():
    if f.startswith('google'):continue
    s=BeautifulSoup(site[f],'html.parser')
    if path.startswith('/blog/') and path!='/blog/':
        crumb=s.select_one('.article-breadcrumb')
        if crumb:
            title=s.h1.get_text(' ',strip=True)
            replace(f,'.article-breadcrumb','<p class="article-breadcrumb">'+a('/','Startseite')+' / '+a('/blog/','Ratgeber')+' / <span>'+html.escape(title)+'</span></p>')
            canon=BeautifulSoup(site[f],'html.parser').select_one('link[rel=canonical]')['href']
            # Duplicate aliases retain only the canonical's identity, no extra schema entity.
            if canon!=B+path:continue
            schema={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Startseite','item':B+'/'},{'@type':'ListItem','position':2,'name':'Ratgeber','item':B+'/blog/'},{'@type':'ListItem','position':3,'name':title,'item':B+path}]}
            site[f]=site[f].replace('</head>','<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False)+'</script>\n</head>')
            note(f,'Sichtbare Breadcrumbs und passende BreadcrumbList ergänzt')
service_schema={'@context':'https://schema.org','@type':'Service','name':'Trockeneisreinigung am Fahrzeug','serviceType':'Fahrzeugreinigung','url':B+'/trockeneisreinigung','provider':{'@type':'AutomotiveBusiness','name':'Powertech Performance','url':B+'/'},'areaServed':{'@type':'City','name':'Erfurt'}}
site[newfile]=site[newfile].replace('</head>','<script type="application/ld+json">'+json.dumps(service_schema,ensure_ascii=False)+'</script>\n</head>')

# Fix heading hierarchy in existing service and overview components without styling changes.
for f,raw in list(site.items()):
    if f.startswith('google'):continue
    s=BeautifulSoup(raw,'html.parser')
    service=s.select_one('#leistungen .grid')
    if service and not s.select_one('#leistungen h2'):
        append_to= s.select_one('#leistungen .container')
        start,end=span(raw,append_to);pos=raw.index('>',start)+1
        site[f]=raw[:pos]+'\n<h2>Leistungen passend zum Fahrzeugzustand</h2>'+raw[pos:];note(f,'Fehlende H2 vor Leistungskarten ergänzt')
if not BeautifulSoup(site['blog/index.html'],'html.parser').select_one('.blog-grid').find_previous_sibling('h2'):
    site['blog/index.html']=site['blog/index.html'].replace('<div class="blog-grid">','<h2>Ratgeber zur Fahrzeugpflege und Technik</h2>\n<div class="blog-grid">',1)

# Permanent repairs only for 23 unambiguous legacy/path variants; the intent-changing case stays open.
cfg=json.loads((R/'vercel.json').read_text('utf8'));added=[]
for m in old['performance']:
    if m['source_url'].split('://',1)[1].split('/',1)[1]=='adblue-deaktivieren/':continue
    original_path=urlsplit(m['source_url']).path
    target=urlsplit(m['candidate'] or m['thematic']).path
    if original_path in paths:continue
    if not target or target not in paths:continue
    assert original_path.rstrip('/')==target or original_path.strip('/')==target.removeprefix('/blog/').strip('/'),(original_path,target)
    rule={'source':original_path,'destination':target,'permanent':True}
    if not any(x['source']==original_path for x in cfg['redirects']):cfg['redirects'].append(rule);added.append({**rule,'impressions':m['impressions'],'reason':'404 im Export; identischer Artikelslug bzw. reine Slash-Variante eines vorhandenen Ziels'})
cfg['rewrites'].append({'source':'/trockeneisreinigung','destination':'/trockeneisreinigung.html'})
for source in ['/trockeneisreinigung.html','/trockeneisreinigung/']:
    cfg['redirects'].append({'source':source,'destination':'/trockeneisreinigung','permanent':True})
# robots now permits noindex to be read; no unrelated path block introduced.
robots='User-agent: *\nAllow: /\n\nSitemap: '+B+'/sitemap.xml\n'
from xml.etree import ElementTree as ET
NS='http://www.sitemaps.org/schemas/sitemap/0.9';ET.register_namespace('',NS)
tree=ET.parse(R/'sitemap.xml');root=tree.getroot();removed=[]
for entry in list(root):
    loc=entry.find('{'+NS+'}loc');path=urlsplit(loc.text).path
    if path not in paths:raise ValueError(path)
    s=BeautifulSoup(site[paths[path]],'html.parser')
    canon=s.select_one('link[rel=canonical]')['href']
    if s.select_one('meta[name=robots]') and 'noindex' in s.select_one('meta[name=robots]').get('content','') or canon!=B+path:
        removed.append(path);root.remove(entry)
    else:loc.text=B+path
node=ET.SubElement(root,'{'+NS+'}url');ET.SubElement(node,'{'+NS+'}loc').text=B+'/trockeneisreinigung'
ET.indent(tree,space='  ')

# Validate protection before writing any HTML.
for f,raw in original.items():
    assert protected(site[f])==baseline['pages'][f], 'Protected code or controls changed: '+f
for f,raw in site.items():
    p=R/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(raw,encoding='utf8')
(R/'vercel.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(R/'robots.txt').write_text(robots,encoding='utf8');tree.write(R/'sitemap.xml',encoding='utf-8',xml_declaration=True)
manifest={'state':'lokal umgesetzt; nicht veröffentlicht','base':B,'changed_pages':records,'metadata':metadata,'redirect_repairs':added,'new_urls':['/trockeneisreinigung'],'deferred_new_urls':{'/blog/felgenversiegelung-pflege/':'Kein Nachfragebeleg und keine produktspezifischen Pflegeangaben; kein zusätzlicher generischer Ratgeber.'},'canonical_primary':primary,'canonical_aliases':[blog('harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung'),blog('harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung-2')],'removed_from_sitemap':removed,'decision_needed':{'/adblue-deaktivieren/':'Zielwechsel von Deaktivierungsangebot zu Diagnose/Reparatur nicht rein technisch eindeutig; fachliche Zielentscheidung erforderlich.','/ads':'Indexierbarkeit bewusst erhalten; separates Ads-/SEO-Ziel benötigt Kampagnenentscheidung.'}}
(O/'implementation.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'pages':len(site),'changed':len(records),'legacy_redirects':len(added),'removed_sitemap':removed},ensure_ascii=False))
