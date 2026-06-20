// mini-coi.js
addEventListener("load", function () {
  if (typeof window.crossOriginIsolated !== "undefined" && !window.crossOriginIsolated) {
    document.head.appendChild(
      Object.assign(document.createElement("script"), {
        src: "https://unpkg.com/coi-serviceworker/coi-serviceworker.js",
      })
    );
  }
});   
