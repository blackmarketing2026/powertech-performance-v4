# Powertech Glanz: Designreferenz

Quelle: lokaler Lovable-Export `C:\Users\Steve\Downloads\powertech-glanz-erfurt`, übernommen nach `lovable-glanz/`. Maßgeblich für die neue Seite sind `lovable-glanz/src/index.css`, `lovable-glanz/tailwind.config.ts` und die Komponenten unter `lovable-glanz/src/components/`.

## Farben

| Rolle | Originalwert | Verwendung |
| --- | --- | --- |
| Hintergrund | `hsl(0 0% 98%)` | helle Seitenfläche |
| Vordergrund | `hsl(283 30% 15%)` | Text und Überschriften |
| Primär | `hsl(283 20% 45%)` | Buttons, Links, Icons |
| Sekundär | `hsl(300 15% 81%)` | Flächen und Akzente |
| Gedämpft | `hsl(300 12% 92%)` | ruhige Flächen |
| Rahmen | `hsl(300 12% 88%)` | Karten und Eingaben |
| Weiß | `hsl(0 0% 100%)` | Karten und Kontrasttext |

Verläufe: Primär von `hsl(283 20% 45%)` zu `hsl(283 25% 55%)`; dezenter Seitenverlauf von `hsl(0 0% 98%)` zu `hsl(300 15% 95%)`. Akzente sind gedämpft violett. WhatsApp behält sein erkennbares Grün.

## Schrift und Logo

Der Export lädt keine externe Schriftdatei. Tailwind verwendet die Systemschrift `ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`. Überschriften sind kräftig, klar und dunkel; Fließtext ist zurückhaltend. Das exportierte Logo ist `lovable-glanz/src/assets/logo.png` (378 × 342 px, transparenter Hintergrund). Es zeigt denselben violetten Fahrzeug-Zahnrad-Bildmarkenkern wie das vorhandene Powertech-Logo. Auf der neuen Seite wird die transparente Exportdatei direkt verwendet; die übrigen Seiten behalten ihre vorhandenen Versionen derselben Bildmarke.

## Aufbau und Komponenten

- Fixierter heller Header mit transparentem Logo und einem violetten Anfrage-Button.
- Hoher Hero mit Fahrzeugfoto, hellem Verlauf, großer linksbündiger Überschrift und vier halbtransparenten Vorteils-Karten.
- Luftige Abschnitte mit mittiger Einführung, abwechselnd fast weißem und dezent violettem Hintergrund.
- Weiße Karten mit weichen Ecken (`0.75rem`), feinem Rand und zurückhaltendem Schatten.
- Violetter Abschluss-CTA, danach zweispaltiger Kontaktbereich und ruhiger Footer.
- Mobile Darstellung über einspaltige Grids; Abstände und Schriftgrößen werden kleiner.

## Umsetzung im bestehenden Projekt

`css/design-system.css` überträgt Farben, Systemschrift, Buttons, Formfelder und Kartenstil auf die bestehenden statischen Seiten. Spezifische Seiten-CSS-Dateien behalten ihre Layouts, damit bestehende Bildaufteilungen, Formulare, Ads und Sonderseiten intakt bleiben. Neue Seiten verwenden diese Tokens; bestehende Routen, Tracking, GTM und Rechtstexte bleiben erhalten.

Die exportierte 50.000-km-Garantie und pauschale Preisangaben sind im Zielprojekt nicht bestätigt. Die übernommene Seite verwendet deshalb belegbare Formulierungen und führt die Bedingungen im Angebot an. Die neue Seite ist bis zur SEO-Entscheidung `noindex,follow` und verweist per Canonical auf die bestehende Keramik-Leistungsseite.
