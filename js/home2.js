(function () {
  const root = document.documentElement;
  const header = document.querySelector('[data-header]');
  const revealItems = Array.from(document.querySelectorAll('[data-reveal]'));
  const compare = document.querySelector('[data-compare]');
  const compareInput = compare ? compare.querySelector('input[type="range"]') : null;

  function updateScrollEffects() {
    const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    const progress = window.scrollY / max;
    root.style.setProperty('--scroll-progress', progress.toFixed(4));
    root.style.setProperty('--hero-y', String(Math.min(90, window.scrollY * 0.14)));

    if (header) {
      header.classList.toggle('is-scrolled', window.scrollY > 18);
    }
  }

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      });
    }, {
      rootMargin: '0px 0px -12% 0px',
      threshold: 0.18
    });

    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add('is-visible'));
  }

  if (compare && compareInput) {
    const setCompare = () => {
      compare.style.setProperty('--split', compareInput.value + '%');
    };

    compareInput.addEventListener('input', setCompare);
    setCompare();
  }

  document.querySelectorAll('.home2-nav a').forEach((link) => {
    link.addEventListener('click', () => {
      const nav = document.getElementById('main-nav');
      const toggle = document.getElementById('nav-toggle');
      if (!nav || !toggle) return;
      nav.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });

  updateScrollEffects();
  window.addEventListener('scroll', updateScrollEffects, { passive: true });
  window.addEventListener('resize', updateScrollEffects);
})();
