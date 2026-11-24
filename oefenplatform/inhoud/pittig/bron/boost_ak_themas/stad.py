"""Stad en platteland — pittig (🚀 Boost, aardrijkskunde).

Eigen vragen strikt binnen ak_stad, met een zelfgetekend schema van een stad
en haar omgeving om op te klikken. ALG geldt voor doorstroom en dubbele
finaliteit; DO_ALLEEN gaat over de hiërarchie van steden, inbreiding en
stadslandbouw (enkel doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, GRIJS, DONKER, LICHTGROEN, ORANJE, ROOD

KAART = Prent("stad-omgeving", "Een stad en haar omgeving", "schema van een stad met een centrum, een ring, een snelweg, akkers en zes letters")
KAART.rect(40, 60, 920, 560, "#eef5e4", DONKER, 0, 1)
for x in range(60, 940, 70):
    KAART.lijn(x, 80, x + 40, 600, "#d7e6c3", 6)
KAART.cirkel(470, 330, 190, "#ece6d8", DONKER, 2)
KAART.cirkel(470, 330, 190, "none", GRIJS, 10)
KAART.cirkel(470, 330, 80, "#d9cfb8", DONKER, 2)
KAART.pad("M 40 560 C 300 520 600 560 960 500", "none", "#7c7c7c", 16)
KAART.rect(720, 470, 150, 70, "#c9c3d9", DONKER, 4, 2)
for i in range(4):
    KAART.rect(735 + i * 34, 485, 24, 40, "#ffffff", DONKER, 2, 1)
KAART.rect(330, 400, 70, 50, "#b98a5a", DONKER, 2, 2)
KAART.lijn(345, 400, 345, 370, DONKER, 6)
for i in range(3):
    for j in range(3):
        KAART.rect(780 + i * 32, 140 + j * 32, 22, 22, ORANJE, DONKER, 2, 1)
KAART.lijn(650, 330, 780, 180, GRIJS, 6)
for i in range(4):
    KAART.rect(520 + i * 22, 180, 16, 60, "#a7a7b7", DONKER, 1, 1)
KAART.pad("M 120 120 L 220 110 L 240 200 L 130 210 Z", LICHTGROEN, DONKER, 1)
PUNTEN = {"A": (470, 330), "B": (365, 425), "C": (810, 170), "D": (795, 505), "E": (555, 210), "F": (180, 160)}
for t, (x, y) in PUNTEN.items():
    KAART.letter(x + 40, y - 35, t)
KAART.tekst(900, 548, "snelweg", 15, "end")
U = "stad-omgeving.svg"
Z = {t: Prent.rond(x + 15, y - 10, 70) for t, (x, y) in PUNTEN.items()}
# A = centrum, B = oude fabriek in de stad, C = nieuwe verkaveling in een dorp, D = bedrijventerrein aan de snelweg,
# E = hoogbouw van sociale woningen, F = akker

ALG = [
    klik("Een bedrijf zoekt goedkope grond die vlot bereikbaar is voor vrachtwagens. Klik op de plaats die het kiest.", U, [Z["D"]],
         "Bij de snelweg, buiten de stad: ruimte, lage grondprijs en bereikbaarheid."),
    klik("Klik op de nieuwe verkaveling waar gezinnen uit de stad naartoe trekken.", U, [Z["C"]],
         "De nieuwe huizen buiten de ring tonen stadsvlucht en verstedelijking van het platteland."),
    klik("Klik op het oude gebouw dat het best in aanmerking komt voor een functiewijziging tot lofts.", U, [Z["B"]],
         "Een oude fabriek in de stad krijgt vaak een nieuwe functie, zoals wonen."),
    casus("Het gezin Peeters woont in een appartement in het centrum. Ze verhuizen naar een nieuwe verkaveling in een dorp twintig kilometer verder, voor een tuin en rust. Beide ouders blijven in de stad werken.", [
        inv("Hoe noem je zo'n verhuis van de stad naar het platteland? Schrijf het woord.", ["stadsvlucht", "de stadsvlucht"],
            "Stadsvlucht: weg uit de stad, op zoek naar ruimte en rust."),
        tabel("Klopt dit over hun nieuwe leven?",
              [("Ze leggen elke dag meer kilometers af.", J), ("Ze pendelen tussen woonplaats en werkplaats.", J), ("Hun verhuis maakt het dorp minder stedelijk.", F)],
              "Meer verkavelingen en pendelaars verstedelijken het platteland."),
        mk("Wat kan er gebeuren als veel gezinnen zo doen?",
           ["Het dorp wordt een woondorp met veel verkeer.", "Het centrum van de stad wordt drukker bewoond.", "Het dorp krijgt meer akkers en minder huizen.", "De snelweg naar de stad raakt minder vol."], 0,
           "Meer huizen, meer auto's, maar niet altijd meer winkels of werk."),
    ]),
    sorteer("Is dit een reden om in de stad of op het platteland te wonen?", ["stad", "platteland"],
            [("dichtbij werk, scholen en ziekenhuizen", "stad"), ("meer ruimte voor hetzelfde geld", "platteland"), ("goed openbaar vervoer", "stad"), ("rust en groen", "platteland"), ("veel cultuur en uitgaan", "stad")],
            "De stad bundelt voorzieningen; het platteland biedt ruimte en rust."),
    tabel("Klopt dit over verstedelijking?",
          [("Steden krijgen meer inwoners.", J), ("Stedelijke kenmerken schuiven op naar het platteland.", J), ("Het gaat enkel over meer inwoners in steden.", F), ("Een luchtfoto van vroeger en nu toont ze goed.", J)],
          "Verstedelijking is ook het platteland dat steeds meer bebouwd raakt."),
    koppel("Welk begrip hoort bij welk voorbeeld?",
           [("functiewijziging", "een kerk wordt een bibliotheek"), ("sociale segregatie", "rijke en arme gezinnen wonen in aparte wijken"), ("multiculturaliteit", "mensen van veel culturen wonen in dezelfde stad"), ("ontvolking", "jongeren trekken weg uit een afgelegen dorp")],
           ["hitte-eilandeffect"], "Elk begrip beschrijft een verandering in stad of platteland."),
    tabel("Klopt dit over sociale segregatie?",
          [("Bevolkingsgroepen wonen in gescheiden wijken.", J), ("De woningprijs is een belangrijke oorzaak.", J), ("Ze is hetzelfde als multiculturaliteit.", F)],
          "Segregatie is een ruimtelijke scheiding; multiculturaliteit gaat over wie er samen woont."),
    casus("In een stad is het op een zomeravond 5 °C warmer dan in de dorpen eromheen. Na een zware bui lopen de straten onder water.", [
        inv("Hoe heet het verschijnsel van de hogere temperatuur in de stad?", ["hitte-eilandeffect", "het hitte-eilandeffect", "hitte-eiland"],
            "Beton en asfalt houden warmte vast."),
        tabel("Wat helpt tegen beide problemen?",
              [("een betonnen plein openbreken en bomen planten", J), ("groendaken aanleggen", J), ("meer parkings in asfalt", F)],
              "Minder verharding laat water in de bodem zakken en koelt de stad."),
        mk("Waarom lopen de straten zo snel onder water?",
           ["Verharding laat het water niet in de bodem.", "De stad ligt altijd lager dan het platteland.", "Er valt in de stad meer regen dan buiten.", "Bomen houden het regenwater tegen."], 0,
           "Beton en asfalt laten geen water door, dus loopt alles snel naar de riolen."),
    ]),
    sleep("Wie dagelijks heen en weer reist tussen wonen en werken, [[pendelt]]. Het opdelen van de open ruimte in kleine stukken heet [[versnippering]]. Een leegstaande fabriek die woningen wordt, kent een [[functiewijziging]].",
          ["segregatie", "stadsvlucht"], "Drie veranderingen in stad en platteland."),
    tabel("In een winkelstraat staat een derde van de panden leeg. Wat is een geloofwaardige verklaring?",
          [("Mensen kopen meer online.", J), ("Grote winkels verhuizen naar de rand van de stad.", J), ("De huurprijzen in de straat zijn te hoog.", J), ("Er wonen te veel mensen in het centrum.", F)],
          "Online winkelen en baanwinkels trekken klanten weg uit het centrum."),
    mk("In welke landen trekken mensen vooral van het platteland naar de stad?",
       ["in veel minder ontwikkelde landen", "enkel in de allerrijkste landen van Europa", "nergens meer, want die trek is al voorbij", "enkel in landen zonder grote steden"], 0,
       "Werk, onderwijs en zorg zitten daar vooral in de stad."),
    keuze("Een stad die inwoners verliest, verliest daarom [[*niet altijd|altijd|nooit]] haar economische functie.",
          "Kantoren, haven en universiteit kunnen blijven."),
    sorteer("Hoort dit bij de verstedelijking van het platteland?", ["ja", "nee"],
            [("nieuwe verkavelingen rond de dorpskern", "ja"), ("winkels langs een steenweg", "ja"), ("meer pendelverkeer", "ja"), ("akkers die er bijkomen", "nee")],
            "Bebouwing, winkels en verkeer schuiven het platteland op."),
    tabel("Klopt dit over armoede en wonen?",
          [("In de stad is er meer kans op werk.", J), ("Wonen is in de stad vaak duurder.", J), ("Armoede duwt mensen altijd weg uit de stad.", F)],
          "Armoede werkt in twee richtingen."),
    klik("Klik op de hoge woonblokken waar vaak gezinnen met een kleiner budget wonen.", U, [Z["E"]],
         "Sociale hoogbouw toont hoe woningprijs en segregatie samenhangen."),
    klik("Klik op het gebied waar versnippering van de open ruimte de landbouw het meest bedreigt.", U, [Z["F"]],
         "De akkers buiten de stad raken versnipperd door wegen en verkavelingen."),
    volgorde("Rangschik hoe een woondorp ontstaat.",
             ["Een snelweg maakt de stad vlot bereikbaar.", "Stedelingen kopen grond in het dorp.", "Er komen verkavelingen rond de dorpskern.", "Veel inwoners pendelen elke dag naar de stad."],
             "Bereikbaarheid trekt nieuwe bewoners aan, die blijven pendelen."),
    tabel("Lees het schema van de stad. Klopt dit?",
          [("Het bedrijventerrein ligt aan de snelweg.", J), ("De akkers liggen binnen de ring.", F), ("Het centrum ligt in het midden van de ring.", J)],
          "Bedrijven zoeken bereikbaarheid, akkers liggen buiten de bebouwing."),
    inv("Hoe noem je het verdwijnen van inwoners uit afgelegen dorpen zonder werk of voorzieningen? Schrijf het woord.", ["ontvolking", "de ontvolking", "ontvolking van het platteland"],
        "Jongeren trekken weg voor studie en werk; scholen en winkels sluiten."),
]

DO_ALLEEN = [
    tabel("Op welke grond heeft deze stad belang?",
          [("hoofdkwartieren van grote bedrijven", "economisch"), ("universiteiten en grote musea", "cultureel"), ("de zetel van een regering", "politiek"), ("een grote internationale beurs", "economisch")],
          "De hiërarchie van steden kijkt naar economisch, cultureel en politiek belang.",
          ["economisch", "cultureel", "politiek"]),
    mk("Waarom staat Brussel hoog in de Europese stedenhiërarchie?",
       ["Er zetelen Europese instellingen.", "Het is de grootste stad van Europa.", "Het ligt in het midden van het continent.", "Het heeft de grootste haven van Europa."], 0,
       "Niet grootte maar belang telt."),
    tabel("Klopt dit over inbreiding?",
          [("Je bouwt op open plekken binnen de bestaande stad.", J), ("Zo blijft de open ruimte buiten de stad gespaard.", J), ("Het betekent nieuwe verkavelingen op akkers.", F)],
          "Inbreiding vult de stad op in plaats van uit te breiden."),
    sorteer("Is dit inbreiding of uitbreiding?", ["inbreiding", "uitbreiding"],
            [("appartementen op een oud bedrijfsterrein in de stad", "inbreiding"), ("een nieuwe wijk op weilanden buiten de stad", "uitbreiding"), ("een lege bouwgrond tussen twee huizen in de stad bebouwen", "inbreiding"), ("een bedrijventerrein op akkers langs de snelweg", "uitbreiding")],
            "Inbreiding blijft binnen de bebouwde stad."),
    tabel("Welke voordelen geeft stadslandbouw?",
          [("kortere afstand tussen teelt en bord", J), ("meer groen in de stad", J), ("genoeg voedsel voor de hele stad", F)],
          "Stadslandbouw helpt, maar voedt de stad niet helemaal."),
    keuze("Een stad kan [[*tegelijk|nooit|enkel na een oorlog]] economisch, cultureel én politiek belangrijk zijn.",
          "Parijs, Londen en Tokio combineren de drie."),
]

DF_ALLEEN = [
    tabel("Welke factoren spelen mee bij de keuze tussen stad en platteland?",
          [("de prijs van een woning", J), ("de afstand tot het werk", J), ("de politieke en de oorlogssituatie", J), ("de kleur van de huizen", F)],
          "Ook klimaat, reliëf en armoede spelen mee."),
    mk("Een dorp krijgt er in twintig jaar drie verkavelingen bij, maar geen enkele winkel. Wat wordt het?",
       ["een woondorp", "een stad met een rijke cultuur", "een landbouwdorp zonder huizen", "een bedrijventerrein"], 0,
       "Mensen wonen er, maar werken en winkelen elders."),
    tabel("Je vergelijkt een luchtfoto van een gemeente van 1970 met een van nu. Waaraan zie je verstedelijking?",
          [("meer bebouwde oppervlakte", J), ("meer wegen", J), ("meer akkers rond het dorp", F)],
          "Bebouwing en wegen nemen de open ruimte in."),
    keuze("Een fietssnelweg of een nieuwe ring [[*verandert|verandert nooit|vernietigt altijd]] waar mensen wonen en werken.",
          "Veranderende mobiliteit verandert ook het landschap."),
    sorteer("Is dit een gevolg voor de stad of voor het platteland?", ["stad", "platteland"],
            [("leegstaande winkels in het centrum", "stad"), ("versnippering van de open ruimte", "platteland"), ("hitte op betonnen pleinen", "stad"), ("ontvolking van afgelegen dorpen", "platteland")],
            "Sommige veranderingen raken het centrum, andere het platteland."),
    mk("Waarom is het straatbeeld van een multiculturele wijk een goede bron?",
       ["Winkels en opschriften tonen wie er woont.", "Het straatbeeld blijft eeuwenlang hetzelfde.", "Er wonen daar helemaal geen mensen meer.", "Het geeft de exacte bevolkingsdichtheid."], 0,
       "Wat je ziet in de straat vertelt veel over de bewoners."),
]

VRAGEN = ALG + DO_ALLEEN
VRAGEN_DF = ALG + DF_ALLEEN
