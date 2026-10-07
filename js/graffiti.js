(() => {
  'use strict';
  const page = document.querySelector('.graffiti-page');
  if (!page) return;
  const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const button = page.querySelector('.motion-toggle');
  const progress = page.querySelector('.frost-progress');
  const canvas = page.querySelector('.cold-atmosphere');
  const context = canvas && canvas.getContext('2d', { alpha: true });
  let paused = false;
  let width = 0;
  let height = 0;
  let scrollAmount = 0;
  let frame = 0;
  let lastTime = 0;
  let scrollFrame = 0;
  let particles = [];

  // Content stays visible even if this script or IntersectionObserver is unavailable.
  if ('IntersectionObserver' in window) {
    const reveals = new IntersectionObserver((entries) => {
      entries.forEach(({ target, isIntersecting }) => {
        if (!isIntersecting) return;
        if (!motionPreference.matches && !paused) target.classList.add('is-entering');
        reveals.unobserve(target);
      });
    }, { threshold: .1 });
    page.querySelectorAll('.reveal').forEach((element) => reveals.observe(element));
  }

  const paintProgress = () => {
    const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    scrollAmount = Math.min(1, Math.max(0, window.scrollY / maxScroll));
    document.documentElement.style.setProperty('--cold', scrollAmount.toFixed(3));
    if (progress) progress.style.transform = `scaleX(${scrollAmount})`;
    scrollFrame = 0;
  };
  window.addEventListener('scroll', () => {
    if (!scrollFrame) scrollFrame = requestAnimationFrame(paintProgress);
  }, { passive: true });

  const particle = (spread = true) => ({
    x: spread ? Math.random() * width : width + Math.random() * 100,
    y: Math.random() * height,
    speed: 24 + Math.random() * 65,
    size: .6 + Math.random() * 1.8,
    opacity: .15 + Math.random() * .5,
    phase: Math.random() * Math.PI * 2,
    trail: Math.random() > .77,
  });

  const resize = () => {
    paintProgress();
    if (!context) return;
    width = window.innerWidth;
    height = window.innerHeight;
    const ratio = Math.min(window.devicePixelRatio || 1, 1.5);
    canvas.width = Math.round(width * ratio);
    canvas.height = Math.round(height * ratio);
    context.setTransform(ratio, 0, 0, ratio, 0, 0);
    particles = Array.from({ length: width < 600 ? 24 : 55 }, () => particle());
  };

  const animate = (time) => {
    if (!context || paused || motionPreference.matches || document.hidden) {
      frame = 0;
      return;
    }
    frame = requestAnimationFrame(animate);
    // Cap painting at 30fps, DPR at 1.5, and particle count on small displays.
    if (time - lastTime < 32) return;
    const delta = Math.min((time - lastTime) / 1000 || .033, .07);
    lastTime = time;
    context.clearRect(0, 0, width, height);
    const gust = 1.3 + Math.sin(time * .00045) * .5;
    particles.forEach((p, index) => {
      p.x -= p.speed * delta * gust;
      p.y += (Math.sin(time * .0006 + p.phase) * 7 + 9) * delta;
      if (p.x < -90 || p.y > height + 20) {
        particles[index] = particle(false);
        return;
      }
      // Keep the reading area calm; wind is brightest along the outer edges.
      const edge = p.x < width * .12 || p.x > width * .68 || p.y > height * .8;
      const alpha = p.opacity * (edge ? .85 : .22) * (.7 + scrollAmount * .3);
      context.strokeStyle = `rgba(200,245,255,${alpha})`;
      context.fillStyle = `rgba(215,249,255,${alpha})`;
      if (p.trail) {
        const trail = 14 + p.speed * .55;
        const gradient = context.createLinearGradient(p.x, p.y, p.x + trail, p.y - trail * .12);
        gradient.addColorStop(0, `rgba(210,248,255,${alpha})`);
        gradient.addColorStop(1, 'rgba(180,234,255,0)');
        context.strokeStyle = gradient;
        context.lineWidth = .65;
        context.beginPath();
        context.moveTo(p.x, p.y);
        context.lineTo(p.x + trail, p.y - trail * .12);
        context.stroke();
      } else {
        context.beginPath();
        context.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        context.fill();
        if (p.size > 2 && edge) {
          context.lineWidth = .6;
          context.beginPath();
          context.moveTo(p.x - 4, p.y); context.lineTo(p.x + 4, p.y);
          context.moveTo(p.x, p.y - 4); context.lineTo(p.x, p.y + 4);
          context.stroke();
        }
      }
    });
  };

  const syncMotion = () => {
    const stopped = paused || motionPreference.matches || document.hidden;
    page.classList.toggle('effects-paused', stopped);
    if (button) {
      button.hidden = motionPreference.matches;
      button.setAttribute('aria-pressed', String(paused));
      button.querySelector('.motion-label').textContent = paused ? 'Effekte starten' : 'Effekte pausieren';
      button.querySelector('.motion-icon').textContent = paused ? '▷' : 'Ⅱ';
    }
    if (stopped) {
      if (frame) cancelAnimationFrame(frame);
      frame = 0;
      if (context && motionPreference.matches) context.clearRect(0, 0, width, height);
    } else if (!frame && context) {
      lastTime = 0;
      frame = requestAnimationFrame(animate);
    }
  };
  if (button) button.addEventListener('click', () => { paused = !paused; syncMotion(); });
  motionPreference.addEventListener('change', syncMotion);
  document.addEventListener('visibilitychange', syncMotion);
  window.addEventListener('resize', resize, { passive: true });
  resize();
  syncMotion();
})();
