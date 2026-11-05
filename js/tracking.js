// Powertech Performance: Klick- und Formularereignisse im dataLayer.
// Das Formularereignis enthaelt keine Eingabedaten.

(function () {
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

  // Nur nach bestaetigtem Versand aufrufen; keine Formulardaten uebertragen.
  function trackFormSuccess(form) {
    try {
      if (!form) return;
      const honeypot = form.querySelector('[name="website"]');
      if (honeypot && honeypot.value) return;
      window.dataLayer.push({ event: 'form_completed' });
    } catch (e) {}
  }

  window.trackEvent = trackEvent;
  window.trackFormSuccess = trackFormSuccess;
})();
