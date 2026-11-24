"""Woordvelden dagelijks leven, eten en wonen — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis l'annonce.\n\n« À LOUER – Appartement douillet de deux chambres au rez-de-chaussée d'un immeuble calme. "
        "Meublé : meubles neufs, rideaux, frigo et machine à laver. La chaudière a été changée l'année dernière. "
        "Petit jardin avec une pelouse et une haie. Loyer : 850 euros par mois. Le propriétaire habite à côté. "
        "Pas d'animaux. Le locataire doit tondre la pelouse. »",
        [
            keuze("Het appartement ligt op [[*het gelijkvloers|de eerste verdieping|de zolder]].", "Le rez-de-chaussée."),
            keuze("« Meublé » betekent dat er al [[*meubels|geen meubels]] in staan.", "Les meubles."),
            mk("Wie woont er naast het appartement?",
               ["de eigenaar", "de vorige huurder", "een gezin met huisdieren", "de buurman die de tuin doet"], 0,
               "Le propriétaire habite à côté."),
            keuze("« le loyer » is [[*de huur|de ketel|het grasveld]].", "Le loyer: het geld dat je elke maand betaalt."),
            mk("Wat staat er in de tuin?",
               ["een grasveld en een haag", "een tuinhuisje en een grote vijver", "een trap naar de kelder", "een vuilnisbak voor de buren"], 0,
               "Une pelouse et une haie."),
        ],
    ),
    sorteer("Hoort het in de keuken of in de tuin?", ["keuken", "tuin"], [
        ["une bouilloire", "keuken"], ["la pelouse", "tuin"], ["un robinet", "keuken"], ["la haie", "tuin"], ["un frigo", "keuken"], ["la terrasse", "tuin"],
    ], "Waterkoker, kraan en koelkast binnen; grasveld, haag en terras buiten."),
    sorteer("Familie of geen familie?", ["familie", "geen familie"], [
        ["une tante", "familie"], ["un locataire", "geen familie"], ["un neveu", "familie"], ["un voisin", "geen familie"], ["une nièce", "familie"], ["un invité", "geen familie"],
    ], "Tante, neef en nicht zijn familie; een huurder, buur of gast niet."),
    koppel("Koppel elke Franse uitdrukking aan haar betekenis.", [
        ["faire la grasse matinée", "uitslapen"], ["en avoir assez", "er genoeg van hebben"], ["s'entendre bien avec", "goed overeenkomen met"], ["déménager", "verhuizen"],
    ], ["afwassen"], "Afwassen is faire la vaisselle."),
    koppel("Koppel elk Frans huishoudwoord aan zijn betekenis.", [
        ["un aspirateur", "een stofzuiger"], ["une poubelle", "een vuilnisbak"], ["un balai", "een bezem"], ["un seau", "een emmer"],
    ], ["een gordijn"], "Een gordijn is un rideau."),
    mk("« Je suis fatigué. Samedi, je vais ___. » Wat past?",
       ["faire la grasse matinée", "faire la lessive à la main", "déménager", "ranger tout le grenier vite"], 0, "Uitslapen na een vermoeiende week."),
    mk("Hoe zeg je « Hij heeft me een goede raad gegeven »?",
       ["Il m'a donné un bon conseil.", "Il m'a donné un bon conseiller.", "Il m'a fait un bon conseil.", "Il m'a donné une bonne conseil."], 0,
       "Un conseil is de raad zelf."),
    mk("Je bent in een snackbar in Parijs. Welke vraag krijg je?",
       ["Sur place ou à emporter ?", "Vous voulez louer un appartement ?", "Vous êtes le nouveau locataire ?", "Vous pouvez faire la vaisselle ?"], 0,
       "Hier eten of meenemen."),
    mk("« Les enfants prennent leur ___ à quatre heures. » Wat past?",
       ["goûter", "dîner", "petit déjeuner", "déjeuner"], 0, "Le goûter: het vieruurtje."),
    mk("« Ce curry est très ___. » Het is pikant. Wat past?",
       ["épicé", "douillet", "équilibré", "meublé"], 0, "Épicé: pikant."),
    mk("Waar woon je als je op « le premier étage » woont?",
       ["op de eerste verdieping", "op het gelijkvloers", "in de kelder onder het gebouw", "op de zolder van het gebouw"], 0,
       "Boven het rez-de-chaussée."),
    inv("Hoe zeg je vork in het Frans? Eén woord, zonder lidwoord.", ["fourchette"], "Une fourchette."),
    inv("Hoe zeg je lift in het Frans? Eén woord, zonder lidwoord.", ["ascenseur"], "Un ascenseur."),
    inv("Hoe zeg je gang in het Frans? Eén woord, zonder lidwoord.", ["couloir"], "Le couloir."),
    inv("Schrijf het meervoud van « un rideau ». Twee woorden.", ["des rideaux"], "Met een x."),
    keuze("« Nous allons au cinéma [[*en bus|avec le bus]]. »", "En bus."),
    keuze("« Ce soir, je reste [[*à la maison|dans la maison chez]]. »", "À la maison."),
    keuze("« Mets le papier [[*à la poubelle|dans la bouilloire]]. »", "Une poubelle: een vuilnisbak."),
    keuze("« Mon frère ne fait jamais les tâches [[*ménagères|ménagers]]. »", "Les tâches ménagères."),
    keuze("« J'ai fait une [[*erreur|faute de faire]] dans mon devoir. »", "Faire une erreur."),
    tabel("Is deze zin juist (dagelijks leven)?", [
        ("Je m'entends bien avec mes voisins.", J), ("Il m'a donné un conseiller.", F),
        ("Les meubles sont neufs.", J), ("J'en ai assez de ce temps.", J),
    ], "Un conseil, niet un conseiller."),
    tabel("Is dit een ruimte in een huis?", [
        ("le grenier", J), ("le couloir", J), ("la pelouse", F), ("le balai", F),
    ], "Zolder en gang; een grasveld en een bezem zijn geen ruimtes."),
    sleep("Le dimanche, je [[range]] ma chambre. Puis j'aide mon père à faire [[la vaisselle]] après le dîner.",
          ["loue", "le loyer"], "Ranger: opruimen. La vaisselle: de vaat."),
    inv("Hoe zeg je de huurder in het Frans? Twee woorden.", ["le locataire"], "Le locataire."),
    volgorde("Zet de maaltijden van een Franse dag in de juiste volgorde.", [
        "le petit déjeuner", "le déjeuner", "le goûter", "le dîner",
    ], "Ontbijt, middagmaal, vieruurtje, avondmaal."),
    open_("Leg in het Nederlands uit wat het verschil is tussen « le propriétaire » en « le locataire ».",
          "Le propriétaire is de eigenaar die verhuurt, le locataire is de huurder die le loyer betaalt.",
          "Eigenaar tegenover huurder."),
]
