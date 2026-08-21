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

### Lokale Entwicklung / Deployment

Der Formularversand läuft nur auf Vercel (oder lokal mit `vercel dev`), da
`api/send-lead.js` eine Serverless Function ist. Bei einem einfachen
`npx serve` o. Ä. ohne Vercel-Runtime schlägt der Versand fehl (kein `/api`-Handler).

```
npm install       # installiert nodemailer für api/send-lead.js
vercel dev         # lokale Entwicklung inkl. Serverless Functions
```

## Status

Startseite inhaltlich fertig, Formularversand angebunden. Es fehlen noch:

- Rechtstexte (Impressum, Datenschutz, AGB) mit echten Inhalten
- Vollständige GTM-/Consent-Mode-Integration (Skill `cookie-consent-gtm`)
- Ggf. weitere Unterseiten (z. B. Chiptuning, wie auf der Originaldomain vorhanden)

## Offene nächste Schritte

- Rechtstexte ausfüllen
- GTM/Consent Mode v2 vollständig verkabeln (Skill `cookie-consent-gtm`)
- Weitere Formulare/Quiz nach obigem Muster mit `/api/send-lead` verbinden
