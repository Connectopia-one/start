# -*- coding: utf-8 -*-
"""Uitdaging Frans 🚀 Boost doorstroom (25 november 2026), in de vormen van het
examen van de Examencommissie: 40 vragen die alle hoofdstukken door elkaar
halen. Een kort verhaal en een formele mail om op te klikken, tabellen,
keuzelijsten, slepen, koppelen, sorteren, volgorde, invulvragen en een korte
schrijfopdracht. Geen nieuwe leerstof: alles staat in de hoofdstukken van
Frans Boost doorstroom. De prenten tekent
inhoud/uitdaging/maak_prenten_boost_frans.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Frans"
BESTAND = "boost-frans-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/frans-boost-uitdaging"
VERHAAL = "verhaal-marche.svg"
MAIL = "mail-benevole.svg"

# klikvakken: _blad.zone(i, 6)
Z = {1: [2, 13.4, 96, 13.7], 2: [2, 27.1, 96, 13.7], 3: [2, 40.8, 96, 13.7],
     4: [2, 54.5, 96, 13.7], 5: [2, 68.2, 96, 13.7], 6: [2, 81.8, 96, 13.7]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Verhaal (prent)
    klik("Lees het verhaal 'Au marché'. Klik op de zin met een plus-que-parfait.",
         VERHAAL, [Z[3]],
         "'Elles avaient oublié' is een plus-que-parfait (imparfait van avoir + voltooid deelwoord). Het vergeten gebeurde vóór het kopen."),
    klik("Klik op de zin die alleen de achtergrond beschrijft, in de imparfait.",
         VERHAAL, [Z[2]],
         "'Il faisait beau' en 'la place était pleine' beschrijven de toestand: dat is de imparfait."),
    klik("Klik op de zin met een futur simple.",
         VERHAAL, [Z[6]],
         "'Léa reviendra' is de futur simple van revenir: ze zal terugkomen."),
    met_prent(VERHAAL, tabel(
        "Wat vertelt het verhaal over Léa? Duid aan wat klopt.",
        [
            ("Léa ging met haar grootmoeder naar de markt.", J),
            ("Het regende die zaterdag.", F),
            ("Een hond stal een stokbrood.", J),
            ("De bakker werd boos.", F),
        ],
        "Het was mooi weer (il faisait beau). Iedereen lachte, ook de bakker (même le boulanger).")),
    met_prent(VERHAAL, keuze(
        "In zin 3 vervangt 'en' [[*un sac|la place|le marché]]. In zin 4 staat 'payaient' in de imparfait omdat het betalen [[*aan de gang was|plots gebeurde]] toen de hond toesloeg.",
        "En vervangt een hoeveelheid of een naamwoord met un/des: elles en ont acheté un = een zak. De imparfait toont wat bezig was, de passé composé wat plots gebeurde.")),

    # Mail (prent)
    klik("Lees de mail aan de bibliotheek. Klik op de zin waarin Emma beleefd een vraag stelt met de conditionnel.",
         MAIL, [Z[4]],
         "'Pourriez-vous …?' is de conditionnel van pouvoir: zo maak je een vraag beleefd."),
    klik("Klik op de zin waarin Emma zegt wat ze wil doen.",
         MAIL, [Z[3]],
         "'Je voudrais travailler comme bénévole': Emma wil vrijwilliger worden in de bibliotheek."),
    met_prent(MAIL, mk(
        "Waarom begint Emma met 'Madame, Monsieur,'?",
        ["Ze kent de naam van de ontvanger niet.", "Ze schrijft een informele mail aan een vriend.", "Zo begin je elke Franse mail, ook aan vrienden.", "Ze schrijft aan twee mensen die ze goed kent."],
        0,
        "In een formele mail aan iemand van wie je de naam niet kent, begin je met 'Madame, Monsieur,'.")),
    met_prent(MAIL, keuze(
        "Emma gebruikt in de hele mail de [[*vous|tu]]-vorm, omdat de mail [[*formeel|informeel]] is.",
        "In een formele Franse mail hou je de vous-vorm aan, ook in de werkwoorden.")),

    # Présent en impératif
    tabel(
        "Is deze présentvorm juist?",
        [
            ("vous faites", J),
            ("vous disez", F),
            ("ils vont", J),
            ("nous mangons", F),
        ],
        "Faire en dire krijgen bij vous -tes: vous faites, vous dites. Bij manger blijft de e voor -ons: nous mangeons."),
    inv("Zet in de bevelende vorm voor vous: (venir) avec moi ! Eén woord.",
        ["venez", "Venez"],
        "De impératif voor vous is de présentvorm zonder vous: venez."),
    keuze(
        "Je vais partir betekent [[*ik ga zo meteen vertrekken|ik ben net vertrokken]]. Je viens de manger betekent [[*ik heb net gegeten|ik ga eten]].",
        "Aller + infinitief is de futur proche. Venir de + infinitief is de passé récent."),

    # Passé composé
    sorteer(
        "Welk hulpwerkwoord krijgt dit werkwoord in de passé composé?",
        ["avoir", "être"],
        [
            ["manger", "avoir"],
            ["aller", "être"],
            ["finir", "avoir"],
            ["arriver", "être"],
            ["prendre", "avoir"],
            ["partir", "être"],
        ],
        "Werkwoorden van beweging en verandering zoals aller, arriver en partir nemen être. De meeste andere nemen avoir."),
    tabel(
        "Klopt het voltooid deelwoord?",
        [
            ("prendre → pris", J),
            ("faire → fait", J),
            ("venir → venu", J),
            ("voir → voyé", F),
        ],
        "Voir is onregelmatig: vu. Prendre, faire en venir hebben ook onregelmatige deelwoorden: pris, fait, venu."),
    keuze(
        "Elles sont [[*parties|parti|partis]] à huit heures. Hier, nous [[*avons|sommes]] mangé au restaurant.",
        "Bij être past het deelwoord zich aan het onderwerp aan: elles → parties. Manger neemt avoir."),

    # Futur en conditionnel
    inv("Zet in de futur simple: demain, nous (finir) le travail. Eén werkwoordsvorm.",
        ["finirons"],
        "Futur simple = infinitief + uitgang. Finir + -ons = finirons."),
    keuze(
        "Si tu travailles bien, tu [[*réussiras|réussirais|réussis]] ton examen. Pour être beleefd zeg je: je [[*voudrais|veux]] un café, s'il vous plaît.",
        "Een si-zin over een echte mogelijkheid: si + présent, futur in de hoofdzin. De conditionnel maakt een vraag beleefder."),
    mk("Welke zin heeft terecht een subjonctif?",
       ["Il faut que tu viennes demain.", "Je pense que tu viens demain.", "Je sais que tu viens demain.", "Il dit que tu viens demain matin."],
       0,
       "Na 'il faut que' volgt de subjonctif. Na 'je pense que', 'je sais que' en 'il dit que' staat de indicatif."),

    # Voornaamwoorden
    koppel(
        "Koppel de zin aan de juiste vervanging.",
        [
            ["Je vois Paul.", "Je le vois."],
            ["Je téléphone à mes parents.", "Je leur téléphone."],
            ["Je vais à Paris.", "J'y vais."],
            ["Je mange des pommes.", "J'en mange."],
        ],
        [],
        "Le vervangt een lijdend voorwerp, leur een meewerkend voorwerp in het meervoud, y een plaats met à en en een hoeveelheid met de/des."),
    keuze(
        "Le livre [[*que|qui]] je lis est passionnant. La fille [[*qui|que]] chante est ma sœur. La ville [[*où|que]] j'habite est petite.",
        "Que is lijdend voorwerp, qui is onderwerp, où verwijst naar een plaats."),
    inv("Vul de tonische vorm in: c'est pour … , het is voor hem. Eén woord.",
        ["lui"],
        "Na een voorzetsel gebruik je de tonische vorm: moi, toi, lui, elle, nous, vous, eux, elles."),

    # Lidwoorden en determinanten
    keuze(
        "Je mange du pain. Ontkennend: je ne mange pas [[*de|du]] pain. J'achète [[*des|les]] pommes au marché (een paar appels, niet bepaald).",
        "Na een ontkenning wordt du, de la en des gewoon de. Des is het onbepaald lidwoord in het meervoud."),
    tabel(
        "Welk bezittelijk determinant past?",
        [
            ("Paul cherche … clés.", "ses"),
            ("Nous aimons … école.", "notre"),
            ("Les élèves oublient … cahiers.", "leurs"),
        ],
        "Ses: meerdere dingen van één bezitter. Notre: één ding van ons. Leurs: meerdere dingen van meerdere bezitters.",
        kolommen=["ses", "notre", "leurs"]),

    # Bijvoeglijk en bijwoord
    tabel(
        "Is de vrouwelijke vorm juist?",
        [
            ("grand → grande", J),
            ("sportif → sportive", J),
            ("beau → beaue", F),
            ("heureux → heureuse", J),
        ],
        "Beau wordt belle. -if wordt -ive, -eux wordt -euse."),
    keuze(
        "Elle chante [[*bien|bon]]. C'est le [[*meilleur|plus bon]] restaurant de la ville. Rapide wordt als bijwoord [[*rapidement|rapide]].",
        "Bien is het bijwoord bij bon. De vergrotende trap van bon is meilleur. Een bijwoord maak je meestal met -ment."),

    inv("Zet in de imparfait: quand j'étais petit, nous (avoir) un chien. Eén werkwoordsvorm.",
        ["avions"],
        "De imparfait vertrekt van de stam van nous in de présent (av-ons) + -ions: nous avions."),
    mk("Je botst per ongeluk tegen iemand op in de metro. Wat zeg je?",
       ["Oh, je suis désolé !", "Je vous prie d'agréer mes salutations.", "Bon appétit et bonne journée !", "Je voudrais un café, s'il vous plaît."],
       0,
       "Om je te verontschuldigen zeg je bijvoorbeeld 'je suis désolé'."),
    # Getallen, datum, cultuur
    inv("Schrijf het getal 70 voluit zoals men het in België zegt.",
        ["septante"],
        "In België zegt men septante, in Frankrijk soixante-dix."),
    tabel(
        "Klopt dit over de Franstalige wereld?",
        [
            ("Frankrijk viert zijn nationale feestdag op 14 juli.", J),
            ("In Québec betekent 'une fin de semaine' het weekend.", J),
            ("Een Fransman die 'quinze jours' zegt, bedoelt vijftien weken.", F),
            ("In een Franse bakkerij zeg je eerst 'Bonjour'.", J),
        ],
        "Quinze jours betekent twee weken. Begroeten bij het binnenkomen hoort bij de Franse omgangsvormen."),
    mk("Hoe sluit je een formele Franse mail af?",
       ["Je vous prie d'agréer mes salutations distinguées.", "Bisous et à bientôt, ma belle, je t'embrasse fort !", "Salut, à plus tard, mon pote, on s'appelle demain !", "Ciao, on se voit samedi soir au café du coin, hein ?"],
       0,
       "Een formele mail sluit je af met een vaste beleefde formule. De andere afsluiters passen bij vrienden."),

    # Woordenschat
    koppel(
        "Wat betekent dit Franse woord? Koppel.",
        [
            ["une ordonnance", "een voorschrift van de dokter"],
            ["une entrée", "een voorgerecht"],
            ["un car", "een autobus voor lange afstand"],
            ["une matière", "een schoolvak"],
        ],
        ["een personenwagen"],
        "Un car is een bus, geen personenwagen (une voiture)."),
    sleep(
        "Ik ben bang voor spinnen: j'ai [[peur]] des araignées. Ik heb dorst: j'ai [[soif]].",
        ["faim", "froid"],
        "Avoir peur = bang zijn, avoir soif = dorst hebben. Avoir faim = honger hebben, avoir froid = het koud hebben."),
    keuze(
        "Quatorze heures trente is [[*half drie in de namiddag|half twee in de namiddag]]. Il fait [[*froid|chaud]] en hiver.",
        "Quatorze heures = 14 uur, trente = dertig minuten: 14.30. In de winter is het koud."),

    # Tekstverbanden en tekstsoorten
    sorteer(
        "Sorteer deze Franse signaalwoorden volgens het verband dat ze leggen.",
        ["Tegenstelling", "Oorzaak", "Gevolg"],
        [
            ["mais", "Tegenstelling"],
            ["parce que", "Oorzaak"],
            ["donc", "Gevolg"],
            ["cependant", "Tegenstelling"],
            ["à cause de", "Oorzaak"],
        ],
        "Mais en cependant: tegenstelling. Parce que en à cause de: oorzaak. Donc: gevolg."),
    volgorde(
        "Zet de signaalwoorden van een recept in de juiste volgorde.",
        ["d'abord", "ensuite", "puis", "enfin"],
        "D'abord = eerst, ensuite en puis = daarna, enfin = ten slotte."),
    mk("'Épluchez quatre pommes de terre et coupez-les en morceaux.' Welke tekstsoort is dit?",
       ["prescriptief", "verhalend", "opiniërend", "literair en poëtisch"],
       0,
       "Een recept geeft instructies in de impératif: het is een prescriptieve tekst."),

    # Zinnen
    keuze(
        "Il ne voit [[*personne|pas personne]]. Een vraag met omkering van 'tu viens' is [[*viens-tu|tu-viens]] ?",
        "Je zegt ne … personne, zonder pas. Bij omkering komt het werkwoord voor het onderwerp, met een streepje."),
    volgorde(
        "Zet de woorden in de juiste volgorde.",
        ["Je", "ne", "le", "lui", "donne", "pas."],
        "Ne komt na het onderwerp, dan de voornaamwoorden (le voor lui), dan het werkwoord en pas."),
    keuze(
        "Ils voyagent [[*au|en]] Portugal et [[*en|au]] France.",
        "Voor een mannelijk land gebruik je au (au Portugal), voor een vrouwelijk land en (en France)."),

    # Schrijfopdracht
    open_("Schrijf een korte mail van 60 à 80 woorden aan een Franse vriend. Vertel wat je vorig weekend deed en vraag of hij volgende zaterdag mee naar de film gaat.",
          "Salut Lucas,\nMerci pour ton message ! Le week-end dernier, je suis allé à la mer avec ma famille. Il faisait froid, mais nous avons fait une longue promenade sur la plage. Le soir, nous avons mangé des frites. Samedi prochain, je vais au cinéma. Tu veux venir avec moi ? Le film commence à quinze heures.\nÀ bientôt,\nThomas",
          "Een goed antwoord heeft een aanspreking en afsluiter, gebruikt de passé composé en de imparfait voor het weekend, stelt een duidelijke vraag en blijft binnen het aantal woorden."),
]
