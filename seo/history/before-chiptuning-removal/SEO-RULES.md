# Verbindliche SEO-Grundlage für Powertech Performance

Stand: 07.09.2026 nach lokaler Umsetzung, noch nicht veröffentlicht. Diese Regeln gelten für weitere SEO-Arbeiten. Aktuelle Nutzeranweisungen haben Vorrang. Die Ausgangsanalyse bleibt unter `history/2026-09-07-analysis/` erhalten.

## Bestand und Architektur

Statische HTML-Website mit Vercel-Rewrites, Vanilla-JavaScript und Node-Serverless-Formularversand. Bestand: 62 Inhaltsseiten, darunter 39 Blogartikel und eine Blogübersicht, plus eine Google-Verifizierungsdatei. Primärquellen: echte HTML-Dateien, `vercel.json`, `robots.txt` und `sitemap.xml`. Der alte CSV-Index ist eine Arbeitsannahme und darf HTML-Befunde nicht überschreiben.

Bestehende Pfadfamilien:

- `/` für die Startseite.
- Endungslose Root-Pfade wie `/adblue-service`, `/chiptuning`, `/luxus-aufbereitung` und Stadtseiten, über 15 explizite Rewrites auf Root-HTML-Dateien.
- `/blog/<slug>/` für die meisten Artikel mit physischer `index.html`.
- Historische Ausnahme `/blog/wie-oft-auto-aufbereiten-lassen.html` unverändert erhalten.
- `/pages/<name>.html` für Kontakt-, Rechts- und Funktionsseiten.
- Bestehende Schreibweise `/glosar` erhalten. Keine automatische Korrektur in `/glossar`.

Der vorhandene Live-Host ist www. Canonicals, URL-Metadaten, JSON-LD und Sitemap sind lokal auf `https://www.powertech-performance.com` vereinheitlicht. Die Host-Konfiguration blieb unverändert. 23 eindeutige historische URL-Varianten erhalten gezielte Redirects, dazu zwei Varianten der neuen Trockeneis-Seite. Insgesamt 67 Redirects und 15 Rewrites. Keine pauschale Slash-Normalisierung: Root- und Artikelpfade unterscheiden sich. `/adblue-deaktivieren/` bleibt bis zur Zielentscheidung offen. Die Veröffentlichung steht aus.

## Daten und Keyword-Zuordnung

`seo-map.csv` ist der vollständige Seiten-/Problemindex, `keyword-map.csv` die Arbeitszuordnung und `url-mapping.csv` der belegte Import-Join. Leere Kennzahlen bedeuten fehlend, nicht null. Seitenimpressionen niemals als Keyword-Impressionen ausgeben. Exportdatum niemals als Berichtszeitraum interpretieren. Query-/Seiten-/Datumsdimensionen und Filter getrennt erhalten. Host, Slash oder `/blog/` nicht stillschweigend umschreiben.

Ein primäres Ziel pro **Suchintention** festlegen; mehrere unterschiedliche Informationsfragen innerhalb eines Clusters bleiben zulässig. Die im aktuellen Mapping genannten Hauptziele sind redaktionelle Vorschläge, keine aus Rankings ermittelten Gewinner. Vor tiefgreifenden Änderungen Query-URL-Daten und Google-Canonical ergänzen.

| Cluster | Primäres Arbeitsziel | Abgrenzung |
|---|---|---|
| Autoaufbereitung Erfurt | `/` | Angebot/Orientierung; `/ads` auf Kampagnenrolle prüfen, Tracking unverändert. |
| Chiptuning | `/chiptuning` | Leistungsanfrage; vorhandene Blogartikel nach eigenen Informationsfragen abgrenzen. |
| AdBlue / SCR | `/adblue-service` | Tatsächlich belegtes Diagnose-/Reparaturangebot; fachlich abgestimmte Ratgeber separat. |
| Keramikversiegelung | `/luxus-aufbereitung` | Angebot; Haltbarkeit als eigener Informationsbeitrag. |
| Innenreinigung | `/blog/innenreinigung-auto-in-der-naehe/` | Vorläufig vorhandene Zielseite; Kostenbeitrag hat eigene Informationsintention. |
| Lackhärte | `/blog/harte-weiche-autolacke-lackaufbereitung/` | Kanonische Hauptfassung; die zwei langen Slugs bleiben erreichbar und referenzieren diese per Canonical. Google-Auswahl noch nicht bestätigt. |
| Lackkorrektur | `/blog/lackkorrektur-wofuer-gut-werterhalt/` | Nutzen; Politurvergleich als vertiefende Frage. |
| Leasingaufbereitung | `/blog/leasing-rueckgabe-aufbereitung-erfurt/` | Leistungsberatung; Checkliste bleibt Hilfsinhalt. |
| Motorraumwäsche | `/blog/motorwaesche-erfurt-vorteile-kosten/` | Bestehende Seite vor Ausbau des Clusters verbessern. |
| Trockeneisreinigung | `/trockeneisreinigung` | Fahrzeugbezug belegt; keine automatische Ausweitung auf Industrie. |
| Felgenpflege | derzeit `/#leistungen` | Ratgeber mangels ausreichender Such-/Produktdaten nicht erstellt; erst mit belegter eigener Informationsfrage neu bewerten. |
| Einzugsgebiet | `/` plus sechs bestehende Stadtseiten | Kundenherkunft, keine behaupteten Niederlassungen. |

## Neue Seiten

Vor Erstellung Bestand, Intention, Leistungen und Kannibalisierungsgruppen prüfen. Nur ein eigenständiges Nutzerproblem rechtfertigt eine neue URL. Bei gleicher Intention zunächst bestehenden Content erweitern. Für jede neue Seite Hauptkeyword-Hypothese, Nutzerfrage, H1/H2-Plan, eigene Belege, ein-/ausgehende Links, vorgesehenen Pfad und Priorität dokumentieren.

Für neue Leistungsseiten die endungslose Root-Architektur, für neue Ratgeber `/blog/<slug>/` verwenden, sofern eine spätere ausdrückliche Architekturentscheidung nichts anderes vorgibt. Physische Datei, Rewrite, Canonical, Linkziel und Sitemap müssen zusammenpassen. Keine Slugs allein wegen Keywordvarianten erzeugen. Technische Bereitstellung erst im autorisierten Umsetzungsschritt.

## Interne Verlinkung und Anchor-Texte

Wichtige Leistungsseiten direkt aus einer crawlbaren Leistungsübersicht und relevanten Fachinhalten verlinken. Die nicht indexierbare Seitenübersicht darf niemals der einzige Zugang sein. Als redaktionelles Prüfziel mindestens zwei sinnvolle unterschiedliche Quellseiten für wichtige Ziele anstreben; dies ist eine Projektregel, keine Google-Mindestzahl.

Pro Link Quelle, Ziel, Anchor und Kontext dokumentieren. Links mit echten `href`-Attributen verwenden. Neue Seiten erst nach Bereitstellung verlinken. Im Haupttext Zielthema verständlich benennen, keine mechanische Wiederholung exakter Keywords. „Jetzt anfragen“ bleibt für Formular-CTAs möglich; Fachinformationen benötigen beschreibende Anker. „Startseite“ darf nicht auf die Kontaktseite zeigen. Navigation, Footer, Breadcrumbs und Inhaltslinks getrennt bewerten. Sprunglinks auf tatsächlich vorhandene IDs prüfen.

Linkzahlen in den Maps zählen unterschiedliche ein-/ausgehende Seiten, ohne Selbstlinks; `internal-links.csv` enthält dagegen jedes Link-Vorkommen einschließlich Wiederholungen und Sprunglinks. Vorschlagszeilen gehören nicht zum gemessenen Bestandsgraphen.

## Title, Description und Überschriften

- Title beschreibt genau den Seitenzweck und verwendet den Ortsbezug nur, wo er sinnvoll ist. Markennamen höchstens einmal anhängen. Keine Garantie-, Preis- oder Zertifizierungsbehauptung ohne Nachweis.
- Etwa 50–60 Zeichen können als redaktionelle Orientierung dienen, sind kein hartes Rankingkriterium. Darstellung hängt unter anderem von Zeichenbreite und Suchergebnis ab. Keine automatischen Kürzungen allein nach Zeichenanzahl.
- Meta Description individuell, verständlich und mit belegtem Nutzen. Etwa 140–160 Zeichen als Orientierung; keine Keywordliste, keine erfundenen Vorteile. CTR erst mit tatsächlichen Klick-/Impressionsdaten beurteilen.
- Eine klare H1 als Projektkonvention. H1 muss Thema und Inhalt treffen, darf vom Title abweichen. H2 gliedern Nutzerfragen, H3 konkretisieren Unterpunkte. Keine Überschriften nur für zusätzliche Keywordvarianten.
- Keine Mindestwortzahl als Qualitätsbeweis. Fehlende Antworten konkret ergänzen, keine Fülltexte.

## Standort- und Ratgeberseiten

Standortseiten nur mit echtem Nutzen: tatsächliches Einzugsgebiet, bestätigter Ablauf für auswärtige Kunden, konkrete Anreiseinformationen und gegebenenfalls belegte lokale Projekte. Keine erfundenen Adressen, Teams oder Niederlassungen. Die sechs bestehenden Stadtseiten sind vor weiterem Ausbau zu individualisieren; reine Ortsersetzung reicht nicht.

Ratgeber beantwortet eine eigenständige Informationsfrage, nennt fachlich belastbare Quellen/Erfahrungen und verlinkt zur passenden Leistung. Keine zweite Angebotsseite im Blog verkleiden. Angaben zu Fahrzeugtechnik, Garantien, Rechtslage, Preisen und Pflegeverfahren vor Veröffentlichung sachlich prüfen. Vorhandene Website-Aussagen sind keine unabhängige Bestätigung ihrer Richtigkeit.

## Kannibalisierung und bestehende URLs

Inhaltliche Überschneidung und beobachtete Ranking-Kannibalisierung getrennt benennen. Letztere benötigt Query × URL × Datum mit vergleichbaren Filtern. Ein Wechsel von URLs oder Verdrängung ist mit dem jetzigen Export nicht feststellbar. Identische Texte sind ein sicherer Inhaltsbefund, kein Beweis eines Rankingverlusts.

Keine bestehenden URLs löschen oder umbenennen. Zusammenlegungen und Redirects mit unklarer Zielgleichheit benötigen eine Entscheidung. Die aktuelle Umsetzungserlaubnis deckt sichere technische Reparaturen ab: 23 eindeutige historische 404-Varianten und die Canonical-Zuordnung identischer Lackhärte-Fassungen sind dokumentiert. Daraus folgt keine pauschale Freigabe für weitere URL-Änderungen. Vor einer solchen Entscheidung Inhalt, Messwerte, interne Links, Backlinks soweit verfügbar und Zielgleichheit prüfen. Keine pauschalen Weiterleitungen aller alten Blogpfade auf die Startseite. Bestehende Verifizierungsdatei erhalten.

## Technische Prüfpunkte und Schutzregeln

Indexierbare Seiten sollen Status 200 und konsistente Host-/Canonical-/Sitemap-Signale haben. Noindex-Seiten nicht in der Suchmaschinen-Sitemap führen. Robots-Sperre nicht als Ersatz für noindex behandeln. Änderung der robots-/Indexierungsstrategie nur im freigegebenen Umsetzungspaket; besonders Rechts-/Funktionsseiten beachten.

JSON-LD nur für sichtbare, belegte Inhalte verwenden. Keine erfundenen Bewertungen, Referenzen oder Rich-Result-Versprechen. Alt-Texte beschreiben Inhaltsbilder; dekorative Bilder können leere Alt-Texte besitzen. Bildgewichte und Darstellung messen, ohne Belegbilder irreführend zu ersetzen.

Formulare, `/api/send-lead`, Google Ads, GTM, Consent, Tracking und bestehende CTAs bei SEO-Arbeiten erhalten. Ausführbare Skripte und Formulare sind gegen den Ausgangsstand geprüft; nur Inhaltslink-Stile ergänzen das bestehende Design. Keine Testanfragen versenden. Keine Preise, Leistungen, Kundenbewertungen oder Referenzen erfinden. Keine massenhaft ähnlichen Seiten und kein Keyword Stuffing.

## Wiederkehrender Arbeitsablauf

1. Neue Exporte unverändert in `Datei Manager` belassen; Format, Spalten, Zeitraum und Filter dokumentieren. Vorherigen Stand archivieren und Quellenhashes erhalten.
2. `python seo/tools/scan.py` liest die aktuelle Website. Voraussetzung: Python und `beautifulsoup4`. Der Parser erwartet aktuell einen URL-Index und einen Impressionen-Export; neue Schemata zuerst berücksichtigen.
3. `python seo/tools/build-reports.py` erzeugt CSVs und technische Nachweise. Bei vorhandener `implementation.json` verwendet es `build-current-reports.py`. Historische Messungen stammen aus dem archivierten Ausgangsstand. Redaktionelle Zuordnungen in `implementation.json` pflegen, nicht nur generierte CSVs überschreiben.
4. `implement.py` ist ein bereits ausgeführtes einmaliges Umsetzungsskript; nicht erneut auf den aktuellen Bestand anwenden. `write-status-docs.py` beschreibt dieses Umsetzungspaket; bei späteren Änderungen seine festen Beschreibungen zuerst aktualisieren oder Dokumente redaktionell fortschreiben.
5. Lokale Kontrolle mit `seo/tools/preview.mjs` und `python seo/tools/validate.py`. Preview benötigt `seo/routing-compiled.json`, erzeugt durch `getTransformedRoutes` aus dem offiziellen Paket `@vercel/routing-utils` und der aktuellen `vercel.json`. Nach Routing-Änderungen neu kompilieren. Die Entwicklungsabhängigkeit liegt außerhalb des Projekts im temporären Verzeichnis `powertech-seo-validation`. Preview blockiert externe Skripte und Formularversand ausschließlich lokal. Keine npm-Build-/Lint-/Testskripte vorhanden.
6. Seitenbestand, Quellenhashes, geschützte Formulare/Skripte/Kontaktwege, Canonicals, Sitemap, H1, Titles, Bilder, interne Links, Sprungziele, JSON-LD, JavaScript-Syntax, Redirects mit Query-Parametern und Maps prüfen. Die Schutzbaseline beschreibt den Stand vor diesem Paket; spätere autorisierte Funktionsänderungen separat dokumentieren.
7. Audit, Content-Plan, Datenanalyse, `implementation-status.csv` und `changes.md` gegen den tatsächlichen Stand prüfen. Status: umgesetzt, teilweise umgesetzt, nicht umgesetzt + Begründung, benötigt meine Entscheidung. Umgesetzt bedeutet bis zur Veröffentlichung ausschließlich lokal.
8. Nach Veröffentlichung öffentliche GET-Prüfung mit `check-live.py` durchführen und mit der historischen Momentaufnahme vergleichen. Der aktuelle Reportgenerator liest weiterhin die archivierte Messung: neue Live-Ergebnisse erst nach bewusster Anpassung des Imports übernehmen und datieren. Sitemap und Google-Canonical in Search Console kontrollieren; Query × URL × Datum beschaffen. Keine Testanfragen versenden.

CSV-Format: UTF-8 mit BOM, Semikolon, korrekt gequotete Felder. JSON enthält die detaillierte technische Evidenz. `summary.json` liefert maschinenlesbare Zählwerte. Keine CSV-Formeln notwendig.

## Externe Grundlagen

Google beschreibt Canonical-Signale als Hinweise; die endgültige Auswahl liegt bei Google: [Canonicalization](https://developers.google.com/search/docs/crawling-indexing/canonicalization). Eine robots-Sperre kann das Auslesen von noindex verhindern: [Noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing). Interne Erreichbarkeit und konsistente URLs: [SEO für Entwickler](https://developers.google.com/search/docs/fundamentals/get-started-developers). Abgerufen am 07.09.2026.
