// Vercel Serverless Function — nimmt Leads von JEDEM Formular/Quiz der Website
// entgegen und verschickt sie per SMTP an das Postfach in smtp_empfaenger.
//
// Benötigte Environment Variables (in Vercel hinterlegt):
//   smtp_server     SMTP-Host
//   smtp_benutzer   SMTP-Benutzername / Absenderadresse
//   smtp_passwort   SMTP-Passwort
//   smtp_empfaenger Zieladresse, an die Leads gesendet werden
// Optional:
//   smtp_port       Standard: 465 (SSL)

const nodemailer = require('nodemailer');
const { buildLeadEmailHtml } = require('./_lib/lead-email');

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }

  const body = req.body || {};

  // Honeypot-Feld — Bots füllen verstecktes Feld aus, echte Nutzer nicht.
  if (body.website) {
    res.status(200).json({ ok: true });
    return;
  }

  const { formName, ...fields } = body;
  const { name, email, message } = fields;

  if (!name || !email || !message) {
    res.status(400).json({ error: 'Bitte Name, E-Mail und Nachricht angeben.' });
    return;
  }

  const requiredEnv = ['smtp_server', 'smtp_benutzer', 'smtp_passwort', 'smtp_empfaenger'];
  const missingEnv = requiredEnv.filter((key) => !process.env[key]);
  if (missingEnv.length) {
    console.error('Fehlende SMTP-Umgebungsvariablen:', missingEnv.join(', '));
    res.status(500).json({ error: 'Formularversand ist aktuell nicht konfiguriert.' });
    return;
  }

  const transporter = nodemailer.createTransport({
    host: process.env.smtp_server,
    port: Number(process.env.smtp_port) || 465,
    secure: (Number(process.env.smtp_port) || 465) === 465,
    auth: {
      user: process.env.smtp_benutzer,
      pass: process.env.smtp_passwort,
    },
  });

  const lines = Object.entries(fields)
    .filter(([, value]) => value !== undefined && value !== null && String(value).trim() !== '')
    .map(([key, value]) => `${key}: ${value}`)
    .join('\n');

  try {
    await transporter.sendMail({
      from: `"Website Powertech Performance" <${process.env.smtp_benutzer}>`,
      to: process.env.smtp_empfaenger,
      replyTo: email,
      subject: `Neue Anfrage über die Website – ${formName || 'Formular'}`,
      text: `Formular: ${formName || 'unbekannt'}\n\n${lines}`,
      html: buildLeadEmailHtml({ fields, formName }),
    });
    res.status(200).json({ ok: true });
  } catch (err) {
    console.error('Mailversand fehlgeschlagen:', err);
    res.status(500).json({ error: 'Versand fehlgeschlagen. Bitte später erneut versuchen.' });
  }
};
