"""Présent, futur, conditionnel, subjonctif en gérondif — pittig (🌍 Beyond doorstroom, Frans)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lisez le message de Chloé.\n\n"
    "« Salut Nina ! Samedi, je vais fêter mes 18 ans. Si tu as le temps, viens à la maison vers 19 h. "
    "Il faut que tu prennes le bus 12, parce que la rue sera fermée. "
    "Je voudrais aussi que tu apportes ta guitare : ce serait génial ! "
    "Quand tu arriveras, envoie-moi un message. "
    "J'aurais dû t'inviter plus tôt, désolée ! Je t'écris en préparant les gâteaux. »"
)

VRAGEN = [
    casus(
        TEKST1,
        [
            tabel(
                "Welke wijs of tijd staat in het bericht?",
                [
                    ("je vais fêter", "futur proche"),
                    ("que tu prennes", "subjonctif"),
                    ("je voudrais", "conditionnel"),
                    ("la rue sera fermée", "futur simple"),
                    ("ce serait génial", "conditionnel"),
                ],
                "Aller + infinitief, il faut que + subjonctif, voudrais/serait, sera.",
                kolommen=["futur proche", "futur simple", "conditionnel", "subjonctif"],
            ),
            mk(
                "Wat drukt Chloé uit met « J'aurais dû t'inviter plus tôt »?",
                ["spijt", "een bevel", "een plan", "een gewoonte"],
                0,
                "Conditionnel passé van devoir: spijt.",
            ),
            keuze(
                "« En préparant les gâteaux » betekent dat Chloé schrijft [[*terwijl ze taarten maakt|nadat ze taarten maakte]].",
                "Gérondif: twee handelingen tegelijk.",
            ),
            keuze(
                "In « Quand tu arriveras » staat een [[*futur simple|présent]], want het gaat over de toekomst.",
                "Na quand gebruikt het Frans voor de toekomst de futur.",
            ),
        ],
    ),
    tabel(
        "Welke vorm van de si-zin is juist?",
        [
            ("Si j'ai de l'argent, je ___ un vélo.", "achèterai"),
            ("Si j'avais de l'argent, j'___ un vélo.", "achèterais"),
            ("Si j'avais eu de l'argent, j'___ un vélo.", "aurais acheté"),
        ],
        "Présent → futur; imparfait → conditionnel; plus-que-parfait → conditionnel passé.",
        kolommen=["achèterai", "achèterais", "aurais acheté"],
    ),
    tabel(
        "Subjonctif of indicatif na deze uitdrukking?",
        [
            ("il faut que", "subjonctif"),
            ("je pense que", "indicatif"),
            ("je veux que", "subjonctif"),
            ("après que", "indicatif"),
            ("bien que", "subjonctif"),
        ],
        "Noodzaak, wil, gevoel en bien que: subjonctif.",
        kolommen=["subjonctif", "indicatif"],
    ),
    koppel(
        "Koppel de infinitief aan de stam van de futur simple.",
        [
            ("aller", "ir-"),
            ("être", "ser-"),
            ("avoir", "aur-"),
            ("faire", "fer-"),
        ],
        ["all-"],
        "Onregelmatige stammen; dezelfde stam in de conditionnel.",
    ),
    sorteer(
        "Gaat het om de toekomst of om een hoffelijke vraag?",
        ["Toekomst", "Hoffelijke vraag"],
        [
            ("Je partirai demain.", "Toekomst"),
            ("Pourriez-vous m'aider ?", "Hoffelijke vraag"),
            ("Nous allons déménager.", "Toekomst"),
            ("Je voudrais un renseignement.", "Hoffelijke vraag"),
            ("Il fera froid ce week-end.", "Toekomst"),
        ],
        "Futur tegenover conditionnel de politesse.",
    ),
    volgorde(
        "Zet de vormen van de futur simple van parler in de volgorde je, tu, il, nous.",
        ["je parlerai", "tu parleras", "il parlera", "nous parlerons"],
        "Uitgangen -rai, -ras, -ra, -rons.",
    ),
    mk(
        "Welk bevel is juist voor tu bij aller?",
        ["Va à la boulangerie !", "Vas à la boulangerie !", "Tu vas à la boulangerie !", "Aller à la boulangerie !"],
        0,
        "Bij aller valt de s weg: va.",
    ),
    mk(
        "Welke zin met si is fout?",
        ["Si j'aurais le temps, je viendrais.", "Si j'avais encore le temps, je viendrais.", "Si j'ai le temps, je viendrai.", "S'il pleut, je reste à la maison."],
        0,
        "Na si nooit een conditionnel.",
    ),
    mk(
        "Welke vorm past: « Il faut que nous ___ à l'heure. » (être)",
        ["soyons", "sommes", "serons", "étions"],
        0,
        "Subjonctif van être: que nous soyons.",
    ),
    mk(
        "Welke vorm past: « Je veux que tu ___ la vérité. » (dire)",
        ["dises", "dis", "diras", "disais"],
        0,
        "Ils disent → que tu dises.",
    ),
    mk(
        "Wat betekent « Il est en train de cuisiner »?",
        ["Hij is aan het koken", "Hij gaat straks koken", "Hij heeft net gekookt", "Hij kookt in de trein"],
        0,
        "Être en train de: bezig zijn met.",
    ),
    mk(
        "Wat is het participe présent van « faire »?",
        ["faisant", "fairant", "fait", "faiant"],
        0,
        "Nous faisons → faisant.",
    ),
    mk(
        "Welke zin betekent « Je had me kunnen helpen »?",
        ["Tu aurais pu m'aider.", "Tu pourras m'aider demain.", "Tu peux m'aider.", "Tu as pu m'aider."],
        0,
        "Conditionnel passé van pouvoir.",
    ),
    keuze(
        "« Nous [[*allons|allez]] partir dans cinq minutes. »",
        "Futur proche: nous allons + infinitief.",
    ),
    keuze(
        "« Je pense qu'il [[*viendra|vienne]] demain. »",
        "Na je pense que (bevestigend): indicatif.",
    ),
    keuze(
        "« Il [[*pleut|pleuvent]] depuis ce matin. »",
        "Onpersoonlijk werkwoord: enkel il.",
    ),
    keuze(
        "« Elle s'est blessée [[*en tombant|en tombée]] dans l'escalier. »",
        "Gérondif: en + participe présent.",
    ),
    keuze(
        "« Ils ne [[*peuvent|pouvent]] pas venir ce soir. »",
        "Pouvoir: ils peuvent.",
    ),
    tabel(
        "Juist of fout over de wijzen en tijden?",
        [
            ("Een wijs zegt hoe je iets bekijkt, een tijd wanneer.", J),
            ("Na vouloir volgt meestal een infinitief zonder voorzetsel.", J),
            ("De subjonctif vorm je uit de ils-vorm van het présent.", J),
            ("In een bevel zet je tu vóór het werkwoord.", F),
        ],
        "In een bevel valt het voornaamwoord weg.",
    ),
    inv(
        "Zet in de futur simple: « L'année prochaine, nous ___ en Espagne. » (aller)",
        ["irons"],
        "Stam ir- + -ons.",
    ),
    inv(
        "Zet in de subjonctif: « Il faut que vous ___ ce formulaire. » (remplir)",
        ["remplissiez"],
        "Ils remplissent → que vous remplissiez.",
    ),
    inv(
        "Zet in de conditionnel: « Tu ___ m'aider, s'il te plaît ? » (pouvoir)",
        ["pourrais"],
        "Stam pourr- + -ais.",
    ),
    sleep(
        "Si j'[[avais]] plus de temps, je [[ferais]] du sport. Mais il faut que je [[finisse]] mes études.",
        ["aurais", "finis"],
        "Si + imparfait, conditionnel; il faut que + subjonctif.",
    ),
    open_(
        "Schrijf in het Frans twee zinnen: wat je zou doen als je een miljoen won, en iets wat je spijt (j'aurais dû …).",
        "Si je gagnais un million, je ferais le tour du monde. J'aurais dû étudier plus pour mon examen de maths.",
    ),
    mk(
        "Welke vorm is de gérondif van « lire »?",
        ["en lisant", "en lirant", "en lu", "en lisé"],
        0,
        "Nous lisons → lisant.",
    ),
    keuze(
        "« Il [[*faut|faux]] partir tout de suite. »",
        "Il faut: onpersoonlijk werkwoord falloir.",
    ),
    tabel(
        "Welke vorm van de impératif is juist?",
        [
            ("Écoute bien !", J),
            ("Écoutes bien !", F),
            ("Finissons ce travail !", J),
            ("Tu prends ton manteau ! (als bevel in schrijftaal)", F),
        ],
        "Bij -er valt de s weg voor tu; het voornaamwoord valt weg.",
    ),
]
