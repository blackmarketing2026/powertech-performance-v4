(() => {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const reveals = document.querySelectorAll('.graffiti-page .reveal');
  if (reducedMotion || !('IntersectionObserver' in window)) {
    reveals.forEach((element) => element.classList.add('is-visible'));
  } else {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    reveals.forEach((element) => observer.observe(element));
  }

  if (reducedMotion) return;
  const progress = document.querySelector('.frost-progress');
  let frame = 0;
  const paint = () => {
    const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    const amount = Math.min(1, Math.max(0, window.scrollY / maxScroll));
    document.documentElement.style.setProperty('--cold', amount.toFixed(3));
    if (progress) progress.style.transform = `scaleX(${amount})`;
    frame = 0;
  };
  window.addEventListener('scroll', () => {
    if (!frame) frame = requestAnimationFrame(paint);
  }, { passive: true });
  window.addEventListener('resize', paint, { passive: true });
  paint();
})();
