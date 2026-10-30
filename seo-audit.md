# SEO-Audit Phase 0 – Bestandsaufnahme powertech-performance.com

Stand: 12.10.2026 · Grundlage: lokales Repository (Commit `ca328af`, identisch mit `origin/main`) und Live-Abfragen der Website am 12.10.2026 · **In dieser Phase wurde nichts an der Website geändert.**

Messwerte (Status-Codes, Canonicals, Zählungen, Textähnlichkeit) sind direkt geprüft. GSC-Zahlen stammen aus dem Prompt (11.07.–10.10.2026) und liegen nicht als Datei im Repo. Empfehlungen und erwartete Wirkungen sind Hypothesen (siehe `seo/data-analysis.md`).

---

## 0. Kurzfazit

1. **Mehrere Punkte aus dem Prompt-Befund sind live schon erledigt.** Die AdBlue-Root-URL, `/fahrzeugaufbereitung-erfurt/` und die meisten `/x` + `/blog/x`-Paare leiten seit dem September-Deployment per 308 weiter. Die GSC-Doppelungen im Zeitraum Juli–Oktober stammen zum Teil aus der Zeit davor.
2. **Neues, größeres Duplikatproblem:** Alle 35 Blogartikel sowie `/ratgeber/…`, `/index.html` und `/blog/index.html` liefern **zusätzlich ohne Slash Status 200**. Das lässt sich mit einer Vercel-Einstellung (`trailingSlash: true`) global beheben.
3. **Doorway-Risiko:** Die sechs Stadtseiten (Gotha, Jena, Suhl, Gera, Nordhausen, Eisenach) sind nach Entfernen des Ortsnamens **zu 100 % textgleich**. Dieselbe Vorlage steckt zu 84–90 % auch in `/luxus-aufbereitung`, `/fahrzeugaufbereitung-aus-erfurt` und `/ads`.
4. **Es fehlen echte Leistungsseiten.** Keramik läuft über eine Vorlagenseite. Lackkorrektur, Innenraum, Cabrio, Oldtimer und Leasing existieren nur als Blogartikel. Startseite und Stadtseiten haben kein JSON-LD.
5. **Zwei harte Widersprüche** zwischen diesem Prompt und den verbindlichen Projektregeln (`AGENTS.md`, `seo/business-policy.json`) betreffen Chiptuning und AdBlue. Ich brauche Ihre Entscheidung, bevor ich weiterarbeite (Abschnitt 1).

---

## 1. Entscheidungen vor Phase 1

| # | Thema | Konflikt / Frage | Meine Empfehlung |
|---|---|---|---|
| **E1** | **Chiptuning / Softwareoptimierung** | Der Prompt nennt Chiptuning als Leistung (Phase 2.3, 2.4, Slug `chiptuning-raum-erfurt`). `AGENTS.md` und `business-policy.json` sagen dagegen: Es gibt **kein Chiptuning**. Die fünf Seiten wurden am 07.09.2026 auf Ihre ausdrückliche Anweisung gelöscht und liefern live 404. | Kein Chiptuning wieder anlegen. Die alten URLs bleiben 404 (oder 410). **Phase 2.4 entfällt dann.** Die GSC-Impressionen für „softwareoptimierung erfurt“ (Pos. 3,2) und „leistungssteigerung erfurt“ (Pos. 6) gehörten zu den gelöschten Seiten und laufen aus. Bitte bestätigen. |
| **E2** | **AdBlue-Service** | Laut `business-policy.json` sind „AdBlue-Deaktivierung“ und „AGR On-Off“ bestätigte Angebote. Prompt 2.7 sagt: Abgas-Deaktivierung darf nicht angeboten werden. `/adblue-service` hat Angebotscharakter: Title und H1 lauten „AdBlue-Deaktivierung & AGR On-Off“, die Karte „AdBlue-Deaktivierung“ verspricht eine Einzelfallprüfung für Offroad/Export, die Karte „AGR On-Off“ fragt nach dem Einsatzzweck. Ein Hinweis zur Rechtslage ist vorhanden. | Prompt 2.7 folgen: Seite auf **AdBlue-/SCR-Diagnose und Reparatur** umstellen, neuer Slug z. B. `/adblue-diagnose-erfurt/`, 301 von `/adblue-service`. AGR On-Off ist rechtlich gleich gelagert und sollte ebenfalls entfallen. Danach müssen `AGENTS.md`, `seo/SEO-RULES.md` und `business-policy.json` angepasst werden. **Das ändere ich nur mit Ihrer ausdrücklichen Freigabe.** Zusätzlich die Frage: Führt Powertech AdBlue-Reparaturen (Pumpe, Sensor, Heizung, Tank) selbst aus oder nur die Diagnose? |
| **E3** | **Money Page Fahrzeugaufbereitung** | Der Prompt verlangt eine neue Seite `/fahrzeugaufbereitung-erfurt/`. Seit heute gibt es auf Ihre Anweisung vom 12.10. die neu gebaute Leistungsseite `/autoaufbereitung`. Zwei Seiten für dieselbe Suchintention würden sich gegenseitig Konkurrenz machen. | **Eine Seite.** `/autoaufbereitung` wird nach `/fahrzeugaufbereitung-erfurt/` verschoben und ausgebaut, 301 von `/autoaufbereitung`. Begründung: „fahrzeugaufbereitung erfurt“ hat 503 Impressionen, „autoaufbereitung erfurt“ nur 121. Die Seite muss also nicht neu gebaut, sondern nur erweitert werden. Alternative: `/autoaufbereitung` behalten und alles dorthin leiten. |
| **E4** | **Slash-Schema** | Der Prompt will überall `/pfad/`. Heute gilt ein gemischtes Schema: Root-Seiten ohne Slash (`/gotha`), Blogartikel mit Slash. `seo/SEO-RULES.md` hatte bewusst keine pauschale Normalisierung vorgesehen. | Wie im Prompt: `"trailingSlash": true` in `vercel.json`. Folgen: 15 Root-Seiten ändern einmalig ihre URL (`/gotha` → `/gotha/`). Die bestehenden Regeln „`/x/` → `/x`“ müssen raus, sonst entsteht eine Schleife. Rewrites, Canonicals, interne Links und Sitemap werden angepasst. Gewinn: Alle 38 Slash-Duplikate verschwinden auf einen Schlag. |
| **E5** | **Stadtseiten** | Die Seiten sind 100 % identisch. Unterscheiden könnten sie sich nur durch echte Fakten, die ich nicht kenne: Hol- & Bringservice, Beispielaufträge, Kundenherkunft. Fahrzeiten kann ich nicht verlässlich angeben. | Bis Sie Fakten liefern: alle sechs Seiten auf **`/einzugsgebiet/`** zusammenlegen (301). Für jede Stadt, zu der Sie echte Informationen liefern, eine eigene Seite `/fahrzeugaufbereitung-<stadt>/`. Für Weimar, Arnstadt und Sondershausen gibt es heute keine Seiten. Die lege ich nur mit echtem Inhalt an. |
| **E6** | **Keramik-Cluster** | Der Prompt sagt: alle Keramik-URLs außer Leistungsseite und einem Ratgeber per 301. Textlich sind die Blogartikel nur zu 16–29 % gleich, thematisch überschneiden sie sich aber stark. | Wie im Prompt (Tabelle in Abschnitt 6). **Ausnahme:** Die fahrzeugspezifischen Artikel (Audi R8, Porsche, Boot, Motorrad, Leasing-Ratgeber) bleiben bestehen, weil sie eine eigene Suchintention haben. Bitte bestätigen. |
| **E7** | `/blog/auto-selber-waschen-erfurt/` | Prompt 3.4: Bietet Powertech eine SB-Waschanlage an? | Falls nein: Die Seite wird auf „Selber waschen oder aufbereiten lassen?“ ausgerichtet (Phase 5). |
| **E8** | `/ads` (Google-Ads-Landingpage) | Die Seite ist indexierbar und zu 89 % mit der Stadtseiten-Vorlage identisch. Laut `AGENTS.md` darf ich Ads und Tracking nicht nebenbei verändern. | `noindex,follow` setzen und aus der Sitemap nehmen. Tracking und Formular bleiben unverändert. Das braucht Ihre Freigabe. |
| **E9** | `/luxus-aufbereitung` | Das ist das heutige Keramik-Ziel. Es handelt sich aber um die Stadtseiten-Vorlage mit einer Keramik-H1. | Die Seite wird zur echten Leistungsseite `/keramikversiegelung-erfurt/` umgebaut (301 von `/luxus-aufbereitung`). |
| **E10** | `/pages/kontakt.html` | Indexierbare Seite mit `.html` in der URL. | Optional `/kontakt/` mit 301. Die Rechtsseiten unter `/pages/*.html` stehen auf noindex und bleiben unverändert. |
| **E11** | `/ratgeber/leasingfahrzeug-keramikversiegelung` | Diese Seite hat **keinen einzigen internen Link** (verwaist), liegt außerhalb von `/blog/` und ist doppelt erreichbar (mit und ohne Slash). | Prüfen, ob es eine Ads-Landingpage ist. Falls nein: Sie wird in den Leasing-Cluster eingebunden und intern verlinkt. |

---

## 2. Prompt-Befund im Abgleich mit dem Live-Stand (12.10.2026)

| Aussage im Prompt | Live geprüft | Folge |
|---|---|---|
| `/adblue-deaktivieren-vor-nachteile-wahrheit/` liefert 200 | **308 → `/blog/…`** | Ist erledigt und bleibt so. Die GSC-Werte konsolidieren sich mit der Zeit. Das Ziel entspricht der Vorgabe im Prompt. |
| `/fahrzeugaufbereitung-erfurt/` → Blog | 308 → `/blog/fahrzeugaufbereitung-erfurt/` ✔ | Die Weiterleitung wird in Phase 1/2 umgedreht (E3). |
| `/gotha` und `/gotha/` (ebenso Suhl, Nordhausen, Gera) | Ohne Slash 200, mit Slash 308 → ohne Slash | Technisch heute schon eindeutig. Ändert sich mit E4/E5. |
| `/jena` | 200; **`/jena/` liefert 404**, ebenso `/eisenach/` und `/luxus-aufbereitung/` | Wird durch die Slash-Regel behoben. |
| `/x` + `/blog/x` für Keramik, Cabrio, Selber-Waschen, AdBlue-Deaktivierung, Oldtimer, Leasing | Root-Varianten leiten bereits per 308 weiter | Ziele werden in Phase 1 auf die neuen Endziele umgestellt, damit keine Ketten entstehen. |
| `chiptuning-raumerfurt`, `softwareoptimierung-erfurt` | 404 (absichtlich gelöscht) | Siehe E1 |
| `/motorwaesche-erfurt-vorteile-kosten/` (Root) | **404** | Neuer 301 auf `/blog/motorwaesche-erfurt-vorteile-kosten/` |
| `/harte-und-weiche-…-lackaufbereitung/` (Root, ohne „-2“) | **404** | Neuer 301 |
| `/blog/wie-oft-auto-aufbereiten-lassen.html` | 200 | 301 auf `/blog/wie-oft-auto-aufbereiten-lassen/` |
| `/trockeneisreinigung` ohne Slash | 200 (kanonische Form) | Ändert sich mit E4 |
| Startseite ohne JSON-LD | Bestätigt | Phase 2 |
| — (neu) | **Alle `/blog/<slug>` ohne Slash liefern 200**, ebenso `/ratgeber/…`, `/index.html` und `/blog/index.html` | Phase 1, `trailingSlash: true` |
| — (neu) | `http://powertech-performance.com/x` braucht 2 Sprünge (zuerst https, dann www) | Unkritisch. Optional in den Vercel-Domain-Einstellungen bereinigen. |
| — (neu) | Vercel leitet mit **308** statt 301 weiter | Google behandelt 308 wie 301. Kein Handlungsbedarf. |

---

## 3. Stack, Build, Hosting, Redirects

- **Statisches HTML** ohne Build-Schritt und ohne CMS. Vanilla-JS (`js/main.js`, `js/tracking.js`, seitenspezifische Skripte), CSS unter `css/`.
- **Hosting: Vercel** (Projekt `powertech-performance-v4`, Edge `fra1`). Serverless-Funktion `api/send-lead.js` mit nodemailer für Formulare.
- **Redirects und Rewrites ausschließlich in `vercel.json`:** heute 67 Redirects (darunter 13 Regex-Muster `/landingpage/…/(.*)`) und 19 Rewrites, die endungslose Root-Pfade auf `*.html` abbilden. Es gibt keine `.htaccess`, kein `_redirects` und kein `netlify.toml`. `trailingSlash` und `cleanUrls` sind nicht gesetzt.
- **Host:** Apex → www und http → https über die Vercel-Domain-Konfiguration (308).
- **Tracking:** GTM mit Consent Mode inline im `<head>` (asynchron). Wird nicht angefasst.
- **Vorhandene SEO-Werkzeuge** unter `seo/tools/` (Python + BeautifulSoup). Sie arbeiten mit dem Datenmodell vom 07.09.; für dieses Audit habe ich einen eigenen, nur lesenden Scan verwendet.

---

## 4. Seiteninventar

62 HTML-Routen, davon 56 indexierbar. Die vollständige Tabelle mit Description-Texten, Bildzählung und allen Feldern liegt in **`seo/audit-2026-10-inventar.csv`** (UTF-8 mit BOM, Semikolon). Wörter = sichtbarer Text ohne Header, Navigation und Footer. „ein/aus“ = Anzahl unterschiedlicher interner Quell- bzw. Zielseiten.

**Auffälligkeiten in Zahlen**

- **H1:** Alle 62 Seiten haben genau eine H1. ✔
- **Canonical:** Auf allen Seiten vorhanden, absolut, mit www. Bei zwei Lackhärte-Fassungen zeigt er absichtlich auf die Hauptfassung. Das wird zu einem 301.
- **Title:** 45 von 56 indexierbaren Titles sind länger als 60 Zeichen, 11 länger als 80 (bis 118). Alle Titles sind einzigartig.
- **Description:** 18 sind länger als 160 Zeichen (bis 247). Zwei Seiten teilen sich dieselbe Description (die beiden Lackhärte-Duplikate).
- **JSON-LD fehlt** auf 17 indexierbaren Seiten, darunter **Startseite**, alle Stadtseiten, `/luxus-aufbereitung`, `/auto-handwaesche-erfurt`, `/blog/` und `/pages/kontakt.html`. LocalBusiness-Markup (`AutomotiveBusiness`) gibt es nur auf `/adblue-service`. Kein Blogartikel hat BlogPosting-Markup, nur BreadcrumbList.
- **WhatsApp-Link fehlt** auf: `/ads`, `/auto-handwaesche-erfurt`, `/blog/`, allen 6 Stadtseiten, `/fahrzeugaufbereitung-aus-erfurt`, `/glosar`, `/luxus-aufbereitung`, `/motorwaesche-trockeneis`, `/online-termin-buchen` und `/pages/kontakt.html`. Ein Telefonlink ist auf allen indexierbaren Seiten vorhanden.
- **Bilder:** 218 von 323 `<img>` haben kein `width`/`height` (CLS-Risiko), vor allem die Vorlagenseiten mit 14 von 15. 296 Bilder sind PNG oder JPG statt WebP/AVIF. Fehlende alt-Attribute: 0.
- **Verwaiste Seite:** `/ratgeber/leasingfahrzeug-keramikversiegelung` (0 eingehende Links)
- **Sitemap:** 55 URLs, aber nur **ein** `<lastmod>`. Sie enthält URLs, die in Phase 1 umziehen. `robots.txt` ist korrekt und verweist auf die Sitemap.
- **Zurück-Taste:** Kein `pushState`, `replaceState`, `popstate` oder `beforeunload` in den HTML-Dateien und in `js/*.js`. ✔ Skripte, die über GTM nachgeladen werden, lassen sich lokal nicht prüfen (TODO: GTM-Container sichten).
- **Render-blocking:** Keine externen synchronen Skripte im `<head>`. Die Skripte stehen am Ende von `<body>`. ✔
- **NAP auf der Website:** Powertech Performance · An der Klinge 10 · 99095 Erfurt · +49 173 7373574. Der Abgleich mit dem Google-Unternehmensprofil ist offen (TODO). **Öffnungszeiten stehen nirgends auf der Website.** Die E-Mail-Adresse lautet `info@powertech-performance.de`, die Website-Domain ist `.com`.
- **Bewertungen:** Auf der Startseite gibt es Chat-Screenshots („Kundenfeedback, direkt aus dem Chat“), aber keine Bewertungen mit Quellenangabe (z. B. Google) und kein Rating-Markup.

**Inventar (Kurzfassung)**

| URL | Title (Zeichen) | Desc. | H1 | Canonical | robots | Wörter | JSON-LD | ein/aus | Tel/WA |
|---|---|---:|---|---|---|---:|---|---|---|
| `/adblue-service` | AdBlue-Deaktivierung & AGR On-Off Erfurt \| Powertech Performance (64) | 146 | AdBlue-Deaktivierung und AGR On-Off in Erfurt | self | index | 1358 | AutomotiveBusiness, BreadcrumbList, FAQPage | 5/5 | j/j |
| `/ads` | Autoaufbereiter in Erfurt \| Powertech Performance (49) | 125 | Autoaufbereiter in Erfurt | self | index | 1159 | – | 1/7 | j/n |
| `/anfrage-danke` | Vielen Dank für Ihre Anfrage \| Powertech Performance (52) | 118 | Danke für deine Anfrage! | self | noindex | 169 | – | 1/7 | j/j |
| `/auto-handwaesche-erfurt` | Exklusive Auto-Handwäsche Erfurt \| Powertech Performance (56) | 144 | Exklusive Auto-Handwäsche in Erfurt | self | index | 543 | – | 2/7 | j/n |
| `/autoaufbereitung` | Autoaufbereitung Erfurt \| Innen, Lack & Pflege \| Powertech (58) | 155 | Autoaufbereitung in Erfurt, abgestimmt auf Ihr Fahrzeug. | self | index | 1022 | Service | 2/9 | j/j |
| `/blog/1-step-2-step-oder-lackkorrektur-lackaufbereitung-im-vergleich/` | 1-Step, 2-Step oder Lackkorrektur? Lackaufbereitung im Vergleich \| Powertech Performance (88) | 157 | 1-Step, 2-Step oder Lackkorrektur? Lackaufbereitung im Vergleich | self | index | 776 | BreadcrumbList | 5/9 | j/j |
| `/blog/1-step-politur-erklaert/` | 1-Step Politur erklärt – Glanz für den Autolack \| Powertech Performance (71) | 120 | 1-Step Politur erklärt – Glanz für den Autolack | self | index | 425 | BreadcrumbList | 2/8 | j/j |
| `/blog/adblue-deaktivieren-vor-nachteile-wahrheit/` | AdBlue deaktivieren: Risiken und Alternativen \| Powertech Performance (69) | 158 | AdBlue deaktivieren: Risiken, Grenzen und Alternativen | self | index | 598 | BreadcrumbList | 3/10 | j/j |
| `/blog/adblue-deaktivierung/` | AdBlue-Deaktivierung rückgängig machen: Prüfbedarf \| Powertech Performance (74) | 152 | AdBlue-Deaktivierung: Rückrüstung prüfen lassen | self | index | 418 | BreadcrumbList | 3/9 | j/j |
| `/blog/audi-r8-aufbereitung-erfurt-keramikversiegelung/` | Audi R8 Aufbereitung in Erfurt: High-End-Pflege & Werterhalt auf höchstem Niveau \| Powertech Performance (104) | 247 | Audi R8 Aufbereitung in Erfurt: High-End-Pflege & Werterhalt auf höchstem Niveau | self | index | 785 | BreadcrumbList | 2/8 | j/j |
| `/blog/aufbereiter-vs-detailer-unterschied/` | Aufbereiter vs. Detailer: Wo liegt der wahre Unterschied für Ihr Fahrzeug? \| Powertech Performance (98) | 155 | Aufbereiter vs. Detailer: Wo liegt der wahre Unterschied für Ihr Fahrzeug? | self | index | 675 | BreadcrumbList | 2/8 | j/j |
| `/blog/auto-selber-waschen-erfurt/` | Auto selber waschen in Erfurt: SB-Wäsche & Pflege \| Powertech Performance (73) | 152 | Auto selber waschen in Erfurt: SB-Wäsche und Pflege | self | index | 526 | BreadcrumbList | 2/10 | j/j |
| `/blog/blog-keramikversiegelung/` | Keramikversiegelung fürs Auto einfach erklärt \| Powertech Performance (69) | 164 | Keramikversiegelung fürs Auto einfach erklärt | self | index | 572 | BreadcrumbList | 2/10 | j/j |
| `/blog/boot-aufbereitung-keramikversiegelung-marine/` | Yacht- & Boot-Versiegelung: Maximaler Schutz gegen Salzwasser & Verwitterung \| Powertech Performance (100) | 166 | Yacht- & Boot-Versiegelung: Maximaler Schutz gegen Salzwasser & Verwitterung | self | index | 633 | BreadcrumbList | 2/8 | j/j |
| `/blog/fahrzeugaufbereitung-erfurt/` | Fahrzeugaufbereitung Erfurt: Glänzendes Auto mit PowerTech Performance \| Powertech Performance (94) | 124 | Fahrzeugaufbereitung Erfurt: Glänzendes Auto mit PowerTech Performance | self | index | 953 | BreadcrumbList | 2/9 | j/j |
| `/blog/flugzeugaufbereitung-innenreinigung-erfurt/` | Flugzeugaufbereitung & Innenreinigung Erfurt \| Powertech Performance (68) | 161 | Flugzeugaufbereitung & Innenreinigung Erfurt | self | index | 621 | BreadcrumbList | 2/8 | j/j |
| `/blog/haltbarkeit-keramikversiegelung-lackschutz/` | Haltbarkeit einer Keramikversiegelung: Wie lange hält der Lackschutz wirklich? \| Powertech Performance (102) | 150 | Haltbarkeit einer Keramikversiegelung: Wie lange hält der Lackschutz wirklich? | self | index | 639 | BreadcrumbList | 9/9 | j/j |
| `/blog/harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung-2/` | Harte und weiche Autolacke – zweite Artikelfassung \| Powertech Performance (74) | 149 | Harte und weiche Autolacke: Der geheime Schlüssel zur perfekten Lackaufbereitung | → /blog/harte-weiche-autolacke-lackaufbereitung/ | index | 670 | – | 1/8 | j/j |
| `/blog/harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung/` | Harte und weiche Autolacke – ältere Artikelfassung \| Powertech Performance (74) | 149 | Harte und weiche Autolacke: Der geheime Schlüssel zur perfekten Lackaufbereitung | → /blog/harte-weiche-autolacke-lackaufbereitung/ | index | 670 | – | 1/8 | j/j |
| `/blog/harte-weiche-autolacke-lackaufbereitung/` | Harte und weiche Autolacke: Lackhärte verstehen \| Powertech Performance (71) | 155 | Harte und weiche Autolacke: Was die Lackhärte bedeutet | self | index | 661 | BreadcrumbList | 5/8 | j/j |
| `/blog/` | Blog – Autoaufbereitung & Fahrzeugpflege \| Powertech Performance (64) | 137 | Blog | self | index | 1268 | – | 53/41 | j/n |
| `/blog/innenreinigung-auto-in-der-naehe/` | Innenreinigung Auto Erfurt – Umfang & Anfrage \| Powertech Performance (69) | 161 | Professionelle Auto-Innenreinigung in Erfurt | self | index | 943 | BreadcrumbList | 7/9 | j/j |
| `/blog/keramik-fuer-auto-erfurt-vorteile-haltbarkeit/` | Keramik fürs Auto: Nutzen und Pflegebedarf \| Powertech Performance (66) | 161 | Keramik fürs Auto: Nutzen und Pflegebedarf | self | index | 688 | BreadcrumbList | 2/10 | j/j |
| `/blog/keramikversiegelung-erfurt-high-end-lackschutz-powertech-performance/` | Keramikversiegelung: Lackzustand und Glanz \| Powertech Performance (66) | 161 | Keramikversiegelung: Lackzustand und Glanz | self | index | 758 | BreadcrumbList | 2/10 | j/j |
| `/blog/keramikversiegelung-profi-lackschutz/` | Keramikversiegelung: Profi oder selbst auftragen? \| Powertech Performance (73) | 168 | Keramikversiegelung: Profi oder selbst auftragen? | self | index | 525 | BreadcrumbList | 2/10 | j/j |
| `/blog/lackierung-oldtimer-erfurt-lackaufbereitung-keramik/` | Was Ihr Oldtimer Ihnen verschweigt: Warum eine einfache Politur Ihren Klassiker ruinieren kann \| Powertech Performance (118) | 192 | Was Ihr Oldtimer Ihnen verschweigt: Warum eine einfache Politur Ihren Klassiker ruinieren kann | self | index | 641 | BreadcrumbList | 2/8 | j/j |
| `/blog/lackkorrektur-wofuer-gut-werterhalt/` | Lackkorrektur: Wofür ist das gut? \| Powertech Performance (57) | 157 | Lackkorrektur: Wofür ist das gut? | self | index | 651 | BreadcrumbList | 5/8 | j/j |
| `/blog/leasing-rueckgabe-aufbereitung-erfurt/` | Leasingrückgabe-Aufbereitung in Erfurt \| Powertech Performance (62) | 158 | Aufbereitung vor der Leasingrückgabe in Erfurt | self | index | 522 | BreadcrumbList | 5/9 | j/j |
| `/blog/leasingauto-aufbereiten/` | Leasingauto zurückgeben – warum sich eine professionelle Aufbereitung wirklich lohnt \| Powertech Performance (108) | 135 | Leasingauto zurückgeben – warum sich eine professionelle Aufbereitung wirklich lohnt | self | index | 570 | BreadcrumbList | 2/9 | j/j |
| `/blog/leasingrueckgabe-checkliste/` | Leasingrückgabe-Checkliste: Fahrzeug vorbereiten \| Powertech Performance (72) | 155 | Leasingrückgabe-Checkliste: Vorbereitung und Übergabe | self | index | 479 | BreadcrumbList | 3/8 | j/j |
| `/blog/motorradaufbereitung-keramikversiegelung-experte/` | Motorradaufbereitung & Keramikschutz \| Powertech Performance Benjamin \| Powertech Performance (93) | 173 | Motorradaufbereitung & Keramikschutz | self | index | 612 | BreadcrumbList | 2/8 | j/j |
| `/blog/motorwaesche-erfurt-vorteile-kosten/` | Motorraumreinigung: Wann eignet sich Trockeneis? \| Powertech Performance (72) | 158 | Motorraumreinigung: Wann eignet sich Trockeneis? | self | index | 445 | BreadcrumbList | 3/9 | j/j |
| `/blog/oldtimer-aufbereitung-erfurt-wertschonende-pflege/` | Oldtimer Aufbereitung Erfurt \| Werterhalt & High-End Pflege \| Powertech Performance (83) | 209 | Oldtimer Aufbereitung Erfurt \| Werterhalt & High-End Pflege | self | index | 660 | BreadcrumbList | 2/8 | j/j |
| `/blog/porsche-aufbereitung-erfurt-keramikversiegelung-zertifiziert/` | Porsche Aufbereitung in Erfurt: Werterhalt & Perfektion für Ihren Sportwagen \| Powertech Performance (100) | 212 | Porsche Aufbereitung in Erfurt: Werterhalt & Perfektion für Ihren Sportwagen | self | index | 601 | BreadcrumbList | 2/8 | j/j |
| `/blog/professionelle-cabrioverdeck-impraegnierung-und-reinigung/` | Professionelle Cabrioverdeck Imprägnierung & Reinigung \| Powertech Performance (78) | 175 | Professionelle Cabrioverdeck Imprägnierung & Reinigung | self | index | 549 | BreadcrumbList | 2/8 | j/j |
| `/blog/professionelle-innenreinigung-auto-in-der-naehe/` | Auto-Innenreinigung: Termin richtig vorbereiten \| Powertech Performance (71) | 161 | Auto-Innenreinigung: So bereiten Sie den Termin vor | self | index | 485 | BreadcrumbList | 1/9 | j/j |
| `/blog/professionelle-keramikversiegelung-erfurt/` | Keramikversiegelung: Leistungsumfang verstehen \| Powertech Performance (70) | 165 | Keramikversiegelung: Leistungsumfang verstehen | self | index | 602 | BreadcrumbList | 2/10 | j/j |
| `/blog/profi-keramikversiegelung/` | Keramikversiegelung: Vorbereitung und Verarbeitung \| Powertech Performance (74) | 169 | Keramikversiegelung: Vorbereitung und Verarbeitung | self | index | 970 | BreadcrumbList | 2/10 | j/j |
| `/blog/was-kostet-eine-auto-reinigung/` | Was kostet eine Auto Innenreinigung? \| Powertech Performance (60) | 216 | Was kostet eine Auto Innenreinigung? | self | index | 496 | BreadcrumbList | 3/9 | j/j |
| `/blog/wie-lange-dauert-adblue-off/` | AdBlue-Probleme: Ablauf und Zeitbedarf der Prüfung \| Powertech Performance (74) | 156 | AdBlue-Probleme: Ablauf und Zeitbedarf klären | self | index | 441 | BreadcrumbList | 2/10 | j/j |
| `/blog/wie-oft-auto-aufbereiten-lassen.html` | Wie oft das Auto aufbereiten lassen? \| Powertech Performance (60) | 154 | Wie oft sollte man sein Auto professionell aufbereiten lassen? | self | index | 592 | BreadcrumbList | 2/9 | j/j |
| `/eisenach` | Autoaufbereitung für Eisenach – Termin in Erfurt \| Powertech Performance (72) | 149 | Autoaufbereitung für Kunden aus Eisenach – in Erfurt | self | index | 1250 | – | 2/8 | j/n |
| `/fahrzeugaufbereitung-aus-erfurt` | Fahrzeugaufbereitung Erfurt: Termin vorbereiten \| Powertech Performance (71) | 149 | Fahrzeugaufbereitung in Erfurt: Den Termin vorbereiten | self | index | 1237 | – | 3/8 | j/n |
| `/gera` | Autoaufbereitung für Gera – Termin in Erfurt \| Powertech Performance (68) | 145 | Autoaufbereitung für Kunden aus Gera – in Erfurt | self | index | 1250 | – | 2/8 | j/n |
| `/glosar` | Glossar – Autoaufbereitung in Erfurt \| Powertech Performance (60) | 105 | Glossar – Autoaufbereitung in Erfurt | self | index | 422 | – | 3/8 | j/n |
| `/gotha` | Autoaufbereitung für Gotha – Termin in Erfurt \| Powertech Performance (69) | 146 | Autoaufbereitung für Kunden aus Gotha – in Erfurt | self | index | 1250 | – | 2/8 | j/n |
| `/graffiti-entfernung-trockeneis` | Graffiti-Entfernung mit Trockeneis in Erfurt \| Powertech (56) | 145 | Graffiti- Entfernung mit Trockeneis. | self | index | 755 | Service | 2/4 | j/j |
| `/` | Autoaufbereitung Erfurt – Pflege & Werterhalt \| Powertech Performance (69) | 137 | Autoaufbereitung in Erfurt mit Tiefenglanz. | self | index | 703 | – | 61/23 | j/j |
| `/jena` | Autoaufbereitung für Jena – Termin in Erfurt \| Powertech Performance (68) | 145 | Autoaufbereitung für Kunden aus Jena – in Erfurt | self | index | 1250 | – | 2/8 | j/n |
| `/luxus-aufbereitung` | Keramikversiegelung Erfurt – Lackschutz & Pflege \| Powertech Performance (72) | 159 | Keramikversiegelung in Erfurt: Schutz für gepflegten Lack | self | index | 1245 | – | 11/9 | j/n |
| `/motorwaesche-trockeneis` | Motorwäsche mit Trockeneis in Erfurt – 150 € Festpreis \| Powertech Performance (78) | 142 | Motorwäsche mit Trockeneis. Motorraum wie neu. | self | index | 901 | Service | 4/9 | j/n |
| `/nordhausen` | Autoaufbereitung für Nordhausen – Termin in Erfurt \| Powertech Performance (74) | 151 | Autoaufbereitung für Kunden aus Nordhausen – in Erfurt | self | index | 1250 | – | 2/8 | j/n |
| `/online-termin-buchen` | Online Termin buchen \| Powertech Performance (44) | 136 | Besichtigungstermin vor Ort an der Halle buchen | self | index | 190 | – | 11/7 | j/n |
| `/pages/agb.html` | AGB – Powertech Performance (27) | 58 | Allgemeine Geschäftsbedingungen | self | noindex | 140 | – | 1/5 | n/n |
| `/pages/cookie-einstellungen.html` | Cookie-Einstellungen – Powertech Performance (44) | 117 | Cookie-Einstellungen | self | noindex | 119 | – | 61/4 | n/n |
| `/pages/datenschutz.html` | Datenschutzerklärung – Powertech Performance (44) | 0 | Datenschutzerklärung | self | noindex | 4370 | – | 61/4 | n/j |
| `/pages/impressum.html` | Impressum – Powertech Performance (33) | 0 | Impressum | self | noindex | 166 | – | 61/4 | j/n |
| `/pages/kontakt.html` | Kontakt – Powertech Performance \| Autoaufbereitung Erfurt (57) | 157 | Kontakt | self | index | 215 | – | 54/7 | j/n |
| `/pages/seitenuebersicht.html` | Seitenübersicht – Powertech Performance (39) | 54 | Seitenübersicht | self | noindex | 306 | – | 58/21 | j/n |
| `/ratgeber/leasingfahrzeug-keramikversiegelung` | Leasingfahrzeug schützen: Keramikversiegelung in Erfurt (55) | 170 | Leasingrückgabe kann teuer werden. Schützen Sie den Lack, bevor Schäden ins Geld gehen. | self | index | 1323 | Article, BreadcrumbList, FAQPage | 0/11 | j/j |
| `/suhl` | Autoaufbereitung für Suhl – Termin in Erfurt \| Powertech Performance (68) | 145 | Autoaufbereitung für Kunden aus Suhl – in Erfurt | self | index | 1250 | – | 2/8 | j/n |
| `/trockeneisreinigung` | Trockeneisreinigung Erfurt – Fahrzeug & Unterboden \| Powertech Performance (74) | 156 | Trockeneisreinigung am Fahrzeug in Erfurt | self | index | 610 | Service | 4/10 | j/j |

---

## 5. Duplikat- und Kannibalisierungsgruppen

Die Ähnlichkeit ist als Jaccard-Wert über 5-Wort-Folgen des sichtbaren Texts gemessen, bei Stadtseiten ohne den Ortsnamen. Inhaltliche Überschneidung beweist noch kein Ranking-Problem; die GSC-Daten im Prompt deuten aber für D1, D3 und D5 darauf hin.

| Gruppe | URLs | Befund |
|---|---|---|
| **D1 Slash-/Index-Duplikate** | 35 × `/blog/<slug>` ohne Slash, `/ratgeber/leasingfahrzeug-keramikversiegelung/`, `/index.html`, `/blog/index.html` | Alle liefern 200 neben der kanonischen URL; nur der Canonical unterscheidet sie |
| **D2 AdBlue** | `/adblue-service`, `/blog/adblue-deaktivieren-vor-nachteile-wahrheit/`, `/blog/adblue-deaktivierung/`, `/blog/wie-lange-dauert-adblue-off/`, `/adblue-deaktivieren/` (404) | Root und Blog des Hauptartikels sind bereits zusammengeführt. `wie-lange-dauert-adblue-off` ist dünn (441 Wörter) und überschneidet sich mit dem Hauptartikel → Phase 4 |
| **D3 Fahrzeug-/Autoaufbereitung Erfurt** | `/`, `/autoaufbereitung`, `/fahrzeugaufbereitung-aus-erfurt`, `/blog/fahrzeugaufbereitung-erfurt/`, `/ads` | Fünf Seiten bedienen eine Suchintention. `/fahrzeugaufbereitung-aus-erfurt` und `/ads` sind zu 90 % identisch |
| **D4 Stadtseiten-Vorlage** | `/gotha`, `/jena`, `/suhl`, `/gera`, `/nordhausen`, `/eisenach` (+ zu 84–90 % `/luxus-aufbereitung`, `/fahrzeugaufbereitung-aus-erfurt`, `/ads`) | **100 % textgleich** bis auf den Ortsnamen → Doorway-Risiko nach 2.2 |
| **D5 Keramik** | `/luxus-aufbereitung`, `/blog/blog-keramikversiegelung/`, `/blog/profi-keramikversiegelung/`, `/blog/professionelle-keramikversiegelung-erfurt/`, `/blog/haltbarkeit-keramikversiegelung-lackschutz/`, `/blog/keramik-fuer-auto-erfurt-vorteile-haltbarkeit/`, `/blog/keramikversiegelung-erfurt-high-end-lackschutz-powertech-performance/`, `/blog/keramikversiegelung-profi-lackschutz/` | 8 URLs zu einem Thema, Textgleichheit 16–29 %. Daneben fahrzeugspezifisch: Audi R8, Porsche, Boot, Motorrad, `/ratgeber/leasingfahrzeug-keramikversiegelung` |
| **D6 Lackhärte** | `/blog/harte-weiche-autolacke-lackaufbereitung/` + zwei lange `…-geheime-schlssel…`-Slugs (einer mit „-2“) | 91–98 % identisch; heute nur per Canonical zusammengeführt |
| **D7 Politur / Lackkorrektur** | `/blog/1-step-politur-erklaert/`, `/blog/1-step-2-step-oder-lackkorrektur-…/`, `/blog/lackkorrektur-wofuer-gut-werterhalt/` | Die 1-Step-Erklärung ist im Vergleichsartikel enthalten. Eine Leistungsseite für Lack fehlt ganz |
| **D8 Innenreinigung** | `/blog/innenreinigung-auto-in-der-naehe/` (Leistungscharakter), `/blog/professionelle-innenreinigung-auto-in-der-naehe/`, `/blog/was-kostet-eine-auto-reinigung/` | Unterschiedliche Fragen, aber keine echte Leistungsseite |
| **D9 Leasing** | `/blog/leasing-rueckgabe-aufbereitung-erfurt/`, `/blog/leasingauto-aufbereiten/`, `/blog/leasingrueckgabe-checkliste/`, `/ratgeber/leasingfahrzeug-keramikversiegelung` | `leasing-rueckgabe…` und `leasingauto-aufbereiten` decken dieselbe Frage ab („Lohnt sich die Aufbereitung vorher?“) |
| **D10 Oldtimer** | `/blog/oldtimer-aufbereitung-erfurt-wertschonende-pflege/`, `/blog/lackierung-oldtimer-erfurt-lackaufbereitung-keramik/` | Zwei Blogartikel, keine Leistungsseite |
| D11 Motor / Trockeneis | `/motorwaesche-trockeneis`, `/trockeneisreinigung`, `/blog/motorwaesche-erfurt-vorteile-kosten/` | Klar abgegrenzt (Leistung, Leistung, Ratgeber). Hier ist nichts zu tun |

---

## 6. Redirect-Map (Vorschlag – nichts davon ist umgesetzt)

Alle Ziele mit `https://www.powertech-performance.com`. Vercel liefert sie als 308 (`permanent: true`). Wo eine bestehende Weiterleitung auf eine URL zeigt, die selbst umzieht, wird sie **direkt auf das Endziel** umgestellt, damit keine Ketten entstehen. Die Spalte „Entsch.“ verweist auf Abschnitt 1.

### 6.1 Global (Phase 1)

| Alt | Ziel | Begründung | Entsch. |
|---|---|---|---|
| alle Pfade ohne Slash (außer Dateien mit Endung) | gleicher Pfad mit `/` | Einheitliches Schema; behebt D1 | E4 |
| `/index.html` | `/` | Index-Duplikat | – |
| `/blog/index.html` | `/blog/` | Index-Duplikat | – |
| bestehende Regeln `/gotha/`→`/gotha`, `/suhl/`, `/gera/`, `/nordhausen/`, `/online-termin-buchen/`, `/trockeneisreinigung/`, `/motorwaesche-trockeneis/`, `/autoaufbereitung/` | **entfernen** | Würden mit `trailingSlash` eine Schleife erzeugen | E4 |
| `/landingpage/<x>` und `/<x>.html` (bestehend) | auf das neue Endziel mit Slash umstellen | Keine Ketten | – |

### 6.2 Inhaltliche Zusammenführungen

| Alt | Ziel | Begründung | Entsch. |
|---|---|---|---|
| `/autoaufbereitung` (+ `.html`) | `/fahrzeugaufbereitung-erfurt/` | Eine Money Page für die Intention „Fahrzeug-/Autoaufbereitung Erfurt“ | E3 |
| `/fahrzeugaufbereitung-erfurt/` | wird **200** (die heutige Weiterleitung auf den Blog fällt weg) | Neue Leistungsseite | E3 |
| `/blog/fahrzeugaufbereitung-erfurt/` | `/fahrzeugaufbereitung-erfurt/` | Der Blogartikel konkurriert mit der Leistungsseite (Pos. 42,5) | E3 |
| `/fahrzeugaufbereitung-aus-erfurt` (+ `.html`, `/landingpage/…`) | `/fahrzeugaufbereitung-erfurt/` | Vorlagen-Duplikat (90 % gleich wie `/ads`) | E3 |
| `/luxus-aufbereitung` (+ `.html`, `/landingpage/…`) | `/keramikversiegelung-erfurt/` | Neue Keramik-Leistungsseite | E9 |
| `/blog/professionelle-keramikversiegelung-erfurt/` (+ Root) | `/keramikversiegelung-erfurt/` | „Leistungsumfang verstehen“ ist eine Leistungsintention | E6 |
| `/blog/profi-keramikversiegelung/` (+ Root) | `/keramikversiegelung-erfurt/` | „Vorbereitung und Verarbeitung“ gehört als Ablauf auf die Leistungsseite | E6 |
| `/blog/keramikversiegelung-erfurt-high-end-lackschutz-powertech-performance/` | `/keramikversiegelung-erfurt/` | Leistungsintention mit Ortsbezug | E6 |
| `/blog/haltbarkeit-keramikversiegelung-lackschutz/` | `/blog/keramikversiegelung-haltbarkeit/` | Wird zum Keramik-Ratgeber (hat heute die meisten eingehenden Links: 9) | E6 |
| `/blog/blog-keramikversiegelung/` | `/blog/keramikversiegelung-haltbarkeit/` | Grundlagen-Info, im Ratgeber aufgehen lassen | E6 |
| `/blog/keramik-fuer-auto-erfurt-vorteile-haltbarkeit/` (+ Root) | `/blog/keramikversiegelung-haltbarkeit/` | Gleiche Frage („Nutzen und Haltbarkeit“) | E6 |
| `/blog/keramikversiegelung-profi-lackschutz/` | `/blog/keramikversiegelung-haltbarkeit/` | Laut Prompt. *Alternative:* behalten, weil „Profi oder selbst auftragen?“ eine eigene Frage ist | E6 |
| `/blog/harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung/` (+ Root) | `/blog/harte-weiche-autolacke-lackaufbereitung/` | Duplikat (91 %), defekter Umlaut im Slug | – |
| `/blog/harte-und-weiche-…-lackaufbereitung-2/` (+ Root) | `/blog/harte-weiche-autolacke-lackaufbereitung/` | Duplikat (98 %), „-2“-Suffix | – |
| `/blog/1-step-politur-erklaert/` | `/blog/1-step-2-step-oder-lackkorrektur-lackaufbereitung-im-vergleich/` | Inhalt ist im Vergleichsartikel enthalten (D7) | Vorschlag |
| `/blog/wie-oft-auto-aufbereiten-lassen.html` | `/blog/wie-oft-auto-aufbereiten-lassen/` | `.html`-Ausreißer; Datei wird in einen Ordner verschoben | – |
| `/motorwaesche-erfurt-vorteile-kosten/` (Root, heute 404) | `/blog/motorwaesche-erfurt-vorteile-kosten/` | Fehlende Root-Variante laut GSC | – |
| `/adblue-deaktivieren/` (heute 404) | `/blog/adblue-deaktivieren-vor-nachteile-wahrheit/` | Gleiche Intention; seit 07.09. offen | – |
| `/adblue-deaktivieren-vor-nachteile-wahrheit/` | `/blog/adblue-deaktivieren-vor-nachteile-wahrheit/` | **besteht bereits**, bleibt | – |
| `/adblue-service` (+ `.html`, `/landingpage/…`) | `/adblue-diagnose-erfurt/` | Umstellung auf eine legale Leistung | E2 |
| `/blog/wie-lange-dauert-adblue-off/` | `/blog/adblue-deaktivieren-vor-nachteile-wahrheit/` | Dünn, „off“ im Slug, Inhalt überschneidet sich → im Hauptartikel aufgehen lassen | Phase 4 |
| `/blog/adblue-deaktivierung/` | behalten (Rückrüstung prüfen = eigene Frage) **oder** in den Hauptartikel | Phase 4 | Phase 4 |
| `/chiptuning`, `/blog/chiptuning-raum-erfurt/`, `/blog/chiptuning-raumerfurt/`, `/blog/softwareoptimierung-erfurt/`, `/blog/softwareoptimierung-dpf-off-erfurt/` + Root-Varianten | **bleiben 404** (optional 410) | Absichtlich gelöscht, kein thematisch passendes Ziel | E1 |
| `/ads` | kein Redirect, sondern `noindex` | Ads-Landingpage | E8 |

### 6.3 Leistungsseiten aus Blogartikeln (Phase 2, Vorschlag)

| Leistung | Heute | Vorschlag |
|---|---|---|
| Lackaufbereitung & Lackkorrektur | nur Ratgeber | neu: `/lackaufbereitung-erfurt/` |
| Keramikversiegelung | `/luxus-aufbereitung` (Vorlage) | `/keramikversiegelung-erfurt/` (siehe 6.2) |
| Innenraumreinigung | `/blog/innenreinigung-auto-in-der-naehe/` (Leistungscharakter) | `/innenraumreinigung-erfurt/`, 301 vom Blogartikel |
| Trockeneisreinigung | `/trockeneisreinigung` | bleibt (mit Slash) |
| Motorwäsche | `/motorwaesche-trockeneis` | bleibt (mit Slash) |
| Cabrioverdeck | `/blog/professionelle-cabrioverdeck-impraegnierung-und-reinigung/` | `/cabrioverdeck-reinigung-erfurt/`, 301 vom Blogartikel |
| Oldtimer-Aufbereitung | 2 Blogartikel | `/oldtimer-aufbereitung-erfurt/`, 301 von `…wertschonende-pflege/`; der Lackier-Artikel bleibt Ratgeber |
| Leasingrückgabe | `/blog/leasing-rueckgabe-aufbereitung-erfurt/` | `/leasingrueckgabe-aufbereitung-erfurt/`, 301; `leasingauto-aufbereiten` → Ratgeber „Lohnt sich eine Aufbereitung vorher?“ |
| Softwareoptimierung / Chiptuning | gelöscht | **entfällt** (E1) |
| Handwäsche, Graffiti-Entfernung | vorhanden | bleiben (mit Slash) |

### 6.4 Stadtseiten (Phase 3, abhängig von E5)

| Alt | Ziel ohne Stadt-Fakten | Ziel mit Stadt-Fakten |
|---|---|---|
| `/gotha`, `/jena`, `/suhl`, `/gera`, `/nordhausen`, `/eisenach` (+ `.html`, `/landingpage/…`, Slash-Varianten) | `/einzugsgebiet/` | `/fahrzeugaufbereitung-<stadt>/` |

---

## 7. Was ich von Ihnen brauche (Fakten statt Erfindung)

Diese Angaben setze ich bis zur Klärung als `<!-- TODO -->`:

1. Entscheidungen **E1–E11** (Abschnitt 1)
2. **Öffnungszeiten** und Link zum **Google-Unternehmensprofil** (für den NAP-Abgleich und `sameAs`), dazu Social-Profile
3. **Preisrahmen „ab …“** für Pakete. Belegt sind auf der Website bisher nur: Motorwäsche 150 € Festpreis, Handwäsche-Aktion 50 €, Keramik „ab 1.000 €“
4. **Keramik-Produkt/-Hersteller und Zertifikate.** Auf der Website steht „IHK-zertifizierte Fachberatung“; einen Nachweis dafür gibt es im Repo nicht
5. **Echte Bewertungen mit Quelle** (z. B. Google-Bewertungen), sofern sie eingebunden werden sollen
6. **Vorher/Nachher-Fotos:** Im Repo liegen `images/galerie-1…4.jpg`, `images/kundenreferenzen/*.webp` und das Startseiten-Slider-Paar. Sind das eigene Arbeiten?
7. **Hol- & Bringservice:** ja/nein, Radius, Kosten
8. **Beispielaufträge pro Stadt** (für E5)
9. **SB-Waschanlage** ja/nein (E7)
10. **AdBlue:** Führt Powertech Reparaturen selbst aus oder nur die Diagnose? (E2)
11. Den **GTM-Container** auf Exit-Intent- oder History-Skripte prüfen (kann ich lokal nicht einsehen)

---

## 8. Dateien dieser Phase

- `seo-audit.md` (dieses Dokument, neu)
- `seo/audit-2026-10-inventar.csv` (vollständiges Inventar, neu)

An Website-Dateien, `vercel.json`, Sitemap, Formularen und Tracking wurde nichts geändert. **Phase 1 beginnt erst nach Ihrer Freigabe.**

---

## 9. Umsetzung am 12.10.2026 (lokal, noch nicht veröffentlicht)

Freigabe: „Ja, mach alles, was richtig ist, aber Autoaufbereitung bleibt.“ Damit gelten alle Empfehlungen aus Abschnitt 1, mit einer Abweichung bei E3: **`/autoaufbereitung/` bleibt die Money Page**. `/fahrzeugaufbereitung-erfurt/`, `/blog/fahrzeugaufbereitung-erfurt/` und `/fahrzeugaufbereitung-aus-erfurt` leiten dorthin.

### Umgesetzt

| Entscheidung | Umsetzung |
|---|---|
| E1 Chiptuning | Nicht wieder angelegt; alte URLs bleiben 404 |
| E2 AdBlue | `/adblue-service` → `/adblue-diagnose-erfurt/`: Diagnose, Reparaturweg, Rückrüstung; Deaktivierung und AGR On-Off entfernt (auch im Glossar und auf der Startseite). Ratgeber zu Nachteilen, TÜV, Strafe und Rechtslage mit Quellen ausgebaut. `AGENTS.md`, `SEO-RULES.md` und `business-policy.json` angepasst |
| E3 Money Page | `/autoaufbereitung/` geschärft: Title deckt Auto- und Fahrzeugaufbereitung ab, Faktenleiste (Dauer 4–10 h), Links zu allen Einzelleistungen, echte Fotos, Service- und BreadcrumbList-Markup |
| E4 Slash-Schema | Explizite Slash-Regel in `vercel.json`, spezifische Weiterleitungen gehen in **einem** Sprung zum Ziel; `/api`, `/ads`, `/anfrage-danke` und Dateien ausgenommen |
| E5 Stadtseiten | Sechs identische Seiten → `/einzugsgebiet/` (eine Seite mit Entfernungen, Ablauf für auswärtige Kunden, Leistungen) |
| E6 Keramik | Leistungsseite `/keramikversiegelung-erfurt/`, Ratgeber `/blog/keramikversiegelung-haltbarkeit/`; sieben weitere Keramik-URLs per 301. Fahrzeugspezifische Artikel bleiben |
| E7 Selber waschen | Ausgerichtet auf „Selber waschen oder aufbereiten lassen?“; Wettbewerberliste entfernt |
| E8 `/ads` | `noindex, follow`; Tracking, Formular und URL unverändert |
| E9 | Neue Leistungsseiten: Lackaufbereitung, Keramik, Innenraum, Cabrioverdeck, Oldtimer, Leasingrückgabe |
| E10 | `/kontakt/` statt `/pages/kontakt.html` (301) |
| E11 | Ratgeber `/ratgeber/leasingfahrzeug-keramikversiegelung/` ist jetzt von drei Seiten verlinkt |

Außerdem:
- Startseite mit neuem Title und AutomotiveBusiness-JSON-LD
- BlogPosting-Markup in allen 20 Artikeln
- BreadcrumbList-Markup auf allen Unterseiten
- Titles mit höchstens 62 Zeichen und Descriptions mit 140–160 Zeichen
- Mobile Anruf-/WhatsApp-Leiste auf allen Seiten außer `/ads`
- Alle Bilder als WebP mit `width`/`height` sowie `loading="lazy"`; Hero mit `fetchpriority="high"`
- Sitemap mit 39 finalen URLs inklusive `<lastmod>`

**Prüfergebnis (lokal, mit dem offiziellen Vercel-Routing-Compiler):** 301 Test-URLs. Alle Sitemap-URLs liefern direkt 200, jede Weiterleitung braucht höchstens einen Sprung, es gibt keine internen Links auf Weiterleitungen und keine kaputten internen Links. Alle JSON-LD-Blöcke sind gültiges JSON, jede Seite hat genau eine H1.

**Werkzeuge:** `seo/tools/urlmap.py` (zentrale URL-Zuordnung), `build-routing.py` (→ `vercel.json`), `rewrite-links.py` (Links und Canonicals), `build-sitemap.py`.

### Nach der Veröffentlichung

1. Live mit `curl -I` prüfen: Stichproben der Redirect-Map sowie `/ads`, `/anfrage-danke`, `/api/send-lead` (Formular) und einen Testversand nur nach Absprache.
2. Google Ads: Ziel-URLs prüfen. `/ads` bleibt gleich. Kampagnen auf andere Seiten sollten auf die neuen Slash-URLs zeigen (sonst ein zusätzlicher Sprung).
3. Search Console: Sitemap neu einreichen und die Seiten `/autoaufbereitung/`, `/keramikversiegelung-erfurt/`, `/lackaufbereitung-erfurt/` und `/einzugsgebiet/` zur Indexierung anmelden. Den Bericht „Generative KI-Funktionen“ beobachten.
4. Rich Results Test bzw. Schema-Validator und Lighthouse mobil laufen lassen. Das ist lokal nicht gemessen.

### Offene TODOs (im HTML als `<!-- TODO -->` markiert)

- Öffnungszeiten, Geo-Koordinaten, Link zum Google-Unternehmensprofil und Social-Profile (`sameAs`); NAP-Abgleich
- Preisrahmen „ab …“ für Pakete, Lack, Innenraum und Cabrio; ab-Preis 1.000 € für Keramik und Oldtimer bestätigen
- Keramik: Produkt/Hersteller und Garantiebedingungen (bisher widersprüchlich: 2 Jahre / 50.000 km / 3–5 Jahre)
- Cabrio: Standzeit der Imprägnierung bestätigen
- Zertifikate (IHK, Keramik-Hersteller) mit Nachweis
- Echte Vorher/Nachher-Fotos (Lack, Keramik, Oldtimer, Leasing)
- Echte Bewertungen mit Quelle
- Hol- und Bringservice; Beispielaufträge pro Stadt
- AdBlue: Welche Reparaturen führt Powertech selbst aus?
- SB-Waschmöglichkeit: ja oder nein?
- GTM-Container auf Skripte prüfen, die die Zurück-Navigation manipulieren
