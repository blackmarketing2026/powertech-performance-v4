# Powertech Performance — Website

Domain: https://powertech-performance.com/

Autoaufbereitung Erfurt (Inhaber: Benjamin Lemmer). Startseite inhaltlich an
[powertech-performance.com](https://www.powertech-performance.com/) angelehnt und überarbeitet.

## Struktur

```
/
├── index.html                     Startseite
├── css/style.css                  Styles & Design-Tokens
├── js/main.js                     Navigation, Lead-Formulare, Cookie-Consent
├── api/send-lead.js               Vercel Serverless Function: Formularversand per SMTP
├── api/_lib/lead-email.js         Baut das HTML-E-Mail-Template für Leads
├── package.json                   Abhängigkeiten (nodemailer) für api/send-lead.js
├── images/                        Bild-Assets
├── pages/
│   ├── impressum.html
│   ├── datenschutz.html
│   ├── agb.html
│   └── cookie-einstellungen.html
├── sitemap.xml
└── robots.txt
```

## Formularversand (Kontaktformulare & Quiz)

Jedes Formular/Quiz auf der Website, das Leads einsammeln soll, wird über einen
gemeinsamen Endpunkt verschickt: **`/api/send-lead`** (Vercel Serverless Function,
`api/send-lead.js`, nutzt `nodemailer` per SMTP).

### Umgebungsvariablen (im Vercel-Projekt hinterlegt)

| Variable          | Bedeutung                                  |
|-------------------|---------------------------------------------|
| `smtp_server`     | SMTP-Host                                    |
| `smtp_benutzer`   | SMTP-Benutzername / Absenderadresse          |
| `smtp_passwort`   | SMTP-Passwort                                |
| `smtp_empfaenger` | Zieladresse, an die alle Leads gesendet werden |
| `smtp_port`       | optional, Standard `465` (SSL)               |

Diese Variablen sind in Vercel unter *Project → Environment Variables* für
*Production* und *Preview* gesetzt und werden nicht im Repository gespeichert.

### Wie ein Formular angebunden wird

Ein Formular wird automatisch an `/api/send-lead` angebunden, wenn es:

1. die Klasse `lead-form` trägt,
2. ein `data-form-name="..."` Attribut hat (erscheint im Betreff der E-Mail),
3. Felder `name`, `email` und `message` enthält (Pflichtfelder — weitere Felder
   wie `phone` oder `vehicle` sind optional und werden automatisch mitgesendet),
4. ein verstecktes Honeypot-Feld `website` besitzt (Spam-Schutz — siehe
   `index.html`, Klasse `.honeypot`).

`js/main.js` (Funktion `initLeadForms`) übernimmt den Rest: Absenden per
`fetch`, Lade-/Erfolgs-/Fehlerstatus im Formular, Zurücksetzen nach Erfolg.

Beispiel — bestehendes Kontaktformular auf der Startseite:

```html
<form class="lead-form" data-form-name="Kontaktformular Startseite" novalidate>
  ...
  <p class="form-status" data-form-status role="status" aria-live="polite"></p>
</form>
```

Ein künftiges Quiz-Formular muss nur dasselbe Muster übernehmen (`lead-form`
Klasse + eigener `data-form-name`), um über denselben E-Mail-Versand zu laufen.

### E-Mail-Template

Die Lead-Mail an `smtp_empfaenger` wird als gestaltetes HTML-Template verschickt
(`api/_lib/lead-email.js`, Funktion `buildLeadEmailHtml`) — mit Logo im Header
(`images/logo-klein.png`, über die absolute Domain `powertech-performance.com`
eingebunden, da E-Mail-Clients keine relativen Pfade laden) und den
Markenfarben der Website. Ein reiner Text-Fallback wird zusätzlich mitgesendet.

Das Template zeigt automatisch passende Aktions-Buttons, je nachdem welche
Felder im jeweiligen Formular ausgefüllt wurden:

| Feld im Formular vorhanden | Button(s) im E-Mail-Header |
|-----------------------------|------------------------------|
| `phone`                     | 💬 WhatsApp (`wa.me/...`) **und** 📞 Anrufen (`tel:...`) |
| `email`                     | ✉️ E-Mail schreiben (`mailto:...`) |

Alle übrigen Formularfelder (`name`, `vehicle`, `message`, sowie beliebige
weitere Felder künftiger Quiz-Formulare) werden darunter als übersichtliche
Liste dargestellt — unbekannte Feldnamen werden automatisch als Label
großgeschrieben, ohne dass am Template etwas angepasst werden muss.

Telefonnummern werden automatisch für `wa.me`/`tel:` normalisiert (führende
`0` wird zu `+49`, Leerzeichen/Sonderzeichen werden entfernt).

### Lokale Entwicklung / Deployment

Der Formularversand läuft nur auf Vercel (oder lokal mit `vercel dev`), da
`api/send-lead.js` eine Serverless Function ist. Bei einem einfachen
`npx serve` o. Ä. ohne Vercel-Runtime schlägt der Versand fehl (kein `/api`-Handler).

```
npm install       # installiert nodemailer für api/send-lead.js
vercel dev         # lokale Entwicklung inkl. Serverless Functions
```

## Cookie-Consent & Tracking (TTDSG/DSGVO)

Der Cookie-Banner (`js/main.js`, Funktionen rund um `initCookieConsent`) ist
rechtssicher nach TTDSG §25 / DSGVO aufgebaut:

- Drei Kategorien: **Notwendig** (immer an), **Statistik** (Google Analytics,
  Microsoft Clarity), **Marketing** (Google Ads Remarketing)
- „Alle ablehnen“ ist genauso leicht erreichbar wie „Alle akzeptieren“, keine
  vorausgewählten optionalen Kategorien
- Einwilligung wird 12 Monate in `localStorage` gespeichert und bei jedem
  Seitenaufruf geprüft; Änderung jederzeit über **/pages/cookie-einstellungen.html**
  (auch im Footer jeder Seite verlinkt)
- Technisch über **Google Consent Mode v2**: `gtag('consent','default', ...)`
  setzt vor dem Laden von GTM alles auf `denied`; erst nach Nutzer-Einwilligung
  wird per `gtag('consent','update', ...)` freigegeben. Microsoft Clarity nutzt
  keinen Google-Consent-Mechanismus und wird deshalb erst nach erteilter
  Statistik-Einwilligung eigenständig nachgeladen (`loadClarity()` in `js/main.js`)

### ⚠️ Platzhalter-IDs eintragen

Es liegen noch keine echten Tracking-IDs vor. Vor Go-live müssen folgende
Platzhalter ersetzt werden:

| Platzhalter | Wo | Ersetzen durch |
|---|---|---|
| `GTM-XXXXXXX` | in **jeder** HTML-Datei (Head-Script + noscript-iframe nach `<body>`) sowie in `api/../lib/templates.js` (Konstante `GTM_CONTAINER_ID`) | echte GTM-Container-ID |
| `XXXXXXXXXX` | `js/main.js`, Konstante `CLARITY_PROJECT_ID` | echte Microsoft-Clarity-Projekt-ID |

Da alle generierten Seiten (Blog, Landingpages) aus `lib/templates.js`
erzeugt werden, reicht es dort, `GTM_CONTAINER_ID` zu ändern und die
Generator-Skripte erneut laufen zu lassen — die von Hand gepflegten Seiten
(`index.html`, `pages/*.html`, `blog/wie-oft-auto-aufbereiten-lassen.html`)
müssen einzeln angepasst werden (Suche nach `GTM-XXXXXXX`).

GA4 und Google Ads Remarketing werden als Tags *innerhalb* von GTM
konfiguriert (Google-Tag-Manager-Oberfläche, nicht im Code dieses Repos).

## Schriften (Google Fonts, lokal gehostet)

„Red Hat Display“ und „Caveat“ liegen als `.woff2`-Dateien lokal unter
`fonts/` und werden über `@font-face` in `css/style.css` eingebunden — es
findet **keine Verbindung zu Google** beim Seitenaufruf statt (siehe
Datenschutzerklärung, Abschnitt 6).

## Status

Startseite inhaltlich fertig, Formularversand angebunden, Cookie-Consent
rechtssicher umgesetzt. Es fehlen noch:

- Echte Tracking-IDs (siehe oben)
- GA4-/Ads-Tags innerhalb des GTM-Containers konfigurieren
- Ggf. weitere Unterseiten, die auf der Originaldomain hinzukommen

## Offene nächste Schritte

- Echte GTM-/Clarity-IDs eintragen (siehe Tabelle oben)
- Weitere Formulare/Quiz nach obigem Muster mit `/api/send-lead` verbinden
