"""Woordvelden: school, werk, reizen en de samenleving — pittig (🚀 Boost doorstroom, Frans).

Eigen vragen strikt binnen fr_wereld: school, beroepen en werk, vervoer en
reizen, landen, winkels, multimedia, de instructietaal, getallen, maten,
het uur, plaats en het weer. Met een zelfgetekende weerkaart."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, BLAUW

WK = Prent("weerkaart-vier-steden", "La météo de demain", "vier vakjes met een weersymbool en een temperatuur, letters A tot D")
VAK = [("A", 80, 90), ("B", 530, 90), ("C", 80, 360), ("D", 530, 360)]
for t, x, y in VAK:
    WK.rect(x, y, 390, 240, "#ffffff", DONKER, 14, 3)
    WK.letter(x + 35, y + 35, t)


def wolk(p, x, y, kl=GRIJS):
    p.cirkel(x - 40, y, 32, kl, DONKER, 2); p.cirkel(x + 5, y - 20, 42, kl, DONKER, 2); p.cirkel(x + 50, y, 32, kl, DONKER, 2)
    p.rect(x - 40, y, 90, 32, kl, kl, 0, 0); p.lijn(x - 72, y + 32, x + 82, y + 32, DONKER, 2)


# A: zon, 28 graden
WK.cirkel(275, 200, 50, GEEL, DONKER, 3)
for dx, dy in ((0, -80), (0, 80), (-80, 0), (80, 0), (57, 57), (-57, -57), (57, -57), (-57, 57)):
    WK.lijn(275 + dx * 0.75, 200 + dy * 0.75, 275 + dx, 200 + dy, DONKER, 4)
WK.tekst(420, 300, "28°", 30, vet=True)
# B: regen, 12 graden
wolk(WK, 720, 180)
for dx in (-40, 0, 40):
    WK.lijn(720 + dx, 230, 710 + dx, 265, BLAUW, 5)
WK.tekst(870, 300, "12°", 30, vet=True)
# C: sneeuw, -3 graden
wolk(WK, 270, 450, "#ffffff")
for dx in (-40, 0, 40):
    WK.tekst(270 + dx, 545, "*", 44, kleur=BLAUW, vet=True)
WK.tekst(420, 570, "−3°", 30, vet=True)
# D: wind, 9 graden
for i, yy in enumerate((440, 480, 520)):
    WK.pad(f"M 620 {yy} C 700 {yy - 20} 760 {yy + 20} 840 {yy - 10}", "none", DONKER, 5)
WK.tekst(870, 570, "9°", 30, vet=True)
U = "weerkaart-vier-steden.svg"
Z = {t: [Prent.zone(x, y, 390, 240)] for t, x, y in VAK}

STAGE = ("Lees de advertentie.\n\n"
         "« La boulangerie Martin cherche un ou une stagiaire pour l'été (du 1er au 31 juillet). "
         "Horaire : du mardi au samedi, de 6 h à 13 h. Vous aidez à préparer le pain et vous servez les clients à la caisse. "
         "Pas besoin d'expérience, mais vous devez être poli et ponctuel. Envoyez votre CV par mail avant le 15 juin. "
         "Entretien d'embauche fin juin. »")

VRAGEN = [
    klik("Bekijk de weerkaart. Klik op het vakje waar het morgen sneeuwt.", U, Z["C"], "Il neige: het sneeuwt."),
    klik("Klik op het vakje waar het morgen regent.", U, Z["B"], "Il pleut: het regent."),
    klik("Klik op het vakje bij: 'Il fait chaud et le soleil brille.'", U, Z["A"], "Il fait chaud: het is warm."),
    klik("Klik op het vakje bij: 'Il y a du vent et il fait frais.'", U, Z["D"], "Il y a du vent: het waait."),
    casus(STAGE, [
        tabel("Klopt dit volgens de advertentie?",
              [("De stage duurt een maand.", J), ("Je werkt ook op zondag.", F), ("Je moet al ervaring hebben.", F), ("Je moet beleefd en stipt zijn.", J)],
              "Du mardi au samedi. Pas besoin d'expérience: geen ervaring nodig."),
        inv("Hoeveel uur werk je per dag? Schrijf het cijfer.", ["7"], "Van 6 tot 13 uur is zeven uur."),
        keuze("'Une caisse' is [[*een kassa|een doos|een keuken]].", "Servir les clients à la caisse: de klanten aan de kassa helpen."),
        keuze("'Un entretien d'embauche' is [[*een sollicitatiegesprek|een stagecontract|een loonbrief]].", "Embaucher: aanwerven."),
        mk("Wat moet je vóór 15 juni doen?",
           ["je cv mailen", "naar de bakkerij gaan voor een sollicitatiegesprek", "brood bakken als proef voor de bakker", "je inschrijven op de school van de bakker"],
           0, "Envoyez votre CV par mail avant le 15 juin."),
    ]),
    sorteer("Wat vraagt de opdracht?", ["iets aanduiden", "zelf iets schrijven"],
            [("cochez", "iets aanduiden"), ("soulignez", "iets aanduiden"), ("entourez", "iets aanduiden"), ("rédigez", "zelf iets schrijven"), ("décrivez", "zelf iets schrijven"), ("complétez", "zelf iets schrijven")],
            "Cocher is aankruisen, entourer omcirkelen, rédiger opstellen."),
    koppel("Koppel de opdracht aan de betekenis.",
           [("barrez", "doorstrepen"), ("reliez", "verbinden"), ("justifiez", "verantwoorden"), ("soulignez", "onderlijnen")],
           ["vertalen"],
           "Wie de instructietaal kent, verliest geen punten."),
    sorteer("En of à?", ["en", "à"],
            [("… train", "en"), ("… pied", "à"), ("… vélo", "à"), ("… avion", "en"), ("… voiture", "en"), ("… cheval", "à")],
            "En als je erin zit, à als je erop zit."),
    sorteer("En, au of de?", ["en", "au", "de"],
            [("J'habite … Belgique.", "en"), ("Il habite … Maroc.", "au"), ("Elle vient … France.", "de"), ("Nous allons … Italie.", "en"), ("Ils vont … Canada.", "au")],
            "En bij vrouwelijke landen, au bij mannelijke; de France zonder lidwoord."),
    tabel("Valse vrienden: klopt dit?",
          [("Passer un examen is slagen.", F), ("Réussir un examen is slagen.", J), ("Un car is een personenwagen.", F), ("Une livre is een pond.", J)],
          "Passer is afleggen; un car is een bus."),
    mk("Hoe schrijf je 92 zoals men het in Frankrijk zegt?",
       ["quatre-vingt-douze", "nonante-deux", "quatre-vingts-douze", "soixante-trente-deux"],
       0, "Vier keer twintig plus twaalf; geen s want er volgt nog een getal."),
    keuze("Je schrijft 3,5 kilo in het Frans als [[*3,5 kg|3.5 kg]].", "Het Frans gebruikt een komma: trois virgule cinq."),
    inv("Vul in: Il y a trop … voitures en ville. Eén woord.", ["de"], "Na een hoeveelheid: trop de, sans lidwoord."),
    mk("Het is 16.45 u. Hoe zeg je het in een gesprek?",
       ["Il est cinq heures moins le quart.", "Il est quatre heures et demie.", "Il est quatre heures moins le quart.", "Il est seize heures et quart."],
       0, "Kwart voor vijf: cinq heures moins le quart."),
    inv("Een uurrooster zegt 'quinze heures trente'. Hoe laat is dat? Schrijf zo: 15.30", ["15.30", "15u30", "15:30", "15 u 30", "15h30"], "Uurroosters tellen tot 24."),
    sleep("Een treinreis: Je voudrais un [[aller-retour]] pour Paris. Le train a dix minutes de [[retard]], et à Lille, j'ai une [[correspondance]].",
          ["horaire", "caisse"], "Aller-retour: heen en terug. Une correspondance: een overstap."),
    keuze("'Il fait un temps de chien' betekent [[*het is hondenweer|het is warm|de hond loopt buiten]].", "Slecht weer."),
    tabel("Hoort het woord bij multimedia?",
          [("un mot de passe", J), ("une pièce jointe", J), ("une étagère", F), ("un écran", J)],
          "Une étagère is een rek."),
    mk("Je ziet in een winkel: 'Réduction de 20 % à la caisse.' Wat betekent dat?",
       ["je krijgt 20 % korting aan de kassa", "je moet aan de kassa 20 % meer betalen", "de kassa is 20 minuten gesloten", "je mag maar 20 stuks kopen"],
       0, "Une réduction: een korting."),
    inv("Vul in: Demain, il va … . Morgen gaat het regenen. Eén werkwoord.", ["pleuvoir"], "Na aller komt de infinitief."),
    mk("Waarom schrijf je 'un étudiant belge' maar 'un Belge'?",
       ["als bijvoeglijk naamwoord krijgt het een kleine letter", "in het Frans is belge altijd een vrouwelijk woord, ook bij een man", "de eerste zin staat in de verleden tijd", "Belge met een hoofdletter is enkel voor vrouwen"],
       0, "Als zelfstandig naamwoord krijgt het een hoofdletter."),
    open_("Schrijf in het Frans twee zinnen over hoe je naar school komt en hoe lang dat duurt.",
          "Je vais à l'école à vélo. Le trajet dure vingt minutes."),
    keuze("Elle travaille comme [[*infirmière|une infirmière|l'infirmière]] à l'hôpital.", "Na comme komt geen lidwoord."),
    mk("'Il est au chômage depuis six mois.' Wat betekent dat?",
       ["hij is al zes maanden werkloos", "hij werkt al zes maanden in een winkel", "hij is al zes maanden op reis", "hij zit al zes maanden op school"],
       0, "Être au chômage: werkloos zijn."),
    sorteer("Welk woordveld: school, werk of reizen?", ["school", "werk", "reizen"],
            [("un bulletin", "school"), ("une interrogation", "school"), ("un plombier", "werk"), ("un emploi", "werk"), ("une auberge de jeunesse", "reizen"), ("un aller simple", "reizen")],
            "Un bulletin is een rapport, une interrogation een toets."),
    keuze("'Le temps' in 'Je n'ai pas le temps' gaat over [[*de tijd|het weer]].", "Quel temps fait-il gaat over het weer."),
]
