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
// Microsoft Clarity), "marketing" (Google Ads Remarketing), "external"
// (externe Medien/Einbettungen, z. B. Karten oder Videos Dritter).
// "Nur notwendige" und "Alle akzeptieren" sind gleichwertig erreichbar,
// keine vorausgewählten optionalen Kategorien. Einwilligung wird
// 12 Monate lokal gespeichert und bei jedem Seitenaufruf geprüft.
//
// CONSENT_VERSION wird erhöht, sobald sich der Umfang der abgefragten
// Kategorien ändert (z. B. neue Kategorie "external" in Version 2).
// Gespeicherte Einwilligungen einer älteren Version gelten als
// ungültig, damit Nutzer die neuen Kategorien aktiv bestätigen —
// bereits gewählte Werte für bestehende Kategorien gehen dabei nicht
// verloren, da sie beim erneuten Öffnen weiterhin vorbelegt werden.
// ---------------------------------------------------------
const COOKIE_CONSENT_KEY = 'ptp_cookie_consent';
const COOKIE_CONSENT_MAX_AGE_DAYS = 365;
const CONSENT_VERSION = 2;
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

// Liefert gespeicherte Einwilligung nur zurück, wenn sie zur aktuellen
// Kategorien-Version passt. Bei älteren Versionen (z. B. vor Einführung
// von "external") werden die bekannten Werte als Vorbelegung für den
// Banner zurückgegeben, gelten aber nicht als gültige Einwilligung.
function getValidStoredConsent() {
  const stored = getStoredConsent();
  if (!stored) return { valid: null, prefill: null };
  if (stored.version === CONSENT_VERSION) return { valid: stored, prefill: stored };
  return { valid: null, prefill: stored };
}

function storeConsent({ analytics, marketing, external }) {
  const data = {
    necessary: true,
    analytics: !!analytics,
    marketing: !!marketing,
    external: !!external,
    version: CONSENT_VERSION,
    timestamp: Date.now(),
  };
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
  window.__consentExternalMedia = !!data.external;
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
  const externalBox = root.querySelector('[id$="-external"]');
  if (analyticsBox) analyticsBox.checked = !!data.analytics;
  if (marketingBox) marketingBox.checked = !!data.marketing;
  if (externalBox) externalBox.checked = !!data.external;
}

function readCategoryCheckboxes(root) {
  return {
    analytics: !!root.querySelector('[id$="-analytics"]')?.checked,
    marketing: !!root.querySelector('[id$="-marketing"]')?.checked,
    external: !!root.querySelector('[id$="-external"]')?.checked,
  };
}

function initCookieConsent() {
  const { valid, prefill } = getValidStoredConsent();
  if (valid) applyConsent(valid);

  initCookieBanner(valid, prefill);
  initCookiePreferencesPage(valid, prefill);
}

function setBannerVisible(banner, visible) {
  banner.classList.toggle('is-visible', visible);
  // Verhindert, dass sich Cookie-Banner und Sticky-Aktionsleiste (Anrufen/WhatsApp) auf Mobile überlappen
  document.body.classList.toggle('cookie-banner-open', visible);
  if (!visible) {
    banner.classList.remove('is-shown');
    document.body.classList.remove('cookie-settings-open');
    return;
  }
  // Zwei Phasen (is-visible -> is-shown), damit die Einblend-Transition greift
  requestAnimationFrame(() => banner.classList.add('is-shown'));
  const firstBtn = banner.querySelector('#cookie-accept-all');
  if (firstBtn) firstBtn.focus();
}

function trapFocus(container, event) {
  if (event.key !== 'Tab') return;
  const focusable = container.querySelectorAll(
    'a[href], button:not([disabled]), input:not([disabled]):not([type="hidden"]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
  );
  const visibleFocusable = Array.from(focusable).filter((el) => el.offsetParent !== null);
  if (!visibleFocusable.length) return;
  const first = visibleFocusable[0];
  const last = visibleFocusable[visibleFocusable.length - 1];
  if (event.shiftKey && document.activeElement === first) {
    event.preventDefault();
    last.focus();
  } else if (!event.shiftKey && document.activeElement === last) {
    event.preventDefault();
    first.focus();
  }
}

function initCookieBanner(stored, prefill) {
  const banner = document.getElementById('cookie-banner');
  if (!banner) return;

  if (!stored) {
    setCategoryCheckboxes(banner, prefill || { analytics: false, marketing: false, external: false });
    setBannerVisible(banner, true);
  } else {
    setCategoryCheckboxes(banner, stored);
  }

  const acceptBtn = banner.querySelector('#cookie-accept-all');
  const necessaryBtn = banner.querySelector('#cookie-necessary-only');
  const saveBtn = banner.querySelector('#cookie-save-selection');
  const settingsAcceptBtn = banner.querySelector('#cookie-settings-accept-all');
  const settingsNecessaryBtn = banner.querySelector('#cookie-settings-necessary-only');

  const simplePanel = banner.querySelector('[data-cookie-simple]');
  const advancedPanel = banner.querySelector('[data-cookie-advanced]');
  const advancedToggle = banner.querySelector('[data-cookie-advanced-toggle]');
  const backBtn = banner.querySelector('[data-cookie-back]');

  function showAdvanced(show) {
    if (!simplePanel || !advancedPanel) return;
    simplePanel.hidden = show;
    advancedPanel.hidden = !show;
    if (advancedToggle) advancedToggle.setAttribute('aria-expanded', String(show));
    document.body.classList.toggle('cookie-settings-open', show);
    if (show) {
      const heading = advancedPanel.querySelector('h3');
      if (heading) {
        heading.setAttribute('tabindex', '-1');
        heading.focus();
      }
    } else if (advancedToggle) {
      advancedToggle.focus();
    }
  }

  if (advancedToggle) advancedToggle.addEventListener('click', () => showAdvanced(true));
  if (backBtn) backBtn.addEventListener('click', () => showAdvanced(false));

  banner.addEventListener('keydown', (event) => {
    trapFocus(banner, event);
    if (event.key === 'Escape' && !advancedPanel.hidden) {
      showAdvanced(false);
    }
  });

  function acceptAll() {
    setCategoryCheckboxes(banner, { analytics: true, marketing: true, external: true });
    applyConsent(storeConsent({ analytics: true, marketing: true, external: true }));
    setBannerVisible(banner, false);
  }

  function necessaryOnly() {
    setCategoryCheckboxes(banner, { analytics: false, marketing: false, external: false });
    applyConsent(storeConsent({ analytics: false, marketing: false, external: false }));
    setBannerVisible(banner, false);
  }

  function saveSelection() {
    applyConsent(storeConsent(readCategoryCheckboxes(banner)));
    setBannerVisible(banner, false);
  }

  if (acceptBtn) acceptBtn.addEventListener('click', acceptAll);
  if (necessaryBtn) necessaryBtn.addEventListener('click', necessaryOnly);
  if (settingsAcceptBtn) settingsAcceptBtn.addEventListener('click', acceptAll);
  if (settingsNecessaryBtn) settingsNecessaryBtn.addEventListener('click', necessaryOnly);
  if (saveBtn) saveBtn.addEventListener('click', saveSelection);
}

// Eigenständige Seite pages/cookie-einstellungen.html: gleiche Kategorien,
// aber dauerhaft sichtbar statt als Banner — Nutzer können ihre Auswahl
// jederzeit nachträglich ändern.
function initCookiePreferencesPage(stored, prefill) {
  const page = document.getElementById('cookie-preferences-page');
  if (!page) return;

  setCategoryCheckboxes(page, stored || prefill || { analytics: false, marketing: false, external: false });

  const statusEl = page.querySelector('#cookie-page-status');
  const saveBtn = page.querySelector('#cookie-page-save');
  const acceptBtn = page.querySelector('#cookie-page-accept-all');
  const necessaryBtn = page.querySelector('#cookie-page-necessary-only');

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
      afterSave(storeConsent(readCategoryCheckboxes(page)));
    });
  }

  if (acceptBtn) {
    acceptBtn.addEventListener('click', () => {
      setCategoryCheckboxes(page, { analytics: true, marketing: true, external: true });
      afterSave(storeConsent({ analytics: true, marketing: true, external: true }));
    });
  }

  if (necessaryBtn) {
    necessaryBtn.addEventListener('click', () => {
      setCategoryCheckboxes(page, { analytics: false, marketing: false, external: false });
      afterSave(storeConsent({ analytics: false, marketing: false, external: false }));
    });
  }
}
