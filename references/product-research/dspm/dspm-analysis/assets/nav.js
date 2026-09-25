(function () {
  const path = window.location.pathname.split('/').pop();
  const links = document.querySelectorAll('[data-nav] a');
  links.forEach((a) => {
    const href = a.getAttribute('href');
    if (href === path) a.style.outline = '2px solid #66b3ff';
  });
})();
