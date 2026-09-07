"""Current, local SEO inventory. Historical live measurements remain separately labelled."""
from pathlib import Path
import csv,json,collections,urllib.parse as U,datetime
O=Path(__file__).resolve().parents[1];R=O.parent;B='https://www.powertech-performance.com'
E=json.loads((O/'evidence.json').read_text('utf8'));I=json.loads((O/'implementation.json').read_text('utf8'))
H=O/'history'/'2026-09-07-analysis';OLD=json.loads((H/'evidence.json').read_text('utf8'))
LIVE=json.loads((H/'live-check.json').read_text('utf8'));LR={r['url']:r for r in LIVE['results']}
P=E['pages'];by={p['path']:p for p in P};oldby={p['path']:p for p in OLD['pages']}
def readcsv(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline=''),delimiter=';'))
oldseo={U.urlsplit(r['URL']).path:r for r in readcsv(H/'seo-map.csv') if r['Dateipfad']}
oldkw={U.urlsplit(r['bestehende Zielseite']).path:r for r in readcsv(H/'keyword-map.csv') if r['bestehende Zielseite']}
proposal=[r for r in readcsv(H/'internal-links.csv') if r['Link-Typ'].startswith('Vorschlag')]
def dump(name,rows):
    with (O/name).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter=';');w.writeheader();w.writerows(rows)
def j(v):return ' | '.join(v)
def allowed(p):return not p['verification'] and 'noindex' not in j(p['robots']).lower()
def primary(p):return allowed(p) and p['canonical']==[p['url']]
def cluster(p):return p['seo_metadata'].get('cluster') or oldseo.get(p['path'],{}).get('Themencluster','Trockeneisreinigung')
def keyword(p):return p['seo_metadata'].get('keyword') or p['source_index'].get('Hauptkeyword (vermutet)','')
def intent(p):return p['seo_metadata'].get('intent') or oldseo.get(p['path'],{}).get('Suchintention','kommerziell / lokal')
def live(p):return LR.get(p['url']) or LR.get('https://powertech-performance.com'+p['path'],{})
redirects={r['source']:r['destination'] for r in E['config']['redirects'] if '(.*)' not in r['source']}
alias=set(I['canonical_aliases']); riskby={path:r.get('Kannibalisierungsrisiko','') for path,r in oldkw.items() if r.get('Kannibalisierungsrisiko','').startswith('K')}
def risks(p):
    path=p['path']
    if path in alias or path==I['canonical_primary']:return 'K1: Canonical-Zuordnung umgesetzt; Google-Auswahl nach Veröffentlichung prüfen'
    if path in riskby:return riskby[path].split(':',1)[0]+': Rollen/Verlinkung teilweise verbessert; Wirkung mangels Query-URL-Daten offen'
    return 'nicht belegt; keine Query-URL-Zeitreihen'
def status(p):
    if p['path']=='/ads':return 'benötigt meine Entscheidung'
    if p['path'] in riskby and p['path'] not in alias and p['path']!=I['canonical_primary']:return 'teilweise umgesetzt'
    if cluster(p)=='Einzugsgebiet':return 'teilweise umgesetzt'
    return 'umgesetzt'
measured={}
for m in OLD['performance']:
    r=LR[m['source_url']]
    c=LR.get(m['candidate'],{})
    if m['candidate'] and r['status']==200 and c.get('status')==200 and r.get('final_url')==c.get('final_url'):
        measured[U.urlsplit(m['candidate']).path]=m
maps=[]
for p in P:
    m=measured.get(p['path'],{});r=live(p); issues=[]
    if primary(p) and len(p['incoming'])<2:issues.append('Wenig interne Unterstützung'+('; Kampagnenrolle offen' if p['path']=='/ads' else ''))
    if p['path'] in alias:issues.append('Erreichbare historische Fassung; Canonical verweist auf Hauptfassung')
    if p['path'] in riskby and p['path'] not in alias and p['path']!=I['canonical_primary']:issues.append('Intent-Überschneidung nach Veröffentlichung beobachten')
    if cluster(p)=='Einzugsgebiet':issues.append('Keine fiktive Niederlassung mehr; weiterer lokaler Mehrwert benötigt Betriebsdaten')
    if not issues:issues.append('Lokale technische Prüfpunkte umgesetzt; Live-Abnahme nach Veröffentlichung offen')
    row={'URL':p['url'],'Seitentyp': 'Leistungsseite' if p['path']=='/trockeneisreinigung' else oldseo.get(p['path'],{}).get('Seitentyp','Verifizierungsdatei'),'Title':p['title'],'Meta Description':j(p['description']),'H1':j(p['headings']['h1']),'Hauptthema':keyword(p) if keyword(p) not in ('','-') else p['title'],'vermutetes Hauptkeyword':keyword(p),'Nebenkeywords':j(p['headings']['h2'][:3]) if allowed(p) else '', 'Suchintention':intent(p),'Themencluster':cluster(p),'interne Links von':j(p['incoming']),'interne Links zu':j(p['outgoing']),'Anzahl eingehender interner Links':len(p['incoming']),'Anzahl ausgehender interner Links':len(p['outgoing']),'Canonical':j(p['canonical']),'Indexierungsstatus':'Verifizierung, kein SEO-Ziel' if p['verification'] else 'noindex; crawlbar' if not allowed(p) else 'index erlaubt; kanonische Hauptfassung' if primary(p) else 'index erlaubt; andere kanonische Fassung','SEO-Status':j(issues),'Optimierungspotenzial':'Nach Veröffentlichung URL-Prüfung; '+('Query-URL-Verteilung und inhaltliche Abgrenzung weiter prüfen' if p['path'] in riskby else 'Indexierung und Suchentwicklung beobachten'),'Priorität':'P1' if p['path'] in riskby else 'P2','Klicks':'','Impressionen':m.get('impressions',''),'CTR':'','durchschnittliche Position':'','relevante Suchanfragen':'','H2':j(p['headings']['h2']),'H3':j(p['headings']['h3']),'Sitemap':'ja' if p['sitemap'] else 'nein','Robots Meta':j(p['robots']),'Bilder und Alt-Texte':json.dumps(p['images'],ensure_ascii=False),'CSS-Bilder / ARIA':json.dumps(p['aria_images'],ensure_ascii=False),'Strukturierte Daten':json.dumps(p['schema'],ensure_ascii=False),'Content-Abschnitte':json.dumps(p['sections'],ensure_ascii=False),'Wörter Hauptinhalt':p['words'],'Dateipfad':p['file'],'Lokaler Status':'200 (Datei / Rewrite)','Live HTTP (Analyse-Snapshot)':r.get('status','nicht geprüft'),'Live Endziel (Analyse-Snapshot)':r.get('final_url',''),'Messwertquelle':m.get('source_url',''),'Messwert-Zuordnung':'Historisch belegtes identisches Endziel; keine Query-Messung' if m else 'keine eindeutig zugeordneten Messwerte','Status':status(p),'Umgesetzte Maßnahmen':j(I['changed_pages'].get(p['file'],[])),'Veröffentlichung':'ausstehend; lokaler Projektstand','Keyword-Basis':'redaktionelle Hypothese; Nebenkeywords sind Überschriftenthemen','Kannibalisierungsrisiko':risks(p)}
    if p['verification']:row.update({'Status':'umgesetzt','Umgesetzte Maßnahmen':'Unverändert erhalten und geprüft','Priorität':'P3','SEO-Status':'kein SEO-Inhaltsziel'})
    maps.append(row)
for m in OLD['performance']:
    path=U.urlsplit(m['source_url']).path
    if path in measured:continue
    row={k:'' for k in maps[0]};target=redirects.get(path)
    row.update({'URL':m['source_url'],'Seitentyp':'Historische Export-URL / Alias','Hauptthema':'Ziel: '+(B+target if target else m['thematic']),'Canonical':'','Indexierungsstatus':'lokaler Redirect auf '+B+target if target else '404 im letzten Live-Check; Zielentscheidung offen','SEO-Status':'404-Behebung lokal implementiert' if target else 'Inhaltliche Zielgleichheit nicht sicher','Optimierungspotenzial':'Redirect nach Veröffentlichung prüfen' if target else 'Entscheidung zu Diagnose-/Reparaturziel erforderlich','Priorität':'P1','Impressionen':m['impressions'],'Lokaler Status':'308 → '+target if target else '404','Live HTTP (Analyse-Snapshot)':LR[m['source_url']]['status'],'Live Endziel (Analyse-Snapshot)':LR[m['source_url']].get('final_url',''),'Messwertquelle':m['source_url'],'Messwert-Zuordnung':'Original-URL; nicht auf Redirectziel aggregiert','Status':'umgesetzt' if target else 'benötigt meine Entscheidung','Umgesetzte Maßnahmen':'Gezielte Weiterleitung wegen belegtem 404 und gleichem Artikel-/Seitenpfad' if target else 'Keine Weiterleitung angelegt','Veröffentlichung':'ausstehend; lokaler Projektstand'})
    maps.append(row)
dump('seo-map.csv',maps)

urlmap=[]
for m in OLD['performance']:
    path=U.urlsplit(m['source_url']).path;target=redirects.get(path)
    urlmap.append({'Export-URL':m['source_url'],'Impressionen':m['impressions'],'Zeitraum':'unbekannt','Live HTTP (Analyse-Snapshot)':LR[m['source_url']]['status'],'Lokale Zuordnung':B+path if path in by else B+target if target else '', 'Lokaler Status':'200' if path in by else '308' if target else '404','Zuordnungstyp':'identische Quell-URL' if path in by else 'Redirect lokal implementiert; kein rückwirkender Messwert-Join' if target else 'nur thematischer Kandidat','Mögliche Zielseite':m['thematic'] if not target and path not in by else '', 'Status':'umgesetzt' if target or path in by else 'benötigt meine Entscheidung','Veröffentlichung':'ausstehend'})
dump('url-mapping.csv',urlmap)

keywords=[]
for p in P:
    key=keyword(p)
    if key in ('','-'):continue
    owner=p['canonical'][0] if p['path'] in alias else B+'/' if p['path']=='/ads' else p['url']
    keywords.append({'Keyword / Suchanfrage':key,'bestehende Zielseite':p['url'],'Klicks':'','Impressionen':'','CTR':'','Position':'','Suchvolumen':'','CPC':'','Suchintention':intent(p),'Themencluster':cluster(p),'Hauptkeyword oder Nebenkeyword':'Nebenkeyword / historische Fassung' if p['path'] in alias else 'Nebenkeyword / Kampagnenvariante' if p['path']=='/ads' else 'Hauptkeyword (redaktionell)','passende bestehende Seite':owner,'mögliche neue Seite':'','Kannibalisierungsrisiko':risks(p),'Priorität':'P1' if p['path'] in riskby else 'P2','Handlungsempfehlung':'beobachten' if p['path'] in riskby else 'keine Änderung notwendig','Status':status(p),'Begründung':'Lokale Optimierung umgesetzt; nächste Bewertung nach Veröffentlichung und mit Query-URL-Zeitreihe.','Datenquelle':'SEO-Analyse und aktuelle Inhalte; ursprünglicher Index unverändert archiviert','Datenart':'Keyword-Hypothese, keine gemessene Suchanfrage','URL-Impressionen (nicht Keyword-Messwert)':measured.get(p['path'],{}).get('impressions',''),'Ursprüngliches vermutetes Keyword':p['source_index'].get('Hauptkeyword (vermutet)',''),'Veröffentlichung':'ausstehend'})
row={k:'' for k in keywords[0]};row.update({'Keyword / Suchanfrage':'Felgenversiegelung pflegen','Suchintention':'informativ','Themencluster':'Felgenpflege','Hauptkeyword oder Nebenkeyword':'Planungshypothese','passende bestehende Seite':B+'/#leistungen','mögliche neue Seite':B+'/blog/felgenversiegelung-pflege/','Priorität':'P3','Handlungsempfehlung':'beobachten','Status':'nicht umgesetzt','Begründung':I['deferred_new_urls']['/blog/felgenversiegelung-pflege/'],'Datenart':'keine Nachfrage-/Produktdaten vorhanden','Veröffentlichung':'keine Datei erstellt'})
keywords.append(row);dump('keyword-map.csv',keywords)

def lk(source,l):return (source,l['path'],l['fragment'],l['anchor'],l['context'])
oldlinks=collections.Counter(lk(p['path'],l) for p in OLD['pages'] for l in p['links'])
rows=[];added=0
for p in P:
    for l in p['links']:
        key=lk(p['path'],l);existing=oldlinks[key]>0
        if existing:oldlinks[key]-=1
        else:added+=1
        rows.append({'Quellseite':p['url'],'Zielseite':l['url']+('#'+l['fragment'] if l['fragment'] else ''),'Anchor-Text':l['anchor'],'Link-Typ':'Bestand: '+('Sprunglink' if l['fragment'] else 'Seitenlink'),'Position/Kontext':l['context'],'Themencluster':cluster(p),'Bewertung':'lokal auflösbar' if l['resolved'] or l['asset'] else 'Ziel prüfen','Optimierungsvorschlag':'','Lokale Ziel-URL':B+l['resolved'] if l['resolved'] else '', 'nofollow':'ja' if 'nofollow' in l['rel'] else 'nein','Status':'umgesetzt','Änderung':'vorhanden, geprüft' if existing else 'neu oder gezielt geändert','Veröffentlichung':'ausstehend'})
proposal_status=[]
for r in proposal:
    source=U.urlsplit(r['Quellseite']).path;target=U.urlsplit(r['Zielseite']).path
    done=source in by and any(l['resolved']==target and l['context']=='Inhalt' for l in by[source]['links'])
    state='umgesetzt' if done else 'nicht umgesetzt'
    reason='Passender Inhaltslink vorhanden' if done else I['deferred_new_urls'].get(target,'Kontextprüfung erforderlich')
    proposal_status.append({'Quellseite':B+source,'Zielseite':B+target,'Status':state,'Begründung':reason})
    if not done:
        row={k:'' for k in rows[0]};row.update({'Quellseite':B+source,'Zielseite':B+target,'Anchor-Text':r['Anchor-Text'],'Link-Typ':'Vorschlag, zurückgestellt','Position/Kontext':r['Position/Kontext'],'Themencluster':r['Themencluster'],'Bewertung':'kein Bestandslink','Optimierungsvorschlag':reason,'Status':state,'Veröffentlichung':'nicht vorhanden'})
        rows.append(row)
dump('internal-links.csv',rows);dump('link-plan-status.csv',proposal_status)

summary={'scope':'lokal umgesetzt; nicht veröffentlicht','scanned_at':E['scanned_at'],'content_pages':len([p for p in P if not p['verification']]),'html':len(P),'existing_content_pages_optimized':len([f for f in I['changed_pages'] if f in {p['file'] for p in OLD['pages']}]),'new_pages':len(I['new_urls']),'new_urls':I['new_urls'],'deferred_new_pages':len(I['deferred_new_urls']),'source_queries':0,'source_keyword_hypotheses':50,'source_keyword_assignments':55,'keyword_map_rows':len(keywords),'seo_map_rows':len(maps),'internal_link_occurrences':sum(len(p['links']) for p in P),'new_or_changed_link_occurrences':added,'implemented_link_proposals':sum(r['Status']=='umgesetzt' for r in proposal_status),'deferred_link_proposals':sum(r['Status']!='umgesetzt' for r in proposal_status),'redirect_repairs':len(I['redirect_repairs']),'redirect_repair_source_impressions':sum(r['impressions'] for r in I['redirect_repairs']),'unresolved_404_source_impressions':sum(m['impressions'] for m in OLD['performance'] if U.urlsplit(m['source_url']).path not in by and U.urlsplit(m['source_url']).path not in redirects),'sitemap_urls':len(E['sitemap']),'canonical_primary_indexable':sum(primary(p) for p in P),'canonical_aliases':len(alias),'noindex':sum(not allowed(p) and not p['verification'] for p in P),'unresolved_internal_targets':sum(not l['resolved'] and not l['asset'] for p in P for l in p['links']),'missing_fragments':sum(l['missing_fragment'] for p in P for l in p['links']),'risk_groups_historical':7,'confirmed_ranking_cannibalization':0,'source_impressions':6493,'matched_historical_impressions':169,'historical_404_impressions':6324}
(O/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
lines=['# Technischer Detailnachweis nach Umsetzung','', 'Aktueller lokaler Stand. Noch nicht veröffentlicht. Originalanalyse und Live-Snapshot: `history/2026-09-07-analysis/`. Neue Messwerte werden nicht vorgetäuscht.','', '## Vollständiger Seitenbestand','', '| URL | Eingehende Seiten | Ausgehende Seiten | Canonical | Sitemap |','|---|---:|---:|---|---|']
for p in P:lines.append(f"| {p['path']} | {len(p['incoming'])} | {len(p['outgoing'])} | {j(p['canonical'])} | {'ja' if p['sitemap'] else 'nein'} |")
lines+=['','## Technische Ergebnisse','',f"{len(P)} HTML-Routen, {len(E['sitemap'])} Sitemap-URLs. {summary['canonical_primary_indexable']} indexierbare kanonische Hauptseiten, zwei erreichbare Canonical-Varianten und sechs noindex-Seiten. Keine Inhaltsseite gelöscht. Alle Canonicals zeigen auf den bestehenden www-Host. Die Host-Weiterleitung selbst wurde nicht geändert.", '',f"{summary['internal_link_occurrences']} interne Link-Vorkommen; {summary['missing_fragments']} fehlende Fragmente und {summary['unresolved_internal_targets']} nicht auflösbare interne Ziele. {summary['implemented_link_proposals']} der 44 ursprünglichen Linkvorschläge umgesetzt. Die beiden Links zum zurückgestellten Felgenpflege-Beitrag fehlen bewusst.", '', '## Bild- und Schema-Inventar','',f"{sum(len(p['images']) for p in P)} img-Elemente; {sum(im['alt'] is None for p in P for im in p['images'])} fehlende alt-Attribute. Leere dekorative Alt-Texte werden nicht künstlich mit Keywords gefüllt. Schema, CSS-ARIA-Bilder, H1/H2/H3, Abschnitte und vollständiger Haupttext werden in evidence.json erfasst und in seo-map.csv referenziert.", '',f"JSON-LD auf {sum(bool(p['schema']) for p in P)} Seiten. BreadcrumbList folgt den sichtbaren Artikel-Breadcrumbs; vorhandene AdBlue-Daten wurden auf www angepasst. Die neue Trockeneis-Seite enthält ausschließlich ein belegtes Service-Objekt, keine Bewertungen oder Preisangaben.", '', '## Architektur und Funktionsschutz','',f"Statische HTML-/CSS-/Vanilla-JS-Seite. {len(E['config']['rewrites'])} Rewrites, {len(E['config']['redirects'])} Redirect-Regeln. 23 neue Reparatur-Redirects und zwei technische Alias-Regeln für die neue Leistungsseite. Offizielle Vercel-Routenkompilierung in routing-compiled.json, GET-basierte lokale Prüfung in validation-results.json.", '', 'JS-Dateien, API-Dateien, Paketkonfiguration, Formularmarkup, Kontaktadressen und ausführbare Skriptblöcke werden gegen protection-baseline.json geprüft. Zwei kleine CSS-Ergänzungen machen Inhaltslinks auf dem vorhandenen dunklen Design lesbar; CTA-Regeln bleiben unverändert.','', '## Grenzen','', 'Der lokale Vorschauserver verwendet die mit @vercel/routing-utils kompilierten Routingmuster. Er emuliert keinen SMTP-Endpunkt, keine Vercel-Cloud und keine Google-Indexierung. Externes Tracking wird ausschließlich im Preview per CSP blockiert; die Produktivdateien erhalten diese CSP nicht. Kein Formular wurde abgesendet. Core Web Vitals und Keyword-Positionen wurden nicht gemessen.']
(O/'technical-inventory.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
print(json.dumps(summary,ensure_ascii=False,indent=2))

if (O/"business-policy.json").exists():
    import runpy
    runpy.run_path(str(O/"tools/apply-business-policy.py"))
