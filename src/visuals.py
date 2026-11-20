"""The site's moving and marked pictures.

Three kinds, each written in a page's Markdown as one token:

  {{story:name|description}}          an animated explanation drawn in the site's own code (STORIES below)
  {{loop:name|caption|description}}   a short recorded loop of the real product (img/loops/, tools/visuals/)
  {{closeup:name|description|First mark|Second mark}}
                                      a close-up with numbered marks (img/closeups/, the places of the marks
                                      beside each picture as .json) and what each one is

Every one has a caption or a legend and a description for screen readers, a pause button for anything that
moves, and a still for visitors who switched motion off in their system (site.js and site.css).
"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
LANGS = ('en', 'de', 'es', 'it')

UI = {
    'pause': {'en': 'Pause', 'de': 'Pause', 'es': 'Pausa', 'it': 'Pausa'},
    'play': {'en': 'Play', 'de': 'Abspielen', 'es': 'Reproducir', 'it': 'Riproduci'},
}

# ---------- animated explanations ----------

STORY_TEXTS = {
    'rule': {
        'wr': {'en': 'Waiting room · Hall A', 'de': 'Warteraum · Saal A', 'es': 'Sala de espera · Sala A', 'it': "Sala d'attesa · Sala A"},
        'nobody': {'en': 'Nobody waiting', 'de': 'Niemand wartet', 'es': 'Nadie espera', 'it': 'Nessuno in attesa'},
        'arrived': {'en': 'Speaker · just arrived', 'de': 'Rednerin · gerade angekommen', 'es': 'Ponente · acaba de llegar', 'it': 'Relatrice · appena arrivata'},
        'rule': {'en': 'Rule · Auto admit', 'de': 'Regel · Automatisch zulassen', 'es': 'Regla · Admitir automáticamente', 'it': 'Regola · Ammissione automatica'},
        'when': {'en': 'When someone enters the waiting room', 'de': 'Wenn jemand den Warteraum betritt', 'es': 'Cuando alguien entra en la sala de espera', 'it': "Quando qualcuno entra in sala d'attesa"},
        'and': {'en': 'and their name is on the list', 'de': 'und der Name auf der Liste steht', 'es': 'y su nombre está en la lista', 'it': 'e il suo nome è nella lista'},
        'then': {'en': 'Then admit them', 'de': 'Dann zulassen', 'es': 'Entonces se le admite', 'it': 'Allora viene ammesso'},
        'meeting': {'en': 'In the meeting · Hall A', 'de': 'Im Meeting · Saal A', 'es': 'En la reunión · Sala A', 'it': 'In riunione · Sala A'},
        'onair': {'en': 'On air', 'de': 'Auf Sendung', 'es': 'Al aire', 'it': 'In onda'},
        'cap_b': {'en': 'A speaker arrives. The rule lets them in.', 'de': 'Eine Rednerin kommt an. Die Regel lässt sie ein.', 'es': 'Llega una ponente. La regla la deja entrar.', 'it': 'Arriva una relatrice. La regola la fa entrare.'},
        'cap': {'en': 'The operator touched nothing.', 'de': 'Der Operator hat nichts angefasst.', 'es': 'El operador no ha tocado nada.', 'it': "L'operatore non ha toccato nulla."},
    },
}


def _rule(t):
    return f'''<div class="st-flow">
<div class="st-tile"><span class="st-label"><span>{t('wr')}</span><span class="st-count"><b class="r-c0">0</b><b class="r-c1">1</b>&nbsp;</span></span>
<div class="st-row r-guest">Dr. Elena Ortega<small>{t('arrived')}</small></div>
<div class="st-empty r-empty">{t('nobody')}</div></div>
<div class="st-link r-l1"></div>
<div class="st-tile r-rule"><span class="st-label"><span>{t('rule')}</span></span>
<div class="st-row r-when">{t('when')}<small>{t('and')}</small></div>
<div class="st-row r-then"><span>{t('then')}</span><span class="r-tick">✓</span></div></div>
<div class="st-link r-l2"></div>
<div class="st-tile"><span class="st-label"><span>{t('meeting')}</span><span class="st-count"><b class="r-m3">2</b><b class="r-m4">3</b>&nbsp;</span></span>
<div class="st-row">Prof. Jonas Weber</div>
<div class="st-row">Dr. Nils Brandt</div>
<div class="st-row r-in">Dr. Elena Ortega</div>
<span class="st-pill">{t('onair')}</span></div>
</div>'''


STORIES = {'rule': _rule}


def _text(text):
    """A caption or a legend line as written in the page: plain text, with **bold**."""
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html.escape(text.strip(), quote=False))


def _button(lang):
    p, q = html.escape(UI['pause'][lang]), html.escape(UI['play'][lang])
    return f'<button type="button" class="viz-pp" hidden data-pause="{p}" data-play="{q}">{p}</button>'


def story(lang, name, alt):
    if name not in STORIES:
        raise SystemExit(f'no story called {name}: there is {", ".join(STORIES)}')
    texts = STORY_TEXTS[name]
    missing = [k for k, v in texts.items() if lang not in v]
    if missing:
        raise SystemExit(f'story {name}: no {lang} text for {", ".join(missing)}')
    t = lambda k: html.escape(texts[k][lang], quote=False)
    return (f'\n<figure class="viz story s-{name}" data-viz>'
            f'<div class="viz-stage" data-surface="console" role="img" aria-label="{html.escape(alt)}">'
            f'<div aria-hidden="true">{STORIES[name](t)}</div></div>'
            f'<figcaption><span><b>{t("cap_b")}</b> {t("cap")}</span>{_button(lang)}</figcaption></figure>\n')


# ---------- recorded loops ----------

def _size(path):
    from PIL import Image  # only for the size, so the page does not jump while pictures load
    return Image.open(path).size


def _file(folder, name, lang, ext):
    for n in (f'{name}-{lang}', f'{name}-en', name):
        if (ROOT / 'img' / folder / f'{n}.{ext}').is_file():
            return n
    raise SystemExit(f'no img/{folder}/{name}*.{ext}')


# On a phone a wide loop is cut to 3:2 so its text stays readable; this is the part to keep, from the left in %.
LOOP_FOCUS = {'director-speaker': 30}


def loop(lang, name, caption, alt):
    n = _file('loops', name, lang, 'webm')
    for ext in ('mp4', 'webp'):
        if not (ROOT / 'img' / 'loops' / f'{n}.{ext}').is_file():
            raise SystemExit(f'img/loops/{n}.{ext} is missing')
    w, h = _size(ROOT / 'img' / 'loops' / f'{n}.webp')
    tall = ' tall' if h > w else ''
    focus = f' style="--focus:{LOOP_FOCUS[name]}%"' if name in LOOP_FOCUS else ''
    return (f'\n<figure class="viz loop{tall}" data-viz{focus}>'
            f'<video muted loop playsinline preload="none" poster="/img/loops/{n}.webp" width="{w}" height="{h}" aria-label="{html.escape(alt)}">'
            f'<source src="/img/loops/{n}.webm" type="video/webm"><source src="/img/loops/{n}.mp4" type="video/mp4"></video>'
            f'<figcaption><span>{_text(caption)}</span>{_button(lang)}</figcaption></figure>\n')


# ---------- close-ups ----------

def closeup(lang, name, alt, legend=()):
    n = _file('closeups', name, lang, 'webp')
    w, h = _size(ROOT / 'img' / 'closeups' / f'{n}.webp')
    marks = json.loads((ROOT / 'img' / 'closeups' / f'{n}.json').read_text())['marks']
    if len(marks) != len(legend):
        raise SystemExit(f'close-up {n}: {len(marks)} marks but {len(legend)} lines saying what they are')
    dots = ''.join(f'<span class="cu-mark" aria-hidden="true" style="left:{x:g}%;top:{y:g}%">{i + 1}</span>' for i, (x, y) in enumerate(marks))
    items = ''.join(f'<li>{_text(item)}</li>' for item in legend)
    # Taken at twice the size, shown at most at its own size, so it stays sharp.
    # A wide one keeps a readable size on a phone and scrolls sideways inside itself.
    wide = ' wide' if w // 2 > 600 else ''
    return (f'\n<figure class="viz closeup{wide}" style="max-width:{w // 2}px"><div class="cu-scroll"><div class="cu-shot" data-surface="console">'
            f'<img src="/img/closeups/{n}.webp" alt="{html.escape(alt)}" width="{w}" height="{h}" loading="lazy">{dots}</div></div>'
            f'<figcaption><ol class="cu-legend">{items}</ol></figcaption></figure>\n')
