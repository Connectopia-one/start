# -*- coding: utf-8 -*-
"""Uitdaging Frans 🌍 Beyond doorstroom (25 november 2026), in de vormen van
het examen van de Examencommissie: 40 vragen die alle hoofdstukken door
elkaar halen. Een zelf geschreven opiniestuk en een sollicitatiebrief om op te
klikken, tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde en een
korte schrijfopdracht. Geen nieuwe leerstof: alles staat in de hoofdstukken
van Frans Beyond doorstroom.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_frans.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Frans"
BESTAND = "beyond-frans-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/frans-beyond-uitdaging"
ARTIKEL = "artikel-voitures.svg"
LETTRE = "lettre-stage.svg"


def zin(i, n=6):
    """Klikvak van zin i (vanaf 1), zie uitdaging/_blad.py."""
    h = 90 + n * 92 + 30
    return [2, round((90 + (i - 1) * 92) / h * 100, 1), 96, round(92 / h * 100, 1)]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Opiniestuk (prent)
    klik("Lees de Franse tekst. Klik op de zin waarin de schrijver zijn persoonlijke mening geeft.",
         ARTIKEL, [zin(5)],
         "'À mon avis' betekent volgens mij. De andere zinnen geven feiten, een voorbeeld of wat anderen vrezen."),
    klik("Klik op de Franse zin die begint met een woord dat een tegenstelling aankondigt.",
         ARTIKEL, [zin(3)],
         "'Pourtant' betekent toch of nochtans. Het zet de vrees van de handelaars tegenover wat er echt gebeurt."),
    klik("Klik op de zin die een concreet voorbeeld geeft.",
         ARTIKEL, [zin(4)],
         "'Par exemple' kondigt een voorbeeld aan: in Gent is de lucht sinds 2017 zuiverder."),
    met_prent(ARTIKEL, tabel(
        "Welke functie heeft het Franse signaalwoord in de tekst?",
        [
            ("Pourtant (zin 3)", "Tegenstelling"),
            ("Par exemple (zin 4)", "Voorbeeld"),
            ("Bref (zin 6)", "Samenvatting of besluit"),
        ],
        "Pourtant brengt een tegenstelling, par exemple een voorbeeld en bref vat samen: kortom.",
        kolommen=["Tegenstelling", "Voorbeeld", "Samenvatting of besluit"])),
    met_prent(ARTIKEL, mk(
        "Wat vrezen de handelaars volgens zin 2?",
        ["Dat ze klanten zullen verliezen.", "Dat de lucht in de stad vuiler wordt.", "Dat er te veel wandelaars komen kijken.", "Dat ze hun winkel moeten verhuizen."],
        0,
        "'Craindre de perdre des clients' betekent vrezen klanten te verliezen.")),

    # Sollicitatiebrief (prent)
    klik("Lees de brief. Klik op de zin die niet past in een formele brief.",
         LETTRE, [zin(4)],
         "'Salut', 'trop cool' en 'bosser' zijn spreektaal. In een sollicitatiebrief blijf je beleefd en zakelijk."),
    klik("Klik op de beleefde slotformule van de brief.",
         LETTRE, [zin(6)],
         "'Veuillez agréer ... mes salutations distinguées' is de vaste formele afsluiting van een Franse brief."),
    met_prent(LETTRE, tabel(
        "Klopt dit over de brief van de kandidate?",
        [
            ("Zin 2 zegt meteen waarom ze schrijft.", J),
            ("De schrijfster is een vrouw: dat zie je aan 'reconnaissante'.", J),
            ("Ze heeft nog nooit in de horeca gewerkt.", F),
            ("Ze vraagt in zin 5 om meteen te mogen beginnen.", F),
        ],
        "Reconnaissante staat in de vrouwelijke vorm. In zin 3 vertelt ze over twee zomers in een restaurant, en in zin 5 vraagt ze een gesprek (un entretien), geen startdatum.")),
    met_prent(LETTRE, keuze(
        "In zin 3 staat het werkwoord in de [[*passé composé|imparfait|plus-que-parfait]]. Zin 5 gebruikt de [[*conditionnel|futur simple|subjonctif]] om beleefd te vragen.",
        "J'ai travaillé is een passé composé: avoir + participe passé. Je serais is de conditionnel van être, de beleefde vorm.")),

    # Tekstsoorten en omgangsvormen
    sorteer(
        "Tot welk soort tekst behoort elk Frans fragment?",
        ["Informatief", "Prescriptief", "Persuasief"],
        [
            ["Mélangez la farine et les œufs.", "Prescriptief"],
            ["La tour Eiffel mesure 330 mètres.", "Informatief"],
            ["Venez nombreux : c'est gratuit !", "Persuasief"],
            ["Ne pas se pencher au dehors.", "Prescriptief"],
            ["Le musée ouvre à 9 heures.", "Informatief"],
            ["Achetez local, sauvez la planète !", "Persuasief"],
        ],
        "Instructies en verboden zijn prescriptief, feiten informatief, en een tekst die je tot iets wil aanzetten is persuasief."),
    tabel(
        "Spreek je deze persoon aan met tu of met vous?",
        [
            ("De directeur van een hotel waar je solliciteert", "vous"),
            ("Je beste vriendin", "tu"),
            ("Een onbekende voorbijganger op straat", "vous"),
            ("Je jongere broer", "tu"),
        ],
        "Vous is de beleefde vorm voor onbekenden en mensen met wie je formeel omgaat. Tu gebruik je voor familie en vrienden.",
        kolommen=["tu", "vous"]),
    mk("In Frankrijk begroet je een vriendin. Wat doe je meestal?",
       ["Je geeft haar een paar kussen op de wangen: la bise.", "Je geeft haar een stevige hand zonder iets te zeggen.", "Je buigt licht het hoofd en houdt afstand van haar.", "Je zwaait van ver en roept enkel 'Bonsoir madame'."],
       0,
       "Faire la bise, kusjes op de wangen, is in Frankrijk de gewone begroeting onder vrienden. Het aantal kussen verschilt per streek."),

    # Literatuur
    tabel(
        "Welke literaire term past bij de omschrijving?",
        [
            ("Het personage dat het verhaal vertelt met 'je'", "un narrateur"),
            ("Een gedicht van veertien regels", "un sonnet"),
            ("Een vergelijking met 'comme'", "une comparaison"),
        ],
        "De verteller heet le narrateur, een sonnet heeft veertien versregels, en een comparaison gebruikt comme.",
        kolommen=["un narrateur", "un sonnet", "une comparaison"]),

    # Woordenschat
    koppel(
        "Koppel het Franse woord aan de juiste vertaling.",
        [
            ["un médecin", "een dokter"],
            ["le loyer", "de huurprijs"],
            ["un horaire", "een dienstregeling"],
            ["un embouteillage", "een file"],
            ["un salaire", "een loon"],
        ],
        ["een bord", "een uurwerk"],
        "Let op: un horaire is een uurrooster of dienstregeling, geen uurwerk (une montre)."),
    sorteer(
        "In welk Frans woordveld past dit woord?",
        ["Gezondheid", "Wonen", "Werk"],
        [
            ["une ordonnance", "Gezondheid"],
            ["le grenier", "Wonen"],
            ["un entretien d'embauche", "Werk"],
            ["une piqûre", "Gezondheid"],
            ["la cave", "Wonen"],
            ["le chômage", "Werk"],
        ],
        "Een voorschrift en een prik horen bij de dokter, een zolder en een kelder bij het huis, een sollicitatiegesprek en werkloosheid bij werk."),
    inv("Hoe zeg je 'het station' in het Frans? Met lidwoord.",
        ["la gare"],
        "La gare is het treinstation. Le métro en l'arrêt de bus zijn andere woorden."),
    keuze(
        "Je vais à la [[*boulangerie|boucherie|librairie]] pour acheter du pain. J'achète des livres à la [[*librairie|bibliothèque|boulangerie]].",
        "Brood koop je in een boulangerie. Een librairie is een boekenwinkel; in een bibliothèque leen je boeken."),

    # Lidwoorden en determinanten
    keuze(
        "Je bois [[*du|de la|des]] lait. Je ne bois pas [[*de|du|le]] café. Il y a beaucoup [[*de|des]] touristes.",
        "Het delend lidwoord du staat voor een onbepaalde hoeveelheid. Na een ontkenning en na beaucoup wordt het de."),
    tabel(
        "Wat is het Franse meervoud?",
        [
            ("un journal", "des journaux"),
            ("un œil", "des yeux"),
            ("un bijou", "des bijoux"),
            ("un travail", "des travaux"),
        ],
        "Woorden op -al en sommige op -ail krijgen -aux, bijou neemt een -x, en œil wordt yeux.",
        kolommen=["des journaux", "des yeux", "des bijoux", "des travaux"]),

    # Voornaamwoorden
    tabel(
        "Welk voornaamwoord vervangt het onderlijnde deel?",
        [
            ("Je téléphone à ma tante. → Je ___ téléphone.", "lui"),
            ("Tu vas à Paris ? → Tu ___ vas ?", "y"),
            ("Elle mange des pommes. → Elle ___ mange.", "en"),
            ("Il regarde le film. → Il ___ regarde.", "le"),
        ],
        "Lui vervangt à + persoon (COI), y een plaats met à, en een hoeveelheid met de, en le een lijdend voorwerp (COD).",
        kolommen=["le", "lui", "y", "en"]),
    mk("Welke Franse zin met twee voornaamwoorden is juist?",
       ["Je le lui ai donné hier.", "Je lui le ai bien donné hier.", "Je l'ai lui donné hier.", "Je lui l'ai donné hier."],
       0,
       "Twee voornaamwoorden samen: le, la, les komen vóór lui en leur. Le wordt niet afgekort voor een medeklinker."),
    keuze(
        "C'est le livre [[*dont|que|qui]] je t'ai parlé. La fille [[*qui|que|dont]] chante est ma sœur.",
        "Dont vervangt de + iets (parler de). Qui is onderwerp van de bijzin."),

    # Bijvoeglijke naamwoorden en bijwoorden
    keuze(
        "Elle a acheté une [[*belle|beau|bel]] robe et un [[*vieil|vieux|vieille]] ordinateur.",
        "Belle is de vrouwelijke vorm. Voor een mannelijk woord met een klinker wordt vieux vieil."),
    tabel(
        "Wat is het bijwoord?",
        [
            ("lent", "lentement"),
            ("vrai", "vraiment"),
            ("évident", "évidemment"),
            ("bon", "bien"),
        ],
        "Meestal vrouwelijke vorm + -ment; na een klinker de mannelijke vorm. Op -ent wordt -emment. Bon is onregelmatig: bien.",
        kolommen=["lentement", "vraiment", "évidemment", "bien"]),
    mk("Hoe zeg je: 'Dit is de beste film van het jaar'?",
       ["C'est le meilleur film de l'année.", "C'est le plus bon film de l'année.", "C'est le mieux film de toute l'année.", "C'est le meilleur film dans l'année."],
       0,
       "Bon heeft een onregelmatige overtreffende trap: le meilleur. Na de overtreffende trap volgt de, niet dans."),

    # Verleden tijden
    keuze(
        "Quand j'[[*étais|ai été]] petit, je [[*jouais|ai joué]] souvent au foot. Un jour, je [[*suis tombé|tombais]] et je me suis cassé le bras.",
        "Een beschrijving of gewoonte in het verleden staat in de imparfait. Een eenmalige gebeurtenis staat in de passé composé."),
    tabel(
        "Met welk hulpwerkwoord vorm je de passé composé?",
        [
            ("aller", "être"),
            ("manger", "avoir"),
            ("se lever", "être"),
            ("venir", "être"),
            ("finir", "avoir"),
        ],
        "Werkwoorden van beweging zoals aller en venir, en alle wederkerende werkwoorden nemen être. De meeste andere nemen avoir.",
        kolommen=["avoir", "être"]),
    inv("Vul het juiste deelwoord in: « Les fleurs ? Je les ai ___ (acheter) au marché. »",
        ["achetées"],
        "Bij avoir regelt het deelwoord zich naar een COD dat ervoor staat: les = les fleurs, vrouwelijk meervoud, dus achetées."),
    mk("In welke zin staat het deelwoord juist?",
       ["Elles sont parties tôt ce matin.", "Elles sont parti tôt ce matin.", "Elles ont parties très tôt ce matin.", "Elles sont partis très tôt ce matin."],
       0,
       "Partir neemt être, en dan regelt het deelwoord zich naar het onderwerp: elles, vrouwelijk meervoud, dus parties."),

    # Futur, conditionnel, subjonctif, gérondif
    tabel(
        "Welke tijd of wijs zie je?",
        [
            ("Demain, nous irons à la mer.", "Futur simple"),
            ("Je voudrais un café, s'il vous plaît.", "Conditionnel"),
            ("Il faut que tu viennes.", "Subjonctif"),
            ("Il écoute de la musique en travaillant.", "Gérondif"),
        ],
        "Irons is de futur van aller, voudrais de conditionnel van vouloir, viennes de subjonctif na il faut que, en + -ant is de gérondif.",
        kolommen=["Futur simple", "Conditionnel", "Subjonctif", "Gérondif"]),
    sleep(
        "Si j'[[avais]] le temps, je [[voyagerais]] plus. Si tu viens demain, nous [[irons]] au cinéma.",
        ["aurai", "voyagerai", "irions"],
        "Een onwaarschijnlijke situatie: si + imparfait, conditionnel. Een reële mogelijkheid: si + présent, futur."),
    keuze(
        "Je veux que tu [[*fasses|fais|feras]] tes devoirs. Bien qu'il [[*soit|est|sera]] malade, il travaille.",
        "Na vouloir que en na bien que volgt de subjonctif: fasses, soit."),
    inv("Zet in de gérondif: « Il chante pendant qu'il prend sa douche. » → Il chante ___ sa douche. Twee woorden.",
        ["en prenant"],
        "Gérondif = en + stam van nous-vorm (pren-ons) + -ant: en prenant."),

    # Zinsbouw, indirecte rede, passief
    volgorde(
        "Zet de Franse woorden in de juiste volgorde.",
        ["Je", "ne", "l'ai", "jamais", "vu", "à Bruxelles"],
        "Bij de passé composé staat ne vóór het hulpwerkwoord, jamais erna, en het voornaamwoord vóór het hulpwerkwoord."),
    tabel(
        "Hoe zet je deze zin in de indirecte rede?",
        [
            ("Il dit : « Je suis fatigué. »", "Il dit qu'il est fatigué."),
            ("Il a dit : « Je viendrai. »", "Il a dit qu'il viendrait."),
            ("Elle demande : « Tu as faim ? »", "Elle demande si j'ai faim."),
        ],
        "Na een hoofdwerkwoord in de verleden tijd schuift de futur naar de conditionnel. Een ja-neevraag wordt ingeleid met si.",
        kolommen=["Il dit qu'il est fatigué.", "Il a dit qu'il viendrait.", "Elle demande si j'ai faim."]),
    mk("Welke Franse zin staat in de passieve vorm?",
       ["La lettre a été écrite par Marie.", "Marie a écrit une lettre hier soir.", "Marie écrivait une lettre chaque soir.", "Marie va écrire une lettre ce soir."],
       0,
       "De passieve zin heeft être + participe passé en vaak par + wie het doet."),
    inv("Zet in de passieve vorm: « Le chat mange la souris. » Begin met « La souris ».",
        ["La souris est mangée par le chat.", "La souris est mangée par le chat", "la souris est mangée par le chat.", "la souris est mangée par le chat"],
        "Passief in de présent: être in de présent + participe passé dat zich naar het onderwerp regelt (mangée), en par le chat."),
    mk("Welke vraag is juist gevormd en formeel?",
       ["Où habitez-vous ?", "Où vous habitez-vous ?", "Où est-ce vous habitez ?", "Où habitez vous-même ?"],
       0,
       "Bij inversie wisselen onderwerp en werkwoord van plaats en komt er een koppelteken tussen: habitez-vous."),

    tabel(
        "Welke negatie past bij de betekenis?",
        [
            ("Ik zie niemand. → Je ne vois ___.", "personne"),
            ("Ik eet niets meer. → Je ne mange ___.", "plus rien"),
            ("Ik ben er nooit geweest. → Je n'y suis ___ allé.", "jamais"),
        ],
        "Ne ... personne is niemand, ne ... plus rien is niets meer, ne ... jamais is nooit.",
        kolommen=["personne", "plus rien", "jamais"]),

    # Schrijfopdracht
    open_("Écris un court e-mail formel (5 à 7 phrases) à un camping en France. Tu veux réserver un emplacement pour une tente pour trois nuits en août et tu demandes s'il y a une piscine. Utilise une formule d'appel et une formule de politesse correctes.",
          "Madame, Monsieur, Je voudrais réserver un emplacement pour une tente du 5 au 8 août. Nous sommes deux adultes et un enfant. Pourriez-vous me dire s'il y a une piscine dans le camping ? Je vous remercie d'avance pour votre réponse. Veuillez agréer, Madame, Monsieur, mes salutations distinguées. Lies Janssens",
          "Een goed antwoord heeft een formele aanspreking (Madame, Monsieur) en slotformule, zegt meteen waarom je schrijft, gebruikt vous en een beleefde vraag (Pourriez-vous ...) en geen spreektaal."),
]
