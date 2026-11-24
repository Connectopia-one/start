"""De verleden tijden — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis le récit de Sarah.\n\n« Samedi dernier, il faisait beau et il y avait beaucoup de monde en ville. Ma sœur et moi, nous sommes allées au marché. "
        "J'ai acheté des fraises et ma sœur a pris des photos. Soudain, un chien est tombé dans la fontaine ! "
        "Quand nous sommes rentrées, maman venait de préparer le dîner. »",
        [
            keuze("« il faisait beau » staat in de [[*imparfait|passé composé]] omdat het het decor beschrijft.", "Het weer: imparfait."),
            keuze("« nous sommes allées » krijgt -es omdat het onderwerp [[*vrouwelijk meervoud|mannelijk enkelvoud]] is.",
                  "Twee zussen: allées."),
            keuze("« Soudain, un chien est tombé » staat in de [[*passé composé|imparfait]].", "Soudain: één gebeurtenis."),
            keuze("« maman venait de préparer le dîner » betekent dat mama het eten [[*net had klaargemaakt|nog moest klaarmaken]].",
                  "Venir de in de imparfait: net gebeurd, in het verleden."),
            mk("Wat deed de zus van Sarah op de markt?",
               ["foto's nemen", "aardbeien kopen voor het eten", "de hond uit de fontein halen", "het eten voor mama klaarmaken"], 0,
               "Ma sœur a pris des photos."),
        ],
    ),
    sorteer("Avoir of être in de passé composé?", ["avoir", "être"], [
        ["manger", "avoir"], ["arriver", "être"], ["finir", "avoir"], ["rester", "être"], ["prendre", "avoir"], ["se coucher", "être"],
    ], "Beweging, verandering en wederkerende werkwoorden nemen être."),
    koppel("Koppel elk werkwoord aan zijn deelwoord.", [
        ["lire", "lu"], ["écrire", "écrit"], ["prendre", "pris"], ["devoir", "dû"],
    ], ["prendu"], "Onregelmatige deelwoorden leer je uit het hoofd."),
    koppel("Koppel elk werkwoord aan zijn deelwoord (tweede reeks).", [
        ["naître", "né"], ["mourir", "mort"], ["ouvrir", "ouvert"], ["avoir", "eu"],
    ], ["mouru"], "Naître en mourir nemen être."),
    tabel("Is de zin juist (passé composé)?", [
        ("Elle est partie hier.", J), ("Ils ont allés au cinéma.", F), ("Je me suis levé tôt.", J), ("Nous avons arrivés à midi.", F),
    ], "Aller en arriver nemen être."),
    tabel("Imparfait of passé composé?", [
        ("Quand j'étais petit, je ___ (jouer) souvent dehors.", "imparfait"),
        ("Hier, j'___ (rencontrer) mon prof en ville.", "passé composé"),
        ("Il ___ (faire) froid ce jour-là.", "imparfait"),
        ("Soudain, la lumière ___ (s'éteindre).", "passé composé"),
    ], "Gewoonte en decor in de imparfait, één gebeurtenis in de passé composé.", kolommen=["imparfait", "passé composé"]),
    mk("« Je lisais quand mon frère ___. » (entrer) Welke vorm past?",
       ["est entré", "entrait", "a entré", "était entrer"], 0, "Wat erin valt: passé composé met être."),
    mk("« Elles se sont ___ tard. » (coucher) Welke vorm past?",
       ["couchées", "couché", "couchés", "couchaient"], 0, "Vrouwelijk meervoud: couchées."),
    mk("Hoe zeg je « Ik heb mijn huiswerk niet gemaakt »?",
       ["Je n'ai pas fait mes devoirs.", "Je n'ai fait pas mes devoirs.", "Je ne pas ai fait mes devoirs.", "Je ai ne pas fait mes devoirs."], 0,
       "Ne ... pas rond het hulpwerkwoord."),
    mk("Hoe zeg je « Ik heb hem gezien »?",
       ["Je l'ai vu.", "J'ai le vu.", "J'ai vu le.", "Je ai le vu."], 0, "Het voornaamwoord staat voor het hulpwerkwoord."),
    mk("« Il ___ monté l'escalier. » Welke vorm past?",
       ["a", "est", "était", "ont"], 0, "Met een lijdend voorwerp neemt monter avoir."),
    mk("Wat betekent « Nous venons de rentrer »?",
       ["We zijn net thuisgekomen.", "We gaan zo meteen naar huis.", "We komen elke dag thuis.", "We waren al lang thuis."], 0,
       "Venir de: passé récent."),
    mk("« Le train ___ quand nous sommes arrivés à la gare. » Welke vorm past?",
       ["venait de partir", "vient de partir", "va partir", "est venu de partir"], 0,
       "In een verhaal in het verleden: venait de."),
    inv("Vul in: « Nous ___ à la mer chaque été. » (aller, imparfait) Eén woord.", ["allions"], "Nous allions."),
    inv("Vul in: « Tu ___ malade hier ? » (être, imparfait) Eén woord.", ["étais"], "Tu étais."),
    inv("Geef het deelwoord van « mettre ».", ["mis"], "J'ai mis."),
    inv("Vul in: « Ils ___ beaucoup de devoirs. » (avoir, imparfait) Eén woord.", ["avaient"], "Ils avaient."),
    keuze("« Hier, nous [[*avons mangé|mangions]] au restaurant. »", "Hier: één gebeurtenis."),
    keuze("« Chaque samedi, je [[*faisais|ai fait]] du vélo. »", "Chaque samedi: gewoonte."),
    keuze("« Elle [[*est née|a né]] en 2009. »", "Naître neemt être."),
    keuze("« Je [[*mangeais|mangais]] une pomme. »", "De e na de g blijft voor -ais."),
    keuze("« Il y [[*avait|a eu]] du monde partout : c'était la fête. »", "Beschrijving: imparfait."),
    tabel("Neemt het werkwoord être in de passé composé?", [
        ("venir", J), ("tomber", J), ("faire", F), ("se promener", J),
    ], "Beweging, verandering en wederkerend: être."),
    volgorde("Zet de woorden in de juiste volgorde: « pas / suis / je / ne / allé »", [
        "je", "ne", "suis", "pas", "allé",
    ], "Ne ... pas rond het hulpwerkwoord."),
    sleep("Il [[pleuvait]] quand je [[suis sorti]] de la maison.",
          ["a plu", "sortais"], "Decor in de imparfait, wat erin valt in de passé composé."),
    open_("Leg in het Nederlands uit waarom je « elle est allée » schrijft maar « elle a mangé ».",
          "Aller neemt être, en dan past het deelwoord zich aan het vrouwelijke onderwerp aan. Bij avoir blijft het deelwoord gewoon staan.",
          "Overeenkomst enkel bij être."),
]
