"""De toekomende tijd en de conditionnel — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis le mail.\n\n« Madame, Monsieur,\n\nNous allons visiter Lyon avec notre classe le mois prochain. Nous arriverons le 12 mai en train et nous resterons trois jours. "
        "Pourriez-vous nous envoyer les prix de votre auberge ? Nous voudrions aussi savoir s'il y aura un repas le soir. "
        "Si vous avez de la place, nous réserverons tout de suite.\n\nJe vous serais reconnaissant de votre réponse.\n\nTom Janssens »",
        [
            keuze("« Nous allons visiter » is een [[*futur proche|futur simple|conditionnel]].", "Aller + infinitief."),
            keuze("« Nous arriverons » is een [[*futur simple|conditionnel|futur proche]].", "Infinitief + -ons."),
            keuze("Tom schrijft « Pourriez-vous » om [[*hoffelijk te vragen|een bevel te geven]].", "Conditionnel de politesse."),
            keuze("« Si vous avez de la place, nous réserverons » : na si staat de [[*présent|futur]].", "Si + présent, dan futur."),
            mk("Wat wil de klas weten?",
               ["de prijzen en of er 's avonds eten is", "hoe laat de trein in Lyon aankomt", "welke musea ze in Lyon kunnen bezoeken", "of ze vijf dagen mogen blijven"], 0,
               "Les prix et s'il y aura un repas le soir."),
        ],
    ),
    tabel("Futur simple of conditionnel?", [
        ("je parlerai", "futur simple"), ("je parlerais", "conditionnel"), ("nous serons", "futur simple"),
        ("nous serions", "conditionnel"), ("ils feront", "futur simple"), ("ils feraient", "conditionnel"),
    ], "Futur: -ai, -ons, -ont. Conditionnel: -ais, -ions, -aient.", kolommen=["futur simple", "conditionnel"]),
    koppel("Koppel elk werkwoord aan zijn stam in de futur simple.", [
        ["aller", "ir-"], ["faire", "fer-"], ["avoir", "aur-"], ["venir", "viendr-"],
    ], ["all-"], "Onregelmatige stammen leer je uit het hoofd."),
    koppel("Koppel elke vorm aan haar betekenis.", [
        ["je voudrais", "ik zou graag willen"], ["tu devrais", "je zou moeten"], ["on pourrait", "we zouden kunnen"], ["il y aura", "er zal zijn"],
    ], ["er was"], "Er was is il y avait."),
    mk("« Quand j'___ dix-huit ans, j'apprendrai à conduire. » (avoir) Welke vorm past?",
       ["aurai", "ai", "aurais", "avais"], 0, "Na quand over later: futur simple."),
    mk("« Si j'avais plus d'argent, je ___ un vélo. » (acheter) Welke vorm past?",
       ["achèterais", "achèterai", "achète", "acheterions"], 0, "Si + imparfait, dan conditionnel."),
    mk("« Demain, il ___ froid. » (faire, futur simple) Welke vorm past?",
       ["fera", "ferait", "faira", "fait"], 0, "Stam fer- + -a."),
    mk("Je bent in een bakkerij. Wat zeg je het beleefdst?",
       ["Je voudrais une baguette, s'il vous plaît.", "Je veux une baguette, et tout de suite.", "Donne-moi une baguette maintenant.", "Une baguette, vite, je suis pressé !"], 0,
       "Je voudrais is de gewone winkelvorm."),
    mk("Je vriend is heel moe. Welke zin geeft een raad?",
       ["Tu devrais dormir plus.", "Tu dormiras plus tard.", "Tu vas dormir maintenant !", "Tu dormais beaucoup trop."], 0,
       "Tu devrais: je zou moeten."),
    mk("« Ce soir, nous ___ regarder un film. » Welke vorm past?",
       ["allons", "irons", "allions", "irions"], 0, "Futur proche: aller in de présent + infinitief."),
    mk("Een krant schrijft: « Il y aurait trois blessés. » Wat betekent dat?",
       ["Er zouden drie gewonden zijn.", "Er waren zeker drie gewonden.", "Er zullen morgen drie gewonden zijn.", "Er zijn drie gewonden genezen."], 0,
       "De conditionnel voor iets dat nog niet zeker is."),
    inv("Vul in: « Nous ___ à la mer l'été prochain. » (aller, futur simple) Eén woord.", ["irons"], "Nous irons."),
    inv("Vul in: « Ils ___ demain. » (venir, futur simple) Eén woord.", ["viendront"], "Ils viendront."),
    inv("Vul in: « Tu ___ m'aider ? » (pouvoir, conditionnel) Eén woord.", ["pourrais"], "Pourrais-tu, tu pourrais."),
    inv("Vul in: « Je ne sais pas encore. Je te le ___ demain. » (dire, futur simple) Eén woord.", ["dirai"], "Je dirai."),
    keuze("« Je [[*vais partir|vais pars]] dans cinq minutes. »", "Na aller komt de infinitief."),
    keuze("« Si tu [[*viens|viendras]], je serai content. »", "Na si: présent."),
    keuze("« Si j'étais toi, je [[*resterais|resterai]] à la maison. »", "Si + imparfait: conditionnel."),
    keuze("« J'[[*achèterai|acheterai]] des fleurs pour maman. »", "Het accent blijft."),
    keuze("« Nous [[*saurons|savrons]] le résultat demain. »", "Savoir: stam saur-."),
    tabel("Is de zin juist (futur en conditionnel)?", [
        ("Je ne vais pas sortir ce soir.", J), ("Si tu viendras, on jouera.", F),
        ("Pourriez-vous fermer la fenêtre ?", J), ("Ils parleleront demain.", F),
    ], "Na si geen futur; ils parleront."),
    volgorde("Zet de woorden in de juiste volgorde: « pas / je / vais / ne / sortir »", [
        "je", "ne", "vais", "pas", "sortir",
    ], "Ne ... pas rond aller, de infinitief erachter."),
    sleep("Si je gagne le match, je [[serai]] très content. Si j'avais le temps, je [[viendrais]] avec toi.",
          ["serais", "viendrai"], "Si + présent: futur; si + imparfait: conditionnel."),
    inv("Vul in: « Demain, il y ___ du soleil. » (avoir, futur simple) Eén woord.", ["aura"], "Il y aura."),
    open_("Leg in het Nederlands uit waarom je in een winkel beter « je voudrais » zegt dan « je veux ».",
          "Je voudrais is de conditionnel en klinkt hoffelijk; je veux klinkt in het Frans bot.",
          "Conditionnel de politesse."),
    mk("Welke zin stelt iets voor?",
       ["On pourrait aller au parc.", "On est allés au parc.", "On allait au parc.", "On va au parc tous les jours."], 0,
       "On pourrait: we zouden kunnen."),
]
