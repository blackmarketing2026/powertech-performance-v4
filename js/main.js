// Powertech Performance — Basis-Script (Grundgerüst)

document.addEventListener('DOMContentLoaded', () => {
  // Footer-Jahr
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Mobile-Navigation
  const navToggle = document.getElementById('nav-toggle');
  const mainNav = document.getElementById('main-nav');
  if (navToggle && mainNav) {
    navToggle.addEventListener('click', () => {
      const isOpen = mainNav.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', String(isOpen));
    });
  }

  initLeadForms();
  initCookieBanner();
});

// ---------------------------------------------------------
// Lead-Formulare (Kontaktformulare, Quiz-Ergebnisformulare, ...)
// Jedes Formular mit der Klasse "lead-form" wird automatisch an
// /api/send-lead angebunden. Ein "data-form-name"-Attribut auf dem
// <form> markiert im Betreff, welches Formular abgesendet wurde.
// ---------------------------------------------------------
function initLeadForms() {
  const forms = document.querySelectorAll('.lead-form');

  forms.forEach((form) => {
    form.addEventListener('submit', async (event) => {
      event.preventDefault();

      const statusEl = form.querySelector('[data-form-status]');
      const submitBtn = form.querySelector('button[type="submit"]');
      const formData = new FormData(form);
      const payload = Object.fromEntries(formData.entries());
      payload.formName = form.dataset.formName || 'Formular';

      setFormStatus(statusEl, 'sending', 'Wird gesendet…');
      if (submitBtn) submitBtn.disabled = true;

      try {
        const response = await fetch('/api/send-lead', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });
        const result = await response.json().catch(() => ({}));

        if (!response.ok) {
          throw new Error(result.error || 'Versand fehlgeschlagen.');
        }

        setFormStatus(statusEl, 'success', 'Danke! Ihre Anfrage wurde gesendet — wir melden uns zeitnah.');
        form.reset();
      } catch (err) {
        setFormStatus(statusEl, 'error', err.message || 'Versand fehlgeschlagen. Bitte versuchen Sie es später erneut oder rufen Sie uns an.');
      } finally {
        if (submitBtn) submitBtn.disabled = false;
      }
    });
  });
}

function setFormStatus(statusEl, state, text) {
  if (!statusEl) return;
  statusEl.textContent = text;
  statusEl.setAttribute('data-state', state);
}

// ---------------------------------------------------------
// Cookie-Consent (Grundgerüst)
// Consent-Kategorien folgen Google Consent Mode v2.
// Volle GTM-Integration folgt in einem separaten Schritt.
// ---------------------------------------------------------
function initCookieBanner() {
  const STORAGE_KEY = 'ptp_cookie_consent';
  const banner = document.getElementById('cookie-banner');
  if (!banner) return;

  const stored = getStoredConsent(STORAGE_KEY);
  if (!stored) {
    banner.classList.add('is-visible');
  }

  const acceptBtn = document.getElementById('cookie-accept-all');
  const rejectBtn = document.getElementById('cookie-reject-all');
  const settingsBtn = document.getElementById('cookie-settings');

  if (acceptBtn) {
    acceptBtn.addEventListener('click', () => {
      setConsent(STORAGE_KEY, {
        analytics_storage: 'granted',
        ad_storage: 'granted',
        ad_user_data: 'granted',
        ad_personalization: 'granted',
      });
      banner.classList.remove('is-visible');
    });
  }

  if (rejectBtn) {
    rejectBtn.addEventListener('click', () => {
      setConsent(STORAGE_KEY, {
        analytics_storage: 'denied',
        ad_storage: 'denied',
        ad_user_data: 'denied',
        ad_personalization: 'denied',
      });
      banner.classList.remove('is-visible');
    });
  }

  if (settingsBtn) {
    settingsBtn.addEventListener('click', () => {
      // TODO: Detaillierte Einstellungen (pro Kategorie) ergänzen
      console.log('Cookie-Einstellungen öffnen (Grundgerüst).');
    });
  }
}

function getStoredConsent(key) {
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : null;
  } catch (e) {
    return null;
  }
}

function setConsent(key, consent) {
  try {
    localStorage.setItem(key, JSON.stringify({ ...consent, timestamp: Date.now() }));
  } catch (e) {
    // localStorage nicht verfügbar — Consent gilt nur für diese Sitzung
  }

  if (typeof window.gtag === 'function') {
    window.gtag('consent', 'update', consent);
  }
}
