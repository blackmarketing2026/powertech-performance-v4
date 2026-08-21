(function () {
  const root = document.documentElement;
  const header = document.querySelector('[data-header]');
  const revealItems = Array.from(document.querySelectorAll('[data-reveal]'));
  const compare = document.querySelector('[data-compare]');
  const compareInput = compare ? compare.querySelector('input[type="range"]') : null;
  const phoneTestimonials = document.querySelector('[data-testimonial-phone]');

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

  if (phoneTestimonials) {
    const track = phoneTestimonials.querySelector('[data-phone-testimonial-track]');
    const slides = track ? Array.from(track.querySelectorAll('.phone-testimonial-slide')) : [];
    const prev = phoneTestimonials.querySelector('[data-phone-testimonial-prev]');
    const next = phoneTestimonials.querySelector('[data-phone-testimonial-next]');
    const dots = phoneTestimonials.querySelector('[data-phone-testimonial-dots]');
    let testimonialIndex = 0;
    let autoplayTimer = null;

    const renderDots = () => {
      if (!dots) return;
      dots.innerHTML = '';
      slides.forEach((slide, index) => {
        const dot = document.createElement('button');
        dot.type = 'button';
        dot.className = 'phone-testimonial-dot';
        dot.setAttribute('aria-label', 'Kundenstimme ' + (index + 1) + ' anzeigen');
        dot.addEventListener('click', () => {
          setTestimonial(index);
          restartAutoplay();
        });
        dots.appendChild(dot);
      });
    };

    const setTestimonial = (index) => {
      if (!slides.length || !track) return;
      testimonialIndex = (index + slides.length) % slides.length;
      phoneTestimonials.style.setProperty('--phone-testimonial-index', String(testimonialIndex));
      slides.forEach((slide, slideIndex) => {
        slide.setAttribute('aria-hidden', slideIndex === testimonialIndex ? 'false' : 'true');
      });
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
      if (slides.length <= 1) return;
      autoplayTimer = window.setInterval(() => setTestimonial(testimonialIndex + 1), 4300);
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
    phoneTestimonials.addEventListener('mouseenter', stopAutoplay);
    phoneTestimonials.addEventListener('mouseleave', startAutoplay);
    phoneTestimonials.addEventListener('focusin', stopAutoplay);
    phoneTestimonials.addEventListener('focusout', startAutoplay);
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        stopAutoplay();
      } else {
        startAutoplay();
      }
    });
    window.addEventListener('resize', () => {
      setTestimonial(testimonialIndex);
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
