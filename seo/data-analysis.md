# Datenanalyse und aktueller Datenstand

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

- `seo-map.csv`: 87 Zeilen = 63 lokale HTML-Routen (62 Inhalte + Verifizierung) + 24 historische Fehler-/Alias-URLs. Lokaler Status und historischer Live-Status stehen in getrennten Spalten.
- `keyword-map.csv`: 57 Zeilen = 55 vorhandene Seitenzuordnungen, eine neue Trockeneis-Zuordnung und eine zurückgestellte Felgenpflege-Idee. Ursprüngliches Keyword und aktuelles redaktionelles Keyword sind getrennt. Die Zahl der **gemessenen** Suchanfragen bleibt null.
- `internal-links.csv`: 1067 tatsächliche interne Link-Vorkommen plus zwei ausdrücklich zurückgestellte Vorschläge. 298 Vorkommen sind neu oder gezielt verändert; das umfasst neue Breadcrumbs und geänderte Anchors, nicht ausschließlich neue Seitenverbindungen.
- `link-plan-status.csv`: alle 44 ursprünglichen Vorschläge, 42 umgesetzt und zwei nicht umgesetzt.
- `url-mapping.csv`: alle 39 Original-URLs mit Messwert, historischem Live-Status und aktuellem lokalen Routing.
- Ein-/Ausgangszahlen der Seitenmap zählen unterschiedliche Seiten ohne Selbstlinks. Die Linkmap enthält Wiederholungen, Navigation, Footer, Breadcrumbs und Sprunglinks.
- `evidence.json`: gesamter aktueller lokaler Scan mit Metadaten, H1/H2/H3, Canonicals, Links, Bildern/Alt, Abschnitten, Haupttext, Schema, Routing und Quellhashes.
- `implementation.json` und `implementation-status.csv`: Änderungen, Begründungen, offene Entscheidungen und zurückgestellte Maßnahmen.

## Sicher belegt

Die aktuellen Dateiinhalte, vorhandenen Routen, Linkziele, Quellenhashes und lokale HTTP-Ergebnisse sind direkt geprüft. 135 lokale GET-Tests bestanden, einschließlich vorhandener Redirectmuster und Query-Parametererhalt. Keine bestehenden Seiten wurden entfernt. Formulare und ausführbare Skriptblöcke sind gegen die Ausgangsfassung abgeglichen. Die neue Seite ist über mehrere existierende Inhaltsseiten erreichbar.

## Hypothesen und Grenzen

Keyword-Zuordnung und erwarteter Nutzen bleiben redaktionelle Einschätzungen. Es gibt keine gemessene Position 4–20, keine gemessene schlechte CTR und keine bestätigte Ranking-Kannibalisierung. Die sieben Risikogruppen aus der Analyse sind keine sieben bewiesenen Rankingprobleme. K1 wurde technisch kanonisiert; die Google-Auswahl ist weiterhin unbekannt.

Die neue Trockeneis-Leistungsseite ist aus tatsächlichem Angebot und eigenständiger kommerzieller Intention begründet, ohne Suchvolumenbehauptung. Der Felgenpflege-Ratgeber wurde mangels Nachfrage-/Produktgrundlage nicht erstellt. Vorhandene Preise, Garantien und Aussagen zu Spezialleistungen sind nicht durch diese Auswertung unabhängig bestätigt.

Kein Deployment, keine Live-Erfolgsbehauptung, kein SMTP-Testversand, kein Core-Web-Vitals-Test. Die lokale Vorschau nutzt offiziell kompilierte Vercel-Routingmuster, ersetzt aber keine Prüfung der Cloudkonfiguration. Browserkontrolle deckt exemplarische Darstellung und mobiles Menü ab, nicht jede interaktive Funktion.

## Aktualisierung

Aktuellen Stand mit `python seo/tools/scan.py` und `python seo/tools/build-reports.py` erzeugen. `build-reports.py` verwendet nach der Umsetzung den aktuellen Generator, statt alte Auditprobleme erneut als offen auszugeben. Lokale Prüfung: `python seo/tools/validate.py` bei laufender Vorschau. Redaktionelle Statusberichte: `python seo/tools/write-status-docs.py` nach erfolgreicher Prüfung.

Der einmalige Umsetzungshelfer `implement.py` ist gegen erneutes Ausführen gesperrt. Neue Änderungen werden am aktuellen Projekt vorgenommen. Das Analysearchiv bleibt historisch; aktuelle und historische Daten dürfen nicht verwechselt werden. Einen neuen Live-Check erst nach Veröffentlichung durchführen und Zeitraum/Filter neuer Search-Console-Exporte dokumentieren.
