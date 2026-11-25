"""Futur, conditionnel en subjonctif — pittig (🚀 Boost doorstroom, Frans).

Eigen vragen strikt binnen fr_toekomst: de futur simple (regelmatig en
onregelmatige stammen), quand + futur, de conditionnel (beleefd, voorwaarde,
onbevestigd nieuws), de subjonctif (vorming, wanneer, infinitief in de plaats)
en de wijzen. Met een zelfgetekend prikbord met vijf berichtjes."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GEEL, LICHTGROEN, ORANJE, BLAUW

PB = Prent("prikbord-berichtjes", "Le tableau d'affichage de l'école", "een prikbord met vijf briefjes, letters A tot E")
PB.rect(40, 55, 920, 570, "#d9b38c", DONKER, 10, 4)
BR = [("A", 70, 85, GEEL, ["Le voyage à Paris", "aura lieu le 4 mai."]),
      ("B", 520, 85, "#ffffff", ["Pourriez-vous rendre", "vos livres avant vendredi ?"]),
      ("C", 70, 265, "#9ec7e6", ["Selon la radio, la grève", "durerait encore deux jours."]),
      ("D", 520, 265, LICHTGROEN, ["Il faut que tous les élèves", "soient là à 8 h 15."]),
      ("E", 295, 445, ORANJE, ["Quand il fera beau, nous", "mangerons dans la cour."])]
for t, x, y, kl, rr in BR:
    PB.rect(x, y, 410, 150, kl, DONKER, 4, 2)
    PB.cirkel(x + 205, y + 8, 8, "#b03a2e", DONKER, 1)
    PB.letter(x + 30, y + 35, t)
    for i, r in enumerate(rr):
        PB.tekst(x + 60, y + 75 + i * 32, r, 21, "start")
U = "prikbord-berichtjes.svg"
Z = {t: [Prent.zone(x, y, 410, 150)] for t, x, y, *_ in BR}

VRAGEN = [
    klik("Bekijk het prikbord. Klik op het briefje met nieuws dat nog niet zeker is.", U, Z["C"], "Durerait: de conditionnel voor onbevestigd nieuws."),
    klik("Klik op het briefje met een beleefde vraag in de conditionnel.", U, Z["B"], "Pourriez-vous: zou u kunnen."),
    klik("Klik op het briefje met een subjonctif.", U, Z["D"], "Il faut que … soient: subjonctif van être."),
    klik("Klik op het briefje met twee keer een futur simple, waar het Nederlands een tegenwoordige tijd zou gebruiken.", U, Z["E"], "Quand il fera beau: na quand de futur."),
    sorteer("Welke stam in de futur?", ["ir-", "aur-", "ser-", "fer-", "viendr-"],
            [("aller", "ir-"), ("avoir", "aur-"), ("être", "ser-"), ("faire", "fer-"), ("venir", "viendr-")],
            "Een kleine groep veelgebruikte werkwoorden heeft een eigen stam."),
    inv("Zet in de futur simple: ils (vendre) leur maison. Eén werkwoordsvorm.", ["vendront"], "Bij -re valt de e weg: vendr- + -ont."),
    inv("Zet in de futur simple: tu (voir) la mer. Eén werkwoordsvorm.", ["verras"], "Voir heeft de stam verr-."),
    keuze("Quand tu [[*arriveras|arrives]] à Lyon, appelle-moi.", "Na quand de futur als het over de toekomst gaat."),
    sorteer("Futur simple of conditionnel?", ["futur simple", "conditionnel"],
            [("je parlerai", "futur simple"), ("je parlerais", "conditionnel"), ("nous irons", "futur simple"), ("nous irions", "conditionnel"), ("il pourra", "futur simple"), ("il pourrait", "conditionnel")],
            "-ai, -ons, -a: futur. -ais, -ions, -ait: conditionnel."),
    mk("'Je parlerais' — hoe is die vorm gebouwd?",
       ["stam van de futur + uitgang van de imparfait", "stam van de imparfait + uitgang van de futur", "infinitief + uitgang van de présent", "stam van de présent + uitgang van de subjonctif"],
       0, "Parler- + -ais."),
    keuze("[[*J'aimerais|J'aimerai|J'aime]] réserver une chambre pour deux nuits, s'il vous plaît.", "Ik zou graag: conditionnel."),
    mk("Een krant schrijft: 'L'incendie aurait fait deux blessés.' Wat bedoelt de krant?",
       ["er zouden twee gewonden zijn, maar het is nog niet zeker", "er zullen morgen zeker twee gewonden vallen in het ziekenhuis", "er waren zeker twee gewonden, dat is bevestigd", "er waren helemaal geen gewonden bij de brand"],
       0, "De conditionnel voor nieuws dat nog niet bevestigd is."),
    inv("Zet in de subjonctif: il faut que nous (finir) ce travail. Eén werkwoordsvorm.", ["finissions"], "Ils finissent geeft finiss- + -ions."),
    sorteer("Indicatif of subjonctif na deze uitdrukking?", ["indicatif", "subjonctif"],
            [("je pense que", "indicatif"), ("il faut que", "subjonctif"), ("il m'a dit que", "indicatif"), ("bien que", "subjonctif"), ("parce que", "indicatif"), ("pour que", "subjonctif")],
            "Gevoel, wil, twijfel en noodzaak vragen de subjonctif."),
    keuze("Je ne pense pas qu'il [[*ait|a]] raison.", "In de ontkenning komt er twijfel bij."),
    keuze("Il est certain qu'il [[*pleuvra|pleuve]] demain.", "Zekerheid vraagt de indicatif."),
    keuze("Il est possible qu'il [[*pleuve|pleuvra]] demain.", "Twijfel vraagt de subjonctif."),
    mk("Welke zin over het vertrek is juist?",
       ["Je suis contente de partir.", "Je suis contente que je parte.", "Je suis contente que je pars.", "Je suis contente de que partir."],
       0, "Zelfde onderwerp: de + infinitief."),
    inv("Vul de subjonctif van aller in: Il faut que nous … à la banque.", ["allions"], "Que nous allions: bij nous en vous de stam all-."),
    sleep("Mijn moeder zegt: Je veux que tu [[sois]] poli, que tu [[fasses]] tes devoirs et que tu [[aies]] de bonnes notes.",
          ["es", "fais"], "Être, faire en avoir hebben een onregelmatige subjonctif."),
    keuze("Bien qu'elle [[*soit|est]] malade, elle vient à l'école.", "Bien que: hoewel, altijd met de subjonctif."),
    tabel("Klopt dit over futur en subjonctif?",
          [("De uitgangen van de futur zijn de présent van avoir.", J), ("De imparfait heeft een r voor de uitgang.", F), ("De subjonctif vertrekt van de ils-vorm.", J), ("Je partirai is losser dan je vais partir.", F)],
          "De futur proche klinkt losser."),
    mk("'Si j'avais le temps, je viendrais.' Waarom staat viendrais in de conditionnel?",
       ["het hangt af van een voorwaarde", "het is een beleefde vraag aan iemand", "het gaat zeker gebeuren", "het gebeurde al gisteren"],
       0, "Si + imparfait, en dan de conditionnel."),
    keuze("Il [[*faudrait|faut]] partir plus tôt, mais ce n'est pas obligatoire.", "Il faudrait klinkt zachter."),
    tabel("Welke wijze?",
          [("que tu viennes", "subjonctif"), ("tu viendrais", "conditionnel"), ("viens !", "impératif"), ("tu viens", "indicatif")],
          "Vijf wijzen: indicatif, impératif, infinitif, subjonctif, conditionnel.", ["indicatif", "subjonctif", "conditionnel", "impératif"]),
    inv("Zet in de conditionnel: nous (devoir) partir. Eén werkwoordsvorm.", ["devrions"], "Devoir heeft de stam devr-."),
    open_("Schrijf in het Frans twee zinnen over wat je zal doen als je klaar bent met school. Begin met 'Quand'.",
          "Quand je serai grand, je voyagerai en Afrique. Ensuite, je travaillerai dans un hôpital."),
    inv("Zet in de futur simple: vous (avoir) le temps. Eén werkwoordsvorm.", ["aurez"], "Avoir heeft de stam aur-."),
    keuze("Elle veut que nous [[*partions|partons]] tout de suite.", "Vouloir que + subjonctif."),
    mk("Hoe zeg je 'ik zal lopen' (courir) in de futur simple?",
       ["je courrai", "je courirai", "je courais", "je courerai"],
       0, "Courir heeft een stam met dubbele r: courr-."),
]
