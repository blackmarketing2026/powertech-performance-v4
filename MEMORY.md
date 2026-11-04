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
