"""Refresh human-readable implementation status, keeping the original audit in history/."""
from pathlib import Path
import json,csv
O=Path(__file__).resolve().parents[1]
I=json.loads((O/'implementation.json').read_text('utf8'));S=json.loads((O/'summary.json').read_text('utf8'));E=json.loads((O/'evidence.json').read_text('utf8'));V=json.loads((O/'validation-results.json').read_text('utf8'))
B=I['base'];P=E['pages'];by={p['file']:p for p in P}
actions=[
('R1','23 historische Export-URLs','umgesetzt','Gezielte permanente Weiterleitungen auf denselben bestehenden Artikel-/Seitenpfad. 6.303 historische Impressionen. Kein pauschaler Root-Fallback.','Nach Veröffentlichung live prüfen.'),
('R2','/adblue-deaktivieren/','benötigt meine Entscheidung','21 historische Impressionen; Wechsel von Deaktivierungsangebot zu Diagnose-/Reparaturintention nicht eindeutig. Keine Weiterleitung angelegt.','Entscheiden, ob /adblue-service der inhaltlich richtige Nachfolger ist.'),
('T1','Alle 61 bisherigen Inhaltsseiten und /trockeneisreinigung','umgesetzt','Canonical-/Metadaten-Host auf den bereits live genutzten www-Host ausgerichtet. Vorhandene Host-Weiterleitung unverändert.','Deployment und Google-Canonical anschließend prüfen.'),
('T2','Sitemap und robots.txt','umgesetzt','Drei noindex-Rechtsseiten und zwei Canonical-Duplikate aus Sitemap genommen; alle fünf robots-Sperren entfernt, damit noindex lesbar bleibt.','Noindex nach Veröffentlichung in der URL-Prüfung kontrollieren.'),
('L1','Startseite, Leistungen, Blog und Ratgeber','umgesetzt','42 von 44 ursprünglichen Inhaltslinkvorschlägen umgesetzt, plus passende Ratgeberverknüpfungen.','Zwei zurückgestellte Vorschläge betreffen den nicht erstellten Felgenpflege-Beitrag.'),
('L2','48 Startseiten-Sprunglinks und irreführender Kontaktanker','umgesetzt','Vorhandene Ziele verwendet und Anchor-Texte korrigiert. Keine fehlenden IDs im aktuellen Gesamtscan.','Keine weitere Maßnahme nötig.'),
('K1','Drei Lackhärte-Fassungen','umgesetzt','Zwei identische Altvarianten verweisen kanonisch auf /blog/harte-weiche-autolacke-lackaufbereitung/. Alle URLs bleiben erreichbar; eindeutige Titles.','Google-Auswahl nach Veröffentlichung beobachten, nicht als Rankinggewinn ausgeben.'),
('K2','Chiptuning, Keramik, Innenraum, Leasing, Autoaufbereitung','teilweise umgesetzt','Leistungsziele gestärkt, Titel/Intentionen präzisiert und Informationsfragen ergänzt; keine blind zusammengelegten URLs.','Restliche breite Textüberschneidungen mit Query-URL-Daten bewerten.'),
('K3','/ads','benötigt meine Entscheidung','Bestehende Indexierbarkeit, Formular, CTAs und Tracking erhalten. Canonical-Host korrigiert und Hauptseite verknüpft.','Dauerhaft organisches Ziel oder reine Kampagnenseite? Erst dann über noindex entscheiden.'),
('C1','AdBlue-Service und drei AdBlue-Ratgeber','umgesetzt','Irreführende pauschale Deaktivierungs-/Zeitversprechen in den drei Artikeln ersetzt; Diagnose, Rückrüstung und Zeitbedarf unterschieden. Blogteaser angepasst.','Fachlich geänderte Texte vor Veröffentlichung betriebsintern mitlesen.'),
('C2','Sechs bestehende Stadtseiten','teilweise umgesetzt','Fiktiven Vor-Ort-Eindruck korrigiert: realer Standort Erfurt. Anfragevorbereitung und Erreichbarkeit ergänzt. Keine neue Stadtseite.','Eigenständige lokale Belege/Anreiseinformationen fehlen; keine Fakten erfunden.'),
('N1','/trockeneisreinigung','umgesetzt','Neue Leistungsseite aus belegtem Bestandsangebot, abgeleitetem Keyword und eigenständiger kommerzieller Intention.','Kein gemessenes Suchvolumen; Bedarf und Wirkung nach Veröffentlichung beobachten.'),
('N2','/blog/felgenversiegelung-pflege/','nicht umgesetzt','Kein Nachfragebeleg und keine Angaben zur tatsächlich verwendeten Versiegelung. Kein austauschbarer Ratgeber erzeugt.','Bei bestätigten Kundennachfragen und Produkthinweisen erneut prüfen.'),
('T3','39 Seiten mit JSON-LD','umgesetzt','Passende BreadcrumbList für sichtbare Artikelpfade; neue Service-Daten, vorhandenes AdBlue-Schema auf www.','Kein Rich-Result- oder Bewertungsversprechen.'),
('T4','Große Bilddateien / Core Web Vitals','nicht umgesetzt','Keine belastbare Laufzeitmessung. Originalbilder und Qualität erhalten; kein pauschales Umkodieren. Leeres inhaltliches Alt-Attribut ergänzt.','Leistungsdaten nach Veröffentlichung separat messen.'),
('D1','Position 4–20 / CTR-Chancen','nicht umgesetzt','Klicks, Positionen, CTR und Query-URL-Zeitreihen fehlen in beiden Quellen.','Passenden Search-Console-Export ergänzen; keine Kennzahlen erfinden.'),
('Q1','Gesamtes Projekt','umgesetzt',f"{V['html_checked']} HTML-Routen, {V['http_checks']} lokale HTTP-Prüfungen, {V['inline_js_parsed']} inline JS-Blöcke geprüft; Ergebnisse {V['result']}.",'Kein Deployment und kein SMTP-Testversand durchgeführt.')]
with (O/'implementation-status.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f,delimiter=';');w.writerow(['ID','Betroffene URLs / Bereich','Status','Umsetzung / Begründung','Nächster Schritt']);w.writerows(actions)

audit=f'''# SEO-Audit nach Umsetzung

Stand: 07.09.2026. **Lokaler Projektstand, noch nicht veröffentlicht.** „Umgesetzt“ bezeichnet Änderungen an den Projektdateien, nicht bereits gemessene Auswirkungen bei Google. Die vollständige Ausgangsanalyse bleibt unverändert unter [history/2026-09-07-analysis/SEO-AUDIT.md](history/2026-09-07-analysis/SEO-AUDIT.md).

## Ergebnis

- {S['existing_content_pages_optimized']} bestehende Inhaltsseiten gezielt technisch und/oder redaktionell optimiert; keine bestehende URL gelöscht oder umbenannt.
- Eine neue Leistungsseite: `/trockeneisreinigung`. Insgesamt {S['content_pages']} Inhaltsseiten plus Google-Verifizierungsdatei.
- {S['redirect_repairs']} gezielte Reparatur-Redirects für alte URLs mit zusammen 6.303 historischen Impressionen. Zwei zusätzliche Alias-Redirects betreffen ausschließlich die neue Trockeneis-Seite.
- {S['internal_link_occurrences']} interne Link-Vorkommen, {S['implemented_link_proposals']} von 44 ursprünglichen Linkvorschlägen umgesetzt. {S['new_or_changed_link_occurrences']} Link-Vorkommen sind neu oder wurden in Ziel, Anchor oder Kontext geändert; diese Zahl ist **nicht** die Zahl neu angelegter Seitenverbindungen.
- Null kaputte interne Ziele, null fehlende Sprungziele, genau eine H1 je Inhaltsseite, keine doppelten Titles.
- {S['sitemap_urls']} kanonische indexierbare Sitemap-URLs. Zwei historische Lackhärte-Fassungen bleiben erreichbar und referenzieren die Hauptfassung.
- Schutzprüfung für alle ursprünglichen HTML-Seiten, Formulare, ausführbaren Skripte und Kontaktwege bestanden. JavaScript-, API- und Paketdateien unverändert. CSS nur um gut lesbare Inhaltslinks ergänzt.

## Kritische Probleme

**Teilweise umgesetzt:** 23 der 24 im Ausgangsaudit beobachteten 404-URLs besitzen jetzt eine eindeutige lokale Weiterleitung. Die Ziele stimmen im Artikelslug überein oder sind reine Slash-Varianten. Der zwingende Grund ist die nachgewiesene Nichterreichbarkeit genau dieser Export-URLs. Weiterleitungen wurden ausschließlich in `vercel.json` implementiert, nicht live veröffentlicht. Originale Messwerte bleiben an ihrer Quell-URL; sie werden nicht auf Nachfolger addiert.

**Benötigt meine Entscheidung:** `/adblue-deaktivieren/` mit 21 historischen Impressionen bleibt ohne Redirect. Der vorgeschlagene Nachfolger `/adblue-service` hat eine andere, diagnostische Angebotsausrichtung. Diese Entscheidung kann nicht allein aus dem Slug abgeleitet werden.

**Umgesetzt:** Canonicals, URL-Metadaten, bestehende JSON-LD-URLs und Sitemap verwenden `https://www.powertech-performance.com`. Die bereits vorhandene Live-Host-Weiterleitung wurde nicht verändert. Nach Veröffentlichung ist die tatsächliche Google-Auswahl zu kontrollieren.

## Hohe Priorität

- **Umgesetzt:** Direkte Links von der Startseite zu Keramik, Chiptuning, AdBlue-Service, Innenraum, Lackkorrektur, Leasing, Motorraum, Termin und Trockeneis. Wichtige Ziele hängen nicht mehr nur an der früher gesperrten Seitenübersicht.
- **Umgesetzt:** 48 fehlende Startseiten-Sprungziele korrigiert. noindex-Seiten sind crawlbar, aber nicht in der Sitemap.
- **Umgesetzt:** Drei AdBlue-Ratgeber nach Risiken/Alternativen, Rückrüstung und Zeitbedarf abgegrenzt und an das Serviceangebot angebunden. Unbelegte pauschale Erfolgs-/Zeitversprechen in diesen neu gefassten Texten entfernt. Die vorhandenen nicht betroffenen DPF-/Spezialfahrzeugartikel bleiben fachlich weiter zu prüfen.
- **Teilweise umgesetzt:** Stadtseiten weisen eindeutig auf den realen Standort Erfurt hin. Weiterer ortsspezifischer Nutzen erfordert tatsächliche Informationen; er wurde nicht erfunden.

## Bestehende Seiten mit Rankingpotenzial

Die folgenden Zahlen sind **historische Seitenimpressionen**, keine aktuellen Rankings:

| URL | Vorhandene Messung | Umgesetzt |
|---|---:|---|
| `/` | 130 | H1/Metadaten präzisiert, Leistungskacheln verlinkt, Termin-/Glossarzugänge und transparente KI-Bildbeschreibung. |
| `/blog/wie-oft-auto-aufbereiten-lassen.html` | 9 | Meta/Title präzisiert, konkrete Bedarfskriterien und Inhaltslinks; zusätzlicher Eingang aus dem Glossar. |
| `/blog/adblue-deaktivieren-vor-nachteile-wahrheit/` | 7 | Sachliche Neuausrichtung, Rechtsquelle, Diagnose-/Serviceverknüpfung; alter gleichnamiger Root-Pfad lokal weitergeleitet. |
| `/blog/wie-lange-dauert-adblue-off/` | 6 | Individueller Zeitbedarf statt pauschalem Zeitversprechen; eigene Informationsintention. |
| `/blog/boot-aufbereitung-keramikversiegelung-marine/` | 4 | Canonical-Host, Breadcrumbs und thematische Verlinkung; keine neuen Leistungsbehauptungen. |
| `/blog/auto-selber-waschen-erfurt/` | 2 | Meta/H1 verbessert, Vorbereitung und Pflegeabgrenzung ergänzt; Betreiberinformationen nicht als neu verifiziert ausgegeben. |

## Seiten mit hoher Impression aber schwacher Position

**Nicht umgesetzt als positionsbasierte Optimierung:** Positionen fehlen. Die 6.095 Impressionen des historischen AdBlue-Root-Pfads begründen die Erreichbarkeitsreparatur, aber keine Behauptung einer Position 4–20. Kein Rankingeffekt aus der lokalen Änderung ableitbar.

## Seiten mit schwacher CTR

**Nicht feststellbar:** Klicks und CTR fehlen. Titles und Descriptions wurden wegen Klarheit, Themenpassung und widersprüchlicher Aussagen verbessert. Es wurden keine CTR-Zahlen erfunden.

## Keyword-Kannibalisierung

Sieben ursprüngliche Risikogruppen bleiben als Verlauf dokumentiert; null bestätigte Ranking-Kannibalisierungsfälle mangels Query-URL-Zeitreihe.

| Gruppe | Status | Aktuelle Umsetzung / Restbedarf |
|---|---|---|
| K1 Lackhärte | umgesetzt | `/blog/harte-weiche-autolacke-lackaufbereitung/` ist kanonisches Ziel der zwei identischen Langslug-Fassungen. Alle drei URLs erhalten. Die Wahl ist eine redaktionelle Canonical-Entscheidung, kein nachgewiesener Rankinggewinner. |
| K2 Chiptuning | teilweise umgesetzt | `/chiptuning` als Leistungsangebot, Beratungsvorbereitung und Risiken als Informationsfragen; Softwareoptimierungsartikel angebunden. Breitere Textüberschneidung beobachten. |
| K3 Keramik | teilweise umgesetzt | `/luxus-aufbereitung` als Leistungsziel; Ratgeber-Metadaten differenzierter und alle zur Beratung verknüpft. Bestehende breite Textüberlappung nicht als vollständig gelöst ausgeben. |
| K4 Innenreinigung | teilweise umgesetzt | Primäres Angebot und Terminvorbereitung unterschieden; Kostenartikel angebunden. Nachfrageverteilung unbekannt. |
| K5 Autoaufbereitung | teilweise umgesetzt | `/` gestärkt, Terminvorbereitung präzisiert; `/ads` bleibt indexierbar. Kampagnenentscheidung offen. |
| K6 Leasing | teilweise umgesetzt | Leistungsberatung und Checkliste verknüpft; Grenzen einer Aufbereitung ergänzt. Keine URL zusammengelegt. |
| K7 AdBlue | teilweise umgesetzt | Inhalte nach Risiken, Rückrüstung, Zeitbedarf und Serviceangebot getrennt. Ob Google die Intentionen sauber trennt, bleibt nach Veröffentlichung zu prüfen. |

Standortseiten sind keine neue achte Risikogruppe. Verschiedene Städte bedeuten nicht automatisch identische Suchintention. Nach der Korrektur des Standorteindrucks bleiben echte lokale Belege erforderlich.

## Interne Verlinkungsprobleme

**Umgesetzt:** 42 konkrete Vorschläge aus dem Ausgangsplan; zusätzliche redaktionelle Querverbindungen und sichtbare Breadcrumbs. Leere oder irreführende Anchor wurden korrigiert. Inhaltslinks auf dunklem Hintergrund sind durch eine kleine CSS-Ergänzung heller und unterstrichen; CTA-Stile bleiben unverändert.

Keine Inhaltsseite ist vollständig verwaist. Die Google-Verifizierungsdatei bleibt bewusst unverlinkt. Die Ads-Seite und Canonical-Altvarianten werden nicht künstlich als weitere SEO-Hauptziele gepusht. Die zwei nicht umgesetzten Planlinks würden zum zurückgestellten Felgenpflege-Beitrag führen. Bestandslinks und Vorschläge sind in `internal-links.csv` getrennt; der vollständige Planabgleich steht in `link-plan-status.csv`.

## Content-Lücken

**Umgesetzt:** Trockeneisreinigung erhält eine eigenständige Leistungsseite. Unterboden ist dort ein Abschnitt, keine zusätzliche Keyword-Seite. Bestehende Artikel zu Innenreinigung, Leasingcheckliste, Motorraum und Aufbereitungsrhythmus wurden ergänzt.

**Nicht umgesetzt:** Industrie-, Graffiti- und Teile-Reinigung sind weiterhin nicht als eigene Angebote belegt. Keine neuen Preis-, Standort-, Bewertungs- oder Zertifizierungsangaben ergänzt. Große Teile der bestehenden Texte bleiben erhalten; ältere Garantie-/Preis-/Spezialfahrzeugbehauptungen werden durch diese Arbeit nicht unabhängig bestätigt.

## Neue Unterseiten

**Umgesetzt:** `/trockeneisreinigung`, Datei `trockeneisreinigung.html`, bestehendes Design und Kontakt-CTAs. Eigenständige H1/H2-Struktur, individuelle Metadaten, Self-Canonical, Service-JSON-LD, Rewrite, Sitemap und Eingang aus Startseite, Motorraumbeitrag, Blogübersicht sowie Seitenübersicht. Grundlage sind das tatsächliche vorhandene Angebot und ein klar abgegrenzter kommerzieller Bedarf; es liegt kein gemessenes Suchvolumen vor.

## Neue Ratgeber-/Blogbeiträge

**Nicht umgesetzt:** `/blog/felgenversiegelung-pflege/`. Der Content-Plan war eine Hypothese ohne Nachfragewerte. Außerdem fehlen Angaben zur verwendeten Versiegelung und deren Pflegevorgaben. Statt eines austauschbaren neuen Beitrags wurde vorhandener Content gestärkt. Es existiert kein Link zu einer nicht bereitgestellten Seite.

## Technische SEO-Punkte

**Umgesetzt:** Host-Signale vereinheitlicht, Sitemap von noindex-/Canonical-Varianten bereinigt, robots-Sperren entfernt, leere H2 entfernt, fehlende H2 vor Leistungskarten ergänzt, doppelte Markenanhänge gekürzt, genau eine H1 pro Inhaltsseite, eindeutige Titles, Alt-Text für das inhaltliche Startseitenbild ergänzt. Vorhandene Bilder und Belege blieben erhalten.

JSON-LD ist syntaktisch gültig. Artikel-Breadcrumbs stimmen mit den sichtbaren Pfaden überein. Die Service-Struktur enthält keine erfundenen Bewertungen, Preise oder Unternehmensdaten.

**Validierung:** {V['html_checked']} HTML-Routen; {V['http_checks']} lokale HTTP-Prüfungen einschließlich aller bisherigen Redirect-Muster und 23 Reparatur-Redirects mit Query-Parametern; {V['inline_js_parsed']} ausführbare Inline-JS-Blöcke geparst. Externe JS-/API-Dateien per `node --check` geprüft. Alle Source-Hashes unverändert, keine Formulare abgesendet. `package.json` enthält keinen Build-, Lint- oder Testprozess; deshalb wurden die konkreten statischen, Routing- und Schutzprüfungen durchgeführt.

Browser: Startseite und neue Leistungsseite visuell geprüft; die neue Seite zusätzlich auf schmalem Viewport. Das mobile Menü wurde geöffnet und seine Links angezeigt. Der Versand eines Formulars wurde bewusst nicht getestet. Die Prüfung verwendet eine lokale Vorschau mit gesperrtem externem Tracking; diese CSP ist keine Änderung an Produktivdateien. Kein Cloud-Deployment, keine Google-Indexierungsprüfung und keine Core-Web-Vitals-Messung.

## Maßnahmen mit geringem Risiko und hohem Potenzial

Bereits umgesetzt: konkrete Einstiegslinks, reparierte Sprungziele, verständliche Titles/Descriptions, lesbare Inhaltsanker, sinnvoll gegliederte Ratgeber und konsistente Sitemap-/Canonical-Angaben. Der nächste Nutzen entsteht durch Veröffentlichung und anschließende Kontrolle, nicht durch weitere pauschale Texterweiterung.

### TOP 10 SEO-Maßnahmen – aktueller Status

| Rang | Maßnahme / URLs | Status | Datenbasis und Ergebnis | Restpunkt |
|---:|---|---|---|---|
| 1 | 23 alte Export-URLs | umgesetzt | 6.303 historische Impressionen; lokale 308-Weiterleitungen auf passende vorhandene Inhalte geprüft | Veröffentlichung und Live-Test; `/adblue-deaktivieren/` separat entscheiden |
| 2 | www-Canonicals und Sitemap | umgesetzt | Vorhandenes Live-Endziel als Host übernommen | Google-Canonical nach Veröffentlichung prüfen |
| 3 | Startseite und Leistungscluster | umgesetzt | 42 von 44 ursprünglichen Linkvorschlägen tatsächlich als Inhaltslinks vorhanden | Zwei Links ohne veröffentlichte Zielseite bleiben zurückgestellt |
| 4 | Drei Lackhärte-Fassungen | umgesetzt | Gemeinsames Canonical-Ziel; keine URL entfernt | Google-Verarbeitung beobachten |
| 5 | AdBlue-Ratgeber und `/adblue-service` | umgesetzt | Sachliche Intentionen und Servicebezug, Teaser korrigiert | Inhaltliche Betriebsprüfung vor Veröffentlichung sinnvoll |
| 6 | K2–K6 | teilweise umgesetzt | Hauptziele und Ratgeberfragen präzisiert | Weitere Entscheidungen anhand Query-URL-Daten; Ads-Rolle offen |
| 7 | Rechts-/Funktionsseiten | umgesetzt | noindex lesbar, Sitemap bereinigt | Gewünschten Ausschluss bei Google prüfen |
| 8 | Fehlende Sprungziele / Anchor | umgesetzt | Gesamtscan: null fehlende IDs und interne Ziele | Keine offenen lokalen Fehler |
| 9 | Sechs Stadtseiten | teilweise umgesetzt | Standort Erfurt eindeutig, keine Ortsniederlassungen suggeriert | Echte ortsspezifische Inhalte fehlen |
| 10 | Trockeneis / Felgenpflege | teilweise umgesetzt | Trockeneis-Leistungsseite vorhanden; Felgenbeitrag zurückgestellt | Produkthinweise und Nachfragebeleg für Felgenthema ergänzen |

## Noch benötigte Entscheidungen

1. Soll `/adblue-deaktivieren/` auf `/adblue-service` weitergeleitet werden? Damit wird bewusst die neue Diagnose-/Reparaturausrichtung zum Nachfolger erklärt.
2. Soll `/ads` dauerhaft organisch indexierbar bleiben oder ausschließlich Anzeigenziel sein? Indexierung wurde erhalten; Ads-/Conversion-Funktionen wurden nicht verändert.

## Fünf URLs für die Search Console nach Veröffentlichung

1. `{B}/blog/adblue-deaktivieren-vor-nachteile-wahrheit/` – Redirect-Eingang vom alten Root-Pfad, Canonical und Query-Verteilung prüfen.
2. `{B}/` – bestehende Sichtbarkeit und neue interne Leistungszugänge.
3. `{B}/chiptuning` – zentrale Leistungsintention gegenüber den Ratgebern.
4. `{B}/luxus-aufbereitung` – Keramik-Hauptziel gegenüber den allgemeinen Artikeln.
5. `{B}/trockeneisreinigung` – erstmalige Indexierung und tatsächliche Suchnachfrage.

Zusätzlich bei Stichproben die historischen 404-URLs und die beiden Lackhärte-Canonicals kontrollieren. Vergleichszeiträume und Filter gleich halten; keine Query-Messungen mit historischen Seitenwerten vermischen.

## Nachweise

`seo-map.csv`, `keyword-map.csv`, `internal-links.csv`, `url-mapping.csv`, `implementation-status.csv`, `link-plan-status.csv`, `technical-inventory.md`, `validation-results.json` und `routing-compiled.json`. Vollständige Ist-Daten: `evidence.json`; Ursprungszustand unter `history/2026-09-07-analysis/`.

Fachliche Grundlagen: [Google zu Canonicals](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), [Google zu noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing), [Vercel-Konfiguration](https://vercel.com/docs/project-configuration/vercel-json), [§ 19 StVZO](https://www.gesetze-im-internet.de/stvzo_2012/__19.html), [ADAC zu Chiptuning](https://www.adac.de/rund-ums-fahrzeug/ausstattung-technik-zubehoer/zubehoer/chip-tuning-und-eco-tuning/), [Kärcher zur Trockeneisreinigung](https://www.kaercher.com/int/professional/know-how/dry-ice-blasting-in-car-workshops.html). Keine Garantie für Ranking- oder Rich-Result-Effekte.
'''
(O/'SEO-AUDIT.md').write_text(audit,encoding='utf8')

content='''# Content-Plan – Stand nach Umsetzung

Stand: 07.09.2026. Änderungen lokal, noch nicht veröffentlicht. Ausführliche ursprüngliche Briefings: [archivierter Content-Plan](history/2026-09-07-analysis/content-plan.md).

## Neue Leistungsseite: umgesetzt

- URL: `/trockeneisreinigung`; Datei: `trockeneisreinigung.html`.
- Hauptkeyword: Trockeneisreinigung Erfurt, redaktionell abgeleitet; keine gemessene Suchanfrage.
- Nebenkeywords/Themen: Trockeneisreinigung Fahrzeug, Unterboden, sensible Technikbereiche.
- Intention: Eignung einer tatsächlich angebotenen Fahrzeugreinigung verstehen und anfragen.
- Begründung: Leistung bereits auf der Startseite vorhanden; eigenständige Methode und kommerzielle Intention. Keine zusätzliche Unterboden- oder Industrie-Seite.
- H1: Trockeneisreinigung am Fahrzeug in Erfurt.
- H2: Trocken reinigen; Unterboden und sensible Bereiche; Vergleich mit Motorraumwäsche; Angaben zur Anfrage; Aufwand und Termin; Anfrage in Erfurt.
- Interne Eingänge: Startseite, Motorraumwäsche-Ratgeber, Blogübersicht und Seitenübersicht.
- Ausgänge: Motorraumwäsche, Besichtigungstermin, Kontakt, Leistungsübersicht.
- CTA: vorhandene Kontaktseite, Telefonnummer und WhatsApp-Komponente; kein neuer Formularmechanismus.
- Technik: endungslose Route über Rewrite, eindeutiger Title/Description, Self-Canonical auf www, Service-JSON-LD, Sitemap.
- Keine Annahmen über eingesetzte Geräte, Pauschalpreise, feste Dauer, Bewertungen oder garantierte Materialverträglichkeit. Technische Erklärung durch Herstellerquelle gestützt.
- Priorität: P2. Status: **umgesetzt**, Veröffentlichung ausstehend. Nachfrage und Indexierung danach prüfen.

## Felgenpflege-Ratgeber: nicht umgesetzt

- Geplante URL: `/blog/felgenversiegelung-pflege/`; keine Datei erstellt.
- Hauptkeyword-Hypothese: Felgenversiegelung pflegen.
- Intention: Nachpflege einer bereits versiegelten Felge.
- Grund für Zurückstellung: kein Nachfragebeleg; verwendete Produkte und deren Pflegevorgaben unbekannt. Die ursprüngliche Ideenliste war keine Bestätigung dieser Fakten.
- Voraussetzung für erneute Bearbeitung: tatsächliche Kundennachfragen oder passende Suchdaten sowie freigegebene Pflegehinweise zu den eingesetzten Produkten.
- Die zwei vorgesehenen internen Links wurden nicht gesetzt; es gibt keine Links ins Leere.
- Priorität: P3. Status: **nicht umgesetzt + Begründung**.

## Bestehende Inhalte: umgesetzt oder teilweise umgesetzt

| Bereich | Umsetzung | Status / Restpunkt |
|---|---|---|
| Startseite | Eindeutige H1 und Metadaten, verlinkte Leistungskacheln, Termin-/Glossarzugänge, transparente KI-Beispielbild-Beschreibung | umgesetzt |
| AdBlue | Drei Ratgeber nach Risiken/Alternativen, Rückrüstung und Zeitbedarf getrennt; Serviceangebot und Blogteaser abgestimmt | umgesetzt; fachlich vor Veröffentlichung betrieblich mitlesen |
| Chiptuning | Leistungsseite präzisiert, Beratungsdaten als eigene Frage, Risikokontext und Querverweise | teilweise umgesetzt; restliche allgemeine Textüberschneidung mit Suchdaten beurteilen |
| Keramik | Leistungsziel gestärkt; Ratgeber-Metadaten nach Fragen differenziert, Pflege-/Leistungslinks ergänzt | teilweise umgesetzt; vorhandene Garantie-/Preisangaben nicht unabhängig verifiziert |
| Innenraum | Leistungsseite und Terminvorbereitung unterschieden; Kostenfaktoren angebunden | teilweise umgesetzt; Wirkung der Abgrenzung beobachten |
| Leasing | Checkliste erhalten und ergänzt; Rückgabeberatung und Grenzen der Aufbereitung erklärt | teilweise umgesetzt; keine Zusage zur Vermeidung sämtlicher Nachzahlungen |
| Eigenwäsche / Pflegeintervall / Motorraum | Konkrete Hinweise, klarere Überschriften und passende Leistungen verknüpft | umgesetzt; vorhandene Betreiber-/Produktspezifika nicht als neu verifiziert ausgegeben |
| Lackhärte | Zwei identische Varianten kanonisch auf eine Hauptfassung bezogen; alle URLs erhalten | umgesetzt, Google-Verarbeitung offen |
| Stadtseiten | Standort Erfurt deutlich gemacht, keine erfundenen Niederlassungen; Anfragevorbereitung ergänzt | teilweise umgesetzt, echter weiterer Ortsnutzen benötigt Fakten |

## Nicht umgesetzte Erweiterungen

Keine Industrie-, Graffiti- oder eigenständigen Teile-Reinigungsseiten. Keine zusätzlichen Stadtseiten, keine generischen weiteren Keramik-/Innenreinigungs-Landingpages. Kein Ausbau bloß wegen Keywordvarianten. Neue Preise, Referenzen und Zertifizierungen wurden nicht erfunden.

## Benötigt meine Entscheidung

- Nachfolger für `/adblue-deaktivieren/`: Diagnose-/Reparaturservice oder andere inhaltliche Lösung.
- Organische Rolle von `/ads`: Indexierbarkeit wurde nicht verändert.

## Erfolgskontrolle

Nach Veröffentlichung HTTP-Endziele, Canonicals, Sitemap und noindex-Seiten prüfen. Anschließend Search-Console-Export mit Datum × Suchanfrage × Seite, Klicks, Impressionen und Positionen nutzen. Die vorhandenen Dateien enthalten weder Positionen noch CTR. Neue Messungen getrennt von den historischen 6.493 Seitenimpressionen führen. Alle aktuellen Einzelzuordnungen stehen in `keyword-map.csv`.
'''
(O/'content-plan.md').write_text(content,encoding='utf8')

data=f'''# Datenanalyse und aktueller Datenstand

Stand: 07.09.2026. Originaldateien unverändert. Website-Optimierung lokal umgesetzt, noch nicht veröffentlicht. Vollständiger Ausgangsbericht: [archivierte Datenanalyse](history/2026-09-07-analysis/data-analysis.md).

## Originaldateien

| Datei unter Datei Manager | Format | Spalten | Zeilen | Nutzung |
|---|---|---|---:|---|
| `https___www.powertech-performance.com_-Performance-on-Search-Generative-AI-Features-2026-09-07 - Seiten.csv` | UTF-8, Komma | Die häufigsten Seiten; Impressionen | 39 | Historische URL-Impressionen, 6.493 insgesamt |
| `seo-url-index.csv` | UTF-8, Semikolon | URL; Seitentitel; Thema; Hauptkeyword (vermutet); Meta Description; Indexierbarkeit; Notizen; Dateipfad | 61 | Ursprüngliches URL-/Themenmapping und 55 Keyword-Zuordnungen, 50 unterschiedliche Hypothesen |

Keine Query-Daten, Klicks, CTR, Positionen, Suchvolumina, CPC, Wettbewerb, Kosten, Conversions oder Ads-Suchbegriffe vorhanden. Diese Felder bleiben leer. Zeitraum und Filter sind unbekannt. Datum im Dateinamen vermutlich Exportdatum, kein Berichtszeitraum. Herkunft als Search-Console-/KI-Feature-Bericht aus Dateinamen vermutet, nicht unabhängig bestätigt.

## Quellenintegrität

- Impressionen-Export: `d28be8918809e9588e5779ebf2ae03cb5d8f5dd1a935886316e99ed87bb5c0f4`.
- URL-Index: `0089e5279ebbe0b88508b3626e4fed0429fb0a96a4221e308a6fc7a0dd485aa3`.
- Beide Hashes nach Umsetzung unverändert, geprüft in `validation-results.json`.
- Gleichnamige Datei im Projektstamm nicht doppelt eingelesen. Originale 61 Dateipfade existieren weiterhin. HTML-Entities werden für Vergleiche dekodiert.

## Historische Suchdaten und aktuelles Routing nicht vermischen

Die ursprüngliche HTTP-Prüfung ist eine historische Momentaufnahme in `history/2026-09-07-analysis/live-check.json` (weiterhin auch als ursprüngliches `live-check.json` vorhanden). 15 erfolgreiche Export-URLs mit 169 Impressionen hatten ein belegtes identisches Endziel. 24 URLs mit 6.324 Impressionen lieferten 404.

Jetzt sind **23 Reparatur-Redirects lokal implementiert**, zu deren Original-URLs 6.303 historische Impressionen gehören. Die übrige URL `/adblue-deaktivieren/` hat 21 Impressionen und benötigt eine Zielentscheidung. Das ist kein gemessener Sichtbarkeitsgewinn. Nach Veröffentlichung müssen diese URLs erneut live geprüft werden.

Der aktuelle www-Host folgt dem bereits vorhandenen öffentlichen Endziel. Eine alte Root-Artikel-URL und ihr neuer Blog-Nachfolger werden nicht rückwirkend zu einer Messzeile addiert. Die 6.095 Impressionen des alten AdBlue-Root-Pfads bleiben dort; die sieben Impressionen des Blogpfads bleiben beim Blogpfad.

Kontrollsummen: **169 + 6.303 + 21 = 6.493**. Auch Canonical-Altvarianten behalten ihre historischen Messwerte als einzelne Quellseiten. Keine Messwerte auf vermutete Keywords übertragen.

## Aktuelle Dateien und Zählregeln

- `seo-map.csv`: {S['seo_map_rows']} Zeilen = 63 lokale HTML-Routen (62 Inhalte + Verifizierung) + 24 historische Fehler-/Alias-URLs. Lokaler Status und historischer Live-Status stehen in getrennten Spalten.
- `keyword-map.csv`: {S['keyword_map_rows']} Zeilen = 55 vorhandene Seitenzuordnungen, eine neue Trockeneis-Zuordnung und eine zurückgestellte Felgenpflege-Idee. Ursprüngliches Keyword und aktuelles redaktionelles Keyword sind getrennt. Die Zahl der **gemessenen** Suchanfragen bleibt null.
- `internal-links.csv`: {S['internal_link_occurrences']} tatsächliche interne Link-Vorkommen plus zwei ausdrücklich zurückgestellte Vorschläge. {S['new_or_changed_link_occurrences']} Vorkommen sind neu oder gezielt verändert; das umfasst neue Breadcrumbs und geänderte Anchors, nicht ausschließlich neue Seitenverbindungen.
- `link-plan-status.csv`: alle 44 ursprünglichen Vorschläge, 42 umgesetzt und zwei nicht umgesetzt.
- `url-mapping.csv`: alle 39 Original-URLs mit Messwert, historischem Live-Status und aktuellem lokalen Routing.
- Ein-/Ausgangszahlen der Seitenmap zählen unterschiedliche Seiten ohne Selbstlinks. Die Linkmap enthält Wiederholungen, Navigation, Footer, Breadcrumbs und Sprunglinks.
- `evidence.json`: gesamter aktueller lokaler Scan mit Metadaten, H1/H2/H3, Canonicals, Links, Bildern/Alt, Abschnitten, Haupttext, Schema, Routing und Quellhashes.
- `implementation.json` und `implementation-status.csv`: Änderungen, Begründungen, offene Entscheidungen und zurückgestellte Maßnahmen.

## Sicher belegt

Die aktuellen Dateiinhalte, vorhandenen Routen, Linkziele, Quellenhashes und lokale HTTP-Ergebnisse sind direkt geprüft. {V['http_checks']} lokale GET-Tests bestanden, einschließlich vorhandener Redirectmuster und Query-Parametererhalt. Keine bestehenden Seiten wurden entfernt. Formulare und ausführbare Skriptblöcke sind gegen die Ausgangsfassung abgeglichen. Die neue Seite ist über mehrere existierende Inhaltsseiten erreichbar.

## Hypothesen und Grenzen

Keyword-Zuordnung und erwarteter Nutzen bleiben redaktionelle Einschätzungen. Es gibt keine gemessene Position 4–20, keine gemessene schlechte CTR und keine bestätigte Ranking-Kannibalisierung. Die sieben Risikogruppen aus der Analyse sind keine sieben bewiesenen Rankingprobleme. K1 wurde technisch kanonisiert; die Google-Auswahl ist weiterhin unbekannt.

Die neue Trockeneis-Leistungsseite ist aus tatsächlichem Angebot und eigenständiger kommerzieller Intention begründet, ohne Suchvolumenbehauptung. Der Felgenpflege-Ratgeber wurde mangels Nachfrage-/Produktgrundlage nicht erstellt. Vorhandene Preise, Garantien und Aussagen zu Spezialleistungen sind nicht durch diese Auswertung unabhängig bestätigt.

Kein Deployment, keine Live-Erfolgsbehauptung, kein SMTP-Testversand, kein Core-Web-Vitals-Test. Die lokale Vorschau nutzt offiziell kompilierte Vercel-Routingmuster, ersetzt aber keine Prüfung der Cloudkonfiguration. Browserkontrolle deckt exemplarische Darstellung und mobiles Menü ab, nicht jede interaktive Funktion.

## Aktualisierung

Aktuellen Stand mit `python seo/tools/scan.py` und `python seo/tools/build-reports.py` erzeugen. `build-reports.py` verwendet nach der Umsetzung den aktuellen Generator, statt alte Auditprobleme erneut als offen auszugeben. Lokale Prüfung: `python seo/tools/validate.py` bei laufender Vorschau. Redaktionelle Statusberichte: `python seo/tools/write-status-docs.py` nach erfolgreicher Prüfung.

Der einmalige Umsetzungshelfer `implement.py` ist gegen erneutes Ausführen gesperrt. Neue Änderungen werden am aktuellen Projekt vorgenommen. Das Analysearchiv bleibt historisch; aktuelle und historische Daten dürfen nicht verwechselt werden. Einen neuen Live-Check erst nach Veröffentlichung durchführen und Zeitraum/Filter neuer Search-Console-Exporte dokumentieren.
'''
(O/'data-analysis.md').write_text(data,encoding='utf8')

changed=['# Umgesetzte Änderungen je bestehender Seite','', 'Lokaler Stand, nicht veröffentlicht. Hauptdokument: SEO-AUDIT.md.','', '| URL | Änderungen |','|---|---|']
for file,notes in I['changed_pages'].items():
    if file in by:changed.append('| '+by[file]['path']+' | '+'; '.join(notes)+' |')
(O/'changes.md').write_text('\n'.join(changed)+'\n',encoding='utf8')
print('Updated audit, content plan, data analysis, implementation status and page-by-page changes.')
