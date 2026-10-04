# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Enkelvoudige en samengestelde stoffen.

Hoort bij "opbouw van materie" van de vakfiche chemie 2de graad
doorstroomfinaliteit, samen met [ch_mengsels]. Samen 10 % van het examen.

Deel 1 gaat over de namen en symbolen van de elementen die de fiche opsomt, en
over het lezen van een formule: de index, de coëfficiënt, het aantal atomen,
het aantal moleculen en het onderscheid tussen een enkelvoudige en een
samengestelde stof. Deel 2 gaat over de triviale namen van de enkelvoudige
stoffen en over de eigenschappen en toepassingen van metalen, niet-metalen en
edelgassen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welk element heeft het symbool Fe?",
        opties=[
            "ijzer",
            "fosfor",
            "fluor",
            "francium",
        ],
        antwoord=0,
        uitleg="Fe komt van het Latijnse ferrum. Fosfor is P en fluor is F.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk symbool hoort bij kalium?",
        opties=[
            "K",
            "Ka",
            "Cl",
            "Ca",
        ],
        antwoord=0,
        uitleg="Kalium is K, van het Latijnse kalium. Ca is calcium, en Cl is chloor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze symbolen horen bij een metaal? Kruis alles aan wat juist is.",
        opties=[
            "Cu",
            "Zn",
            "S",
            "Ne",
        ],
        antwoord=[0, 1],
        uitleg="Cu is koper en Zn is zink, allebei metalen. S is zwavel, een niet-metaal, en Ne is neon, een edelgas.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de formule 3 H₂SO₄: wat is het getal 3?",
        opties=[
            "de coëfficiënt",
            "de index",
            "het atoomnummer",
            "het massagetal",
        ],
        antwoord=0,
        uitleg="De coëfficiënt staat vooraan en zegt hoeveel deeltjes van die stof er zijn. De index staat rechts onderaan bij een symbool.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de formule H₂SO₄: wat betekent de 4 achter de O?",
        opties=[
            "er zitten vier zuurstofatomen in de molecule",
            "er zijn vier moleculen van de stof",
            "zuurstof staat in groep vier",
            "de stof heeft vier bindingen",
        ],
        antwoord=0,
        uitleg="Een index hoort bij het symbool ervoor en zegt hoeveel atomen van dat element in één deeltje zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel atomen in totaal zitten er in één molecule H₂SO₄?",
        opties=[
            "zeven",
            "drie",
            "zes",
            "vier",
        ],
        antwoord=0,
        uitleg="Twee waterstof, één zwavel en vier zuurstof: samen zeven atomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel verschillende atoomsoorten komen voor in 2 Ca(NO₃)₂?",
        opties=[
            "drie",
            "twee",
            "vier",
            "zes",
        ],
        antwoord=0,
        uitleg="Calcium, stikstof en zuurstof: drie elementen. De coëfficiënt 2 en de indexen veranderen het aantal soorten niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn enkelvoudig? Kruis alles aan wat juist is.",
        opties=[
            "O₂",
            "Fe",
            "H₂O",
            "NaCl",
        ],
        antwoord=[0, 1],
        uitleg="Een enkelvoudige stof bevat maar één element. O₂ bestaat enkel uit zuurstof, ijzer enkel uit ijzer. Water en keukenzout bevatten meerdere elementen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is O₃ een enkelvoudige stof, ook al staan er drie atomen in?",
        opties=[
            "alle atomen horen bij hetzelfde element",
            "er staat geen coëfficiënt voor",
            "het is een gas bij kamertemperatuur",
            "drie is een oneven getal",
        ],
        antwoord=0,
        uitleg="Enkelvoudig of samengesteld hangt af van het aantal verschillende elementen, niet van het aantal atomen. O₃ bevat enkel zuurstof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij een synthese?",
        opties=[
            "uit meerdere stoffen ontstaat één nieuwe stof",
            "een stof valt uiteen in haar bestanddelen",
            "een mengsel wordt gescheiden met een filter",
            "een stof verandert enkel van aggregatietoestand",
        ],
        antwoord=0,
        uitleg="Synthese is opbouwen: twee of meer stoffen vormen samen een nieuwe stof. Analyse is het omgekeerde, uiteenvallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men de schrijfwijze NaCl voor keukenzout?",
        opties=[
            "een formule-eenheid",
            "een brutoformule",
            "een structuurformule",
            "een modelvoorstelling",
        ],
        antwoord=0,
        uitleg="Bij een ionverbinding bestaan er geen losse moleculen. De formule geeft de kleinste verhouding en heet daarom een formule-eenheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Het symbool van natrium is Na.",
        antwoord=True,
        uitleg="Na komt van natrium. Het symbool van stikstof is N, dus let op het verschil.",
    ),
    dict(
        type="waarofniet",
        vraag="Het symbool van koolstof is Co.",
        antwoord=False,
        uitleg="Koolstof is C. Co is kobalt, een metaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Het eerste letterteken van een elementsymbool wordt met een hoofdletter geschreven.",
        antwoord=True,
        uitleg="De eerste letter is altijd een hoofdletter en een eventuele tweede letter is klein, zoals bij Mg of Cl.",
    ),
    dict(
        type="waarofniet",
        vraag="Een coëfficiënt 2 voor H₂O betekent dat er twee zuurstofatomen in één molecule zitten.",
        antwoord=False,
        uitleg="De coëfficiënt geldt voor het hele deeltje: 2 H₂O zijn twee watermoleculen, dus vier waterstof- en twee zuurstofatomen in totaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Analyse en synthese zijn hetzelfde soort omzetting.",
        antwoord=False,
        uitleg="Bij analyse valt een stof uiteen in eenvoudiger stoffen; bij synthese worden stoffen juist samengevoegd.",
    ),
    dict(
        type="invultekst",
        vraag="Welk element heeft het symbool Ag?",
        antwoord=["zilver", "het zilver"],
        uitleg="Ag komt van het Latijnse argentum. Au is goud, van aurum.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is het symbool van het element magnesium?",
        antwoord=["Mg"],
        uitleg="Magnesium is Mg. Mn is mangaan, dus de tweede letter maakt het verschil.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel waterstofatomen zitten er in totaal in 3 H₂O?",
        antwoord=["6", "zes"],
        uitleg="Per molecule twee waterstofatomen, en drie moleculen: dat zijn zes waterstofatomen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een stof die uit meerdere verschillende elementen bestaat?",
        antwoord=["samengesteld", "een samengestelde stof", "samengestelde stof"],
        uitleg="Een samengestelde stof bevat atomen van minstens twee elementen, zoals water of keukenzout.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke formule hoort bij zuurstofgas?",
        opties=[
            "O₂",
            "O",
            "O₃",
            "H₂O",
        ],
        antwoord=0,
        uitleg="Zuurstofgas bestaat uit moleculen van twee zuurstofatomen. O₃ is ozon en O alleen is een los atoom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof heeft de triviale naam ozon?",
        opties=[
            "O₃",
            "O₂",
            "CO₂",
            "H₂O₂",
        ],
        antwoord=0,
        uitleg="Ozon bestaat uit drie zuurstofatomen per molecule. Het beschermt ons hoog in de atmosfeer tegen uv-straling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschappen horen bij metalen? Kruis alles aan wat juist is.",
        opties=[
            "ze geleiden elektriciteit goed",
            "ze zijn vervormbaar",
            "ze zijn bij kamertemperatuur altijd een gas",
            "ze hebben geen glans",
        ],
        antwoord=[0, 1],
        uitleg="Metalen geleiden elektriciteit en warmte, zijn vervormbaar en hebben glans. Op kwik na zijn ze bij kamertemperatuur vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men helium in een weerballon?",
        opties=[
            "het is licht en reageert niet",
            "het geleidt elektriciteit uitstekend",
            "het brandt met een heldere vlam",
            "het lost goed op in water",
        ],
        antwoord=0,
        uitleg="Helium is een edelgas: het is inert en dus niet brandbaar, en het is veel lichter dan lucht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke enkelvoudige stoffen gebruikt men omdat ze met niets reageren? Kruis alles aan wat juist is.",
        opties=[
            "neon in lichtreclame",
            "helium in een ballon",
            "chloorgas in een zwembad",
            "zuurstofgas in een ziekenhuis",
        ],
        antwoord=[0, 1],
        uitleg="Neon en helium zijn edelgassen en dus inert. Chloorgas en zuurstofgas worden juist gebruikt omdát ze reageren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Grafiet en diamant bestaan allebei uit koolstof. Waarom zijn hun eigenschappen zo verschillend?",
        opties=[
            "de atomen liggen anders geschikt",
            "diamant bevat ook zuurstof",
            "grafiet is een mengsel",
            "diamant heeft een ander atoomnummer",
        ],
        antwoord=0,
        uitleg="In diamant zit elk koolstofatoom aan vier andere vast in een stevig ruimtelijk rooster. In grafiet liggen de atomen in lagen die over elkaar schuiven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geleidt grafiet elektriciteit en diamant niet?",
        opties=[
            "in grafiet kunnen elektronen zich vrij bewegen",
            "grafiet is zachter dan diamant",
            "grafiet is zwart van kleur",
            "diamant is doorzichtig",
        ],
        antwoord=0,
        uitleg="In grafiet hoort elk koolstofatoom maar aan drie andere vast; de overblijvende elektronen bewegen vrij door de lagen. In diamant zit elk elektron vast in een binding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn edelgassen? Kruis alles aan wat juist is.",
        opties=[
            "He",
            "Ar",
            "N₂",
            "Cl₂",
        ],
        antwoord=[0, 1],
        uitleg="Helium en argon staan in de laatste groep van het periodiek systeem en reageren met vrijwel niets. Stikstofgas en chloorgas zijn niet-metalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Chloorgas valt op door zijn kleur. Welke is dat?",
        opties=[
            "geelgroen",
            "diepblauw",
            "roodbruin",
            "kleurloos",
        ],
        antwoord=0,
        uitleg="Cl₂ is een geelgroen gas met een scherpe geur. Die kleur is een van de weinige die de fiche uitdrukkelijk vraagt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kleur heeft zuiver koper?",
        opties=[
            "roodbruin",
            "zilvergrijs",
            "geelgroen",
            "diepzwart",
        ],
        antwoord=0,
        uitleg="Koper is roodbruin en glanzend. Dat maakt het makkelijk te onderscheiden van de meeste andere metalen, die zilvergrijs zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men waterstofgas als brandstof?",
        opties=[
            "bij de verbranding ontstaat enkel water",
            "het is een edelgas en dus veilig",
            "het is het zwaarste gas dat er bestaat",
            "het lost niet op in water",
        ],
        antwoord=0,
        uitleg="Waterstof verbrandt met zuurstof tot water, dus komt er geen koolstofdioxide vrij. Het gas is wel heel brandbaar en vraagt dus voorzichtigheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Edelgassen zijn inert: ze gaan bijna geen reacties aan.",
        antwoord=True,
        uitleg="Hun buitenste schil is volledig gevuld, dus hebben ze niets te winnen bij een binding.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij kamertemperatuur zijn alle metalen vast.",
        antwoord=False,
        uitleg="Kwik is bij kamertemperatuur vloeibaar. Dat is de uitzondering onder de metalen.",
    ),
    dict(
        type="waarofniet",
        vraag="Niet-metalen geleiden elektriciteit even goed als metalen.",
        antwoord=False,
        uitleg="Bij een niet-metaal zitten de elektronen vast in bindingen, dus geleidt het slecht. Grafiet is de bekende uitzondering.",
    ),
    dict(
        type="waarofniet",
        vraag="De triviale naam van N₂ is stikstofgas.",
        antwoord=True,
        uitleg="Stikstofgas vormt bijna vier vijfde van de lucht. De IUPAC-naam is distikstof.",
    ),
    dict(
        type="waarofniet",
        vraag="Ozon en zuurstofgas zijn dezelfde stof, want ze bestaan uit hetzelfde element.",
        antwoord=False,
        uitleg="Het aantal atomen per molecule verschilt, en daarmee ook de eigenschappen: ozon ruikt scherp en is giftig om in te ademen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke enkelvoudige stof gebruikt men in de potloodstift, omdat de lagen erin over elkaar schuiven?",
        antwoord=["grafiet", "het grafiet"],
        uitleg="Grafiet bestaat uit koolstoflagen die loslaten. Daarom laat een potlood een streep na op papier.",
    ),
    dict(
        type="invultekst",
        vraag="Welke enkelvoudige stof heeft de triviale naam waterstofgas?",
        antwoord=["H2", "diwaterstof", "H₂"],
        uitleg="Waterstofgas bestaat uit moleculen van twee waterstofatomen, dus H₂. De IUPAC-naam is diwaterstof.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de eigenschap van een metaal om zich te laten pletten en buigen zonder te breken?",
        antwoord=["vervormbaarheid", "de vervormbaarheid", "vervormbaar"],
        uitleg="Omdat de elektronen in een metaal vrij bewegen, kunnen de atomen langs elkaar schuiven zonder dat de binding breekt.",
    ),
    dict(
        type="invultekst",
        vraag="Welke enkelvoudige stof, hard en doorzichtig, gebruikt men in boor- en zaagwerktuigen?",
        antwoord=["diamant", "het diamant"],
        uitleg="In diamant hangt elk koolstofatoom aan vier andere vast. Dat ruimtelijke rooster maakt het de hardste natuurlijke stof.",
    ),
]
