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
    'EN · DE · ES · IT', '© 2026 Spectacast · spectacast.com',
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
