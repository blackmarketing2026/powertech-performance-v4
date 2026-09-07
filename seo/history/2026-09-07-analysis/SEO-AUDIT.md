# SEO-Audit Powertech Performance

Stand: 07.09.2026. Vollständiger lokaler HTML-Scan plus öffentliche HTTP-Prüfung aller Projekt- und Export-URLs. Keine Website-, URL-, Formular-, Design- oder Trackingänderungen umgesetzt.

## Ergebnis und Leseschlüssel

- **61 Inhaltsseiten** plus eine Google-Verifizierungsdatei; alle 62 lokalen Routen live erreichbar, Titel stimmen mit lokalem Stand überein.
- **39 URL-Datensätze, 6.493 Seitenimpressionen**, Zeitraum unbekannt; **0 beobachtete Suchanfragen**. 55 Keyword-Zuordnungen im Quellindex enthalten 50 unterschiedliche vermutete Keywords.
- **24 Export-URLs liefern 404**, ihnen gehören 6.324 Impressionen. Das sind 97,4 % der exportierten Zeilensumme, kein gemessener Trafficverlust und keine allgemeine Aussage über die gesamte organische Suche.
- **7 Kannibalisierungs-Risikogruppen**, davon eine Gruppe aus drei nachweislich identischen Artikel-Haupttexten. **0 bestätigte Ranking-Kannibalisierungsfälle**, weil Query-URL-Zeitreihen fehlen.
- **55 lokal indexierbare Seiten mit Optimierungsbedarf**: alle mit Host-/Canonical-Konflikt, davon 52 mit nur einer verlinkenden Quellseite. Dies ist überwiegend technische und interne Linkarbeit, keine Empfehlung, 55 Seiten großflächig neu zu schreiben.
- **2 neue Seiten empfohlen**: eine Trockeneis-Leistungsseite und ein Felgenpflege-Ratgeber; beide ohne gemessenen Nachfragebeleg. **44 konkrete interne Linkvorschläge** ergänzen die 893 Bestands-Linkvorkommen.

P1 = zuerst bearbeiten, P2 = anschließend, P3 = nachgeordnet. Prioritäten berücksichtigen nachgewiesene Erreichbarkeit, vorhandene Impressionen, Inhaltsüberschneidung und interne Erschließung. Keine erfundenen Suchvolumen-, Positions- oder Umsatzwerte. HTTP-Status ist eine Momentaufnahme; Indexierungsstatus bei Google wurde nicht über die Search Console geprüft.

## Kritische Probleme

### Suchdaten-URLs sind nicht erreichbar

24 von 39 Original-URLs antworten live mit 404. Die 18 historischen Root-Artikel-/Angebotspfade fehlen lokal. Weitere sechs Root-Pfade mit abschließendem Slash antworten ebenfalls 404, obwohl die endungslose Projektseite existiert. Für jede URL sind Originalwert, Status und möglicher Nachfolger in `url-mapping.csv` dokumentiert.

| Aktuell nicht erreichbare Export-URL (www-Host) | Impressionen | Möglicher bestehender Inhalt, noch kein Redirect-Auftrag |
|---|---:|---|
| `/adblue-deaktivieren-vor-nachteile-wahrheit/` | 6.095 | `/blog/adblue-deaktivieren-vor-nachteile-wahrheit/` |
| `/auto-selber-waschen-erfurt/` | 48 | `/blog/auto-selber-waschen-erfurt/` |
| `/chiptuning-raum-erfurt/` | 47 | `/blog/chiptuning-raum-erfurt/` |
| `/softwareoptimierung-dpf-off-erfurt/` | 33 | `/blog/softwareoptimierung-dpf-off-erfurt/` |
| `/adblue-deaktivierung/` | 22 | `/blog/adblue-deaktivierung/` |
| `/adblue-deaktivieren/` | 21 | `/adblue-service`, nur thematischer Vorschlag; Inhalt/Intention gesondert prüfen |
| `/chiptuning/` | 17 | `/chiptuning` |
| `/nordhausen/` | 8 | `/nordhausen` |

Die verbleibenden 16 betroffenen URLs stehen vollständig in `url-mapping.csv`. Beispiel: 6.095 Impressionen der alten AdBlue-URL werden **nicht** zu den 7 Impressionen der heutigen Blog-URL addiert. Zeitpunkt und Ursache des Erreichbarkeitsverlusts sind unbekannt. Nach Inhaltsprüfung einen individuellen Wiederherstellungs-/Redirect-Plan zur Freigabe vorlegen; keine pauschale Umleitung auf die Startseite.

### Canonical-Ziele werden selbst weitergeleitet

Die 61 Inhaltsseiten deklarieren `https://powertech-performance.com/...` als Canonical. Live führt dieser Host per 308 zu `https://www.powertech-performance.com/...`. Das www-Endziel enthält weiterhin den non-www-Canonical. Auch die lokale Sitemap verwendet non-www. Das erzeugt widersprüchliche Hinweise zur bevorzugten URL, belegt aber allein noch keine falsche Google-Indexierung.

Konkrete nächste Entscheidung: technisch gewünschte Hauptdomain festlegen; Host-Weiterleitung, Canonicals, Sitemap und interne absolute URLs gemeinsam ausrichten. Den aktuell funktionierenden www-Host nicht ohne Abgleich der Search-Console-/Deployment-Konfiguration umkehren. Vollständige Weiterleitungsschritte stehen in `live-check.json`.

## Hohe Priorität

1. **13 indexierbare Seiten nur über gesperrte Seitenübersicht verlinkt.** Darunter `/adblue-service`, `/chiptuning`, `/luxus-aufbereitung`, `/ads`, `/glosar`, `/online-termin-buchen`, `/fahrzeugaufbereitung-aus-erfurt` und sechs Stadtseiten. Die Quelle `/pages/seitenuebersicht.html` ist per robots.txt gesperrt und noindex. Ein Link aus dieser Quelle ist kein verlässlicher crawlbarer Hauptzugang. Die Sitemap ersetzt sinnvolle Inhaltsverlinkung nicht.
2. **Drei identische Lackhärte-Haupttexte.** Identischer Text, Title und H1 auf drei indexierbaren, selbst-kanonischen URLs. Vor weiteren Textänderungen Rollenentscheidung treffen, siehe K1.
3. **AdBlue-Inhalte widersprechen der zentralen Angebotspositionierung.** `/adblue-service` betont Diagnose, Reparatur, Rückrüstung und zulässige Anwendungen; mehrere Blogtexte verkaufen Deaktivierung als dauerhafte Problemlösung. Der Vor-/Nachteile-Artikel enthält rechtliche Hinweise, relativiert sie anschließend aber sprachlich. Aussagen, Snippets und Leistungsversprechen fachlich abstimmen. Dies ist eine Feststellung widersprüchlicher Inhalte, keine neue rechtliche Bewertung oder Freigabe einer Dienstleistung.
4. **Sechs Stadtseiten mit identischem Haupttext nach Ortsersetzung.** `/eisenach`, `/gera`, `/gotha`, `/jena`, `/nordhausen`, `/suhl`. Vorhandene Seiten mit echtem eigenständigem Nutzen verbessern; keine weiteren Ortskopien.
5. **Indexierungssignale widersprechen sich.** Sitemap enthält `/pages/agb.html`, `/pages/datenschutz.html`, `/pages/impressum.html`, obwohl noindex und robots-gesperrt. Robots-Sperren verhindern außerdem bei Cookie-Einstellungen und Seitenübersicht das verlässliche Auslesen des vorhandenen noindex.

## Bestehende Seiten mit Rankingpotenzial

Rankingpotenzial bezeichnet hier einen plausiblen Optimierungsansatz, keine nachgewiesene Position. Für die folgende Tabelle sind nur über ein identisches Live-Endziel verbundene **Seitenimpressionen** verwendet.

| Projekt-URL | Zugeordnete Impressionen | Ansatz |
|---|---:|---|
| `/` | 130 | Leistungen direkt erschließen, zentrale Suchintention stärken, Metadaten nicht mit Orts-/Leistungslisten überladen. |
| `/blog/wie-oft-auto-aufbereiten-lassen.html` | 9 | Konkrete Nutzungsfälle/Intervalle fachlich erweitern; Links zu passenden Leistungen. |
| `/blog/adblue-deaktivieren-vor-nachteile-wahrheit/` | 7 | Fachliche Konsistenz, sachliches Snippet, klarer Link zur Diagnose-/Reparaturberatung. |
| `/blog/wie-lange-dauert-adblue-off/` | 6 | Inhalt und Zeitversprechen fachlich abgleichen; eigene Informationsfrage klar definieren. |
| `/blog/boot-aufbereitung-keramikversiegelung-marine/` | 4 | Tatsächlichen Leistungsumfang belegen; nur passende Pflege-/Anfrageverknüpfungen. |
| `/blog/auto-selber-waschen-erfurt/` | 2 | Konkrete lokale Frage besser beantworten; keine ungeprüften Waschplatzdaten ergänzen. |
| `/blog/harte-weiche-autolacke-lackaufbereitung/` | 2 | K1-Duplikatgruppe vor Optimierung lösen; keine Gewinnerentscheidung aus zwei Impressionen. |
| `/blog/motorradaufbereitung-keramikversiegelung-experte/` | 2 | Leistungs-/Garantiebelege und thematische Verlinkung prüfen. |

Sieben weitere erreichbare Export-URLs besitzen je eine Impression. Alle Zuordnungen sind in `seo-map.csv` sichtbar. Die Tabelle summiert keine vermuteten historischen Nachfolger zusammen.

## Seiten mit hoher Impression aber schwacher Position

**Nicht feststellbar: Positionsdaten fehlen.** Die alte AdBlue-URL mit 6.095 Impressionen ist ein prioritäres Erreichbarkeitsproblem. Sie darf nicht als schlecht rankende Seite bezeichnet werden. Ein künftiger Export muss Positionen je Query/Seite und Zeitraum liefern; erst dann mittlere/schwache Positionen bei relevantem Impressionenvolumen priorisieren.

## Seiten mit schwacher CTR

**Nicht feststellbar: Klicks und CTR fehlen.** Aus Impressionen allein lässt sich keine Klickrate berechnen. Die Felder bleiben leer. Snippets werden derzeit aufgrund von Inhalt, Klarheit und Konsistenz zur Prüfung vorgeschlagen, nicht aufgrund einer behaupteten schlechten CTR.

## Keyword-Kannibalisierung

Es wurden sieben redaktionelle Risikogruppen abgegrenzt. **Google-Wechsel zwischen URLs, gemeinsames Ranking für identische Suchanfragen und Verdrängung einer wichtigeren Seite sind nicht nachgewiesen.** Dafür fehlen Suchanfrage × URL × Datum sowie Klicks/Positionen. Unterschiedliche Exporteinträge für alte und neue Pfade beweisen keinen zeitlichen Wechsel.

### K1 — Lackhärte: bestätigtes Inhaltsduplikat, hohes Risiko

- `/blog/harte-weiche-autolacke-lackaufbereitung/`
- `/blog/harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung/`
- `/blog/harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung-2/`

Alle drei haben denselben extrahierten Artikel-Haupttext mit 422 Wörtern sowie gleichen Title und H1. Je ein Link von der Blogübersicht, drei Self-Canonicals. Zugeordnete Seitenimpressionen: 2, 1 und 1, nicht Query-Rankings. Der Quellindex ordnet allen dasselbe vermutete Hauptkeyword zu. Vorläufiger Vertreter ist die kürzere bereits vorhandene URL; Auswahl muss mit URL-/Query-Historie und gegebenenfalls Backlinks abgesichert werden. Keine automatische Zusammenlegung oder Weiterleitung.

### K2 — Chiptuning: gleiche kommerzielle Intention, hohes Risiko

`/chiptuning`, `/blog/chiptuning-raum-erfurt/`, `/blog/chiptuning-raumerfurt/`, `/blog/softwareoptimierung-erfurt/`.

Die beiden Chiptuning-Blogartikel haben im Index dasselbe vermutete Hauptkeyword „Chiptuning Raum Erfurt“. Die Softwareoptimierung überschneidet sich mit dem Leistungsangebot. Alle vier haben nur eine verlinkende Quellseite. Vorläufig `/chiptuning` als Leistungsziel; Blogseiten nur mit eigenständigen Fragen fortführen. 47 Impressionen auf altem Root-Artikelpfad, 17 auf `/chiptuning/` und 3 auf altem Softwarepfad gehören zu 404-URLs und werden nicht als Rankings dieser vier Seiten ausgegeben.

### K3 — Keramik: breite Angebotsüberlappung, hohes Risiko

`/luxus-aufbereitung` und die Blogpfade `/blog/professionelle-keramikversiegelung-erfurt/`, `/blog/profi-keramikversiegelung/`, `/blog/keramikversiegelung-profi-lackschutz/`, `/blog/keramikversiegelung-erfurt-high-end-lackschutz-powertech-performance/`, `/blog/keramik-fuer-auto-erfurt-vorteile-haltbarkeit/`, `/blog/blog-keramikversiegelung/`.

Sie behandeln allgemein professionellen Keramikschutz, Nutzen und Angebot. Vorläufig `/luxus-aufbereitung` als Leistungsziel. Weitere Seiten nur über klar unterschiedliche, im Text tatsächlich beantwortete Fragen abgrenzen. Der vorhandene spezifische Haltbarkeitsartikel bleibt als eigene Informationsintention außerhalb dieser Risikogruppe. Keine neue Keramik-Landingpage vorschlagen.

### K4 — Innenreinigung: gleiche lokale Intention, hohes Risiko

`/blog/innenreinigung-auto-in-der-naehe/` und `/blog/professionelle-innenreinigung-auto-in-der-naehe/`.

Gleiches vermutetes Keyword im Quellindex, sehr ähnliche H1 und Dienstleistungsansprache. 667 bzw. 200 Wörter, aber Textlänge begründet keinen Rankinggewinner. Vorläufig die umfangreichere vorhandene Seite als redaktionelles Hauptziel; Rollenentscheidung offen. `/blog/was-kostet-eine-auto-reinigung/` bleibt separat für Kostenfaktoren und wird intern angebunden.

### K5 — Autoaufbereitung Erfurt: vier Angebotsseiten, hohes Risiko

`/`, `/ads`, `/fahrzeugaufbereitung-aus-erfurt`, `/blog/fahrzeugaufbereitung-erfurt/`.

Auto-/Fahrzeugaufbereitung im selben Ort; `/ads` ist aktuell indexierbar und in der Sitemap. Zwei Seiten besitzen dasselbe vermutete Hauptkeyword „Fahrzeugaufbereitung Erfurt“. `/` erhält 130 zugeordnete Seitenimpressionen. Startseite als primäres Ziel; Kampagnenrolle und Blogintention klären. Kein automatisches noindex der Ads-Seite und keine Änderung an Tracking/Conversion-Abläufen.

### K6 — Leasing: ähnliche Angebotsintention, mittleres Risiko

`/blog/leasingauto-aufbereiten/` und `/blog/leasing-rueckgabe-aufbereitung-erfurt/`.

Beide argumentieren mit Aufbereitung vor Rückgabe und möglichen Nachzahlungen. Vorläufig lokaler Rückgabeartikel als Leistungsberatung. Inhaltliche Abgrenzung prüfen, keine Rankingverdrängung behaupten. `/blog/leasingrueckgabe-checkliste/` deckt eine eigene praktische Frage ab und bleibt außerhalb der Gruppe.

### K7 — AdBlue: Überschneidung und widersprüchliche Ausrichtung, mittleres Risiko

`/adblue-service`, `/blog/adblue-deaktivierung/`, `/blog/adblue-deaktivieren-vor-nachteile-wahrheit/`, `/blog/wie-lange-dauert-adblue-off/`.

Die Fragen sind teilweise verschieden, aber Artikel führen wieder zu ähnlichen Angebotsversprechen. Gemeinsame redaktionelle Positionierung nötig. Service-Seite als Angebotsziel; Fachartikel müssen ihre spezifische Frage sachlich beantworten. Zugeordnete Artikelimpressionen 7 und 6 zeigen keine Suchanfragen oder Verdrängung. Diese Gruppe ist schwächerer Kannibalisierungsverdacht als K1–K5, aber hoher Bedarf an inhaltlicher Konsistenz.

**Separater Qualitätsbefund:** sechs Stadtseiten nach Ortsersetzung identisch. Wegen verschiedener lokaler Suchintentionen nicht als achte bestätigte Kannibalisierungsgruppe zählen. Ebenfalls keine doppelte Zählung historischer 404-Pfade als zusätzliche konkurrierende Seiten.

## Interne Verlinkungsprobleme

- 893 interne Link-Vorkommen wurden mit Anchor, Kontext und Ziel erfasst. Ein-/Ausgangszahlen der Seitenmap zählen dagegen unterschiedliche Quell-/Zielseiten ohne Selbstlinks.
- Keine echten Orphan-Inhaltsseiten im vollständigen lokalen Graphen. Die unverlinkte Google-Verifizierungsdatei ist kein Problem.
- 39 Artikel besitzen ausschließlich die Blogübersicht als verlinkende Seite. Relevante Querverweise und Verbindungen zu Leistungen fehlen.
- 13 indexierbare Seiten sind nur über die gesperrte Seitenübersicht verknüpft. Sie sind keine absoluten Orphans, aber im crawlbaren internen Graphen schwach erschlossen.
- 46 Links auf `/#ueber-uns` und zwei auf `/#faq` haben kein entsprechendes Startseitenziel. Passende vorhandene IDs auswählen, statt blind neue Textabschnitte anzulegen.
- Ein Link mit Anchor „Startseite“ im Artikel `/blog/innenreinigung-auto-in-der-naehe/` führt zur Kontaktseite. Anchor/Ziel korrigieren.
- Generische Inhaltsanker wie „www.powertech-performance.com“ vermitteln wenig Thema. Formular-CTAs wie „Jetzt anfragen“ sind hingegen kontextabhängig angemessen.
- Blogbanner werben auch auf Chiptuning-/AdBlue-Artikeln pauschal für Autoaufbereitung. Das ist kein technischer Linkfehler, aber ein unpassender Angebotskontext; fachbezogene Kontakt-/Serviceverknüpfung prüfen.

44 genaue Vorschläge stehen als **Vorschlag**-Zeilen in `internal-links.csv`, getrennt von Bestandslinks. Dazu gehören Startseite → Keramik/AdBlue/Chiptuning/Motorraum/Innenreinigung, Haltbarkeit ↔ Keramik-Leistung sowie Checkliste → Leasingberatung. Vier Vorschläge betreffen die zwei noch nicht existierenden neuen Seiten und dürfen erst nach Veröffentlichung umgesetzt werden.

## Content-Lücken

Die Leistungsübersicht deckt Lackkorrektur, Keramik, Innenraum, Lederpflege, Leasing, Felgen, Trockeneis, Motorraumwäsche und mehrstufiges Finish ab. Trockeneis hat noch keine eigene Leistungsseite; Felgen-Nachpflege keinen spezifischen Ratgeber. Bestehende knappe Artikel zu Eigenwäsche, 1-Step-Politur und Leasingcheckliste benötigen eher konkrete Antworten als zusätzliche URLs.

Die Keyword-Daten bieten keine gemessenen Informationsfragen, kein Suchvolumen und keine Positionslücken. Content-Lücken werden deshalb aus tatsächlichem Leistungsbestand, vorhandenen Überschriften und fehlender zielgerichteter Verlinkung abgeleitet. Industrie-, Teile- oder Graffiti-Reinigung sind nicht als eigenständige Leistungen belegt.

## Neue Unterseiten

Eine Empfehlung: **`/trockeneisreinigung`** für die tatsächlich auf der Startseite genannte fahrzeugbezogene Leistung. Unterboden zunächst als Abschnitt integrieren. P2, nach den bestehenden technischen Problemen. Vollständiges Briefing mit Keyword-Hypothesen, H1/H2 und Links in `content-plan.md`.

Keine zusätzliche Keramik-, Innenraum-, Motorwäsche- oder pauschale Unterboden-Landingpage. Vorhandene Intentionen zuerst klar zuordnen.

## Neue Ratgeber-/Blogbeiträge

Eine Empfehlung: **`/blog/felgenversiegelung-pflege/`** für die Nachpflege versiegelter Felgen. Angebot auf Startseite belegt; genaue Pflegehinweise müssen zum tatsächlich verwendeten Produkt passen. P3, kein Nachfragebeleg. Das Briefing steht in `content-plan.md`.

Weitere gute Themen wie Haltbarkeit, Lackhärte, Leasingcheckliste und Innenreinigungskosten sind schon vorhanden und werden nicht erneut vorgeschlagen.

## Technische SEO-Punkte

- Architektur: statische Multipage-Site, 14 Vercel-Rewrites, 42 Redirect-Regeln, Node-Mail-Endpunkt. Keine neue Framework-Migration nötig.
- Sitemap: 58 URLs, davon 55 lokal indexierbar und drei noindex-Rechtsseiten. Alle Sitemap-URLs besitzen eine lokale Inhaltsdatei. Kein Beweis der tatsächlichen Google-Indexierung.
- robots.txt: fünf disallow-Pfade, jeweils auch noindex im HTML. Die Danke-Seite ist noindex und nicht in der Sitemap.
- Alle 61 Inhaltsseiten haben genau eine H1 und einen Canonical. Impressum und Datenschutz haben keine Meta Description; dies hat für die ausdrücklich ausgeschlossenen Seiten keine hohe Rankingpriorität.
- Strukturierte Daten nur auf `/adblue-service`: AutomotiveBusiness, BreadcrumbList, FAQPage; JSON syntaktisch parsebar. Keine anderen JSON-LD-Seiten. Fehlendes Schema ist kein Indexierungsblocker. Eigene Unternehmensdaten später konsistent strukturieren, ohne Bewertungen oder Garantien zu erfinden.
- Bilder: 295 img-Elemente, null fehlende alt-Attribute, zwei leere Alt-Texte; Smartphone-Rahmen plausibel dekorativ, Nachherbild auf sinnvolle Beschreibung prüfen. Keine lokal fehlenden img-Dateien. Große Assets bis 3,92 MB; Dateigrößen sind keine gemessenen Ladezeiten.
- Hauptnavigation und Footer sind pro Seite ausgewertet; Breadcrumbs im Artikel führen zur Blogübersicht. Die komplette H1/H2/H3-, Bilder-/Alt-, Abschnitte- und Schema-Erfassung steht in `seo-map.csv`, vollständige Haupttexte zusätzlich in `evidence.json`.
- Die Startseite zeigt einen Text über „passend erzeugte KI-Bilder“ und zugleich „echtes Bildpaar“. Redaktionelle Klarheit und transparente Bildkennzeichnung prüfen. Keine künstlichen Vorher-/Nachherbilder als Kundenreferenz darstellen; keine echten Referenzen hinzuerfinden.
- Browser-Rendering, Layout, JavaScript-Laufzeit, Core Web Vitals und Search-Console-URL-Prüfung wurden nicht gemessen. Titelvergleich live/lokal ist kein vollständiger Bytevergleich des öffentlich ausgelieferten Inhalts. Formulare wurden nicht abgesendet, Tracking nicht ausgeführt.

## Maßnahmen mit geringem Risiko und hohem Potenzial

1. Passende Inhaltslinks zu bereits erreichbaren Leistungsseiten ergänzen; dadurch die Abhängigkeit von der gesperrten Seitenübersicht reduzieren.
2. 48 fehlgeleitete Sprunglinks und den falschen Startseiten-Anchor gezielt korrigieren.
3. Query-URL-Daten samt Zeitraum und Filter ergänzen; anschließend Risikogruppen mit tatsächlicher Suchverteilung abgleichen.
4. Bestehende Ratgeber um fehlende konkrete Antworten ergänzen, ohne neue URLs oder pauschale Textverlängerung.
5. Redaktionsrollen für Keramik, Chiptuning, Innenreinigung und Leasing schriftlich festlegen, bevor Inhalte geändert werden.

Host-Wechsel, Weiterleitungen, Canonical-Änderungen und Duplikat-Zusammenlegungen sind koordinierte Folgepakete mit Freigabe, keine bereits autorisierten Sofortänderungen.

### TOP 10 SEO-Maßnahmen

Sortiert nach qualitativ erwartetem Nutzen. Keine Wirkungsgarantie oder erfundene Trafficprognose.

| Rang | Betroffene URL(s) | Problem | Datenbasis | Konkrete Maßnahme | Erwarteter SEO-Effekt | Risiko | Priorität |
|---:|---|---|---|---|---|---|---|
| 1 | 24 Export-URLs, zuerst `/adblue-deaktivieren-vor-nachteile-wahrheit/` | HTTP 404 bei URLs mit Suchsichtbarkeit | 6.324/6.493 Export-Impressionen; alle 24 Statuswerte live geprüft | Inhaltliche Nachfolger aus `url-mapping.csv` prüfen; individuellen Wiederherstellungs-/Redirect-Plan freigeben lassen und erst danach umsetzen | Erreichbarkeit für Suchende und konsistente historische URL-Signale wiederherstellen | mittel: falsche Zielgleichheit oder pauschale Redirects | P1 |
| 2 | Alle 61 Inhaltsseiten, Sitemap, Host-Konfiguration | www-Weiterleitung gegen non-www-Canonical | 61 HTML-Canonicals und Live-Redirectketten | Hauptdomain abstimmen; Canonicals, Sitemap, absolute Links und Host-Routing konsistent ausrichten | Klarere kanonische Signale und weniger unnötige Umwege | mittel: betrifft die gesamte Domain | P1 |
| 3 | `/`, `/adblue-service`, `/chiptuning`, `/luxus-aufbereitung` und weitere schwach erschlossene Ziele | 13 indexierbare Seiten nur aus gesperrter Seitenübersicht | Vollständiger Linkgraph; 39 weitere Artikel nur über Blogübersicht | Vorrangige konkrete Inhaltslinks aus `internal-links.csv` ergänzen | Bessere interne Erreichbarkeit und thematische Einordnung | gering bei bestehenden Status-200-Zielen | P1 |
| 4 | Drei Lackhärte-Artikel, siehe K1 | Identischer Haupttext auf drei URLs | 422 identische Wörter, gleiche H1/Title, 2/1/1 Seitenimpressionen | Bevorzugte Rolle mit Query-/URL-Historie prüfen; klare Abgrenzung oder einzeln freizugebende Konsolidierung planen | Weniger redundante Inhalte und eindeutigere Zielseitenwahl | mittel bei URL-Eingriffen; Analyse gering | P1 |
| 5 | `/adblue-service`, drei AdBlue-Blogartikel, Blogteaser | Widersprüchliche Angebotspositionierung | HTML-Angebotstexte; 7/6 zugeordnete Artikelimpressionen; größter alter Pfad 404 | Aussagen fachlich prüfen und Diagnose-/Reparaturangebot, Ratgeber und Snippets aufeinander abstimmen | Bessere Relevanz und verlässlichere Nutzererwartung | mittel: fachliche Prüfung erforderlich | P1 |
| 6 | K2–K6, insbesondere `/chiptuning`, `/luxus-aufbereitung`, `/` und Innenreinigungsartikel | Mehrere ähnliche kommerzielle Zielseiten | Keyword-Hypothesen, H1/Title und Haupttexte; keine Query-Rankings | Hauptziel je Intention festlegen, Artikelrollen konkretisieren, Querverweise ergänzen; Ads-Rolle gesondert prüfen | Klarere Themenzuständigkeit und geringeres Kannibalisierungsrisiko | gering für Mapping, mittel für größere Inhalts-/Indexierungsänderungen | P1 |
| 7 | `/pages/agb.html`, `/pages/datenschutz.html`, `/pages/impressum.html`, Cookie-Einstellungen, Seitenübersicht | noindex, Sitemap und robots-Sperren inkonsistent | 3 noindex-URLs in Sitemap; 5 blockierte noindex-Seiten | Gewünschten Ausschlusszustand dokumentieren; Sitemap bereinigen und Crawling-/noindex-Strategie abgestimmt korrigieren | Konsistentere Crawl-/Indexierungshinweise | gering bis mittel: unerwünschte Indexierung vermeiden | P2 |
| 8 | 46 Verweise auf `/#ueber-uns`, zwei auf `/#faq`; Innenreinigungsartikel | Fehlende IDs und irreführender Anchor | 48 konkrete Sprunglink-Vorkommen; „Startseite“ führt zu Kontakt | Passende vorhandene IDs/Zieltexte einsetzen und betroffene Links erneut prüfen | Bessere Navigation und verständlichere interne Verweise | gering | P2 |
| 9 | `/eisenach`, `/gera`, `/gotha`, `/jena`, `/nordhausen`, `/suhl` | Gleicher Text nach Ortsersetzung | Vergleich der vollständigen Haupttexte; schwache Verlinkung | Reale Einzugsgebiets-/Anreiseinformationen ergänzen; keine weiteren Ortskopien | Mehr eigenständiger Nutzen für lokale Suchintentionen | gering bei belegten Angaben | P2 |
| 10 | vorgeschlagen `/trockeneisreinigung`, später `/blog/felgenversiegelung-pflege/` | Tatsächliches Angebot ohne spezifischen Zielinhalt | Leistungsfelder in index.html; keine Nachfragekennzahlen | Zwei Briefings aus `content-plan.md` nach Leistungs-/Faktenprüfung ausarbeiten | Abdeckung bislang unzureichend beantworteter eigenständiger Intentionen | gering bis mittel; Nachfrage noch ungemessen | P2 / P3 |

## Nachweise und fachliche Grundlagen

Lokale Primärquellen: alle HTML-Dateien, `vercel.json`, `robots.txt`, `sitemap.xml`, CSS/JS, API-Dateien sowie die beiden unveränderten CSV-Dateien. Detailinventar: `technical-inventory.md`. Original-URL-Zuordnung: `url-mapping.csv`. Prüfergebnisse: `evidence.json`, `live-check.json`, `summary.json`.

Die Empfehlung zu konsistenten Canonicals folgt [Google Search Central: Canonicalization](https://developers.google.com/search/docs/crawling-indexing/canonicalization). Robots-Sperren können das Auslesen eines noindex verhindern: [Google Search Central: Noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing). Zur internen Erreichbarkeit: [SEO für Entwickler](https://developers.google.com/search/docs/fundamentals/get-started-developers). Diese Grundlagen ersetzen keine individuellen Search-Console-Messwerte.
