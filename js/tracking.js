// Powertech Performance — Conversion-Tracking per dataLayer
//
// Alle Tags (Google Ads, GA4) werden ausschließlich im Google Tag Manager
// (GTM-5PQPZTPC) konfiguriert. Dieses Script pusht nur Events in den
// dataLayer — kein gtag.js, keine Conversion-IDs. Consent Mode wird
// unverändert vom Cookie-Banner in main.js gesteuert.
//
// Events:
//   phone_click     link_location, phone_number, link_url
//   whatsapp_click  link_location, link_url
//   form_submit     form_type, form_id, service (nur Auswahlwert)
// Jedes Event erhält zusätzlich page_path und event_id.
//
// Personenbezogene Daten (Name, E-Mail, Telefon des Nutzers, Freitext)
// werden nie in normale Events geschrieben. Ausnahme: der abschaltbare
// Enhanced-Conversions-Block unten (user_data), standardmäßig AUS.
// ---------------------------------------------------------

(function () {
  // Enhanced Conversions: bei true wird beim form_submit zusätzlich
  // user_data { email, phone_number (E.164) } gepusht. Das Hashing
  // übernimmt der Google-Tag im GTM. Vor dem Aktivieren Datenschutz-
  // erklärung prüfen und im GTM "Erweiterte Conversions" einrichten.
  const ENHANCED_CONVERSIONS_ENABLED = false;

  // Zeitfenster, in dem ein zweites Erfolgs-Event desselben Formulars
  // als Doppel-Feuern gilt (Doppelklick, doppelter Callback).
  const FORM_DEDUPE_MS = 3000;

  // Reihenfolge = Priorität. Ein data-track-location am Link (oder an
  // einem Elternelement) überschreibt die automatische Erkennung.
  const LOCATION_SELECTORS = [
    ['sticky', '.sticky-mobile-actions, .mobile-actions'],
    ['header', '.site-header, .home2-header, .graffiti-header'],
    ['footer', '.site-footer, .home2-footer, .graffiti-footer'],
    ['hero', '[class*="hero"]'],
    ['contact', '[class*="contact"], .wash-booking-info'],
    ['banner', '[class*="banner"]'],
    ['cta', '[class*="cta"]'],
  ];

  function createEventId() {
    try {
      if (window.crypto && typeof window.crypto.randomUUID === 'function') {
        return window.crypto.randomUUID();
      }
    } catch (e) {
      // Fallback unten
    }
    return Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 10);
  }

  function trackEvent(eventName, params) {
    if (!eventName) return;
    try {
      window.dataLayer = window.dataLayer || [];
      const data = Object.assign(
        { page_path: window.location.pathname, event_id: createEventId() },
        params || {}
      );
      data.event = eventName;
      window.dataLayer.push(data);
    } catch (e) {
      // Tracking darf Klicks und Formularversand nie blockieren.
    }
  }

  function getLinkLocation(link) {
    const tagged = link.closest('[data-track-location]');
    if (tagged) return tagged.getAttribute('data-track-location') || 'unknown';
    for (let i = 0; i < LOCATION_SELECTORS.length; i++) {
      if (link.closest(LOCATION_SELECTORS[i][1])) return LOCATION_SELECTORS[i][0];
    }
    return 'unknown';
  }

  function isWhatsAppHref(href) {
    return /^(https?:\/\/(wa\.me|api\.whatsapp\.com)\/|whatsapp:\/\/)/i.test(href);
  }

  // Event-Delegation (capture) — erfasst auch später eingefügte Links.
  document.addEventListener('click', (event) => {
    try {
      const link = event.target && event.target.closest ? event.target.closest('a[href]') : null;
      if (!link) return;
      const href = (link.getAttribute('href') || '').trim();

      if (/^tel:/i.test(href)) {
        trackEvent('phone_click', {
          link_location: getLinkLocation(link),
          phone_number: href.replace(/^tel:/i, '').replace(/[^\d+]/g, ''),
          link_url: href,
        });
      } else if (isWhatsAppHref(href)) {
        trackEvent('whatsapp_click', {
          link_location: getLinkLocation(link),
          link_url: href,
        });
      }
    } catch (e) {
      // ignorieren
    }
  }, true);

  // ---------------------------------------------------------
  // Formular-Erfolg — nur nach bestätigtem Versand aufrufen
  // (2xx-Antwort von /api/send-lead), vor form.reset().
  // ---------------------------------------------------------
  const lastFormSuccess = new WeakMap();

  function slugify(value) {
    return String(value)
      .toLowerCase()
      .replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
  }

  // Nur Auswahlfelder (select/radio) — nie Freitext.
  function getSelectedService(form) {
    const select = form.querySelector('select[name="service"]');
    if (select && select.value) return slugify(select.value);
    const radio = form.querySelector('input[type="radio"][name="service"]:checked');
    if (radio && radio.value) return slugify(radio.value);
    return undefined;
  }

  function toE164(raw) {
    let phone = String(raw || '').trim().replace(/[^\d+]/g, '');
    if (!phone) return undefined;
    if (phone.indexOf('00') === 0) phone = '+' + phone.slice(2);
    else if (phone.charAt(0) === '0') phone = '+49' + phone.slice(1);
    else if (phone.charAt(0) !== '+') phone = '+49' + phone;
    phone = '+' + phone.slice(1).replace(/\+/g, '');
    return /^\+[1-9]\d{6,14}$/.test(phone) ? phone : undefined;
  }

  function getUserData(form) {
    const emailField = form.querySelector('[name="email"]');
    const phoneField = form.querySelector('[name="phone"]');
    const userData = {};
    const email = emailField ? emailField.value.trim().toLowerCase() : '';
    if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) userData.email = email;
    const phone = toE164(phoneField ? phoneField.value : '');
    if (phone) userData.phone_number = phone;
    return Object.keys(userData).length ? userData : undefined;
  }

  function trackFormSuccess(form, formType) {
    try {
      if (!form) return;
      const now = Date.now();
      const last = lastFormSuccess.get(form);
      if (last && now - last < FORM_DEDUPE_MS) return;
      lastFormSuccess.set(form, now);

      const params = {
        form_type: formType || form.getAttribute('data-form-type') || 'kontakt',
        form_id: form.id || form.getAttribute('name') || form.getAttribute('data-form-name') || 'unknown',
        service: getSelectedService(form),
      };

      if (ENHANCED_CONVERSIONS_ENABLED) {
        const userData = getUserData(form);
        if (userData) params.user_data = userData;
      }

      trackEvent('form_submit', params);
    } catch (e) {
      // ignorieren
    }
  }

  window.trackEvent = trackEvent;
  window.trackFormSuccess = trackFormSuccess;
})();
