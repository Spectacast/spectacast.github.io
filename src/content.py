"""Texts and numbers shared by the pages of spectacast.com: seller details, plans, prices, VAT, and the
labels of the header and footer in every language. The page texts themselves are in pages/ and home.html."""
from decimal import Decimal

# Known values. A value wrapped in [] is a placeholder still to confirm: shown highlighted.
VALUES = {
    'en': {
        'SELLER': 'Spectacast',
        'SELLER_DETAILS': '[registered address, VAT number, company register number]',
        'ADDRESS': '[registered address]',
        'COURT': '[city]',
        'EMAIL': 'support@spectacast.com', 'PRIVACY_EMAIL': 'privacy@spectacast.com',
        'EMAIL_PROVIDER': '[email provider]',
        'REFUND_DAYS': '14',
        'INCLUDED_MINUTES': '300',
        'MINUTE_PRICE': '€ 0.10',
        'MIC_PRIVACY_URL': '<a href="https://regiamic.com/privacy/">regiamic.com/privacy</a>',
    },
    'de': {
        'SELLER': 'Spectacast',
        'SELLER_DETAILS': '[Anschrift, Umsatzsteuer-ID, Handelsregisternummer]',
        'ADDRESS': '[Anschrift]',
        'COURT': '[Ort]',
        'EMAIL': 'support@spectacast.com', 'PRIVACY_EMAIL': 'privacy@spectacast.com',
        'EMAIL_PROVIDER': '[E-Mail-Anbieter]',
        'REFUND_DAYS': '14',
        'INCLUDED_MINUTES': '300',
        'MINUTE_PRICE': '0,10 €',
        'MIC_PRIVACY_URL': '<a href="https://regiamic.com/privacy/">regiamic.com/privacy</a>',
    },
    'es': {
        'SELLER': 'Spectacast',
        'SELLER_DETAILS': '[domicilio social, NIF-IVA, número de registro mercantil]',
        'ADDRESS': '[domicilio social]',
        'COURT': '[ciudad]',
        'EMAIL': 'support@spectacast.com', 'PRIVACY_EMAIL': 'privacy@spectacast.com',
        'EMAIL_PROVIDER': '[proveedor de correo]',
        'REFUND_DAYS': '14',
        'INCLUDED_MINUTES': '300',
        'MINUTE_PRICE': '0,10 €',
        'MIC_PRIVACY_URL': '<a href="https://regiamic.com/privacy/">regiamic.com/privacy</a>',
    },
    'it': {
        'SELLER': 'Spectacast',
        'SELLER_DETAILS': '[sede legale, partita IVA, numero REA]',
        'ADDRESS': '[sede legale]',
        'COURT': '[città]',
        'EMAIL': 'support@spectacast.com', 'PRIVACY_EMAIL': 'privacy@spectacast.com',
        'EMAIL_PROVIDER': '[fornitore email]',
        'REFUND_DAYS': '14',
        'INCLUDED_MINUTES': '300',
        'MINUTE_PRICE': '€ 0,10',
        'MIC_PRIVACY_URL': '<a href="https://regiamic.com/privacy/">regiamic.com/privacy</a>',
    },
}

PLANS = {
    'en': {
        'year': 'Yearly', 'event': 'Event pass', 'per_year': 'per hall / year', 'per_event': 'per hall / event, up to 7 days',
        'from': 'Billing', 'plans': [
            ('Pass', 'Badges, doors and attendance.', 'Spectacast Pass',
             ['Badges with QR codes, printed or emailed', 'Door scanning on any phone, tablet or scanner, also offline',
              'Live occupancy per room', 'Attendance reports and certificates', 'Import from a spreadsheet or a registration site']),
            ('Director', 'The control room, on its own.', 'Spectacast Director',
             ['One dashboard for every hall, with rules', 'Connectors for OBS, NDI, Dante, Sennheiser EW-DX, MIDI',
              'Your own connectors over HTTP, OSC or sockets', 'Multiview of every hall', 'Add Meet and Mic later by moving to Show']),
            ('Show', 'The control room for hybrid halls.', 'Spectacast Director, Meet and Mic',
             ['Director: one dashboard for every hall, with rules', 'Meet: each meeting participant as its own feed',
              'Mic: phones as wireless mics and talkback', 'Connectors for OBS, NDI, Dante, Sennheiser EW-DX, MIDI', 'Works offline in the hall']),
            ('Complete', 'Everything, with live translation.', 'All five modules',
             ['Everything in Show', 'Everything in Pass', 'Translator: live speech translation into other languages',
              '300 translation minutes per hall included', 'Extra minutes billed by use']),
        ]},
    'de': {
        'year': 'Jährlich', 'event': 'Event-Pass', 'per_year': 'pro Saal / Jahr', 'per_event': 'pro Saal / Event, bis zu 7 Tage',
        'from': 'Abrechnung', 'plans': [
            ('Pass', 'Badges, Einlass und Anwesenheit.', 'Spectacast Pass',
             ['Badges mit QR-Code, gedruckt oder per E-Mail', 'Scannen am Eingang mit Telefon, Tablet oder Scanner, auch offline',
              'Belegung der Räume in Echtzeit', 'Anwesenheitsberichte und Teilnahmebescheinigungen', 'Import aus einer Tabelle oder einer Anmeldeseite']),
            ('Director', 'Die Regie, einzeln.', 'Spectacast Director',
             ['Ein Dashboard für alle Säle, mit Regeln', 'Konnektoren für OBS, NDI, Dante, Sennheiser EW-DX, MIDI',
              'Eigene Konnektoren über HTTP, OSC oder Sockets', 'Multiview aller Säle', 'Meet und Mic später durch Wechsel zu Show hinzufügen']),
            ('Show', 'Die Regie für hybride Säle.', 'Spectacast Director, Meet und Mic',
             ['Director: ein Dashboard für alle Säle, mit Regeln', 'Meet: jeder Meeting-Teilnehmer als eigenes Signal',
              'Mic: Telefone als Funkmikrofone und Intercom', 'Konnektoren für OBS, NDI, Dante, Sennheiser EW-DX, MIDI', 'Funktioniert offline im Saal']),
            ('Complete', 'Alles, mit Live-Übersetzung.', 'Alle fünf Module',
             ['Alles aus Show', 'Alles aus Pass', 'Translator: Live-Übersetzung von Sprache in andere Sprachen',
              '300 Übersetzungsminuten pro Saal enthalten', 'Zusätzliche Minuten nach Verbrauch']),
        ]},
    'es': {
        'year': 'Anual', 'event': 'Pase de evento', 'per_year': 'por sala / año', 'per_event': 'por sala / evento, hasta 7 días',
        'from': 'Facturación', 'plans': [
            ('Pass', 'Acreditaciones, accesos y asistencia.', 'Spectacast Pass',
             ['Acreditaciones con código QR, impresas o por correo electrónico', 'Lectura en las puertas con teléfono, tableta o lector, también sin conexión',
              'Ocupación de las salas en tiempo real', 'Informes de asistencia y certificados', 'Importación desde una hoja de cálculo o un sitio de inscripción']),
            ('Director', 'La sala de control, por separado.', 'Spectacast Director',
             ['Un panel para todas las salas, con reglas', 'Conectores para OBS, NDI, Dante, Sennheiser EW-DX, MIDI',
              'Tus propios conectores por HTTP, OSC o sockets', 'Multiview de todas las salas', 'Añade Meet y Mic más adelante pasando a Show']),
            ('Show', 'La sala de control para salas híbridas.', 'Spectacast Director, Meet y Mic',
             ['Director: un panel para todas las salas, con reglas', 'Meet: cada participante de la reunión como señal separada',
              'Mic: teléfonos como micrófonos inalámbricos e intercomunicador', 'Conectores para OBS, NDI, Dante, Sennheiser EW-DX, MIDI', 'Funciona sin conexión en la sala']),
            ('Complete', 'Todo, con traducción en directo.', 'Los cinco módulos',
             ['Todo lo de Show', 'Todo lo de Pass', 'Translator: traducción de voz en directo a otros idiomas',
              '300 minutos de traducción por sala incluidos', 'Minutos adicionales según el uso']),
        ]},
    'it': {
        'year': 'Annuale', 'event': 'Pass evento', 'per_year': 'per sala / anno', 'per_event': 'per sala / evento, fino a 7 giorni',
        'from': 'Fatturazione', 'plans': [
            ('Pass', 'Badge, ingressi e presenze.', 'Spectacast Pass',
             ['Badge con codice QR, stampati o inviati via email', 'Lettura agli ingressi con telefono, tablet o lettore, anche offline',
              'Occupazione delle sale in tempo reale', 'Report di presenza e attestati', 'Import da foglio di calcolo o sito di iscrizione']),
            ('Director', 'La regia, da sola.', 'Spectacast Director',
             ['Una dashboard per tutte le sale, con regole', 'Connettori per OBS, NDI, Dante, Sennheiser EW-DX, MIDI',
              'I tuoi connettori via HTTP, OSC o socket', 'Multiview di tutte le sale', 'Aggiungi Meet e Mic in seguito passando a Show']),
            ('Show', 'La regia per sale ibride.', 'Spectacast Director, Meet e Mic',
             ['Director: una dashboard per tutte le sale, con regole', 'Meet: ogni partecipante alla riunione come flusso separato',
              'Mic: telefoni come radiomicrofoni e intercom', 'Connettori per OBS, NDI, Dante, Sennheiser EW-DX, MIDI', 'Funziona offline in sala']),
            ('Complete', 'Tutto, con la traduzione simultanea.', 'Tutti e cinque i moduli',
             ['Tutto di Show', 'Tutto di Pass', 'Translator: traduzione simultanea del parlato in altre lingue',
              '300 minuti di traduzione per sala inclusi', 'Minuti in più a consumo']),
        ]},
}
# Prices before VAT, in euros: (yearly, event pass). Private buyers pay VAT on top, so every price is also shown
# with the VAT of one example country per language (decided 18 Nov 2026: individuals can buy as well as businesses).
PRICES = {'Pass': (490, 90), 'Director': (590, 150), 'Show': (1200, 290), 'Complete': (1800, 390)}
MINUTE = Decimal('0.10')
VAT = {'en': 19, 'de': 19, 'es': 21, 'it': 22}  # Germany, Germany, Spain, Italy
VAT_WHERE = {'en': '19% VAT in Germany', 'de': '19\u00a0% Mehrwertsteuer in Deutschland',
             'es': 'el 21\u00a0% de IVA de España', 'it': "l'IVA italiana al 22%"}
NET = {'en': ', before VAT', 'de': ', ohne MwSt.', 'es': ', sin IVA', 'it': ', IVA esclusa'}
VAT_LINE = {'en': '<strong>{}</strong> with 19% VAT in Germany',
            'de': '<strong>{}</strong> mit 19\u00a0% MwSt. in Deutschland',
            'es': '<strong>{}</strong> con el 21\u00a0% de IVA de España',
            'it': "<strong>{}</strong> con l'IVA italiana al 22%"}


