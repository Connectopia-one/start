# -*- coding: utf-8 -*-
"""Wisselende woorden bij de taalvakken van 🌱 Start.

    python3 start/bron/varianten_start.py

Kim, 30 september 2026: "kunnen we de spelling van de taalvakken dan niet
eerst aanpassen? dat dit overal is?" Tot dan stonden de wisselende woorden
alleen bij het gratis spellinghoofdstuk van Nederlands 🌱 Start en bij de twee
spellinghoofdstukken van Nederlands ✨ Spark.

Wat hier wel en niet in staat. Een vraag krijgt wisselende woorden als de
leerstof in de **regel** zit en niet in het woord: welk woord is een werkwoord,
welke vorm hoort bij nous, wat is het meervoud van. Dan toetst elk woord
precies hetzelfde. Een vraag over een begrip of een uitdrukking (wat is een
lidwoord, wat betekent 'de kat uit de boom kijken') krijgt er geen: daar valt
niets te wisselen zonder dat de vraag een andere vraag wordt.

Alles met de hand geschreven en nagelezen, nooit door een taalmodel bedacht:
de welkomstbrief aan de testgezinnen belooft uitdrukkelijk geen AI in de
oefeningen.

De eerste beurt is de vraag zelf; de lijstjes hieronder zijn beurt twee en
verder. Een variant noemt alleen wat verandert; de rest komt van de vraag.
Zie lib/spellingvariant.ts.
"""
import json
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
NIVEAU = HIER.parent

VARIANTEN = {}

# ═════════════════════════════════ Nederlands — Taalsysteem en taalgebruik

VARIANTEN[("nederlands.json", "Taalsysteem en taalgebruik")] = {
    "Welk woord is een werkwoord?": [
        dict(opties=["schrift", "rekenen", "stil", "groot"], antwoord=1,
             uitleg="Rekenen zegt wat iemand doet. Stil en groot zeggen hoe iets is, een schrift is een ding."),
        dict(opties=["vogel", "fluiten", "klein", "nat"], antwoord=1,
             uitleg="Fluiten zegt wat iemand doet. Klein en nat zeggen hoe iets is, een vogel is een dier."),
        dict(opties=["deur", "poetsen", "warm", "zacht"], antwoord=1,
             uitleg="Poetsen zegt wat iemand doet. Warm en zacht zeggen hoe iets is, een deur is een ding."),
    ],
    "Wat is het onderwerp in de zin 'De hond blaft luid.'?": [
        dict(vraag="Wat is het onderwerp in de zin 'De juf schrijft op het bord.'?",
             opties=["De juf", "schrijft", "op het bord", "schrijft op"], antwoord=0,
             uitleg="Het onderwerp is wie of wat het werkwoord doet: wie schrijft er? De juf."),
        dict(vraag="Wat is het onderwerp in de zin 'Een merel bouwt een nest.'?",
             opties=["Een merel", "bouwt", "een nest", "bouwt een"], antwoord=0,
             uitleg="Wie bouwt er? Een merel. Dat is het onderwerp."),
        dict(vraag="Wat is het onderwerp in de zin 'Mijn zus kookt soep.'?",
             opties=["Mijn zus", "kookt", "soep", "kookt soep"], antwoord=0,
             uitleg="Wie kookt er? Mijn zus. Dat is het onderwerp."),
    ],
    "Welk woord is een bijvoeglijk naamwoord?": [
        dict(opties=["boek", "moeilijk", "leren", "ik"], antwoord=1,
             uitleg="Moeilijk zegt iets over een zelfstandig naamwoord: een moeilijk boek."),
        dict(opties=["rivier", "diep", "zwemmen", "het"], antwoord=1,
             uitleg="Diep zegt iets over een zelfstandig naamwoord: een diepe rivier."),
        dict(opties=["kast", "wiebelig", "zitten", "jullie"], antwoord=1,
             uitleg="Wiebelig zegt iets over een zelfstandig naamwoord: een wiebelige kast."),
    ],
    "'Wij' is een persoonlijk voornaamwoord.": [
        dict(vraag="'Jullie' is een persoonlijk voornaamwoord.", antwoord=True,
             uitleg="Ik, jij, hij, zij, wij, jullie en zij zijn persoonlijke voornaamwoorden."),
        dict(vraag="'Groen' is een persoonlijk voornaamwoord.", antwoord=False,
             uitleg="Niet juist. Groen is een bijvoeglijk naamwoord. Ik, jij, hij, zij, wij en jullie zijn persoonlijke voornaamwoorden."),
        dict(vraag="'Zij' is een persoonlijk voornaamwoord.", antwoord=True,
             uitleg="Zij hoort in het rijtje ik, jij, hij, zij, wij, jullie, zij."),
    ],
    "Wat is het gezegde in de zin 'Mats leest een boek.'?": [
        dict(vraag="Wat is het gezegde in de zin 'Lore tekent een huis.'?",
             opties=["Lore", "tekent", "een huis", "huis"], antwoord=1,
             uitleg="Het gezegde is het werkwoord: tekent."),
        dict(vraag="Wat is het gezegde in de zin 'De koe eet gras.'?",
             opties=["De koe", "eet", "gras", "de"], antwoord=1,
             uitleg="Het gezegde is het werkwoord: eet."),
        dict(vraag="Wat is het gezegde in de zin 'Papa wast de auto.'?",
             opties=["Papa", "wast", "de auto", "auto"], antwoord=1,
             uitleg="Het gezegde is het werkwoord: wast."),
    ],
    "Hoeveel lettergrepen heeft het woord vakantie?": [
        dict(vraag="Hoeveel lettergrepen heeft het woord banaan?", antwoord="2",
             uitleg="Ba-naan, dus twee lettergrepen."),
        dict(vraag="Hoeveel lettergrepen heeft het woord olifant?", antwoord="3",
             uitleg="O-li-fant, dus drie lettergrepen."),
        dict(vraag="Hoeveel lettergrepen heeft het woord tomaat?", antwoord="2",
             uitleg="To-maat, dus twee lettergrepen."),
    ],
    "Welk woord is een samenstelling?": [
        dict(opties=["kast", "voetbal", "zwemmen", "blauw"], antwoord=1,
             uitleg="Voet en bal zijn allebei bestaande woorden. Samen vormen ze voetbal."),
        dict(opties=["appel", "zonnebril", "rennen", "koud"], antwoord=1,
             uitleg="Zon en bril zijn allebei bestaande woorden. Samen vormen ze zonnebril."),
        dict(opties=["raam", "tandenborstel", "kijken", "zwaar"], antwoord=1,
             uitleg="Tanden en borstel zijn allebei bestaande woorden. Samen vormen ze tandenborstel."),
    ],
    "Welke zin is een vraagzin?": [
        dict(opties=["De zon schijnt.", "Wil je een koekje?", "Doe de deur dicht.", "Wat een lawaai!"], antwoord=1,
             uitleg="In een vraagzin staat het werkwoord vooraan en eindigt de zin op een vraagteken."),
        dict(opties=["Ik lees een boek.", "Waar woon jij?", "Kom binnen.", "Wat mooi!"], antwoord=1,
             uitleg="Waar woon jij? begint met een vraagwoord en eindigt op een vraagteken."),
        dict(opties=["We gaan zwemmen.", "Heb je mijn jas gezien?", "Zet dat weg.", "Wat een geluk!"], antwoord=1,
             uitleg="Heb staat vooraan en de zin eindigt op een vraagteken, dus is het een vraagzin."),
    ],
    "Welk woord is een zelfstandig naamwoord?": [
        dict(opties=["blij", "fietsen", "stoel", "erg"], antwoord=2,
             uitleg="Een stoel is een ding, dus een zelfstandig naamwoord."),
        dict(opties=["hoog", "springen", "brug", "vaak"], antwoord=2,
             uitleg="Een brug is een ding, dus een zelfstandig naamwoord."),
        dict(opties=["stil", "werken", "brood", "nooit"], antwoord=2,
             uitleg="Brood is een ding, dus een zelfstandig naamwoord."),
    ],
    "Wat is het lijdend voorwerp in 'Ik eet een appel.'?": [
        dict(vraag="Wat is het lijdend voorwerp in 'Zij drinkt melk.'?",
             opties=["Zij", "drinkt", "melk", "drinkt melk"], antwoord=2,
             uitleg="Vraag: wat drinkt zij? Melk."),
        dict(vraag="Wat is het lijdend voorwerp in 'Wij kopen bloemen.'?",
             opties=["Wij", "kopen", "bloemen", "kopen bloemen"], antwoord=2,
             uitleg="Vraag: wat kopen wij? Bloemen."),
        dict(vraag="Wat is het lijdend voorwerp in 'Hij schrijft een brief.'?",
             opties=["Hij", "schrijft", "een brief", "schrijft een"], antwoord=2,
             uitleg="Vraag: wat schrijft hij? Een brief."),
    ],
    "Welk woord is een voorzetsel?": [
        dict(opties=["naast", "zingen", "muur", "klein"], antwoord=0,
             uitleg="Naast, op, in, onder en achter geven een plaats of richting aan."),
        dict(opties=["achter", "tekenen", "bos", "snel"], antwoord=0,
             uitleg="Achter, op, in, naast en onder geven een plaats of richting aan."),
        dict(opties=["tussen", "dromen", "trap", "dik"], antwoord=0,
             uitleg="Tussen, op, in, naast en achter geven een plaats of richting aan."),
    ],
    "Hoeveel lettergrepen heeft het woord computer?": [
        dict(vraag="Hoeveel lettergrepen heeft het woord bibliotheek?", antwoord="4",
             uitleg="Bi-bli-o-theek, dus vier lettergrepen."),
        dict(vraag="Hoeveel lettergrepen heeft het woord regen?", antwoord="2",
             uitleg="Re-gen, dus twee lettergrepen."),
        dict(vraag="Hoeveel lettergrepen heeft het woord winkelkar?", antwoord="3",
             uitleg="Win-kel-kar, dus drie lettergrepen."),
    ],
    "Welke zin bevat een verkleinwoord?": [
        dict(opties=["De kat slaapt.", "Het katje slaapt.", "De katten slapen.", "Kat, kom hier."], antwoord=1,
             uitleg="Katje eindigt op -je, en dat is een verkleinwoord."),
        dict(opties=["De boom valt.", "Het boompje valt.", "De bomen vallen.", "Boom, pas op."], antwoord=1,
             uitleg="Boompje eindigt op -pje, en dat is een verkleinwoord."),
        dict(opties=["De man lacht.", "Het mannetje lacht.", "De mannen lachen.", "Man, kijk uit."], antwoord=1,
             uitleg="Mannetje eindigt op -tje, en dat is een verkleinwoord."),
    ],
    "Het woord snelheid is een samenstelling van twee woorden.": [
        dict(vraag="Het woord vriendschap is een samenstelling van twee woorden.", antwoord=False,
             uitleg="Niet juist. Vriendschap is een afleiding: vriend plus de uitgang -schap. Bij een samenstelling plak je twee bestaande woorden aan elkaar, zoals tandpasta."),
        dict(vraag="Het woord tafelpoot is een samenstelling van twee woorden.", antwoord=True,
             uitleg="Klopt. Tafel en poot bestaan allebei op zichzelf."),
        dict(vraag="Het woord blijheid is een samenstelling van twee woorden.", antwoord=False,
             uitleg="Niet juist. Blijheid is een afleiding: blij plus de uitgang -heid."),
    ],
    "Welk woord hoort niet in het rijtje: fiets, auto, trein, boom?": [
        dict(vraag="Welk woord hoort niet in het rijtje: appel, peer, banaan, kruk?",
             opties=["appel", "peer", "banaan", "kruk"], antwoord=3,
             uitleg="De eerste drie zijn fruit, een kruk niet."),
        dict(vraag="Welk woord hoort niet in het rijtje: hond, kat, konijn, tafel?",
             opties=["hond", "kat", "konijn", "tafel"], antwoord=3,
             uitleg="De eerste drie zijn dieren, een tafel niet."),
        dict(vraag="Welk woord hoort niet in het rijtje: rood, blauw, groen, potlood?",
             opties=["rood", "blauw", "groen", "potlood"], antwoord=3,
             uitleg="De eerste drie zijn kleuren, een potlood niet."),
    ],
    "In de zin 'De kat slaapt' staat het werkwoord in het enkelvoud.": [
        dict(vraag="In de zin 'De honden blaffen' staat het werkwoord in het enkelvoud.", antwoord=False,
             uitleg="Niet juist. Er zijn meer honden, dus blaffen en niet blaft. Dat is meervoud."),
        dict(vraag="In de zin 'Het kind speelt' staat het werkwoord in het enkelvoud.", antwoord=True,
             uitleg="Er is één kind, dus speelt en niet spelen."),
        dict(vraag="In de zin 'De kinderen spelen' staat het werkwoord in het enkelvoud.", antwoord=False,
             uitleg="Niet juist. Er zijn meer kinderen, dus spelen en niet speelt. Dat is meervoud."),
    ],
}

# ═══════════════════════════════════════════════ Frans — Être en avoir

VARIANTEN[("frans.json", "Être en avoir")] = {
    'Vul aan: "Tu ... mon ami."': [
        dict(vraag='Vul aan: "Je ... en classe." (ik ben in de klas)',
             opties=["suis", "es", "est", "sont"], antwoord=0,
             uitleg="Bij je hoort suis: je suis en classe, ik ben in de klas."),
        dict(vraag='Vul aan: "Il ... mon frère." (hij is mijn broer)',
             opties=["est", "es", "suis", "êtes"], antwoord=0,
             uitleg="Bij il en elle hoort est: il est mon frère."),
        dict(vraag='Vul aan: "Elles ... à la maison." (zij zijn thuis)',
             opties=["sont", "est", "sommes", "es"], antwoord=0,
             uitleg="Bij ils en elles hoort sont: elles sont à la maison."),
    ],
    'Vul aan: "Elle ... gentille." (zij is lief)': [
        dict(vraag='Vul aan: "Nous ... belges." (wij zijn Belgen)', antwoord="sommes",
             uitleg="Nous sommes belges. Bij nous hoort sommes."),
        dict(vraag='Vul aan: "Vous ... prêts." (jullie zijn klaar)', antwoord="êtes",
             uitleg="Vous êtes prêts. Bij vous hoort êtes, met een dakje op de e."),
        dict(vraag='Vul aan: "Tu ... fatigué." (jij bent moe)', antwoord="es",
             uitleg="Tu es fatigué. Bij tu hoort es, zonder t."),
    ],
    'Welke vorm hoort bij "nous"?': [
        dict(vraag='Welke vorm van être hoort bij "vous"?',
             opties=["sommes", "êtes", "sont", "es"], antwoord=1,
             uitleg="Vous êtes: jullie zijn. Nous sommes is wij zijn, ils sont is zij zijn."),
        dict(vraag='Welke vorm van être hoort bij "ils"?',
             opties=["est", "sommes", "sont", "êtes"], antwoord=2,
             uitleg="Ils sont: zij zijn. Il est is hij is."),
        dict(vraag='Welke vorm van être hoort bij "je"?',
             opties=["suis", "es", "est", "sommes"], antwoord=0,
             uitleg="Je suis: ik ben. Tu es is jij bent."),
    ],
    'Vul aan: "Vous ... en retard." (jullie zijn te laat)': [
        dict(vraag='Vul aan: "Nous ... en retard." (wij zijn te laat)',
             opties=["sommes", "êtes", "sont", "suis"], antwoord=0,
             uitleg="Nous sommes en retard. Bij nous hoort sommes."),
        dict(vraag='Vul aan: "Tu ... en retard." (jij bent te laat)',
             opties=["es", "est", "êtes", "sont"], antwoord=0,
             uitleg="Tu es en retard. Bij tu hoort es."),
        dict(vraag='Vul aan: "Ils ... en retard." (zij zijn te laat)',
             opties=["sont", "est", "sommes", "êtes"], antwoord=0,
             uitleg="Ils sont en retard. Bij ils hoort sont."),
    ],
    'Vul aan: "J\'... un chien." (ik heb een hond)': [
        dict(vraag='Vul aan: "Tu ... un vélo." (jij hebt een fiets)', antwoord="as",
             uitleg="Tu as un vélo. Bij tu hoort as, met een s."),
        dict(vraag='Vul aan: "Nous ... un chat." (wij hebben een kat)', antwoord="avons",
             uitleg="Nous avons un chat. Bij nous hoort avons."),
        dict(vraag='Vul aan: "Ils ... une voiture." (zij hebben een auto)', antwoord="ont",
             uitleg="Ils ont une voiture. Pas op: ils sont is zij zijn, ils ont is zij hebben."),
    ],
    'Welke vorm hoort bij "il" of "elle" bij avoir?': [
        dict(vraag='Welke vorm van avoir hoort bij "tu"?',
             opties=["ai", "as", "a", "avez"], antwoord=1,
             uitleg="Tu as: jij hebt. Met een s, want tu krijgt bijna altijd een s."),
        dict(vraag='Welke vorm van avoir hoort bij "vous"?',
             opties=["avons", "avez", "ont", "as"], antwoord=1,
             uitleg="Vous avez: jullie hebben. Nous avons is wij hebben."),
        dict(vraag='Welke vorm van avoir hoort bij "je"?',
             opties=["ai", "as", "a", "avons"], antwoord=0,
             uitleg="J'ai: ik heb. Je en ai worden samen j'ai."),
    ],
    'Vul aan: "Nous ... une grande maison."': [
        dict(vraag='Vul aan: "Vous ... une grande maison."',
             opties=["avons", "avez", "ont", "ai"], antwoord=1,
             uitleg="Vous avez une grande maison: jullie hebben een groot huis."),
        dict(vraag='Vul aan: "Elle ... une grande maison."',
             opties=["a", "as", "ont", "avez"], antwoord=0,
             uitleg="Elle a une grande maison: zij heeft een groot huis."),
        dict(vraag='Vul aan: "Tu ... une grande maison."',
             opties=["as", "avons", "avez", "ont"], antwoord=0,
             uitleg="Tu as une grande maison: jij hebt een groot huis."),
    ],
    'Vul aan: "Ils ... deux chats."': [
        dict(vraag='Vul aan: "Elle ... deux frères."',
             opties=["a", "as", "ont", "avez"], antwoord=0,
             uitleg="Elle a deux frères: zij heeft twee broers."),
        dict(vraag='Vul aan: "Nous ... deux chiens."',
             opties=["avons", "avez", "ont", "a"], antwoord=0,
             uitleg="Nous avons deux chiens: wij hebben twee honden."),
        dict(vraag='Vul aan: "Vous ... deux vélos."',
             opties=["avez", "avons", "ont", "as"], antwoord=0,
             uitleg="Vous avez deux vélos: jullie hebben twee fietsen."),
    ],
    'Welke zin betekent "Zij zijn moe"?': [
        dict(vraag='Welke zin betekent "Wij zijn blij"?',
             opties=["Nous avons contents", "Nous sommes contents", "Nous est contents", "Nous sont contents"],
             antwoord=1, uitleg="Nous sommes contents. Blij zijn is een toestand, dus être."),
        dict(vraag='Welke zin betekent "Jij bent klein"?',
             opties=["Tu as petit", "Tu es petit", "Tu est petit", "Tu sont petit"],
             antwoord=1, uitleg="Tu es petit. Klein zijn is een toestand, dus être."),
        dict(vraag='Welke zin betekent "Hij is ziek"?',
             opties=["Il a malade", "Il est malade", "Il es malade", "Il sont malade"],
             antwoord=1, uitleg="Il est malade. Ziek zijn is een toestand, dus être."),
    ],
    'Hoe zeg je "Ik heb honger"?': [
        dict(vraag='Hoe zeg je "Ik heb dorst"?',
             opties=["Je suis soif", "J'ai soif", "Je suis de soif", "J'ai de soif"], antwoord=1,
             uitleg="J'ai soif. In het Nederlands ben je dorstig, in het Frans héb je dorst."),
        dict(vraag='Hoe zeg je "Ik heb het warm"?',
             opties=["Je suis chaud", "J'ai chaud", "Je suis de chaud", "J'ai le chaud"], antwoord=1,
             uitleg="J'ai chaud. Je suis chaud zou betekenen dat jij zelf warm aanvoelt."),
        dict(vraag='Hoe zeg je "Ik ben twaalf jaar"?',
             opties=["Je suis douze ans", "J'ai douze ans", "Je suis de douze ans", "J'ai de douze ans"], antwoord=1,
             uitleg="J'ai douze ans. Voor je leeftijd gebruikt het Frans avoir: je hébt twaalf jaar."),
    ],
    'Vul aan: "Tu ... raison." (je hebt gelijk)': [
        dict(vraag='Vul aan: "Il ... raison." (hij heeft gelijk)', antwoord="a",
             uitleg="Il a raison. Bij il hoort a, zonder s en zonder accent."),
        dict(vraag='Vul aan: "Nous ... raison." (wij hebben gelijk)', antwoord="avons",
             uitleg="Nous avons raison. Bij nous hoort avons."),
        dict(vraag='Vul aan: "J\'... raison." (ik heb gelijk)', antwoord="ai",
             uitleg="J'ai raison. Je en ai worden samen j'ai."),
    ],
    'Welke zin betekent "Wij hebben drie honden"?': [
        dict(vraag='Welke zin betekent "Zij hebben twee katten"?',
             opties=["Ils sont deux chats", "Ils ont deux chats", "Ils avons deux chats", "Ils avez deux chats"],
             antwoord=1, uitleg="Ils ont deux chats. Met sont zou er staan dat zij twee katten zíjn."),
        dict(vraag='Welke zin betekent "Jullie hebben een grote tuin"?',
             opties=["Vous êtes un grand jardin", "Vous avez un grand jardin", "Vous avons un grand jardin",
                     "Vous ont un grand jardin"],
             antwoord=1, uitleg="Vous avez un grand jardin. Bij vous hoort avez."),
        dict(vraag='Welke zin betekent "Ik heb twee zussen"?',
             opties=["Je suis deux sœurs", "J'ai deux sœurs", "J'as deux sœurs", "J'ont deux sœurs"],
             antwoord=1, uitleg="J'ai deux sœurs. Bij je hoort ai, en samen wordt dat j'ai."),
    ],
    'Vul aan: "Elles ... contentes." (zij zijn blij)': [
        dict(vraag='Vul aan: "Il ... content." (hij is blij)',
             opties=["a", "est", "ont", "es"], antwoord=1,
             uitleg="Il est content. Blij zijn is een toestand, dus être."),
        dict(vraag='Vul aan: "Nous ... contents." (wij zijn blij)',
             opties=["avons", "sommes", "ont", "êtes"], antwoord=1,
             uitleg="Nous sommes contents. Blij zijn is een toestand, dus être."),
        dict(vraag='Vul aan: "Tu ... content." (jij bent blij)',
             opties=["as", "es", "est", "sont"], antwoord=1,
             uitleg="Tu es content. Blij zijn is een toestand, dus être."),
    ],
}

# ═════════════════════════════════════════ Frans — De tegenwoordige tijd

VARIANTEN[("frans.json", "De tegenwoordige tijd")] = {
    'Vul aan: "Je ... français." (ik spreek Frans)': [
        dict(vraag='Vul aan: "Il ... beaucoup." (hij praat veel)',
             opties=["parle", "parles", "parlons", "parlent"], antwoord=0,
             uitleg="Il parle beaucoup. Bij il hoort de uitgang -e."),
        dict(vraag='Vul aan: "Nous ... à table." (wij praten aan tafel)',
             opties=["parlons", "parlez", "parle", "parles"], antwoord=0,
             uitleg="Nous parlons à table. Bij nous is het altijd -ons."),
        dict(vraag='Vul aan: "Vous ... trop vite." (jullie praten te snel)',
             opties=["parlez", "parlons", "parle", "parlent"], antwoord=0,
             uitleg="Vous parlez trop vite. Bij vous hoort de uitgang -ez."),
    ],
    'Vul aan: "Tu ... au football." (van jouer, spelen)': [
        dict(vraag='Vul aan: "Il ... au tennis." (van jouer, spelen)', antwoord="joue",
             uitleg="Il joue au tennis. Bij il hoort de uitgang -e."),
        dict(vraag='Vul aan: "Nous ... dans le jardin." (van jouer, spelen)', antwoord="jouons",
             uitleg="Nous jouons dans le jardin. Bij nous is het altijd -ons."),
        dict(vraag='Vul aan: "Elles ... ensemble." (van jouer, spelen)', antwoord="jouent",
             uitleg="Elles jouent ensemble. Bij elles hoort -ent, en die uitgang hoor je niet."),
    ],
    'Welke uitgang krijgt een werkwoord op -er bij "nous"?': [
        dict(vraag='Welke uitgang krijgt een werkwoord op -er bij "vous"?',
             opties=["-ez", "-ent", "-ons", "-es"], antwoord=0,
             uitleg="Vous parlez, vous jouez, vous regardez: bij vous is het altijd -ez."),
        dict(vraag='Welke uitgang krijgt een werkwoord op -er bij "tu"?',
             opties=["-e", "-es", "-ons", "-ez"], antwoord=1,
             uitleg="Tu parles, tu joues, tu regardes: bij tu is het altijd -es."),
        dict(vraag='Welke uitgang krijgt een werkwoord op -er bij "ils"?',
             opties=["-e", "-es", "-ent", "-ez"], antwoord=2,
             uitleg="Ils parlent, ils jouent, ils regardent: bij ils is het -ent, en die hoor je niet."),
    ],
    'Vul aan: "Vous ... la télé."': [
        dict(vraag='Vul aan: "Nous ... la télé."',
             opties=["regardez", "regardons", "regarde", "regardent"], antwoord=1,
             uitleg="Nous regardons la télé. Bij nous hoort de uitgang -ons."),
        dict(vraag='Vul aan: "Elle ... la télé."',
             opties=["regardez", "regardons", "regarde", "regardent"], antwoord=2,
             uitleg="Elle regarde la télé. Bij elle hoort de uitgang -e."),
        dict(vraag='Vul aan: "Ils ... la télé."',
             opties=["regardez", "regardons", "regarde", "regardent"], antwoord=3,
             uitleg="Ils regardent la télé. Bij ils hoort de uitgang -ent."),
    ],
    "In welke zin staat de uitgang van het werkwoord juist?": [
        dict(opties=["Ils chante une chanson", "Il chantent une chanson", "Ils chantent une chanson",
                     "Ils chantes une chanson"], antwoord=2,
             uitleg="Ils chantent une chanson: zij zingen een lied. Meer personen, dus de uitgang -ent."),
        dict(opties=["Nous mangez une pizza", "Nous mangeons une pizza", "Nous mange une pizza",
                     "Nous mangent une pizza"], antwoord=1,
             uitleg="Nous mangeons une pizza: wij eten een pizza. Bij nous hoort -ons, en manger houdt zijn e."),
        dict(opties=["Tu regarde un film", "Tu regardes un film", "Tu regardez un film",
                     "Tu regardent un film"], antwoord=1,
             uitleg="Tu regardes un film: jij kijkt naar een film. Bij tu hoort -es."),
    ],
    'Vul aan: "Nous ... à l\'école." (van aller, gaan)': [
        dict(vraag='Vul aan: "Tu ... à la piscine." (van aller, gaan)', antwoord="vas",
             uitleg="Tu vas à la piscine. Aller gaat zo: je vais, tu vas, il va, nous allons, vous allez, ils vont."),
        dict(vraag='Vul aan: "Vous ... au marché." (van aller, gaan)', antwoord="allez",
             uitleg="Vous allez au marché. Bij vous hoort allez."),
        dict(vraag='Vul aan: "Elle ... au travail." (van aller, gaan)', antwoord="va",
             uitleg="Elle va au travail. Bij il en elle hoort va."),
    ],
    'Vul aan: "Je ... au cinéma." (ik ga naar de bioscoop)': [
        dict(vraag='Vul aan: "Tu ... au cinéma." (jij gaat naar de bioscoop)',
             opties=["va", "vais", "vas", "allez"], antwoord=2,
             uitleg="Tu vas au cinéma. Bij tu hoort vas."),
        dict(vraag='Vul aan: "Nous ... au cinéma." (wij gaan naar de bioscoop)',
             opties=["va", "allons", "vais", "allez"], antwoord=1,
             uitleg="Nous allons au cinéma. Bij nous hoort allons."),
        dict(vraag='Vul aan: "Ils ... au cinéma." (zij gaan naar de bioscoop)',
             opties=["vont", "vais", "vas", "allez"], antwoord=0,
             uitleg="Ils vont au cinéma. Bij ils hoort vont."),
    ],
    'Vul aan: "Qu\'est-ce que tu ...?" (wat doe je, van faire)': [
        dict(vraag='Vul aan: "Qu\'est-ce qu\'il ...?" (wat doet hij, van faire)', antwoord="fait",
             uitleg="Qu'est-ce qu'il fait ? Bij il hoort fait."),
        dict(vraag='Vul aan: "Qu\'est-ce que vous ...?" (wat doen jullie, van faire)', antwoord="faites",
             uitleg="Qu'est-ce que vous faites ? Bij vous hoort faites, niet faisez."),
        dict(vraag='Vul aan: "Qu\'est-ce qu\'elles ...?" (wat doen zij, van faire)', antwoord="font",
             uitleg="Qu'est-ce qu'elles font ? Bij elles hoort font."),
    ],
    "In welke zin staat het werkwoord fout?": [
        dict(opties=["Elle chante bien", "Nous jouons dehors", "Vous parlez vite", "Tu parle français"],
             antwoord=3, uitleg="Tu parle français klopt niet: bij tu hoort parles, met een s."),
        dict(opties=["Je regarde la télé", "Ils mangent une pomme", "Nous chantons fort", "Il parlent vite"],
             antwoord=3, uitleg="Il parlent vite klopt niet: bij il hoort parle, zonder -nt."),
        dict(opties=["Tu joues au foot", "Vous dansez bien", "Elles écoutent la radio", "Nous parlez français"],
             antwoord=3, uitleg="Nous parlez français klopt niet: bij nous hoort parlons."),
    ],
    'Vul aan: "Ils ... à la maison." (van aller)': [
        dict(vraag='Vul aan: "Vous ... à la maison." (van aller)',
             opties=["va", "vont", "allons", "allez"], antwoord=3,
             uitleg="Vous allez à la maison: jullie gaan naar huis."),
        dict(vraag='Vul aan: "Je ... à la maison." (van aller)',
             opties=["vais", "vont", "allons", "allez"], antwoord=0,
             uitleg="Je vais à la maison: ik ga naar huis."),
        dict(vraag='Vul aan: "Elle ... à la maison." (van aller)',
             opties=["va", "vont", "allons", "allez"], antwoord=0,
             uitleg="Elle va à la maison: zij gaat naar huis."),
    ],
    'Vul aan: "Elle ... de la musique." (van écouter, luisteren)': [
        dict(vraag='Vul aan: "Nous ... de la musique." (van écouter, luisteren)', antwoord="écoutons",
             uitleg="Nous écoutons de la musique. Bij nous hoort -ons."),
        dict(vraag='Vul aan: "Tu ... la radio." (van écouter, luisteren)', antwoord="écoutes",
             uitleg="Tu écoutes la radio. Bij tu hoort -es."),
        dict(vraag='Vul aan: "Ils ... le professeur." (van écouter, luisteren)', antwoord="écoutent",
             uitleg="Ils écoutent le professeur. Bij ils hoort -ent, en die uitgang hoor je niet."),
    ],
}

# ═══════════════════════════════════════════════ Frans — Zinnen bouwen

VARIANTEN[("frans.json", "Zinnen bouwen")] = {
    'Vul aan: "... fille" (het meisje)': [
        dict(vraag='Vul aan: "... table" (de tafel)',
             opties=["Le", "La", "Les", "Un"], antwoord=1,
             uitleg="La table. Table is vrouwelijk, dus la."),
        dict(vraag='Vul aan: "... livre" (het boek)',
             opties=["Le", "La", "Les", "Une"], antwoord=0,
             uitleg="Le livre. Livre is mannelijk, dus le."),
        dict(vraag='Vul aan: "... maison" (het huis)',
             opties=["Le", "La", "Les", "Un"], antwoord=1,
             uitleg="La maison. Maison is vrouwelijk, dus la."),
    ],
    'Vul het lidwoord aan: "... garçon" (de jongen)': [
        dict(vraag='Vul het lidwoord aan: "... porte" (de deur)', antwoord="la",
             uitleg="La porte. Porte is vrouwelijk, dus la."),
        dict(vraag='Vul het lidwoord aan: "... chien" (de hond)', antwoord="le",
             uitleg="Le chien. Chien is mannelijk, dus le."),
        dict(vraag='Vul het lidwoord aan: "... voiture" (de auto)', antwoord="la",
             uitleg="La voiture. Voiture is vrouwelijk, dus la."),
    ],
    'Wat is het meervoud van "le livre"?': [
        dict(vraag='Wat is het meervoud van "la table"?',
             opties=["le tables", "les table", "les tables", "la tables"], antwoord=2,
             uitleg="Les tables. In het meervoud wordt le en la allebei les, en het woord krijgt een s."),
        dict(vraag='Wat is het meervoud van "le chien"?',
             opties=["les chien", "les chiens", "le chiens", "la chiens"], antwoord=1,
             uitleg="Les chiens. Het lidwoord wordt les en het woord krijgt een s."),
        dict(vraag='Wat is het meervoud van "la fleur"?',
             opties=["la fleurs", "les fleur", "le fleurs", "les fleurs"], antwoord=3,
             uitleg="Les fleurs. Het lidwoord wordt les en het woord krijgt een s."),
    ],
    '"Un" en "une" betekenen een. Welke hoort bij "table"?': [
        dict(vraag='"Un" en "une" betekenen een. Welke hoort bij "livre"?',
             opties=["un", "une", "des", "les"], antwoord=0,
             uitleg="Un livre, want livre is mannelijk. Une table, want table is vrouwelijk."),
        dict(vraag='"Un" en "une" betekenen een. Welke hoort bij "maison"?',
             opties=["un", "une", "des", "les"], antwoord=1,
             uitleg="Une maison, want maison is vrouwelijk."),
        dict(vraag='"Un" en "une" betekenen een. Welke hoort bij "chien"?',
             opties=["un", "une", "des", "les"], antwoord=0,
             uitleg="Un chien, want chien is mannelijk."),
    ],
    'Vul aan: "Je ... parle pas anglais." (het ontbrekende woordje)': [
        dict(vraag='Vul aan: "Il ... mange pas de viande." (het ontbrekende woordje)', antwoord="ne",
             uitleg="Il ne mange pas de viande: hij eet geen vlees. Ne staat voor het werkwoord."),
        dict(vraag='Vul aan: "Nous ne regardons ... la télé." (het ontbrekende woordje)', antwoord="pas",
             uitleg="Nous ne regardons pas la télé: wij kijken geen televisie. Pas staat achter het werkwoord."),
        dict(vraag='Vul aan: "Elle ne chante ... bien." (het ontbrekende woordje)', antwoord="pas",
             uitleg="Elle ne chante pas bien: zij zingt niet goed. Het werkwoord staat tussen ne en pas."),
    ],
    'Hoe zeg je "Ik heb geen hond"?': [
        dict(vraag='Hoe zeg je "Ik heb geen fiets"?',
             opties=["Je n'ai pas de vélo", "Je ne pas ai vélo", "Je n'ai vélo pas", "Je pas ai de vélo"],
             antwoord=0, uitleg="Je n'ai pas de vélo. Ne wordt n' voor een klinker, en na een ontkenning wordt un meestal de."),
        dict(vraag='Hoe zeg je "Hij eet geen vlees"?',
             opties=["Il ne mange pas de viande", "Il mange ne pas viande", "Il ne pas mange viande",
                     "Il mange pas ne de viande"],
             antwoord=0, uitleg="Il ne mange pas de viande. Het werkwoord staat tussen ne en pas."),
        dict(vraag='Hoe zeg je "Wij kijken geen televisie"?',
             opties=["Nous ne regardons pas la télé", "Nous regardons ne pas la télé",
                     "Nous ne pas regardons la télé", "Nous regardons pas ne la télé"],
             antwoord=0, uitleg="Nous ne regardons pas la télé. Het werkwoord staat tussen ne en pas."),
    ],
    'Wat betekent "où" in een vraag?': [
        dict(vraag='Wat betekent "quand" in een vraag?',
             opties=["wanneer", "waarom", "waar", "hoe"], antwoord=0,
             uitleg="Quand is wanneer: Quand est-ce que tu arrives ?"),
        dict(vraag='Wat betekent "comment" in een vraag?',
             opties=["wanneer", "waarom", "waar", "hoe"], antwoord=3,
             uitleg="Comment is hoe: Comment ça va ?"),
        dict(vraag='Wat betekent "pourquoi" in een vraag?',
             opties=["wanneer", "waarom", "waar", "hoe"], antwoord=1,
             uitleg="Pourquoi is waarom. Het antwoord begint meestal met parce que, omdat."),
    ],
    "Welk Frans vraagwoord betekent waarom?": [
        dict(vraag="Welk Frans vraagwoord betekent hoe?", antwoord="comment",
             uitleg="Comment is hoe: Comment tu t'appelles ?"),
        dict(vraag="Welk Frans vraagwoord betekent waar?", antwoord="où",
             uitleg="Où is waar: Où habites-tu ?"),
        dict(vraag="Welk Frans vraagwoord betekent wanneer?", antwoord="quand",
             uitleg="Quand is wanneer: Quand est-ce qu'on mange ?"),
    ],
    'Welke zin betekent "een rode auto"?': [
        dict(vraag='Welke zin betekent "een zwarte hond"?',
             opties=["Un noir chien", "Une chien noir", "Un chien noirs", "Un chien noir"], antwoord=3,
             uitleg="Un chien noir. Chien is mannelijk (un), en de kleur komt erachter."),
        dict(vraag='Welke zin betekent "een groene deur"?',
             opties=["Une verte porte", "Un porte verte", "Une porte vertes", "Une porte verte"], antwoord=3,
             uitleg="Une porte verte. Porte is vrouwelijk (une), dus de kleur krijgt een e, en ze komt erachter."),
        dict(vraag='Welke zin betekent "een blauwe fiets"?',
             opties=["Un bleu vélo", "Un vélo bleus", "Un vélo bleu", "Une vélo bleu"], antwoord=2,
             uitleg="Un vélo bleu. Vélo is mannelijk (un), en de kleur komt erachter."),
    ],
    'Wat betekent "et"?': [
        dict(vraag='Wat betekent "ou"?', opties=["of", "maar", "en", "want"], antwoord=0,
             uitleg="Ou is of: du thé ou du café ?"),
        dict(vraag='Wat betekent "mais"?', opties=["of", "maar", "en", "want"], antwoord=1,
             uitleg="Mais is maar: J'aime le chocolat, mais je préfère les bonbons."),
        dict(vraag='Wat betekent "parce que"?', opties=["of", "maar", "en", "omdat"], antwoord=3,
             uitleg="Parce que is omdat. Het is het antwoord op pourquoi."),
    ],
    "Welk Frans woordje betekent maar?": [
        dict(vraag="Welk Frans woordje betekent en?", antwoord="et",
             uitleg="Et is en: un chien et un chat."),
        dict(vraag="Welk Frans woordje betekent omdat?", antwoord="parce que",
             uitleg="Parce que is omdat: Je reste à la maison parce qu'il pleut."),
        dict(vraag="Welk Frans woordje betekent of?", antwoord="ou",
             uitleg="Ou is of: tu viens ou tu restes ?"),
    ],
}

# ═══════════════════════════════════════════════ Engels — To be en to have

VARIANTEN[("engels.json", "To be en to have")] = {
    'Vul aan: "She ... my best friend."': [
        dict(vraag='Vul aan: "He ... my neighbour."', antwoord="is",
             uitleg="He is my neighbour. Bij he, she en it hoort is."),
        dict(vraag='Vul aan: "They ... my cousins."', antwoord="are",
             uitleg="They are my cousins. Bij we, you en they hoort are."),
        dict(vraag='Vul aan: "I ... in the garden."', antwoord="am",
             uitleg="I am in the garden. Am hoort enkel bij I."),
    ],
    'Vul aan: "We ... in the same class."': [
        dict(vraag='Vul aan: "You ... very kind."', antwoord="are",
             uitleg="You are very kind. Bij you hoort are, ook als het over één persoon gaat."),
        dict(vraag='Vul aan: "It ... very cold today."', antwoord="is",
             uitleg="It is very cold today. Bij it hoort is."),
        dict(vraag='Vul aan: "My sister ... at school."', antwoord="is",
             uitleg="My sister is at school. My sister is hetzelfde als she, dus is."),
    ],
    'Welke zin is juist bij "he"?': [
        dict(vraag='Welke zin is juist bij "she"?',
             opties=["She are tired.", "She is tired.", "She am tired.", "She be tired."], antwoord=1,
             uitleg="Bij she hoort is. Am hoort enkel bij I."),
        dict(vraag='Welke zin is juist bij "we"?',
             opties=["We is ready.", "We are ready.", "We am ready.", "We be ready."], antwoord=1,
             uitleg="Bij we hoort are, net als bij you en they."),
        dict(vraag='Welke zin is juist bij "I"?',
             opties=["I is hungry.", "I are hungry.", "I am hungry.", "I be hungry."], antwoord=2,
             uitleg="Bij I hoort am, en bij niemand anders."),
    ],
    'Bij "I" hoort de vorm "is".': [
        dict(vraag='Bij "they" hoort de vorm "are".', antwoord=True,
             uitleg="Klopt. Bij we, you en they hoort are."),
        dict(vraag='Bij "it" hoort de vorm "are".', antwoord=False,
             uitleg="Niet juist. Bij it hoort is, net als bij he en she."),
        dict(vraag='Bij "you" hoort de vorm "are".', antwoord=True,
             uitleg="Klopt, ook als je tegen één persoon praat: you are."),
    ],
    'Wat is de ontkenning van "They are late"?': [
        dict(vraag='Wat is de ontkenning van "She is angry"?',
             opties=["She not is angry.", "She isn't angry.", "She doesn't is angry.", "She aren't angry."],
             antwoord=1, uitleg="Bij to be zet je not achter de werkwoordsvorm: she is not, korter she isn't."),
        dict(vraag='Wat is de ontkenning van "We are ready"?',
             opties=["We not are ready.", "We aren't ready.", "We don't are ready.", "We isn't ready."],
             antwoord=1, uitleg="We are not ready, korter we aren't ready."),
        dict(vraag='Wat is de ontkenning van "I am tired"?',
             opties=["I not am tired.", "I'm not tired.", "I don't am tired.", "I amn't tired."],
             antwoord=1, uitleg="I am not tired, korter I'm not tired. Amn't bestaat niet."),
    ],
    'Vul aan: "I ... a new bike." (hebben)': [
        dict(vraag='Vul aan: "We ... a big garden." (hebben)', antwoord=["have", "have got"],
             uitleg="We have a big garden, of we have got a big garden."),
        dict(vraag='Vul aan: "They ... two dogs." (hebben)', antwoord=["have", "have got"],
             uitleg="They have two dogs, of they have got two dogs."),
        dict(vraag='Vul aan: "You ... a nice jacket." (hebben)', antwoord=["have", "have got"],
             uitleg="You have a nice jacket, of you have got a nice jacket."),
    ],
    'Welke zin is juist met "to have"?': [
        dict(opties=["My sister have a cat.", "My sister has a cat.", "My sister haves a cat.",
                     "My sister having a cat."], antwoord=1,
             uitleg="My sister is hetzelfde als she, en bij she hoort has."),
        dict(opties=["The teacher have a car.", "The teacher haves a car.", "The teacher has a car.",
                     "The teacher having a car."], antwoord=2,
             uitleg="The teacher is hetzelfde als he of she, en dan is het has."),
        dict(opties=["My friends has a boat.", "My friends have a boat.", "My friends haves a boat.",
                     "My friends having a boat."], antwoord=1,
             uitleg="My friends is meervoud, hetzelfde als they, en dan is het have."),
    ],
    'Hoe maak je een vraag van "You are ready"?': [
        dict(vraag='Hoe maak je een vraag van "She is at home"?',
             opties=["She is at home?", "Is she at home?", "Does she is at home?", "At home is she?"],
             antwoord=1, uitleg="Bij to be draai je gewoon om: Is she at home?"),
        dict(vraag='Hoe maak je een vraag van "They are hungry"?',
             opties=["They are hungry?", "Are they hungry?", "Do they are hungry?", "Hungry are they?"],
             antwoord=1, uitleg="Bij to be draai je gewoon om: Are they hungry?"),
        dict(vraag='Hoe maak je een vraag van "It is cold"?',
             opties=["It is cold?", "Is it cold?", "Does it is cold?", "Cold it is?"],
             antwoord=1, uitleg="Bij to be draai je gewoon om: Is it cold?"),
    ],
    'Vul aan: "... you tired?" (vraag met to be)': [
        dict(vraag='Vul aan: "... she your sister?" (vraag met to be)', antwoord="Is",
             uitleg="Is she your sister? betekent: is zij jouw zus?"),
        dict(vraag='Vul aan: "... they at school?" (vraag met to be)', antwoord="Are",
             uitleg="Are they at school? betekent: zijn zij op school?"),
        dict(vraag='Vul aan: "... I too late?" (vraag met to be)', antwoord="Am",
             uitleg="Am I too late? betekent: ben ik te laat? Bij I hoort am."),
    ],
    'Welke korte vorm hoort bij "they are"?': [
        dict(vraag='Welke korte vorm hoort bij "she is"?',
             opties=["she's", "shes", "she'is", "she are"], antwoord=0,
             uitleg="She's, met een apostrof in de plaats van de i van is."),
        dict(vraag='Welke korte vorm hoort bij "I am"?',
             opties=["I'm", "Im", "I'am", "I're"], antwoord=0,
             uitleg="I'm, met een apostrof in de plaats van de a van am."),
        dict(vraag='Welke korte vorm hoort bij "we are"?',
             opties=["we're", "were", "we'are", "weare"], antwoord=0,
             uitleg="We're, met een apostrof. Were zonder apostrof is de verleden tijd van are."),
    ],
    'Vul aan: "She ... two brothers." (hebben)': [
        dict(vraag='Vul aan: "He ... a new phone." (hebben)', antwoord="has",
             uitleg="He has a new phone. Bij he hoort has."),
        dict(vraag='Vul aan: "We ... enough time." (hebben)', antwoord="have",
             uitleg="We have enough time. Bij we hoort have."),
        dict(vraag='Vul aan: "My cousin ... a rabbit." (hebben)', antwoord="has",
             uitleg="My cousin has a rabbit. My cousin is hetzelfde als he of she, dus has."),
    ],
    'Wat is de ontkenning van "I have a pen"?': [
        dict(vraag='Wat is de ontkenning van "She has a bike"?',
             opties=["She has not a bike.", "She doesn't have a bike.", "She not has a bike.",
                     "She don't has a bike."], antwoord=1,
             uitleg="Bij she hoort doesn't, en daarna komt have zonder s."),
        dict(vraag='Wat is de ontkenning van "They have a dog"?',
             opties=["They have not a dog.", "They don't have a dog.", "They not have a dog.",
                     "They doesn't have a dog."], antwoord=1,
             uitleg="Bij they hoort don't: they don't have a dog."),
        dict(vraag='Wat is de ontkenning van "He has time"?',
             opties=["He has not time.", "He doesn't have time.", "He don't have time.",
                     "He not has time."], antwoord=1,
             uitleg="Bij he hoort doesn't, en daarna komt have zonder s."),
    ],
    "Welke zin is juist bij een meervoud?": [
        dict(opties=["Where is your shoes?", "Where are your shoes?", "Where am your shoes?",
                     "Where be your shoes?"], antwoord=1,
             uitleg="Shoes is meervoud, dus are."),
        dict(opties=["Where is my keys?", "Where are my keys?", "Where am my keys?",
                     "Where be my keys?"], antwoord=1,
             uitleg="Keys is meervoud, dus are."),
        dict(opties=["Where is the children?", "Where are the children?", "Where am the children?",
                     "Where be the children?"], antwoord=1,
             uitleg="Children is meervoud, ook al staat er geen s op het einde, dus are."),
    ],
    'Vul aan: "My parents ... at work."': [
        dict(vraag='Vul aan: "My friends ... in the garden."', antwoord="are",
             uitleg="My friends are in the garden. Friends is meervoud, dus are."),
        dict(vraag='Vul aan: "The dog ... in the kitchen."', antwoord="is",
             uitleg="The dog is in the kitchen. Eén hond, dus is."),
        dict(vraag='Vul aan: "The shops ... closed today."', antwoord="are",
             uitleg="The shops are closed today. Shops is meervoud, dus are."),
    ],
    'Wat betekent "We aren\'t at home"?': [
        dict(vraag='Wat betekent "She isn\'t at school"?',
             opties=["Zij is op school.", "Zij is niet op school.", "Zij gaat naar school.",
                     "Zij heeft geen school."], antwoord=1,
             uitleg="Isn't is is not, dus: zij is niet op school."),
        dict(vraag='Wat betekent "They haven\'t got a car"?',
             opties=["Zij hebben een auto.", "Zij hebben geen auto.", "Zij kopen een auto.",
                     "Zij rijden met de auto."], antwoord=1,
             uitleg="Haven't is have not, dus: zij hebben geen auto."),
        dict(vraag='Wat betekent "I\'m not hungry"?',
             opties=["Ik heb honger.", "Ik heb geen honger.", "Ik ben moe.", "Ik eet niet graag."],
             antwoord=1, uitleg="I'm not is I am not, dus: ik heb geen honger."),
    ],
}

# ══════════════════════════════════════════ Engels — De tegenwoordige tijd

VARIANTEN[("engels.json", "De tegenwoordige tijd")] = {
    "Welke zin is juist in de tegenwoordige tijd?": [
        dict(opties=["She read a book.", "She reads a book.", "She reading a book.",
                     "She is read a book."], antwoord=1,
             uitleg="Bij he, she en it komt er een -s achter het werkwoord: she reads."),
        dict(opties=["It rain a lot here.", "It rains a lot here.", "It raining a lot here.",
                     "It is rain a lot here."], antwoord=1,
             uitleg="Bij it komt er een -s achter het werkwoord: it rains."),
        dict(opties=["My brother work in a bank.", "My brother works in a bank.",
                     "My brother working in a bank.", "My brother is work in a bank."], antwoord=1,
             uitleg="My brother is hetzelfde als he, dus komt er een -s bij: works."),
    ],
    'Vul aan: "She ... to school by bike." (gaan)': [
        dict(vraag='Vul aan: "He ... to the shop every day." (gaan)', antwoord="goes",
             uitleg="He goes to the shop every day. Na go komt er -es bij."),
        dict(vraag='Vul aan: "They ... to the park on Sunday." (gaan)', antwoord="go",
             uitleg="They go to the park on Sunday. Bij they komt er niets bij."),
        dict(vraag='Vul aan: "My sister ... to the pool on Friday." (gaan)', antwoord="goes",
             uitleg="My sister goes to the pool on Friday. My sister is hetzelfde als she."),
    ],
    'Wat is de vraagvorm van "You like pizza"?': [
        dict(vraag='Wat is de vraagvorm van "He likes football"?',
             opties=["Do he like football?", "Does he like football?", "Does he likes football?",
                     "He does like football?"], antwoord=1,
             uitleg="Bij he gebruik je does, en daarna valt de -s van het werkwoord weg."),
        dict(vraag='Wat is de vraagvorm van "They live here"?',
             opties=["Do they live here?", "Does they live here?", "Do they lives here?",
                     "They do live here?"], antwoord=0,
             uitleg="Bij they gebruik je do, en het werkwoord blijft zoals het is."),
        dict(vraag='Wat is de vraagvorm van "She works on Saturday"?',
             opties=["Do she work on Saturday?", "Does she works on Saturday?",
                     "Does she work on Saturday?", "She does work on Saturday?"], antwoord=2,
             uitleg="Bij she gebruik je does, en daarna valt de -s van works weg."),
    ],
    'Vul aan: "... he speak English?" (vraag)': [
        dict(vraag='Vul aan: "... they play tennis?" (vraag)', antwoord="Do",
             uitleg="Do they play tennis? Bij they hoort do."),
        dict(vraag='Vul aan: "... she know the answer?" (vraag)', antwoord="Does",
             uitleg="Does she know the answer? Bij she hoort does, en know verliest zijn -s."),
        dict(vraag='Vul aan: "... you live in Genk?" (vraag)', antwoord="Do",
             uitleg="Do you live in Genk? Bij you hoort do."),
    ],
    "Welke ontkennende zin is juist?": [
        dict(opties=["He don't like fish.", "He doesn't likes fish.", "He doesn't like fish.",
                     "He not likes fish."], antwoord=2,
             uitleg="Bij he hoort doesn't, en daarna komt het werkwoord zonder -s."),
        dict(opties=["We doesn't play tennis.", "We don't play tennis.", "We don't plays tennis.",
                     "We not play tennis."], antwoord=1,
             uitleg="Bij we hoort don't, en daarna komt het werkwoord zonder -s."),
        dict(opties=["She don't watch television.", "She doesn't watches television.",
                     "She not watch television.", "She doesn't watch television."], antwoord=3,
             uitleg="Bij she hoort doesn't, en daarna komt het werkwoord zonder -s."),
    ],
    'Vul aan: "My father ... in a shop." (werken)': [
        dict(vraag='Vul aan: "My mother ... in a hospital." (werken)', antwoord="works",
             uitleg="My mother works in a hospital. My mother is hetzelfde als she, dus -s erbij."),
        dict(vraag='Vul aan: "My parents ... in the same office." (werken)', antwoord="work",
             uitleg="My parents work in the same office. My parents is meervoud, dus geen -s."),
        dict(vraag='Vul aan: "My uncle ... at the airport." (werken)', antwoord="works",
             uitleg="My uncle works at the airport. My uncle is hetzelfde als he, dus -s erbij."),
    ],
    "Welke zin klopt?": [
        dict(opties=["He trys again.", "He tries again.", "He tryes again.", "He try again."], antwoord=1,
             uitleg="Een medeklinker plus -y wordt -ies: try wordt tries."),
        dict(opties=["She carrys her bag.", "She carryes her bag.", "She carries her bag.",
                     "She carry her bag."], antwoord=2,
             uitleg="Een medeklinker plus -y wordt -ies: carry wordt carries."),
        dict(opties=["It flys away.", "It flyes away.", "It fly away.", "It flies away."], antwoord=3,
             uitleg="Een medeklinker plus -y wordt -ies: fly wordt flies."),
    ],
    'Vul aan: "They ... in Antwerp." (wonen)': [
        dict(vraag='Vul aan: "We ... near the station." (wonen)', antwoord="live",
             uitleg="We live near the station. Bij we komt er geen -s bij."),
        dict(vraag='Vul aan: "She ... in a big house." (wonen)', antwoord="lives",
             uitleg="She lives in a big house. Bij she komt er een -s bij."),
        dict(vraag='Vul aan: "My grandparents ... in Spain." (wonen)', antwoord="live",
             uitleg="My grandparents live in Spain. Meervoud, dus geen -s."),
    ],
    'Wat is de ontkenning van "He knows the answer"?': [
        dict(vraag='Wat is de ontkenning van "She speaks French"?',
             opties=["She don't speak French.", "She doesn't speaks French.",
                     "She doesn't speak French.", "She not speaks French."], antwoord=2,
             uitleg="Doesn't hoort bij she, en daarna valt de -s van het werkwoord weg."),
        dict(vraag='Wat is de ontkenning van "They want ice cream"?',
             opties=["They doesn't want ice cream.", "They don't want ice cream.",
                     "They don't wants ice cream.", "They not want ice cream."], antwoord=1,
             uitleg="Don't hoort bij they, en het werkwoord blijft zoals het is."),
        dict(vraag='Wat is de ontkenning van "It works well"?',
             opties=["It don't work well.", "It doesn't works well.", "It not works well.",
                     "It doesn't work well."], antwoord=3,
             uitleg="Doesn't hoort bij it, en daarna valt de -s van works weg."),
    ],
    'Vul aan: "She ... her homework after dinner." (doen)': [
        dict(vraag='Vul aan: "He ... the dishes every evening." (doen)', antwoord="does",
             uitleg="He does the dishes every evening. To do wordt does bij he."),
        dict(vraag='Vul aan: "They ... their homework together." (doen)', antwoord="do",
             uitleg="They do their homework together. Bij they blijft het do."),
        dict(vraag='Vul aan: "My brother ... nothing on Sunday." (doen)', antwoord="does",
             uitleg="My brother does nothing on Sunday. My brother is hetzelfde als he."),
    ],
    "Welke vraag is juist gebouwd?": [
        dict(opties=["Does he plays the guitar?", "Does he play the guitar?", "Do he play the guitar?",
                     "Is he play the guitar?"], antwoord=1,
             uitleg="Na does gebruik je het werkwoord zonder -s."),
        dict(opties=["Do they lives in Hasselt?", "Does they live in Hasselt?",
                     "Do they live in Hasselt?", "Are they live in Hasselt?"], antwoord=2,
             uitleg="Bij they hoort do, en het werkwoord blijft zoals het is."),
        dict(opties=["Does your sister likes music?", "Do your sister like music?",
                     "Does your sister like music?", "Is your sister like music?"], antwoord=2,
             uitleg="Your sister is hetzelfde als she, dus does, en dan het werkwoord zonder -s."),
    ],
    'Vul aan: "He ... a lot of books." (lezen)': [
        dict(vraag='Vul aan: "She ... the newspaper every morning." (lezen)', antwoord="reads",
             uitleg="She reads the newspaper every morning. Bij she komt er een -s bij."),
        dict(vraag='Vul aan: "We ... a story before bed." (lezen)', antwoord="read",
             uitleg="We read a story before bed. Bij we komt er geen -s bij."),
        dict(vraag='Vul aan: "My friend ... comics." (lezen)', antwoord="reads",
             uitleg="My friend reads comics. My friend is hetzelfde als he of she, dus -s erbij."),
    ],
}

# ══════════════════════════════════════════════ Engels — Zinnen bouwen

VARIANTEN[("engels.json", "Zinnen bouwen")] = {
    'Wat is het meervoud van "child"?': [
        dict(vraag='Wat is het meervoud van "woman"?',
             opties=["womans", "womens", "women", "womanes"], antwoord=2,
             uitleg="Women is een onregelmatig meervoud; er komt geen -s bij."),
        dict(vraag='Wat is het meervoud van "mouse"?',
             opties=["mouses", "mice", "mousen", "mices"], antwoord=1,
             uitleg="Mice is een onregelmatig meervoud; er komt geen -s bij."),
        dict(vraag='Wat is het meervoud van "tooth"?',
             opties=["tooths", "toothes", "teeth", "teeths"], antwoord=2,
             uitleg="Teeth is een onregelmatig meervoud, net als foot dat feet wordt."),
    ],
    'Vul aan: het meervoud van "box" is ...': [
        dict(vraag='Vul aan: het meervoud van "watch" is ...', antwoord="watches",
             uitleg="Watches. Na -x, -s, -ch en -sh komt er -es bij."),
        dict(vraag='Vul aan: het meervoud van "bus" is ...', antwoord="buses",
             uitleg="Buses. Na -s komt er -es bij."),
        dict(vraag='Vul aan: het meervoud van "brush" is ...', antwoord="brushes",
             uitleg="Brushes. Na -sh komt er -es bij."),
    ],
    'Welk lidwoord hoort hier: "... apple"?': [
        dict(vraag='Welk lidwoord hoort hier: "... house"?',
             opties=["a", "an", "one of", "some"], antwoord=0,
             uitleg="A house. House begint met een h die je hoort, dus geen klinkerklank."),
        dict(vraag='Welk lidwoord hoort hier: "... orange"?',
             opties=["a", "an", "one of", "some"], antwoord=1,
             uitleg="An orange, want orange begint met een klinkerklank."),
        dict(vraag='Welk lidwoord hoort hier: "... book"?',
             opties=["a", "an", "one of", "some"], antwoord=0,
             uitleg="A book, want book begint met een medeklinkerklank."),
    ],
    'Vul aan: het meervoud van "man" is ...': [
        dict(vraag='Vul aan: het meervoud van "goose" is ...', antwoord="geese",
             uitleg="Geese. Net als tooth dat teeth wordt."),
        dict(vraag='Vul aan: het meervoud van "person" is ...', antwoord="people",
             uitleg="People. Persons bestaat wel, maar people is wat je gewoon zegt."),
        dict(vraag='Vul aan: het meervoud van "sheep" is ...', antwoord="sheep",
             uitleg="Sheep blijft sheep. One sheep, ten sheep."),
    ],
    'Vul aan: "There ... two cats in the garden."': [
        dict(vraag='Vul aan: "There ... a bird on the roof."', antwoord="is",
             uitleg="There is a bird, want a bird is enkelvoud."),
        dict(vraag='Vul aan: "There ... three chairs in the room."', antwoord="are",
             uitleg="There are three chairs, want three chairs is meervoud."),
        dict(vraag='Vul aan: "There ... a letter for you."', antwoord="is",
             uitleg="There is a letter, want a letter is enkelvoud."),
    ],
    "Welk vraagwoord vraagt naar een reden?": [
        dict(vraag="Welk vraagwoord vraagt naar een tijdstip?",
             opties=["Where", "Why", "When", "Who"], antwoord=2,
             uitleg="When betekent wanneer."),
        dict(vraag="Welk vraagwoord vraagt naar een persoon?",
             opties=["Where", "Why", "When", "Who"], antwoord=3,
             uitleg="Who betekent wie."),
        dict(vraag="Welk vraagwoord vraagt naar een manier?",
             opties=["How", "Why", "When", "Who"], antwoord=0,
             uitleg="How betekent hoe: How do you do that?"),
    ],
    'Wat is het meervoud van "city"?': [
        dict(vraag='Wat is het meervoud van "baby"?',
             opties=["babys", "babyes", "babies", "babie"], antwoord=2,
             uitleg="Een medeklinker plus -y wordt -ies: baby wordt babies."),
        dict(vraag='Wat is het meervoud van "story"?',
             opties=["storys", "stories", "storyes", "storie"], antwoord=1,
             uitleg="Een medeklinker plus -y wordt -ies: story wordt stories."),
        dict(vraag='Wat is het meervoud van "party"?',
             opties=["partys", "partyes", "partie", "parties"], antwoord=3,
             uitleg="Een medeklinker plus -y wordt -ies: party wordt parties."),
    ],
    'Vul aan: "This is ... book." Het boek is van mij.': [
        dict(vraag='Vul aan: "This is ... bag." De tas is van jou.', antwoord="your",
             uitleg="This is your bag. Your betekent jouw."),
        dict(vraag='Vul aan: "This is ... house." Het huis is van ons.', antwoord="our",
             uitleg="This is our house. Our betekent ons of onze."),
        dict(vraag='Vul aan: "This is ... ball." De bal is van hem.', antwoord="his",
             uitleg="This is his ball. His betekent zijn."),
    ],
    "Welke zin toont juist van wie de fiets is?": [
        dict(vraag="Welke zin toont juist van wie het boek is?",
             opties=["Toms book is new.", "Tom's book is new.", "Book of Tom is new.",
                     "Tom book is new."], antwoord=1,
             uitleg="Met 's toon je aan van wie iets is: Tom's book."),
        dict(vraag="Welke zin toont juist van wie de hond is?",
             opties=["My sister's dog is big.", "My sisters dog is big.", "Dog of my sister is big.",
                     "My sister dog is big."], antwoord=0,
             uitleg="Met 's toon je aan van wie iets is: my sister's dog."),
        dict(vraag="Welke zin toont juist van wie de auto is?",
             opties=["Annas car is red.", "Car of Anna is red.", "Anna's car is red.",
                     "Anna car is red."], antwoord=2,
             uitleg="Met 's toon je aan van wie iets is: Anna's car."),
    ],
    'Vul aan: het meervoud van "foot" is ...': [
        dict(vraag='Vul aan: het meervoud van "knife" is ...', antwoord="knives",
             uitleg="Knives. De f wordt een v en er komt -es bij."),
        dict(vraag='Vul aan: het meervoud van "leaf" is ...', antwoord="leaves",
             uitleg="Leaves. De f wordt een v en er komt -es bij."),
        dict(vraag='Vul aan: het meervoud van "fish" is ...', antwoord="fish",
             uitleg="Fish blijft fish, ook als het er honderd zijn."),
    ],
    "Welk vraagwoord vraagt naar een plaats?": [
        dict(vraag="Welk vraagwoord vraagt naar een ding?",
             opties=["What", "Where", "Why", "Which"], antwoord=0,
             uitleg="What betekent wat: What is that?"),
        dict(vraag="Welk vraagwoord vraagt naar een keuze tussen twee dingen?",
             opties=["What", "Where", "Why", "Which"], antwoord=3,
             uitleg="Which betekent welke: Which one do you want?"),
        dict(vraag="Welk vraagwoord vraagt van wie iets is?",
             opties=["Whose", "Where", "Why", "Which"], antwoord=0,
             uitleg="Whose betekent van wie: Whose bag is this?"),
    ],
    'Welke zin is juist met "good"?': [
        dict(opties=["She is good in maths.", "She is good at maths.", "She is good on maths.",
                     "She is a good in maths."], antwoord=1,
             uitleg="Good at, niet good in. Je bent good at maths."),
        dict(opties=["They are good on sports.", "They are good in sports.", "They are good at sports.",
                     "They are a good at sports."], antwoord=2,
             uitleg="Good at, niet good on. Je bent good at sports."),
        dict(opties=["He is good in drawing.", "He is good at drawing.", "He is good on drawing.",
                     "He is a good at drawing."], antwoord=1,
             uitleg="Good at, niet good in. Je bent good at drawing."),
    ],
}


# ──────────────────────────────────────────────────────────────────────────
# Nakijken en wegschrijven
# ──────────────────────────────────────────────────────────────────────────

def samen(vraag: dict, variant: dict) -> dict:
    """Een variant aangevuld met wat ze niet zelf zegt, net als in het platform."""
    heel = {k: v for k, v in vraag.items() if k != "varianten"}
    heel.update(variant)
    return heel


def keur(plek: str, vraag: dict):
    soort = vraag["type"]
    if soort == "meerkeuze":
        opties = vraag["opties"]
        assert len(opties) >= 3, f"{plek}: maar {len(opties)} opties"
        assert len(set(opties)) == len(opties), f"{plek}: twee gelijke opties"
        antwoord = vraag["antwoord"]
        nummers = antwoord if isinstance(antwoord, list) else [antwoord]
        assert nummers, f"{plek}: geen antwoord"
        assert len(set(nummers)) == len(nummers), f"{plek}: hetzelfde antwoord twee keer"
        for a in nummers:
            assert isinstance(a, int) and 0 <= a < len(opties), f"{plek}: antwoord {a} bestaat niet"
    elif soort == "waarofniet":
        assert isinstance(vraag["antwoord"], bool), f"{plek}: waar of niet waar zonder boolean"
    elif soort == "invultekst":
        antwoord = vraag["antwoord"]
        antwoorden = antwoord if isinstance(antwoord, list) else [antwoord]
        assert antwoorden, f"{plek}: geen ingevuld antwoord"
        for a in antwoorden:
            assert isinstance(a, str) and a.strip(), f"{plek}: geen ingevuld antwoord"
            assert len(a.split()) <= 3, f"{plek}: te lang invulantwoord {a!r}"
        assert vraag.get("opties") is None, f"{plek}: invulvraag met opties"
    else:
        raise AssertionError(f"{plek}: onbekend type {soort}")
    assert vraag.get("uitleg"), f"{plek}: geen uitleg"


def zet_varianten(bestand: str, stil: bool = False) -> list:
    """Zet de varianten in <bestand> en geeft de hoofdstukken terug die er een kregen."""
    pad = NIVEAU / bestand
    data = json.loads(pad.read_text(encoding="utf-8"))
    geraakt = []
    for (welk, hoofdstuk), lijsten in VARIANTEN.items():
        if welk != bestand:
            continue
        kandidaten = [h for h in data["hoofdstukken"] if h["titel"] == hoofdstuk]
        assert len(kandidaten) == 1, f"{bestand}: {hoofdstuk} staat {len(kandidaten)} keer"
        h = kandidaten[0]
        per_tekst = {v["vraag"]: v for v in h["vragen"]}
        for tekst in lijsten:
            assert tekst in per_tekst, f"{bestand} / {hoofdstuk}: geen vraag met de tekst {tekst!r}"

        # Eerst alles nakijken, dan pas wegschrijven.
        rondes = {}
        for tekst, varianten in lijsten.items():
            vraag = per_tekst[tekst]
            for n, variant in enumerate(varianten, start=2):
                plek = f"{bestand} / {hoofdstuk} / {tekst[:40]}…, beurt {n}"
                assert "type" not in variant, f"{plek}: een variant mag het type niet veranderen"
                heel = samen(vraag, variant)
                keur(plek, heel)
                assert isinstance(heel["antwoord"], list) == isinstance(vraag["antwoord"], list), (
                    f"{plek}: de ene vorm heeft meerdere juiste antwoorden en de andere niet")
                rondes.setdefault(n, []).append(heel["vraag"])

        # Geen enkele ronde mag twee keer dezelfde vraag tonen. De vragen
        # zonder varianten blijven in elke ronde staan, dus die tellen mee.
        vast = [v["vraag"] for v in h["vragen"] if v["vraag"] not in lijsten]
        for n, teksten in rondes.items():
            alle = vast + teksten
            dubbel = {t for t in alle if alle.count(t) > 1}
            assert not dubbel, f"{bestand} / {hoofdstuk}, beurt {n}: staat twee keer: {dubbel}"

        for tekst, varianten in lijsten.items():
            per_tekst[tekst]["varianten"] = varianten
        geraakt.append(h)
        if not stil:
            woorden = sum(len(v) for v in lijsten.values())
            print(f"  {hoofdstuk}: {len(lijsten)} vragen, {woorden} wisselende beurten")

    pad.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return geraakt


def main():
    bestanden = sorted({b for b, _ in VARIANTEN})
    totaal = 0
    for bestand in bestanden:
        print(bestand)
        geraakt = zet_varianten(bestand)
        deel = NIVEAU.parent / "varianten" / f"start-{bestand.replace('.json', '')}-varianten.json"
        deel.parent.mkdir(exist_ok=True)
        deel.write_text(
            json.dumps({"hoofdstukken": geraakt}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8")
        vragen = sum(len(h["vragen"]) for h in geraakt)
        print(f"  → {deel.name}: {len(geraakt)} hoofdstukken, {vragen} vragen\n")
        totaal += sum(len(l) for (b, _), l in VARIANTEN.items() if b == bestand)
    print(f"{totaal} vragen met wisselende woorden.")


if __name__ == "__main__":
    sys.exit(main())
