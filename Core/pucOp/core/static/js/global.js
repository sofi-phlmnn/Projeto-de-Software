(function () {
  const drawer = document.getElementById('site-drawer');
  const backdrop = document.getElementById('drawerBackdrop');
  const btn = document.getElementById('hamburgerBtn');

  if (!drawer || !backdrop || !btn) return;

  const openDrawer = () => {
    drawer.classList.add('is-open');
    backdrop.hidden = false;
    document.body.classList.add('no-scroll');
    btn.setAttribute('aria-expanded', 'true');
    drawer.setAttribute('aria-hidden', 'false');
  };

  const closeDrawer = () => {
    drawer.classList.remove('is-open');
    backdrop.hidden = true;
    document.body.classList.remove('no-scroll');
    btn.setAttribute('aria-expanded', 'false');
    drawer.setAttribute('aria-hidden', 'true');
  };

  btn.addEventListener('click', () => {
    const isOpen = drawer.classList.contains('is-open');
    isOpen ? closeDrawer() : openDrawer();
  });

  backdrop.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeDrawer();
  });

  // Fecha se um link do drawer for clicado
  drawer.addEventListener('click', (e) => {
    const a = e.target.closest('a');
    if (a) closeDrawer();
  });

  // ---- Realce de link ativo (client-side, fallback/extra) ----
  const markActive = (selector) => {
    const links = document.querySelectorAll(selector);
    const path = window.location.pathname.replace(/\/+$/, '') || '/';

    links.forEach(a => {
      try {
        const href = a.getAttribute('href');
        if (!href) return;
        // normaliza
        const normHref = href.replace(window.location.origin, '').replace(/\/+$/, '') || '/';
        // ativa quando caminho bater exatamente ou quando o caminho atual começa com o href (útil para subrotas)
        if (path === normHref || (normHref !== '/' && path.startsWith(normHref))) {
          a.classList.add('is-active');
          a.setAttribute('aria-current', 'page');
        }
      } catch {}
    });
  };

  // marca nos dois menus
  markActive('.topnav__link');
  markActive('.drawer__link');
})();
