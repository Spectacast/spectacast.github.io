// The site's moving pictures (src/visuals.py): each plays only while it is on screen, has a button to pause
// it, and stays a still for visitors who switched motion off in their system until they press Play.
(function () {
  var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var figures = document.querySelectorAll('[data-viz]');
  if (!figures.length) return;

  function setUp(figure) {
    // A loop recorded for light and for dark pages has two videos; the style sheet shows one of them.
    var videos = figure.querySelectorAll('video');
    function shown() {
      for (var i = 0; i < videos.length; i++) if (videos[i].offsetWidth) return videos[i];
      return videos[0];
    }
    var button = figure.querySelector('.viz-pp');
    var stopped = still;      // the visitor's own choice
    var visible = false;
    var steps = !still && +figure.dataset.steps || 0, beat = 0, timer = 0;
    if (steps) figure.dataset.step = 0;

    function apply() {
      var run = visible && !stopped;
      var video = shown();
      if (video) {
        for (var i = 0; i < videos.length; i++) if (videos[i] !== video) videos[i].pause();
        if (run) {
          var p = video.play();   // the file is fetched now, not before (preload="none")
          // The browser may refuse to start it (a phone saving power): then it is stopped, and the button says so.
          if (p && p.catch) p.catch(function () { if (!stopped && video.paused) { stopped = true; label(); } });
        } else {
          video.pause();
        }
      } else {
        figure.classList.toggle('paused', !run);
        if (steps) {
          // Only start or stop the beat when that changes: the browser reports on scrolling many times over.
          if (run) { if (!timer) timer = setInterval(next, 1300); }
          else { clearInterval(timer); timer = 0; }
        }
      }
      label();
    }
    // A story told in steps: one more every beat, three beats on the last, then from the start.
    function next() {
      beat = beat >= steps + 3 ? 0 : beat + 1;
      figure.dataset.step = Math.min(beat, steps);
    }
    function label() {
      if (button) button.textContent = stopped ? button.dataset.play : button.dataset.pause;
    }

    // An animated explanation moves only once this script is here to pause it; until then it is its still.
    if (!videos.length && !still) figure.classList.add('on');
    if (button && (videos.length || !still)) {
      button.hidden = false;
      button.addEventListener('click', function () {
        stopped = !stopped;
        // Whoever presses Play is looking at it, however little of it the window shows.
        if (!stopped) visible = true;
        // A story in steps is paused on its whole picture, not on a half-built one, and plays again from the start.
        if (steps) { beat = 0; if (stopped) delete figure.dataset.step; else figure.dataset.step = 0; }
        apply();
      });
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
