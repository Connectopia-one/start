"""De tegenwoordige tijd en de gebiedende wijs — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis le message de Julie.\n\n« Salut Marc ! Le samedi, je me lève tard. Mes parents font les courses et moi, je finis mes devoirs. "
        "L'après-midi, nous allons au parc avec le chien, sauf quand il pleut. Ce week-end, il faut fêter l'anniversaire de mamie. "
        "Viens avec nous ! Et n'oublie pas ton maillot : on va à la piscine après. »",
        [
            keuze("« je me lève » is een vorm van een [[*wederkerend|onpersoonlijk]] werkwoord.", "Se lever: opstaan."),
            keuze("« je finis » is de présent van [[*finir|finer|finissir]].", "Je finis, nous finissons."),
            keuze("« il pleut » is een [[*onpersoonlijk|wederkerend]] werkwoord.", "Pleuvoir bestaat enkel met il."),
            keuze("« Viens avec nous ! » is een [[*gebiedende wijs|vraag]].", "Een bevel bij tu, zonder voornaamwoord."),
            mk("Wat moet er dit weekend gebeuren?",
               ["oma's verjaardag vieren", "de hond naar de dierenarts brengen", "boodschappen doen voor oma", "huiswerk maken met Marc"], 0,
               "Il faut fêter l'anniversaire de mamie."),
        ],
    ),
    tabel("Is de vorm juist?", [
        ("nous mangons", F), ("ils prennent", J), ("vous faisez", F), ("elles vont", J),
    ], "Nous mangeons met e; vous faites."),
    tabel("Is de vorm juist (wederkerend en gebiedend)?", [
        ("Lève-toi !", J), ("Ne te lève pas !", J), ("Ne lève-toi pas !", F), ("Couche-te !", F),
    ], "Bij een gewoon bevel achteraan met toi; bij een verbod vooraan."),
    sorteer("Krijgt het werkwoord bij nous -ons of -issons?", ["-ons", "-issons"], [
        ["parler", "-ons"], ["finir", "-issons"], ["chanter", "-ons"], ["choisir", "-issons"], ["danser", "-ons"], ["réussir", "-issons"],
    ], "Regelmatige -ir-werkwoorden krijgen -iss- in het meervoud."),
    koppel("Koppel elk onderwerp aan de juiste vorm van être.", [
        ["je", "suis"], ["nous", "sommes"], ["vous", "êtes"], ["ils", "sont"],
    ], ["sommez"], "Être is onregelmatig."),
    mk("« Nous ___ beaucoup d'eau en été. » (boire) Welke vorm past?",
       ["buvons", "boivons", "boirons", "bovons"], 0, "Nous buvons."),
    mk("« Ils ___ venir, mais ils n'ont pas le temps. » (vouloir) Welke vorm past?",
       ["veulent", "voulent", "veuillent", "vouloient"], 0, "Ils veulent."),
    mk("« Tu ___ où est la gare ? » (savoir) Welke vorm past?",
       ["sais", "sait", "savez", "savons"], 0, "Tu sais."),
    mk("« Vous ___ toujours la vérité. » (dire) Welke vorm past?",
       ["dites", "disez", "dizez", "disent"], 0, "Vous dites, net als vous faites."),
    mk("« Nous ___ le match à huit heures. » (commencer) Welke vorm past?",
       ["commençons", "commencons", "commenceons", "commencions"], 0, "Cédille voor de o."),
    mk("« J'___ un cadeau pour ma sœur. » (acheter) Welke vorm past?",
       ["achète", "achete", "achètes", "achèt"], 0, "J'achète met accent grave."),
    mk("« ___ ! On est en retard ! » Je zegt tegen een vriend dat hij zich moet haasten. Welke vorm past?",
       ["Dépêche-toi", "Te dépêche", "Dépêche-te", "Toi te dépêche"], 0, "Bevel bij tu: dépêche-toi."),
    inv("Vul in: « Elles ___ la porte. » (ouvrir) Eén woord.", ["ouvrent"], "Ouvrir volgt de -er-uitgangen."),
    inv("Vul in: « Ils ___ chez nous ce soir. » (venir) Eén woord.", ["viennent"], "Ils viennent, met twee n'en."),
    inv("Vul in: « Je ___ mon ami. » (payer) Eén woord.", ["paie", "paye"], "De y wordt i bij je."),
    inv("Geef de gebiedende wijs van « être » bij vous. Eén woord.", ["soyez", "Soyez"], "Sois, soyons, soyez."),
    inv("Vul in: « ___-vous, s'il vous plaît. » (s'asseoir, bevel bij vous) Eén woord.", ["asseyez", "Asseyez"],
        "Asseyez-vous."),
    keuze("« Nous [[*nous|se]] promenons dans le parc. »", "Bij nous: nous nous."),
    keuze("« [[*Il|On]] neige depuis ce matin. »", "Neiger bestaat enkel met il."),
    keuze("« Il [[*y a|est]] trois chaises dans la cuisine. »", "Il y a: er zijn."),
    keuze("« Ne [[*me|moi]] parle pas comme ça ! »", "In een verbod blijft me vooraan."),
    tabel("Is het werkwoord wederkerend in het Frans?", [
        ("se promener (wandelen)", J), ("se coucher (gaan slapen)", J), ("manger (eten)", F), ("se souvenir de (zich herinneren)", J),
    ], "Wandelen en gaan slapen hebben in het Nederlands geen zich."),
    volgorde("Zet de woorden in de juiste volgorde voor een vraag: « tu / est-ce que / ce soir / viens »", [
        "est-ce que", "tu", "viens", "ce soir",
    ], "Est-ce que vooraan, daarna de gewone volgorde."),
    sleep("Le matin, je [[me]] lève à sept heures. Ensuite, nous [[prenons]] le bus.",
          ["te", "prennons"], "Je me lève; nous prenons met één n."),
    open_("Leg in het Nederlands uit waarom je « nous mangeons » schrijft met een e na de g.",
          "Om de zachte g-klank te houden voor de o.",
          "Zonder e zou de g hard klinken."),
    mk("Wat betekent « Il faut étudier pour l'examen »?",
       ["We moeten studeren voor het examen.", "Hij wil niet studeren voor het examen.", "Het examen is heel moeilijk om te studeren.", "Hij studeert graag voor elk examen."], 0,
       "Il faut + infinitief: het moet."),
]
