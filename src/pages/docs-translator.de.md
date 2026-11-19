# Translator-Anleitung

<p class="lede">Translator hört einer sprechenden Person zu und sagt live in einer anderen Sprache, was sie sagt, auf jedem Audioausgang. Ein Translator, Spur genannt, pro Sprache.</p>

## Was Sie brauchen

- Einen Windows-PC im Saal oder in der Regie, mit Spectacast Setup installiert und in Ihrem Konto aktiviert.
- Einen Plan mit Translator: Seine Minuten kommen mit der Lizenz des PCs, ohne etwas einzurichten. Oder Ihren eigenen Schlüssel für Google Gemini oder OpenAI.
- Einen Eingang mit der Stimme der sprechenden Person: ein Mikrofon, der Mischer, ein Telefon über [Mic](/de/hilfe/mic/) oder ein Signal über NDI.

## Die Bedienseite

Jede Spur hat ihre eigene Bedienseite, unter **http://127.0.0.1:4720** für die erste Spur auf diesem PC. Wählen Sie:

1. das **Mikrofon**, also den Eingang: eine Soundkarte oder eine NDI-Quelle, etwa eine teilnehmende Person aus [Meet](/de/hilfe/meet/);
2. den **Ausgang**: eine Soundkarte, ein virtuelles Kabel in OBS oder den Mischer, oder den Dolmetschkanal von Meet;
3. die **Zielsprache**, in der gesprochen wird;

und drücken Sie **Starten**. Die Seite zeigt jeden Satz zweimal, wie gehört und wie gesagt, während er gesprochen wird.

{{shot:translator|Die Bedienseite von Translator: was auf Italienisch gehört und was auf Englisch gesagt wurde, Zeile für Zeile}}

## Engines

Die Engine bestimmt, wie Translator klingt und wie schnell er antwortet. Google Gemini ist voreingestellt; OpenAI ist die andere. Die **Dolmetsch**-Engines arbeiten wie eine Konferenzdolmetscherin: Geben Sie ihnen auf der Bedienseite das **Thema** der Sitzung; außerdem verwenden sie ein Glossar mit Namen und Fachbegriffen auf dem PC, einer pro Zeile. Das Glossar richten wir mit Ihnen ein.

## Sinnumkehr erkennen

Während eine Spur läuft, liest ein zweites Modell das Gehörte neben dem Gesagten und markiert rot die Stellen, an denen die Übersetzung etwas anderes sagt: ein verlorenes „nicht“, eine Zahl, links statt rechts, ein Name. Es ändert nichts an dem, was die Spur sagt; es ist für die Person, die die Spur beobachtet. Das Kästchen **Warnen, wenn sich der Sinn umkehrt** schaltet es aus.

## Im Meeting

Um Zuhörenden im Online-Meeting eine Sprache zu geben, stellen Sie den Ausgang der Spur auf den Dolmetschkanal von Meet. Meet tritt als Dolmetscher dieser Sprache bei, und die Zuhörenden wählen die Sprache in Zoom. Siehe [Meet](/de/hilfe/meet/).

## Nach einem Neustart

Eine Spur merkt sich, was sie getan hat. Nach einem Neustart des PCs kommt sie mit demselben Eingang, Ausgang und derselben Sprache zurück und startet wieder, wenn sie lief; zehn Minuten lang versucht sie es erneut, solange eine Soundkarte oder das Netzwerk noch fehlt.

## Minuten

Jede Minute, die eine Spur spricht, zählt, pro Sprache. Pläne mit Translator enthalten {{INCLUDED_MINUTES}} Minuten pro Saal; Ihr Konto zeigt, wie viele Sie verbraucht haben. Siehe [Konto und Abrechnung](/de/hilfe/konto-und-abrechnung/).
