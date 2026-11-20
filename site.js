// The site's moving pictures (src/visuals.py): each plays only while it is on screen, has a button to pause
// it, and stays a still for visitors who switched motion off in their system until they press Play.
(function () {
  var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var figures = document.querySelectorAll('[data-viz]');
  if (!figures.length) return;

  function setUp(figure) {
    var video = figure.querySelector('video');
    var button = figure.querySelector('.viz-pp');
    var stopped = still;      // the visitor's own choice
    var visible = false;

    function apply() {
      var run = visible && !stopped;
      if (video) {
        if (run) {
          var p = video.play();   // the file is fetched now, not before (preload="none")
          // The browser may refuse to start it (a phone saving power): then it is stopped, and the button says so.
          if (p && p.catch) p.catch(function () { if (!stopped && video.paused) { stopped = true; label(); } });
        } else {
          video.pause();
        }
      } else {
        figure.classList.toggle('paused', !run);
      }
      label();
    }
    function label() {
      if (button) button.textContent = stopped ? button.dataset.play : button.dataset.pause;
    }

    // An animated explanation moves only once this script is here to pause it; until then it is its still.
    if (!video && !still) figure.classList.add('on');
    if (button && (video || !still)) {
      button.hidden = false;
      // Whoever presses Play is looking at it, however little of it the window shows.
      button.addEventListener('click', function () { stopped = !stopped; if (!stopped) visible = true; apply(); });
    }
    if ('IntersectionObserver' in window) {
      // On screen: a good third of it, or, when it is taller than the window, half the window.
      new IntersectionObserver(function (entries) {
        var e = entries[entries.length - 1];
        visible = e.isIntersecting && (e.intersectionRatio >= 0.35 || e.intersectionRect.height >= window.innerHeight * 0.5);
        apply();
      }, { threshold: [0, 0.1, 0.2, 0.35, 0.5, 0.75] }).observe(figure);
    } else {
      visible = true;
      apply();
    }
  }
  figures.forEach(setUp);
})();
