(function () {
  if (!document.querySelector(".arithmatex")) return;

  var loader = document.currentScript;
  if (!loader) {
    console.error("Unable to resolve the MathJax configuration path.");
    return;
  }

  var config = document.createElement("script");
  config.src = new URL("mathjax-config.js", loader.src).href;
  config.onload = function () {
    var mathjax = document.createElement("script");
    mathjax.src = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js";
    mathjax.async = true;
    mathjax.onerror = function () {
      console.error("Failed to load MathJax from jsDelivr.");
    };
    document.head.appendChild(mathjax);
  };
  config.onerror = function () {
    console.error("Failed to load the MathJax configuration.");
  };
  document.head.appendChild(config);
})();
