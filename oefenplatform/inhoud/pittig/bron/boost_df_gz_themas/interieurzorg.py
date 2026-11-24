"""Interieurzorg: ruimtes, vuil en technieken — pittig (🛠️ Boost dubbele finaliteit, gezondheidszorg en welzijn).

Eigen vragen strikt binnen gz_interieurzorg, met een zelfgetekend grondplan
van een woning."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL

GP = Prent("grondplan-woning", "Grondplan van een woning", "zes ruimtes zonder naam: met een bed, met een bad en toilet, met een fornuis, met een zetel, een smalle ruimte met een trap, en een ruimte met rekken, met letters A tot F")
MUUR = 4
GP.rect(60, 60, 880, 520, "#fbfaf6", DONKER, 0, 6)
GP.lijn(380, 60, 380, 580, DONKER, MUUR); GP.lijn(620, 60, 620, 580, DONKER, MUUR)
GP.lijn(60, 320, 380, 320, DONKER, MUUR); GP.lijn(620, 320, 940, 320, DONKER, MUUR); GP.lijn(380, 320, 620, 320, DONKER, MUUR)
# A slaapkamer (linksboven): bed
GP.rect(110, 110, 150, 190, "#dfe8f5", DONKER, 8, 2); GP.rect(125, 120, 120, 40, "white", DONKER, 8, 2)
# B badkamer (linksonder): bad en toilet
GP.rect(90, 360, 200, 90, "#d8eef5", DONKER, 30, 2); GP.ellips(320, 520, 28, 38, "white", DONKER, 2)
# C gang met trap (midden)
for y in range(110, 300, 24):
    GP.lijn(420, y, 580, y, "#888", 3)
# D keuken (rechtsboven): fornuis
GP.rect(700, 90, 180, 110, "#eee", DONKER, 6, 2)
for x, y in ((745, 125), (835, 125), (745, 170), (835, 170)):
    GP.cirkel(x, y, 16, "none", DONKER, 3)
# E woonkamer (rechtsonder): zetel
GP.rect(690, 470, 220, 70, "#e9d8c4", DONKER, 14, 2); GP.rect(690, 440, 220, 35, "#d9c2a8", DONKER, 10, 2)
# F berging (midden onder): rekken
for y in (380, 440, 500):
    GP.rect(420, y, 160, 18, "#c9a878", DONKER, 2, 2)
LET = {"A": (310, 230), "B": (180, 520), "C": (500, 300), "D": (780, 260), "E": (780, 380), "F": (500, 540)}
for t, (x, y) in LET.items():
    GP.letter(x, y, t)
U = "grondplan-woning.svg"
ZK = {"A": Prent.zone(60, 60, 320, 260), "B": Prent.zone(60, 320, 320, 260), "C": Prent.zone(380, 60, 240, 260),
      "D": Prent.zone(620, 60, 320, 260), "E": Prent.zone(620, 320, 320, 260), "F": Prent.zone(380, 320, 240, 260)}

VRAGEN = [
    klik("Klik op de verkeersruimte: daar passeer je, je blijft er niet.", U, [ZK["C"]],
         "De gang, de hal en de trap zijn verkeersruimtes."),
    klik("Klik op de bergruimte.", U, [ZK["F"]],
         "De kelder, de zolder en de berging dienen om spullen op te bergen."),
    klik("Klik op de sanitaire ruimte.", U, [ZK["B"]],
         "Sanitair zijn het bad en het toilet."),
    klik("Klik op de ruimte die je elke dag schoonmaakt omdat er met voedsel gewerkt wordt.", U, [ZK["D"]],
         "In de keuken is de graad van hygiëne hoog."),
    klik("Klik op een woonruimte.", U, [ZK["E"]],
         "De woonkamer is een woonruimte. De slaapkamer is een slaapruimte."),
    sorteer("Welk soort ruimte is dit?", ["woonruimte", "slaapruimte", "sanitaire ruimte", "verkeersruimte", "bergruimte"],
            [("de woonkamer", "woonruimte"), ("de kinderkamer", "slaapruimte"), ("het toilet", "sanitaire ruimte"), ("de hal", "verkeersruimte"), ("de zolder", "bergruimte"), ("de trap", "verkeersruimte")],
            "De keuken en bijkeuken vormen een eigen groep."),
    tabel("Is dit een taak van de interieurzorg?",
          [("ruimtes onderhouden", J), ("planten verzorgen", J), ("hemden strijken", F), ("dieren verzorgen", J)],
          "Strijken hoort bij de linnenzorg."),
    sorteer("Reinigen of schoonmaken?", ["reinigen", "schoonmaken"],
            [("de badkamer", "schoonmaken"), ("een vaas", "reinigen"), ("de slaapkamer", "schoonmaken"), ("een lamp", "reinigen")],
            "Je reinigt een voorwerp en je maakt een ruimte schoon."),
    sorteer("Welk soort onderhoud is dit?", ["dagelijks", "periodiek", "specifiek"],
            [("het aanrecht na het koken", "dagelijks"), ("de grote schoonmaak in de lente", "periodiek"), ("de kamer na een buikgriep", "specifiek"), ("elke week de ramen", "periodiek"), ("de feestzaal na een verjaardagsfeest", "specifiek")],
            "Specifiek onderhoud doe je bij een bijzondere aanleiding."),
    tabel("Hangt de onderhoudsfrequentie hiervan af?",
          [("het gebruiksdoel", J), ("de bezettingsgraad", J), ("de poetsnorm van de bewoner", J), ("de kleur van de muren", F)],
          "Ook de graad van hygiëne speelt mee."),
    mk("De refter van een school met 300 leerlingen wordt sneller vuil dan een vergaderzaal voor vijf. Welke factor speelt hier vooral?",
       ["de bezettingsgraad", "de poetsnorm", "de kleur van de vloer", "de grootte van de ramen"],
       0, "Hoe meer mensen er gebruik van maken, hoe sneller de ruimte vuil wordt."),
    mk("Mevrouw Claes vindt haar kamer pas proper als alles blinkt, haar buurman vindt een beetje stof niet erg. Wat verschilt?",
       ["hun poetsnorm", "hun bezettingsgraad", "het gebruiksdoel van hun kamer", "de graad van hygiëne in de keuken"],
       0, "De poetsnorm is wat iemand proper vindt."),
    sorteer("Welk soort vuil is dit?", ["droog vuil", "aangekleefd vuil", "ingedrongen vuil", "onzichtbaar vuil"],
            [("kruimels op tafel", "droog vuil"), ("een opgedroogde druppel op het aanrecht", "aangekleefd vuil"), ("een ingetrokken vetvlek in de zetel", "ingedrongen vuil"), ("bacteriën op een kraan", "onzichtbaar vuil"), ("haren op de vloer", "droog vuil")],
            "Onzichtbaar vuil zie je niet, maar het is er wel."),
    mk("Waarom poets je ook een kraan die er proper uitziet?",
       ["er kan onzichtbaar vuil op zitten", "het staat zo in de poetsnorm van elk huis", "een kraan wordt anders snel roestig", "dan blinkt hij nog meer"],
       0, "Net het vuil dat je niet ziet, de kiemen, maakt mensen ziek."),
    koppel("Koppel het vuil aan de beste techniek.",
           [("stof op een kast", "droog schoonmaken"), ("kiemen op een snijplank", "ontsmetten"), ("vingerafdrukken op een deur", "klam vochtig schoonmaken")],
           ["opwarmen"],
           "Opwarmen is geen schoonmaaktechniek."),
    tabel("Klopt dit over schoonmaaktechnieken?",
          [("Droog vuil verwijder je met veel water.", F), ("Ontsmetten doe je nadat je hebt schoongemaakt.", J), ("Bij klam vochtig schoonmaken wordt het oppervlak nat.", F)],
          "De doek is net vochtig genoeg om het vuil mee te nemen."),
    keuze("Een ontsmettingsmiddel werkt niet door [[*een laag vuil|een open raam|een propere doek]] heen.",
          "Daarom maak je eerst schoon."),
    tabel("Is dit een factor van de Sinner-cirkel?",
          [("tijd", J), ("chemie", J), ("temperatuur", J), ("mechanische handeling", J), ("de kleur van het product", F)],
          "Tijd, chemie, temperatuur en mechanische handeling bepalen samen het resultaat."),
    mk("Je gebruikt minder schoonmaakproduct. Wat moet je volgens de Sinner-cirkel doen?",
       ["meer tijd, warmte of wrijving inzetten", "kouder water gebruiken", "minder lang poetsen", "het product verdunnen met nog meer water"],
       0, "Je vult de ene factor aan met de andere."),
    mk("Je poetst een vettige kookplaat. Waarom neem je warm water in plaats van koud?",
       ["vet en vuil lossen sneller op", "warm water bevat meer zeep", "koud water doodt de kiemen niet", "warm water droogt meteen op"],
       0, "Warmte maakt vuil losser."),
    keuze("Wrijven, borstelen en draaien horen bij de [[*mechanische handeling|chemie|temperatuur]] van de Sinner-cirkel.",
          "De vierde factor naast tijd, chemie en temperatuur."),
    inv("Hoe noem je de cirkel met tijd, chemie, temperatuur en mechanische handeling? Hoogstens twee woorden.",
        ["sinner-cirkel", "de sinner-cirkel", "sinnercirkel", "sinner cirkel"],
        "De Sinner-cirkel."),
    casus("Lars werkt als poetshulp bij een gezin. Hij veegt het stof van de kast met een natte doek, ontsmet het toilet voor hij het schoonmaakt en poetst de badkamer maar één keer per maand.", [
        tabel("Wat doet Lars fout?",
              [("stof met een natte doek afnemen", J), ("ontsmetten voor het schoonmaken", J), ("de badkamer te weinig onderhouden", J), ("het toilet ontsmetten", F)],
              "Het toilet ontsmetten is goed, maar pas na het schoonmaken."),
        keuze("Stof op een kast haalt Lars beter [[*droog|nat|met bleekwater]] weg.", "Anders smeert hij het uit tot een vlek."),
        mk("Waarom vraagt een badkamer meer onderhoud dan een zolder?",
           ["het gebruiksdoel en de hygiëne liggen hoger", "een zolder is altijd veel vochtiger en kouder", "de bewoner gaat bijna nooit naar de badkamer", "een badkamer heeft meer ramen dan een zolder"],
           0, "Sanitaire ruimtes vragen een hoge graad van hygiëne."),
    ]),
    tabel("Klopt dit over onderhoud?",
          [("De grote schoonmaak is periodiek onderhoud.", J), ("Een badkamer vraagt vaker onderhoud dan een zolder.", J), ("De keuken is een sanitaire ruimte.", F)],
          "Sanitair zijn het bad en het toilet."),
    inv("Hoe noem je de soort ruimte waar je enkel passeert, zoals de hal? Eén woord.", ["verkeersruimte", "verkeersruimtes", "een verkeersruimte"], "Een verkeersruimte."),
    keuze("Onderhoud dat wekelijks of maandelijks terugkomt, heet [[*periodiek|specifiek|dagelijks]] onderhoud.", "Tot en met de grote schoonmaak."),
    keuze("Ingedrongen vuil zit [[*diep in het materiaal|los op het oppervlak|enkel in de lucht]].", "Zoals een ingetrokken vetvlek."),
    open_("Leg uit wat de bezettingsgraad is en waarom die de onderhoudsfrequentie mee bepaalt.",
          "De bezettingsgraad is hoeveel mensen een ruimte gebruiken. Hoe meer mensen er komen, hoe sneller de ruimte vuil wordt, en hoe vaker je ze moet onderhouden."),
]
