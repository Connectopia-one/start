"""Grondstoffen, energie en industrie — pittig (🚀 Boost, aardrijkskunde).

Eigen vragen strikt binnen ak_grondstoffen, met een zelfgetekende doorsnede
van een landschap om op te klikken. ALG geldt voor doorstroom en dubbele
finaliteit; DO_ALLEEN gaat over outsourcing en reconversie (enkel doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, GRIJS, DONKER, LICHTGROEN, ORANJE, GEEL

L = Prent("landschap-energie", "Doorsnede van een landschap", "doorsnede met bergen en een stuwmeer, een groeve, een mijn met schacht, een fabriek aan een haven, windmolens in zee en zonnepanelen")
L.rect(0, 60, 1000, 240, "#eaf3fb", "none", 0, 0)
L.pad("M 0 300 L 0 150 L 90 90 L 170 160 L 240 110 L 300 300 Z", "#cfc6b0", DONKER, 2)
L.rect(160, 230, 120, 70, BLAUW, DONKER, 0, 1)
L.rect(270, 200, 16, 100, GRIJS, DONKER, 0, 2)
L.rect(0, 300, 1000, 300, "#c9b48f", DONKER, 0, 1)
L.rect(0, 430, 1000, 40, "#3a3a3a", "none", 0, 0)
L.tekst(500, 456, "steenkoollaag", 15, kleur="#ffffff")
L.pad("M 330 300 L 360 360 L 470 360 L 500 300 Z", "#e6dcc6", DONKER, 2)
L.rect(560, 230, 14, 230, "#555555", DONKER, 0, 2)
L.pad("M 545 230 L 590 230 L 567 190 Z", GRIJS, DONKER, 2)
L.rect(640, 250, 90, 50, "#b9a1c9", DONKER, 0, 2)
L.rect(700, 210, 14, 40, GRIJS, DONKER, 0, 1)
L.rect(740, 290, 260, 310, "#7fb2d9", "none", 0, 0)
L.rect(740, 270, 40, 30, ORANJE, DONKER, 0, 1)
for x in (860, 930):
    L.lijn(x, 300, x, 170, DONKER, 4)
    L.pad(f"M {x} 170 L {x-30} 140 M {x} 170 L {x+35} 160 M {x} 170 L {x-5} 210", "none", DONKER, 4)
for i in range(3):
    L.rect(40 + i * 40, 280, 32, 14, GEEL, DONKER, 0, 1)
PUNTEN = {"A": (220, 210), "B": (415, 330), "C": (567, 400), "D": (685, 230), "E": (895, 120), "F": (95, 270)}
for t, (x, y) in PUNTEN.items():
    L.letter(x, y - 40 if t != "C" else y, t)
U = "landschap-energie.svg"
Z = {t: Prent.rond(x, (y - 40 if t != "C" else y) + 10, 65) for t, (x, y) in PUNTEN.items()}
# A = stuwdam/waterkracht, B = groeve (dagbouw), C = mijn, D = fabriek aan haven, E = windmolens op zee, F = zonnepanelen

ALG = [
    klik("Klik op de plaats waar een grondstof in open lucht ontgonnen wordt.", U, [Z["B"]],
         "Een groeve of dagbouw ligt in open lucht."),
    klik("Klik op de plaats waar men ondergronds naar de steenkoollaag gaat.", U, [Z["C"]],
         "Een mijn bereikt de laag via een schacht."),
    klik("Klik op de hernieuwbare energiebron die werkt met stromend water.", U, [Z["A"]],
         "Een stuwdam met een waterkrachtcentrale."),
    klik("Klik op de fabriek die haar grondstoffen per schip ontvangt.", U, [Z["D"]],
         "Een fabriek aan de haven: grondstoffen en afzetmarkten overzee."),
    sorteer("Hernieuwbaar of niet-hernieuwbaar?", ["hernieuwbaar", "niet-hernieuwbaar"],
            [("windenergie", "hernieuwbaar"), ("aardgas", "niet-hernieuwbaar"), ("zonne-energie", "hernieuwbaar"), ("uranium voor kerncentrales", "niet-hernieuwbaar"), ("waterkracht", "hernieuwbaar"), ("steenkool", "niet-hernieuwbaar")],
            "Hernieuwbare bronnen raken niet op; uranium wel, ook al stoot een kerncentrale weinig CO₂ uit."),
    casus("In een land worden grote voorraden van een zeldzaam metaal voor batterijen ontdekt. Een buitenlands bedrijf opent er een groeve.", [
        tabel("Klopt dit over de nieuwe groeve?",
              [("De vraag naar zulke metalen stijgt door elektrische auto's.", J), ("Het land wordt daardoor vanzelf welvarend.", F), ("Als de winst naar het buitenland gaat, blijft er weinig over in het land.", J)],
              "Een voorraad alleen maakt niet rijk."),
        mk("Wanneer start het bedrijf de ontginning?",
           ["als de opbrengst de kosten overtreft", "meteen nadat de voorraad gevonden is", "pas als de voorraad bijna op is", "enkel als het land in oorlog is"], 0,
           "Ontginnen kost veel; het moet renderen."),
        tabel("Welke ruimtelijke gevolgen heeft de groeve?",
              [("het landschap verandert blijvend", J), ("er komen wegen en vrachtverkeer bij", J), ("het bos rond de groeve groeit aan", F)],
              "Ontginning laat sporen na in het landschap."),
    ]),
    koppel("Welke factor verklaart de plaats?",
           [("windmolens op de Noordzee", "het waait er harder en constanter"), ("zonneparken in zonnige streken", "meer zonuren geven meer opbrengst"), ("oude mijnen in de Kempen", "de steenkoollaag zat in de ondergrond"), ("chemie in de haven van Antwerpen", "grondstoffen komen er per schip binnen")],
           ["de lonen zijn er het laagst"], "Elke plaats heeft een fysische of economische reden."),
    tabel("Klopt dit over recyclage?",
          [("Oud schroot en batterijen zijn een bron van grondstoffen.", J), ("Recyclage van metalen kost meestal veel minder energie.", J), ("Recyclage maakt ontginning helemaal overbodig.", F)],
          "Recyclage vult ontginning aan, maar vervangt ze niet volledig."),
    mk("Een staalfabriek uit 1900 staat naast een steenkoolmijn. Wat verklaart die keuze het best?",
       ["Steenkool was zwaar en duur om te vervoeren.", "De arbeiders wilden dicht bij de kust wonen.", "Fabrieken mochten wettelijk nergens anders staan.", "De lonen waren daar het allerhoogst van het land."], 0,
       "Voor elke ton staal was veel steenkool nodig."),
    tabel("Klopt dit over moderne industrie?",
          [("Ze kiest haar plaats vrijer dan vroeger.", J), ("Ze heeft geen transport meer nodig.", F), ("Ze zoekt vaak goedkope grond bij snelwegen.", J)],
          "Ze is minder gebonden aan grondstoffen, maar niet aan vervoer."),
    casus("In een mijnstreek sluiten tussen 1966 en 1992 alle steenkoolmijnen.", [
        inv("Hoe noem je het verdwijnen van industrie uit een streek die er sterk op draaide?", ["de-industrialisatie", "desindustrialisatie", "deïndustrialisatie"],
            "Fabrieken en mijnen sluiten, de streek moet een nieuwe economie zoeken."),
        tabel("Welke gevolgen heeft de sluiting voor de streek?",
              [("de werkloosheid stijgt", J), ("winkels en toeleveranciers verliezen klanten", J), ("de mijnterreinen worden vanzelf natuur", F)],
              "Een sluiting raakt veel meer dan de mijn zelf."),
    ]),
    sorteer("Is dit een fysische of een geopolitieke factor bij energie en industrie?", ["fysisch", "geopolitiek"],
            [("het klimaat", "fysisch"), ("lidmaatschap van een handelsblok", "geopolitiek"), ("het reliëf voor een stuwdam", "fysisch"), ("een oorlog in het land", "geopolitiek"), ("de staatsvorm", "geopolitiek")],
            "Fysisch komt uit de natuur, geopolitiek uit de macht tussen staten."),
    sleep("Een grondstof in open lucht ontginnen heet [[dagbouw]]. Werk met de hand is [[traditionele]] ontginning, werk met grote machines [[moderne]] ontginning.",
          ["ondergronds", "recyclage"], "Plaats en manier van ontginnen."),
    keuze("Klimaatverandering kan de opbrengst van een waterkrachtcentrale [[*doen dalen|nooit veranderen|altijd verdubbelen]].",
          "Minder sneeuw en neerslag betekent minder water in het stuwmeer."),
    mk("Een kledingbedrijf laat naaien in een land met lage lonen en verkoopt in Europa. Wat toont dat?",
       ["Productie en afzetmarkt liggen ver uiteen.", "Kleding wordt enkel in Europa gekocht.", "Europese lonen zijn de laagste ter wereld.", "Het bedrijf heeft geen afzetmarkt nodig."], 0,
       "Waar iets gemaakt wordt en waar het verkocht wordt, kan verschillen."),
    tabel("Klopt dit over de afzetmarkt?",
          [("Het is de plaats waar een product verkocht wordt.", J), ("Bij bederfelijke producten weegt de nabijheid van klanten zwaar.", J), ("Voor elk product weegt de nabijheid van klanten even zwaar.", F)],
          "Zware of bederfelijke producten maak je best dicht bij de klant."),
    klik("Klik op de energiebron die vooral in streken met veel zonuren rendeert.", U, [Z["F"]],
         "Zonnepanelen brengen meer op waar de zon vaak schijnt."),
    volgorde("Rangschik hoe een mijnstreek ontstaat.",
             ["Men vindt een steenkoollaag in de ondergrond.", "Er worden schachten gegraven.", "Zware industrie vestigt zich vlak bij de mijn.", "Er komen woonwijken voor de arbeiders."],
             "Ontginning trekt industrie en bewoners aan."),
    tabel("Lees de doorsnede van het landschap. Klopt dit?",
          [("De groeve ligt hoger dan de steenkoollaag.", J), ("De windmolens staan op land.", F), ("De fabriek ligt aan het water.", J)],
          "De windmolens staan in zee, de fabriek aan de haven."),
    klik("Klik op de energiebron die in België vooral op de Noordzee staat.", U, [Z["E"]],
         "Windmolenparken op zee: daar waait het harder en constanter."),
    mk("Waarom kiest een bedrijf voor dagbouw als de grondstof dicht bij het oppervlak zit?",
       ["Het is goedkoper en veiliger.", "Het levert altijd zuiverder erts op.", "Het laat geen sporen na in het landschap.", "Het mag in België enkel zo."], 0,
       "Geen schachten en gangen: minder kosten en minder gevaar."),
    inv("Hoe noem je energiebronnen zoals wind, zon en waterkracht met één woord? Vul aan: ... energiebronnen.", ["hernieuwbare", "hernieuwbaar"],
        "Ze raken niet op."),
]

DO_ALLEEN = [
    tabel("Klopt dit over outsourcing?",
          [("Werk wordt naar een bedrijf in een ander land verplaatst.", J), ("Lagere lonen zijn de enige reden.", F), ("Ook regels en nabijheid van markten spelen mee.", J)],
          "Lonen wegen mee, maar niet alleen."),
    casus("De oude mijnsite van een stad wordt omgebouwd tot een bedrijvenpark met een campus.", [
        inv("Hoe noem je het omvormen van een oud industrieterrein tot iets nieuws?", ["reconversie", "de reconversie"],
            "Reconversie geeft een oude site een nieuwe economische functie."),
        mk("Waarom kiest een stad voor reconversie?",
           ["om nieuw werk te maken op oude grond", "om de oude mijnen opnieuw te openen", "om meer steenkool te kunnen invoeren", "om de site voorgoed leeg te laten"], 0,
           "De grond en de gebouwen krijgen een nieuw leven."),
    ]),
    keuze("Een bedrijf dat zijn klantendienst naar een ander land verplaatst, doet aan [[*outsourcing|reconversie|recyclage]].",
          "Werk uitbesteden aan een bedrijf elders."),
    sorteer("Is dit outsourcing of reconversie?", ["outsourcing", "reconversie"],
            [("een fabriek laat onderdelen in Azië maken", "outsourcing"), ("een oude haven wordt een woonwijk", "reconversie"), ("een bank laat haar boekhouding in het buitenland doen", "outsourcing"), ("een mijngebouw wordt een museum", "reconversie")],
            "Outsourcing verplaatst werk, reconversie geeft een plaats een nieuwe functie."),
]

DF_ALLEEN = [
    tabel("Welke sociaaleconomische factoren spelen mee bij de keuze waar een fabriek komt?",
          [("de lonen", J), ("de opleiding van de werknemers", J), ("de nabijheid van klanten", J), ("de kleur van de bodem", F)],
          "Wie een fabriek bouwt, kijkt naar mensen en markten."),
    mk("Een land met olie raakt in oorlog. Wat gebeurt er met de olieproductie?",
       ["Ze valt terug.", "Ze verdubbelt vanzelf.", "Ze blijft altijd gelijk.", "Ze stopt in alle andere landen."], 0,
       "Investeerders en werknemers vertrekken; installaties raken beschadigd."),
    keuze("Kernenergie is [[*niet-hernieuwbaar|hernieuwbaar|een vorm van windenergie]], want uranium raakt op.",
          "Weinig CO₂ betekent niet dat de bron hernieuwbaar is."),
    tabel("Je zoekt op een topografische kaart een streek met zware industrie. Welke tekens wijzen erop?",
          [("grote bedrijventerreinen bij een haven", J), ("spoorlijnen en kanalen", J), ("kleine akkers en hagen", F)],
          "Zware industrie heeft ruimte en vervoer over water of spoor nodig."),
    keuze("Een land dat lid is van een handelsblok, voert [[*makkelijker|moeilijker|nooit]] uit naar de andere leden.",
          "Binnen een handelsblok vallen tarieven en grenscontroles weg."),
]

VRAGEN = ALG + DO_ALLEEN
VRAGEN_DF = ALG + DF_ALLEEN
