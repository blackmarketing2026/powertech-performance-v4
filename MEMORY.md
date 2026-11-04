# Projektgedächtnis – Powertech Performance

## Nutzung

Auf ausdrücklichen Nutzerwunsch vom 31.10.2026: vor jeder Arbeit lesen und nach abgeschlossenen Arbeiten fortschreiben. Entscheidungen und Ergebnisse knapp und nachvollziehbar dokumentieren; Datum, betroffene Dateien, Prüfungen, lokale Commits, Veröffentlichungsstand und offene Punkte nennen. Keine Geheimnisse oder Zugangsdaten speichern. Frühere Einträge sind Verlauf, keine pauschale Freigabe für neue Aktionen. Aktuelle Nutzeranweisungen haben Vorrang.

## Projekt

- Website: https://www.powertech-performance.com/
- Repository: https://github.com/blackmarketing2026/powertech-performance-v4
- Lokaler Ordner: `C:/Users/Steve/Documents/Codex/2026-10-31/github/powertech-performance-v4`
- Statische HTML-Seiten, gemeinsame CSS-/JavaScript-Dateien, Vercel-Routing, Formularversand über `/api/send-lead`.
- Weitere verbindliche Hinweise: `AGENTS.md`, `seo/SEO-RULES.md`, `seo/business-policy.json`.

## 31.10.2026 – Projekt heruntergeladen

- Nutzer möchte hier weiterarbeiten, weil VS Code nicht funktioniert.
- Repository vollständig einschließlich Versionsverlauf geklont; Basis: `main`, Commit `498db6d`.

## 31.10.2026 – AdBlue-/NOx-Seite überarbeitet

- Nutzerauftrag: bestehende Seite `/adblue-diagnose-erfurt/` auf Auskodierung von AdBlue-Systemen und NOx-Sensoren für PKW, Transporter, Camper und Wohnmobile ausrichten. Kostenloses Angebot als zentrale Handlungsaufforderung. Hinweis auf Erlöschen der Betriebserlaubnis und Anpassung an das neue Design-Schema.
- Umsetzung: `adblue-diagnose-erfurt.html`, neue seitenspezifische `css/adblue.css`. Helle Gestaltung mit bestehenden Pflaumen-/Lilatönen, angepasste Leistungen, Fahrzeugkarten, Ablauf, Angebotsformular-Texte, FAQ, Metadaten und strukturierte Daten.
- Betriebserlaubnis-Hinweis im Einstieg, am Formular, im Rechtsabschnitt, in FAQ und Footer. Kein Betrieb im öffentlichen Straßenverkehr nach emissionsverschlechternder Auskodierung. Quelle auf der Seite: https://www.gesetze-im-internet.de/stvzo_2012/__19.html
- Vorhandene Begrenzung bis Baujahr 2021 beibehalten; individuelle technische Prüfung statt pauschaler Machbarkeitszusage.
- Die ausdrückliche neue Nutzeranweisung ersetzt für diese Seite die ältere Diagnose-Beschränkung. Dokumentiert in `AGENTS.md`, `seo/SEO-RULES.md` und `seo/business-policy.json` unter `page_override_2026_10_31`. Keine Erweiterung auf AGR, DPF oder Chiptuning.
- SEO-Zuordnungen in `seo/implementation.json`, `seo/keyword-map.csv` und `seo/seo-map.csv` aktualisiert. Historische Messwerte und Exporte erhalten.
- Bestehende URL, ausführbare Skripte, Formularfelder, Versand-Endpunkt und Telefon-/WhatsApp-Ziele erhalten. Keine Testanfragen versendet.
- Prüfung bestanden: Browseransicht bei 1440, 390 und 320 Pixel Breite ohne seitliche Überläufe oder JavaScript-Fehler; Angebots-Sprunglink und FAQ geprüft. H1, Sprungziele, lokale Assets, JSON-LD und Übereinstimmung sichtbarer FAQ mit Schema geprüft. `git diff --check` bestanden.
- Die eingecheckte `seo/routing-compiled.json` ist gegenüber `vercel.json` veraltet. Daher lokale Browserprüfung direkt über die HTML-Datei durchgeführt; das bestehende Rewrite in `vercel.json` für die öffentliche URL wurde bestätigt. Routing nicht verändert.
- Vorschau: `../outputs/adblue-vorschau.png`. Prüfskripte und weitere Screenshots liegen außerhalb des Repositorys unter `../work/`.
- Lokal gesichert als Commit `a37aedb` (`Update AdBlue and NOx service offer with light design and legal notices`). **Nicht gepusht und nicht veröffentlicht.** Keine Veröffentlichung in diesem Chat autorisiert.

## 31.10.2026 – Dauerhaftes Markdown-Gedächtnis eingerichtet

- `MEMORY.md` angelegt und bisherige Arbeit nachgetragen.
- Lese- und Aktualisierungspflicht in Projekt- und Arbeitsordner-`AGENTS.md` ergänzt.
- Reine Dokumentationsänderung; keine zusätzliche Website-Änderung und keine Veröffentlichung.

## 31.10.2026 – Push freigegeben

- Nutzer hat mit „bitte pushen“ den Upload des aktuellen Stands auf GitHub ausdrücklich autorisiert.
- Umfang: Website-Commit `a37aedb` und Projektdokumentation (`AGENTS.md`, `MEMORY.md`). Vorhandene Desktop-/Mobilprüfungen bestanden; keine erneute Inhaltsänderung. `git diff --check` vor Push bestanden.
- Erfolgreich auf `origin/main` gepusht: Website-Commit `a37aedb` und Dokumentations-Commit `56a1c34`.
- Öffentliche Prüfung nach kurzer Bereitstellungszeit bestanden: `/adblue-diagnose-erfurt/` antwortet mit HTTP 200 und enthält das neue NOx-Angebot, `/css/adblue.css` sowie den hervorgehobenen Betriebserlaubnis-Hinweis. Die neue Version ist damit öffentlich ausgeliefert. Keine Formular-Testanfrage versendet; keine zusätzliche Live-Browserprüfung durchgeführt.
- Die früheren Angaben „nicht veröffentlicht“ oben beschreiben den damaligen Stand und sind durch diesen Veröffentlichungseintrag überholt.

## 04.11.2026 – Du-Ansprache auf der gesamten Website

- Aktuelle ausdrückliche Nutzerentscheidung: Alle öffentlich sichtbaren Texte einschließlich Angebotsseiten, Blog, Cookie-Hinweisen und Rechtstexten verwenden die Du-Form. Die Regel steht nun auch in `AGENTS.md`. Grammatische Bezüge auf Dinge oder Dritte mit „Sie“ bleiben erhalten.
- 51 HTML-Dateien sowie `js/main.js` und `js/blog-promo.js` redaktionell umgestellt. Formulare, Tracking, URLs und Angebote nicht funktional verändert. Die bereits auf GitHub vorhandene AdBlue-Seite wurde für die reine Anspracheänderung als Ausgangsstand übernommen.
- Geprüft: direkte Anreden in HTML-Texten und Attributen, JSON-LD, Linkziele, Formularfelder, ausführbare Skriptblöcke, JavaScript-Syntax, `git diff --check` sowie Browser-Stichproben bei schmaler Breite. Keine Testanfragen versendet.
- `python seo/tools/validate.py` meldete Fehler aus der älteren Funktionsbaseline und fehlender Routing-Vorschau; der fokussierte Strukturvergleich gegen `origin/main` zeigte keine veränderten Formulare, ausführbaren Skripte oder Linkziele.
- Über die verbundene GitHub-App auf `main` veröffentlicht: Commit `d916722c56f41d1027315b732305aff17a0a2941`. Öffentliche GET-Stichproben für Startseite, Autoaufbereitung, Datenschutz und einen Blogartikel antworteten mit HTTP 200 und zeigten die Du-Ansprache. Kein lokaler Commit für dieses Paket.

## 04.11.2026 – SEO-Datenbedarf und nächste Schritte

- SEO-Regeln, Datenanalyse und bestehende Seiten- und Keyword-Zuordnungen für eine Beratung zum weiteren Rankingwachstum berücksichtigt. Historische Impressionen haben keinen gesicherten Berichtszeitraum; aktuelle Suchanfragen, Klicks, CTR und Positionen fehlen in der dokumentierten Datenbasis. Zuordnungen sind Hypothesen, keine Rankingnachweise.
- Empfohlen: aktuelle Search-Console-Exporte und Indexierungsansichten, ergänzend Daten des Google-Unternehmensprofils und vorhandene Anfragezahlen; danach Priorisierung bestehender Kernleistungsseiten und gezielte Prüfung. Keine Website-, Tracking- oder Routingänderungen und kein Commit oder Push; Veröffentlichung unverändert. Offen: aktuelle Daten und Ergebnisse der Auswertung.

## 04.11.2026 – Search-Console-Auswertung Autoaufbereitung

- Nutzerziel: mehr passende Anfragen für Autoaufbereitung, insbesondere Leasingrückläufer. Gelieferten Search-Console-ZIP (Web, 03.08.–02.11.2026), Sitemap-Text und Screenshot der Seitenindexierung ausgewertet; Originaldatei unverändert gelassen. Diagramm: 1.459 Klicks, 38.401 Impressionen; URL- und Query-Daten getrennt bewertet. Suchanfragen-Export auf 1.000 Zeilen begrenzt, keine Query-URL-Zeitreihe.
- Beispiele: „fahrzeugaufbereitung erfurt“ 606 Impressionen/4 Klicks, „autoaufbereitung erfurt“ 195/2; „leasingrückgabe aufbereitung“ 76/0. Eigene URL /autoaufbereitung/ 22/0; Leistungsseite Leasing im Zeitraum nicht als eigene Zeile aufgeführt. Historischer Leasing-Blogpfad 183/2, leitet bei öffentlicher GET-Prüfung aktuell auf die Leistungsseite; die Werte nicht als Messwerte des Ziels ausgeben.
- Öffentliche Leasing-Leistungsseite antwortet 200, enthält jedoch sichtbare Fragezeichen anstelle von Umlauten im Einstiegsbereich; lokale Datei zeigt denselben Befund. Screenshot allein erlaubt keine Zuordnung der 404- und Indexierungskategorien zu URLs. Sitemap-Inhalt zeigt keine Search-Console-Verarbeitungsbestätigung. Google-Unternehmensprofil-Daten fehlen.
- Priorität: Textfehler und Indexierung der Kernseiten prüfen, Leasing- und Autoaufbereitungsseiten anhand echter Angebote und Referenzen verbessern; keine Rankinggarantie. Keine Websiteänderungen, kein Commit oder Push; Veröffentlichung unverändert. Offen: URL-Listen aus Indexierungsberichten, URL-Prüfung der Kernseiten, Unternehmensprofil und bestätigte Leistungs-/Preisdetails.

## 04.11.2026 – SEO-Verbesserungen für Fahrzeugaufbereitung

- Nutzerauftrag: Ranking und Anfragen für Autoaufbereitung und Leasingrückgabe verbessern; Startseite nicht verändern. In `leasingrueckgabe-aufbereitung-erfurt.html` beschädigte Umlaute repariert, Einstieg auf Leasingrückläufer ausgerichtet und Kosten, Anfrageablauf sowie Grenzen erläutert. `autoaufbereitung.html` nennt konkrete Anlässe und verlinkt im passenden Kontext zur Leasingseite. `css/autoaufbereitung.css` lässt Breadcrumbs bei schmalen Displays umbrechen; Startseite bindet dieses Stylesheet nicht ein. `seo/data-analysis.md` dokumentiert Export, Hash, getrennte Messwerte und Einschränkungen.
- Geprüft: `git diff --check`, jeweils eine H1, eindeutige IDs, Sprungziele, Canonical und JSON-LD; Formulare und Skripte gegenüber Ausgangsstand unverändert. Browserprüfung beider Seiten bei 1440, 390 und 320 Pixeln ohne Überlauf oder JavaScript-Seitenfehler, externe Ressourcen lokal blockiert. Startseitendatei unverändert. Keine Formular-Testanfrage.
- Website und Datenanalyse lokal in Commit `a573ac2` gesichert; nicht gepusht oder veröffentlicht. Offene Punkte: Search-Console-URL-Prüfung und Indexierungslisten, Unternehmensprofil, belastbare Vorher-nachher-Fotos und bestätigte Preisrahmen; Rankingwirkung erst nach Veröffentlichung und Beobachtung messbar. Bereits vorher bestehende Änderungen an `seo/validation-results.json` und unversionierte Dateien nicht angetastet.

## 04.11.2026 – SEO-Paket veröffentlicht und Briefing ergänzt

- Nutzer hat den Push ausdrücklich freigegeben und um einen Bericht über alle geänderten Seiten sowie die Anpassung der Regeln an das neue Briefing gebeten. `AGENTS.md` und `seo/SEO-RULES.md` priorisieren passende Anfragen für Autoaufbereitung und Leasingrückgabe, belegte Angebote und die getrennte Bewertung von Sichtbarkeit und Anfragen. Die Startseite bleibt für dieses Paket unverändert.
- Commits `a573ac2`, `39eeec1` und `818c39c` auf `origin/main` gepusht. Öffentliche GET-Prüfung nach Bereitstellung: `/autoaufbereitung/`, `/leasingrueckgabe-aufbereitung-erfurt/` und `/css/autoaufbereitung.css` HTTP 200 mit den jeweiligen Änderungen. Kein Live-Formularversand getestet. Die offenen Search-Console- und Betriebsdaten sowie die spätere Erfolgsmessung bleiben bestehen.

## 04.11.2026 – Ideen für zusätzliche SEO-Seiten

- Nutzer wünscht zunächst Ideen, keine Umsetzung. Bestehenden Seitenbestand, Suchdaten vom 03.08.–02.11.2026 und beispielhafte lokale Suchergebnisse berücksichtigt. Schwerpunkte als Hypothesen: Verkaufsaufbereitung, Tierhaare, Gerüche und nachvollziehbare Kundenprojekte; Kosten- und Leasingfragen zunächst mit vorhandenen Seiten abgleichen. Einzelne Suchanfragen mit wenigen Impressionen belegen kein Suchvolumen oder regionale Nachfrage. Fachliche Betriebsdaten und echte Beispiele sind für neue Seiten erforderlich.
- Keine Website-, Routing- oder Trackingänderung, kein Commit oder Push. Offen: Nutzerentscheidung zu Ideen, Betriebsdetails, Search-Console-Indexierungsprüfung und Erfolgsmessung.

## 04.11.2026 – Vier neue Themen zur Fahrzeugaufbereitung

- Nutzer beauftragte die Umsetzung der vorgeschlagenen Ideen. Er bestätigte Firmenfahrzeug-Anfragen über Kontaktformular, Telefon und WhatsApp mit persönlicher Abstimmung durch Benjamin; echte Vorher-nachher-Bilder und Falldaten sind aktuell nicht vorhanden.
- Vier neue Ratgeberseiten in `blog/`: `autoaufbereitung-vor-verkauf-erfurt`, `tierhaare-auto-entfernen-erfurt`, `geruch-im-auto-innenraumreinigung-erfurt` und `firmenfahrzeuge-autoaufbereitung-erfurt`. Passende Links in Ratgeberübersicht, Autoaufbereitungs- und Innenraumleistungsseite; Sitemap mit vorgesehenem Generator erstellt. Inhalte und Zuordnung in `seo/ideen-umsetzung-2026-11-04.md` dokumentiert. Kein Vorher-nachher-Projekt erfunden; bleibt offen.
- Geprüft: je eine H1, Canonical, parsebares JSON-LD, Sitemap und Kontaktlink; alle vier neuen Seiten lokal bei 1440, 390 und 320 Pixeln ohne Überlauf oder JavaScript-Seitenfehler, externe Ressourcen blockiert. Vorhandene Formulare und Skripte auf geänderten Bestandsseiten unverändert, Startseite unverändert. Keine Testanfrage gesendet. `git diff --check` geprüft. Kein Push für dieses neue Paket beauftragt; Veröffentlichung steht aus. Bereits vorhandene Änderung an `seo/validation-results.json` und unversionierte Hilfsdaten nicht Bestandteil.
