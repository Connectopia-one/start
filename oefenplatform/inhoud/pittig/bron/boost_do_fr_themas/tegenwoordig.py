"""Présent, impératif en de wederkerende werkwoorden — pittig (🚀 Boost doorstroom, Frans).

Eigen vragen strikt binnen fr_tegenwoordig: de présent (regelmatig en
onregelmatig), de infinitief na een werkwoord, il faut en devoir, de
impératif, de wederkerende en onpersoonlijke werkwoorden, futur proche en
passé récent, wijzen en tijden. Met een zelfgetekend zwembadreglement."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, BLAUW

RG = Prent("reglement-zwembad", "Piscine communale – Règlement", "een bord met vijf regels, letters A tot E")
RG.rect(60, 55, 880, 570, "#eaf4fb", BLAUW, 14, 5)
RG.tekst(500, 110, "RÈGLEMENT", 34, vet=True, kleur=BLAUW)
RL = [("A", 190, "Prenez une douche avant d'entrer dans l'eau."), ("B", 275, "Ne courez pas au bord du bassin."),
      ("C", 360, "Il faut porter un bonnet de bain."), ("D", 445, "Les enfants de moins de 8 ans doivent être accompagnés."),
      ("E", 530, "Nous venons de rénover les vestiaires : merci de les respecter !")]
for t, y, r in RL:
    RG.letter(105, y - 7, t)
    RG.tekst(145, y, r, 22, "start")
U = "reglement-zwembad.svg"
Z = {t: [Prent.zone(80, y - 40, 840, 62)] for t, y, _ in RL}

VRAGEN = [
    klik("Bekijk het reglement. Klik op het ontkennende bevel.", U, Z["B"], "Ne courez pas: loop niet."),
    klik("Klik op de regel met een onpersoonlijk werkwoord dat een verplichting uitdrukt.", U, Z["C"], "Il faut: men moet."),
    klik("Klik op de regel die zegt wat er net gebeurd is.", U, Z["E"], "Nous venons de rénover: we hebben net vernieuwd (passé récent)."),
    klik("Klik op de regel waarin devoir zegt wie iets moet.", U, Z["D"], "Les enfants … doivent: devoir noemt wie moet."),
    sorteer("Welke infinitief?", ["être", "avoir", "aller", "faire"],
            [("vous êtes", "être"), ("ils ont", "avoir"), ("ils vont", "aller"), ("vous faites", "faire"), ("ils sont", "être"), ("ils font", "faire")],
            "De vier werkwoorden die je het vaakst nodig hebt."),
    sleep("Vul de présent in: Le matin, je [[prends]] le bus. Nous [[finissons]] les cours à 16 h. Mes amis [[viennent]] chez moi.",
          ["prenons", "finisons"], "Prendre, finir met -iss-, venir."),
    inv("Vervoeg: ils (boire) de l'eau. Eén werkwoordsvorm.", ["boivent"], "Boire: je bois, nous buvons, ils boivent."),
    tabel("Is de vorm van de présent juist?",
          [("nous mangeons", J), ("vous disez", F), ("je peux", J), ("ils prenent", F), ("tu finis", J)],
          "Vous dites; ils prennent met dubbele n."),
    keuze("Je suis [[*en train de|en train|à]] lire : ik ben aan het lezen.", "Être en train de + infinitief."),
    sorteer("Infinitief rechtstreeks, met de of met à?", ["rechtstreeks", "de", "à"],
            [("je veux … partir", "rechtstreeks"), ("j'essaie … comprendre", "de"), ("je commence … lire", "à"), ("je dois … travailler", "rechtstreeks"), ("j'ai oublié … téléphoner", "de")],
            "Na vouloir, pouvoir, devoir en aller geen woordje ertussen."),
    sorteer("Welke vorm?", ["infinitief", "vervoegd", "voltooid deelwoord"],
            [("aller", "infinitief"), ("allez", "vervoegd"), ("allé", "voltooid deelwoord"), ("parler", "infinitief"), ("parlé", "voltooid deelwoord"), ("parlez", "vervoegd")],
            "Aan de uitgang zie je welke vorm het is."),
    keuze("Bevel aan een vriend: [[*Regarde|Regardes|Regardez-tu]] ce film !", "Werkwoorden op -er verliezen de s in de tu-vorm."),
    keuze("Bevel aan je klas: [[*Soyez|Êtes|Soyons pas]] à l'heure !", "Être heeft een eigen bevelende vorm: sois, soyons, soyez."),
    inv("Zet in de bevelende vorm voor vous: (se dépêcher) ! Twee woorden met een streepje.", ["Dépêchez-vous", "dépêchez-vous"], "Het voornaamwoord komt erachter."),
    keuze("Ontkennend bevel: [[*Ne te lève pas|Ne lève-toi pas|Lève-toi pas]] !", "In de ontkenning springt het voornaamwoord weer naar voren."),
    inv("Vervoeg: nous (se promener) dans le parc. Drie woorden.", ["nous nous promenons"], "Nous nous promenons: nous staat er twee keer."),
    sorteer("Futur proche of passé récent?", ["futur proche", "passé récent"],
            [("Je vais partir.", "futur proche"), ("Je viens de partir.", "passé récent"), ("Il va pleuvoir.", "futur proche"), ("Elle vient d'arriver.", "passé récent")],
            "Aller + infinitief: zo meteen. Venir de + infinitief: net gebeurd."),
    mk("'Le film vient de commencer.' Wat betekent dat?",
       ["de film is net begonnen", "de film begint zo meteen", "de film komt binnenkort uit", "de film begint niet"],
       0, "Venir de: net gebeurd."),
    mk("'Il vient chercher son frère.' Wat betekent dat?",
       ["hij komt zijn broer halen", "hij heeft zijn broer net gehaald", "hij heeft zijn broer gezocht", "hij moet zijn broer zoeken"],
       0, "Zonder de is het geen passé récent: hij komt om te halen."),
    tabel("Is dit een wijze of een tijd?",
          [("indicatif", "wijze"), ("imparfait", "tijd"), ("subjonctif", "wijze"), ("présent", "tijd"), ("impératif", "wijze")],
          "De wijze zegt hoe je iets voorstelt, de tijd wanneer.", ["wijze", "tijd"]),
    mk("Welke zin heeft een onpersoonlijk werkwoord?",
       ["Il neige depuis ce matin.", "Il part demain matin avec sa sœur.", "Il mange une pomme verte.", "Il lit un roman policier."],
       0, "Bij neiger is il een loos woordje."),
    inv("Vervoeg: elle (s'appeler) Julie. Eén woord met apostrof.", ["s'appelle"], "S'appeler: elle s'appelle, met dubbele l."),
    keuze("[[*Il faut|Il doit]] partir maintenant : men moet nu vertrekken.", "Il faut laat open wie moet."),
    mk("Welke vormen klinken allemaal hetzelfde?",
       ["je chante, tu chantes, ils chantent", "nous chantons, vous chantez, ils chantent", "je chante, nous chantons, chantez", "chanter, chanté, chantons"],
       0, "-e, -es en -ent zwijgen."),
    keuze("Bevel aan een vriend: [[*Finis|Fini|Finit]] ton assiette !", "Bij finir blijft de s staan."),
    volgorde("Zet de présent van aller in de juiste volgorde: je, tu, il, nous, vous, ils.",
             ["vais", "vas", "va", "allons", "allez", "vont"],
             "Alleen nous en vous houden de stam all-."),
    tabel("Klopt dit over de présent en de impératif?",
          [("De impératif heeft maar drie vormen.", J), ("Wederkerende werkwoorden gaan in de passé composé met être.", J), ("'Je veux de partir' is juist.", F), ("Na pour komt een infinitief.", J)],
          "Je veux partir, zonder de."),
    open_("Schrijf in het Frans drie regels voor de klas, met drie verschillende bevelende vormen (vous), waarvan één ontkennend.",
          "Rangez vos affaires. Levez la main pour parler. Ne mangez pas en classe."),
    inv("Vervoeg: Qu'est-ce que vous (faire) ce week-end ? Eén werkwoordsvorm.", ["faites"], "Vous faites, zoals vous êtes en vous dites."),
    mk("'Tu dois rentrer avant minuit.' Wat zegt devoir hier meer dan il faut?",
       ["wie er moet", "wanneer je moet", "waarom je moet", "hoe je moet"],
       0, "Devoir noemt het onderwerp; il faut laat het open."),
]
