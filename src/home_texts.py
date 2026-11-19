"""Texts of the home page of spectacast.com in the other languages.

English is the source and lives in src/home.html. Each entry here is
the English text exactly as on the page (whitespace does not matter), with its translations.
build.py stops when the page holds a text that is neither here nor in KEEP, so a change to the
English page cannot be published without its translations.
"""

# Text that is the same in every language: names, numbers, punctuation.
KEEP = {
    'spectacast', 'Spectacast', 'Director', 'Meet', 'Mic', 'Translator', 'Pass',
    'Multiview', 'Windows · macOS', 'Android', 'iOS', 'Offline',
    'OBS Studio', 'NDI', 'Spectacast Meet', 'Spectacast Mic', 'Spectacast Translator',
    'Sennheiser EW-DX', 'Dante', 'MIDI', '18', '7', '1', '·',
    'EN · DE · ES · IT', '© 2026 Spectacast · spectacast.com', '{{cta}}',
    'Buongiorno a tutti e grazie per essere qui.', 'Good morning everyone, and thank you for being here.',
    'Dr. Elena Ortega', '4',
}

# Attributes in <head>: description and social card.
HEAD = {
    'Spectacast runs live hybrid events: the halls, the online meeting, the microphones and live translation from one control room, through connectors for the tools you already use, and attendance at the doors with Pass.': {
        'de': 'Spectacast steuert hybride Live-Veranstaltungen: die Säle, das Online-Meeting, die Mikrofone und die Live-Übersetzung aus einer Regie, über Konnektoren für die Werkzeuge, die Sie schon nutzen, und die Anwesenheit an den Eingängen mit Pass.',
        'es': 'Spectacast dirige eventos híbridos en directo: las salas, la reunión en línea, los micrófonos y la traducción en directo desde una sola sala de control, mediante conectores para las herramientas que ya usas, y la asistencia en las puertas con Pass.',
        'it': 'Spectacast gestisce eventi ibridi dal vivo: le sale, la riunione online, i microfoni e la traduzione simultanea da un\'unica regia, tramite connettori per gli strumenti che usi già, e le presenze agli ingressi con Pass.',
    },
    'One control room for the hall, the meeting and the mics.': {
        'de': 'Eine Regie für den Saal, das Meeting und die Mikrofone.',
        'es': 'Una sola sala de control para la sala, la reunión y los micrófonos.',
        'it': 'Un\'unica regia per la sala, la riunione e i microfoni.',
    },
}

BODY = {
    # Home page as redesigned on 19 Nov 2026
    'Spectacast runs congresses and shows that happen in a room and online at once. Every hall, every remote speaker and every microphone on one dashboard, with rules that take care of the routine.': {
        'de': 'Spectacast steuert Kongresse und Shows, die im Saal und online zugleich stattfinden. Jeder Saal, jede zugeschaltete Person und jedes Mikrofon auf einem Dashboard, mit Regeln, die die Routine übernehmen.',
        'es': 'Spectacast dirige congresos y eventos que ocurren en una sala y en línea a la vez. Cada sala, cada ponente remoto y cada micrófono en un solo panel, con reglas que se ocupan de la rutina.',
        'it': "Spectacast gestisce congressi ed eventi che si svolgono in sala e online allo stesso tempo. Ogni sala, ogni relatore remoto e ogni microfono in un'unica dashboard, con regole che si occupano della routine.",
    },
    'Keeps running when the internet drops': {
        'de': 'Läuft weiter, wenn das Internet ausfällt',
        'es': 'Sigue funcionando si se cae internet',
        'it': 'Continua a funzionare se cade internet',
    },
    'Works with OBS, NDI and Zoom': {
        'de': 'Arbeitet mit OBS, NDI und Zoom',
        'es': 'Funciona con OBS, NDI y Zoom',
        'it': 'Funziona con OBS, NDI e Zoom',
    },
    'In English, German, Spanish and Italian': {
        'de': 'Auf Deutsch, Englisch, Spanisch und Italienisch',
        'es': 'En español, inglés, alemán e italiano',
        'it': 'In italiano, inglese, tedesco e spagnolo',
    },
    'Hall A': {
        'de': 'Saal A',
        'es': 'Sala A',
        'it': 'Sala A',
    },
    'On air': {
        'de': 'Auf Sendung',
        'es': 'Al aire',
        'it': 'In onda',
    },
    'Program · meeting and mics': {
        'de': 'Program · Meeting und Mikrofone',
        'es': 'Program · reunión y micrófonos',
        'it': 'Program · riunione e microfoni',
    },
    'Meeting': {
        'de': 'Meeting',
        'es': 'Reunión',
        'it': 'Riunione',
    },
    "4 in the hall's meeting": {
        'de': '4 im Meeting des Saals',
        'es': '4 en la reunión de la sala',
        'it': '4 nella riunione della sala',
    },
    '1 in the waiting room': {
        'de': '1 im Warteraum',
        'es': '1 en la sala de espera',
        'it': "1 in sala d'attesa",
    },
    'Admit': {
        'de': 'Zulassen',
        'es': 'Admitir',
        'it': 'Ammetti',
    },
    "Sofia's phone": {
        'de': 'Sofias Telefon',
        'es': 'El teléfono de Sofía',
        'it': 'Il telefono di Sofia',
    },
    'Question from the floor': {
        'de': 'Frage aus dem Publikum',
        'es': 'Pregunta del público',
        'it': 'Domanda dal pubblico',
    },
    'Door · Hall A': {
        'de': 'Zugang · Saal A',
        'es': 'Acceso · Sala A',
        'it': 'Varco · Sala A',
    },
    'Welcome, Sofia': {
        'de': 'Willkommen, Sofia',
        'es': 'Bienvenida, Sofía',
        'it': 'Benvenuta, Sofia',
    },
    'Faculty · 62 of 400 inside': {
        'de': 'Faculty · 62 von 400 im Saal',
        'es': 'Ponentes · 62 de 400 dentro',
        'it': 'Faculty · 62 di 400 in sala',
    },
    'Spectacast Director during a congress: four halls side by side, each with its meeting, its waiting room, Preview and Program.': {
        'de': 'Spectacast Director während eines Kongresses: vier Säle nebeneinander, jeder mit seinem Meeting, seinem Warteraum, Preview und Program.',
        'es': 'Spectacast Director durante un congreso: cuatro salas una al lado de otra, cada una con su reunión, su sala de espera, Preview y Program.',
        'it': "Spectacast Director durante un congresso: quattro sale affiancate, ognuna con la sua riunione, la sua sala d'attesa, Preview e Program.",
    },
    'How it fits together': {
        'de': 'So greift es ineinander',
        'es': 'Cómo encaja todo',
        'it': 'Come si combina tutto',
    },
    'A PC in every hall. One screen for all of them.': {
        'de': 'Ein PC in jedem Saal. Ein Bildschirm für alle.',
        'es': 'Un PC en cada sala. Una sola pantalla para todas.',
        'it': 'Un PC in ogni sala. Un solo schermo per tutte.',
    },
    'In each hall': {
        'de': 'In jedem Saal',
        'es': 'En cada sala',
        'it': 'In ogni sala',
    },
    "A PC with OBS Studio and Spectacast Meet puts the remote speakers on the hall's screen and sends the hall back to them.": {
        'de': 'Ein PC mit OBS Studio und Spectacast Meet bringt die zugeschalteten Vortragenden auf die Leinwand des Saals und schickt ihnen den Saal zurück.',
        'es': 'Un PC con OBS Studio y Spectacast Meet pone a los ponentes remotos en la pantalla de la sala y les devuelve la sala.',
        'it': 'Un PC con OBS Studio e Spectacast Meet porta i relatori remoti sullo schermo della sala e rimanda loro la sala.',
    },
    'In the control room': {
        'de': 'In der Regie',
        'es': 'En la sala de control',
        'it': 'In regia',
    },
    "Director sees every hall PC over the venue's own network. One operator follows the halls side by side and steps in where needed.": {
        'de': 'Director sieht jeden Saal-PC über das Netzwerk der Location. Eine Person verfolgt die Säle nebeneinander und greift ein, wo es nötig ist.',
        'es': 'Director ve cada PC de sala por la red del recinto. Un solo operador sigue las salas una al lado de otra e interviene donde hace falta.',
        'it': 'Director vede ogni PC di sala sulla rete della sede. Un solo operatore segue le sale affiancate e interviene dove serve.',
    },
    'Online': {
        'de': 'Online',
        'es': 'En línea',
        'it': 'Online',
    },
    'Speakers and audience join an ordinary Zoom meeting, with nothing new to install on their side.': {
        'de': 'Vortragende und Publikum treten einem gewöhnlichen Zoom-Meeting bei und müssen nichts Neues installieren.',
        'es': 'Ponentes y público se unen a una reunión de Zoom normal, sin instalar nada nuevo.',
        'it': 'Relatori e pubblico entrano in una normale riunione Zoom, senza installare nulla di nuovo.',
    },
    'At the doors': {
        'de': 'An den Zugängen',
        'es': 'En las puertas',
        'it': 'Agli ingressi',
    },
    'Phones and scanners read the badges with Pass and count who is in which session, and for how long.': {
        'de': 'Telefone und Scanner lesen mit Pass die Badges und zählen, wer in welcher Sitzung ist und wie lange.',
        'es': 'Teléfonos y lectores leen las acreditaciones con Pass y cuentan quién está en cada sesión y durante cuánto tiempo.',
        'it': 'Telefoni e lettori leggono i badge con Pass e contano chi è in quale sessione, e per quanto tempo.',
    },
    'Five modules. Take the ones you need.': {
        'de': 'Fünf Module. Nehmen Sie, was Sie brauchen.',
        'es': 'Cinco módulos. Elige los que necesitas.',
        'it': 'Cinque moduli. Prendi quelli che ti servono.',
    },
    'One dashboard sees every hall PC, the meeting and the mics at once. Put a speaker on air with one touch, and let rules do what an operator would otherwise do by hand.': {
        'de': 'Ein Dashboard sieht jeden Saal-PC, das Meeting und die Mikrofone zugleich. Schalten Sie Vortragende mit einem Tastendruck auf Sendung, und lassen Sie Regeln erledigen, was sonst von Hand zu tun wäre.',
        'es': 'Un solo panel ve cada PC de sala, la reunión y los micrófonos a la vez. Pon a un ponente al aire con un toque y deja que las reglas hagan lo que un operador haría a mano.',
        'it': "Un'unica dashboard vede ogni PC di sala, la riunione e i microfoni insieme. Manda in onda un relatore con un tocco e lascia alle regole ciò che un operatore farebbe a mano.",
    },
    'Every hall side by side': {
        'de': 'Alle Säle nebeneinander',
        'es': 'Todas las salas una al lado de otra',
        'it': 'Tutte le sale affiancate',
    },
    'Rules for admitting people, hand-overs and audio': {
        'de': 'Regeln für Einlass ins Meeting, Übergaben und Audio',
        'es': 'Reglas para admitir personas, relevos y audio',
        'it': 'Regole per ammissioni, passaggi e audio',
    },
    'Connectors for the tools you already use': {
        'de': 'Konnektoren für die Werkzeuge, die Sie schon nutzen',
        'es': 'Conectores para las herramientas que ya usas',
        'it': 'Connettori per gli strumenti che usi già',
    },
    'More about Director →': {
        'de': 'Mehr über Director →',
        'es': 'Más sobre Director →',
        'it': 'Scopri Director →',
    },
    'Joins the online meeting from the hall PC and gives each participant, the gallery and every screen share its own video feed with sound, for the hall to use like a camera.': {
        'de': 'Tritt dem Online-Meeting vom Saal-PC aus bei und gibt jeder teilnehmenden Person, der Galerie und jeder Bildschirmfreigabe ein eigenes Videosignal mit Ton, das der Saal wie eine Kamera nutzt.',
        'es': 'Se une a la reunión en línea desde el PC de sala y da a cada participante, a la galería y a cada pantalla compartida su propia señal de vídeo con sonido, que la sala usa como una cámara.',
        'it': 'Entra nella riunione online dal PC di sala e dà a ogni partecipante, alla galleria e a ogni schermo condiviso un proprio flusso video con audio, che la sala usa come una camera.',
    },
    'More about Meet →': {
        'de': 'Mehr über Meet →',
        'es': 'Más sobre Meet →',
        'it': 'Scopri Meet →',
    },
    "Speakers and crew talk into the phone they already have. The hall PC receives each one as an audio device, next to the hall's own microphones.": {
        'de': 'Vortragende und Team sprechen in das Telefon, das sie schon haben. Der Saal-PC empfängt jedes als Audiogerät, neben den Mikrofonen des Saals.',
        'es': 'Ponentes y equipo hablan por el teléfono que ya tienen. El PC de sala recibe cada uno como un dispositivo de audio, junto a los micrófonos de la sala.',
        'it': 'Relatori e squadra parlano nel telefono che hanno già. Il PC di sala riceve ciascuno come un dispositivo audio, accanto ai microfoni della sala.',
    },
    'More about Mic →': {
        'de': 'Mehr über Mic →',
        'es': 'Más sobre Mic →',
        'it': 'Scopri Mic →',
    },
    "Listens to a speaker and says it in another language on any audio output: the hall, the meeting's interpretation channel or a headset.": {
        'de': 'Hört einer sprechenden Person zu und sagt es in einer anderen Sprache auf jedem Audioausgang: im Saal, auf dem Dolmetschkanal des Meetings oder im Kopfhörer.',
        'es': 'Escucha a quien habla y lo dice en otro idioma por cualquier salida de audio: la sala, el canal de interpretación de la reunión o unos auriculares.',
        'it': "Ascolta chi parla e lo dice in un'altra lingua su qualsiasi uscita audio: la sala, il canale di interpretariato della riunione o una cuffia.",
    },
    'Every sentence shown as heard and as said': {
        'de': 'Jeder Satz, wie gehört und wie gesagt',
        'es': 'Cada frase, tal como se oyó y como se dijo',
        'it': 'Ogni frase, come sentita e come detta',
    },
    'A warning when the meaning flips': {
        'de': 'Eine Warnung, wenn sich der Sinn umkehrt',
        'es': 'Un aviso cuando el sentido se invierte',
        'it': 'Un avviso quando il senso si capovolge',
    },
    'Google Gemini or OpenAI, or your own key': {
        'de': 'Google Gemini oder OpenAI, oder Ihr eigener Schlüssel',
        'es': 'Google Gemini u OpenAI, o tu propia clave',
        'it': 'Google Gemini o OpenAI, o una tua chiave',
    },
    'More about Translator →': {
        'de': 'Mehr über Translator →',
        'es': 'Más sobre Translator →',
        'it': 'Scopri Translator →',
    },
    'Every badge carries a QR code. A phone, a tablet or a scanner at each door answers at once in green, amber or red, even when the network is down.': {
        'de': 'Jedes Badge trägt einen QR-Code. Ein Telefon, ein Tablet oder ein Scanner an jedem Zugang antwortet sofort in Grün, Gelb oder Rot, auch wenn das Netzwerk ausfällt.',
        'es': 'Cada acreditación lleva un código QR. Un teléfono, una tableta o un lector en cada puerta responde al instante en verde, ámbar o rojo, incluso sin red.',
        'it': 'Ogni badge ha un codice QR. Un telefono, un tablet o un lettore a ogni ingresso risponde subito in verde, giallo o rosso, anche senza rete.',
    },
    'Your rooms, sessions and rules': {
        'de': 'Ihre Räume, Sitzungen und Regeln',
        'es': 'Tus salas, sesiones y reglas',
        'it': 'Le tue sale, sessioni e regole',
    },
    'Live occupancy for every room': {
        'de': 'Live-Belegung für jeden Raum',
        'es': 'Aforo en directo de cada sala',
        'it': 'Occupazione in tempo reale di ogni sala',
    },
    'Attendance reports and certificates': {
        'de': 'Anwesenheitsberichte und Bescheinigungen',
        'es': 'Informes de asistencia y certificados',
        'it': 'Report delle presenze e attestati',
    },
    'More about Pass →': {
        'de': 'Mehr über Pass →',
        'es': 'Más sobre Pass →',
        'it': 'Scopri Pass →',
    },
    'Works with the tools you already use.': {
        'de': 'Arbeitet mit den Werkzeugen, die Sie schon nutzen.',
        'es': 'Funciona con las herramientas que ya usas.',
        'it': 'Funziona con gli strumenti che usi già.',
    },
    "Director's fleet page: each hall's meeting, people, waiting room and output": {
        'de': 'Die Flotte in Director: Meeting, Personen, Warteraum und Ausgang jedes Saals',
        'es': 'La flota en Director: la reunión, las personas, la sala de espera y la salida de cada sala',
        'it': "La flotta in Director: riunione, persone, sala d'attesa e uscita di ogni sala",
    },
    'The Translator control page: what was heard in Italian and what was said in English, line by line': {
        'de': 'Die Bedienseite von Translator: was auf Italienisch gehört und was auf Englisch gesagt wurde, Zeile für Zeile',
        'es': 'La página de control de Translator: lo que se oyó en italiano y lo que se dijo en inglés, línea a línea',
        'it': 'La pagina di controllo di Translator: quello che è stato sentito in italiano e quello che è stato detto in inglese, riga per riga',
    },
    'Pass during the congress: how many people are in each room, and the latest scans at the doors': {
        'de': 'Pass während des Kongresses: wie viele Personen in jedem Raum sind, und die letzten Scans an den Eingängen',
        'es': 'Pass durante el congreso: cuántas personas hay en cada sala y las últimas lecturas en las puertas',
        'it': 'Pass durante il congresso: quante persone ci sono in ogni sala e le ultime letture agli ingressi',
    },
    'The door app on a phone: a green screen with "Welcome Sofia"': {
        'de': 'Die Einlass-App auf einem Telefon: ein grüner Bildschirm mit „Welcome Sofia“',
        'es': 'La app de puerta en un teléfono: una pantalla verde con «Welcome Sofia»',
        'it': "L'app dell'ingresso su un telefono: uno schermo verde con «Welcome Sofia»",
    },
    'Read more →': {'de': 'Mehr erfahren →', 'es': 'Saber más →', 'it': 'Scopri di più →'},
    'Spectacast Director with four halls side by side: who is in each meeting, the waiting room, Preview and Program': {
        'de': 'Spectacast Director mit vier Sälen nebeneinander: wer in jedem Meeting ist, der Warteraum, Preview und Program',
        'es': 'Spectacast Director con cuatro salas una al lado de otra: quién está en cada reunión, la sala de espera, Preview y Program',
        'it': "Spectacast Director con quattro sale affiancate: chi è in ogni riunione, la sala d'attesa, Preview e Program",
    },
    # Navigation and section titles
    'Modules': {'de': 'Module', 'es': 'Módulos', 'it': 'Moduli'},
    'Connectors': {'de': 'Konnektoren', 'es': 'Conectores', 'it': 'Connettori'},
    'In production': {'de': 'Im Einsatz', 'es': 'En producción', 'it': 'In produzione'},
    'Pricing': {'de': 'Preise', 'es': 'Precios', 'it': 'Prezzi'},
    'Terms': {'de': 'AGB', 'es': 'Términos', 'it': 'Termini'},
    'Refund Policy': {'de': 'Erstattungen', 'es': 'Reembolsos', 'it': 'Rimborsi'},
    'Privacy': {'de': 'Datenschutz', 'es': 'Privacidad', 'it': 'Privacy'},

    # Hero
    'Live hybrid events': {'de': 'Hybride Live-Veranstaltungen', 'es': 'Eventos híbridos en directo', 'it': 'Eventi ibridi dal vivo'},
    'One control room for the hall, the meeting and the mics.': HEAD['One control room for the hall, the meeting and the mics.'],
    'Spectacast runs congresses and shows that happen in a room and online at once. The halls, the meeting with its remote speakers, the video feeds and the microphones are driven from one dashboard, through connectors for the tools you already use, with rules that take care of the routine.': {
        'de': 'Spectacast steuert Kongresse und Shows, die gleichzeitig im Saal und online stattfinden. Die Säle, das Meeting mit seinen zugeschalteten Sprechern, die Videosignale und die Mikrofone werden von einem Dashboard aus geführt, über Konnektoren für die Werkzeuge, die Sie schon nutzen, mit Regeln, die die Routine übernehmen.',
        'es': 'Spectacast dirige congresos y shows que ocurren a la vez en una sala y en línea. Las salas, la reunión con sus ponentes remotos, las señales de vídeo y los micrófonos se manejan desde un solo panel, mediante conectores para las herramientas que ya usas, con reglas que se ocupan de la rutina.',
        'it': 'Spectacast gestisce congressi e show che si svolgono insieme in sala e online. Le sale, la riunione con i relatori da remoto, i flussi video e i microfoni si guidano da un\'unica dashboard, tramite connettori per gli strumenti che usi già, con regole che si occupano della routine.',
    },

    # Director
    'The control room.': {'de': 'Die Regie.', 'es': 'La sala de control.', 'it': 'La regia.'},
    'An engine and a web dashboard that see every hall PC, the meeting and the mics at once. Cut scenes, admit and place remote speakers, route audio, and let rules do what an operator would do anyway. It talks to each tool through a connector, so the mixer, the video transport and the meeting platform are a choice, not a given.': {
        'de': 'Eine Engine und ein Web-Dashboard, die jeden Saal-PC, das Meeting und die Mikrofone gleichzeitig im Blick haben. Szenen umschalten, zugeschaltete Sprecher einlassen und platzieren, Ton routen und Regeln das tun lassen, was ein Operator ohnehin tun würde. Mit jedem Werkzeug spricht Director über einen Konnektor, sodass der Mischer, der Videotransport und die Meeting-Plattform eine Wahl sind und keine Vorgabe.',
        'es': 'Un motor y un panel web que ven a la vez cada PC de sala, la reunión y los micrófonos. Cambia de escena, admite y coloca a los ponentes remotos, encamina el audio y deja que las reglas hagan lo que un operador haría de todos modos. Habla con cada herramienta a través de un conector, de modo que el mezclador, el transporte de vídeo y la plataforma de reuniones son una elección, no una imposición.',
        'it': 'Un motore e una dashboard web che vedono insieme ogni PC di sala, la riunione e i microfoni. Cambia scena, ammetti e posiziona i relatori da remoto, instrada l\'audio e lascia che le regole facciano ciò che un operatore farebbe comunque. Parla con ogni strumento tramite un connettore, così il mixer, il trasporto video e la piattaforma di riunione sono una scelta, non un vincolo.',
    },
    'Rules': {'de': 'Regeln', 'es': 'Reglas', 'it': 'Regole'},

    # Meet
    'The meeting, as separate feeds.': {'de': 'Das Meeting, als einzelne Signale.', 'es': 'La reunión, en señales separadas.', 'it': 'La riunione, in flussi separati.'},
    'Joins the online meeting and gives each participant, the gallery and screen shares their own video feed, with the audio, for the hall to use like any other source. Director controls who goes where. Zoom today; the meeting platform is a connector.': {
        'de': 'Nimmt am Online-Meeting teil und gibt jedem Teilnehmer, der Galerie und den Bildschirmfreigaben ein eigenes Videosignal mit Ton, das der Saal wie jede andere Quelle nutzt. Director steuert, wer wohin geht. Heute Zoom; die Meeting-Plattform ist ein Konnektor.',
        'es': 'Se une a la reunión en línea y da a cada participante, a la galería y a las pantallas compartidas su propia señal de vídeo, con el audio, para que la sala la use como cualquier otra fuente. Director controla quién va a dónde. Hoy Zoom; la plataforma de reuniones es un conector.',
        'it': 'Entra nella riunione online e dà a ogni partecipante, alla galleria e alle condivisioni schermo un proprio flusso video, con l\'audio, che la sala usa come qualsiasi altra sorgente. Director controlla chi va dove. Oggi Zoom; la piattaforma di riunione è un connettore.',
    },
    'Isolated feeds': {'de': 'Einzelne Signale', 'es': 'Señales aisladas', 'it': 'Flussi separati'},
    'Remote control': {'de': 'Fernsteuerung', 'es': 'Control remoto', 'it': 'Controllo remoto'},

    # Mic
    'Phones as microphones.': {'de': 'Telefone als Mikrofone.', 'es': 'Teléfonos como micrófonos.', 'it': 'Telefoni come microfoni.'},
    "Speakers and the control room use their phones as wireless mics and talkback. The PC side receives them as audio devices, next to the hall's own mics.": {
        'de': 'Sprecher und Regie nutzen ihre Telefone als Funkmikrofone und Intercom. Der PC empfängt sie als Audiogeräte, neben den eigenen Mikrofonen des Saals.',
        'es': 'Los ponentes y la sala de control usan sus teléfonos como micrófonos inalámbricos e intercomunicador. El PC los recibe como dispositivos de audio, junto a los micrófonos propios de la sala.',
        'it': 'I relatori e la regia usano i telefoni come radiomicrofoni e intercom. Il PC li riceve come dispositivi audio, accanto ai microfoni della sala.',
    },

    # Translator
    'Live translation, as an audio source.': {'de': 'Live-Übersetzung, als Audioquelle.', 'es': 'Traducción en directo, como fuente de audio.', 'it': 'Traduzione simultanea, come sorgente audio.'},
    'Takes a microphone, a hall mic or a phone through Mic, and gives back the speech translated into another language on any audio output, for the hall, the meeting or a headset. Director starts and stops it like any other device. Google Gemini or OpenAI today; the translation service is a connector.': {
        'de': 'Nimmt ein Mikrofon, ein Saalmikrofon oder ein Telefon über Mic und gibt die Sprache in eine andere Sprache übersetzt auf einem beliebigen Audioausgang zurück, für den Saal, das Meeting oder einen Kopfhörer. Director startet und stoppt es wie jedes andere Gerät. Heute Google Gemini oder OpenAI; der Übersetzungsdienst ist ein Konnektor.',
        'es': 'Toma un micrófono, un micrófono de sala o un teléfono a través de Mic y devuelve la voz traducida a otro idioma en cualquier salida de audio, para la sala, la reunión o unos auriculares. Director lo inicia y lo detiene como cualquier otro dispositivo. Hoy Google Gemini u OpenAI; el servicio de traducción es un conector.',
        'it': 'Prende un microfono, un microfono di sala o un telefono tramite Mic e restituisce il parlato tradotto in un\'altra lingua su qualsiasi uscita audio, per la sala, la riunione o una cuffia. Director lo avvia e lo ferma come qualsiasi altro dispositivo. Oggi Google Gemini o OpenAI; il servizio di traduzione è un connettore.',
    },
    'Live speech': {'de': 'Sprache in Echtzeit', 'es': 'Voz en directo', 'it': 'Parlato dal vivo'},
    'Web control': {'de': 'Steuerung im Browser', 'es': 'Control web', 'it': 'Controllo web'},

    # Pass
    'Badges, doors and attendance.': {'de': 'Badges, Einlass und Anwesenheit.', 'es': 'Acreditaciones, accesos y asistencia.', 'it': 'Badge, ingressi e presenze.'},
    'Every badge carries a QR code. At each door a phone, a tablet or any keyboard scanner reads it, and the door answers at once in green, amber or red with a sound, even when the network drops: scans wait offline and are sent when it is back. Afterwards Pass tells who was in which session, when and for how long, ready to export. The organiser sets the categories and the rules for each event, tries them in a tester, imports attendees from a spreadsheet or a registration site and prints the badges.': {
        'de': 'Jedes Badge trägt einen QR-Code. An jedem Eingang liest ihn ein Telefon, ein Tablet oder ein beliebiger Tastatur-Scanner, und der Eingang antwortet sofort in Grün, Gelb oder Rot mit einem Ton, auch wenn das Netz ausfällt: Scans warten offline und werden gesendet, sobald es wieder da ist. Danach zeigt Pass, wer in welcher Sitzung war, wann und wie lange, fertig zum Export. Der Veranstalter legt Kategorien und Regeln für jede Veranstaltung fest, probiert sie in einem Tester aus, importiert Teilnehmer aus einer Tabelle oder einer Anmeldeseite und druckt die Badges.',
        'es': 'Cada acreditación lleva un código QR. En cada puerta lo lee un teléfono, una tableta o cualquier lector de teclado, y la puerta responde al instante en verde, ámbar o rojo con un sonido, incluso cuando cae la red: las lecturas esperan sin conexión y se envían cuando vuelve. Después, Pass indica quién estuvo en qué sesión, cuándo y durante cuánto tiempo, listo para exportar. El organizador define las categorías y las reglas de cada evento, las prueba en un simulador, importa asistentes desde una hoja de cálculo o un sitio de inscripción e imprime las acreditaciones.',
        'it': 'Ogni badge porta un codice QR. A ogni ingresso lo legge un telefono, un tablet o qualsiasi lettore a tastiera, e l\'ingresso risponde subito in verde, giallo o rosso con un suono, anche quando cade la rete: le letture aspettano offline e partono quando torna. Poi Pass dice chi era in quale sessione, quando e per quanto tempo, pronto da esportare. L\'organizzatore definisce le categorie e le regole di ogni evento, le prova in un tester, importa i partecipanti da un foglio di calcolo o da un sito di iscrizione e stampa i badge.',
    },
    'Web scan app': {'de': 'Scan-App im Browser', 'es': 'App web de lectura', 'it': 'App web di lettura'},
    'Any scanner': {'de': 'Jeder Scanner', 'es': 'Cualquier lector', 'it': 'Qualsiasi lettore'},
    'Badge print': {'de': 'Badge-Druck', 'es': 'Impresión de acreditaciones', 'it': 'Stampa badge'},
    'Live occupancy': {'de': 'Belegung in Echtzeit', 'es': 'Ocupación en tiempo real', 'it': 'Occupazione in tempo reale'},
    'Reports': {'de': 'Berichte', 'es': 'Informes', 'it': 'Report'},

    # Connectors
    'Director coordinates, the connectors do the talking. These ship today; new ones are written against one small interface, so more can follow, and a place to share them is the plan.': {
        'de': 'Director koordiniert, die Konnektoren sprechen mit den Geräten. Diese gibt es heute; neue werden gegen eine kleine Schnittstelle geschrieben, sodass weitere folgen können, und ein Ort, um sie zu teilen, ist geplant.',
        'es': 'Director coordina, los conectores hablan con los equipos. Estos existen hoy; los nuevos se escriben contra una interfaz pequeña, así que pueden llegar más, y está previsto un lugar para compartirlos.',
        'it': 'Director coordina, i connettori parlano con gli apparati. Questi ci sono già oggi; i nuovi si scrivono su un\'interfaccia piccola, quindi altri possono seguire, ed è previsto un posto dove condividerli.',
    },
    'scenes, sources, outputs and audio on every hall PC': {'de': 'Szenen, Quellen, Ausgänge und Ton auf jedem Saal-PC', 'es': 'escenas, fuentes, salidas y audio en cada PC de sala', 'it': 'scene, sorgenti, uscite e audio su ogni PC di sala'},
    'video and audio between PCs, with a multiview to watch it all': {'de': 'Video und Ton zwischen PCs, mit einem Multiview für den Überblick', 'es': 'vídeo y audio entre PC, con un multiview para verlo todo', 'it': 'video e audio tra i PC, con un multiview per vedere tutto'},
    'the online meeting as isolated feeds, and who is in it': {'de': 'das Online-Meeting als einzelne Signale, und wer darin ist', 'es': 'la reunión en línea en señales aisladas, y quién está en ella', 'it': 'la riunione online in flussi separati, e chi c\'è dentro'},
    'phones as mics and talkback': {'de': 'Telefone als Mikrofone und Intercom', 'es': 'teléfonos como micrófonos e intercomunicador', 'it': 'telefoni come microfoni e intercom'},
    'live translation of a speaker into another language': {'de': 'Live-Übersetzung eines Sprechers in eine andere Sprache', 'es': 'traducción en directo de un ponente a otro idioma', 'it': 'traduzione simultanea di un relatore in un\'altra lingua'},
    "the hall's wireless mics: levels, battery, who is on": {'de': 'die Funkmikrofone des Saals: Pegel, Akku, wer aktiv ist', 'es': 'los micrófonos inalámbricos de la sala: niveles, batería, quién está activo', 'it': 'i radiomicrofoni della sala: livelli, batteria, chi è attivo'},
    "the hall's networked audio, through Dante Virtual Soundcard on the mic hub": {'de': 'das Audionetzwerk des Saals, über Dante Virtual Soundcard auf dem Mikrofon-Hub', 'es': 'el audio en red de la sala, mediante Dante Virtual Soundcard en el concentrador de micrófonos', 'it': 'l\'audio in rete della sala, tramite Dante Virtual Soundcard sull\'hub dei microfoni'},
    'control surfaces and faders': {'de': 'Bedienpulte und Fader', 'es': 'superficies de control y faders', 'it': 'superfici di controllo e fader'},
    'Folders': {'de': 'Ordner', 'es': 'Carpetas', 'it': 'Cartelle'},
    'clips and files that appear during the show': {'de': 'Clips und Dateien, die während der Show auftauchen', 'es': 'clips y archivos que aparecen durante el show', 'it': 'clip e file che compaiono durante lo show'},
    'Your own': {'de': 'Ihr eigener', 'es': 'El tuyo', 'it': 'Il tuo'},
    'any protocol you describe, HTTP, OSC or raw sockets': {'de': 'jedes Protokoll, das Sie beschreiben: HTTP, OSC oder direkte Sockets', 'es': 'cualquier protocolo que describas: HTTP, OSC o sockets directos', 'it': 'qualsiasi protocollo tu descriva: HTTP, OSC o socket diretti'},

    # In production
    'A medical congress, eighteen halls, one control room': {'de': 'Ein Medizinkongress, achtzehn Säle, eine Regie', 'es': 'Un congreso médico, dieciocho salas, una sola sala de control', 'it': 'Un congresso medico, diciotto sale, un\'unica regia'},
    "Each hall has a PC with OBS and a camera, and its own meeting that connects the auditorium with the operating room, the faculty's hospitals and the remote speakers. Everyone in the meeting appears in the hall as a separate feed, and the hall's program goes back to them. Hall mics and phone mics reach whichever PC needs them. One operator watches all eighteen, and the rules handle admitting people, hand-overs between speakers and the audio routing that would otherwise be done by hand, many times a day.": {
        'de': 'Jeder Saal hat einen PC mit OBS und einer Kamera und ein eigenes Meeting, das das Auditorium mit dem Operationssaal, den Kliniken der Referenten und den zugeschalteten Sprechern verbindet. Jeder im Meeting erscheint im Saal als eigenes Signal, und das Programm des Saals geht zu ihnen zurück. Saalmikrofone und Telefon-Mikrofone erreichen den PC, der sie braucht. Ein Operator überblickt alle achtzehn, und die Regeln übernehmen das Einlassen, die Übergaben zwischen Sprechern und das Audio-Routing, das sonst viele Male am Tag von Hand erledigt würde.',
        'es': 'Cada sala tiene un PC con OBS y una cámara, y su propia reunión que conecta el auditorio con el quirófano, los hospitales de los ponentes y los ponentes remotos. Cada persona de la reunión aparece en la sala como una señal separada, y el programa de la sala vuelve a ellas. Los micrófonos de sala y los de teléfono llegan al PC que los necesita. Un solo operador vigila las dieciocho, y las reglas se encargan de admitir a las personas, de los relevos entre ponentes y del encaminamiento de audio que de otro modo se haría a mano muchas veces al día.',
        'it': 'Ogni sala ha un PC con OBS e una telecamera, e una propria riunione che collega l\'auditorium con la sala operatoria, gli ospedali della faculty e i relatori da remoto. Chiunque sia nella riunione compare in sala come flusso separato, e il programma della sala torna a loro. I microfoni di sala e quelli dei telefoni arrivano al PC che ne ha bisogno. Un solo operatore le segue tutte e diciotto, e le regole gestiscono le ammissioni, i passaggi tra relatori e l\'instradamento audio che altrimenti si farebbe a mano, molte volte al giorno.',
    },
    'halls, each a station': {'de': 'Säle, jeder eine Station', 'es': 'salas, cada una un puesto', 'it': 'sale, ognuna una postazione'},
    'meetings, one per hall': {'de': 'Meetings, eines pro Saal', 'es': 'reuniones, una por sala', 'it': 'riunioni, una per sala'},
    'connectors in use': {'de': 'Konnektoren im Einsatz', 'es': 'conectores en uso', 'it': 'connettori in uso'},
    'operator': {'de': 'Operator', 'es': 'operador', 'it': 'operatore'},

    # Footer
    'Zoom is a trademark of Zoom Communications, Inc. NDI is a registered trademark of Vizrt NDI AB. OBS Studio is a project of the OBS Project.': {
        'de': 'Zoom ist eine Marke von Zoom Communications, Inc. NDI ist eine eingetragene Marke der Vizrt NDI AB. OBS Studio ist ein Projekt des OBS Project.',
        'es': 'Zoom es una marca de Zoom Communications, Inc. NDI es una marca registrada de Vizrt NDI AB. OBS Studio es un proyecto de OBS Project.',
        'it': 'Zoom è un marchio di Zoom Communications, Inc. NDI è un marchio registrato di Vizrt NDI AB. OBS Studio è un progetto di OBS Project.',
    },
}
