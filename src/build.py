#!/usr/bin/env python3
"""Builds spectacast.com in English, German, Spanish and Italian.

    pip install markdown
    python3 src/build.py          # writes the pages into the repository root
    python3 src/build.py --check  # also fails on a missing language, a broken link or a missing anchor

Sources, all in this folder:
  home.html           the English body of the home page; home_texts.py holds its translations, and the build
                      stops on an English text without them, so the page cannot go out half translated
  pages/<key>.<lang>.md  pricing and the legal pages, one file per language
  content.py          seller details, plans, prices, VAT
  this file           the shared page frame (header, footer, head tags) and the labels it uses

Every page goes through one frame, so the header, the footer and the buttons are the same everywhere.
LAUNCHED switches the buttons that may only appear at the 1.0 launch (sign in, free trial, downloads).
"""
import html
import pathlib
import re
import sys
from decimal import Decimal, ROUND_HALF_UP

import markdown

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import content as C  # noqa: E402
import home_texts as T  # noqa: E402

OUT = HERE.parent
SITE = 'https://spectacast.com'

# Liviu, 19 Nov 2026: pages and docs go live as they are merged; the free trial, downloads and checkout
# appear only on launch day. Until then the header offers "Contact us".
LAUNCHED = False
CONTACT = 'info@spectacast.com'
SIGN_IN = '/account/'
TRIAL = '/account/'  # the sign-up page of Account, once it exists

LANGS = ('en', 'de', 'es', 'it')  # English is the source; the order shown in the language menu
NAMES = {'en': 'English', 'de': 'Deutsch', 'es': 'Español', 'it': 'Italiano'}
PAGES = {  # key: path per language
    'home': {'en': '', 'de': 'de/', 'es': 'es/', 'it': 'it/'},
    'pricing': {'en': 'pricing/', 'de': 'de/preise/', 'es': 'es/precios/', 'it': 'it/prezzi/'},
    'terms': {'en': 'terms/', 'de': 'de/agb/', 'es': 'es/terminos/', 'it': 'it/termini/'},
    'refunds': {'en': 'refunds/', 'de': 'de/erstattung/', 'es': 'es/reembolsos/', 'it': 'it/rimborsi/'},
    'privacy': {'en': 'privacy/', 'de': 'de/datenschutz/', 'es': 'es/privacidad/', 'it': 'it/privacy/'},
}
# Product pages live under a folder of their own: /pass and /meet on this domain belong to the apps.
PRODUCTS = ('director', 'meet', 'mic', 'translator', 'pass')
PRODUCT_DIR = {'en': 'products/', 'de': 'de/produkte/', 'es': 'es/productos/', 'it': 'it/prodotti/'}
for _p in PRODUCTS:
    PAGES[_p] = {l: f'{d}{_p}/' for l, d in PRODUCT_DIR.items()}
FOOTER_LINKS = ('pricing', 'terms', 'refunds', 'privacy')
# Paths served by other programs behind the same domain: links to them are not checked here.
OTHER_APPS = ('/account', '/pass', '/program', '/meet')

LABELS = {
    'en': {'terms': 'Terms', 'refunds': 'Refund Policy', 'privacy': 'Privacy', 'pricing': 'Pricing',
           'product': 'Product', 'contact': 'Contact us', 'signin': 'Sign in', 'trial': 'Start free trial',
           'menu': 'Main menu', 'plans': 'Included in', 'see_pricing': 'See pricing', 'more': 'More about', 'products': 'Products', 'langs': 'Language',
           'draft': 'Draft: the highlighted parts are still to be filled in.'},
    'de': {'terms': 'AGB', 'refunds': 'Erstattungen', 'privacy': 'Datenschutz', 'pricing': 'Preise',
           'product': 'Produkt', 'contact': 'Kontakt', 'signin': 'Anmelden', 'trial': 'Kostenlos testen',
           'menu': 'Hauptmenü', 'plans': 'Enthalten in', 'see_pricing': 'Preise ansehen', 'more': 'Mehr über', 'products': 'Produkte', 'langs': 'Sprache',
           'draft': 'Entwurf: Die markierten Stellen sind noch zu ergänzen.'},
    'es': {'terms': 'Términos', 'refunds': 'Reembolsos', 'privacy': 'Privacidad', 'pricing': 'Precios',
           'product': 'Producto', 'contact': 'Contacto', 'signin': 'Iniciar sesión', 'trial': 'Prueba gratis',
           'menu': 'Menú principal', 'plans': 'Incluido en', 'see_pricing': 'Ver precios', 'more': 'Más sobre', 'products': 'Productos', 'langs': 'Idioma',
           'draft': 'Borrador: las partes resaltadas aún están por completar.'},
    'it': {'terms': 'Termini', 'refunds': 'Rimborsi', 'privacy': 'Privacy', 'pricing': 'Prezzi',
           'product': 'Prodotto', 'contact': 'Contattaci', 'signin': 'Accedi', 'trial': 'Prova gratis',
           'menu': 'Menu principale', 'plans': 'Incluso in', 'see_pricing': 'Vedi i prezzi', 'more': 'Scopri', 'products': 'Prodotti', 'langs': 'Lingua',
           'draft': 'Bozza: le parti evidenziate sono ancora da completare.'},
}
TRADEMARKS = ('Zoom is a trademark of Zoom Communications, Inc. NDI is a registered trademark of Vizrt NDI AB. '
              'OBS Studio is a project of the OBS Project.')
DATE = {'en': '18 November 2026', 'de': '18. November 2026', 'es': '18 de noviembre de 2026', 'it': '18 novembre 2026'}

MARK_SVG = ('<svg viewBox="140 80 250 340" aria-hidden="true"><path d="M290 116 H252 A68 68 0 0 0 252 252 H260 '
            'A68 68 0 0 1 260 388 H196" fill="none" stroke="currentColor" stroke-width="56" stroke-linecap="round" '
            'stroke-linejoin="round"/><circle cx="356" cy="116" r="27" fill="#ff3b30"/></svg>')


# ---------- money ----------

def euro(lang, amount, places):
    """An amount written the way the language writes money: € 1,428.00 / 1.428,00 € / € 1.428,00."""
    s = f'{amount:,.{places}f}'
    if lang != 'en':
        s = s.replace(',', ' ').replace('.', ',').replace(' ', '.')
    return f'{s} €' if lang in ('de', 'es') else f'€ {s}'


def gross(lang, net, places=2):
    q = Decimal(1).scaleb(-places)
    return (Decimal(net) * (100 + C.VAT[lang]) / 100).quantize(q, ROUND_HALF_UP)


def money(lang, name):
    """Yearly and event price of a plan before VAT, and the same two with the example VAT."""
    return [(euro(lang, x, 0), euro(lang, gross(lang, x), 2)) for x in C.PRICES[name]]


def mark(s):
    """[text] (not followed by '(') -> highlighted placeholder."""
    return re.sub(r'\[([^\]\[]+)\](?!\()', r'<mark class="todo">\1</mark>', s)


# ---------- frame ----------

def url(lang, key):
    return '/' + PAGES[key][lang]


def alternates(key):
    out = [f'<link rel="alternate" hreflang="{l}" href="{SITE}{url(l, key)}">' for l in LANGS]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}{url("en", key)}">')
    return '\n'.join(out)


def header(lang, key):
    l = LABELS[lang]
    current = ' aria-current="page"' if key == 'pricing' else ''
    nav = [f'<a class="nav-product" href="{url(lang, "home")}#modules">{l["product"]}</a>',
           f'<a href="{url(lang, "pricing")}"{current}>{l["pricing"]}</a>']
    langs = ''.join(f'<a href="{url(x, key)}" hreflang="{x}" lang="{x}" aria-label="{NAMES[x]}">{x.upper()}</a>'
                    for x in LANGS if x != lang)
    if LAUNCHED:
        cta = (f'<a class="signin" href="{SIGN_IN}">{l["signin"]}</a>'
               f'<a class="sc-btn sc-btn--primary" href="{TRIAL}">{l["trial"]}</a>')
    else:
        cta = f'<a class="sc-btn sc-btn--primary" href="mailto:{CONTACT}">{l["contact"]}</a>'
    return f'''<header class="site-head">
    <a class="brand" href="{url(lang, 'home')}">{MARK_SVG}spectacast</a>
    <nav aria-label="{l['menu']}">{''.join(nav)}</nav>
    <nav class="langs" aria-label="{l['langs']}">{langs}</nav>
    <div class="cta">{cta}</div>
  </header>'''


def footer(lang, key):
    l = LABELS[lang]
    links = ' · '.join(f'<a href="{url(lang, k)}">{l[k]}</a>' for k in FOOTER_LINKS)
    langs = ' · '.join(NAMES[x] if x == lang else f'<a href="{url(x, key)}" hreflang="{x}" lang="{x}">{NAMES[x]}</a>'
                       for x in LANGS)
    seller = mark(C.VALUES[lang]['SELLER'])
    marks = TRADEMARKS if lang == 'en' else T.BODY[TRADEMARKS][lang]
    return f'''<footer class="site-foot">
    <p>{links} · <a href="mailto:{CONTACT}">{CONTACT}</a></p>
    <p>{langs}</p>
    <p>© 2026 {seller} · spectacast.com</p>
    <p>{html.escape(marks, quote=False)}</p>
  </footer>'''


def og_image(body):
    m = re.search(r'<img src="(/img/screens/[^"]+)"', body)
    return SITE + (m.group(1) if m else '/brand/lockup-light.png')


def frame(lang, key, title, description, body, main_class):
    """A whole page: head tags, header, the page's own body and the footer."""
    full_title = title if key == 'home' else f'{title} · Spectacast'
    d = html.escape(description)
    return f'''<!doctype html>
<html lang="{lang}" class="sc">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title, quote=False)}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{SITE}{url(lang, key)}">
{alternates(key)}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Spectacast">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{SITE}{url(lang, key)}">
<meta property="og:image" content="{og_image(body)}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/design/spectacast.css">
<link rel="stylesheet" href="/site.css">
</head>
<body>
<div class="wrap">
  {header(lang, key)}
  <main class="{main_class}">
{body}
  </main>
  {footer(lang, key)}
</div>
</body>
</html>
'''


# ---------- pages from Markdown ----------

def plans_html(lang):
    p = C.PLANS[lang]
    out = [f'''<div class="billing" role="radiogroup" aria-label="{p['from']}">
  <input type="radio" name="billing" id="b-year" checked><label for="b-year">{p['year']}</label>
  <input type="radio" name="billing" id="b-event"><label for="b-event">{p['event']}</label>
</div>
<div class="plans">''']
    for name, what, mods, feats in p['plans']:
        (year, year_vat), (event, event_vat) = money(lang, name)
        vat = C.VAT_LINE[lang]
        lis = ''.join(f'<li>{mark(html.escape(f))}</li>' for f in feats)
        out.append(f'''  <article class="plan">
    <h3><span>Spectacast</span> {name}</h3>
    <p class="what">{what}</p>
    <p class="mods">{mods}</p>
    <div class="price">
      <p class="p-year"><b>{mark(year)}</b> {p['per_year']}{C.NET[lang]}<span class="vat">{vat.format(year_vat)}</span></p>
      <p class="p-event"><b>{mark(event)}</b> {mark(p['per_event'])}{C.NET[lang]}<span class="vat">{vat.format(event_vat)}</span></p>
    </div>
    <ul>{lis}</ul>
  </article>''')
    out.append('</div>')
    return '\n'.join(out)


def text_of(fragment):
    return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', '', fragment))).strip()


IMG = OUT / 'img' / 'screens'


def shot(lang, name, alt, cls=''):
    """A screenshot: the page's language when there is one, and the dark one in dark mode when there is one."""
    def have(n):
        return (IMG / f'{n}.webp').is_file()
    base = next((n for n in (f'{name}-{lang}', f'{name}-en', f'{name}-light', name) if have(n)), None)
    if base is None:
        raise SystemExit(f'no screenshot img/screens/{name}*.webp')
    dark = base[:-6] + '-dark' if base.endswith('-light') and have(base[:-6] + '-dark') else None
    from PIL import Image  # only for the size, so the page does not jump while images load
    w, h = Image.open(IMG / f'{base}.webp').size
    img = f'<img src="/img/screens/{base}.webp" alt="{html.escape(alt)}" width="{w}" height="{h}" loading="lazy">'
    if dark:
        img = f'<picture><source srcset="/img/screens/{dark}.webp" media="(prefers-color-scheme: dark)">{img}</picture>'
    return f'\n<figure class="shot {cls}">{img}</figure>\n'


def product_blocks(lang, md):
    """{{shot:name|alt}}, {{phone:name|alt}}, {{plans:A,B}} and {{cta}} in a product page's Markdown."""
    l = LABELS[lang]
    md = re.sub(r'\{\{shot:([\w-]+)\|([^}]+)\}\}', lambda m: shot(lang, m.group(1), m.group(2)), md)
    md = re.sub(r'\{\{phone:([\w-]+)\|([^}]+)\}\}', lambda m: shot(lang, m.group(1), m.group(2), 'phone'), md)

    def plans(m):
        names = [n.strip() for n in m.group(1).split(',')]
        chips = ''.join(f'<span>Spectacast {n}</span>' for n in names)
        return (f'\n<div class="in-plans"><b>{l["plans"]}</b>{chips}'
                f'<a href="{url(lang, "pricing")}">{l["see_pricing"]} →</a></div>\n')
    md = re.sub(r'\{\{plans:([^}]+)\}\}', plans, md)
    if LAUNCHED:
        cta = f'<a class="sc-btn sc-btn--primary" href="{TRIAL}">{l["trial"]}</a>'
    else:
        cta = f'<a class="sc-btn sc-btn--primary" href="mailto:{CONTACT}">{l["contact"]}</a>'
    cta += f'<a class="sc-btn" href="{url(lang, "pricing")}">{l["see_pricing"]}</a>'
    return md.replace('{{cta}}', f'\n<div class="cta-row">{cta}</div>\n')


def md_page(lang, key):
    v = dict(C.VALUES[lang])
    v['date'] = DATE[lang]
    for k, name in (('terms', 'TERMS_URL'), ('refunds', 'REFUND_URL'), ('privacy', 'PRIVACY_URL')):
        v[name] = url(lang, k)
    v['VAT_WHERE'] = C.VAT_WHERE[lang]
    v['MINUTE_GROSS'] = euro(lang, gross(lang, C.MINUTE, 3), 3)
    assert v['MINUTE_PRICE'] == euro(lang, C.MINUTE, 2), v['MINUTE_PRICE']
    md = (HERE / 'pages' / f'{key}.{lang}.md').read_text()
    if key in PRODUCTS:
        md = product_blocks(lang, md)
    md = re.sub(r'\{\{(\w+)\}\}', lambda m: v[m.group(1)], md)
    body = mark(markdown.markdown(md, extensions=['tables']))
    if key == 'pricing':
        body = body.replace('<!--PLANS-->', plans_html(lang))
    title = text_of(re.search(r'<h1>(.*?)</h1>', body).group(1))
    # The description is the first paragraph after the title (for the legal pages: the paragraph after the date).
    paras = [text_of(p) for p in re.findall(r'<p>(.*?)</p>', body, re.S)]
    paras = [p for p in paras if len(p) > 60]
    description = paras[0] if paras else title
    if len(description) > 200:
        description = description[:197].rsplit(' ', 1)[0].rstrip(',;:') + '…'
    if 'class="todo"' in body:
        body = f'<p class="draft-note">{LABELS[lang]["draft"]}</p>\n' + body
    main = 'pricing' if key == 'pricing' else 'product' if key in PRODUCTS else 'doc'
    return frame(lang, key, title, description, body, main)


# ---------- home page ----------

def norm(t):
    return re.sub(r'\s+', ' ', t).strip()


def home_page(lang):
    """The home page: home.html is the English body, the other languages are made from it with home_texts.py."""
    body = (HERE / 'home.html').read_text()
    title_en = 'Spectacast'
    desc_en = next(iter(T.HEAD))
    if lang != 'en':
        def sub(m):
            raw = m.group(1)
            t = norm(html.unescape(raw))
            if not t or t in T.KEEP:
                return m.group(0)
            if t not in T.BODY:
                raise SystemExit(f'home page: no {lang} translation for {t!r} (add it to src/home_texts.py)')
            lead, trail = raw[:len(raw) - len(raw.lstrip())], raw[len(raw.rstrip()):]
            return '>' + lead + html.escape(T.BODY[t][lang], quote=False) + trail + '<'

        body = re.sub(r'>([^<]+)<', sub, body)

        def alt(m):
            t = norm(html.unescape(m.group(1)))
            if t not in T.BODY:
                raise SystemExit(f'home page: no {lang} translation for the image text {t!r}')
            return f'alt="{html.escape(T.BODY[t][lang])}"'
        body = re.sub(r'alt="([^"]+)"', alt, body)
        # A screenshot in this language when there is one.
        body = re.sub(r'(/img/screens/[\w-]+)-en\.webp',
                      lambda m: f'{m.group(1)}-{lang}.webp' if (OUT / f'{m.group(1)[1:]}-{lang}.webp').is_file() else m.group(0),
                      body)
    for key in PAGES:  # links written for English point to the same page in this language
        body = body.replace(f'href="{url("en", key)}"', f'href="{url(lang, key)}"') if key != 'home' else body
    description = desc_en if lang == 'en' else T.HEAD[desc_en][lang]
    return frame(lang, 'home', title_en, description, body.rstrip('\n'), 'home')


# ---------- checks ----------

def check(written):
    """Every page in every language, and every link between our pages pointing at something that exists."""
    problems = []
    for key, paths in PAGES.items():
        missing = [l for l in LANGS if l not in paths]
        if missing:
            problems.append(f'{key}: no page in {", ".join(missing)}')
    ids = {}
    for path, text in written.items():
        ids[path] = set(re.findall(r'\bid="([^"]+)"', text))
    for path, text in written.items():
        for ref in re.findall(r'(?:href|src)="([^"]+)"', text):
            if ref.startswith(('mailto:', 'http://', 'https://')):
                continue
            if ref.startswith('#'):
                target, frag = path, ref[1:]
            else:
                if not ref.startswith('/'):
                    problems.append(f'{path}: relative link {ref}')
                    continue
                if '..' in ref.split('/'):
                    problems.append(f'{path}: link with .. {ref}')
                    continue
                if any(ref == a or ref.startswith(a + '/') or ref.startswith(a + '?') for a in OTHER_APPS):
                    continue
                target, _, frag = ref.partition('#')
                target = target.split('?', 1)[0]
                f = OUT / target.lstrip('/')
                if target.endswith('/'):
                    f = f / 'index.html'
                if not f.is_file():
                    problems.append(f'{path}: broken link {ref}')
                    continue
                target = target if target.endswith('/') else None
            if frag and target is not None:
                if target not in ids:
                    problems.append(f'{path}: anchor {ref} points to a page this build does not make')
                elif frag not in ids[target]:
                    problems.append(f'{path}: no anchor #{frag} on {target}')
    if 'class="todo"' in ''.join(written.values()) and LAUNCHED:
        problems.append('placeholders [..] are still on the pages at launch')
    return problems


def sitemap(keys):
    rows = []
    for key in keys:
        alts = ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{url(l, key)}"/>' for l in LANGS)
        for lang in LANGS:
            rows.append(f'  <url>\n    <loc>{SITE}{url(lang, key)}</loc>{alts}\n  </url>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + '\n'.join(rows) + '\n</urlset>\n')


def main():
    written = {}
    for key, paths in PAGES.items():
        for lang, path in paths.items():
            page = home_page(lang) if key == 'home' else md_page(lang, key)
            d = OUT / path
            d.mkdir(parents=True, exist_ok=True)
            (d / 'index.html').write_text(page)
            written['/' + path] = page
    (OUT / 'sitemap.xml').write_text(sitemap(PAGES))
    (OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    print(f'wrote {len(written)} pages, sitemap.xml and robots.txt')
    if '--check' in sys.argv:
        problems = check(written)
        for p in problems:
            print('PROBLEM', p)
        if problems:
            sys.exit(1)
        print('check: every page in', ', '.join(LANGS), 'and every link resolves')


if __name__ == '__main__':
    main()
