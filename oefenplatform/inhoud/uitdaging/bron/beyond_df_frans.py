# -*- coding: utf-8 -*-
"""Uitdaging Frans 🌍 Beyond dubbele finaliteit (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die alle hoofdstukken
door elkaar halen. Een zelf geschreven affiche en een berichtje om op te
klikken, tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde en een
korte schrijfopdracht. Geen nieuwe leerstof: alles staat in de hoofdstukken
van Frans Beyond dubbele finaliteit.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_df_frans.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Frans"
BESTAND = "beyond-df-frans-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/frans-beyond-df-uitdaging"
AFFICHE = "affiche-brocante.svg"
SMS = "sms-hugo.svg"


def zin(i, n=6):
    """Klikvak van zin i (vanaf 1), zie uitdaging/_blad.py."""
    h = 90 + n * 92 + 30
    return [2, round((90 + (i - 1) * 92) / h * 100, 1), 96, round(92 / h * 100, 1)]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Affiche (prent)
    klik("Lees de affiche. Klik op de regel die zegt hoeveel je betaalt als je zelf iets wil verkopen.",
         AFFICHE, [zin(4)],
         "'Un emplacement pour vendre coûte 10 euros': een standplaats om te verkopen kost 10 euro."),
    klik("Klik op de regel met een verbod.",
         AFFICHE, [zin(6)],
         "'Il est interdit de ...' betekent: het is verboden om ... Je mag er geen dieren verkopen."),
    klik("Klik op de regel die zegt tegen wanneer je je moet inschrijven.",
         AFFICHE, [zin(5)],
         "'Inscrivez-vous avant le 1er juin': schrijf je in vóór 1 juni, op het gemeentehuis (la mairie)."),
    met_prent(AFFICHE, tabel(
        "Klopt dit volgens de affiche?",
        [
            ("De rommelmarkt is op een zondag.", J),
            ("Bezoekers betalen 10 euro inkom.", F),
            ("De markt duurt tot 17 uur.", J),
            ("Je schrijft je in bij de politie.", F),
        ],
        "Le dimanche = zondag, de ingang is gratis voor bezoekers, de markt loopt tot 17 uur en je schrijft je in op de mairie (gemeentehuis).")),
    met_prent(AFFICHE, keuze(
        "In regel 5 staat het werkwoord in de [[*gebiedende wijs|verleden tijd|toekomende tijd]]. Een affiche is vooral een [[*informatieve|narratieve]] tekst.",
        "'Inscrivez-vous' is een bevel in de vous-vorm. De affiche geeft praktische informatie.")),

    # SMS (prent)
    klik("Lees het bericht van Hugo. Klik op de zin waarin hij een voorstel doet om eerst iets te eten.",
         SMS, [zin(4)],
         "'On pourrait manger une pizza' betekent: we zouden een pizza kunnen eten. De conditionnel maakt het voorstel vriendelijk."),
    klik("Klik op de zin die zegt hoe Hugo naar Léa komt.",
         SMS, [zin(5)],
         "'Je passe te chercher à 19 heures en vélo': ik kom je om 19 uur met de fiets halen."),
    met_prent(SMS, tabel(
        "Wat betekent dit stukje uit het bericht?",
        [
            ("Tu es libre samedi soir ?", "Ben je zaterdagavond vrij?"),
            ("un concert gratuit", "een gratis concert"),
            ("Réponds-moi vite !", "Antwoord me snel!"),
        ],
        "Libre is vrij, gratuit is gratis en réponds-moi is de gebiedende wijs van répondre met moi.",
        kolommen=["Ben je zaterdagavond vrij?", "een gratis concert", "Antwoord me snel!"])),
    met_prent(SMS, mk(
        "Welk antwoord van Léa past bij het bericht?",
        ["Super idée ! À samedi, 19 heures !", "Madame, Monsieur, je vous remercie.", "Je voudrais réserver une chambre double.", "Veuillez agréer mes salutations distinguées."],
        0,
        "Het bericht is informeel. Een kort, enthousiast antwoord past; formele briefzinnen niet.")),

    # Tekstsoorten en cultuur
    tabel(
        "Tot welk soort tekst behoort deze Franse zin?",
        [
            ("Prenez la deuxième rue à gauche.", "Instructie"),
            ("Il était une fois un roi très riche.", "Verhaal"),
            ("Achetez maintenant : -50 % sur tout !", "Reclame"),
            ("Paris compte environ deux millions d'habitants.", "Informatie"),
        ],
        "Een wegbeschrijving geeft instructies, 'il était une fois' begint een verhaal, een korting wil je laten kopen, een feit informeert.",
        kolommen=["Informatie", "Instructie", "Verhaal", "Reclame"]),
    keuze(
        "Als je in Frankrijk een onbekende volwassene aanspreekt, zeg je [[*vous|tu]]. 's Avonds groet je met [[*bonsoir|bonjour|bonne nuit]] als je ergens binnenkomt.",
        "Vous is beleefd. Bonsoir gebruik je als groet 's avonds; bonne nuit zeg je pas bij het slapengaan."),
    mk("Wat bestel je in een Franse bakkerij als je een stokbrood wil?",
       ["Une baguette, s'il vous plaît.", "Un croissant au jambon, merci.", "Une bouteille de lait, merci bien.", "Un steak frites, s'il vous plaît."],
       0,
       "Une baguette is het typische lange Franse stokbrood."),

    # Woordvelden
    koppel(
        "Koppel het Franse woord aan de vertaling.",
        [
            ["la gare", "het station"],
            ["un médicament", "een geneesmiddel"],
            ["le salaire", "het loon"],
            ["une poubelle", "een vuilnisbak"],
            ["un horaire", "een uurrooster"],
        ],
        ["een schilderij", "een boekhandel"],
        "Deze woorden komen uit de woordvelden reizen, gezondheid, werk, milieu en school."),
    sorteer(
        "In welk woordveld past dit Franse woord?",
        ["Eten", "Wonen", "Natuur en milieu"],
        [
            ["le fromage", "Eten"],
            ["la cuisine", "Wonen"],
            ["le recyclage", "Natuur en milieu"],
            ["une salade", "Eten"],
            ["la chambre", "Wonen"],
            ["la pollution", "Natuur en milieu"],
        ],
        "Kaas en sla horen bij eten, keuken en slaapkamer bij wonen, recyclage en vervuiling bij milieu."),
    inv("Hoe zeg je 'de dokter' in het Frans? Met lidwoord.",
        ["le médecin", "le docteur"],
        "Le médecin of le docteur is de dokter."),
    keuze(
        "Ik heb buikpijn: j'ai mal [[*au ventre|à la ventre|aux ventre]]. Ik heb keelpijn: j'ai mal [[*à la gorge|au gorge]].",
        "À + le wordt au (le ventre is mannelijk). La gorge is vrouwelijk: à la gorge."),

    # Lidwoorden en getallen
    keuze(
        "Je mange [[*des|de les]] pommes. Je n'ai pas [[*de|des|un]] voiture. C'est le livre [[*du|de le]] professeur.",
        "De + les wordt des, de + le wordt du. Na een ontkenning wordt un, une, des: de."),
    tabel(
        "Schrijf het getal.",
        [
            ("soixante-dix", "70"),
            ("quatre-vingts", "80"),
            ("quatre-vingt-dix", "90"),
            ("cent vingt", "120"),
        ],
        "In Frankrijk zeg je soixante-dix (60 + 10), quatre-vingts (4 · 20) en quatre-vingt-dix (4 · 20 + 10). In België hoor je ook septante en nonante.",
        kolommen=["70", "80", "90", "120"]),
    tabel(
        "Welk bezittelijk woord past?",
        [
            ("C'est ___ sœur. (van mij)", "ma"),
            ("Ce sont ___ parents. (van ons)", "nos"),
            ("Il a perdu ___ clés. (van hem)", "ses"),
        ],
        "Ma voor een vrouwelijk enkelvoud, nos voor 'onze' in het meervoud, ses voor 'zijn' of 'haar' in het meervoud.",
        kolommen=["ma", "nos", "ses"]),

    # Voornaamwoorden
    keuze(
        "Tu vois le chien ? Oui, je [[*le|lui|la]] vois. Tu parles à Marie ? Oui, je [[*lui|la|le]] parle.",
        "Le vervangt een mannelijk lijdend voorwerp. Lui vervangt à + persoon (meewerkend voorwerp)."),
    keuze(
        "C'est la fille [[*qui|que]] habite à côté. C'est le film [[*que|qui]] j'ai vu hier.",
        "Qui is onderwerp van de bijzin (zij woont), que is lijdend voorwerp (ik heb hem gezien)."),

    # Bijvoeglijke naamwoorden en bijwoorden
    tabel(
        "Wat is de vrouwelijke vorm?",
        [
            ("grand", "grande"),
            ("heureux", "heureuse"),
            ("sportif", "sportive"),
            ("beau", "belle"),
        ],
        "Meestal komt er een -e bij. -eux wordt -euse, -if wordt -ive en beau is onregelmatig: belle.",
        kolommen=["grande", "heureuse", "sportive", "belle"]),
    keuze(
        "Il parle [[*lentement|lent]]. Elle chante [[*bien|bon]]. Paris est [[*plus grand que|plus grand de]] Bruxelles.",
        "Een bijwoord zegt hoe iemand iets doet: lentement, bien. Bij een vergelijking gebruik je plus ... que."),
    tabel(
        "Welk Frans voorzetsel hoort bij het land of de stad?",
        [
            ("J'habite ___ Belgique.", "en"),
            ("Je vais ___ Paris.", "à"),
            ("Il vient ___ Canada.", "du"),
        ],
        "En bij vrouwelijke landen, à bij steden, du (de + le) bij mannelijke landen waar je vandaan komt.",
        kolommen=["en", "à", "du"]),

    # Tijden
    tabel(
        "Vervoeg in de présent.",
        [
            ("nous (aller)", "allons"),
            ("ils (faire)", "font"),
            ("vous (être)", "êtes"),
            ("je (prendre)", "prends"),
        ],
        "Aller, faire, être en prendre zijn onregelmatig en moet je kennen.",
        kolommen=["allons", "font", "êtes", "prends"]),
    keuze(
        "Hier, je [[*suis allé|ai allé]] au cinéma. Nous [[*avons mangé|sommes mangé]] au restaurant. Elle [[*est partie|a partie]] à huit heures.",
        "Aller en partir nemen être; manger neemt avoir. Bij être regelt het deelwoord zich naar het onderwerp: elle est partie."),
    tabel(
        "Passé composé of imparfait?",
        [
            ("Quand j'étais petit, je jouais au foot.", "Imparfait"),
            ("Hier, j'ai acheté un vélo.", "Passé composé"),
            ("Il faisait beau ce jour-là.", "Imparfait"),
            ("Soudain, le téléphone a sonné.", "Passé composé"),
        ],
        "Imparfait voor een beschrijving of gewoonte in het verleden, passé composé voor een afgeronde handeling.",
        kolommen=["Passé composé", "Imparfait"]),
    inv("Vervoeg in de futur simple: « Demain, je ___ (finir) mon travail. »",
        ["finirai"],
        "Futur simple: infinitief + uitgang: finir + ai = finirai."),
    keuze(
        "Je [[*voudrais|veux|voulais]] un café, s'il vous plaît. Si j'avais de l'argent, j'[[*achèterais|achète|achèterai]] une moto.",
        "De conditionnel maakt een vraag beleefd. Na si + imparfait volgt de conditionnel."),
    mk("Welke zin staat in de futur proche?",
       ["Je vais partir demain.", "Je suis parti hier matin.", "Je partais chaque matin.", "Je partirais bien demain."],
       0,
       "Futur proche: aller in de présent + infinitief: je vais partir."),

    # Zinsbouw
    volgorde(
        "Zet de Franse woorden in de juiste volgorde.",
        ["Je", "ne", "mange", "jamais", "de viande", "le soir"],
        "Ne staat voor het werkwoord en jamais erna."),
    sleep(
        "Les filles sont [[contentes]]. Mon frère et ma sœur sont [[grands]].",
        ["content", "grandes"],
        "Het bijvoeglijk naamwoord past zich aan: vrouwelijk meervoud krijgt -es. Bij een mannelijk en een vrouwelijk woord samen gebruik je het mannelijk meervoud."),
    mk("Hoe stel je deze vraag beleefd? Je wil weten waar het station is.",
       ["Pardon, pourriez-vous me dire où est la gare ?", "Hé, la gare elle est où, dis-moi vite ?", "Gare ? Où ? Vite, je suis pressé, mon vieux !", "Tu dois me dire où se trouve la gare tout de suite."],
       0,
       "Pardon en pourriez-vous (conditionnel) maken de vraag beleefd."),

    # Extra
    keuze(
        "Op het menu staat « plat du jour ». Dat is [[*de dagschotel|het dessert|de drankkaart]].",
        "Le plat du jour is de schotel van de dag."),
    tabel(
        "Formeel of informeel in het Frans?",
        [
            ("Madame, Monsieur,", "Formeel"),
            ("Coucou !", "Informeel"),
            ("Je vous prie d'agréer mes salutations distinguées.", "Formeel"),
            ("À plus !", "Informeel"),
        ],
        "In een formele brief gebruik je vaste beleefde formules. Tegen vrienden mag het kort en los.",
        kolommen=["Formeel", "Informeel"]),
    mk("Wat betekent « Il pleut des cordes » ?",
       ["Het regent pijpenstelen.", "Het touw is nat geworden.", "Er hangen koorden in de lucht.", "Het is een beetje bewolkt."],
       0,
       "Een uitdrukking voor hevige regen: het regent pijpenstelen."),

    tabel(
        "Welk woord hoort bij het verkeer?",
        [
            ("Het licht staat op rood: le ___", "feu"),
            ("Waar je de trein neemt: le ___", "quai"),
            ("Waar je veilig oversteekt: le passage ___", "piéton"),
        ],
        "Le feu rouge is het rode licht, le quai het perron en le passage piéton het zebrapad.",
        kolommen=["feu", "quai", "piéton"]),
    keuze(
        "Il fait froid : [[*mets|met|mettre]] ton manteau ! [[*Allons|Allez-nous]] au parc ensemble !",
        "Gebiedende wijs: tu-vorm zonder onderwerp (mets), nous-vorm: allons."),
    inv("Vul in met de juiste vorm van « avoir » in de présent: « Nous ___ deux chats. »",
        ["avons"],
        "Avoir: j'ai, tu as, il a, nous avons, vous avez, ils ont."),

    # Schrijfopdracht
    open_("Écris un court message (4 à 6 phrases) à un ami. Tu l'invites à faire du vélo dimanche. Dis où et quand vous partez, ce que vous allez faire et demande une réponse.",
          "Salut Tom ! Tu veux faire du vélo avec moi dimanche ? On part à dix heures devant l'école. On va rouler jusqu'au lac et on va pique-niquer là-bas. N'oublie pas ton casque ! Réponds-moi vite. À dimanche, Lies",
          "Een goed antwoord heeft een informele begroeting en afsluiting, zegt waar en wanneer jullie vertrekken, wat jullie gaan doen (aller + infinitief) en vraagt om een antwoord."),
]
