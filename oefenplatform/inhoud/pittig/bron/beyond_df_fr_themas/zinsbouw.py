"""Zinsbouw, zinsdelen en congruentie — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis le texte.\n\n« Ma sœur et moi, nous habitons à Namur. Le samedi, nous allons à la piscine parce que nous aimons nager. "
        "Ma sœur téléphone souvent à notre grand-mère, mais moi, je ne téléphone jamais : je préfère écrire des lettres. "
        "Quelle belle idée, dit mamie ! Les lettres qu'elle reçoit sont toujours longues et drôles. »",
        [
            keuze("« nous allons » volgt het onderwerp « ma sœur et moi », want dat is hetzelfde als [[*nous|vous|ils]].", "Ma sœur et moi = nous."),
            keuze("« parce que » betekent [[*omdat|maar|dus]].", "Parce que geeft een reden."),
            keuze("In « Ma sœur téléphone à notre grand-mère » is « à notre grand-mère » een [[*COI|COD]].", "Na à: COI."),
            keuze("« Quelle belle idée ! » is een [[*uitroepzin|vraagzin|bevelzin]].", "Quel vooraan en een uitroepteken."),
            keuze("« longues et drôles » krijgen een s omdat « les lettres » [[*meervoud|enkelvoud]] is.", "Het bijvoeglijk naamwoord volgt het naamwoord."),
        ],
    ),
    tabel("Welk soort zin is het?", [
        ("Tu viens avec nous ?", "vraagzin"), ("Ferme la porte !", "bevelzin"), ("Comme c'est beau !", "uitroepzin"), ("Il pleut depuis ce matin.", "mededelende zin"),
    ], "Vraagteken, bevel zonder onderwerp, quel of comme met uitroepteken.",
        kolommen=["vraagzin", "bevelzin", "uitroepzin", "mededelende zin"]),
    tabel("COD of COI?", [
        ("Je regarde la télé.", "COD"), ("Je parle à mon prof.", "COI"), ("Elle mange une pomme.", "COD"), ("Il ressemble à son père.", "COI"),
    ], "Zonder voorzetsel COD, met à COI.", kolommen=["COD", "COI"]),
    koppel("Koppel elk voegwoord aan zijn betekenis.", [
        ["mais", "maar"], ["donc", "dus"], ["parce que", "omdat"], ["pendant que", "terwijl"],
    ], ["hoewel"], "Hoewel staat niet in de lijst."),
    koppel("Koppel elke ontkenning aan haar betekenis.", [
        ["ne ... jamais", "nooit"], ["ne ... rien", "niets"], ["ne ... plus", "niet meer"], ["ne ... personne", "niemand"],
    ], ["altijd"], "Toujours is altijd."),
    mk("« Les élèves et le prof ___ en classe. » (travailler) Welke vorm past?",
       ["travaillent", "travaille", "travailles", "travaillerons"], 0, "Twee onderwerpen samen: meervoud."),
    mk("« Beaucoup de touristes ___ à Bruges. » (venir) Welke vorm past?",
       ["viennent", "vient", "venons", "venaient-ils"], 0, "Het werkwoord volgt touristes."),
    mk("Welke zin over mijn vriendinnen klopt?",
       ["Mes amies sont contentes.", "Mes amies sont content.", "Mes amies est contentes.", "Mes amies sont contentes, elle."], 0,
       "Vrouwelijk meervoud: contentes."),
    mk("Welke zin heeft de juiste woordorde?",
       ["Il me donne le livre.", "Il le me donne le livre.", "Il donne me le livre.", "Il donne le livre à me."], 0,
       "Me staat voor het werkwoord."),
    mk("« Je ne vais pas à la fête ___ je suis malade. » Welk voegwoord past?",
       ["parce que", "mais", "donc", "pendant que"], 0, "Een reden: parce que."),
    mk("« Il fait froid, ___ je mets un pull. » Welk voegwoord past?",
       ["donc", "parce que", "pendant que", "ou"], 0, "Een gevolg: donc."),
    mk("Wat is het sujet in « Demain, mes parents partent en vacances »?",
       ["mes parents", "demain", "en vacances", "partent en vacances"], 0, "Wie vertrekt? Mes parents."),
    inv("Vul in: « Ma sœur et moi ___ au cinéma. » (aller) Eén woord.", ["allons"], "Ma sœur et moi = nous."),
    inv("Vul in: « On ___ à huit heures. » (manger) Eén woord.", ["mange"], "On vraagt enkelvoud."),
    inv("Vul in: « Ce sont des livres ___. » (intéressant) Eén woord.", ["intéressants"], "Meervoud: s."),
    inv("Vul in: « Je reste ici ___ il pleut. » (omdat) Twee woorden.", ["parce qu'", "parce que", "car"], "Parce qu' voor een klinker."),
    keuze("« Je ne mange [[*jamais|toujours]] de viande : je suis végétarien. »", "Ne ... jamais: nooit."),
    keuze("« Je [[*la|lui]] regarde. » (la télé)", "COD vervangen door la."),
    keuze("« Je [[*lui|le]] téléphone ce soir. » (à ma mère)", "COI met à vervangen door lui."),
    keuze("« [[*Est-ce que|Est-ce qu']] tu as faim ? »", "Est-ce que voor een medeklinker."),
    keuze("« Si seulement il [[*faisait|fait]] beau ! »", "Wenszin: si seulement + imparfait."),
    tabel("Is de zin juist (zinsbouw)?", [
        ("Demain, je vais à Paris.", J), ("Je ne sais rien pas.", F), ("Les filles sont grandes.", J), ("Nous joue au foot.", F),
    ], "Ne ... rien zonder pas; nous jouons."),
    volgorde("Zet de woorden in de juiste volgorde: « une pomme / Marie / à son frère / donne »", [
        "Marie", "donne", "une pomme", "à son frère",
    ], "Sujet, verbe, COD, COI."),
    sleep("Je reste à la maison [[parce qu']]il pleut, [[mais]] demain je sortirai.",
          ["donc", "pendant qu'"], "Een reden en een tegenstelling."),
    mk("In welke zin zegt een bijzin met qui iets over le garçon?",
       ["Le garçon qui joue au foot est mon frère.", "Le garçon joue au foot et il rit.", "Le garçon joue au foot avec son frère.", "Le garçon ne joue jamais au foot le soir, lui."], 0,
       "Qui joue au foot zegt iets over le garçon."),
    open_("Leg in het Nederlands uit waarom je « les enfants jouent » schrijft met -ent.",
          "Les enfants is meervoud (ils), dus het werkwoord krijgt de uitgang -ent.",
          "Het werkwoord volgt het onderwerp."),
]
