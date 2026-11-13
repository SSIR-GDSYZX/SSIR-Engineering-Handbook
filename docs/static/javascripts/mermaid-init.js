(function () {
  var diagrams = document.querySelectorAll(".mermaid");
  if (!diagrams.length) return;

  var script = document.createElement("script");
  script.src = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js";
  script.async = true;
  script.onload = function () {
    if (!window.mermaid) {
      console.error("Mermaid loaded without exposing its API.");
      return;
    }

    window.mermaid.initialize({ startOnLoad: false });
    window.mermaid.run({ nodes: Array.from(diagrams) }).catch(function (error) {
      console.error("Mermaid diagram rendering failed.", error);
    });
  };
  script.onerror = function () {
    console.error("Failed to load Mermaid from jsDelivr.");
  };
  document.head.appendChild(script);
})();
