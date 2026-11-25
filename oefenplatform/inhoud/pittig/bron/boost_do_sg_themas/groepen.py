"""Sociale groepen en de typologie van Merton — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_groepen: primaire en secundaire groepen,
formele en informele groepen, en de typologie van Merton. Met vier
zelfgetekende taferelen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, ROOD, BLAUW, LICHTGROEN, ORANJE

MT = Prent("vier-taferelen-merton", "Vier taferelen", "vier vakjes met mensen, letters A tot D")
VAK = [("A", 40, 60), ("B", 520, 60), ("C", 40, 340), ("D", 520, 340)]
for t, x, y in VAK:
    MT.rect(x, y, 440, 260, "#ffffff", DONKER, 12, 3)
    MT.letter(x + 410, y + 230, t)
def mens(x, y, kleur=GRIJS, s=1.0):
    MT.cirkel(x, y, 12 * s, kleur, DONKER, 2); MT.rect(x - 11 * s, y + 13 * s, 22 * s, 32 * s, kleur, DONKER, 5, 2)
# A: gezin rond een tafel
MT.ellips(260, 210, 120, 40, "#e8d3a8", DONKER, 3)
for (px, py) in ((160, 150), (220, 135), (300, 135), (360, 150)):
    mens(px, py)
MT.cirkel(230, 205, 12, "#ffffff", DONKER, 1); MT.cirkel(290, 205, 12, "#ffffff", DONKER, 1)
# B: wachtende mensen bij een bushalte, elk met de rug of kant naar elkaar
MT.lijn(570, 120, 570, 290, DONKER, 4); MT.rect(548, 100, 44, 30, GEEL, DONKER, 4, 2)
for i, k in enumerate((BLAUW, ORANJE, LICHTGROEN, ROOD)):
    mens(640 + i * 70, 205 + (i % 2) * 15, k)
# C: supporters in een tribune met dezelfde sjaal
for r in range(2):
    MT.rect(70, 450 + r * 55, 380, 10, GRIJS, DONKER, 0, 1)
    for i in range(7):
        mens(95 + i * 52, 402 + r * 55, GRIJS, 0.85)
        MT.rect(85 + i * 52, 413 + r * 55, 22, 6, ROOD, DONKER, 1, 1)
# D: raster van gelijke poppetjes met een groot 16-teken (alle zestienjarigen)
for r in range(3):
    for i in range(6):
        MT.cirkel(560 + i * 34, 400 + r * 60, 8, GRIJS, DONKER, 1); MT.rect(553 + i * 34, 409 + r * 60, 14, 22, GRIJS, DONKER, 3, 1)
MT.cirkel(840, 460, 48, GEEL, DONKER, 3); MT.tekst(840, 474, "16", 40, vet=True)
U = "vier-taferelen-merton.svg"
Z = {t: [Prent.zone(x, y, 440, 260)] for t, x, y in VAK}

KLAS = ("Lees het verhaal.\n\n"
        "In september komt een nieuwe klas samen: 22 leerlingen die elkaar niet kennen, met een klastitularis, een uurrooster en een schoolreglement. "
        "In de loop van het jaar groeit er een hecht groepje van vier vriendinnen dat elke woensdag samen gaat zwemmen, zonder vaste afspraken. "
        "Alle leerlingen van de school dragen op de sportdag trots een T-shirt in de schoolkleuren, ook al kennen ze elkaar lang niet allemaal.")

VRAGEN = [
    klik("Bekijk de vier taferelen. Klik op het tafereel dat bij Merton een primaire groep is.", U, Z["A"], "Klein, hecht en met persoonlijk contact."),
    klik("Klik op het tafereel dat bij Merton een samenzijn is.", U, Z["B"], "Alleen de plaats en het moment verbinden hen."),
    klik("Klik op het tafereel dat bij Merton een collectiviteit is.", U, Z["C"], "Gedeelde waarden en een gevoel van samenhoren, zonder elkaar te kennen."),
    klik("Klik op het tafereel dat bij Merton een sociale categorie is.", U, Z["D"], "Eén gedeeld kenmerk, verder niets."),
    casus(KLAS, [
        sorteer("Hoe deel je deze groep in?", ["secundair en formeel", "primair en informeel"],
                [("de nieuwe klas in september", "secundair en formeel"), ("de vier vriendinnen die gaan zwemmen", "primair en informeel")],
                "Primair of secundair gaat over de band, formeel of informeel over de regels."),
        keuze("Het groepje vriendinnen groeit [[*binnen|buiten]] de klas: binnen een secundaire groep kan een primaire groep ontstaan.", "Zoals collega's die vrienden worden."),
        keuze("Alle leerlingen in schoolkleuren, die elkaar niet allemaal kennen maar zich wel verbonden voelen, vormen bij Merton een [[*collectiviteit|samenzijn|primaire groep]].", "Gedeeld gevoel, geen persoonlijk contact met iedereen."),
        mk("Waarom is de klas in september nog geen primaire groep?",
           ["de leerlingen kennen elkaar nog niet", "omdat er te weinig leerlingen in de klas zitten", "omdat er nog geen schoolreglement is", "omdat een klas nooit een groepsgevoel kan krijgen"],
           0, "Een primaire groep heeft een sterke persoonlijke band."),
    ]),
    sorteer("Welke soort van Merton?", ["primaire groep", "collectiviteit", "sociale categorie", "samenzijn"],
            [("een hechte vriendengroep", "primaire groep"), ("alle gelovigen van een godsdienst", "collectiviteit"), ("alle linkshandigen in een land", "sociale categorie"), ("de mensen in een wachtzaal", "samenzijn"), ("alle supporters van dezelfde ploeg", "collectiviteit")],
            "Merton kijkt naar contact en gedeeld gevoel."),
    sorteer("Formeel of informeel?", ["formeel", "informeel"],
            [("een sportclub met statuten", "formeel"), ("buren die samen een straatfeest organiseren zonder statuten", "informeel"), ("een vakbond", "formeel"), ("vrienden die op zaterdag samen gamen", "informeel")],
            "Vastgelegde regels en rollen tegenover spontane groei."),
    tabel("Klopt dit over sociale groepen?",
          [("Een primaire groep heeft veel leden.", F), ("Een groep kan tegelijk secundair en formeel zijn.", J), ("In een informele groep liggen de rollen vooraf vast.", F), ("Een collectiviteit kan miljoenen leden tellen.", J)],
          "Een primaire groep is net klein."),
    keuze("Het verschil tussen primair en formeel: het ene gaat over de [[*band|regels|grootte]], het andere over de regels.", "Twee aparte indelingen."),
    mk("Alle mensen met een zeldzame ziekte vormen eerst gewoon een sociale categorie. Wat maakt er een collectiviteit van?",
       ["ze gaan zich met elkaar verbonden voelen", "ze gaan allemaal in dezelfde straat wonen", "de ziekte verdwijnt bij iedereen tegelijk", "er komen statuten met een voorzitter en secretaris"],
       0, "Zodra mensen met hetzelfde kenmerk zich verbonden voelen."),
    keuze("In een secundaire groep draait het contact om de [[*taak|band zelf|familie]].", "Je werkt samen aan iets."),
    tabel("Is deze soort van Merton zonder persoonlijk contact?",
          [("de collectiviteit", J), ("de sociale categorie", J), ("het samenzijn", J), ("de primaire groep", F)],
          "Enkel de primaire groep heeft persoonlijk contact."),
    volgorde("Zet de soorten van Merton van sterkste naar zwakste band.",
             ["primaire groep", "collectiviteit", "sociale categorie", "samenzijn"],
             "De band loopt af in sterkte."),
    mk("Een opmerking van je beste vriend raakt je meer dan dezelfde opmerking van een onbekende collega. Waarom?",
       ["het contact met je vriend is persoonlijk", "omdat vrienden altijd statuten hebben", "omdat een vriendengroep meer leden heeft dan een bedrijf", "omdat vriendschap op het tertiaire niveau werkt"],
       0, "Wat iemand zegt die je graag ziet, raakt dieper."),
    keuze("Een bedrijf met tweehonderd werknemers is een [[*secundaire|primaire]] groep.", "Groot en doelgericht."),
    sleep("Een [[primaire]] groep is klein en hecht. Een [[formele]] groep heeft vaste regels. Een [[informele]] groep ontstaat spontaan.",
          ["tertiaire", "dominante"], "Twee indelingen naast elkaar."),
    inv("Hoe heet bij Merton een toevallige verzameling mensen op één plek? Eén woord.", ["samenzijn", "een samenzijn", "het samenzijn"], "Mensen in dezelfde bus of lift."),
    tabel("Is deze groep primair?",
          [("het gezin", J), ("een hechte vriendenkring", J), ("een bedrijf met tweehonderd werknemers", F), ("een klein team dat jaren samenwerkt", J)],
          "Weinig leden, persoonlijk contact en een sterke band."),
    keuze("Bij Merton heeft een sociale categorie [[*geen|wel een]] gevoel van samenhoren.", "Ze deelt alleen een kenmerk."),
    mk("Een jeugdwerker wil weten welke groep het gedrag van een jongere het sterkst stuurt. Hoe helpt de indeling van groepen hem?",
       ["je kan hun invloed beter inschatten", "zo weet je meteen wie de leider is", "zo kan je elke groep een cijfer geven", "zo hoef je niet meer met groepen te praten"],
       0, "Een primaire groep stuurt je gedrag sterker dan een samenzijn."),
    keuze("Een school is groot, doelgericht en heeft vastgelegde regels. Ze is dus secundair en [[*formeel|informeel]].", "Beide indelingen tegelijk."),
    keuze("Merton onderscheidt zijn vier soorten aan de hand van het persoonlijk contact en het [[*gedeelde gevoel|aantal leden|gebouw]].", "Is er contact, is er een gedeeld gevoel?"),
    keuze("Een hechte vriendengroep die al jaren samen op reis gaat, zonder vaste afspraken, is primair en [[*informeel|formeel]].", "Hecht en zonder vastgelegde regels."),
    tabel("Is deze groep formeel?",
          [("een school", J), ("een vakbond", J), ("een sportclub met statuten", J), ("een groepje dat spontaan samen voetbalt op het plein", F)],
          "Vastgelegde regels en rollen."),
    mk("Alle fans van een band delen iets wat alle mensen met blauwe ogen niet delen. Wat?",
       ["een gevoel van samenhoren", "een gemeenschappelijk kenmerk dat alle leden delen", "persoonlijk contact tussen alle leden van de groep", "een vaste plaats waar ze samenkomen"],
       0, "Beide delen een kenmerk, maar alleen de collectiviteit deelt een gevoel."),
    keuze("Een samenzijn bestaat [[*alleen zolang mensen op één plek zijn|ook als iedereen weer naar huis is|enkel online]].", "Mensen in dezelfde lift."),
    open_("Geef van jezelf een voorbeeld van een primaire groep en een collectiviteit waartoe je behoort, en leg het verschil uit.",
          "Primaire groep: mijn gezin of mijn beste vrienden, klein en hecht met persoonlijk contact. Collectiviteit: alle supporters van mijn voetbalclub. Ik ken ze niet allemaal, maar we delen een gevoel van samenhoren en dezelfde waarden rond de club."),
]
