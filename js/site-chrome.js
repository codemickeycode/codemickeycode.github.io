(function () {
  const header = '<header class="site-header"><div class="shell nav"><a class="wordmark" href="index.html">code<span>mickey</span>code</a><button class="menu-toggle" type="button" aria-label="Toggle navigation" aria-expanded="false" aria-controls="site-menu">Menu</button><nav class="menu" id="site-menu" aria-label="Main navigation"><a href="about.html">About</a><a href="work.html">Work</a><a href="https://blog.codemickeycode.com/" target="_blank" rel="noopener">Blog</a></nav></div></header>';
  const footer = '<footer class="site-footer"><div class="shell footer-inner"><span>Code. Passion. Freedom. Making a Difference.</span><span>© <span data-year></span> Micaela Reyes</span></div></footer>';

  document.querySelectorAll('[data-partial="header"]').forEach(function (placeholder) {
    placeholder.outerHTML = header;
  });

  document.querySelectorAll('[data-partial="footer"]').forEach(function (placeholder) {
    placeholder.outerHTML = footer;
  });
}());
