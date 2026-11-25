"""Passé composé, imparfait en plus-que-parfait — pittig (🚀 Boost doorstroom, Frans).

Eigen vragen strikt binnen fr_verleden: de passé composé met avoir of être en
de overeenkomst, de voltooide deelwoorden, de imparfait, de keuze tussen de
twee en de plus-que-parfait. Met een zelfgetekend verhaaltje in vijf zinnen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER

VH = Prent("verhaal-vijf-zinnen", "Un samedi pas comme les autres", "een verhaaltje van vijf zinnen, letters A tot E")
VH.rect(50, 55, 900, 570, "#ffffff", DONKER, 10, 3)
ZN = [("A", 140, ["C'était un samedi d'hiver et il neigeait depuis le matin."]),
      ("B", 225, ["Comme d'habitude, ma sœur regardait des dessins animés."]),
      ("C", 310, ["Tout à coup, quelqu'un a sonné à la porte."]),
      ("D", 395, ["C'était notre voisin : il avait perdu son chat", "la veille au soir."]),
      ("E", 510, ["Nous sommes sortis tous ensemble et nous l'avons", "retrouvé dans le garage."])]
for t, y, rr in ZN:
    VH.letter(95, y - 7, t)
    for i, r in enumerate(rr):
        VH.tekst(135, y + i * 32, r, 22, "start")
U = "verhaal-vijf-zinnen.svg"
Z = {t: [Prent.zone(65, y - 40, 870, 60 + 32 * (len(rr) - 1))] for t, y, rr in ZN}

VRAGEN = [
    klik("Bekijk het verhaaltje. Klik op de zin met een plus-que-parfait.", U, Z["D"], "Il avait perdu: hij was zijn kat al kwijt vóór het aanbellen."),
    klik("Klik op de zin die een gewoonte beschrijft.", U, Z["B"], "Comme d'habitude … regardait: een gewoonte, dus imparfait."),
    klik("Klik op de zin met een plotse gebeurtenis die het verhaal op gang trekt.", U, Z["C"], "Tout à coup … a sonné: passé composé."),
    klik("Klik op de zin met een passé composé met être.", U, Z["E"], "Nous sommes sortis: sortir zonder voorwerp gaat met être."),
    sorteer("Avoir of être in de passé composé?", ["avoir", "être"],
            [("manger", "avoir"), ("aller", "être"), ("se lever", "être"), ("faire", "avoir"), ("naître", "être"), ("être", "avoir")],
            "Être zelf gaat met avoir: j'ai été."),
    koppel("Koppel de infinitief aan het voltooid deelwoord.",
           [("boire", "bu"), ("mettre", "mis"), ("écrire", "écrit"), ("avoir", "eu"), ("être", "été")],
           ["fais"],
           "Onregelmatige deelwoorden leer je als woordjes."),
    tabel("Is de overeenkomst juist?",
          [("Elle est partie.", J), ("Elles ont mangées.", F), ("Nous sommes restés.", J), ("Ils sont venu.", F), ("Elle s'est levée.", J)],
          "Na avoir blijft het deelwoord onveranderd; met être past het zich aan."),
    inv("Vul in: Mes cousines sont … hier (arriver).", ["arrivées"], "Vrouwelijk meervoud: -ées."),
    keuze("Il [[*a monté|est monté]] les valises au grenier.", "Les valises is een lijdend voorwerp: avoir."),
    keuze("Elle [[*est descendue|a descendu]] à la cave.", "Zonder voorwerp is descendre een beweging: être."),
    mk("Hoe ontken je 'Nous avons vu ce film'?",
       ["Nous n'avons pas vu ce film.", "Nous n'avons vu pas ce film.", "Nous avons ne pas vu ce film.", "Ne nous avons pas vu ce film."],
       0, "Ne en pas sluiten alleen het hulpwerkwoord in."),
    sorteer("Imparfait of passé composé?", ["imparfait", "passé composé"],
            [("decor: het weer", "imparfait"), ("een gewoonte", "imparfait"), ("een plotse gebeurtenis", "passé composé"), ("een toestand: ik was moe", "imparfait"), ("een afgeronde handeling: ik heb gegeten", "passé composé")],
            "De imparfait schildert, de passé composé vertelt."),
    sleep("Vul in: Quand j'[[étais]] petit, nous [[allions]] chaque été à la mer. Un jour, mon père [[a acheté]] un bateau.",
          ["suis", "allons"], "Toestand en gewoonte in de imparfait, één gebeurtenis in de passé composé."),
    inv("Zet in de imparfait: nous (finir) tard. Eén werkwoordsvorm.", ["finissions"], "Nous finissons geeft finiss- + -ions."),
    inv("Zet in de imparfait: ils (avoir) peur. Eén werkwoordsvorm.", ["avaient"], "Nous avons geeft av- + -aient."),
    keuze("Être heeft een eigen stam in de imparfait: j'[[*étais|êtais|étions]].", "Ét- is de enige onregelmatige stam."),
    sorteer("Welke tijd kondigt het woord meestal aan?", ["imparfait", "passé composé"],
            [("d'habitude", "imparfait"), ("tout à coup", "passé composé"), ("chaque semaine", "imparfait"), ("soudain", "passé composé"), ("souvent", "imparfait"), ("hier soir", "passé composé")],
            "Gewoonte of plots moment."),
    mk("'Quand nous sommes arrivés, le film avait commencé.' Wat gebeurde eerst?",
       ["de film begon", "wij kwamen aan", "allebei tegelijk", "de film eindigde"],
       0, "De plus-que-parfait zet de gebeurtenis een stap verder terug."),
    inv("Vul in: Elle … déjà partie quand j'ai téléphoné. Eén woord.", ["était"], "Partir met être; être in de imparfait."),
    keuze("Ils [[*avaient|étaient]] oublié leurs livres.", "Oublier gaat met avoir."),
    volgorde("Zet de gebeurtenissen in de volgorde waarin ze echt gebeurden: 'Hier, j'ai trouvé le portefeuille que Paul avait perdu la semaine dernière.'",
             ["Paul verliest zijn portefeuille.", "Er gaat een week voorbij.", "Ik vind de portefeuille."],
             "Avait perdu ligt vóór ai trouvé."),
    tabel("Welke tijd?",
          [("j'avais mangé", "plus-que-parfait"), ("je mangeais", "imparfait"), ("j'ai mangé", "passé composé"), ("j'étais sorti", "plus-que-parfait"), ("je suis sorti", "passé composé")],
          "Het hulpwerkwoord in de imparfait maakt een plus-que-parfait.", ["passé composé", "imparfait", "plus-que-parfait"]),
    mk("'Ik las een boek toen het licht uitviel.' Hoe zeg je dat in het Frans?",
       ["Je lisais un livre quand la lumière s'est éteinte.", "J'ai lu un livre quand la lumière s'éteignait.", "Je lisais un livre quand la lumière s'éteignait soudain.", "J'ai lu un livre quand la lumière s'est éteinte."],
       0, "Lezen was aan de gang (imparfait), het licht viel op één moment uit (passé composé)."),
    keuze("Nous nous [[*sommes|avons]] dépêchés pour ne pas rater le bus.", "Wederkerende werkwoorden gaan altijd met être."),
    tabel("Klopt dit over de verleden tijden?",
          [("Eu is het deelwoord van avoir.", J), ("Avoir, aller en faire hebben een onregelmatige stam in de imparfait.", F), ("De imparfait vertrekt van de nous-vorm.", J), ("'Avait' is een futur simple.", F)],
          "Enkel être heeft een eigen stam in de imparfait."),
    open_("Vertel in het Frans in drie zinnen wat je vorig weekend deed. Gebruik de imparfait voor het weer en de passé composé voor wat je deed.",
          "Samedi, il faisait beau. Je suis allé au parc avec mes amis et nous avons joué au foot. Le soir, j'ai regardé un film."),
    inv("Vul het deelwoord van pouvoir in: Je n'ai pas … venir.", ["pu"], "Pouvoir geeft pu, zoals voir vu."),
    keuze("Ma sœur [[*est née|a né|est né]] en 2012.", "Naître gaat met être, en het deelwoord past zich aan."),
    keuze("In de être-groep is het tegengestelde van monter: [[*descendre|rester|naître]].", "Monter en descendre, entrer en sortir, naître en mourir."),
    keuze("Il faisait nuit. Soudain, le chien [[*a aboyé|aboyait]].", "Soudain: een plotse gebeurtenis, dus passé composé."),
]
