(() => {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const layer = document.createElement('div');
  layer.className = 'wash-pointer-foam';
  layer.setAttribute('aria-hidden', 'true');
  document.body.append(layer);

  const sizes = [7, 10, 14, 20, 29, 40, 52];
  const maxBubbles = 90;
  let lastMove = 0;
  let lastX = -100;
  let lastY = -100;

  function addBubble(x, y, index) {
    const bubble = document.createElement('span');
    const size = sizes[Math.floor(Math.random() * sizes.length)];
    const spread = index % 2 ? 1 : -1;
    bubble.className = `wash-pointer-bubble${size <= 14 ? ' is-foam' : ''}`;
    bubble.style.setProperty('--x', `${x + (Math.random() - .5) * 34}px`);
    bubble.style.setProperty('--y', `${y + (Math.random() - .5) * 26}px`);
    bubble.style.setProperty('--size', `${size}px`);
    bubble.style.setProperty('--dx', `${spread * (16 + Math.random() * 54)}px`);
    bubble.style.setProperty('--dy', `${-42 - Math.random() * 88}px`);
    bubble.style.setProperty('--duration', `${900 + Math.random() * 700}ms`);
    bubble.addEventListener('animationend', () => bubble.remove(), { once: true });
    layer.append(bubble);
  }

  function burst(x, y, count) {
    if (reducedMotion.matches || document.hidden) return;
    for (let i = 0; i < count; i += 1) addBubble(x, y, i);
    while (layer.childElementCount > maxBubbles) layer.firstElementChild.remove();
  }

  document.addEventListener('pointermove', (event) => {
    if (event.pointerType !== 'mouse') return;
    const now = performance.now();
    if (now - lastMove < 45 || Math.hypot(event.clientX - lastX, event.clientY - lastY) < 12) return;
    lastMove = now;
    lastX = event.clientX;
    lastY = event.clientY;
    burst(event.clientX, event.clientY, 3);
  }, { passive: true });

  document.addEventListener('pointerdown', (event) => {
    if (event.pointerType === 'touch') burst(event.clientX, event.clientY, 12);
  }, { passive: true });

  reducedMotion.addEventListener('change', () => {
    if (reducedMotion.matches) layer.replaceChildren();
  });
})();
