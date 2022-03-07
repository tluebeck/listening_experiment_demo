#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Listening Experiment Py: SAQI - A Spatial Audio Inventory

        (C) 2021 by Tim Lübeck
                TH Köln - University of Applied Sciences
                Institute of Communications Engineering
                Department of Acoustics and Audio Signal Processing
"""

from enum import Enum

class Vocabulary(Enum):
    timbre = 1
    tonalness = 2
    geometry = 3
    room = 4
    time_behaviour = 5
    dynamics = 6
    artifacts = 7
    general = 8
    
class Item(Enum):
    difference = 0
    toneColorBrightDark = 1
    highFrequencyToneColor = 2
    midFrequencyToneColor = 3
    lowFrequencyToneColor = 4
    sharpness = 5
    roughness = 6
    combFilterColoration = 7
    metallicToneColor = 8
    tonalness = 9
    pitch = 10
    dopplerEffect = 11
    horizontalDirection = 12
    verticalDirection = 13
    frontBackPosition = 14
    distance = 15
    depth = 16
    width = 17
    height = 18
    externalization = 19
    localizability = 20
    spatialDisintegration = 21
    levelOfReverberation = 22
    durationOfReverberation = 23
    envelopment = 24
    preEchoes = 25
    postEchoes = 26
    temporalDisintegration = 27
    crispness = 28
    speed = 29
    sequenceOfEvents = 30
    responsiveness = 31
    loudness = 32
    dynamicRange = 33
    dynamicCompressionEffects = 34
    pitchedArtifact = 35
    impulsiveArtifact = 36
    noiseLikeArtifact = 37
    alienSource = 38
    ghostSource = 39
    distortion = 40
    tactileVibration = 41
    clarity = 42
    speechIntelligibility = 43
    naturalness = 44
    presence = 45
    degreeOfLiking = 46
    other = 47
    # custom attributes
    coloration = 48
    sourcePosition = 49
    sourceWidth = 50
    
attribute_names_en = [
    'difference',
    'tone color bright-dark',
    'high-frequency tone color',
    'mid-frequency tone color',
    'low-frequency tone color',
    'sharpness',
    'roughness',
    'comb filter coloration',
    'metallic tone color',
    'tonalness',
    'pitch',
    'doppler effect',
    'horizontal direction',
    'vertical direction',
    'front-back position',
    'distance',
    'depth',
    'width',
    'height',
    'externalization',
    'localizability',
    'spatial disintegration',
    'level of reverberation',
    'duration of reverberation',
    'envelopment (by reverberation)',
    'pre-echoes',
    'post-echoes',
    'temporal disintegration',
    'crispness',
    'speed',
    'sequence of events',
    'responsiveness',
    'loudness',
    'dynamic range',
    'dynamic compression effects',
    'pitched artifact',
    'impulsive artifact',
    'noise-like artifact',
    'alien source',
    'ghost source',
    'distortion',
    'tactile vibration',
    'clarity',
    'speech intelligibility',
    'naturalness',
    'presence',
    'degree-of-liking',
    'other',
    # custom attributes
    'coloration',
    'source position',
    'source extension'
]

attribute_names_ger = [
    'Unterschied',
    'Klangfarbe hell-dunkel',
    'Klangfarbliche Ausprägung im Höhenbereich',
    'Klangfarbliche Ausprägung im Mittenbereich',
    'Klangfarbliche Ausprägung im Tiefenbereich',
    'Schärfe',
    'Rauigkeit',
    'Kammfilterartigkeit',
    'Metallische Klangfarbe',
    'Tonhaltigkeit',
    'Tonhöhe',
    'Dopplereffekt',
    'Richtung Azimut',
    'Richtung Elevation',
    'Vorn-Hinten-Lage',
    'Entfernung',
    'Tiefenausdehnung',
    'Breitenausdehnung',
    'Höhenausdehnung',
    'Externalisierungsgrad',
    'Lokalisierbarkeit',
    'Räumliches Zerfallen',
    'Nachhallstärke',
    'Nachhalldauer',
    'Nachhallumhüllung',
    'Vorechos',
    'Nachechos',
    'Zeitliches Zerfallen',
    'Knackigkeit',
    'Wiedergabegeschwindigkeit',
    'Szenenablauf',
    'Reaktionsschnelligkeit',
    'Lautheit',
    'Dynamik',
    'Kompressoreffekte',
    'Tonhaltiges Fremdgeräusch',
    'Impulshaftes Fremdgeräusch',
    'Rauschhaftes Fremdgeräusch',
    'Fremdquelle',
    'Geisterquelle',
    'Verzerrungen',
    'Vibration',
    'Klarheit',
    'Sprachverständlichkeit',
    'Natürlichkeit',
    'Präsenz',
    'Gefallen',
    'Sonstiges',
    # custom attributes
    'Klangverfärbung',
    'Schallquellenposition',
    'Quellausdehnung'
]
labels_en = [
    ['none', 'very large'],
    ['darker', 'brighter'],
    ['attenuated', 'emphasized'],
    ['attenuated', 'emphasized'],
    ['attenuated', 'emphasized'],
    ['less sharp', 'sharper'],
    ['less rough', 'more rough'],
    ['less pronounced', 'more pronounced'],
    ['less pronounced', 'more pronounced'],
    ['less tonal', 'more tonal'],
    ['lower', 'higher'],
    ['less pronounced', 'more pronounced'],
    ['shifted anticlockwise', 'shifted clockwise'],
    ['shifted down', 'shifted up'],
    ['not confused', 'confused'],
    ['closer', 'more distant'],
    ['less deep', 'deeper'],
    ['less wide', 'wider'],
    ['less high', 'higher'],
    ['more internalized', 'more externalized'],
    ['more difficult', 'easier'],
    ['more coherent', 'more disjointed'],
    ['less', 'more'],
    ['shorter', 'longer'],
    ['less pronounced', 'more pronounced'],
    ['less intense', 'more intense'],
    ['less intense', 'more intense'],
    ['more coherent', 'more disjointed'],
    ['less pronounced', 'more pronounced'],
    ['reduced', 'increased'],
    ['unchanged', 'changed'],
    ['lower', 'higher'],
    ['quieter', 'louder'],
    ['smaller', 'larger'],
    ['less pronounced', 'more pronounced'],
    ['less intense', 'more intense'],
    ['less intense', 'more intense'],
    ['less intense', 'more intense'],
    ['less intense', 'more intense'],
    ['less intense', 'more intense'],
    ['less intense', 'more intense'],
    ['less intense', 'more intense'],
    ['less pronounced', 'more pronounced'],
    ['lower', 'higher'],
    ['lower', 'higher'],
    ['lower', 'higher'],
    ['lower', 'higher'],
    ['less pronounced', 'more pronounced'],
    # custom attributes
    ['none', 'very large'],  # coloration
    ['unchanchged', 'changed'],  # source position
    ['wider', 'less wide']  #  source extension
]

labels_ger = [
    ['gar keiner', 'sehr großer'],
    ['dunkler', 'heller'],
    ['Höhen abgesenkt', 'Höhen angehoben'],
    ['Mitten abgesenkt', 'Mitten angehoben'],
    ['Tiefen abgesenkt', 'Tiefen angehoben'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['weniger tonal', 'tonaler'],
    ['tiefer', 'höher'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['entgegen dem Uhrzeigersinn versetzt', 'im Uhrzeigersinn versetzt'],
    ['nach unten versetzt', 'nach oben versetzt'],
    ['nicht vertauscht', 'vertauscht'],
    ['näher', 'ferner'],
    ['kürzer', 'tiefer'],
    ['schmaler', 'breiter'],
    ['niedriger', 'höher'],
    ['internalisierter', 'externalisierter'],
    ['unpräziser', 'präziser'],
    ['fusionierter', 'zerfallener'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['kürzer', 'länger'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['fusionierter' 'zerfallener'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['verlangsamt' 'beschleunigt'],
    ['unverändert', 'stark verändert'],
    ['geringer', 'höher'],
    ['leiser', 'lauter'],
    ['geringer', 'höher'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['schwächer ausgeprägt', 'stärker ausgeprägt'],
    ['geringer', 'höher'],
    ['unnatürlicher', 'natürlicher'],
    ['geringer', 'höher'],
    ['gefällt weniger', 'gefällt mehr'],
    ['schwächer ausgerpägt', 'stärker ausgeprägt'],
    # custom attributes
    ['gar keine', 'sehr große'],  # Klangverfärbung
    ['unverändert', 'verändert'],  # quellposition
    ['breiter', 'weniger breit']  #  quellausdehnung

]
circumscriptions_en = [
    'Existence of a noticeable difference.',  #0
    'Timbral impression which is determined by the ratio of high to low frequency components.', #1
    'Timbral change in a limited frequency range.',
    'Timbral change in a limited frequency range.',
    'Timbral change in a limited frequency range.',
    'Timbral impression which e.g., is indicative for the force with which a sound source is excited. Example:' 
      '- Hard/soft beating of percussion instruments.'
      '- Hard/soft plucking of string instruments (classic guitar, harp).'
      '- Emphasized high frequencies may promote a "sharp" sound impression.',
    'Timbral impression of fierce or aggressive modulation/vibration, whereas individual oscillations are hardly distinguishable. Often rated as unpleasant.',
    'Often perceived as tonal coloration. "Hollow" sound. Example: Speaking through a tube.',
    'Coloration with pronounced narrow-band resonances, often as a result of low density of natural frequencies. Often heard when exciting metallic objects such as gongs, bells, tin cans. Applicable to room simulations, plate reverb, spring reverb, too.',
    'Perceptibility of a pitch in a sound. Example for tonal sounds: voiced speech, beeps',
    'The perception of pitch allows arranging tonal signals along a scale "higher - lower".',
    'Continuous change of pitch. Often perceived as a "continuous detuning". Example: "Detuned" sound of the siren of a fast-moving ambulance.',
    'Direction of a sound source in the horizontal plane.',
    'Direction of a sound source in the vertical plane.',
    'Refers to the position of a sound source before or behind the listener only. Impression of a position difference of a sound source caused by "reflecting" its position on the frontal plane going through the listener.',
    'Perceived distance of a sound source.',
    'Perceived extent of a sound source in radial direction.',
    'Perceived extent of a sound source in horizontal direction.',
    'Perceived extent of a sound source in vertical direction.',
    'Describes the distinctness with which a sound source is perceived within or outside the head regardless of their distance.'
       'Terminologically often enclosed between the phenomena of in-head localization and out-of-head localization.'
       'Examples:'
       '- Poorly/not externalized = Perceived position of sound sources at diotic sound presentation via headphones.'
       '- Good/strongly externalized = Perceived position of a natural source in reverberant environment and when allowing for movements of the listener.',
    'If localizability is low, spatial extent and location of a sound source are difficult to estimate, or appear diffuse, resp. If localizability is high, a sound source is clearly delimited. Low/high localizability is often associated with high/low perceived extent of a sound source.'
       'Examples: sound sources in highly diffuse sound field are poorly localizable.',
    'Sound sources, which - by experience - should have a united spatial shape, appear spatially separated. Possible cause: Parts of the sound source have been synthesized/simulated using separated algorithms/simulation methods and between those exists an unwanted offset in spatial parameters.'
       'Examples: - Fingering noise and playing tones of an instrument appear at different positions. - Spirant and voiced phonemes of speech are synthesized separately and then reproduced with an unwanted spatial separation.',
    'Perception of a strong reverberant sound field, caused by a high ratio of reflected to direct sound energy.' 
       'Leads to the impression of high diffusivity in case of stationary excitation (in the sense of a low D/R-ratio).'
       'Example: The perceived intensity of reverberation differs significantly between rather small and very large spaces, such as living rooms and churches.',
    'Duration of the reverberant decay. Well audible at the end of signals.',
    'Sensation of being spatially surrounded by the reverberation. With more pronounced envelopment of reverberation, it is increasingly difficult to assign a specific position, a limited extension or a preferred direction to the reverberation.'
       'Impressions of either low or high reverberation envelopment arise with either diotic or dichotic (i.e., uncorrelated) presentation of reverberant audio material.',
    'Copies of a sound with mostly lower loudness prior to the actually intended the starting point of a sound.',
    'Copies of a sound with mostly decreasing loudness after the actually intended the starting point of a sound.'
       'Example: Repetition of one''s own voice through reflection on mountain walls',
    'Sound sources, which - by experience - should have a united temporal shape, appear temporally separated.'
       'Causes similar to "spatial disintegration", however, here: due to timing-offsets in synthesis.' 
       'Example: Fingering noise and playing tones of an instrument appear at different points in time.',
    'Characteristic which is affected by the impulse fidelity of systems. Perception of the reproduction of transients. Transients can either be more soft/more smoothed/less precise, or - as opposed -  be quicker/more precise/ more exact.' 
       'Example for "smoothed" transients: A transmission system that exhibits strong group delay distortions. Counter-example: Result of an equalization aiming at phase linearization.',
    'A scene is identical in content and sound, but evolves faster or slower. Does not have to be accompanied by a change in pitch.' 
       'Examples of technical reasons:'
       '- rotation speed' 
       '- sample rate conversion' 
       '- time stretching' 
       '- changed duration of pauses between signal starting points'
       '- movements proceed at a different speed',
    'Order or occurrence of scene components.' 
       'Example: A dog suddenly barks at the end, instead - and as opposed to the reference - at the beginning.',
    'Characteristic that is affected by latencies in the reproduction system. Distinguishes between more or less delayed reactions of a reproduction system with respect to user interactions.',
    'Perceived loudness of a sound source. Disappearance of a sound source can be stated by a loudness equaling zero.' 
       'Example of a loudness contrast: whispering vs. screaming',
    'Amount of loudness differences between loud and soft passages. In signals with a smaller dynamic range loud and soft passages differ less from the average loudness. Signals with a larger dynamic range contain both very loud and very soft passages.',
    'Sound changes beyond the long-term loudness. Collective category for a variety of percepts caused by dynamic compression.' 
        'Examples:' 
        '- More compact sound of sum-compressed music tracks in comparison to the unedited original.' 
        '- "Compressor pumping": Energy peaks in audio signals (bass drums, speech plosives) lead to a sudden drop in signal loudness which needs a susceptible period of time to recover.',
    'Perception of a clearly unintended sound event. For example, a disturbing tone which is clearly not associated with the presented scene, such as an unexpected beep.',
    'Perception of a clearly unintended sound event. For example, a short disturbing sound which is clearly not associated with the presented scene, such as an unexpected click.',
    'Perception of a clearly unintended sound event. For example, a noise which is clearly not associated with the presented scene, such as a background noise from of a fan.',
    'Perception of a clearly unintended sound event. Examples:' 
        '- An interfering radio signal.'
        '- A wrongly unmuted mixing desk channel.',
    'Spatially separated, nearly simultaneous and not necessarily identical image of a sound source.' 
        'A kind of a spatial copy of a signal: A sound source appears at one or more additional positions in the scene.'
       'Examples:'
       '- Two sound sources which are erroneously playing back the same audio content.'
       '- Double images when down-mixing main and spot microphone recordings.'
       '- Spatial aliasing in wave field synthesis (WFS): Sound sources are perceived as ambivalent in direction.',
    'Percept as a result of non-linear distortions as caused e.g. by clipping. Scratchy or "broken" sound. Often dependent on signal amplitude. Perceptual quality can vary widely depending on the type of distortion.'
       'Example: Clipping of digital input stages.',
    'Perception at the border between auditory and tactile modality. Vibration caused by a sound source can be felt through mechanical coupling to supporting surfaces.'
       'Examples:'
       '- live concert: Bass can be "felt in the stomach".'
       '- Headphone cushions vibrate noticeably on the ear/head.',
    'Clarity/clearness with respect to any characteristic of elements of a sound scene. Impression of how clearly different elements in a scene can be distinguished from each other or how well various properties of individual scene elements can be detected. The term is thus to be understood much broader than the in realm of room acoustics, where clarity is used to predict the impression of declining transparency with increasing reverberation.',
    'Impression of how well the words of a speaker can be understood.'
       '- Typical for low speech intelligibility: train station announcements'
       '- Typical for high speech intelligibility: newscaster',
    'Impression that a signal is in accordance with the expectation/former experience of an equivalent signal.',
    'Perception of "being-in-the-scene", or "spatial presence". Impression of being inside a presented scene or to be spatially integrated into the scene.',
    'Difference with respect to pleasantness/unpleasantness. Evaluation of the perceived overall difference with respect to the degree of enjoyment or displeasure. Note that "preference" might not be used synonymously, as, e.g., there may be situations where something is preferred that is - at the same time - not liked most.',
    'Another, previously unrecognized difference.',
    # custom
    'Timbral change',  # Coloration
    'Change of sound source position',  # Source direction
    'Change of the apparent source width'  #  sourceWidth
]


circumscriptions_ger = [
    'Existenz eines wahrnehmbaren Unterschieds.',
    'Klangeindruck, der durch das Verhältnis hoher zu tiefer Frequenzanteile bestimmt wird.',
    'Klangliche Veränderungen in einem begrenzten Frequenzbereich.',
    'Klangliche Veränderungen in einem begrenzten Frequenzbereich.',
    'Klangliche Veränderungen in einem begrenzten Frequenzbereich.',
    'Klangeindruck, der z.B. auf den Kraftaufwand schließen lässt, mit dem eine Klangquelle angeregt wird.'
      'Beispiele:'
      '- hart/weich angeschlagene Perkussionsinstrumente'
      '- hart/weich gezupfte Saiteninstrumente (klassische Gitarre, Harfe)'
      '- Eine Überbetonung hoher Frequenzen kann einen "scharfen" Klangeindruck fördern.',
    'Klangeindruck heftiger oder aggressiver Modulation/Vibration,'
       'wobei Einzelschwingungen kaum mehr unterscheidbar sind.'
       'Oft als unangenehm bewertet.',
    'Oft tonal wirkende Klangverfrbung. "Hohler" Klang.'
      'Beispiel: Sprechen durch ein Rohr.',
    'Klangverfärbung, die von schmalbandig-resonierenden Anteilen geprägt ist, häufig als Resultat einer geringen Eigenfrequenzdichte.'
      'Häufig bei Anregung von metallenen Gegenständen wie z.B. Gongs, Glocken, scheppernde Blechdosene hörbar.' 
      'Anwendbar auch auf Raumsimulationen, Plattenhall, Hallfolie u..',
    'Wahrnehmbarkeit einer Tonhöhe in einem Klang.'
       'Beispiele tonhaltiger Signale:'
       '- Stimmhafte Sprachanteile,'
       '- Pieptöne.',
    'Die Tonhöhenwahrnehmung erlaubt die Anordnung tonhaltiger Signale entlang einer Skala: "höher - tiefer".',
    'Veränderung der Tonhöhe. Oft als "kontinuierliche Verstimmung" wahrgenommen.'
       'Beispiel: "Verstimmter" Klang der Sirene eines schnell vorbeifahrenden Krankenwagens.',
    'Richtung von Schallquellen in der Horizontalebene.',
    'Richtung von Schallquellen in der Vertikalebene.',
    'Meint nur die Lage vor bzw. hinter dem Hörer. Eindruck des Positionsunterschieds einer Schallquelle, der bei Positionsspiegelung an der durch den Hörer gehend gedachten Frontalebene zustande kommt.',
    'Wahrgenommene Distanz einer Schallquelle.',
    'Wahrgenommene Ausdehnung einer Schallquelle in radialer Richtung.',
    'Wahrgenommene Ausdehnung einer Schallquelle in horizontaler Richtung.',
    'Wahrgenommene Ausdehnung einer Schallquelle in vertikaler Richtung.',
    'Beschreibt die Deutlichkeit, mit der eine Schallquelle - unabhängig von ihrer Distanz - innerhalb oder auerhalb des Kopfes wahrgenommen wird.'
        'Fachlich oft auch zwischen Phänomenen "Im-Kopf-Lokalisation" und "Außer-Kopf-Lokalisation" eingegrenzt.' 
        'Beispiele:'
        '- Schlecht/nicht externalisiert = wahrgenommener Schallquellenort bei diotischer Schallpräsentation per Kopfhörer;'
        '- Gut/stark externalisiert = wahrgenommener Schallquellenort beim Hören einer natürlichen Schallquelle in nachhallbehafteter Umgebung unter Zulassen von Bewegungen des Hörers.',
    'Bei geringer Lokalisierbarkeit sind räumliche Ausdehnung und Ort einer Schallquelle schlecht abschätzbar bzw. erscheinen diffus.' 
        'Bei hoher Lokalisierbarkeit erscheint eine Schallquelle dagegen klar umgrenzt.' 
        'Geringe bzw. groe Lokalisierbarkeiten gehen oft mit großer bzw. geringer wahrgenommener Ausdehnung einer Schallquelle einher.'
        'Beispiel: Schallquellen in stark diffusen Schallfeldern sind schlecht lokalisierbar.',
    'Schallquellen, die erfahrungsgem eine einheitliche räumliche Gestalt haben sollten, erscheinen räumlich separiert.'
        'Mögliche Ursache:'
        'Teile der Schallquelle werden verschiedentlich synthetisiert/simuliert und zwischen den Syntheseverfahren/-engines besteht ein fälschlicher oder ungewollter Versatz bzgl. räumlicher Parameter.' 
        'Beispiele:'
        '- Griffgeräusche und Töne einer Instrumentenquelle kommen nicht vom selben Ort' 
        '- Frikative und Vokale eines Sprechers werden getrennt synthetisiert und dann fälschlich räumlich versetzt wiedergegeben',
    'Wahrnehmung starker Raumanteile, ausgelöst durch ein hohes Verhältnis von reflektierter zu direkter Schallenergie. Führt bei stationrer Anregung zum Eindruck hoher Diffusität (im Sinne eines geringen D/R-Verähltnisses).'
       'Beispiel: Die empfundene Nachhallstärke unterscheidet sich wesentlich zwischen eher kleinen und sehr großen Räumen, wie z.B. zwischen Wohnzimmern und Kirchen.',
    'Dauer des Nachhall-Ausklangvorgangs. Vor allem am Ende von Signalen hörbar.',
    'Wahrnehmung des "vom-Nachhall-räumlich-umhüllt-Seins". Bei hoher Nachhallumhllung kann dem Nachhall nur schwer ein spezifischer Ort, eine begrenzte Ausdehnung oder eine Vorzugsrichtung zugewiesen werden. Eindrcke eher niedriger bzw. eher hoher Nachhallumhüllung entstehen z.B. bei diotisch vs. dichotisch (z.B. dekorreliert) präsentiertem verhallten Material.',
    'Kopien von Schallquellen mit meist geringerer Lautheit bereits vor Beginn des eigentlich intendierten Klangeinsatzes.',
    'Kopien von Schallquellen mit meist abnehmender Lautheit nach Beginn des eigentlich intendierten Klangeinsatzes. Beispiel: Wiederholung der eigenen Stimme durch Reflektion an Gebirgswänden.',
    'Objekte, die erwartungsgemäß eine einheitliche zeitliche Gestalt haben, erscheinen zeitlich separiert. Ursache analog zu "räumliches Zerfallen", nur: hier zeitliche Versätze bei Synthese.'
        'Beispiel: Griffgeräusche und Töne einer Instrumentenquelle kommen nicht zur selben Zeit.',
    'Eigenschaft, die durch die Impulstreue von Systemen beeinflusst wird. Wahrnehmung des Verlaufs von Einschwingvorgängen. Können im Vergleich weicher/verschliffener/weniger präzise, aber auch umgekehrt schneller/präziser/exakter sein.'
        'Beispiel für "verschliffenere" Transienten: Ein Übertragungssystem, das starke Gruppenlaufzeitverzerrungen einfügt.'
        'Gegenbeispiel: Ergebnis einer auf Linearphasigkeit abzielenden Phasenentzerrung.',
    'Eine Szene läuft inhaltlich & klanglich identisch aber offensichtlich schneller oder langsamer ab. Muss nicht mit Tonhöhenänderung einhergehen.' 
        'Beispiele technischer Ursachen:' 
        '- Umdrehungsgeschwindigkeit' 
        '- Sample Rate Conversion'
        '- Time Stretching'
        '- Veränderte Pausen zwischen Signaleinsätzen' 
        '- Bewegungen laufen mit veränderter Geschwindigkeit ab',
    'Reihenfolge oder Auftreten von Szenekomponenten.' 
        'Beispiel: Ein Hund bellt plötzlich am Schluss, anstatt - wie in der Referenz - zu Beginn.',
    'Eigenschaft, die durch Latenzen im System beeinflusst wird. Zur Unterscheidung von einerseits mehr, andererseits weniger verzögerten Reaktionen der Wiedergabeumgebung auf Nutzerinteraktionen.',
    'Wahrgenommene Lautstärke einer Schallquelle. Verschwinden von Objekten ist durch Lautheit = 0 abbildbar.' 
        'Beispiel eines Lautheitsgegensatzes: Flüstern vs. Schreien.',
    'Größe der Lautheitsunterschiede zwischen lauten und leisen Passagen. Bei Signalen geringerer Dynamik unterscheiden sich laute und leise Passagen weniger von der durchschnittlichen Lautheit. Dagegen enthalten Signale mit hoher Dynamik sowohl sehr laute als auch sehr leise Passagen.',
    'Klangveränderungen jenseits des langfristigen Lautheitsverlaufs. Sammelkategorie für eine Vielzahl von durch Dynamikkompression hervorgerufenen Perzepten.'
        'Beispiele: Kompakterer Klang eines summenkomprimierten Musiktracks gegenüber dem unbearbeiteten Original.'
        '"Kompressorpumpen": Bei Signalenergiespitzen (Bassdrumeinstze, Plosivlaute) fällt die Signallautheit plötzlich ab und kehrt nach einer spürbaren Zeitspanne wieder auf das vorherige Niveau zurück.',
    'Ausbildung einer eigenständigen, in der Szene eindeutig nicht intendierten Wahrnehmungsgestalt.'
        'Beispiel: Ein eindeutig nicht zur präsentierten Szene gehöriger Störton, wie z.B. ein unerwarteter Piepton "aus der Technik".',
    'Ausbildung einer eigenständigen, in der Szene eindeutig nicht intendierten Wahrnehmungsgestalt.' 
        'Beispiel: Ein eindeutig nicht zur präsentierten Szene gehöriges, kurzes Störgeräusch wie z.B. ein Knacksen "aus der Technik".',
    'Ausbildung einer eigenständigen, in der Szene eindeutig nicht intendierten Wahrnehmungsgestalt.'
        'Beispiel: Ein eindeutig nicht zur präsentierten Szene gehöriges Rauschen wie z.B. ein Hintergrundrauschen von Lüftern.',
    'Ausbildung einer eigenständigen, in der Szene eindeutig nicht intendierten Wahrnehmungsgestalt.'
        'Beispiele:'
        '- ein eingekoppeltes Radiosignal' 
        '- ein versehentlich nicht "stumm" geschalteter Mischpultkanal',
    'Räumlich getrenntes, annhernd gleichzeitiges, nicht unbedingt identisches, Abbild einer Schallquelle.'
        'Eine Art örtliche Signalkopie: Eine Schallquelle taucht an einem oder mehreren zusätzlichen Orten in der Szene auf.'
        'Beispiele:'
        '- Zwei Schallquellen geben fälschlich denselben Audioinhalt wieder.'
        '- Doppelabbildung bei Mischungen mit Haupt-/Stützmikrofonierung.'
        '- Räumliches Aliasing bei WFS: Schallquellen werden als richtungsmehrdeutig wahrgenommen.',
    'Perzept infolge von nichtlinearen Verzerrungen, wie sie z.B. durch Übersteuerungen entstehen. Kratziger oder "kaputter" Sound. Oft von Signalamplitude abhngig. Kann seine Qualität je nach Art der Übersteuerung stark ändern.'
        'Beispiel: Clipping bei Übersteuerung von digitalen Eingangsstufen.',
    'Wahrnehmung am Grenzbereich zwischen auditiver und taktiler Modalitt. Spürbarkeit von Vibrationen, die von einer Schallquelle verursacht werden, z.B. durch mechanische Ankopplung an Auflagefälchen. ' 
        'Beispiele:'
        '- Livekonzert: Bass "geht in den Magen".'
        '- Kopfhörerauflagen vibrieren spürbar auf Ohren/an Schläfe.',
    'Klarheit/Deutlichkeit beliebiger Szeneninhalte. Eindruck davon, wie klar Szeneninhalte voneinander unterschieden und wie gut verschiedenste Eigenschaften einzelner Szeneninhalte erkannt werden können. Der Begriff ist also weiter gefasst, als der in der Raumakustik durch das Klarheitsmaß prädizierte Eindruck einer mit steigender Nachhallenergie sinkenden Transparenz.',
    'Eindruck davon, wie gut die Worte eines Sprechers verstanden werden können.' 
        'Typisch für geringe Sprachverständlichkeit: Bahnhofsdurchsagen.' 
        'Typisch für hohe Sprachverständlichkeit: Nachrichtensprecher.',
    'Eindruck, dass ein Signal der Erwartung/Erfahrung an eine solches Signal entspricht.',
    '"In-der-Szene-Sein" im Sinne räumlicher Präsenz. Eindruck in einer präsentierten Szene vor Ort, in die Szene räumlich integriert zu sein.',
    'Unterschied bzgl. Angenehmheit/Unangenehmheit.',
    'Weiterer, bisher noch nicht erfasster Unterschied.',
    # custom
    'Klangliche Veränderung',  # Coloration
    'Schallquellen Positionssänderung',  # Source Direction
    'Veränderung der Quellbreite'
]

phrases_en = [
    'Is there a noticeable difference between the two stimuli? If there is, please rate perceived amount of this difference.'
       'Does stimulus A differ from your expectations? If there is, please rate the perceived amount of this difference.',
     'Please rate:',
     'Is the perceived difference ...',
     '... constant in time?',
     '... varying periodically or otherwise rule-based?',
     '... varying non-regularly?',
     '... continuously?',
     '... discontinuously?',
     'Does the perceived difference depend on ...',
     '... your actions?',
     '... scene events?',
     '... nothing of the before mentioned?',
     'Which of the following entities would you assign the perceived difference to (multiple selections possible)?',
     'Did you perceive any other difference not mentioned before? If so, please name and rate the perceived amount of this difference.'
        'Does stimulus A differ from your expectations in any other way not mentioned before? If so, please name and rate the perceived amount of this difference.',
     'Please name the difference',
     'up to 180'
]

phrases_ger = [
    'Können Sie zwischen den beiden Stimuli einen Unterschied wahrnehmen? Wenn ja, bewerten Sie bitte die Ausprägung des wahrgenommenen Unterschieds.'
       'Unterscheidet sich Stimulus A von Ihrer Erwartung? Wenn ja, bewerten Sie bitte die Ausprägung des wahrgenommenen Unterschieds!',
     'Bewerten Sie:',
     'Ist der wahrgenommene Unterschied...',
     '... konstant?',
     '... regelhaft zeitveränderlich?',
     '... regellos zeitveränderlich?',
     '... und dabei stetig?',
     '... und dabei unstetig?',
     'Ist der wahrgenommene Unterschied abähngig von...',
     '... Ihren Reaktionen?',
     '... Ereignissen in der Szene?',
     '... keinem davon.',
     'Welchem der folgenden Objekte (oder auch mehreren davon) würden Sie den wahrgenommenen Unterschied zuordnen?',
     'Können Sie zwischen den beiden Stimuli sonst noch einen Unterschied wahrnehmen? Wenn ja, benennen und bewerten Sie die Auspräung der Qualität.'
        'Unterscheidet sich Stimulus A in einer sonstigen Weise von Ihrer Erwartung? Wenn ja, benennen und bewerten Sie die Ausprägung der Qualiätt.',
     'Benennen Sie den Unterschied',
     'bis 180'
]