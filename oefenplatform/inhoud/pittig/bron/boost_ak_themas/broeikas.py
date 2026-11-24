"""Het versterkte broeikaseffect — pittig (🚀 Boost, aardrijkskunde).

Eigen vragen strikt binnen ak_broeikas, met een zelfgetekend schema van de
vier sferen om op te klikken. ALG geldt voor doorstroom en dubbele finaliteit;
DO_ALLEEN gaat over de stralingsbalans, het albedo en tropische ziektes (enkel doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, GRIJS, DONKER, LICHTGROEN, GROEN, ORANJE

SF = Prent("vier-sferen", "De vier sferen en de koolstof", "schema met lucht bovenaan, een bos, een oceaan, een fabriek en een ondergrondse laag met aardolie, met vijf letters")
SF.rect(0, 60, 1000, 220, "#e8f1fa", "none", 0, 0)
for x in (150, 330, 520, 760):
    SF.ellips(x, 120, 70, 26, "#ffffff", GRIJS, 1)
SF.rect(0, 280, 1000, 360, "#c9b48f", DONKER, 0, 1)
SF.rect(600, 280, 400, 140, "#7fb2d9", DONKER, 0, 1)
for x in range(60, 400, 60):
    SF.rect(x - 5, 230, 10, 50, "#7a5a3a", DONKER, 0, 1)
    SF.cirkel(x, 220, 28, GROEN, DONKER, 1)
SF.rect(430, 210, 90, 70, "#b9a1c9", DONKER, 0, 2)
SF.rect(495, 160, 16, 50, GRIJS, DONKER, 0, 1)
SF.pad("M 503 160 C 490 130 520 110 505 85", "none", GRIJS, 6)
SF.ellips(300, 520, 180, 45, "#2b2b2b", DONKER, 1)
SF.tekst(300, 527, "aardolie", 16, kleur="#ffffff")
SF.pijl(130, 160, 130, 195, DONKER, 3)
PUNTEN = {"A": (880, 110), "B": (180, 180), "C": (800, 350), "D": (520, 520), "E": (475, 245)}
for t, (x, y) in PUNTEN.items():
    SF.letter(x, y, t)
U = "vier-sferen.svg"
Z = {"A": Prent.zone(0, 60, 1000, 140), "B": Prent.zone(30, 180, 340, 100), "C": Prent.zone(600, 285, 400, 135),
     "D": Prent.zone(100, 440, 500, 160), "E": Prent.zone(420, 150, 110, 130)}
# A = atmosfeer, B = biosfeer (bos), C = hydrosfeer (oceaan), D = geosfeer (aardolie), E = fabriek die verbrandt

ALG = [
    klik("Klik op de sfeer waar koolstof miljoenen jaren als fossiele brandstof opgeslagen zit.", U, [Z["D"]],
         "Aardolie, steenkool en aardgas zitten in de geosfeer."),
    klik("Klik op de sfeer die bij fotosynthese koolstof uit de lucht opneemt.", U, [Z["B"]],
         "Planten halen CO₂ uit de atmosfeer: de koolstof gaat naar de biosfeer."),
    klik("Klik op de sfeer die een groot deel van de extra CO₂ en warmte opslorpt en daardoor verzuurt.", U, [Z["C"]],
         "De oceanen in de hydrosfeer nemen CO₂ op; het water wordt zuurder."),
    klik("Klik op de plaats waar koolstof uit de geosfeer snel naar de atmosfeer gaat.", U, [Z["E"]],
         "Bij het verbranden van fossiele brandstoffen komt CO₂ vrij."),
    koppel("Welke sfeer hoort bij welke omschrijving?",
           [("geosfeer", "gesteenten en bodem"), ("biosfeer", "alles wat leeft"), ("atmosfeer", "de lucht rond de aarde"), ("hydrosfeer", "oceanen, rivieren en ijs")],
           ["stratosfeer van de maan"], "Koolstof beweegt tussen die vier sferen."),
    sorteer("Komt er koolstof in de atmosfeer bij of gaat er uit?", ["komt erbij", "gaat eruit"],
            [("steenkool verbranden", "komt erbij"), ("een bos groeit", "gaat eruit"), ("een bos brandt af", "komt erbij"), ("de oceaan neemt CO₂ op", "gaat eruit"), ("een vulkaan barst uit", "komt erbij")],
            "Verbranding en vulkanen voegen toe; fotosynthese en oceanen halen weg."),
    tabel("Klopt dit over broeikasgassen?",
          [("Methaan komt onder meer van herkauwers en rijstvelden.", J), ("Lachgas komt in de landbouw vooral van bemesting.", J), ("Waterdamp is een broeikasgas.", J), ("Zuurstof is het belangrijkste broeikasgas.", F)],
          "Waterdamp, CO₂, methaan en lachgas zijn de broeikasgassen."),
    casus("Een grafiek toont de CO₂ in de lucht: 315 ppm in 1960, 370 ppm in 2000 en 420 ppm in 2023.", [
        inv("Met hoeveel ppm steeg de CO₂ tussen 1960 en 2023?", ["105", "105 ppm"],
            "420 − 315 = 105 ppm."),
        tabel("Klopt dit over de grafiek?",
              [("De stijging ging na 2000 sneller dan ervoor.", J), ("Je let eerst op de eenheid en de tijdas.", J), ("De grafiek bewijst dat elke zomer heter wordt.", F)],
              "50 ppm in 23 jaar tegenover 55 ppm in 40 jaar; een trend is geen bewijs voor elke zomer."),
        mk("Waar komt het grootste deel van die extra CO₂ vandaan?",
           ["fossiele brandstoffen verbranden", "de uitademing van alle mensen samen", "het verdampen van zeewater in de tropen", "de ademhaling van de bomen in het bos"], 0,
           "Steenkool, olie en gas verbranden geeft de meeste CO₂."),
    ]),
    tabel("Klopt dit over het broeikaseffect?",
          [("Zonder het natuurlijke broeikaseffect zou het op aarde ongeveer −18 °C zijn.", J), ("Het versterkte broeikaseffect komt van extra gassen door de mens.", J), ("We moeten het broeikaseffect volledig wegwerken.", F)],
          "Het natuurlijke effect maakt leven mogelijk; het versterkte doet de aarde opwarmen."),
    tabel("Klopt dit over de zeespiegel?",
          [("Warmer water zet uit.", J), ("Smeltend landijs doet de zeespiegel stijgen.", J), ("Smeltend drijvend zee-ijs doet de zeespiegel stijgen.", F), ("Delta's en lage eilanden lopen het grootste risico.", J)],
          "Drijvend ijs verplaatst al evenveel water als het smeltwater inneemt."),
    sorteer("Is dit weer of klimaat?", ["weer", "klimaat"],
            [("een hittegolf vorige week", "weer"), ("de gemiddelde temperatuur over dertig jaar", "klimaat"), ("een storm morgen", "weer"), ("steeds drogere zomers sinds 1990", "klimaat")],
            "Weer is vandaag, klimaat is het gemiddelde over lange tijd."),
    mk("In welke richting schuiven klimaatzones door de opwarming?",
       ["naar de polen en de bergen op", "naar de evenaar en de bergen af", "ze blijven waar ze altijd lagen", "enkel naar het westen van elk continent"], 0,
       "Warmere zones schuiven op naar hogere breedte en hoogte."),
    tabel("Welke gevolgen heeft het versterkte broeikaseffect?",
          [("langere droogtes", J), ("hevigere buien", J), ("verlies aan biodiversiteit", J), ("meer zee-ijs in de zomer", F)],
          "Soorten schuiven mee of verdwijnen; het weer wordt extremer."),
    casus("In de toendra van Siberië dooit de bevroren bodem steeds dieper.", [
        inv("Hoe noem je bodem die het hele jaar bevroren is?", ["permafrost", "de permafrost"],
            "Permafrost bevat veel oude koolstof."),
        tabel("Klopt dit over de dooiende permafrost?",
              [("Bij het dooien komen methaan en CO₂ vrij.", J), ("Dat versterkt de opwarming zelf.", J), ("Dat is een terugkoppeling.", J), ("Het verzwakt de opwarming.", F)],
              "Een gevolg dat zijn eigen oorzaak versterkt, is een terugkoppeling."),
    ]),
    tabel("Klopt dit over de verdeling van de gevolgen?",
          [("Ligging, reliëf en welvaart bepalen hoe kwetsbaar een land is.", J), ("Landen met de hoogste uitstoot worden altijd het hardst getroffen.", F), ("Een arm laaggelegen land kan zich moeilijker beschermen.", J)],
          "Wie het minst uitstoot, lijdt soms het meest."),
    sleep("Bij [[fotosynthese]] gaat koolstof van de atmosfeer naar de biosfeer. Bij [[verbranding]] van fossiele brandstoffen gaat ze van de geosfeer naar de atmosfeer. Opgenomen CO₂ maakt de oceaan [[zuurder]].",
          ["verdamping", "zouter"], "De koolstofcyclus verbindt de vier sferen."),
    keuze("Voor Vlaanderen betekent de opwarming [[*zowel meer droogte als meer hevige buien|enkel meer regen|geen enkele verandering]].",
          "Water wordt zowel te veel als te weinig."),
    inv("Wat is de scheikundige formule van koolstofdioxide?", ["CO2", "co2", "CO₂"],
        "Eén koolstofatoom en twee zuurstofatomen."),
    klik("Klik op de sfeer waar de broeikasgassen de warmte vasthouden.", U, [Z["A"]],
         "De broeikasgassen zitten in de atmosfeer."),
    mk("Het aardoppervlak straalt 's nachts warmte uit. Wat doen de broeikasgassen daarmee?",
       ["Ze houden een deel ervan vast.", "Ze sturen alle warmte naar de zon terug.", "Ze zetten de warmte om in zuurstof.", "Ze laten alle warmte meteen ontsnappen."], 0,
       "Zonlicht komt binnen, maar een deel van de uitgestraalde warmte blijft hangen."),
    sorteer("Uit welke bron komt dit broeikasgas vooral?", ["koolstofdioxide", "methaan", "lachgas"],
            [("auto's en centrales", "koolstofdioxide"), ("koeien en schapen", "methaan"), ("bemeste akkers", "lachgas"), ("rijstvelden onder water", "methaan"), ("ontbossing door brand", "koolstofdioxide")],
            "Elk gas heeft zijn eigen grote bronnen."),
    tabel("Hoe weet men dat de CO₂ in de lucht al decennia stijgt?",
          [("metingen op weerstations zoals op Hawaï", J), ("luchtbelletjes in oud ijs", J), ("één warme dag in juli", F)],
          "Lange meetreeksen en ijskernen tonen de trend."),
    inv("Een land stoot 12 ton CO₂ per inwoner uit, een ander 2 ton. Hoeveel keer meer is dat?", ["6", "6 keer", "zes"],
        "12 / 2 = 6: per inwoner verschilt de uitstoot sterk."),
]

DO_ALLEEN = [
    tabel("Klopt dit over albedo en stralingsbalans?",
          [("Verse sneeuw heeft een hoog albedo.", J), ("Een donkere oceaan kaatst veel straling terug.", F), ("De stralingsbalans vergelijkt binnenkomende en uitgaande straling.", J)],
          "Wit kaatst terug, donker slorpt op."),
    volgorde("Rangschik van hoogste naar laagste albedo.",
             ["verse sneeuw", "zand in de woestijn", "een groen bos", "een donkere oceaan"],
             "Hoe lichter het oppervlak, hoe meer het terugkaatst."),
    mk("Zee-ijs smelt en er komt donker water bloot. Wat gebeurt er?",
       ["het albedo daalt en het warmt op", "het albedo stijgt en het wordt daar kouder", "er verandert niets aan de opname van warmte", "het water kaatst nu alle straling terug"], 0,
       "Minder ijs betekent een lager albedo en meer opwarming: een terugkoppeling."),
    tabel("Waarom kunnen tropische ziektes zich naar onze streken uitbreiden?",
          [("De muggen die ze overbrengen, overleven hier steeds beter.", J), ("Warmere winters doden minder muggen.", J), ("Ziektes worden door koude verspreid.", F)],
          "Een warmer klimaat verschuift ook het leefgebied van muggen."),
]

DF_ALLEEN = [
    volgorde("Rangschik de reis van koolstof in een stuk steenkool.",
             ["Een plant neemt CO₂ op uit de lucht.", "De plant sterft en wordt bedolven.", "Na miljoenen jaren wordt ze steenkool in de bodem.", "De steenkool wordt verbrand en CO₂ komt in de lucht."],
             "Biosfeer, geosfeer en weer atmosfeer."),
    mk("In welke sfeer zit het ijs van een gletsjer?",
       ["de hydrosfeer", "de geosfeer", "de biosfeer", "de atmosfeer boven het ijs"], 0,
       "Al het water, ook ijs, hoort bij de hydrosfeer."),
    tabel("Klopt dit over de koolstofcyclus?",
          [("Koolstof blijft voorgoed in één sfeer.", F), ("Een boom slaat koolstof op tot hij vergaat of brandt.", J), ("Vulkanen brengen koolstof uit de geosfeer naar de lucht.", J)],
          "Koolstof beweegt voortdurend tussen de sferen."),
    keuze("Het natuurlijke broeikaseffect is [[*nodig voor leven|altijd schadelijk|door de mens gemaakt]].",
          "Zonder zou het gemiddeld ver onder nul zijn."),
]

VRAGEN = ALG + DO_ALLEEN
VRAGEN_DF = ALG + DF_ALLEEN
