"""Lidwoorden, aanwijzers, bezitters en getallen — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis la liste de courses de Léa.\n\n« Pour la fête de samedi : un kilo de tomates, du fromage, de la salade, des chips et beaucoup de jus d'orange. "
        "Il n'y a plus de pain à la maison. Mon frère va aux magasins avec ses amis. "
        "Cette fête, c'est pour les quatre-vingts ans de notre grand-père ! »",
        [
            keuze("« un kilo de tomates » : na een hoeveelheid komt enkel [[*de|des|du]].", "Un kilo de, beaucoup de."),
            keuze("« de la salade » is een [[*partitief lidwoord|samengetrokken lidwoord]].", "Een onbepaalde hoeveelheid."),
            keuze("« Il n'y a plus de pain » : na ne ... plus wordt du [[*de|des]].", "Net als na pas."),
            keuze("« aux magasins » is à + [[*les|le|la]].", "À + les = aux."),
            inv("Hoe oud wordt de grootvader? Geef het getal.", ["80", "tachtig"], "Quatre-vingts: 80."),
        ],
    ),
    tabel("Is het samengetrokken lidwoord juist?", [
        ("Je vais au cinéma.", J), ("Je viens de le magasin.", F), ("Je parle aux élèves.", J), ("Je vais à le parc.", F),
    ], "De + le = du; à + le = au."),
    sorteer("Ce, cet of cette?", ["ce", "cet", "cette"], [
        ["___ jardin", "ce"], ["___ arbre", "cet"], ["___ semaine", "cette"], ["___ livre", "ce"], ["___ enfant", "cet"], ["___ maison", "cette"],
    ], "Cet voor een mannelijk woord met een klinker."),
    sorteer("Mon of ma?", ["mon", "ma"], [
        ["___ frère", "mon"], ["___ sœur", "ma"], ["___ amie", "mon"], ["___ école", "mon"], ["___ voiture", "ma"], ["___ vélo", "mon"],
    ], "Voor een klinker wordt ma altijd mon."),
    koppel("Koppel elk getal aan de Franse schrijfwijze (Frankrijk).", [
        ["71", "soixante et onze"], ["80", "quatre-vingts"], ["81", "quatre-vingt-un"], ["200", "deux cents"],
    ], ["deux milles"], "Mille krijgt nooit een s."),
    koppel("Koppel elk rangtelwoord aan het getal.", [
        ["premier", "1"], ["cinquième", "5"], ["neuvième", "9"], ["vingt et unième", "21"],
    ], ["unième"], "Unième bestaat niet alleen."),
    mk("« Je ne bois pas ___ café. » Welk woord past?",
       ["de", "du", "le", "des"], 0, "Na een ontkenning: de."),
    mk("« Ce n'est pas ___ pain, c'est du gâteau. » Welk woord past?",
       ["du", "de", "le", "d'"], 0, "Na être blijft het partitief lidwoord."),
    mk("Hoe zeg je « Ik heb pijn aan mijn hand »?",
       ["J'ai mal à la main.", "J'ai mal à ma main.", "J'ai mal de la main.", "J'ai mal au main."], 0,
       "Bij een lichaamsdeel: bepaald lidwoord."),
    mk("Hoe zeg je « Hij is leraar »?",
       ["Il est professeur.", "Il est un professeur.", "Il est le professeur.", "Il est du professeur."], 0,
       "Bij een beroep na être valt het lidwoord weg."),
    mk("« Les enfants jouent avec ___ chiens. » Hun honden, meer dan één. Wat past?",
       ["leurs", "leur", "ses", "son"], 0, "Leurs bij meer dingen."),
    mk("« ___ heure est-il ? » Welke vorm past?",
       ["Quelle", "Quel", "Quels", "Quelles"], 0, "Heure is vrouwelijk enkelvoud."),
    mk("Wat is het meervoud van « un animal »?",
       ["des animaux", "des animals", "des animales", "des animauxs"], 0, "-al wordt -aux."),
    inv("Vul in: « J'aime ___ chocolat. » (in het algemeen) Eén woord.", ["le"], "Algemene uitspraak: le."),
    inv("Vul in: « Elle boit ___ eau. » Twee woorden.", ["de l'", "de l"], "De l' voor een klinker."),
    inv("Schrijf « de derde » in het Frans. Eén woord.", ["troisième"], "Trois + -ième."),
    inv("Vul in: « ___ jour, je vais à l'école à pied. » (elke) Eén woord.", ["chaque", "Chaque"], "Chaque + enkelvoud."),
    keuze("« Il a [[*quelques|chaque]] amis à Paris. »", "Quelques: enkele."),
    keuze("« Ils habitent [[*aux|au]] Pays-Bas. »", "Les Pays-Bas: aux."),
    keuze("« [[*Ces|Cettes]] maisons sont belles. »", "Ces voor mannelijk en vrouwelijk meervoud."),
    keuze("« C'est [[*votre|vos]] école ? »", "Votre bij één ding."),
    keuze("« On est le [[*premier|un]] mai. »", "Enkel de eerste krijgt een rangtelwoord."),
    tabel("Is het woord mannelijk?", [
        ("le voyage", J), ("la table", F), ("le fromage", J), ("l'eau", F),
    ], "Woorden op -age zijn meestal mannelijk; eau is vrouwelijk."),
    volgorde("Zet de getallen van klein naar groot.", [
        "soixante-dix", "soixante et onze", "quatre-vingts", "quatre-vingt-dix",
    ], "70, 71, 80, 90."),
    sleep("Je voudrais [[un litre de]] lait et [[du]] fromage, s'il vous plaît.",
          ["un litre du", "de le"], "Na een hoeveelheid de; voor een mannelijk woord du."),
    open_("Leg in het Nederlands uit waarom je « mon amie » zegt en niet « ma amie ».",
          "Voor een woord dat met een klinker begint wordt ma mon, om de klank.",
          "Zo botsen twee klinkers niet."),
]
