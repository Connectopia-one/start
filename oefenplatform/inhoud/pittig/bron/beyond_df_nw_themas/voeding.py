"""Voedingsbestanddelen en etiketten — pittig (Beyond dubbele finaliteit, natuurwetenschappen).

Twee prentvragen over vetzuren uit natuurwetenschappen Beyond, verder eigen vragen binnen nwd_voeding."""
from ..beyond_nw_themas import biomoleculen as B
from ..beyond_bio_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(B.VRAGEN, [4, 13]) + [
    casus(
        "Op een doos ontbijtgranen staat per \\(100\\) g: energie \\(1600\\) kJ, vet \\(4\\) g waarvan verzadigd \\(1\\) g, koolhydraten \\(75\\) g waarvan suikers \\(30\\) g, "
        "vezels \\(5\\) g, eiwit \\(8\\) g, zout \\(0{,}6\\) g. De ingrediëntenlijst begint met: tarwebloem, suiker, maïs, ... (kan sporen van **noten** bevatten). Een kom bevat \\(40\\) g.",
        [
            inv("Hoeveel gram suiker eet je met één kom?", ["12", "12 g", "12 gram"], "\\(30 \\cdot 0{,}4 = 12\\) g."),
            inv("Hoeveel kilojoule levert één kom?", ["640", "640 kJ", "640 kilojoule"], "\\(1600 \\cdot 0{,}4 = 640\\) kJ."),
            mk("Wat leer je uit de volgorde van de ingrediënten?",
               ["Er zit meer tarwebloem in dan suiker.", "Er zit meer suiker in dan tarwebloem.", "Tarwebloem en suiker zitten er evenveel in.", "De volgorde zegt enkel iets over de smaak."], 0,
               "De lijst begint met wat er het meest in zit."),
            keuze("Iemand met een notenallergie eet deze granen [[*beter niet|gerust]].", "Sporen van noten kunnen al een reactie geven."),
            keuze("Welke voedingsstof levert in deze granen de meeste energie? [[*koolhydraten|vetten|eiwitten]]", "Vijfenzeventig gram koolhydraten tegenover vier gram vet en acht gram eiwit."),
        ],
    ),
    sorteer("Levert deze voedingsstof energie of niet?", ["levert energie", "levert geen energie"], [
        ["zetmeel", "levert energie"], ["olijfolie", "levert energie"], ["eiwit uit een ei", "levert energie"],
        ["water", "levert geen energie"], ["vitamine C", "levert geen energie"], ["calcium", "levert geen energie"],
    ], "Koolhydraten, vetten en eiwitten leveren kilojoules; water, mineralen en vitaminen niet."),
    koppel("Koppel elke voedingsstof aan een functie in het lichaam.", [
        ["eiwitten", "spieren en weefsels opbouwen en herstellen"], ["calcium", "botten en tanden stevig maken"],
        ["ijzer", "hemoglobine maken voor het zuurstofvervoer"], ["vetten", "energie opslaan en isoleren"],
    ], ["het bloed vloeibaarder maken"], "Elke voedingsstof heeft zijn eigen taak."),
    tabel("Snel of traag in het bloed?", [
        ("glucose", "Snel"), ("zetmeel uit volkorenpasta", "Traag"), ("fructose uit een appel", "Snel"), ("zetmeel uit aardappelen", "Traag"),
    ], "Losse suikermoleculen gaan meteen door; zetmeel moet eerst geknipt worden.", kolommen=["Snel", "Traag"]),
    mk("Een wielrenner moet om \\(15\\) uur een lange rit rijden. Wat is het beste plan?",
       ["om \\(12\\) uur pasta, tijdens de rit een banaan", "om \\(14{,}55\\) uur nog snel een groot bord pasta", "de hele dag niets, dan een cola om \\(15\\) uur", "om \\(12\\) uur enkel een glas water"], 0,
       "Zetmeel geeft traag energie voor de rit, fruit snel tijdens de rit."),
    mk("Waarom is olijfolie bij kamertemperatuur vloeibaar en boter vast?",
       ["Olijfolie bevat vooral onverzadigde vetzuren met een knik.", "Olijfolie bevat veel meer water dan boter, en water is altijd vloeibaar.", "Boter bevat vooral eiwitten in plaats van vet, en die stollen vanzelf.", "Olijfolie bevat geen enkel vetzuur."], 0,
       "Geknikte ketens stapelen minder dicht."),
    tabel("Klopt dit over water?", [
        ("Water levert geen kilojoules.", J),
        ("Zonder water verlopen de reacties in je cellen niet.", J),
        ("Water is een mineraal.", F),
    ], "Water is een eigen voedingsstof, zonder energie maar onmisbaar."),
    keuze("Een tekort aan [[*ijzer|calcium|vitamine C]] maakt je moe, omdat je bloed minder zuurstof vervoert.", "IJzer is nodig voor hemoglobine."),
    tabel("Klopt dit over vitaminen?", [
        ("Vitaminen leveren geen energie.", J),
        ("Je hebt er maar kleine hoeveelheden van nodig.", J),
        ("Hoe meer vitaminen, hoe beter, zonder bovengrens.", F),
    ], "Ook een nuttige stof kan in te grote hoeveelheid schaden."),
    volgorde("Zet deze producten van meest naar minst aanbevolen volgens de voedingsdriehoek.", [
        "water", "groenten", "volkorenbrood", "chips",
    ], "Water en plantaardige producten onderaan de driehoek, snacks bovenaan of erbuiten."),
    sleep("Op een etiket staan de ingrediënten [[van veel naar weinig]]. De [[allergenen]] staan in het vet. De energie staat meestal per [[honderd gram]].",
          ["van weinig naar veel", "vitaminen", "portie van één kilo"],
          "Zo kan je producten eerlijk vergelijken."),
    mk("Twee yoghurts: A heeft \\(12\\) g suiker per \\(100\\) g, B heeft \\(9\\) g suiker per potje van \\(125\\) g. Welke bevat per \\(100\\) g het minst suiker?",
       ["B, met \\(7{,}2\\) g per \\(100\\) g", "A, want \\(12\\) is een rond getal", "B, met \\(9\\) g per \\(100\\) g", "ze bevatten evenveel suiker"], 0,
       "\\(9 : 1{,}25 = 7{,}2\\) g per honderd gram."),
    inv("Een fles frisdrank van \\(1{,}5\\) L bevat \\(10\\) g suiker per \\(100\\) mL. Hoeveel gram suiker zit in de hele fles?", ["150", "150 g", "150 gram"],
        "Vijftien keer honderd milliliter, dus \\(15 \\cdot 10 = 150\\) g."),
    tabel("Telt dit mee in de nutriscore of in de ecoscore?", [
        ("veel zout", "Nutriscore"), ("de verpakking", "Ecoscore"), ("veel vezels", "Nutriscore"), ("het transport", "Ecoscore"), ("veel verzadigd vet", "Nutriscore"),
    ], "De nutriscore gaat over je gezondheid, de ecoscore over het milieu.", kolommen=["Nutriscore", "Ecoscore"]),
    mk("Chips met nutriscore C en chips met nutriscore D. Wat mag je besluiten?",
       ["De C-chips zijn iets minder ongezond dan de D-chips.", "De C-chips zijn even gezond als een appel of een peer.", "Je mag van de C-chips onbeperkt eten zonder enig probleem.", "De nutriscore zegt niets over chips."], 0,
       "De nutriscore vergelijkt binnen dezelfde productgroep."),
    keuze("Aardbeien in de winter uit een ver land krijgen meestal een [[*slechtere|betere]] ecoscore dan Belgische aardbeien in juni.", "Transport en verwarmde serres wegen door in de levenscyclus."),
    volgorde("Zet de stappen van de levenscyclus van een pak melk in de juiste volgorde.", [
        "koeien melken op de boerderij", "de melk verwerken en verpakken in de fabriek", "het pak vervoeren naar de winkel", "het pak uitdrinken thuis", "het lege pak in de pmd-zak",
    ], "De ecoscore kijkt naar die hele weg."),
    tabel("Klopt dit over allergenen?", [
        ("De wet verplicht de bekendste allergenen op het etiket te vermelden.", J),
        ("Een allergeen staat altijd achteraan de ingrediëntenlijst.", F),
        ("« Kan sporen bevatten » betekent dat het niet in het recept staat, maar er toch in kan zitten.", J),
    ], "Allergenen staan op hun plaats in de lijst, maar in het vet of met hoofdletters."),
    mk("Een sportdrank en een glas water: na een uur rustig wandelen. Wat is het verstandigst?",
       ["water, want je verbruikte weinig energie", "de sportdrank, want die heeft meer vitaminen", "allebei samen, voor het beste resultaat", "niets drinken, want je zweette nauwelijks"], 0,
       "Een sportdrank levert suiker die je na een rustige wandeling niet nodig hebt."),
    open_("Leg uit waarom je beter producten vergelijkt per honderd gram dan per verpakking.",
          "Verpakkingen zijn even groot noch even zwaar. Per honderd gram vergelijk je de samenstelling eerlijk.",
          "Een kleine verpakking lijkt anders minder suiker te bevatten, ook al is het product zoeter."),
    inv("Een reep chocolade van \\(50\\) g levert \\(2200\\) kJ per \\(100\\) g. Hoeveel kilojoule levert de hele reep?", ["1100", "1100 kJ", "1100 kilojoule"],
        "De helft van honderd gram, dus de helft van \\(2200\\)."),
    keuze("Brood, rijst en aardappelen zijn rijk aan [[*zetmeel|eiwit|vitamine D]].", "Het zijn de klassieke zetmeelbronnen."),
    tabel("Monosacharide of polysacharide?", [
        ("glucose", "Monosacharide"), ("zetmeel", "Polysacharide"), ("fructose", "Monosacharide"),
    ], "Mono is één suikermolecule, poly een lange keten.", kolommen=["Monosacharide", "Polysacharide"]),
    mk("Waarom kan je met een stuk fruit sneller een energiedip opvangen dan met een boterham?",
       ["Fruitsuiker hoeft niet eerst geknipt te worden.", "Fruit bevat per hap veel meer kilojoules dan brood.", "Brood bevat helemaal geen koolhydraten, alleen vezels.", "Fruit bevat vooral eiwitten en vetten."], 0,
       "Glucose en fructose gaan meteen in het bloed."),
]
