# -*- coding: utf-8 -*-
"""Uitdaging Frans 🌱 Start (11 november 2026): woorden, jezelf voorstellen,
être en avoir, de tegenwoordige tijd, zinsbouw en de weg vragen door elkaar,
met echte Franse zinnetjes om uit te lezen. Geen nieuwe leerstof.
"""
NIVEAU = "start"
VAK = "Frans"
BESTAND = "start-frans-uitdaging.json"


def mk(vraag, opties, plaats, uitleg):
    """opties[0] is het juiste antwoord; plaats is waar het komt te staan."""
    rest = list(opties[1:])
    rest.insert(plaats, opties[0])
    return {"type": "meerkeuze", "vraag": vraag, "opties": rest, "antwoord": plaats, "uitleg": uitleg}


def iv(vraag, antwoord, uitleg):
    return {"type": "invultekst", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def wn(vraag, antwoord, uitleg):
    return {"type": "waarofniet", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


VRAGEN = [
    mk("Lees: 'Je m'appelle Hugo. J'ai dix ans. J'ai une sœur et deux frères.' Hoeveel kinderen zijn er in het gezin van Hugo?",
       ["vier", "drie", "twee", "vijf"], 1,
       "Hugo heeft een zus en twee broers. Hugo zelf telt ook mee, dus samen zijn ze met vier."),
    mk("Welke zin bevat geen enkele fout?",
       ["Nous sommes en retard et nous allons à l'école.", "Nous avons en retard et nous allons à l'école.",
        "Nous sommes en retard et nous vont à l'école.", "Nous sommes en retard et nous allez à l'école."], 2,
       "Te laat zijn gaat met être (nous sommes), en bij nous hoort de vorm allons van aller."),
    iv("Lees: 'Aujourd'hui, c'est lundi. Demain, je vais au parc.' Op welke dag gaat de schrijver naar het park? Antwoord met het Franse woord.", "mardi",
       "Aujourd'hui is vandaag (lundi, maandag) en demain is morgen. De dag na lundi is mardi."),
    wn("In 'Il fait froid et j'ai froid' staan twee verschillende werkwoorden.", True,
       "Over het weer zegt het Frans il fait (faire). Het zelf koud hebben gaat met avoir: j'ai froid."),
    mk("Lees: 'Il pleut. Léa ne va pas au parc, elle regarde la télé.' Wat doet Léa?",
       ["Ze kijkt tv.", "Ze gaat naar het park.", "Ze speelt in de regen.", "Ze gaat naar school."], 3,
       "Ne va pas betekent gaat niet. Léa blijft dus binnen en kijkt naar de televisie."),
    mk("Welke vraag past bij het antwoord 'J'habite à Genk.'?",
       ["Où est-ce que tu habites ?", "Quel âge as-tu ?", "Comment tu t'appelles ?", "Ça va ?"], 1,
       "J'habite à Genk vertelt waar je woont. Waar is où."),
    iv("Reken uit en schrijf het antwoord in het Frans: dix plus dix.", "vingt",
       "Dix is 10. 10 plus 10 is 20, en dat is vingt."),
    mk("Welke zin over een broer is juist en ontkennend?",
       ["Elle n'a pas de frère.", "Elle ne a pas de frère.", "Elle n'a pas un frère.", "Elle n'est pas de frère."], 2,
       "Ne wordt n' voor a, na pas komt de, en een broer hebben gaat met avoir."),
    wn("Tegen je oma zeg je vous, omdat je haar heel goed kent.", False,
       "Tegen familie en mensen die je goed kent, zeg je tu. Vous is voor volwassenen die je niet goed kent."),
    mk("Lees: 'Le samedi, je vais à la boulangerie à pied avec mon père.' Hoe gaan ze naar de bakker?",
       ["te voet", "met de fiets", "met de bus", "met de auto"], 2,
       "À pied betekent te voet. Met de fiets zou à vélo zijn."),
    mk("Welke kleur krijg je als je jaune en bleu mengt?",
       ["vert", "rouge", "gris", "rose"], 1,
       "Geel (jaune) en blauw (bleu) samen geeft groen: vert."),
    iv("Vul aan: 'Mes frères ... douze ans.' (zij hebben)", "ont",
       "Je leeftijd gaat met avoir. Mes frères is ils, en bij ils hoort ont."),
    wn("Bonne nuit zeg je als je 's morgens op school aankomt.", False,
       "Bonne nuit zeg je voor het slapengaan. 's Morgens zeg je bonjour."),
    mk("Welke zin gaat over het weer?",
       ["Il fait beau.", "Il a faim.", "Il est gentil.", "Il va à l'école."], 3,
       "Over het weer zegt het Frans il fait: il fait beau is het is mooi weer."),
    mk("Lees: 'Je m'appelle Anna. Je suis belge, mais je viens de France.' Wat klopt?",
       ["Anna is Belg maar komt uit Frankrijk.", "Anna is Frans en woont in België.",
        "Anna komt uit België en woont in Frankrijk.", "Anna is Belg en is nooit in Frankrijk geweest."], 1,
       "Je suis belge is ik ben Belg, je viens de France is ik kom uit Frankrijk. Mais is maar."),
    wn("In 'Les enfants jouent à la récréation' hoor je de -ent van jouent niet.", True,
       "De uitgang -ent schrijf je wel, maar je spreekt hem niet uit."),
    iv("Vul het lidwoord aan: 'Où est ... gare ?'", "la",
       "Gare is vrouwelijk, dus la gare: waar is het station?"),
    mk("Het is le 31 décembre. Welke maand begint morgen?",
       ["janvier", "novembre", "février", "juin"], 2,
       "Décembre is de laatste maand. Daarna begint het nieuwe jaar met janvier."),
    wn("'Tu vas' en 'tu as' betekenen hetzelfde.", False,
       "Tu vas komt van aller (jij gaat), tu as komt van avoir (jij hebt)."),
    mk("Welke zin betekent 'Mijn ouders zijn niet thuis'?",
       ["Mes parents ne sont pas à la maison.", "Mes parents n'ont pas à la maison.",
        "Mon parents ne sont pas à la maison.", "Mes parents sont pas à la maison."], 0,
       "Ouders zijn meer dan één, dus mes en sont. De ontkenning staat er rond: ne sont pas."),
]
