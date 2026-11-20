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
    'fits': {
        'online': {'en': 'Online · the Zoom meeting', 'de': 'Online · das Zoom-Meeting', 'es': 'En línea · la reunión de Zoom', 'it': 'Online · la riunione Zoom'},
        'remote': {'en': 'Remote speaker', 'de': 'Zugeschaltete Rednerin', 'es': 'Ponente remota', 'it': 'Relatrice da remoto'},
        'audience': {'en': 'Audience online', 'de': 'Publikum online', 'es': 'Público en línea', 'it': 'Pubblico online'},
        'watching': {'en': 'sees and hears Hall A', 'de': 'sieht und hört Saal A', 'es': 've y oye la Sala A', 'it': 'vede e sente la Sala A'},
        'live': {'en': 'Live', 'de': 'Live', 'es': 'En directo', 'it': 'In diretta'},
        'control': {'en': 'Control room · Director', 'de': 'Regie · Director', 'es': 'Sala de control · Director', 'it': 'Regia · Director'},
        'spot': {'en': 'Spotlight', 'de': 'Spotlight', 'es': 'Destacada', 'it': 'In evidenza'},
        'inhall': {'en': 'In Hall A · the screen', 'de': 'In Saal A · die Leinwand', 'es': 'En la Sala A · la pantalla', 'it': 'In Sala A · lo schermo'},
        'idle': {'en': 'Waiting for the speaker', 'de': 'Wartet auf die Rednerin', 'es': 'Esperando a la ponente', 'it': 'In attesa della relatrice'},
        'pc': {'en': "The hall's PC, with OBS Studio and Spectacast Meet", 'de': 'Der Saal-PC, mit OBS Studio und Spectacast Meet', 'es': 'El PC de la sala, con OBS Studio y Spectacast Meet', 'it': 'Il PC di sala, con OBS Studio e Spectacast Meet'},
        'cap_b': {'en': "A remote speaker joins. The operator puts them on the hall's screen.", 'de': 'Eine Rednerin schaltet sich zu. Die Regie bringt sie auf die Leinwand im Saal.', 'es': 'Se conecta una ponente remota. El operador la pone en la pantalla de la sala.', 'it': 'Una relatrice si collega da remoto. La regia la porta sullo schermo della sala.'},
        'cap': {'en': 'The hall goes back out to everyone online.', 'de': 'Der Saal geht zurück an alle, die online dabei sind.', 'es': 'La sala vuelve a todos los que están en línea.', 'it': 'La sala torna a tutti quelli che sono online.'},
        'alt': {
            'en': 'Animation: a remote speaker joins the Zoom meeting and appears in Director in the control room. The operator picks her and puts her in the spotlight, she appears on the screen in Hall A, and the audience online sees and hears the hall.',
            'de': 'Animation: Eine Rednerin schaltet sich ins Zoom-Meeting zu und erscheint in Director in der Regie. Der Operator wählt sie aus und setzt sie ins Spotlight, sie erscheint auf der Leinwand in Saal A, und das Publikum online sieht und hört den Saal.',
            'es': 'Animación: una ponente remota se conecta a la reunión de Zoom y aparece en Director, en la sala de control. El operador la elige y la destaca, ella aparece en la pantalla de la Sala A y el público en línea ve y oye la sala.',
            'it': "Animazione: una relatrice si collega da remoto alla riunione Zoom e compare in Director, in regia. L'operatore la sceglie e la mette in evidenza, lei compare sullo schermo della Sala A e il pubblico online vede e sente la sala.",
        },
    },
    # The stories below are told in steps (STEPS): site.js moves them on, site.css shows what each step adds.
    'cert': {
        'doors': {'en': 'At the doors · Hall A', 'de': 'An den Eingängen · Saal A', 'es': 'En las puertas · Sala A', 'it': 'Agli ingressi · Sala A'},
        'in': {'en': 'in', 'de': 'ein', 'es': 'entrada', 'it': 'entrata'},
        'out': {'en': 'out', 'de': 'aus', 'es': 'salida', 'it': 'uscita'},
        'att': {'en': 'Attendance', 'de': 'Anwesenheit', 'es': 'Asistencia', 'it': 'Presenze'},
        'minutes': {'en': '218 minutes in sessions', 'de': '218 Minuten in Sessions', 'es': '218 minutos en sesiones', 'it': '218 minuti nelle sessioni'},
        'percent': {'en': '87 % of the program', 'de': '87 % des Programms', 'es': '87 % del programa', 'it': '87 % del programma'},
        'needed': {'en': 'you asked for 75 %', 'de': 'verlangt sind 75 %', 'es': 'pides el 75 %', 'it': 'ne chiedi il 75 %'},
        'cert': {'en': 'Certificate', 'de': 'Bescheinigung', 'es': 'Certificado', 'it': 'Attestato'},
        'notyet': {'en': 'Not yet', 'de': 'Noch nicht', 'es': 'Todavía no', 'it': 'Non ancora'},
        'title': {'en': 'Certificate of attendance', 'de': 'Teilnahmebescheinigung', 'es': 'Certificado de asistencia', 'it': 'Attestato di presenza'},
        'ready': {'en': 'Ready to download', 'de': 'Bereit zum Download', 'es': 'Listo para descargar', 'it': 'Pronto da scaricare'},
        'cap_b': {'en': 'Scans become minutes. Minutes become the certificate.', 'de': 'Aus Scans werden Minuten. Aus Minuten wird die Bescheinigung.', 'es': 'Las lecturas se convierten en minutos. Los minutos, en el certificado.', 'it': "Le letture diventano minuti. I minuti diventano l'attestato."},
        'cap': {'en': 'Whoever meets the requirements you set downloads it themselves.', 'de': 'Wer Ihre Vorgaben erfüllt, lädt sie selbst herunter.', 'es': 'Quien cumple los requisitos que pones lo descarga por su cuenta.', 'it': 'Chi soddisfa i requisiti che imposti lo scarica da solo.'},
        'alt': {
            'en': 'Animation: Sofia Navarro is scanned in at 09:02 and out at 12:40 at the Hall A door. Pass counts 218 minutes in sessions, 87 % of the program where 75 % is asked, and her certificate of attendance is ready to download.',
            'de': 'Animation: Sofia Navarro wird am Eingang von Saal A um 09:02 beim Hineingehen und um 12:40 beim Hinausgehen gescannt. Pass zählt 218 Minuten in Sessions, 87 % des Programms bei verlangten 75 %, und ihre Teilnahmebescheinigung steht zum Download bereit.',
            'es': 'Animación: a Sofia Navarro se le lee la acreditación al entrar a las 09:02 y al salir a las 12:40 en la puerta de la Sala A. Pass cuenta 218 minutos en sesiones, el 87 % del programa cuando se pide el 75 %, y su certificado de asistencia queda listo para descargar.',
            'it': "Animazione: il badge di Sofia Navarro viene letto all'ingresso della Sala A alle 09:02 in entrata e alle 12:40 in uscita. Pass conta 218 minuti nelle sessioni, l'87 % del programma a fronte del 75 % richiesto, e il suo attestato di presenza è pronto da scaricare.",
        },
    },
    'translate': {
        'heard': {'en': 'Heard · Italian', 'de': 'Gehört · Italienisch', 'es': 'Oído · italiano', 'it': 'Sentito · italiano'},
        'mic': {'en': "The speaker's microphone", 'de': 'Das Mikrofon der Rednerin', 'es': 'El micrófono de la ponente', 'it': 'Il microfono della relatrice'},
        'pair': {'en': 'Italian → English', 'de': 'Italienisch → Englisch', 'es': 'Italiano → inglés', 'it': 'Italiano → inglese'},
        'said': {'en': 'Said · English', 'de': 'Gesprochen · Englisch', 'es': 'Dicho · inglés', 'it': 'Detto · inglese'},
        'hall': {'en': "The hall's speakers", 'de': 'Die Lautsprecher im Saal', 'es': 'Los altavoces de la sala', 'it': 'Gli altoparlanti della sala'},
        'channel': {'en': 'An interpretation channel of the meeting', 'de': 'Ein Dolmetschkanal des Meetings', 'es': 'Un canal de interpretación de la reunión', 'it': 'Un canale di interpretariato della riunione'},
        'headsets': {'en': 'The headsets', 'de': 'Die Kopfhörer', 'es': 'Los auriculares', 'it': 'Le cuffie'},
        'cap_b': {'en': 'The speaker talks in Italian. The hall hears English.', 'de': 'Die Rednerin spricht Italienisch. Der Saal hört Englisch.', 'es': 'La ponente habla en italiano. La sala oye inglés.', 'it': 'La relatrice parla in italiano. La sala sente inglese.'},
        'cap': {'en': 'On any audio output, and you can read both.', 'de': 'Auf jedem Audioausgang, und beides lässt sich mitlesen.', 'es': 'En cualquier salida de audio, y puedes leer las dos.', 'it': 'Su qualsiasi uscita audio, e puoi leggere entrambe.'},
        'alt': {
            'en': 'Animation: a speaker says a sentence in Italian into the microphone. Spectacast Translator shows it as heard and as said in English, and the English voice goes to the hall\'s speakers, an interpretation channel of the meeting and the headsets.',
            'de': 'Animation: Eine Rednerin sagt einen Satz auf Italienisch ins Mikrofon. Spectacast Translator zeigt ihn wie gehört und wie auf Englisch gesprochen, und die englische Stimme geht an die Lautsprecher im Saal, einen Dolmetschkanal des Meetings und die Kopfhörer.',
            'es': 'Animación: una ponente dice una frase en italiano al micrófono. Spectacast Translator la muestra tal como se oyó y tal como se dijo en inglés, y la voz en inglés va a los altavoces de la sala, a un canal de interpretación de la reunión y a los auriculares.',
            'it': "Animazione: una relatrice dice una frase in italiano al microfono. Spectacast Translator la mostra come sentita e come detta in inglese, e la voce in inglese va agli altoparlanti della sala, a un canale di interpretariato della riunione e alle cuffie.",
        },
    },
    'feeds': {
        'meeting': {'en': 'The Zoom meeting', 'de': 'Das Zoom-Meeting', 'es': 'La reunión de Zoom', 'it': 'La riunione Zoom'},
        'home': {'en': 'Speaker, at home', 'de': 'Rednerin, zu Hause', 'es': 'Ponente, en casa', 'it': 'Relatrice, da casa'},
        'theatre': {'en': 'Surgeon, in the operating room', 'de': 'Chirurg, im OP', 'es': 'Cirujano, en el quirófano', 'it': 'Chirurgo, in sala operatoria'},
        'slides': {'en': 'Slides', 'de': 'Folien', 'es': 'Diapositivas', 'it': 'Slide'},
        'share': {'en': 'A screen share', 'de': 'Eine Bildschirmfreigabe', 'es': 'Una pantalla compartida', 'it': 'Uno schermo condiviso'},
        'pc': {'en': 'Hall PC · Spectacast Meet', 'de': 'Saal-PC · Spectacast Meet', 'es': 'PC de la sala · Spectacast Meet', 'it': 'PC di sala · Spectacast Meet'},
        'each': {'en': 'A feed for each one', 'de': 'Ein Signal für jede Person', 'es': 'Una señal para cada uno', 'it': 'Un segnale per ognuno'},
        'sound': {'en': 'video and sound, over NDI', 'de': 'Bild und Ton, über NDI', 'es': 'vídeo y sonido, por NDI', 'it': 'video e audio, via NDI'},
        'sources': {'en': 'Sources in OBS or the mixer', 'de': 'Quellen in OBS oder im Mischpult', 'es': 'Fuentes en OBS o en el mezclador', 'it': 'Sorgenti in OBS o nel mixer'},
        'onscreen': {'en': 'On the screen', 'de': 'Auf der Leinwand', 'es': 'En pantalla', 'it': 'Sullo schermo'},
        'cap_b': {'en': 'Everyone in the meeting becomes a source of their own.', 'de': 'Jede Person im Meeting wird zu einer eigenen Quelle.', 'es': 'Cada persona de la reunión se convierte en una fuente propia.', 'it': 'Ogni persona in riunione diventa una sorgente a sé.'},
        'cap': {'en': 'The hall picks them like cameras.', 'de': 'Der Saal wählt sie wie Kameras.', 'es': 'La sala las elige como cámaras.', 'it': 'La sala le sceglie come telecamere.'},
        'alt': {
            'en': 'Animation: a speaker at home, a surgeon in the operating room and a screen share are in the Zoom meeting. Spectacast Meet on the hall PC gives each one a feed of its own over NDI, they appear one by one as sources in OBS or the mixer, and the first is put on the screen.',
            'de': 'Animation: Eine Rednerin zu Hause, ein Chirurg im OP und eine Bildschirmfreigabe sind im Zoom-Meeting. Spectacast Meet auf dem Saal-PC gibt jedem ein eigenes Signal über NDI, sie erscheinen nacheinander als Quellen in OBS oder im Mischpult, und die erste kommt auf die Leinwand.',
            'es': 'Animación: una ponente en casa, un cirujano en el quirófano y una pantalla compartida están en la reunión de Zoom. Spectacast Meet, en el PC de la sala, da a cada uno una señal propia por NDI, aparecen una a una como fuentes en OBS o en el mezclador, y la primera se pone en pantalla.',
            'it': "Animazione: una relatrice da casa, un chirurgo in sala operatoria e uno schermo condiviso sono nella riunione Zoom. Spectacast Meet, sul PC di sala, dà a ognuno un segnale proprio via NDI, compaiono uno dopo l'altro come sorgenti in OBS o nel mixer, e la prima va sullo schermo.",
        },
    },
    'mic': {
        'phone': {'en': 'A phone · Spectacast Mic', 'de': 'Ein Telefon · Spectacast Mic', 'es': 'Un teléfono · Spectacast Mic', 'it': 'Un telefono · Spectacast Mic'},
        'channel': {'en': 'Channel · Hall A', 'de': 'Kanal · Saal A', 'es': 'Canal · Sala A', 'it': 'Canale · Sala A'},
        'question': {'en': 'A question from the floor', 'de': 'Eine Frage aus dem Publikum', 'es': 'Una pregunta del público', 'it': 'Una domanda dalla platea'},
        'heard': {'en': 'You can be heard', 'de': 'Sie sind zu hören', 'es': 'Se te oye', 'it': 'Ti sentono'},
        'pc': {'en': 'Hall PC · Mic receiver', 'de': 'Saal-PC · Mic-Empfänger', 'es': 'PC de la sala · receptor de Mic', 'it': 'PC di sala · ricevitore Mic'},
        'wifi': {'en': "Over the venue's Wi-Fi", 'de': 'Über das WLAN vor Ort', 'es': 'Por la wifi del recinto', 'it': 'Sul Wi-Fi della sede'},
        'nointernet': {'en': 'no internet needed', 'de': 'ohne Internet', 'es': 'sin internet', 'it': 'senza internet'},
        'inputs': {'en': 'Audio inputs · OBS, mixer, meeting', 'de': 'Audioeingänge · OBS, Mischpult, Meeting', 'es': 'Entradas de audio · OBS, mezclador, reunión', 'it': 'Ingressi audio · OBS, mixer, riunione'},
        'hallmic': {'en': 'Hall microphone', 'de': 'Saalmikrofon', 'es': 'Micrófono de sala', 'it': 'Microfono di sala'},
        'cap_b': {'en': 'Someone talks into their phone. The hall PC gets one more microphone.', 'de': 'Jemand spricht ins eigene Telefon. Der Saal-PC bekommt ein weiteres Mikrofon.', 'es': 'Alguien habla a su teléfono. El PC de la sala recibe un micrófono más.', 'it': 'Qualcuno parla nel proprio telefono. Il PC di sala riceve un microfono in più.'},
        'cap': {'en': 'Next to the hall\'s own, for OBS, the mixer or the meeting.', 'de': 'Neben denen des Saals, für OBS, das Mischpult oder das Meeting.', 'es': 'Junto a los de la sala, para OBS, el mezclador o la reunión.', 'it': 'Accanto a quelli della sala, per OBS, il mixer o la riunione.'},
        'alt': {
            'en': 'Animation: someone in the audience joins the Hall A channel in the Spectacast Mic app and talks into the phone. Over the venue\'s Wi-Fi the Mic receiver on the hall PC gets the voice, and it appears as one more audio input, next to the hall microphone.',
            'de': 'Animation: Jemand im Publikum tritt in der App Spectacast Mic dem Kanal von Saal A bei und spricht ins Telefon. Über das WLAN vor Ort erhält der Mic-Empfänger auf dem Saal-PC die Stimme, und sie erscheint als weiterer Audioeingang neben dem Saalmikrofon.',
            'es': 'Animación: alguien del público entra en el canal de la Sala A en la app Spectacast Mic y habla al teléfono. Por la wifi del recinto, el receptor de Mic del PC de la sala recibe la voz, y aparece como una entrada de audio más, junto al micrófono de sala.',
            'it': "Animazione: qualcuno in platea entra nel canale della Sala A nell'app Spectacast Mic e parla nel telefono. Sul Wi-Fi della sede il ricevitore Mic del PC di sala riceve la voce, che compare come un ingresso audio in più, accanto al microfono di sala.",
        },
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


def _fits(t):
    return f"""<div class="st-flow">
<div class="st-tile"><span class="st-label"><span>{t('online')}</span></span>
<div class="st-row f-spk">Dr. Elena Ortega<small>{t('remote')}</small></div>
<div class="st-row f-pair"><span>{t('audience')}<small>{t('watching')}</small></span><span class="f-pill f-live">{t('live')}</span></div></div>
<div class="st-link f-l1"></div>
<div class="st-tile"><span class="st-label"><span>{t('control')}</span></span>
<div class="st-row">Prof. Jonas Weber</div>
<div class="st-row">Dr. Nils Brandt</div>
<div class="st-row f-pair f-pick"><span>Dr. Elena Ortega</span><span class="f-pill f-spot">{t('spot')}</span><i class="f-tap"></i></div></div>
<div class="st-link f-l2"></div>
<div class="st-tile"><span class="st-label"><span>{t('inhall')}</span></span>
<div class="f-screen"><span class="f-idle">{t('idle')}</span><span class="f-on">Dr. Elena Ortega<i class="f-meter"><b></b></i></span></div>
<small class="f-pc">{t('pc')}</small></div>
</div>"""


METER = '<i class="f-meter"><b></b></i>'


def _cert(t):
    return f"""<div class="st-flow">
<div class="st-tile"><span class="st-label"><span>{t('doors')}</span></span>
<div class="st-row at-1">Sofia Navarro<small>09:02 → {t('in')}</small></div>
<div class="st-row at-2">Sofia Navarro<small>12:40 ← {t('out')}</small></div></div>
<div class="st-link go-3"></div>
<div class="st-tile hot-3"><span class="st-label"><span>{t('att')}</span></span>
<div class="st-row at-3">{t('minutes')}</div>
<div class="st-row at-4">{t('percent')}<i class="f-meter wide"><b style="width:87%"></b></i><small>{t('needed')}</small></div></div>
<div class="st-link go-5"></div>
<div class="st-tile hot-5"><span class="st-label"><span>{t('cert')}</span></span>
<div class="st-stack"><div class="st-empty till-5">{t('notyet')}</div>
<div class="st-paper at-5"><b>{t('title')}</b>Sofia Navarro<span class="f-pill f-spot">{t('ready')}</span></div></div></div>
</div>"""


def _translate(t):
    return f"""<div class="st-flow">
<div class="st-tile"><span class="st-label"><span>{t('heard')}</span></span>
<div class="st-row">{t('mic')}{METER}</div>
<div class="st-row at-1" lang="it">Buongiorno a tutti e grazie per essere qui.</div></div>
<div class="st-link go-2"></div>
<div class="st-tile hot-2"><span class="st-label"><span>Spectacast Translator</span></span>
<div class="st-row">{t('pair')}</div>
<div class="st-row at-3" lang="en">Good morning everyone, and thank you for being here.</div></div>
<div class="st-link go-4"></div>
<div class="st-tile"><span class="st-label"><span>{t('said')}</span></span>
<div class="st-row at-5">{t('hall')}{METER}</div>
<div class="st-row at-5">{t('channel')}{METER}</div>
<div class="st-row at-5">{t('headsets')}{METER}</div></div>
</div>"""


def _feeds(t):
    return f"""<div class="st-flow">
<div class="st-tile"><span class="st-label"><span>{t('meeting')}</span></span>
<div class="st-row">Dr. Elena Ortega<small>{t('home')}</small></div>
<div class="st-row">Prof. Jonas Weber<small>{t('theatre')}</small></div>
<div class="st-row">{t('slides')}<small>{t('share')}</small></div></div>
<div class="st-link go-1"></div>
<div class="st-tile hot-1"><span class="st-label"><span>{t('pc')}</span></span>
<div class="st-row at-1">{t('each')}<small>{t('sound')}</small></div></div>
<div class="st-link go-2"></div>
<div class="st-tile"><span class="st-label"><span>{t('sources')}</span></span>
<div class="st-row f-pair at-2"><span>Dr. Elena Ortega</span><span class="f-pill f-live at-5">{t('onscreen')}</span></div>
<div class="st-row at-3">Prof. Jonas Weber</div>
<div class="st-row at-4">{t('slides')}</div></div>
</div>"""


def _mic(t):
    return f"""<div class="st-flow">
<div class="st-tile"><span class="st-label"><span>{t('phone')}</span></span>
<div class="st-row">{t('channel')}<small>{t('question')}</small></div>
<div class="st-row at-1">{t('heard')}{METER}</div></div>
<div class="st-link go-2"></div>
<div class="st-tile hot-2"><span class="st-label"><span>{t('pc')}</span></span>
<div class="st-row at-2">{t('wifi')}<small>{t('nointernet')}</small></div></div>
<div class="st-link go-3"></div>
<div class="st-tile"><span class="st-label"><span>{t('inputs')}</span></span>
<div class="st-row">{t('hallmic')}{METER}</div>
<div class="st-row at-4">Spectacast Mic 1{METER}</div></div>
</div>"""


STORIES = {'rule': _rule, 'fits': _fits, 'cert': _cert, 'translate': _translate, 'feeds': _feeds, 'mic': _mic}
# Stories told in steps, with how many steps each has.
STEPS = {'cert': 5, 'translate': 5, 'feeds': 5, 'mic': 4}


def _text(text):
    """A caption or a legend line as written in the page: plain text, with **bold**."""
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html.escape(text.strip(), quote=False))


def _button(lang):
    p, q = html.escape(UI['pause'][lang]), html.escape(UI['play'][lang])
    return f'<button type="button" class="viz-pp" hidden data-pause="{p}" data-play="{q}">{p}</button>'


def story(lang, name, alt=None):
    """alt: the description for screen readers; without one, the story's own 'alt' text."""
    if name not in STORIES:
        raise SystemExit(f'no story called {name}: there is {", ".join(STORIES)}')
    texts = STORY_TEXTS[name]
    missing = [k for k, v in texts.items() if lang not in v]
    if missing:
        raise SystemExit(f'story {name}: no {lang} text for {", ".join(missing)}')
    t = lambda k: html.escape(texts[k][lang], quote=False)
    alt = alt or texts['alt'][lang]
    steps = f' data-steps="{STEPS[name]}"' if name in STEPS else ''
    return (f'\n<figure class="viz story s-{name}" data-viz{steps}>'
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
LOOP_FOCUS = {'director-speaker': 30, 'pass-scan': 0}


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
