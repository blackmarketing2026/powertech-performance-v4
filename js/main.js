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
  initCookieConsent();
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
// Cookie-Consent (TTDSG/DSGVO, Google Consent Mode v2)
//
// Kategorien: "necessary" (immer an), "analytics" (Google Analytics,
// Microsoft Clarity), "marketing" (Google Ads Remarketing). "Alle
// ablehnen" und "Alle akzeptieren" sind gleichwertig erreichbar,
// keine vorausgewählten optionalen Kategorien. Einwilligung wird
// 12 Monate lokal gespeichert und bei jedem Seitenaufruf geprüft.
// ---------------------------------------------------------
const COOKIE_CONSENT_KEY = 'ptp_cookie_consent';
const COOKIE_CONSENT_MAX_AGE_DAYS = 365;
const CLARITY_PROJECT_ID = 'XXXXXXXXXX'; // TODO: echte Clarity-Projekt-ID eintragen

function getStoredConsent() {
  try {
    const raw = localStorage.getItem(COOKIE_CONSENT_KEY);
    if (!raw) return null;
    const data = JSON.parse(raw);
    if (!data || typeof data.timestamp !== 'number') return null;
    const ageDays = (Date.now() - data.timestamp) / (1000 * 60 * 60 * 24);
    if (ageDays > COOKIE_CONSENT_MAX_AGE_DAYS) return null;
    return data;
  } catch (e) {
    return null;
  }
}

function storeConsent({ analytics, marketing }) {
  const data = { necessary: true, analytics: !!analytics, marketing: !!marketing, timestamp: Date.now() };
  try {
    localStorage.setItem(COOKIE_CONSENT_KEY, JSON.stringify(data));
  } catch (e) {
    // localStorage nicht verfügbar — Consent gilt nur für diese Sitzung
  }
  return data;
}

function applyConsent(data) {
  if (typeof window.gtag === 'function') {
    window.gtag('consent', 'update', {
      analytics_storage: data.analytics ? 'granted' : 'denied',
      ad_storage: data.marketing ? 'granted' : 'denied',
      ad_user_data: data.marketing ? 'granted' : 'denied',
      ad_personalization: data.marketing ? 'granted' : 'denied',
    });
  }
  if (data.analytics) loadClarity();
}

// Microsoft Clarity nutzt kein Google Consent Mode — Script wird
// deshalb nur bei erteilter Statistik-Einwilligung nachgeladen.
function loadClarity() {
  if (window.__clarityLoaded || CLARITY_PROJECT_ID.startsWith('XXX')) return;
  window.__clarityLoaded = true;
  (function (c, l, a, r, i, t, y) {
    c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
    t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i;
    y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
  })(window, document, 'clarity', 'script', CLARITY_PROJECT_ID);
}

function setCategoryCheckboxes(root, data) {
  const analyticsBox = root.querySelector('[id$="-analytics"]');
  const marketingBox = root.querySelector('[id$="-marketing"]');
  if (analyticsBox) analyticsBox.checked = !!data.analytics;
  if (marketingBox) marketingBox.checked = !!data.marketing;
}

function initCookieConsent() {
  const stored = getStoredConsent();
  if (stored) applyConsent(stored);

  initCookieBanner(stored);
  initCookiePreferencesPage(stored);
}

function setBannerVisible(banner, visible) {
  banner.classList.toggle('is-visible', visible);
  // Verhindert, dass sich Cookie-Banner und Sticky-Aktionsleiste (Anrufen/WhatsApp) auf Mobile überlappen
  document.body.classList.toggle('cookie-banner-open', visible);
}

function initCookieBanner(stored) {
  const banner = document.getElementById('cookie-banner');
  if (!banner) return;

  if (!stored) {
    setBannerVisible(banner, true);
  } else {
    setCategoryCheckboxes(banner, stored);
  }

  const acceptBtn = banner.querySelector('#cookie-accept-all');
  const rejectBtn = banner.querySelector('#cookie-reject-all');
  const saveBtn = banner.querySelector('#cookie-save-selection');

  const simplePanel = banner.querySelector('[data-cookie-simple]');
  const advancedPanel = banner.querySelector('[data-cookie-advanced]');
  const advancedToggle = banner.querySelector('[data-cookie-advanced-toggle]');
  const backBtn = banner.querySelector('[data-cookie-back]');
  const selectAllBtn = banner.querySelector('[data-cookie-select-all]');
  const selectNoneBtn = banner.querySelector('[data-cookie-select-none]');

  function showAdvanced(show) {
    if (!simplePanel || !advancedPanel) return;
    simplePanel.hidden = show;
    advancedPanel.hidden = !show;
    if (advancedToggle) advancedToggle.setAttribute('aria-expanded', String(show));
  }

  if (advancedToggle) advancedToggle.addEventListener('click', () => showAdvanced(true));
  if (backBtn) backBtn.addEventListener('click', () => showAdvanced(false));

  if (selectAllBtn) {
    selectAllBtn.addEventListener('click', () => setCategoryCheckboxes(banner, { analytics: true, marketing: true }));
  }
  if (selectNoneBtn) {
    selectNoneBtn.addEventListener('click', () => setCategoryCheckboxes(banner, { analytics: false, marketing: false }));
  }

  if (acceptBtn) {
    acceptBtn.addEventListener('click', () => {
      setCategoryCheckboxes(banner, { analytics: true, marketing: true });
      applyConsent(storeConsent({ analytics: true, marketing: true }));
      setBannerVisible(banner, false);
    });
  }

  if (rejectBtn) {
    rejectBtn.addEventListener('click', () => {
      setCategoryCheckboxes(banner, { analytics: false, marketing: false });
      applyConsent(storeConsent({ analytics: false, marketing: false }));
      setBannerVisible(banner, false);
    });
  }

  if (saveBtn) {
    saveBtn.addEventListener('click', () => {
      const analytics = banner.querySelector('[id$="-analytics"]').checked;
      const marketing = banner.querySelector('[id$="-marketing"]').checked;
      applyConsent(storeConsent({ analytics, marketing }));
      setBannerVisible(banner, false);
    });
  }
}

// Eigenständige Seite pages/cookie-einstellungen.html: gleiche Kategorien,
// aber dauerhaft sichtbar statt als Banner — Nutzer können ihre Auswahl
// jederzeit nachträglich ändern.
function initCookiePreferencesPage(stored) {
  const page = document.getElementById('cookie-preferences-page');
  if (!page) return;

  setCategoryCheckboxes(page, stored || { analytics: false, marketing: false });

  const statusEl = page.querySelector('#cookie-page-status');
  const saveBtn = page.querySelector('#cookie-page-save');
  const acceptBtn = page.querySelector('#cookie-page-accept-all');
  const rejectBtn = page.querySelector('#cookie-page-reject-all');

  function afterSave(data) {
    applyConsent(data);
    const banner = document.getElementById('cookie-banner');
    if (banner) banner.classList.remove('is-visible');
    if (statusEl) {
      statusEl.textContent = 'Ihre Auswahl wurde gespeichert.';
      statusEl.hidden = false;
    }
  }

  if (saveBtn) {
    saveBtn.addEventListener('click', () => {
      const analytics = page.querySelector('[id$="-analytics"]').checked;
      const marketing = page.querySelector('[id$="-marketing"]').checked;
      afterSave(storeConsent({ analytics, marketing }));
    });
  }

  if (acceptBtn) {
    acceptBtn.addEventListener('click', () => {
      setCategoryCheckboxes(page, { analytics: true, marketing: true });
      afterSave(storeConsent({ analytics: true, marketing: true }));
    });
  }

  if (rejectBtn) {
    rejectBtn.addEventListener('click', () => {
      setCategoryCheckboxes(page, { analytics: false, marketing: false });
      afterSave(storeConsent({ analytics: false, marketing: false }));
    });
  }
}
