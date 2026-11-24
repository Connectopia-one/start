"""Verleden tijden — pittig (🌍 Beyond doorstroom, Frans)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lisez le récit.\n\n"
    "C'était un samedi de juillet. Il faisait chaud et nous étions à la plage avec mes cousins. "
    "Mon oncle lisait le journal pendant que les enfants jouaient dans l'eau. "
    "Soudain, ma petite cousine a crié : elle avait perdu sa bague dans le sable. "
    "Nous l'avons cherchée pendant une heure. Finalement, mon frère l'a trouvée sous une serviette. "
    "Le soir, nous sommes rentrés fatigués mais contents."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            tabel(
                "Welke tijd staat in de tekst?",
                [
                    ("il faisait chaud", "imparfait"),
                    ("ma cousine a crié", "passé composé"),
                    ("elle avait perdu", "plus-que-parfait"),
                    ("mon oncle lisait", "imparfait"),
                    ("nous sommes rentrés", "passé composé"),
                ],
                "Decor en bezigheid: imparfait; gebeurtenis: passé composé; nog eerder: plus-que-parfait.",
                kolommen=["imparfait", "passé composé", "plus-que-parfait"],
            ),
            mk(
                "Waarom staat « avait perdu » in de plus-que-parfait?",
                ["Het verlies kwam vóór de kreet", "Het is een vaste gewoonte van haar", "Het beschrijft het weer op het strand", "Het gebeurt pas later in het verhaal"],
                0,
                "Iets wat nog eerder gebeurde dan een andere verleden handeling.",
            ),
            keuze(
                "In « mon frère l'a trouvée » krijgt trouvée een -e omdat l' [[*voor la bague staat|het onderwerp is]].",
                "Een lijdend voorwerp vóór avoir: het deelwoord komt ermee overeen.",
            ),
            keuze(
                "Het woord « soudain » kondigt [[*een plotse gebeurtenis|een gewoonte]] aan.",
                "Soudain: plots, dus passé composé.",
            ),
            inv(
                "Welk hulpwerkwoord gebruikt de verteller bij rentrer? Geef de vorm uit de tekst.",
                ["sommes"],
                "Nous sommes rentrés: rentrer neemt être.",
            ),
        ],
    ),
    sorteer(
        "Neemt dit werkwoord avoir of être in de passé composé?",
        ["avoir", "être"],
        [
            ("manger", "avoir"),
            ("tomber", "être"),
            ("se lever", "être"),
            ("prendre", "avoir"),
            ("venir", "être"),
            ("faire", "avoir"),
        ],
        "Wederkerende werkwoorden en een kleine groep zoals aller, venir, tomber nemen être.",
    ),
    tabel(
        "Wat is het voltooid deelwoord?",
        [
            ("mettre", "mis"),
            ("voir", "vu"),
            ("écrire", "écrit"),
            ("apprendre", "appris"),
        ],
        "Onregelmatige deelwoorden leer je vanbuiten.",
        kolommen=["mis", "vu", "écrit", "appris"],
    ),
    koppel(
        "Koppel de nous-vorm van het présent aan de imparfait.",
        [
            ("nous finissons", "je finissais"),
            ("nous faisons", "je faisais"),
            ("nous prenons", "je prenais"),
            ("nous buvons", "je buvais"),
        ],
        ["j'étions"],
        "Stam van de nous-vorm + -ais.",
    ),
    volgorde(
        "Zet deze gebeurtenissen in de volgorde waarin ze echt gebeurden: « Quand je suis arrivé, le film avait commencé. Je venais de m'asseoir quand mon téléphone a sonné. »",
        ["le film a commencé", "je suis arrivé", "je me suis assis", "mon téléphone a sonné"],
        "De plus-que-parfait gaat vooraf; venir de: net.",
    ),
    mk(
        "Welke zin met partir in de passé composé is juist?",
        ["Elles sont parties à 8 h.", "Elles ont parties à huit heures.", "Elles sont parti à huit heures.", "Elles ont partis à huit heures."],
        0,
        "Partir neemt être; het deelwoord volgt elles.",
    ),
    mk(
        "Welke tijd past: « Quand j'avais dix ans, je ___ au foot tous les mercredis. »",
        ["jouais", "ai joué", "avais joué", "viens de jouer"],
        0,
        "Tous les mercredis: gewoonte, dus imparfait.",
    ),
    mk(
        "« Nous venons de finir le repas. » Wanneer was de maaltijd gedaan?",
        ["net, daarnet", "lang geleden", "morgen", "elke dag opnieuw"],
        0,
        "Venir de + infinitief: passé récent.",
    ),
    mk(
        "Welke vorm is juist: « Les fleurs qu'il a ___ sont belles. » (offrir)",
        ["offertes", "offert", "offerts", "offrites"],
        0,
        "Que = les fleurs, vrouwelijk meervoud, vóór avoir.",
    ),
    mk(
        "Welke zin is juist bij een wederkerend werkwoord?",
        ["Elle s'est brossé les dents.", "Elle s'est brossée les dents.", "Elle a brossé se les dents.", "Elle s'a brossé les dents."],
        0,
        "Les dents is het lijdend voorwerp; se is hier meewerkend.",
    ),
    mk(
        "Welke tijd gebruik je in een mail aan een vriend over je weekend?",
        ["passé composé en imparfait", "vooral de passé simple uit boeken", "enkel de plus-que-parfait", "de futur simple en de conditionnel"],
        0,
        "De passé simple is boekentaal.",
    ),
    keuze(
        "« Il [[*pleuvait|a plu]] quand je suis sorti, alors j'ai pris un parapluie. » (achtergrond)",
        "Het weer als decor: imparfait.",
    ),
    keuze(
        "« Hier soir, je [[*suis allé|ai allé]] au cinéma. »",
        "Aller neemt être.",
    ),
    keuze(
        "« Ils [[*ont|sont]] mangé une pizza. »",
        "Manger neemt avoir.",
    ),
    keuze(
        "« Quand nous sommes arrivés, le train [[*était déjà parti|partait déjà]]. »",
        "Nog eerder: plus-que-parfait.",
    ),
    keuze(
        "« Elles nous ont [[*parlé|parlées]] de leur voyage. »",
        "Nous is een COI: geen overeenkomst.",
    ),
    tabel(
        "Juist of fout over de verleden tijden?",
        [
            ("De imparfait van être begint met ét-.", J),
            ("De uitgang voor ils in de imparfait is -aient.", J),
            ("Met avoir komt het deelwoord altijd overeen met het onderwerp.", F),
            ("De plus-que-parfait gebruikt het hulpwerkwoord in de imparfait.", J),
        ],
        "Met avoir: enkel overeenkomst met een lijdend voorwerp dat vóór staat.",
    ),
    inv(
        "Zet in de imparfait: « Tu ___ toujours en retard. » (être)",
        ["étais"],
        "Tu étais.",
    ),
    inv(
        "Zet in de passé composé met één woord voor het deelwoord: « Nous avons ___ nos devoirs. » (faire)",
        ["fait"],
        "Faire: fait.",
    ),
    inv(
        "Zet in de plus-que-parfait (enkel het hulpwerkwoord): « Elle ___ déjà mangé quand je suis venu. »",
        ["avait"],
        "Avoir in de imparfait + deelwoord.",
    ),
    sleep(
        "Quand j'[[étais]] petit, nous [[allions]] chaque été en Bretagne. Une année, mon père [[a perdu]] les clés de la voiture.",
        ["suis", "perdait"],
        "Gewoonte in de imparfait, één gebeurtenis in de passé composé.",
    ),
    open_(
        "Vertel in het Frans in drie zinnen over een vakantiedag: één zin met het weer (imparfait), één met wat er plots gebeurde (passé composé) en één met wat al eerder gebeurd was (plus-que-parfait).",
        "Il faisait beau à Nice. Soudain, mon sac a disparu. Je l'avais laissé sur la plage.",
    ),
    mk(
        "Welke vorm is juist voor « wij waren gelukkig »?",
        ["Nous étions heureux.", "Nous avons été heureux tous.", "Nous sommes étés heureux.", "Nous étons heureux."],
        0,
        "Être in de imparfait: nous étions.",
    ),
    mk(
        "Waarom staat « lisait » in de imparfait in « il lisait quand on a sonné »?",
        ["Het is de bezigheid op de achtergrond", "Het is een plotse, korte gebeurtenis", "Het gebeurde nog vóór al de rest", "Het is een bevel aan de lezer"],
        0,
        "Bezigheid die onderbroken wordt: imparfait.",
    ),
    keuze(
        "« Hier, il [[*a neigé|neigeait]] toute la journée, puis le soleil est revenu. » (afgeronde periode)",
        "Een afgebakende periode die voorbij is: passé composé.",
    ),
    tabel(
        "Imparfait of passé composé?",
        [
            ("Chaque matin, je ___ le bus. (prendre)", "prenais"),
            ("Ce matin-là, j'___ le train. (prendre)", "ai pris"),
            ("Le ciel ___ gris. (être)", "était"),
        ],
        "Gewoonte en decor: imparfait; één keer: passé composé.",
        kolommen=["prenais", "ai pris", "était"],
    ),
]
