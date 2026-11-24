(() => {
  const $ = (s) => document.querySelector(s);
  const root = ($('meta[name=root]') || {}).content || './';
  const html = document.documentElement;
  // theme: system, then light, then dark
  const THEMES = ['', 'light', 'dark'];
  try { const t = localStorage.getItem('beril.docs.theme'); if (t) html.dataset.theme = t; } catch (e) {}
  $('#theme').onclick = () => {
    const cur = html.dataset.theme || '';
    const next = THEMES[(THEMES.indexOf(cur) + 1) % THEMES.length];
    if (next) html.dataset.theme = next; else delete html.dataset.theme;
    try { localStorage.setItem('beril.docs.theme', next); } catch (e) {}
  };
  // mobile drawer
  const menu = $('#menu');
  const setOpen = (o) => { document.body.classList.toggle('open', o); menu.setAttribute('aria-expanded', o); };
  menu.onclick = () => setOpen(!document.body.classList.contains('open'));
  $('#scrim').onclick = () => setOpen(false);
  // keep the active link in view
  const on = document.querySelector('.nav a.on');
  if (on) on.scrollIntoView({ block: 'center' });
  // copy buttons
  document.querySelectorAll('.doc pre').forEach((pre) => {
    const b = document.createElement('button');
    b.className = 'copy'; b.type = 'button'; b.textContent = 'Copy';
    b.onclick = async () => {
      try { await navigator.clipboard.writeText(pre.innerText.replace(/\n?Copy$/, '')); b.textContent = 'Copied'; } catch (e) { b.textContent = 'Press Ctrl C'; }
      setTimeout(() => (b.textContent = 'Copy'), 1400);
    };
    pre.appendChild(b);
  });
  // table of contents scroll spy
  const links = [...document.querySelectorAll('.toc a')];
  if (links.length && 'IntersectionObserver' in window) {
    const map = new Map(links.map((a) => [a.getAttribute('href').slice(1), a]));
    const io = new IntersectionObserver((es) => {
      es.forEach((e) => { if (e.isIntersecting) { links.forEach((l) => l.classList.remove('on')); const a = map.get(e.target.id); if (a) a.classList.add('on'); } });
    }, { rootMargin: '-72px 0px -70% 0px' });
    document.querySelectorAll('.doc h2[id], .doc h3[id]').forEach((h) => io.observe(h));
  }
  // search palette
  const pal = $('#pal'), inp = $('#palin'), list = $('#pallist');
  const data = window.BERIL_SEARCH || [];
  let sel = 0, hits = [];
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  function score(p, terms) {
    let s = 0;
    const t = p.t.toLowerCase(), g = p.g.toLowerCase(), h = p.h.join(' ').toLowerCase(), x = p.x.toLowerCase();
    for (const w of terms) {
      let k = 0;
      if (t === w) k += 12; else if (t.startsWith(w)) k += 8; else if (t.includes(w)) k += 6;
      if (h.includes(w)) k += 3;
      if (g.includes(w)) k += 1;
      if (x.includes(w)) k += 1;
      if (!k) return 0;
      s += k;
    }
    return s;
  }
  function snippet(p, terms) {
    const x = p.x, lo = x.toLowerCase();
    let i = -1;
    for (const w of terms) { i = lo.indexOf(w); if (i >= 0) break; }
    if (i < 0) return p.x.slice(0, 110);
    return (i > 30 ? '…' : '') + x.slice(Math.max(0, i - 30), i + 90);
  }
  function render() {
    const terms = inp.value.toLowerCase().split(/\s+/).filter(Boolean);
    hits = terms.length
      ? data.map((p) => [score(p, terms), p]).filter((a) => a[0] > 0).sort((a, b) => b[0] - a[0]).slice(0, 12).map((a) => a[1])
      : data.slice(0, 8);
    sel = Math.min(sel, Math.max(0, hits.length - 1));
    list.innerHTML = hits.length
      ? hits.map((p, i) => `<a class="hit ${i === sel ? 'on' : ''}" href="${root}${p.u}" data-i="${i}"><b>${esc(p.t)}</b><small>${esc(p.g)} · ${esc(snippet(p, terms))}</small></a>`).join('')
      : '<div class="empty">No match.</div>';
  }
  const open = () => { pal.hidden = false; inp.value = ''; sel = 0; render(); inp.focus(); };
  const close = () => { pal.hidden = true; };
  $('#searchbtn').onclick = open;
  pal.onclick = (e) => { if (e.target === pal) close(); };
  inp.oninput = () => { sel = 0; render(); };
  inp.onkeydown = (e) => {
    if (e.key === 'ArrowDown') { e.preventDefault(); sel = Math.min(sel + 1, hits.length - 1); render(); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); sel = Math.max(sel - 1, 0); render(); }
    else if (e.key === 'Enter' && hits[sel]) { location.href = root + hits[sel].u; }
  };
  addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); pal.hidden ? open() : close(); return; }
    const tag = (document.activeElement || {}).tagName;
    if (e.key === '/' && tag !== 'INPUT' && tag !== 'TEXTAREA') { e.preventDefault(); open(); }
    if (e.key === 'Escape') { close(); setOpen(false); }
  });
})();
