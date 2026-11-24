"""Kwaliteitsbewust handelen — pittig (🛠️ Boost dubbele finaliteit, gezondheidszorg en welzijn).

Eigen vragen strikt binnen gz_kwaliteitsbewust, met zelfgetekende
veiligheidstekens zonder tekst."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL

TK = Prent("vijf-tekens", "Vijf veiligheidstekens", "vijf tekens naast elkaar: een rode cirkel met streep, een blauwe cirkel, een gele driehoek, een groen rechthoekje en een witte ruit met rode rand, met letters A tot E")
TK.cirkel(120, 260, 75, "white", "#d22", 14); TK.lijn(68, 208, 172, 312, "#d22", 14)
TK.cirkel(310, 260, 75, "#1f5fbf", "#1f5fbf", 2); TK.cirkel(310, 260, 30, "white", "white", 2)
TK.pad("M 500 180 L 585 330 L 415 330 Z", "#f7d417", DONKER, 8)
TK.rect(615, 200, 170, 120, "#1f9a45", "#1f9a45", 10, 2); TK.rect(680, 225, 40, 70, "white", "white", 4, 2)
TK.pad("M 890 175 L 975 260 L 890 345 L 805 260 Z", "white", "#d22", 10); TK.cirkel(890, 260, 18, DONKER, DONKER, 2)
LET = {"A": (120, 400), "B": (310, 400), "C": (500, 400), "D": (700, 400), "E": (890, 400)}
for t, (x, y) in LET.items():
    TK.letter(x, y, t)
U = "vijf-tekens.svg"
ZT = {"A": Prent.rond(120, 260, 80), "B": Prent.rond(310, 260, 80), "C": Prent.rond(500, 270, 80), "D": Prent.rond(700, 260, 85), "E": Prent.rond(890, 260, 85)}
Z = {t: [*ZT[t]] for t in ZT}

VRAGEN = [
    klik("Klik op het teken dat zegt dat iets niet mag.", U, [ZT["A"], Prent.rond(120, 400, 30)],
         "Een verbodsteken is een rode cirkel met een streep erdoor."),
    klik("Klik op het teken dat zegt dat iets verplicht is, zoals een veiligheidsbril dragen.", U, [ZT["B"], Prent.rond(310, 400, 30)],
         "Een gebodsteken is een blauwe cirkel."),
    klik("Klik op het teken dat de weg naar de nooduitgang of de verbanddoos wijst.", U, [ZT["D"], Prent.rond(700, 400, 30)],
         "Reddingstekens zijn groen."),
    klik("Klik op het gevarensymbool dat je op het etiket van een schoonmaakproduct vindt.", U, [ZT["E"], Prent.rond(890, 400, 30)],
         "Een gevarensymbool is een ruit met een rode rand en een zwart teken erin."),
    sorteer("Welke factor van kwaliteitsbewust handelen is dit vooral?", ["hygiënisch", "ergonomisch", "milieubewust", "economisch"],
            [("handen wassen voor je een maaltijd klaarmaakt", "hygiënisch"), ("de strijkplank op heuphoogte zetten", "ergonomisch"), ("glas en pmd apart sorteren", "milieubewust"), ("niet meer zeep gebruiken dan nodig", "economisch")],
            "Economisch of kostenbewust handelen let op materiaal en tijd."),
    tabel("Is dit een factor van kwaliteitsbewust handelen?",
          [("veilig handelen", J), ("zo snel mogelijk werken", F), ("methodisch handelen", J), ("belevingsgericht handelen", J)],
          "Snelheid staat niet in het rijtje van zeven."),
    inv("Hoeveel factoren heeft kwaliteitsbewust handelen? Een getal.", ["7", "zeven"], "Zeven."),
    tabel("Hoort dit bij respectvol handelen?",
          [("respect voor jezelf", J), ("respect voor het materiaal", J), ("respect voor het weer", F), ("respect voor anderen", J)],
          "Respect gaat in drie richtingen."),
    sorteer("Wat hoort bij de belevingswereld van meneer Jacobs?", ["gevoel", "nood", "wens", "beperking"],
            [("hij is vandaag verdrietig", "gevoel"), ("hij heeft dorst", "nood"), ("hij wil graag naar buiten", "wens"), ("hij hoort slecht", "beperking")],
            "Gevoelens, noden, wensen en beperkingen vormen de belevingswereld."),
    mk("Mevrouw Lambrechts wil haar soep liever lauw. Je zet ze toch heet op tafel, omdat dat zo hoort. Welke factor vergeet je?",
       ["belevingsgericht", "milieubewust handelen", "ergonomisch handelen", "economisch handelen"],
       0, "Je houdt rekening met de wensen van de ander."),
    volgorde("Zet de stappen van het OVUR-schema in de juiste volgorde.",
             ["oriënteren", "voorbereiden", "uitvoeren", "reflecteren"],
             "Eerst nagaan wat de opdracht precies is."),
    koppel("Koppel de vraag aan de stap van OVUR.",
           [("Wat is de opdracht precies?", "oriënteren"), ("Wat heb ik nodig?", "voorbereiden"), ("Ging het goed, wat doe ik een volgende keer anders?", "reflecteren")],
           ["recycleren"],
           "Recycleren hoort bij de Ladder van Lansink."),
    tabel("Is dit een huishoudelijke taak?",
          [("maaltijdzorg", J), ("linnenzorg", J), ("de boekhouding", F), ("interieurzorg", J)],
          "De drie huishoudelijke taken zijn maaltijd-, interieur- en linnenzorg."),
    volgorde("Zet de vijf S'en in de juiste volgorde.",
             ["scheiden", "schikken", "schoonmaken", "standaardiseren", "standhouden"],
             "Scheiden en schikken organiseren, schoonmaken inspecteert, de laatste twee onderhouden."),
    mk("In de berging leg je alle dweilen, emmers en sponzen telkens op een vaste plaats met een etiketje. Welke S is dat vooral?",
       ["schikken", "scheiden", "schoonmaken", "standhouden"],
       0, "Schikken: alles krijgt een vaste plaats."),
    keuze("Bij standaardiseren [[*leg je de goede manier vast voor iedereen|gooi je wat je niet nodig hebt weg|maak je de werkplek schoon]].",
          "Zo doet iedereen het telkens op dezelfde manier."),
    tabel("Wat lees je af van het etiket van een schoonmaakproduct?",
          [("de dosering", J), ("de gevarensymbolen", J), ("de prijs in elke winkel", F), ("het gebruik", J)],
          "Ook de veiligheidsaanduidingen staan erop."),
    volgorde("Zet de manier om een zware doos op te tillen in de juiste volgorde.",
             ["zak door je knieën", "neem de doos dicht bij je lichaam", "kom recht met een rechte rug"],
             "Hou je rug recht en de last dicht bij je lichaam."),
    tabel("Hoort dit bij ergonomisch handelen?",
          [("een goede zithouding", J), ("de schikking van je werkpost", J), ("enkel het tillen", F), ("een goede stahouding", J)],
          "Ergonomie stemt het werk af op het lichaam."),
    mk("Je gebruikt het strijkijzer de hele tijd en de kleerhangers af en toe. Wat leg je het dichtst bij je?",
       ["het strijkijzer", "de kleerhangers", "allebei even ver", "de wasmand met vuile was"],
       0, "Je houdt rekening met de gebruiksfrequentie en de reikwijdte."),
    volgorde("Zet de Ladder van Lansink van beste naar slechtste manier.",
             ["preventie", "hergebruiken", "recycleren", "verbranden"],
             "Afval voorkomen is het beste."),
    sorteer("In welke afvalcategorie hoort dit?", ["gft", "pmd", "kga", "papier en karton"],
            [("een bananenschil", "gft"), ("een leeg melkpak", "pmd"), ("een lege batterij", "kga"), ("een oude krant", "papier en karton"), ("een plastic fles", "pmd")],
            "Een batterij is klein gevaarlijk afval."),
    mk("Je neemt een herbruikbare drinkfles mee in plaats van elke dag een blikje te kopen. Welke trede van de Ladder van Lansink is dat?",
       ["preventie", "recycleren", "verbranden", "hergebruiken"],
       0, "Je voorkomt dat er afval ontstaat."),
    casus("In het woonzorgcentrum maakt Jana de kamer van een bewoner schoon. Ze neemt een nieuwe fles ontkalker, leest het etiket niet, giet er royaal van in een emmer en sleurt de volle emmer met een kromme rug de trap op.", [
        tabel("Klopt dit over hoe Jana werkte?",
              [("Ze handelde veilig.", F), ("Ze tilde ergonomisch.", F), ("Ze gebruikte meer product dan nodig.", J)],
              "Ze leest het etiket niet, tilt verkeerd en gebruikt te veel product."),
        keuze("Op het etiket had ze de [[*dosering|houdbaarheid van de emmer|kleur van de vloer]] kunnen lezen.", "Ook de gevarensymbolen staan erop."),
        mk("Wat had Jana beter gedaan met de volle emmer?",
           ["door de knieën zakken, emmer dicht bij het lichaam", "de emmer met gestrekte armen ver voor zich uit dragen", "de emmer met een kromme rug veel sneller de trap op dragen", "de emmer met één vinger aan het hengsel snel optillen"],
           0, "Rug recht, last dicht bij het lichaam."),
    ]),
    keuze("Hygiënisch handelen betekent dat je zo werkt dat [[*ziektekiemen zich niet verspreiden|je zo weinig mogelijk tijd verliest|het materiaal lang meegaat]].",
          "Handen wassen is daar het bekendste voorbeeld van."),
    tabel("Klopt dit over de gevarentekens?",
          [("Een reddingsteken is groen.", J), ("Een gebodsteken is een rode cirkel met een streep.", F), ("Een verbodsteken zegt dat iets niet mag.", J)],
          "Een gebodsteken is een blauwe cirkel."),
    keuze("Kostenbewust handelen let op de kosten van het materiaal én van de [[*tijd|kleur|geur]] die je besteedt.",
          "Zuinig omgaan met materiaal en tijd."),
    open_("Leg uit waarom je bij het schoonmaken methodisch werkt. Gebruik het OVUR-schema.",
          "Je werkt volgens een vast plan, zodat je niets vergeet. Je oriënteert eerst wat er moet gebeuren, bereidt je materiaal voor, voert het werk uit en reflecteert daarna of het goed ging."),
]
