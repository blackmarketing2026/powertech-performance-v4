(function () {
  if (!/^\/(blog|ratgeber)\//.test(window.location.pathname)) return;
  const target = '/keramikversiegelung/?aktion=keramik20#contact';
  const image = '/images/keramik-promo.jpg';
  const logo = '/images/logo-klein.webp';

  function offerCard(variant, titleId) {
    const card = document.createElement('article');
    card.className = 'pt-offer pt-offer--' + variant;
    card.innerHTML = `
      <div class="pt-offer__visual">
        <img class="pt-offer__photo" src="${image}" alt="Gepflegter Fahrzeuglack" loading="lazy" width="1920" height="1080">
        <img class="pt-offer__logo" src="${logo}" alt="" loading="lazy" width="72" height="65">
      </div>
      <div class="pt-offer__content">
        <span class="pt-offer__eyebrow">Aktuelles Angebot · Powertech Erfurt</span>
        <h2${titleId ? ` id="${titleId}"` : ''}>20 % Rabatt auf Keramikversiegelung</h2>
        <p>Glanz und Lackschutz passend zu Ihrem Fahrzeug. Fragen Sie jetzt Ihr persönliches Angebot an.</p>
        <a class="pt-offer__button" href="${target}">Kostenloses Angebot anfragen <span aria-hidden="true">↗</span></a>
      </div>`;
    return card;
  }

  const sidebar = document.querySelector('.article-sidebar');
  if (sidebar) {
    const oldPromo = sidebar.querySelector('.promo-card.promo-dark');
    if (oldPromo) oldPromo.replaceWith(offerCard('sidebar'));
    else sidebar.prepend(offerCard('sidebar'));
    const firstParagraph = document.querySelector('.article-body p');
    if (firstParagraph) firstParagraph.after(offerCard('mobile'));
  } else {
    const anchor = document.querySelector('.blog-hero, .guide-hero');
    if (anchor) anchor.after(offerCard('inline'));
  }

  const dialog = document.createElement('dialog');
  dialog.className = 'pt-offer-dialog';
  dialog.setAttribute('aria-labelledby', 'pt-offer-dialog-title');
  const close = document.createElement('button');
  close.type = 'button';
  close.className = 'pt-offer-dialog__close';
  close.setAttribute('aria-label', 'Angebotsfenster schließen');
  close.textContent = '×';
  dialog.append(close, offerCard('modal', 'pt-offer-dialog-title'));
  document.body.appendChild(dialog);

  let previousFocus = null;
  close.addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (event) => {
    if (event.target === dialog) dialog.close();
  });
  dialog.addEventListener('close', () => {
    if (previousFocus && previousFocus.isConnected) previousFocus.focus();
  });

  function showWhenConsentReady() {
    const cookieBanner = document.getElementById('cookie-banner');
    if (cookieBanner && cookieBanner.classList.contains('is-visible')) {
      const observer = new MutationObserver(() => {
        if (!cookieBanner.classList.contains('is-visible')) {
          observer.disconnect();
          window.setTimeout(showWhenConsentReady, 600);
        }
      });
      observer.observe(cookieBanner, { attributes: true, attributeFilter: ['class'] });
      return;
    }
    if (dialog.open || !document.body.contains(dialog)) return;
    previousFocus = document.activeElement;
    dialog.showModal();
    close.focus();
  }

  window.setTimeout(showWhenConsentReady, 3500);
})();
