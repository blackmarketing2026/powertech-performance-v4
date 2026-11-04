# Projektgedächtnis

Auf ausdrücklichen Nutzerwunsch vom 31.10.2026 vor jeder Arbeit `MEMORY.md` lesen. Nach abgeschlossenen Arbeiten dort Datum, Änderungen, Entscheidungen, relevante Prüfungen, lokale Commits, Veröffentlichungsstand und offene Punkte festhalten. Keine Geheimnisse oder Zugangsdaten speichern. Aktuelle Nutzeranweisungen haben Vorrang vor älteren Gedächtniseinträgen.

# SEO-Arbeiten

## Ziel und Prioritäten seit 04.11.2026

SEO soll passende Anfragen für Autoaufbereitung und Fahrzeugpflege in Erfurt fördern; die Aufbereitung vor der Leasingrückgabe und für Leasingrückläufer ist ein wichtiger Anlass neben anderen. Bestehende Leistungsseiten und hilfreiche Ratgeber anhand tatsächlicher Suchdaten, belegter Leistungen und verständlicher Anfragewege gezielt verbessern. Suchklicks und Rankings nicht mit Anfragen oder Aufträgen gleichsetzen; Wirkung nach Veröffentlichung anhand vergleichbarer Zeiträume prüfen. Preise, Kundenergebnisse und Garantien nicht erfinden. Die Startseite für das am 04.11.2026 beauftragte SEO-Paket nicht verändern; spätere ausdrückliche Nutzeranweisungen gelten für ihren jeweiligen Auftrag.

## Ansprache

Alle öffentlich sichtbaren Website-Texte, einschließlich Formulare, Blog, Cookie-Hinweise und Rechtstexte, sprechen Besucher in der Du-Form an. Grammatische Bezüge auf Dritte bleiben davon unberührt.

Vor SEO-, Content-, Metadaten-, internen Link- oder Routing-Änderungen zuerst
`seo/SEO-RULES.md` lesen. Den aktuellen Bestand in `seo/seo-map.csv` und die
Zuordnung in `seo/keyword-map.csv` berücksichtigen. Messwerte und Hypothesen
gemäß `seo/data-analysis.md` unterscheiden.

Eine Analyse oder ein Maßnahmenvorschlag autorisiert keine URL-Löschung,
Umbenennung, Zusammenlegung oder Weiterleitung. Aktuelle ausdrückliche
Nutzeranweisungen haben Vorrang. Formulare, Tracking, Google Ads und GTM nicht
nebenbei verändern.

## Verbindlicher Leistungsumfang

Powertech bietet KEIN Chiptuning, keine Stage-1/2-Leistungssteigerung und keine allgemeine Kennfeldoptimierung an. Keine Chiptuning-Seiten, Links, Keywords oder Angebote wieder anlegen, auch nicht aufgrund historischer SEO-Dateien.

Abgassysteme: Seit der Nutzerfreigabe vom 12.10.2026 bietet Powertech KEINE AdBlue-/SCR-Deaktivierung, kein AGR On-Off und kein DPF-Off an (in Deutschland für Straßenfahrzeuge unzulässig, § 19 Abs. 2 StVZO). Zulässig und angeboten: AdBlue-/SCR-Diagnose, Klärung des Reparaturwegs und Prüfung einer Rückrüstung auf Serienstand (`/adblue-diagnose-erfurt/`). AdBlue-Inhalte bleiben rein informativ, ohne Anleitung. Autoaufbereitung und Fahrzeugpflege sind das Kerngeschäft. Maßgeblich: `seo/business-policy.json`. Originalexporte und historische Audits sind nur Belege, keine aktuellen Leistungsangaben. Bestehende rechtliche Hinweise, Tracking und Formulare erhalten.

## URL-Schema

Einheitlich `https://www.powertech-performance.com/pfad/` mit Slash. Ausnahmen: `/ads` und `/anfrage-danke` (Ads-/Conversion-URLs) sowie Dateien unter `/pages/*.html`. Redirects und Rewrites werden aus `seo/tools/urlmap.py` mit `python seo/tools/build-routing.py` erzeugt, die Sitemap mit `python seo/tools/build-sitemap.py`. `vercel.json` nicht von Hand bearbeiten. Stand und Begründungen: `seo-audit.md`.


## Seitenbezogene Nutzeranweisung vom 31.10.2026

Für `/adblue-diagnose-erfurt/` ersetzt die aktuelle ausdrückliche Nutzeranweisung die bisherige Beschränkung auf Diagnose: AdBlue-System- und NOx-Sensor-Auskodierung für PKW, Transporter, Camper und Wohnmobile, kostenloses Angebot, klarer Hinweis auf Erlöschen der Betriebserlaubnis und Verbot des Betriebs im öffentlichen Straßenverkehr. Details: `business-policy.json` (im Verzeichnis `seo/`), `page_override_2026_10_31`. Keine Erweiterung auf AGR, DPF oder Chiptuning. Bestehende URL und technische Kontakt-/Tracking-Integration erhalten.
