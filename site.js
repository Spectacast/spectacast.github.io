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
          if (!video.currentSrc && !video.dataset.loaded) {
            video.dataset.loaded = '1';
            video.querySelectorAll('source[data-src]').forEach(function (s) { s.src = s.dataset.src; });
            video.load();
          }
          var p = video.play();
          if (p && p.catch) p.catch(function () {});
        } else {
          video.pause();
        }
      } else {
        figure.classList.toggle('paused', !run);
      }
      if (button) {
        button.textContent = stopped ? button.dataset.play : button.dataset.pause;
        button.setAttribute('aria-pressed', String(stopped));
      }
    }

    if (button && (video || !still)) {
      button.hidden = false;
      button.addEventListener('click', function () { stopped = !stopped; apply(); });
    }
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        visible = entries[entries.length - 1].isIntersecting;
        apply();
      }, { threshold: 0.35 }).observe(figure);
    } else {
      visible = true;
      apply();
    }
  }
  figures.forEach(setUp);
})();
