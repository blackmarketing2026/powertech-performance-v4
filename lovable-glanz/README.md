# Powertech Glanz Erfurt

Quellcode der aus dem Lovable-Export übernommenen Keramikversiegelungsseite. Der Build wird statisch nach `../glanz-erfurt/` geschrieben und auf Vercel unter `/glanz-erfurt/` bereitgestellt. Das bestehende Git-Repository, die übrigen Seiten und die Vercel-Funktion `/api/send-lead` bleiben erhalten.

```bash
cd lovable-glanz
npm ci
npm run dev
```

Der lokale Vite-Server zeigt die Seite unter `http://localhost:8080/glanz-erfurt/`. Für den statischen Build: `npm run build`. Das Kontaktformular verwendet im veröffentlichten Projekt `/api/send-lead`; lokal muss die Vercel-Funktion verfügbar sein, damit echte Anfragen versendet werden.

Für den bestehenden SMTP-Versand werden serverseitig `smtp_server`, `smtp_benutzer`, `smtp_passwort` und `smtp_empfaenger` benötigt. Das vorhandene Lead-System ist die einzige Formularintegration.
