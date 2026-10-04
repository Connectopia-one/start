# -*- coding: utf-8 -*-
"""De celcyclus, mitose en meiose — 🌍 Beyond, biologie.

Deel 1 gaat over de celcyclus en de mitose: de fasen van de interfase, de
controlepunten, en wat er in profase, metafase, anafase en telofase gebeurt.
Deel 2 gaat over de meiose, over mixing en crossing-over, en over de
vergelijking van de twee celdelingen.

De fiche vraagt uitdrukkelijk de vergelijking van mitose en meiose, en ze
vraagt het belang en het principe van mixing en crossing-over. Daarom staan in
deel 2 vier vragen die de twee delingen naast elkaar zetten, en niet alleen
vragen over de meiose apart.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Uit welke twee grote delen bestaat de celcyclus?",
        opties=[
            "de interfase en de M-fase",
            "de profase en de telofase",
            "de meiose I en de meiose II",
            "de G0-fase en de cytokinese",
        ],
        antwoord=0,
        uitleg="In de interfase groeit de cel en kopieert ze haar DNA. In de M-fase deelt "
        "ze zich, kern eerst en daarna het cytoplasma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de G1-fase?",
        opties=[
            "de cel groeit en maakt eiwitten aan",
            "het DNA wordt gekopieerd",
            "de chromosomen worden uiteengetrokken",
            "het cytoplasma wordt in twee gedeeld",
        ],
        antwoord=0,
        uitleg="G1 is de eerste groeifase: de cel maakt organellen en eiwitten bij. Pas in "
        "de S-fase komt er DNA bij.",
    ),
    dict(
        type="invultekst",
        vraag="In welke fase van de interfase wordt het DNA gekopieerd?",
        antwoord=["S-fase", "S", "de S-fase"],
        uitleg="S staat voor synthese. Daarna heeft elk chromosoom twee identieke "
        "zusterchromatiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de G0-fase?",
        opties=[
            "een rusttoestand buiten de celcyclus",
            "de fase waarin het DNA gekopieerd wordt",
            "de laatste fase van de mitose",
            "de fase waarin de cel in twee gaat",
        ],
        antwoord=0,
        uitleg="Een cel in G0 doet haar werk maar deelt niet meer. Zenuwcellen en "
        "spiercellen blijven daar hun hele leven in; een levercel kan er weer uit komen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dienen de controlepunten in de celcyclus? Kruis alles aan wat juist is.",
        opties=[
            "nakijken of het DNA onbeschadigd is",
            "nakijken of de cel groot genoeg is",
            "het DNA sneller kopiëren",
            "de chromosomen zichtbaar maken",
        ],
        antwoord=[0, 1],
        uitleg="Op een controlepunt wordt de cyclus stilgelegd tot alles in orde is. "
        "Werken die punten niet meer, dan kan een cel ongeremd blijven delen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de profase van de mitose?",
        opties=[
            "de chromosomen condenseren en het kernmembraan verdwijnt",
            "de chromosomen gaan op het evenaarsvlak staan",
            "de chromatiden worden naar de polen getrokken",
            "er vormt zich een nieuw kernmembraan",
        ],
        antwoord=0,
        uitleg="Het chromatine rolt op tot zichtbare chromosomen, het kernmembraan valt "
        "uiteen en de spoelfiguur wordt opgebouwd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het vlak in het midden van de cel waar de chromosomen tijdens de metafase gaan staan?",
        antwoord=["evenaarsvlak", "het evenaarsvlak", "equatorvlak"],
        uitleg="In de metafase staan alle chromosomen netjes op het evenaarsvlak. Van daar "
        "worden de chromatiden in de anafase uiteengetrokken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de anafase van de mitose?",
        opties=[
            "de zusterchromatiden gaan naar de polen",
            "de homologe chromosomen gaan naar de polen",
            "het DNA wordt gekopieerd",
            "er ontstaat een celplaat in het midden",
        ],
        antwoord=0,
        uitleg="De trekdraden verkorten en trekken van elk chromosoom één chromatide naar "
        "elke pool. Daardoor krijgen beide dochtercellen dezelfde informatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaruit bestaat de spoelfiguur?",
        opties=[
            "uit microtubuli",
            "uit histonen",
            "uit chromatiden",
            "uit celmembraan",
        ],
        antwoord=0,
        uitleg="De microtubuli van de spoelfiguur werken als steun- en trekdraden. Ze "
        "grijpen aan op het kinetochoor van elk chromosoom.",
    ),
    dict(
        type="waarofniet",
        vraag="In de telofase vormt zich rond elke groep chromosomen een nieuw kernmembraan.",
        antwoord=True,
        uitleg="De chromosomen rollen weer los en er komt opnieuw een kernmembraan rond. "
        "Daarna volgt de cytokinese.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de cytokinese?",
        opties=[
            "het verdelen van het cytoplasma",
            "het verdelen van de chromosomen",
            "het kopiëren van het DNA",
            "het opbouwen van de spoelfiguur",
        ],
        antwoord=0,
        uitleg="Na de kerndeling wordt het cytoplasma in twee gedeeld. Bij een dierlijke "
        "cel knijpt het membraan toe, bij een plantencel ontstaat er een celplaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de cytokinese bij een plant en bij een dier?",
        opties=[
            "bij een plant ontstaat er een celplaat",
            "bij een plant gebeurt er geen cytokinese",
            "bij een dier blijft het cytoplasma gemeenschappelijk",
            "bij een dier komen er twee kernen in één cel",
        ],
        antwoord=0,
        uitleg="Een plantencel heeft een celwand en kan niet toeknijpen. Daarom bouwt ze "
        "in het midden een celplaat, die tot een nieuwe celwand wordt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel dochtercellen levert één mitose op?",
        antwoord=["2", "twee"],
        uitleg="Eén mitose geeft twee dochtercellen, elk met hetzelfde aantal chromosomen "
        "als de moedercel. Daarom is de mitose de deling van groei en herstel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de mitose in ons lichaam? Kruis alles aan wat juist is.",
        opties=[
            "groeien",
            "beschadigd weefsel herstellen",
            "geslachtscellen maken",
            "het aantal chromosomen halveren",
        ],
        antwoord=[0, 1],
        uitleg="De mitose levert twee identieke cellen en zorgt dus voor groei, herstel en "
        "vervanging. Gameten maken en halveren is het werk van de meiose.",
    ),
    dict(
        type="waarofniet",
        vraag="Na een mitose heeft elke dochtercel de helft van het aantal chromosomen van de moedercel.",
        antwoord=False,
        uitleg="Na een mitose heeft elke dochtercel precies hetzelfde aantal. Halveren "
        "gebeurt alleen bij de meiose.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke reeks geeft de fasen van de mitose in de juiste orde?",
        opties=[
            "profase, metafase, anafase, telofase",
            "metafase, profase, telofase, anafase",
            "anafase, telofase, profase, metafase",
            "telofase, anafase, metafase, profase",
        ],
        antwoord=0,
        uitleg="Eerst condenseren, dan opstellen, dan uiteentrekken, dan weer twee kernen "
        "vormen. De cytokinese volgt daar nog op.",
    ),
    dict(
        type="waarofniet",
        vraag="Tijdens de interfase zijn de chromosomen onder de microscoop als losse staafjes te zien.",
        antwoord=False,
        uitleg="In de interfase ligt het DNA als chromatine los in de kern. Pas als het in "
        "de profase condenseert, worden de chromosomen zichtbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Aan het begin van de mitose bestaat elk chromosoom uit twee zusterchromatiden.",
        antwoord=True,
        uitleg="Na de S-fase heeft elk chromosoom twee chromatiden, samengehouden aan het "
        "centromeer. In de anafase worden die van elkaar getrokken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de hele periode tussen twee celdelingen?",
        antwoord=["interfase", "de interfase"],
        uitleg="De interfase bestaat uit G1, S en G2 en duurt veel langer dan de deling "
        "zelf. Een cel is dus het grootste deel van haar leven niet aan het delen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de G2-fase?",
        opties=[
            "de cel bereidt de deling voor en keurt het DNA",
            "het DNA wordt voor het eerst gekopieerd",
            "de cel stapt uit de celcyclus",
            "het cytoplasma wordt al in twee gedeeld",
        ],
        antwoord=0,
        uitleg="In G2 groeit de cel verder en worden de kopieën nagekeken. Op het "
        "controlepunt aan het eind van G2 beslist de cel of de deling kan starten.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het resultaat van een volledige meiose?",
        opties=[
            "vier haploïde cellen",
            "twee haploïde cellen",
            "vier diploïde cellen",
            "twee diploïde cellen",
        ],
        antwoord=0,
        uitleg="Na meiose I en meiose II zijn er vier cellen, elk met de helft van het "
        "aantal chromosomen. Bij de mens is dat 23.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in meiose I dat in een mitose nooit gebeurt?",
        opties=[
            "de homologe chromosomen gaan uit elkaar",
            "de zusterchromatiden gaan uit elkaar",
            "het kernmembraan valt uiteen",
            "de spoelfiguur wordt opgebouwd",
        ],
        antwoord=0,
        uitleg="In meiose I worden de paren gescheiden, niet de chromatiden. Daardoor "
        "wordt de cel haploïd; dat heet de reductiedeling.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het uitwisselen van stukken tussen twee homologe chromosomen?",
        antwoord=["crossing-over", "overkruising", "crossing over"],
        uitleg="Tijdens de profase van meiose I leggen homologen zich tegen elkaar en "
        "wisselen stukken uit. De plaats waar ze kruisen heet een chiasma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het belang van crossing-over?",
        opties=[
            "nieuwe combinaties van allelen maken",
            "het aantal chromosomen halveren",
            "het DNA kopiëren voor de deling",
            "de cel groter maken voor ze deelt",
        ],
        antwoord=0,
        uitleg="Door de uitwisseling komen allelen van vader en moeder op één chromosoom "
        "samen. Dat heet recombinatie en vergroot de variatie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de plaats waar twee homologe chromosomen elkaar kruisen?",
        antwoord=["chiasma", "een chiasma", "chiasmata"],
        uitleg="Op het chiasma worden de stukken uitgewisseld. Eén paar chromosomen kan er "
        "meerdere hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is mixing bij de meiose?",
        opties=[
            "de paren verdelen zich toevallig over de polen",
            "de chromatiden wisselen stukken uit",
            "twee gameten smelten samen",
            "het DNA wordt dubbel gekopieerd",
        ],
        antwoord=0,
        uitleg="Elk paar gaat onafhankelijk van de andere paren naar een pool. Bij 23 "
        "paren geeft dat al meer dan acht miljoen mogelijke combinaties, en crossing-over "
        "komt daar nog bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is variatie tussen gameten belangrijk? Kruis alles aan wat juist is.",
        opties=[
            "broers en zussen verschillen daardoor van elkaar",
            "een soort kan zich beter aanpassen",
            "de gameten worden daardoor diploïd",
            "de celcyclus verloopt daardoor sneller",
        ],
        antwoord=[0, 1],
        uitleg="Mixing en crossing-over maken elke gameet anders. Die variatie is het "
        "materiaal waarop selectie later kan werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in meiose II?",
        opties=[
            "de zusterchromatiden worden gescheiden",
            "de homologe chromosomen worden gescheiden",
            "het DNA wordt opnieuw gekopieerd",
            "de vier cellen smelten weer samen",
        ],
        antwoord=0,
        uitleg="Meiose II lijkt op een mitose, maar start in haploïde cellen. Daarna zijn "
        "er vier cellen met elk één chromatide per chromosoom.",
    ),
    dict(
        type="waarofniet",
        vraag="Tussen meiose I en meiose II wordt het DNA opnieuw gekopieerd.",
        antwoord=False,
        uitleg="Er komt geen tweede S-fase. Anders zou het aantal chromosomen niet "
        "gehalveerd worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarin verschillen mitose en meiose? Kruis alles aan wat juist is.",
        opties=[
            "de mitose geeft twee cellen, de meiose vier",
            "de meiose halveert het chromosomenaantal",
            "alleen bij de mitose wordt het DNA gekopieerd",
            "alleen bij de meiose is er een spoelfiguur",
        ],
        antwoord=[0, 1],
        uitleg="Bij beide delingen hoort er een S-fase voor en een spoelfiguur tijdens. "
        "Het aantal dochtercellen en het halveren zijn de echte verschillen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zijn de dochtercellen van een mitose en van een meiose erfelijk gelijk aan elkaar?",
        opties=[
            "bij de mitose wel, bij de meiose niet",
            "bij de meiose wel, bij de mitose niet",
            "bij beide delingen wel",
            "bij beide delingen niet",
        ],
        antwoord=0,
        uitleg="Een mitose geeft twee identieke cellen. Door mixing en crossing-over zijn "
        "de vier cellen van een meiose alle vier verschillend.",
    ),
    dict(
        type="waarofniet",
        vraag="Een meiose gebeurt bij de mens alleen in de eierstokken en de teelballen.",
        antwoord=True,
        uitleg="Alleen de geslachtsklieren maken gameten. Alle andere weefsels delen met "
        "een mitose.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel chromosomen heeft een menselijke cel na meiose I?",
        opties=[
            "23",
            "46",
            "92",
            "12",
        ],
        antwoord=0,
        uitleg="Na meiose I zijn de paren gescheiden, dus is de cel al haploïd. Elk van die "
        "23 chromosomen heeft nog twee chromatiden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een celdeling waarbij het aantal chromosomen gehalveerd wordt?",
        antwoord=["reductiedeling", "een reductiedeling", "meiose"],
        uitleg="Meiose I is de reductiedeling. Meiose II is een gewone deling van de "
        "chromatiden, maar dan in haploïde cellen.",
    ),
    dict(
        type="waarofniet",
        vraag="Wordt een chromosomenpaar bij de meiose verkeerd verdeeld, dan krijgt een gameet een chromosoom te veel of te weinig.",
        antwoord=True,
        uitleg="Zo'n fout heet een non-disjunctie. Bevrucht die gameet toch, dan heeft het "
        "kind een chromosoom te veel of te weinig, zoals bij trisomie 21.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een crossing-over wisselen twee zusterchromatiden van hetzelfde chromosoom stukken uit.",
        antwoord=False,
        uitleg="De uitwisseling gebeurt tussen homologe chromosomen, dus tussen dat van de "
        "vader en dat van de moeder. Zusterchromatiden zijn identiek, daar valt niets te "
        "wisselen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom blijft het aantal chromosomen van een soort over de generaties gelijk?",
        opties=[
            "de meiose halveert en de bevruchting verdubbelt",
            "de mitose halveert en de meiose verdubbelt",
            "elke gameet is diploïd",
            "de bevruchting halveert het aantal",
        ],
        antwoord=0,
        uitleg="Twee haploïde gameten geven samen weer een diploïde zygote. Zonder de "
        "halvering zou het aantal elke generatie verdubbelen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de cellen die uit een meiose komen en bij de voortplanting gebruikt worden?",
        antwoord=["gameten", "geslachtscellen", "voortplantingscellen"],
        uitleg="Gameten, geslachtscellen en voortplantingscellen zijn drie woorden voor "
        "dezelfde cellen. Bij de mens zijn dat de eicel en de zaadcel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben mitose en meiose met elkaar gemeen? Kruis alles aan wat juist is.",
        opties=[
            "er gaat een S-fase aan vooraf",
            "er wordt een spoelfiguur gebruikt",
            "ze leveren allebei vier cellen op",
            "ze gebeuren allebei alleen in de geslachtsklieren",
        ],
        antwoord=[0, 1],
        uitleg="Beide delingen kopiëren eerst het DNA en trekken de chromosomen daarna "
        "met microtubuli uiteen. Het aantal cellen en de plaats in het lichaam verschillen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gaat een cel met beschadigd DNA het best niet in deling?",
        opties=[
            "de fout wordt dan aan alle dochtercellen doorgegeven",
            "de cel zou dan te groot worden",
            "de spoelfiguur kan dan niet gevormd worden",
            "het kernmembraan blijft dan dicht",
        ],
        antwoord=0,
        uitleg="Daarom legt een controlepunt de cyclus stil tot de schade herstelde. Lukt "
        "dat niet, dan gaat de cel in geprogrammeerde celdood.",
    ),
]
