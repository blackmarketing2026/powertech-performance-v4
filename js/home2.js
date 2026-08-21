(function () {
  const root = document.documentElement;
  const header = document.querySelector('[data-header]');
  const revealItems = Array.from(document.querySelectorAll('[data-reveal]'));
  const compare = document.querySelector('[data-compare]');
  const compareInput = compare ? compare.querySelector('input[type="range"]') : null;
  const testimonials = document.querySelector('[data-testimonials]');

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

  if (testimonials) {
    const track = testimonials.querySelector('[data-testimonial-track]');
    const cards = track ? Array.from(track.querySelectorAll('.testimonial-card')) : [];
    const prev = testimonials.querySelector('[data-testimonial-prev]');
    const next = testimonials.querySelector('[data-testimonial-next]');
    const dots = testimonials.querySelector('[data-testimonial-dots]');
    let testimonialIndex = 0;

    const setTestimonial = (index) => {
      if (!cards.length || !track) return;
      testimonialIndex = (index + cards.length) % cards.length;
      testimonials.style.setProperty('--testimonial-index', String(testimonialIndex));
      testimonials.style.setProperty('--testimonial-shift', cards[testimonialIndex].offsetLeft + 'px');
      if (dots) {
        dots.querySelectorAll('button').forEach((dot, dotIndex) => {
          dot.classList.toggle('is-active', dotIndex === testimonialIndex);
          dot.setAttribute('aria-current', dotIndex === testimonialIndex ? 'true' : 'false');
        });
      }
    };

    if (dots) {
      cards.forEach((_, index) => {
        const dot = document.createElement('button');
        dot.type = 'button';
        dot.className = 'testimonial-dot';
        dot.setAttribute('aria-label', 'Bewertung ' + (index + 1) + ' anzeigen');
        dot.addEventListener('click', () => setTestimonial(index));
        dots.appendChild(dot);
      });
    }

    if (prev) prev.addEventListener('click', () => setTestimonial(testimonialIndex - 1));
    if (next) next.addEventListener('click', () => setTestimonial(testimonialIndex + 1));
    window.addEventListener('resize', () => setTestimonial(testimonialIndex));
    setTestimonial(0);
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
