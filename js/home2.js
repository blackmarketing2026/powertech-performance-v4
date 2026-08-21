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
    let autoplayTimer = null;

    const getVisibleCount = () => {
      const value = parseInt(getComputedStyle(testimonials).getPropertyValue('--testimonial-visible'), 10);
      return Number.isFinite(value) ? Math.max(1, Math.min(cards.length, value)) : 1;
    };

    const getMaxIndex = () => Math.max(0, cards.length - getVisibleCount());

    const renderDots = () => {
      if (!dots) return;
      dots.innerHTML = '';
      for (let index = 0; index <= getMaxIndex(); index += 1) {
        const dot = document.createElement('button');
        dot.type = 'button';
        dot.className = 'testimonial-dot';
        dot.setAttribute('aria-label', 'Bewertungsgruppe ' + (index + 1) + ' anzeigen');
        dot.addEventListener('click', () => {
          setTestimonial(index);
          restartAutoplay();
        });
        dots.appendChild(dot);
      }
    };

    const setTestimonial = (index) => {
      if (!cards.length || !track) return;
      const maxIndex = getMaxIndex();
      testimonialIndex = index > maxIndex ? 0 : index < 0 ? maxIndex : index;
      testimonials.style.setProperty('--testimonial-index', String(testimonialIndex));
      testimonials.style.setProperty('--testimonial-shift', cards[testimonialIndex].offsetLeft + 'px');
      if (dots) {
        dots.querySelectorAll('button').forEach((dot, dotIndex) => {
          dot.classList.toggle('is-active', dotIndex === testimonialIndex);
          dot.setAttribute('aria-current', dotIndex === testimonialIndex ? 'true' : 'false');
        });
      }
    };

    const stopAutoplay = () => {
      if (!autoplayTimer) return;
      window.clearInterval(autoplayTimer);
      autoplayTimer = null;
    };

    const startAutoplay = () => {
      stopAutoplay();
      if (cards.length <= getVisibleCount()) return;
      autoplayTimer = window.setInterval(() => setTestimonial(testimonialIndex + 1), 4600);
    };

    const restartAutoplay = () => {
      stopAutoplay();
      startAutoplay();
    };

    renderDots();

    if (prev) prev.addEventListener('click', () => {
      setTestimonial(testimonialIndex - 1);
      restartAutoplay();
    });
    if (next) next.addEventListener('click', () => {
      setTestimonial(testimonialIndex + 1);
      restartAutoplay();
    });
    testimonials.addEventListener('mouseenter', stopAutoplay);
    testimonials.addEventListener('mouseleave', startAutoplay);
    testimonials.addEventListener('focusin', stopAutoplay);
    testimonials.addEventListener('focusout', startAutoplay);
    window.addEventListener('resize', () => {
      renderDots();
      setTestimonial(testimonialIndex);
      restartAutoplay();
    });
    setTestimonial(0);
    startAutoplay();
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
