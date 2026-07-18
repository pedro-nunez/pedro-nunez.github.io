// Wires up the light/dark toggle button (see _includes/header.html and
// the .theme-toggle rule in main.css). The initial data-theme attribute
// (if any) is set earlier by the inline script in _layouts/default.html,
// so a stored choice takes effect before the page paints; this file only
// needs to handle clicks and keep the button's icon in sync.

(function () {
  function currentTheme() {
    var stored = document.documentElement.getAttribute("data-theme");
    if (stored === "light" || stored === "dark") return stored;
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  // Shows the theme a click would switch TO, not the current one.
  function updateIcon(button, theme) {
    button.textContent = theme === "dark" ? "☀️" : "🌙";
  }

  document.addEventListener("DOMContentLoaded", function () {
    var button = document.getElementById("theme-toggle");
    if (!button) return;

    updateIcon(button, currentTheme());

    button.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      localStorage.setItem("theme", next);
      updateIcon(button, next);
    });
  });
})();
