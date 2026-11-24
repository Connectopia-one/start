"""Een geografisch onderzoek voeren — pittig (🚀 Boost, aardrijkskunde).

Eigen vragen strikt binnen ak_onderzoek, met een zelfgetekend scherm van een
digitale kaart om op te klikken. Dezelfde vragen voor doorstroom en dubbele finaliteit."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, GRIJS, DONKER, LICHTGROEN, ORANJE

SCH = Prent("digitale-kaart", "Scherm van een digitale kaart", "venster van een digitale kaart met een zoekbalk, een knop voor lagen, een meetlat, een schuifje voor transparantie en een legende, elk met een letter")
SCH.rect(20, 60, 960, 560, "#ffffff", DONKER, 8, 2)
SCH.rect(20, 60, 960, 60, "#eef1f4", DONKER, 8, 1)
SCH.rect(50, 75, 360, 32, "#ffffff", DONKER, 6, 1)
SCH.tekst(65, 97, "Zoek een adres of coördinaten ...", 15, "start", GRIJS)
SCH.rect(440, 75, 110, 32, "#dde6ee", DONKER, 6, 1)
SCH.tekst(495, 97, "Lagen", 16)
SCH.rect(570, 75, 50, 32, "#dde6ee", DONKER, 6, 1)
SCH.lijn(580, 98, 610, 84, DONKER, 3)
for i in range(5):
    SCH.lijn(583 + i * 6, 95 - i * 3, 585 + i * 6, 99 - i * 3, DONKER, 1)
SCH.rect(40, 140, 700, 460, "#e6efd9", DONKER, 0, 1)
SCH.pad("M 40 400 C 200 360 350 450 520 380 C 620 340 680 380 740 360", "none", BLAUW, 10)
SCH.pad("M 380 360 L 520 330 L 600 380 L 520 450 L 400 440 Z", "#7fb2d9", BLAUW, 1)
for x, y in [(150, 220), (190, 250), (230, 210), (600, 210), (640, 240)]:
    SCH.rect(x, y, 26, 22, "#c9a27a", DONKER, 2, 1)
SCH.rect(760, 140, 200, 120, "#f6f6f6", DONKER, 6, 1)
SCH.tekst(775, 165, "Transparantie", 15, "start")
SCH.lijn(780, 200, 940, 200, GRIJS, 6)
SCH.cirkel(880, 200, 12, ORANJE, DONKER, 1)
SCH.rect(760, 290, 200, 200, "#f6f6f6", DONKER, 6, 1)
SCH.tekst(775, 315, "Legende", 15, "start", vet=True)
SCH.rect(780, 335, 26, 18, "#7fb2d9", DONKER, 0, 1)
SCH.tekst(815, 350, "overstromings-", 14, "start")
SCH.tekst(815, 368, "gevoelig gebied", 14, "start")
SCH.rect(780, 390, 26, 18, "#c9a27a", DONKER, 0, 1)
SCH.tekst(815, 405, "gebouw", 14, "start")
PUNTEN = {"A": (230, 140), "B": (495, 140), "C": (595, 140), "D": (860, 240), "E": (930, 470)}
for t, (x, y) in PUNTEN.items():
    SCH.letter(x, y, t)
U = "digitale-kaart.svg"
Z = {"A": Prent.zone(45, 70, 370, 90), "B": Prent.zone(435, 70, 120, 90), "C": Prent.zone(565, 70, 60, 90),
     "D": Prent.zone(760, 140, 200, 120), "E": Prent.zone(760, 290, 200, 200)}

VRAGEN = [
    klik("Klik op het gereedschap waarmee je de oppervlakte van een bedrijventerrein meet.", U, [Z["C"]],
         "Met het meetgereedschap bepaal je afstanden en oppervlakten."),
    klik("Klik op wat je gebruikt om een adres in je gemeente op de kaart te vinden.", U, [Z["A"]],
         "De zoekbalk brengt je naar een adres of coördinaten."),
    klik("Klik op het onderdeel waarmee je twee lagen tegelijk zichtbaar maakt, zodat je de onderste laag doorheen de bovenste ziet.", U, [Z["D"]],
         "Met de transparantie zie je een thematische laag en een luchtfoto samen."),
    klik("Klik op het onderdeel dat uitlegt wat de blauwe vlakken betekenen.", U, [Z["E"]],
         "De legende verklaart kleuren en symbolen."),
    klik("Klik op de knop waarmee je een laag met luchtfoto's van 1971 kan aanzetten.", U, [Z["B"]],
         "Bij de lagen kies je welke kaarten zichtbaar zijn."),
    casus("Lotte onderzoekt waarom het in haar gemeente elke ochtend file staat aan de schoolpoort.", [
        volgorde("Rangschik de stappen van haar onderzoek.",
                 ["een onderzoeksvraag en een hypothese opschrijven", "bronnen en terreingegevens verzamelen", "de gegevens verwerken in een schema", "een besluit trekken en de beperkingen noemen"],
                 "Vraag, gegevens, verwerking, besluit."),
        tabel("Klopt dit over haar hypothese?",
              [("Ze schrijft die op vóór ze meet.", J), ("Haar onderzoek mislukt als de hypothese fout blijkt.", F), ("Een hypothese is een verwachting die je toetst.", J)],
              "Een weerlegde hypothese leert ook iets."),
        tabel("Welke gegevens passen bij haar vraag?",
              [("het aantal auto's per kwartier", J), ("waar de kinderen wonen", J), ("de luchtkwaliteit aan de poort", J), ("het klimatogram van Brazilië", F)],
              "Mobiliteit gaat over verkeer, afstand en hinder."),
    ]),
    sorteer("Over welk onderzoeksthema gaat deze vraag?", ["mobiliteit", "water", "landgebruik", "klimaatverandering"],
            [("Waarom staat het elke ochtend vast op de ring?", "mobiliteit"), ("Welke straten lopen onder bij hevige regen?", "water"), ("Hoeveel akkerland werd sinds 1970 bebouwd?", "landgebruik"), ("Worden de zomers in onze stad heter?", "klimaatverandering"), ("Is er genoeg grondwater voor de landbouw?", "water")],
            "Mobiliteit, water, veranderend landgebruik en klimaatverandering zijn de vier thema's."),
    tabel("Welke onderzoeksvraag is goed geformuleerd?",
          [("Hoeveel hectare open ruimte verdween in onze gemeente tussen 2000 en 2020?", J), ("Is aardrijkskunde leuk?", F), ("Waarom loopt de Demerstraat bij hevige regen onder water?", J)],
          "Een goede vraag is concreet, afgebakend en te onderzoeken."),
    tabel("Klopt dit over terreinwerk?",
          [("Bij terreinkartering noteer je op een kaart wat je waar ziet.", J), ("Terreinwerk verandert je mentale kaart van een gebied.", J), ("Een filmpje van een terreinoefening moet je net zo nauwkeurig bekijken als echt terreinwerk.", J), ("Wat je op het terrein ziet, hoef je niet te noteren.", F)],
          "Waarnemen, noteren en verwerken."),
    casus("Je onderzoekt of de open ruimte in je gemeente kleiner werd.", [
        mk("Welke aanpak past het best?",
           ["luchtfoto's van vroeger en nu vergelijken", "één luchtfoto van vandaag bekijken", "een hypothese pas achteraf opschrijven", "de inwoners vragen naar hun lievelingskleur"], 0,
           "Enkel door jaren te vergelijken zie je wat veranderde."),
        inv("Op de foto van 1990 is 600 ha open, nu nog 450 ha. Hoeveel procent ging verloren?", ["25", "25 %"],
            "150 / 600 = 25 %."),
        tabel("Wat noteer je bij elke luchtfoto?",
              [("het jaartal", J), ("de bron", J), ("je eigen mening over het landschap", F)],
              "Zonder jaartal en bron is de vergelijking niet te controleren."),
    ]),
    tabel("Welke beperkingen heeft een digitale kaart?",
          [("Sommige lagen zijn ouder dan ze lijken.", J), ("Wat je ziet, hangt af van de lagen die je aanzet.", J), ("Een luchtfoto toont altijd de toestand van vandaag.", F)],
          "Kijk telkens na wanneer een laag gemaakt werd."),
    koppel("Welke bron gebruik je voor welke vraag?",
           [("de neerslag van de voorbije dertig jaar", "een klimatogram of meetreeks"), ("de oppervlakte van een bedrijventerrein", "het meetgereedschap van een digitale kaart"), ("welke huizen in overstromingsgebied liggen", "een overstromingslaag over een luchtfoto"), ("hoe bewoners hun wijk zien", "een mentale kaart of een bevraging")],
           ["een kaart van de wereldblokken"], "Kies de bron die bij je vraag past."),
    tabel("Klopt dit over een systeemdenkschema?",
          [("Het toont hoe de elementen van je onderzoek samenhangen.", J), ("Pijlen tonen oorzaken en gevolgen.", J), ("Het vervangt je onderzoeksvraag.", F)],
          "Het schema verbindt neerslag, verharding, riolering en bewoners bijvoorbeeld."),
    sorteer("Hoort dit element in een schema over wateroverlast?", ["ja", "nee"],
            [("hevige neerslag", "ja"), ("verharding", "ja"), ("de capaciteit van de riolering", "ja"), ("het aantal toeristen in de Alpen", "nee"), ("de ligging in een vallei", "ja")],
            "Kies de elementen die het probleem verklaren."),
    mk("Je besluit dat de files toenemen. Waarop moet dat besluit steunen?",
       ["op je gegevens en metingen", "op wat je ouders denken", "op je eerste indruk van de straat", "op één foto van een drukke dag"], 0,
       "Een besluit volgt uit de gegevens."),
    keuze("Een besluit mag ook zeggen dat er [[*te weinig gegevens|te veel lezers|geen hypothese]] waren om de vraag te beantwoorden.",
          "Eerlijk zijn over de grenzen hoort bij goed onderzoek."),
    tabel("Welke hulpmiddelen mag je op het examen aardrijkskunde gebruiken?",
          [("een atlas", J), ("een digitale kaart zoals Geopunt", J), ("een rekenmachine", J), ("je gsm om berichten te sturen", F)],
          "De examencommissie zet de toegelaten hulpmiddelen zelf op een rij."),
    sleep("Leg de laag met [[overstromingsgevoelige]] gebieden over een [[luchtfoto]] en maak ze half [[transparant]]. Zo zie je welke huizen gevaar lopen.",
          ["toeristische", "groter"], "Lagen combineren is de kracht van een digitale kaart."),
    inv("Op een digitale kaart meet je een fietspad van 2,4 km in 4 stukken van gelijke lengte. Hoe lang is elk stuk in meter?", ["600", "600 m"],
        "2400 m / 4 = 600 m."),
    mk("Waarom noteer je ook welke laag je niet gevonden hebt?",
       ["Zo weet de lezer waar je besluit stopt.", "Zo lijkt je onderzoek langer.", "Omdat het examen dat altijd zo verplicht.", "Omdat ontbrekende lagen altijd fout zijn."], 0,
       "Je toont eerlijk wat je onderzoek niet kon bewijzen."),
    tabel("Klopt dit over bronnen?",
          [("Een verouderde kaart kan de toestand van nu verkeerd voorstellen.", J), ("Bij een meting noteer je wanneer en waar je meet.", J), ("Elke bron op het internet is betrouwbaar.", F)],
          "Jaartal, plaats en maker maken een bron controleerbaar."),
    casus("Ahmed meet het verkeerslawaai langs een drukke weg: 72 dB om 8 uur, 65 dB om 11 uur en 74 dB om 17 uur.", [
        tabel("Klopt dit over zijn metingen?",
              [("Het is het luidst tijdens de spits.", J), ("Het lawaai is de hele dag gelijk.", F), ("Hij moet noteren waar hij precies stond.", J)],
              "Spitsuren geven meer verkeer en lawaai."),
        inv("Hoeveel dB scheelt het tussen de stilste en de luidste meting?", ["9", "9 dB"],
            "74 − 65 = 9 dB."),
    ]),
    mk("Je legt de overstromingslaag over een luchtfoto van je wijk. Wat onderzoek je zo?",
       ["welke gebouwen in risicogebied liggen", "hoe oud de bewoners van de wijk zijn", "hoeveel files er elke ochtend staan", "welke vegetatiezone de wijk heeft"], 0,
       "Twee lagen samen tonen waar gevaar en bebouwing elkaar raken."),
    keuze("In het onderzoeksdeel van het examen kan [[*alle leerstof|enkel de kaartleer|geen leerstof]] van aardrijkskunde terugkomen.",
          "Onderzoek gebruikt kennis uit alle thema's."),
    sorteer("Is dit een geografische hulpbron of geen hulpbron?", ["hulpbron", "geen hulpbron"],
            [("een satellietbeeld", "hulpbron"), ("een statistiek van inwoners", "hulpbron"), ("een gerucht op sociale media zonder bron", "geen hulpbron"), ("een topografische kaart", "hulpbron")],
            "Een hulpbron is controleerbaar en past bij de vraag."),
]
