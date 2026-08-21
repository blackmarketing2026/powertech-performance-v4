// Baut die HTML-E-Mail für eingehende Leads (Kontaktformulare, Quiz, ...).
// Wird von api/send-lead.js genutzt.

// Die eigentliche Domain zeigt möglicherweise noch nicht auf dieses Vercel-
// Projekt (DNS/Custom-Domain nicht verbunden). Damit das Logo in der Mail
// trotzdem lädt, wird bevorzugt die von Vercel automatisch gesetzte
// Deployment-URL verwendet — die funktioniert immer, unabhängig vom DNS-Status
// der Wunschdomain. Sobald die Domain sauber auf Vercel zeigt, kann man sie
// hier zusätzlich fest hinterlegen.
const SITE_URL = process.env.VERCEL_PROJECT_PRODUCTION_URL
  ? `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}`
  : process.env.VERCEL_URL
    ? `https://${process.env.VERCEL_URL}`
    : 'https://powertech-performance.com';
const LOGO_URL = `${SITE_URL}/images/logo-klein.png`;

const FIELD_LABELS = {
  name: 'Name',
  email: 'E-Mail',
  phone: 'Telefon',
  vehicle: 'Fahrzeug',
  message: 'Nachricht',
};

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function labelFor(key) {
  if (FIELD_LABELS[key]) return FIELD_LABELS[key];
  return key.charAt(0).toUpperCase() + key.slice(1);
}

// Wandelt eine eingegebene Telefonnummer in eine wa.me-taugliche Ziffernfolge
// um (Ländervorwahl, keine Leerzeichen/Sonderzeichen, kein führendes "+").
function toWhatsAppDigits(phone) {
  let digits = String(phone).replace(/[^\d+]/g, '');
  if (digits.startsWith('+')) digits = digits.slice(1);
  else if (digits.startsWith('00')) digits = digits.slice(2);
  else if (digits.startsWith('0')) digits = '49' + digits.slice(1);
  return digits;
}

// Wandelt eine eingegebene Telefonnummer in eine gültige tel:-Zielangabe um.
function toTelHref(phone) {
  let digits = String(phone).replace(/[^\d+]/g, '');
  if (digits.startsWith('+')) return digits;
  if (digits.startsWith('00')) return `+${digits.slice(2)}`;
  if (digits.startsWith('0')) return `+49${digits.slice(1)}`;
  return `+${digits}`;
}

function actionButton({ href, bg, color = '#ffffff', border, label }) {
  const borderStyle = border ? `border:2px solid ${border};` : 'border:2px solid transparent;';
  return `
    <td style="padding:0 6px 12px;" align="center">
      <a href="${href}" target="_blank" rel="noopener"
         style="display:inline-block;min-width:150px;padding:10px 20px;background-color:${bg};color:${color};
                font-family:'Red Hat Display',Arial,sans-serif;font-size:14px;font-weight:700;
                text-decoration:none;border-radius:8px;text-align:center;${borderStyle}">
        ${label}
      </a>
    </td>`;
}

function buildLeadEmailHtml({ fields, formName }) {
  const { name, email, phone, message, ...rest } = fields;

  const buttons = [];
  if (phone) {
    buttons.push(actionButton({
      href: `https://wa.me/${toWhatsAppDigits(phone)}`,
      bg: '#1EA30E',
      label: '💬 WhatsApp',
    }));
    buttons.push(actionButton({
      href: `tel:${toTelHref(phone)}`,
      bg: '#7E3E98',
      label: '📞 Anrufen',
    }));
  }
  if (email) {
    buttons.push(actionButton({
      href: `mailto:${email}`,
      bg: '#F3ECF7',
      color: '#7E3E98',
      border: '#7E3E98',
      label: '✉️ E-Mail schreiben',
    }));
  }

  const buttonsHtml = buttons.length
    ? `
    <tr>
      <td style="padding:8px 24px 4px;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
          <tr>${buttons.join('')}</tr>
        </table>
      </td>
    </tr>`
    : '';

  const orderedFields = [
    ['name', name],
    ['email', email],
    ['phone', phone],
    ...Object.entries(rest),
    ['message', message],
  ].filter(([, value]) => value !== undefined && value !== null && String(value).trim() !== '');

  const rowsHtml = orderedFields
    .map(([key, value]) => `
    <tr>
      <td style="padding:10px 24px;border-bottom:1px solid #EFE7F2;">
        <p style="margin:0 0 2px;font-family:'Red Hat Display',Arial,sans-serif;font-size:11px;
                  font-weight:700;letter-spacing:0.5px;text-transform:uppercase;color:#7E3E98;opacity:0.7;">
          ${labelFor(key)}
        </p>
        <p style="margin:0;font-family:'Red Hat Display',Arial,sans-serif;font-size:15px;color:#2B2233;
                  white-space:pre-line;">
          ${escapeHtml(value)}
        </p>
      </td>
    </tr>`)
    .join('');

  return `<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Neue Anfrage – ${escapeHtml(formName || 'Website')}</title>
</head>
<body style="margin:0;padding:0;background-color:#F8F5FA;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#F8F5FA;padding:32px 12px;">
    <tr>
      <td align="center">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0"
               style="max-width:600px;width:100%;background-color:#ffffff;border-radius:14px;overflow:hidden;
                      box-shadow:0 4px 20px rgba(110,82,131,0.12);">

          <!-- Header -->
          <tr>
            <td style="background:linear-gradient(135deg,#6E5283 0%,#5d4570 40%,#8b6fa0 70%,#4c3c5a 100%);
                       padding:28px 24px;text-align:center;">
              <img src="${LOGO_URL}" alt="Logo" width="56" height="56"
                   style="display:block;width:56px;height:56px;margin:0 auto 12px;border-radius:8px;
                          font-family:'Red Hat Display',Arial,sans-serif;font-size:10px;color:#ffffff;">
              <p style="margin:0;font-family:'Red Hat Display',Arial,sans-serif;font-size:20px;font-weight:700;color:#ffffff;">
                Neue Anfrage über die Website
              </p>
              <p style="margin:6px 0 0;font-family:'Red Hat Display',Arial,sans-serif;font-size:13px;color:#DECEE0;">
                ${escapeHtml(formName || 'Formular')}
              </p>
            </td>
          </tr>

          <!-- Action-Buttons -->
          <tr>
            <td>
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
                ${buttonsHtml}
              </table>
            </td>
          </tr>

          <!-- Felder -->
          <tr>
            <td>
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-top:8px;">
                ${rowsHtml}
              </table>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="padding:20px 24px;background-color:#F8F5FA;text-align:center;">
              <p style="margin:0;font-family:'Red Hat Display',Arial,sans-serif;font-size:12px;color:#6E5283;opacity:0.7;">
                Diese Anfrage wurde automatisch über
                <a href="${SITE_URL}" style="color:#7E3E98;text-decoration:underline;">powertech-performance.com</a>
                gesendet.
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>`;
}

module.exports = { buildLeadEmailHtml };
