"""Kunstanalyse en kunstreflectie — pittig (🌍 Beyond doorstroom,
kunstbeschouwing en filosofie). Strikt binnen beyond/bron/kfb_analyse.py:
de richtvragen (hoe en waarmee, wat, waarvoor, wie waar en wanneer), de
samenhang, de factoren die een interpretatie beïnvloeden en de perspectieven
(persoonlijk, critici, groot publiek, musea en galerieën, economisch)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, BLAUW, ORANJE, GEEL, ROOD

# Prent: vijf manieren om naar een werk te kijken ----------------------------------
PE = Prent("vijf-blikken", "Wie kijkt er naar het kunstwerk?",
           "in het midden een schilderij; rondom vijf tekeningen: A één persoon met een hartje, B een krant met een recensie, C een museumgebouw met zuilen, D een veilinghamer met een prijs, E een grote groep mensen met telefoons")
PLEK = {}
PE.rect(400, 230, 200, 160, "#fbfaf5", DONKER, 4, 4)
PE.rect(415, 245, 170, 130, LICHTGROEN, DONKER, 0, 2)
PE.pad("M 415 375 L 470 300 L 510 340 L 545 290 L 585 375 Z", "#7fae6b", DONKER, 2)
PE.cirkel(550, 270, 14, GEEL, DONKER, 2)


def plek(letter, x, y, b=190, h=150):
    PE.rect(x, y, b, h, "#ffffff", DONKER, 12, 2)
    PE.letter(x + 24, y + 24, letter)
    PLEK[letter] = (x, y, b, h)


plek("A", 40, 60)
PE.cirkel(135, 115, 22, "#f1d9b5", DONKER, 2)
PE.pad("M 100 190 Q 135 140 170 190 Z", BLAUW, DONKER, 2)
PE.pad("M 185 95 c -6 -12 -24 -6 -16 8 l 16 14 l 16 -14 c 8 -14 -10 -20 -16 -8 Z", ROOD, ROOD, 1)
plek("B", 770, 60)
PE.rect(825, 95, 120, 100, "#f4f1e8", DONKER, 2, 2)
PE.rect(833, 104, 104, 16, DONKER, DONKER, 0, 0)
for i in range(5):
    PE.lijn(835, 134 + i * 12, 935 - (i % 2) * 30, 134 + i * 12, GRIJS, 3)
PE.tekst(885, 117, "★★☆☆☆", 13, kleur="#ffffff")
plek("C", 40, 430)
PE.pad("M 75 500 L 135 465 L 195 500 Z", "#e9e2cf", DONKER, 2)
for x in (85, 110, 135, 160, 185):
    PE.rect(x - 5, 505, 10, 50, "#e9e2cf", DONKER, 0, 2)
PE.rect(72, 555, 126, 10, "#e9e2cf", DONKER, 0, 2)
plek("D", 770, 430)
PE.rect(820, 515, 80, 18, "#8a6d4b", DONKER, 3, 2)
PE.pad("M 870 515 L 905 470", "none", DONKER, 6)
PE.rect(880, 455, 50, 24, "#8a6d4b", DONKER, 3, 2)
PE.tekst(880, 565, "€ 2 000 000", 18, vet=True)
plek("E", 405, 440, 190, 160)
for i in range(4):
    for j in range(2):
        x, y = 450 + i * 32, 500 + j * 45
        PE.cirkel(x, y, 12, "#f1d9b5", DONKER, 1)
        PE.rect(x + 6, y - 22, 9, 14, DONKER, DONKER, 2, 1)
for x1, y1, x2, y2 in ((230, 160, 400, 260), (770, 160, 600, 260), (230, 490, 400, 370), (770, 490, 600, 370), (500, 440, 500, 395)):
    PE.pijl(x1, y1, x2, y2, GRIJS, 3)


def pz(l):
    return [Prent.zone(*PLEK[l])]


VRAGEN = [
    klik("Een recensent schrijft dat het werk technisch sterk is, maar inhoudelijk oppervlakkig. Klik op dat perspectief.", PE.bestand, pz("B"),
         "Kunstcritici analyseren en beoordelen een werk in kranten en tijdschriften."),
    klik("Klik op het economisch perspectief.", PE.bestand, pz("D"),
         "Het economisch perspectief kijkt naar waarde, verkoop en de invloed op de kunstmarkt."),
    klik("Klik op het perspectief dat de subjectieve ervaring van één kijker toont.", PE.bestand, pz("A"),
         "Het persoonlijk perspectief gaat over je eigen gevoel en herinneringen bij een werk."),
    met_prent(PE.bestand, keuze("Vak C staat voor het perspectief van [[*musea en galerieën|de kunstcritici|het grote publiek]]. Vak E staat voor het perspectief van [[*het grote publiek|de musea|de veiling]].",
              "Musea bepalen mee wat als belangrijk geldt. Het publiek reageert met massa's tegelijk.")),
    met_prent(PE.bestand, tabel("Hoort dit vak bij het persoonlijk perspectief of bij het derde persoonsperspectief?", [
        ("vak A", "persoonlijk"),
        ("vak B", "derde persoon"),
        ("vak C", "derde persoon"),
        ("vak E", "derde persoon"),
    ], "Critici, publiek en musea horen bij het derde persoonsperspectief, de meer objectieve observatie. Het economisch perspectief is een apart perspectief.",
       kolommen=["persoonlijk", "derde persoon"])),
    sorteer("Welke richtvraag beantwoord je?", ["hoe en waarmee?", "wat?", "waarvoor?", "wie, waar en wanneer?"], [
        ["olieverf op doek, dikke toetsen", "hoe en waarmee?"],
        ["een moeder met een kind in een keuken", "wat?"],
        ["om gelovigen het verhaal uit te leggen", "waarvoor?"],
        ["geschilderd in 1937 in Parijs", "wie, waar en wanneer?"],
        ["trage maat, lage tonen, mineur", "hoe en waarmee?"],
        ["om mensen te overtuigen soldaat te worden", "waarvoor?"],
    ], "Middelen van vormgeving, inhoud, functie en context: de vier richtvragen."),
    koppel("Koppel de beïnvloedende factor aan het voorbeeld.", [
        ["tijd en ruimte", "een werk dat in 1863 schokte, is nu een meesterwerk"],
        ["veranderende kennis en technologie", "een röntgenfoto toont een ouder schilderij eronder"],
        ["modetrends", "een vergeten stijl wordt plots weer populair"],
        ["persoonlijk referentiekader", "een pianist hoort meer in een concert"],
    ], ["het merk van de lamp in het museum"], "Dat zijn de vier factoren die een interpretatie beïnvloeden."),
    tabel("Klopt dit over de kunstanalyse?", [
        ("Je begint best met beschrijven wat je ziet, nog zonder oordeel.", J),
        ("De richtvragen werken ook voor dans, muziek en film.", J),
        ("Het materiaal van een beeld heeft geen invloed op hoe je het ervaart.", F),
        ("In een goede analyse kijk je nooit naar de tijd waarin het werk ontstond.", F),
    ], "Eerst beschrijven, dan analyseren en interpreteren. De context hoort er altijd bij."),
    casus(
        "In een museum hangt een groot schilderij uit 1937. Het is enkel in zwart, wit en grijs. Je ziet gebroken lichamen, een schreeuwend paard, "
        "een moeder met een dood kind en een lamp die fel brandt. De schilder maakte het na het bombardement op een Spaans stadje, voor een wereldtentoonstelling in Parijs.",
        [
            tabel("Bij welke richtvraag hoort dit?", [
                ("enkel zwart, wit en grijs", "hoe en waarmee?"),
                ("een moeder met een dood kind", "wat?"),
                ("de gruwel van een bombardement aanklagen", "waarvoor?"),
                ("1937, Parijs, de Spaanse Burgeroorlog", "wie, waar en wanneer?"),
            ], "Zo beantwoord je de vier richtvragen bij één werk.",
               kolommen=["hoe en waarmee?", "wat?", "waarvoor?", "wie, waar en wanneer?"]),
            mk("Welke uitspraak toont de samenhang tussen de vier richtvragen?",
               ["een oorlog leidt tot een aanklacht in grijze tinten", "de kleuren zijn toevallig gekozen en zeggen niets",
                "de grootte van het doek bepaalt de prijs op een veiling", "het werk is mooi omdat het in een museum hangt"], 0,
               "Context (oorlog), functie (aanklacht) en vormgeving (geen kleur, gebroken vormen) horen samen."),
            keuze("Een bezoeker die zelf een oorlog meemaakte, voelt bij dit werk iets anders dan een andere bezoeker. Dat komt door het [[*persoonlijk referentiekader|economisch perspectief|perspectief van de critici]].",
                  "Je eigen ervaringen kleuren hoe je een werk ziet."),
        ],
    ),
    mk("Een werk van Van Gogh verkocht bijna niet tijdens zijn leven. Vandaag staan er lange rijen. Wat toont dit?",
       ["waardering verandert met de tijd", "Van Gogh schilderde zijn werken na zijn dood opnieuw",
        "zijn werken waren vroeger veel kleiner dan nu", "onverkochte kunst blijft altijd onbekend"], 0,
       "Critici, musea en publiek veranderen samen hoe een werk gewaardeerd wordt."),
    mk("Een bericht over een kunstwerk gaat viraal en duizenden mensen gaan het zien. Welk perspectief speelt hier vooral?",
       ["het grote publiek", "de kunstcritici in de krant", "het persoonlijk perspectief van één kijker", "de opdrachtgever van het werk"], 0,
       "De reactie van heel veel mensen samen bepaalt hier de aandacht."),
    tabel("Klopt dit over interpretatie?", [
        ("Twee mensen kunnen hetzelfde werk heel anders interpreteren.", J),
        ("De betekenis van een werk ligt voor altijd vast.", F),
        ("Een hoge veilingprijs bewijst dat een werk het mooiste van zijn tijd is.", F),
        ("Het publiek kan een werk bekend maken, ook als critici het minder goed vinden.", J),
    ], "Interpretatie en waardering zijn niet vast en hangen af van wie kijkt."),
    sleep("Bij een beeld stel je de vraag of het [[gehouwen]], gegoten of geboetseerd is: dat hoort bij de [[techniek]].",
          ["onderwerp", "functie"], "Bij beeldhouwkunst kun je wegnemen, toevoegen, gieten of samenvoegen."),
    volgorde("Zet de stappen van een kunstanalyse in een logische volgorde.", [
        "goed kijken en beschrijven wat je ziet",
        "de middelen van vormgeving analyseren",
        "de functie en de context zoeken",
        "de samenhang uitleggen en je eigen oordeel onderbouwen",
    ], "Van beschrijven naar analyseren, interpreteren en pas op het einde oordelen."),
    mk("Een affiche uit 1914 toont een soldaat die naar de kijker wijst: 'Jouw land heeft je nodig'. Welke functie heeft dit werk?",
       ["politiek", "decoratief, om een kamer te versieren", "religieus, om het geloof uit te leggen", "ontspannend, om de kijker te laten lachen"], 0,
       "Propaganda wil overtuigen. De wijzende vinger spreekt de kijker rechtstreeks aan."),
    keuze("Een museum hangt een onbekende kunstenaar in zijn grootste zaal. Daardoor lijkt het werk meteen [[*belangrijker|minder waard|ouder]]. Dat toont de invloed van [[*musea en galerieën|het persoonlijk referentiekader|modetrends]].",
          "Wat musea tonen of kopen, krijgt meer aandacht en waardering."),
    inv("Hoe heet alles wat je meebrengt als kijker: je ervaringen, je opvoeding, je kennis en je smaak? Je persoonlijk ...", ["referentiekader"],
        "Het referentiekader kleurt hoe je een werk ziet."),
    tabel("Welk perspectief spreekt hier?", [
        ("'Dit werk maakt me rustig, het doet me denken aan de zee.'", "persoonlijk"),
        ("'De verkoop van deze kunstenaar is in een jaar verdrievoudigd.'", "economisch"),
        ("'De compositie is sterk, maar de kleuren zijn vlak.'", "criticus"),
    ], "Persoonlijk gevoel, marktwaarde en een onderbouwd oordeel zijn drie verschillende perspectieven.",
       kolommen=["persoonlijk", "economisch", "criticus"]),
    mk("Waarom is het nuttig om vanuit meerdere perspectieven over een werk na te denken?",
       ["de betekenis hangt niet van één mening af", "zo bewijs je dat jouw mening de enige juiste is",
        "dan hoef je zelf niet meer naar het werk te kijken", "zo ken je meteen de veilingprijs van het werk"], 0,
       "Door perspectieven te vergelijken, onderbouw je je eigen mening beter."),
    keuze("Bij muziek zijn tempo en klankkleur antwoorden op de richtvraag [[*hoe en waarmee?|waarvoor?|wie, waar en wanneer?]]. Of het lied voor een begrafenis geschreven werd, hoort bij [[*waarvoor?|hoe en waarmee?|wat?]].",
          "Bouwstenen horen bij hoe en waarmee, het doel bij waarvoor."),
    mk("Je noteert bij een beeld: koud, glad wit marmer. Welke richtvraag beantwoord je?",
       ["hoe en waarmee?", "wat?", "waarvoor?", "wie, waar en wanneer?"], 0,
       "Het materiaal is een middel van vormgeving."),
    mk("Een kunsthistoricus leest in een brief van de schilder wat hij met een werk bedoelde. Welke factor kan de interpretatie dan veranderen?",
       ["veranderende kennis", "modetrends in de kunstmarkt", "het persoonlijk referentiekader van de schilder", "de prijs van het ticket"], 0,
       "Nieuwe kennis over een werk kan de manier veranderen waarop we het begrijpen."),
    tabel("Is dit een beschrijving of al een oordeel?", [
        ("Op de voorgrond staan drie figuren in een driehoek.", "beschrijving"),
        ("Dit is het mooiste schilderij van de zaal.", "oordeel"),
        ("De achtergrond is donker, het licht valt van links.", "beschrijving"),
        ("De kleuren zijn lelijk gekozen.", "oordeel"),
    ], "In een analyse beschrijf je eerst, zonder oordeel. Een oordeel onderbouw je op het einde.",
       kolommen=["beschrijving", "oordeel"]),
    keuze("Een kunstwerk uit Japan wordt in België anders begrepen dan in Japan. Dat komt door de factor [[*tijd en ruimte|modetrends|technologie]]. Een kijker die Japans leerde, begrijpt de tekens op het werk wel, door zijn [[*persoonlijk referentiekader|economisch perspectief|museum]].",
          "Plaats en eigen kennis beïnvloeden allebei de interpretatie."),
    mk("Welke vraag hoort bij de richtvraag wie, waar en wanneer?",
       ["in welke stad en eeuw ontstond het werk?", "met welke kleuren is het werk geschilderd?",
        "wat stelt het werk precies voor?", "waarvoor werd het werk gemaakt?"], 0,
       "Wie, waar en wanneer is de context."),
    tabel("Klopt dit over het economisch perspectief?", [
        ("Een hoge veilingprijs kan de vraag naar werk van dezelfde kunstenaar doen stijgen.", J),
        ("Het economisch perspectief kijkt naar waarde, verkoop en marktimpact.", J),
        ("Het economisch perspectief is hetzelfde als je eigen gevoel bij een werk.", F),
    ], "Het economisch perspectief staat naast het persoonlijke en het derde persoonsperspectief."),
    mk("Een dansvoorstelling: dansers bewegen traag en raken elkaar telkens even aan, onder blauw licht. Welke richtvraag beantwoord je met die zin?",
       ["hoe en waarmee?", "waarvoor?", "wie, waar en wanneer?", "wat is de prijs?"], 0,
       "Tempo, relatie en licht zijn middelen van vormgeving."),
    open_("Kies een kunstwerk en leg uit hoe de interpretatie ervan kan veranderen door de tijd en door nieuwe technologie.",
          "Een schilderij dat vroeger schokkend gevonden werd, zoals een naakt in een gewone omgeving, lijkt vandaag minder vreemd. De tijd veranderde wat mensen gewoon vinden. Nieuwe technologie, zoals röntgenfoto's, kan tonen dat de schilder iets overschilderde. Daardoor begrijpen we beter hoe hij werkte en wat hij bedoelde."),
]
