"""Productie, toegevoegde waarde en het bbp — pittig (🚀 Boost doorstroom, economie).

Eigen vragen strikt binnen ec_bbp, met een zelfgetekende staafgrafiek van groeicijfers."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, ORANJE, ROOD, DONKER, LIJN

GR = Prent("groeicijfers", "Reële groei van het bbp van land X (in %)", "staafgrafiek met de reële groei van het bbp in procent, 2020 tot 2025")
JAREN = [("2020", -5.0), ("2021", 6.0), ("2022", 3.0), ("2023", 1.5), ("2024", 1.0), ("2025", -0.5)]
def Yg(v): return 330 - v * 36
for v in range(-6, 8, 2):
    GR.lijn(140, Yg(v), 900, Yg(v), "#e2ded2", 1)
    GR.tekst(128, Yg(v) + 6, f"{v}", 16, "end")
GR.lijn(140, Yg(0), 900, Yg(0), DONKER, 3)
STAAF = {}
for i, (j, v) in enumerate(JAREN):
    x = 180 + i * 120
    top, h = (Yg(v), Yg(0) - Yg(v)) if v >= 0 else (Yg(0), Yg(v) - Yg(0))
    GR.rect(x, top, 70, h, BLAUW if v >= 0 else ROOD, DONKER, 0, 1)
    GR.tekst(x + 35, 600, j, 18)
    STAAF[j] = Prent.zone(x - 10, min(top, Yg(0)) - 20, 90, max(h, 10) + 40)
U = "groeicijfers.svg"

VRAGEN = [
    klik("Klik op het jaar waarin de economie het sterkst kromp.", U, [STAAF["2020"]],
         "2020 heeft de laagste staaf: −5 %, een krimp."),
    klik("Klik op het jaar met de hoogste reële groei.", U, [STAAF["2021"]],
         "2021: +6 %."),
    klik("Na 2021 wordt de staaf elk jaar lager. Klik op het eerste jaar waarin er geen groei meer was, maar krimp.", U, [STAAF["2025"]],
         "In 2023 en 2024 is er nog groei, al is ze kleiner. Pas in 2025 is het cijfer negatief."),
    tabel("Klopt dit volgens de grafiek?",
          [("In 2023 was het reële bbp groter dan in 2022.", J), ("In 2024 daalde het reële bbp.", F), ("In 2025 daalde het reële bbp.", J)],
          "Een lagere maar positieve staaf is nog altijd groei.", ),
    casus("Een bedrijfskolom voor een houten tafel.\n\nDe bosbouwer verkoopt hout voor 150 euro aan de zagerij. De zagerij verkoopt planken voor 380 euro aan de meubelmaker. De meubelmaker verkoopt de tafel voor 900 euro aan de meubelwinkel. De winkel verkoopt de tafel voor 1 250 euro aan een gezin.", [
        tabel("Hoe groot is de toegevoegde waarde van deze schakel?",
              [("de zagerij", "230"), ("de meubelmaker", "520"), ("de meubelwinkel", "350")],
              "Omzet min de aankopen bij de vorige schakel.",
              kolommen=["230", "350", "520"]),
        inv("Hoe groot is de totale toegevoegde waarde van de hele kolom, in euro? Schrijf enkel het getal.", ["1250", "1 250", "1.250"],
            "150 + 230 + 520 + 350 = 1 250, de prijs van het eindproduct."),
        mk("Waarom tel je niet alle omzetten op (150 + 380 + 900 + 1 250)?",
           ["Dan tel je het hout meerdere keren mee.", "Omdat de winkel geen echte waarde toevoegt.", "Omdat de bosbouwer geen omzet heeft gemaakt.", "Omdat enkel de laatste verkoop in het bbp telt."], 0,
           "De omzet van elke schakel bevat de waarde van de vorige schakels."),
    ]),
    inv("Een loodgieter koopt buizen voor 300 euro en factureert 1 000 euro. Hoeveel toegevoegde waarde maakt hij? Schrijf enkel het getal.", ["700"],
        "1 000 − 300 = 700 euro, verdeeld over loon en winst."),
    sorteer("Telt dit mee in het Belgische bbp van dit jaar?", ["telt mee", "telt niet mee"],
            [("een nieuwe auto gemaakt in Gent", "telt mee"), ("de verkoop van een tweedehandsfiets tussen buren", "telt niet mee"), ("een knipbeurt bij de kapper", "telt mee"), ("koken voor je eigen gezin", "telt niet mee"), ("de les van een betaalde leerkracht", "telt mee"), ("vrijwilligerswerk in de jeugdbeweging", "telt niet mee")],
            "Enkel nieuwe productie via een markt, in België, dit jaar."),
    tabel("In welk bbp telt deze productie?",
          [("Een Japans bedrijf maakt auto's in Gent.", "Belgisch bbp"), ("Een Belgisch bedrijf bouwt een fabriek en produceert in Polen.", "Pools bbp"), ("Een Belgische bakker bakt in Leuven.", "Belgisch bbp")],
          "Binnenlands: waar de productie gebeurt, niet wie de eigenaar is.",
          kolommen=["Belgisch bbp", "Pools bbp"]),
    keuze("Het bbp is een [[*stroomgrootheid|voorraadgrootheid]], want het meet een hoeveelheid per jaar.",
          "Een stroom hoort bij een periode."),
    keuze("Het woord bruto zegt dat de [[*afschrijvingen|belastingen|invoer]] er nog niet af zijn getrokken.",
          "Bruto = vóór de slijtage van machines en gebouwen."),
    tabel("Nominaal of reëel?",
          [("gerekend met de prijzen van elk jaar zelf", "nominaal"), ("gerekend met de prijzen van een basisjaar", "reëel"), ("stijgt ook als enkel de prijzen stijgen", "nominaal"), ("toont of er echt meer geproduceerd is", "reëel")],
          "Het reële bbp haalt het prijseffect eruit.",
          kolommen=["nominaal", "reëel"]),
    inv("Het nominale bbp stijgt met 6 %, de prijzen met 4 %. Hoe groot is de reële groei ongeveer, in procent? Schrijf enkel het getal.", ["2", "2 %", "2%"],
        "6 − 4 = ongeveer 2 %."),
    inv("Het nominale bbp stijgt met 1 %, de prijzen met 3 %. Hoe groot is de reële groei ongeveer, in procent? Schrijf het getal met het teken.", ["-2", "−2", "-2 %", "−2 %", "-2%"],
        "1 − 3 = −2 %: in euro meer, in hoeveelheid minder."),
    inv("Het bbp stijgt van 250 naar 260 miljard euro. Hoe groot is de groei in procent? Schrijf enkel het getal.", ["4", "4 %", "4%"],
        "10 / 250 = 0,04 = 4 %."),
    inv("Een land heeft een bbp van 90 miljard euro en 2 miljoen inwoners. Hoe groot is het bbp per capita in euro? Schrijf enkel het getal.", ["45000", "45 000", "45.000"],
        "90 000 000 000 / 2 000 000 = 45 000 euro."),
    tabel("Wat gebeurt er met het bbp per capita?",
          [("bbp +3 %, bevolking +1 %", "stijgt"), ("bbp +1 %, bevolking +2 %", "daalt"), ("bbp +2 %, bevolking +2 %", "blijft ongeveer gelijk")],
          "Vergelijk de groei van de koek met de groei van het aantal eters.",
          kolommen=["stijgt", "daalt", "blijft ongeveer gelijk"]),
    casus("Een tabel van land Y (in miljard euro).\n\n2026: nominaal bbp 800\n2027: nominaal bbp 840\nPrijsstijging in 2027: 3 %", [
        inv("Hoe groot is de nominale groei in 2027, in procent? Schrijf enkel het getal.", ["5", "5 %", "5%"],
            "40 / 800 = 0,05 = 5 %."),
        inv("Hoe groot is de reële groei ongeveer, in procent? Schrijf enkel het getal.", ["2", "2 %", "2%"],
            "5 − 3 = ongeveer 2 %."),
    ]),
    mk("Welke uitspraak over toegevoegde waarde klopt?",
       ["Ze wordt verdeeld als loon, intrest, pacht en winst.", "Ze is altijd gelijk aan de omzet van het bedrijf.", "Ze is het geld dat een bedrijf aan zijn leveranciers betaalt.", "Ze telt enkel bij bedrijven die tastbare goederen maken."], 0,
       "De toegevoegde waarde vergoedt de productiefactoren."),
    tabel("Is dit een beperking van het bbp als maatstaf?",
          [("Het telt onbetaald werk niet mee.", J), ("Het zegt niets over hoe het inkomen verdeeld is.", J), ("Het meet de productie in een land.", F), ("Het telt herstellingen na een ramp als productie.", J)],
          "Het bbp meet productie, geen welzijn."),
    keuze("In het basisjaar zijn het nominale en het reële bbp [[*even groot|altijd verschillend|nul]].",
          "Je rekent dan met dezelfde prijzen."),
    koppel("Welke bron hoort bij welke beschrijving?",
           [("Statbel", "de Belgische overheidsdienst voor de statistiek"), ("Nationale Bank van België", "volgt de Belgische economie en de financiële gegevens op")],
           ["een krant met meningen"], "Officiële cijfers haal je bij betrouwbare bronnen."),
    keuze("Een transportbedrijf brengt bananen van de haven naar de winkel. Het [[*voegt waarde toe|voegt geen waarde toe, want het maakt niets]].",
          "Diensten zijn ook productie."),
    sleep("De toegevoegde waarde is de [[omzet]] min de [[aankopen]] bij andere bedrijven. Het [[bbp]] is de som van alle toegevoegde waarden in een land in één jaar.",
          ["winst", "lonen"], "De kern van het thema in één zin."),
    inv("Hoe noem je het jaar waarvan je de prijzen gebruikt om het reële bbp te berekenen? Schrijf één woord.", ["basisjaar", "referentiejaar"],
        "In dat jaar zijn nominaal en reëel gelijk."),
    keuze("Na een overstroming worden veel huizen hersteld. Het bbp [[*stijgt|daalt|blijft gelijk]], hoewel het land er niet beter aan toe is.",
          "Herstellingen zijn betaalde productie."),
    mk("Waarom vergelijk je de welvaart van landen liever met het bbp per capita?",
       ["Een groot land lijkt anders rijker.", "Het bbp zelf wordt niet berekend.", "Kleine landen hebben geen bbp-cijfer.", "Het bbp per capita telt ook vrijwilligerswerk."], 0,
       "Je deelt door het aantal inwoners om eerlijk te vergelijken."),
    open_("Leg uit waarom een handelaar met een grote omzet toch een kleine toegevoegde waarde kan hebben.",
          "Als hij bijna alles wat hij verkoopt eerst duur moet inkopen, blijft er na aftrek van de aankopen weinig over.",
          "Toegevoegde waarde = omzet − aankopen."),
]
