(function () {
  // Nur für lokale Tests auf 'advanced' setzen. Basic ist der Standard.
  const GOOGLE_CONSENT_MODE = 'basic';
  const KEY = 'ptp_cookie_consent';
  const VERSION = 3;
  const MAX_AGE = 365 * 24 * 60 * 60 * 1000;
  let loaded = false;
  let marketing = false;
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  const denied = { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied' };
  window.gtag('consent', 'default', denied);
  if (GOOGLE_CONSENT_MODE === 'advanced') {
    window.gtag('set', 'ads_data_redaction', true);
    window.gtag('set', 'url_passthrough', false);
  }
  function loadGtm() {
    if (loaded) return;
    loaded = true;
    // Vor Einwilligung abgeschlossene Formulare nicht nachtraeglich senden.
    if (GOOGLE_CONSENT_MODE === 'basic') {
      for (let i = window.dataLayer.length - 1; i >= 0; i--) {
        if (window.dataLayer[i] && window.dataLayer[i].event === 'form_completed') window.dataLayer.splice(i, 1);
      }
    }
    window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtm.js?id=GTM-5PQPZTPC';
    document.head.appendChild(script);
  }
  function update(data, initial) {
    const previouslyGranted = marketing;
    marketing = !!data.marketing;
    window.gtag('consent', 'update', {
      ad_storage: marketing ? 'granted' : 'denied',
      ad_user_data: marketing ? 'granted' : 'denied',
      ad_personalization: marketing ? 'granted' : 'denied',
      analytics_storage: 'denied'
    });
    window.__consentExternalMedia = !!data.external;
    if (GOOGLE_CONSENT_MODE === 'advanced' || marketing) loadGtm();
    // Ein bereits ausgeführter Container lässt sich nicht entladen. Nach Widerruf
    // erhält die Seite daher einen neuen, in Basic vollständig blockierten Kontext.
    if (!initial && GOOGLE_CONSENT_MODE === 'basic' && previouslyGranted && !marketing && loaded) location.reload();
  }
  window.ptpConsent = {
    update: function (data) { update(data, false); },
    canTrackAds: function () { return GOOGLE_CONSENT_MODE === 'advanced' || marketing; }
  };
  let stored = null;
  try {
    const value = JSON.parse(localStorage.getItem(KEY));
    if (value && value.version === VERSION && typeof value.timestamp === 'number' && value.timestamp <= Date.now() && Date.now() - value.timestamp <= MAX_AGE) stored = value;
  } catch (_) {}
  if (stored) update(stored, true);
  else if (GOOGLE_CONSENT_MODE === 'advanced') loadGtm();
})();
