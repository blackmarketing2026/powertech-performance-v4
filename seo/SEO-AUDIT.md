# SEO-Audit nach Umsetzung

Stand: 07.09.2026. **Lokaler Projektstand, noch nicht veröffentlicht.** „Umgesetzt“ bezeichnet Änderungen an den Projektdateien, nicht bereits gemessene Auswirkungen bei Google. Die vollständige Ausgangsanalyse bleibt unverändert unter [history/2026-09-07-analysis/SEO-AUDIT.md](history/2026-09-07-analysis/SEO-AUDIT.md).

## Ergebnis

- 61 bestehende Inhaltsseiten gezielt technisch und/oder redaktionell optimiert; keine bestehende URL gelöscht oder umbenannt.
- Eine neue Leistungsseite: `/trockeneisreinigung`. Insgesamt 62 Inhaltsseiten plus Google-Verifizierungsdatei.
- 23 gezielte Reparatur-Redirects für alte URLs mit zusammen 6.303 historischen Impressionen. Zwei zusätzliche Alias-Redirects betreffen ausschließlich die neue Trockeneis-Seite.
- 1067 interne Link-Vorkommen, 42 von 44 ursprünglichen Linkvorschlägen umgesetzt. 298 Link-Vorkommen sind neu oder wurden in Ziel, Anchor oder Kontext geändert; diese Zahl ist **nicht** die Zahl neu angelegter Seitenverbindungen.
- Null kaputte interne Ziele, null fehlende Sprungziele, genau eine H1 je Inhaltsseite, keine doppelten Titles.
- 54 kanonische indexierbare Sitemap-URLs. Zwei historische Lackhärte-Fassungen bleiben erreichbar und referenzieren die Hauptfassung.
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

**Validierung:** 63 HTML-Routen; 135 lokale HTTP-Prüfungen einschließlich aller bisherigen Redirect-Muster und 23 Reparatur-Redirects mit Query-Parametern; 188 ausführbare Inline-JS-Blöcke geparst. Externe JS-/API-Dateien per `node --check` geprüft. Alle Source-Hashes unverändert, keine Formulare abgesendet. `package.json` enthält keinen Build-, Lint- oder Testprozess; deshalb wurden die konkreten statischen, Routing- und Schutzprüfungen durchgeführt.

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

1. `https://www.powertech-performance.com/blog/adblue-deaktivieren-vor-nachteile-wahrheit/` – Redirect-Eingang vom alten Root-Pfad, Canonical und Query-Verteilung prüfen.
2. `https://www.powertech-performance.com/` – bestehende Sichtbarkeit und neue interne Leistungszugänge.
3. `https://www.powertech-performance.com/chiptuning` – zentrale Leistungsintention gegenüber den Ratgebern.
4. `https://www.powertech-performance.com/luxus-aufbereitung` – Keramik-Hauptziel gegenüber den allgemeinen Artikeln.
5. `https://www.powertech-performance.com/trockeneisreinigung` – erstmalige Indexierung und tatsächliche Suchnachfrage.

Zusätzlich bei Stichproben die historischen 404-URLs und die beiden Lackhärte-Canonicals kontrollieren. Vergleichszeiträume und Filter gleich halten; keine Query-Messungen mit historischen Seitenwerten vermischen.

## Nachweise

`seo-map.csv`, `keyword-map.csv`, `internal-links.csv`, `url-mapping.csv`, `implementation-status.csv`, `link-plan-status.csv`, `technical-inventory.md`, `validation-results.json` und `routing-compiled.json`. Vollständige Ist-Daten: `evidence.json`; Ursprungszustand unter `history/2026-09-07-analysis/`.

Fachliche Grundlagen: [Google zu Canonicals](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), [Google zu noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing), [Vercel-Konfiguration](https://vercel.com/docs/project-configuration/vercel-json), [§ 19 StVZO](https://www.gesetze-im-internet.de/stvzo_2012/__19.html), [ADAC zu Chiptuning](https://www.adac.de/rund-ums-fahrzeug/ausstattung-technik-zubehoer/zubehoer/chip-tuning-und-eco-tuning/), [Kärcher zur Trockeneisreinigung](https://www.kaercher.com/int/professional/know-how/dry-ice-blasting-in-car-workshops.html). Keine Garantie für Ranking- oder Rich-Result-Effekte.
