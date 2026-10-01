# -*- coding: utf-8 -*-
"""Poëzie: dichtvormen, strofen en rijm — 🌍 Beyond, Nederlands.

Naast de termenlijst van de vakfiches geschreven. Deel 1: de dichtvormen en
de strofen. Deel 2: ritme, rijm, enjambement en de overige poëziebegrippen.

Geen enkel citaat wordt aan een bestaande dichter toegeschreven. Waar er een
voorbeeldregel nodig is, staat er een zelf geschreven regeltje zonder naam.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Uit hoeveel verzen bestaat een sonnet?",
        opties=[
            "veertien",
            "twaalf",
            "zestien",
            "tien",
        ],
        antwoord=0,
        uitleg="Veertien verzen, klassiek verdeeld in twee kwatrijnen en twee terzetten, of in een octaaf en een sextet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke dichtvormen bestaan er?",
        opties=[
            "het rondeel",
            "de ode",
            "de elegie",
            "de alinea",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een alinea hoort bij proza. De drie andere zijn vaste dichtvormen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een gedicht waarvan de eerste letters van de verzen samen een woord vormen? Antwoord met één woord.",
        antwoord=["acrostichon"],
        uitleg="Lees de beginletters van boven naar beneden en je krijgt een naam of een woord.",
    ),
    dict(
        type="waarofniet",
        vraag="Een haiku telt vijf verzen.",
        antwoord=False,
        uitleg="Een haiku telt er drie, van vijf, zeven en vijf lettergrepen, vaak met een natuurbeeld en een plotse wending.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een elegie?",
        opties=[
            "een klaagzang om een verlies",
            "een lofzang op een persoon of een zaak",
            "een kort spotgedicht met een vaste maat",
            "een gedicht waarin de vorm een tekening maakt",
        ],
        antwoord=0,
        uitleg="Een elegie treurt. Een ode doet net het omgekeerde: die prijst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kort, grappig gedicht van vijf verzen met een vast rijmschema en een onverwachte afloop. Wat is dat?",
        opties=[
            "een limerick",
            "een hymne",
            "een ballade",
            "een minnelied",
        ],
        antwoord=0,
        uitleg="De limerick heeft vijf verzen met het rijmschema aabba en leeft van de pointe.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ode is een lofzang.",
        antwoord=True,
        uitleg="Een ode bezingt iemand of iets met verhevenheid. Een hymne doet hetzelfde, maar dan vaak voor een god of een gemeenschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is visuele poëzie?",
        opties=[
            "poëzie waarin de vorm op de bladzijde meespeelt",
            "poëzie die enkel hardop voorgelezen mag worden",
            "poëzie die een schilderij beschrijft",
            "poëzie die in een museum gemaakt werd",
        ],
        antwoord=0,
        uitleg="De woorden vormen samen een beeld, of de plaatsing op de bladzijde draagt zelf betekenis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen worden vooral mondeling of op een podium gebracht?",
        opties=[
            "slampoetry",
            "het minnelied",
            "de ballade",
            "typografische poëzie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Typografische poëzie moet je net zien staan. De drie andere leven van de stem en het publiek.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een strofe van vier verzen? Antwoord met één woord.",
        antwoord=["kwatrijn"],
        uitleg="Kwatrijn komt van vier. Het is de meest voorkomende strofe in de Nederlandse poëzie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een distichon is een strofe van drie verzen.",
        antwoord=False,
        uitleg="Een distichon telt er twee. Drie verzen heet een terzet of een terzine.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel verzen telt een octaaf?",
        opties=[
            "acht",
            "zes",
            "zeven",
            "vijf",
        ],
        antwoord=0,
        uitleg="Een octaaf of octet is de strofe van acht verzen waarmee een sonnet vaak opent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke strofen horen bij hun aantal verzen?",
        opties=[
            "kwintet is vijf",
            "sextet is zes",
            "septet is zeven",
            "terzine is vier",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een terzine telt drie verzen, niet vier. Vier verzen is een kwatrijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Parlandopoëzie klinkt alsof iemand gewoon aan het praten is.",
        antwoord=True,
        uitleg="Parlando betekent sprekend. De toon is alledaags en de vorm valt nauwelijks op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een ballade?",
        opties=[
            "een verhalend gedicht, vaak met een refrein",
            "een gedicht van precies drie verzen",
            "een gedicht zonder enig rijm",
            "een gedicht dat een voorwerp beschrijft",
        ],
        antwoord=0,
        uitleg="Een ballade vertelt een verhaal op rijm, oorspronkelijk om te zingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een envoi?",
        opties=[
            "de korte slotstrofe met een opdracht",
            "de eerste strofe van een lang gedicht",
            "het terugkerende vers in een refrein",
            "de titel die boven het gedicht staat",
        ],
        antwoord=0,
        uitleg="Het envoi sluit een ballade of refrein af en richt zich vaak rechtstreeks tot iemand.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het vers dat in een refrein telkens terugkeert? Antwoord met één woord.",
        antwoord=["stok", "stokregel"],
        uitleg="De stok of stokregel sluit elke strofe van een refrein af.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dierendicht is een gedicht waarin dieren optreden of toegesproken worden.",
        antwoord=True,
        uitleg="De dieren kunnen er zichzelf zijn of een menselijk trekje belichamen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rondeel valt op doordat?",
        opties=[
            "bepaalde verzen letterlijk terugkeren",
            "er geen enkel rijmwoord in staat",
            "elk vers met dezelfde letter begint",
            "het altijd over de liefde gaat",
        ],
        antwoord=0,
        uitleg="Door de herhaling draait het gedicht rond zijn as, en krijgt dezelfde regel telkens een andere kleur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gedicht waarin een ridder zijn liefde bezingt voor een onbereikbare vrouw. Welke vorm is dat?",
        opties=[
            "het minnelied",
            "de elegie",
            "de hymne",
            "de limerick",
        ],
        antwoord=0,
        uitleg="Het minnelied komt uit de hoofse middeleeuwse traditie, waarin de verheven en onbereikbare liefde centraal staat.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is eindrijm?",
        opties=[
            "de laatste klanken van verzen die overeenkomen",
            "de beginletters van woorden die overeenkomen",
            "het aantal lettergrepen per vers",
            "de wending in het midden van een gedicht",
        ],
        antwoord=0,
        uitleg="Eindrijm hoor je aan het einde van de verzen. Beginletters die overeenkomen heet alliteratie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is alliteratie?",
        opties=[
            "dezelfde beginklank bij opeenvolgende woorden",
            "dezelfde eindklank bij opeenvolgende verzen",
            "dezelfde klinker midden in de woorden",
            "dezelfde zin die telkens herhaald wordt",
        ],
        antwoord=0,
        uitleg="Zeven zachte zuchten: de s en de z vooraan maken de regel hoorbaar. Alliteratie heet ook stafrijm.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je alliteratie met een ander woord? Antwoord met één woord.",
        antwoord=["stafrijm"],
        uitleg="De staf is de beginmedeklinker die terugkeert.",
    ),
    dict(
        type="waarofniet",
        vraag="Assonantie is rijm waarbij enkel de klinkers overeenkomen.",
        antwoord=True,
        uitleg="Haan en straat assoneren: de aa klinkt gelijk, de medeklinkers niet. Assonantie heet ook klinkerrijm of halfrijm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gedicht heeft het rijmschema abab. Hoe heet dat?",
        opties=[
            "gekruist rijm",
            "gepaard rijm",
            "omarmend rijm",
            "verspringend rijm",
        ],
        antwoord=0,
        uitleg="De rijmklanken kruisen elkaar: eerste met derde, tweede met vierde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rijmschema's horen bij hun naam?",
        opties=[
            "aabb is gepaard rijm",
            "abba is omarmend rijm",
            "abab is gekruist rijm",
            "aaaa is omarmend rijm",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij abba omarmt het eerste rijm het tweede. Vier dezelfde klanken na elkaar is geen omarmend rijm.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij mannelijk of staand rijm ligt de klemtoon op de laatste lettergreep.",
        antwoord=True,
        uitleg="Hand en land rijmen staand. Bij vrouwelijk of slepend rijm volgt er nog een doffe lettergreep, zoals in lopen en hopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een enjambement?",
        opties=[
            "een zin die over de versregel heen doorloopt",
            "een vers dat elders letterlijk herhaald wordt",
            "een strofe die uit twee verzen bestaat",
            "een wending halverwege het gedicht",
        ],
        antwoord=0,
        uitleg="De zin stopt niet waar het vers stopt. Dat geeft spanning en zet nadruk op het woord dat vooraan belandt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de volta in een sonnet?",
        opties=[
            "de wending in de gedachtegang",
            "de laatste strofe van het gedicht",
            "de maat waarin het geschreven is",
            "het terugkerende rijmwoord",
        ],
        antwoord=0,
        uitleg="Klassiek ligt de volta tussen het octaaf en het sextet: daar slaat het gedicht een andere richting in.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de wending in een gedicht met één woord? Antwoord met één woord.",
        antwoord=["volta", "wending"],
        uitleg="De volta is het scharnier van een sonnet.",
    ),
    dict(
        type="waarofniet",
        vraag="Het lyrisch subject is altijd de dichter zelf.",
        antwoord=False,
        uitleg="De ik in een gedicht is een rol, net als een personage in een roman. Soms valt hij samen met de dichter, maar dat hoeft niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een semantisch veld?",
        opties=[
            "een groep woorden rond hetzelfde betekenisgebied",
            "een strofe waarin alle woorden rijmen",
            "de witruimte rond een gedicht op de bladzijde",
            "een reeks verzen zonder leestekens",
        ],
        antwoord=0,
        uitleg="Zeil, anker, kiel, golf en kust horen tot hetzelfde veld. Wie zo'n veld opmerkt, ziet waar het gedicht naartoe wijst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met het ritme van een gedicht?",
        opties=[
            "de afwisseling van sterke en zwakke lettergrepen",
            "het aantal strofen waaruit het hele gedicht is opgebouwd",
            "de snelheid waarmee je het gedicht voorleest",
            "het rijmschema dat de dichter gekozen heeft",
        ],
        antwoord=0,
        uitleg="Het ritme hoor je als je het gedicht hardop leest: het patroon van sterke en zwakke lettergrepen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gedicht zonder rijm en zonder vaste maat bestaat niet.",
        antwoord=False,
        uitleg="Vrije verzen zijn er volop, zeker sinds de twintigste eeuw. Beeld, ritme en witruimte dragen dan de vorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een gedicht staat: 'de wind / draagt wat de bomen / niet meer houden'. Wat valt op aan de vorm?",
        opties=[
            "de zin loopt over de versgrenzen heen",
            "er is een strak rijmschema gebruikt",
            "er staan vier verzen in deze strofe",
            "elk vers begint met dezelfde klank",
        ],
        antwoord=0,
        uitleg="Dat is enjambement. Het woord dat net voor of net na de breuk staat, krijgt daardoor extra gewicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke begrippen gaan over klank in de poëzie?",
        opties=[
            "assonantie",
            "alliteratie",
            "volrijm",
            "enjambement",
        ],
        antwoord=[0, 1, 2],
        uitleg="Enjambement gaat over de bouw van de zin tegenover het vers, niet over klank. De drie andere zijn klankverschijnselen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je rijm waarbij klinker én medeklinkers overeenkomen, zoals in boom en stroom? Antwoord met één woord.",
        antwoord=["volrijm"],
        uitleg="Bij volrijm klinkt het hele rijmdeel gelijk, niet enkel de klinker.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rijmschema noteer je met letters, waarbij dezelfde letter dezelfde rijmklank aangeeft.",
        antwoord=True,
        uitleg="Zo staat abba voor vier verzen waarvan het eerste met het vierde rijmt en het tweede met het derde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig om een gedicht hardop te lezen?",
        opties=[
            "klank en ritme komen pas dan tot hun recht",
            "je leest het dan automatisch sneller uit",
            "je hoeft de woorden dan niet te begrijpen",
            "je ziet dan hoeveel strofen er zijn",
        ],
        antwoord=0,
        uitleg="Veel van wat een gedicht doet, zit in het geluid. Op papier hoor je dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een dichter zet één woord alleen op een regel, met veel wit eromheen. Wat bereikt zij daarmee?",
        opties=[
            "het woord krijgt alle aandacht",
            "het gedicht wordt daardoor langer",
            "het rijmschema verandert erdoor",
            "de strofe wordt een kwatrijn",
        ],
        antwoord=0,
        uitleg="Wit is in de poëzie geen leegte maar een middel. Wat alleen staat, weegt zwaarder.",
    ),
]
