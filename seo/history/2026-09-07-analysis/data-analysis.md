# Datenanalyse

Stand: 7. September 2026. Die Originaldateien werden ausschließlich gelesen.

## Gefundene Dateien

| Datei im Ordner `Datei Manager` | Format | Datensätze | Spalten | Verwendbarkeit |
|---|---|---:|---|---|
| `https___www.powertech-performance.com_-Performance-on-Search-Generative-AI-Features-2026-09-07 - Seiten.csv` | UTF-8, Komma | 39 | Die häufigsten Seiten; Impressionen | Gemessene Impressionen auf URL-Ebene. Dateiname deutet auf Search-Console-Export zu generativen KI-Suchfunktionen hin; genaue Berichtskonfiguration nicht enthalten. |
| `seo-url-index.csv` | UTF-8, Semikolon | 61 | URL; Seitentitel; Thema; Hauptkeyword (vermutet); Meta Description; Indexierbarkeit; Notizen; Dateipfad | Bestehender redaktioneller Seitenindex mit Keyword-Hypothesen; kein Ranking- oder Suchanfragenexport. Angaben werden gegen HTML geprüft. |

Der 07.09.2026 im Dateinamen ist ein vermutetes Exportdatum, kein belegter Berichtszeitraum. Beide Dateien enthalten weder Start-/Enddatum noch Länder-, Geräte- oder Suchtypfilter. Der Zeitraum ist unbekannt.

Es fehlen Suchanfragen, Klicks, CTR, durchschnittliche Position, Suchvolumen, CPC, Wettbewerb, Conversions, Kosten und Google-Ads-Suchbegriffe. Fehlende Messwerte bleiben leer; sie werden nicht als Null interpretiert. Die 55 nichtleeren Keyword-Zuordnungen ergeben 50 unterschiedliche vermutete Keywords. Es gibt **0 beobachtete Suchanfragen**. URL-Impressionen dürfen nicht auf diese Keywords übertragen werden.

Die gleichnamige Datei im Projektstamm ist eine zusätzliche Kopie und wird nicht als dritte Datenquelle gezählt. Herkunft des redaktionellen Index und Filter des Impressionen-Exports sind nicht unabhängig verifiziert.

## Integrität der Quellen

- Impressionen-Export SHA-256: `d28be8918809e9588e5779ebf2ae03cb5d8f5dd1a935886316e99ed87bb5c0f4`.
- URL-Index SHA-256: `0089e5279ebbe0b88508b3626e4fed0429fb0a96a4221e308a6fc7a0dd485aa3`.

## Zuordnung und Grenzen

Die anschließende Auswertung dokumentiert exakte URL-Treffer getrennt von Host-/Slash-Varianten und nur thematisch ähnlichen historischen Pfaden. Insbesondere ein zusätzliches `/blog/` ist keine belegte Weiterleitung. Canonicals aus HTML sind Absichtserklärungen der Website, kein Nachweis der von Google gewählten kanonischen URL oder einer erfolgreichen Indexierung.

## Ergebnis des vollständigen Imports und der Website-Verknüpfung

- 39 eindeutige Export-URLs, keine doppelten URL-Zeilen, Summe **6.493 Impressionen**. Dies ist die Summe des gelieferten Ausschnitts, kein verifiziertes Search-Console-Gesamtergebnis. Es fehlen Berichtfilter und eventuell weitere Exporttabs.
- 61 eindeutige URL-/Dateipfad-Zeilen im Seitenindex; alle Dateien existieren. 55 Keyword-Zuordnungen, 50 verschiedene vermutete Keywords; sechs Funktions-/Rechtsseiten ohne Keyword. Die ursprünglichen Keywords wurden als Hypothesen erhalten. Zwei neue Planungshypothesen wurden getrennt ergänzt, daher 57 Zeilen in `keyword-map.csv` und 52 verschiedene Begriffe einschließlich der neuen Ideen.
- Beide Dateien sind UTF-8 und enthalten keine Unicode-Ersatzzeichen. Der Seitenindex enthält teilweise HTML-Entities wie `&amp;` in Descriptions. Der Vergleich dekodiert Entities; daraus wird keine inhaltliche Änderung abgeleitet. Quellspalten und Originalwerte sind in `evidence.json` erhalten.
- Die Datei `seo-url-index.csv` im Projektstamm hat denselben SHA-256 wie die Kopie in `Datei Manager`; sie wird nicht doppelt eingelesen.
- Lokaler Scan: 62 HTML-Dateien = 61 Inhaltsseiten + eine Google-Verifizierungsdatei. Keine HTML-Inhaltsseite wurde ausgelassen. Abhängigkeiten in `node_modules` und Git-Metadaten sind keine Website-Seiten. Physische Root-HTML-Dateien werden anhand der vorhandenen Rewrites ihren öffentlichen Pfaden zugeordnet; Blog-index.html wird als Verzeichnispfad erfasst. Die vollständigen Rewrite-/Redirect-Muster stehen in `evidence.json`.
- **0 buchstabengetreue URL-Treffer** zwischen www-Export und non-www-Projekt-URLs. Daher zusätzlicher HTTP-Abgleich statt stiller Host-Normalisierung.
- **15 Export-URLs mit 169 Impressionen** haben dasselbe erfolgreiche Live-Endziel wie die entsprechende Projekt-URL. Nur diese Messwerte wurden auf die bestehende Projektseite übertragen. Beispiel: www-Startseite 130 Impressionen; non-www-Startseite leitet nachweislich exakt dorthin.
- **24 Export-URLs mit 6.324 Impressionen** sind aktuell 404. Davon 18 nicht vorhandene historische Root-Pfade und sechs nicht funktionierende Slash-Varianten bestehender endungsloser Seiten. Diese Kennzahlen bleiben an der Original-URL. Mögliche Zielseiten sind ausschließlich Prüfungsvorschläge.
- Die 24 nicht zugeordneten Mess-URLs stehen zusätzlich als eigene Zeilen in `seo-map.csv`: 62 lokale Routen + 24 Fehler-URLs = **86 Zeilen**. Erfolgreiche www-Varianten sind als Messwertquelle/Live-Endziel der lokalen Zeile sichtbar und werden dort nicht doppelt gezählt. Der unveränderte Rohbestand aller 39 Export-URLs steht in `url-mapping.csv`.
- Kontrollsumme: **169 + 6.324 = 6.493**. Keine Messwertübertragung zwischen alter Root-URL und heutigem `/blog/`-Kandidaten. Kein Query-CTR-/Positionswert berechnet.

## Öffentliche HTTP-Prüfung

103 verschiedene Adressen geprüft: 62 lokale Routen, 39 www-Exportadressen sowie robots.txt und sitemap.xml. Ergebnis nach Verfolgung tatsächlicher Redirectketten: 79 Antworten mit Status 200, 24 mit Status 404. Alle lokalen Routen waren erreichbar. Die Live-Titel aller lokalen HTML-Dateien stimmten mit dem lokalen Stand überein. Das bestätigt keine vollständige Inhaltsidentität oder korrekte Google-Indexierung.

Die Prüfung verwendet öffentliche GET-Abfragen ohne Formulare, Cookies, JavaScript oder Tracking. Pro URL werden Status, endgültige Adresse, Redirectschritte, Title, H1, Canonical, robots-Meta und X-Robots-Tag gespeichert. Der UTC-Prüfzeitpunkt steht in `live-check.json`. Es handelt sich um eine Momentaufnahme aus dieser Umgebung, nicht um Uptime-Monitoring oder die Googlebot-Perspektive.

## Sichere Feststellungen

Dateinamen, Formate, Spalten, Zeilenanzahlen, unveränderte Hashes, tatsächliche HTML-Metadaten/Überschriften/Links, vorhandene Leistungen im Wortlaut, deklarierte Canonicals/noindex, robots-Regeln und Sitemap-Einträge sind direkt belegt. Die drei Lackhärte-Artikel haben exakt gleichen extrahierten Haupttext. Alle sechs Stadtseiten sind nach Ortsersetzung im Haupttext identisch. Die HTTP-Statuswerte und Redirectketten sind zum Prüftermin beobachtet.

Die Website **nennt** Leistungen und bestimmte Preise/Garantien/Zertifizierungen. Diese Nennung ist keine unabhängige Bestätigung der Tatsachen. Keine solchen Angaben wurden neu erfunden oder als verifiziert in den Maßnahmenplan übernommen.

## Hypothesen und nicht mögliche Aussagen

- Herkunft als Search-Console-/KI-Feature-Bericht aus dem Dateinamen vermutet, aber Berichtstyp und Filter nicht verifiziert. Nicht automatisch als vollständigen organischen Suchbericht behandeln.
- Berichtszeitraum, Query-Nachfrage, Suchvolumen, Kosten und Conversions unbekannt.
- Kein Nachweis schlechter Positionen, niedriger CTR, verlorener Klicks, URL-Wechsel über die Zeit oder verdrängter Hauptseiten möglich.
- 50 ursprüngliche Keywords sind ausdrücklich vermutet; zwei zusätzliche Begriffe sind redaktionelle Planung. Kein Keyword besitzt eine gemessene Impressionenzahl. Die Zusatzspalte `URL-Impressionen (nicht Keyword-Messwert)` enthält nur eindeutig zugeordnete Seitenwerte und ist nicht über Keyword-Zeilen zu aggregieren.
- Sieben Cannibalisierungsgruppen sind redaktionelle Risiken. Eine davon hat bestätigte Inhaltsduplikate, aber keine bestätigte Ranking-Kannibalisierung. Themenähnlichkeit und ein identischer Text sind unterschiedliche Evidenzstärken.
- Historische URL-Zielgleichheit ist vor Redirects inhaltlich zu prüfen. Eine gleiche Slug-Zeichenfolge allein beweist sie nicht.
- Keine Behauptung über Core Web Vitals, Rich-Result-Berechtigung oder Indexierung durch Google. Die statische Erfassung ersetzt keinen gerenderten Browser-Test.

## Dauerhafte Nutzung und Zählregeln

`seo/SEO-RULES.md` beschreibt den Aktualisierungsablauf. Die ergänzenden Skripte schreiben nur Auswertungen im SEO-Ordner. Originaldateien und Website werden nicht angefasst. Die drei CSVs sowie `url-mapping.csv` verwenden UTF-8 mit BOM und Semikolon, Felder werden korrekt gequotet.

Seitenmap: ein-/ausgehende **unterschiedliche Seiten**, keine Selbstlinks. Linkmap: **893 einzelne Link-Vorkommen** einschließlich Navigation, Footer, Breadcrumbs, Selbst-/Sprunglinks und Wiederholungen; zusätzlich 44 deutlich markierte Vorschläge. Keywordmap: eine Zeile pro vorhandener Seiten-/Keyword-Zuordnung statt künstlicher Zusammenfassung mehrerer konkurrierender URLs. Haupttext wird aus `.article-body`, sonst `main`, sonst `body` extrahiert; Script-/Style-/noscript-Text entfernt. Wortzahlen sind technische Hilfswerte, kein Qualitätsmaß.

Die sieben angeforderten Kerndokumente sind erstellt. Ergänzend erleichtern `url-mapping.csv`, `technical-inventory.md`, `evidence.json`, `live-check.json`, `summary.json` und die Skripte die Prüfung und Wiederholung. Das neue Root-`AGENTS.md` verweist künftige SEO-Arbeiten verbindlich auf das Regelwerk; es verändert keine Website-Funktion.
