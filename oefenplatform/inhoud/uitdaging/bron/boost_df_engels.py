# -*- coding: utf-8 -*-
"""Uitdaging Engels 🚀 Boost dubbele finaliteit (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die alle hoofdstukken
door elkaar halen, van tekstanalyse en tekstsoorten tot woordenschat,
grammatica, uitspraak en de Engelstalige wereld. Een verzonnen mededeling en
zes losse zinnen om op te klikken, tabellen, keuzelijsten, slepen, koppelen,
sorteren, volgorde, een casus en een korte schrijfopdracht. Geen nieuwe
leerstof: alles staat in de hoofdstukken van dit vak.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_df_engels.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Engels"
BESTAND = "boost-df-engels-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/engels-boost-df-uitdaging"
ZWEMBAD = "mededeling-zwembad.svg"
ZINNEN = "zes-zinnen.svg"
Z = {1: [2, 13.4, 96, 13.7], 2: [2, 27.1, 96, 13.7], 3: [2, 40.8, 96, 13.7],
     4: [2, 54.5, 96, 13.7], 5: [2, 68.2, 96, 13.7], 6: [2, 81.8, 96, 13.7]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Mededeling van het zwembad
    klik("Lees de mededeling van het zwembad. Klik op de zin die zegt waarom het zwembad dichtgaat.",
         ZWEMBAD, [Z[2]],
         "'Because' kondigt een oorzaak aan: de oude verwarming is kapot en moet vervangen worden."),
    klik("Klik op de zin met een tegenstelling.",
         ZWEMBAD, [Z[5]],
         "'However' kondigt een tegenstelling aan: je kan in het andere zwembad zwemmen, maar er is geen duikplank."),
    klik("Klik op de zin die zegt wat je moet meebrengen.",
         ZWEMBAD, [Z[4]],
         "'Please bring your Parkside card' vraagt je om je kaart mee te nemen, anders betaal je twee keer."),
    klik("Je wil tijdens de sluiting toch zwemmen. Klik op de zin die zegt waar dat kan.",
         ZWEMBAD, [Z[3]],
         "Tijdens de twee weken kan je in het Lakeview Centre zwemmen."),
    met_prent(ZWEMBAD, tabel(
        "Klopt dit volgens de mededeling?",
        [
            ("Het zwembad is twee weken dicht.", J),
            ("In het Lakeview Centre kan je ook duiken van een plank.", F),
            ("Het zwembad gaat dicht door een lek in het dak.", F),
        ],
        "Van 6 tot 19 april is twee weken. Het Lakeview Centre heeft geen duikplank. De oorzaak is de kapotte verwarming, niet het dak.")),
    met_prent(ZWEMBAD, keuze(
        "Deze tekst is vooral een [[*informatieve|narratieve|persuasieve]] tekst. Het woord 'it' in zin 2 verwijst naar [[*the old heating system|the pool]].",
        "De tekst geeft informatie over een sluiting. 'It' verwijst naar het laatst genoemde ding dat vervangen moet worden: de verwarming.")),

    # Zes zinnen
    klik("Bekijk de zes zinnen. Klik op de zin die fout is door 'since' en 'for'.",
         ZINNEN, [Z[1]],
         "Bij een duur gebruik je 'for': She has lived in Leeds for three years. 'Since' staat bij een beginpunt, zoals since 2020."),
    klik("Klik op de zin met een fout meervoud.",
         ZINNEN, [Z[4]],
         "Het meervoud van 'child' is onregelmatig: children."),
    klik("Klik op de zin met een fout in de overtreffende trap.",
         ZINNEN, [Z[5]],
         "Bij een kort woord als 'tall' gebruik je -est: the tallest boy. 'Most' gebruik je bij lange woorden."),
    met_prent(ZINNEN, tabel(
        "Welke tijd staat er in deze zin?",
        [
            ("zin 2", "present simple"),
            ("zin 3", "past simple"),
            ("zin 6", "will-toekomst"),
        ],
        "'Doesn't like' is present simple, 'went' is de past simple van 'go' en 'will call' is de toekomst met will.",
        kolommen=["present simple", "past simple", "will-toekomst"])),

    # Tekstsoorten en tekstverbanden
    tabel(
        "Welke tekstsoort hoort bij elk van deze vier korte Engelse zinnen?",
        [
            ("'Mix the flour and the eggs, then bake for twenty minutes.'", "prescriptief"),
            ("'Save water: take a shower instead of a bath!'", "persuasief"),
            ("'Last summer I got lost in the woods with my dog.'", "narratief"),
            ("'The museum is open from Tuesday to Sunday.'", "informatief"),
        ],
        "Een recept zegt wat je moet doen. Een campagne wil je overtuigen. Een verhaal vertelt wat er gebeurde. Openingsuren geven informatie.",
        kolommen=["informatief", "persuasief", "prescriptief", "narratief"]),
    koppel(
        "Koppel het signaalwoord aan het verband dat het aankondigt.",
        [
            ["because", "oorzaak"],
            ["so", "gevolg"],
            ["however", "tegenstelling"],
            ["for example", "voorbeeld"],
        ],
        ["tijd"],
        "Signaalwoorden maken het verband tussen zinnen zichtbaar."),
    mk("'Although it was raining, we went for a walk.' Wat doet 'although' in deze zin?",
       ["Het geeft een tegenstelling aan: de regen hield ons niet tegen",
        "Het geeft de oorzaak aan waarom we gingen wandelen in de regen",
        "Het geeft een gevolg aan van het slechte weer van die middag",
        "Het geeft de tijd aan waarop we die dag vertrokken voor de wandeling"],
       0,
       "'Although' betekent 'hoewel'. Je verwacht dat regen je binnen houdt, maar toch ga je wandelen."),

    # Woordenschat
    koppel(
        "Koppel het Britse woord aan het Amerikaanse.",
        [
            ["lift", "elevator"],
            ["flat", "apartment"],
            ["holiday", "vacation"],
            ["autumn", "fall"],
        ],
        ["subway"],
        "Brits en Amerikaans Engels hebben soms andere woorden voor hetzelfde ding."),
    sorteer(
        "Bij welk woordveld hoort dit woord?",
        ["gezondheid", "reizen", "school"],
        [
            ["sore throat", "gezondheid"],
            ["return ticket", "reizen"],
            ["primary school", "school"],
            ["delayed", "reizen"],
            ["headache", "gezondheid"],
        ],
        "Woorden leer je best per woordveld: wat bij de dokter hoort, wat bij een treinreis hoort, wat op school hoort."),
    keuze(
        "De zoon van je zus is je [[*nephew|niece|cousin]]. 'A fortnight' duurt [[*two weeks|four weeks]].",
        "Een nephew is een neef (zoon van je broer of zus), een niece een nicht. Een fortnight is veertien dagen."),
    mk("In een Britse winkel hangt het bordje 'Please queue here.' Wat doe je?",
       ["Je gaat netjes in de rij staan en wacht op je beurt",
        "Je vraagt hier om hulp aan een medewerker van de winkel",
        "Je betaalt hier meteen aan de kassa zonder te wachten",
        "Je laat hier je tas achter tot je klaar bent met winkelen"],
       0,
       "'Queue' betekent een rij. In het Verenigd Koninkrijk wacht je netjes je beurt af."),

    # Grammatica
    inv("Vul de past simple in: Yesterday I … (write) a letter to my aunt.",
        ["wrote"],
        "'Write' is onregelmatig: write, wrote, written."),
    keuze(
        "I have known her [[*for|since]] ten years. We have lived here [[*since|for]] 2019.",
        "'For' staat bij een duur, 'since' bij een beginpunt."),
    tabel(
        "Is deze Engelse zin grammaticaal juist?",
        [
            ("Who wants a cup of tea?", J),
            ("Did you was at home yesterday?", F),
            ("She doesn't play the piano.", J),
            ("I am knowing the answer.", F),
        ],
        "Vraag je met 'who' naar het onderwerp, dan komt er geen 'do'. Bij 'to be' gebruik je geen 'did': Were you at home? 'Know' zet je niet in de -ing-vorm."),
    sleep(
        "While we [[were]] waiting for the bus, it [[started]] to rain.",
        ["was", "starts"],
        "De langere handeling staat in de past continuous (were waiting), de korte handeling die ze onderbreekt in de past simple (started)."),
    volgorde(
        "Zet de woorden in de juiste volgorde voor een vraag.",
        ["Does", "your brother", "play", "tennis", "on Saturdays?"],
        "Een vraag in de present simple: does + onderwerp + werkwoord + de rest."),
    mk("Welk woord vul je in? I don't have … money left.",
       ["much", "many", "a few", "few of"],
       0,
       "'Money' is ontelbaar, dus gebruik je 'much'. 'Many' en 'a few' staan bij telbare woorden."),
    keuze(
        "Voor 'hour' zet je [[*an|a]], want de h hoor je niet. 'The cat licked [[*its|it's]] paw.'",
        "'An' staat voor een klinkerklank. 'Its' is bezittelijk, 'it's' is de korte vorm van 'it is'."),
    inv("Schrijf het bijwoord bij 'careful'. Eén woord.",
        ["carefully"],
        "Het bijwoord maak je met -ly: careful wordt carefully."),
    mk("Waar staat de komma? Kies de juiste zin.",
       ["When the film ended, we went home.",
        "When the film ended we, went straight home.",
        "When, the film ended we went home.",
        "When the film, ended we went home."],
       0,
       "Staat de bijzin vooraan, dan komt de komma tussen de bijzin en de hoofdzin."),

    inv("Schrijf het meervoud van 'woman'. Eén woord.",
        ["women"],
        "'Woman' heeft een onregelmatig meervoud: women."),
    keuze(
        "This is the girl [[*whose|who]] bike was stolen. The man [[*who|which]] lives next door is a doctor.",
        "'Whose' wijst op bezit. Bij personen gebruik je 'who', bij dingen 'which'."),
    tabel(
        "Kijkt deze zin vooruit naar de toekomst?",
        [
            ("I think it will rain tomorrow.", J),
            ("We went to Paris last year.", F),
            ("I'll help you with your homework later.", J),
        ],
        "'Will' en de korte vorm 'll' maken de toekomende tijd. 'Went' is verleden tijd."),
    mk("'He has hardly slept.' Wat betekent dat?",
       ["Hij heeft bijna niet geslapen",
        "Hij heeft heel hard en diep geslapen",
        "Hij heeft veel te lang en te laat geslapen",
        "Hij heeft eindelijk een hele nacht geslapen"],
       0,
       "'Hardly' betekent bijna niet. Het heeft niets met 'hard' te maken."),
    sleep(
        "In the United Kingdom, 'the [[ground floor]]' is the floor at street level. You buy newspapers and sweets at the [[newsagent]].",
        ["first floor", "estate agent"],
        "De ground floor is het gelijkvloers. Bij de newsagent koop je kranten en snoep; een estate agent verkoopt huizen."),

    # Uitspraak en spelling
    tabel(
        "Klopt dit over uitspraak en spelling?",
        [
            ("In 'island' spreek je de s niet uit.", J),
            ("De dagen van de week schrijf je met een kleine letter.", F),
            ("Het meervoud van 'leaf' is 'leaves'.", J),
        ],
        "De s in island is stom. Dagen van de week krijgen in het Engels een hoofdletter. Sommige woorden op -f krijgen -ves."),
    keuze(
        "In 'computer' ligt de klemtoon op de [[*tweede|eerste|derde]] lettergreep. 'They're' is de korte vorm van [[*they are|there is]].",
        "com-PU-ter. 'Their', 'there' en 'they're' klinken gelijk, maar betekenen iets anders."),

    # Gesprekken en conventies
    koppel(
        "Koppel de situatie aan de gepaste reactie.",
        [
            ["Iemand zegt: 'I'm sorry I'm late.'", "Don't worry, we've only just started."],
            ["Je volgt je gesprekspartner niet.", "Could you speak a bit more slowly, please?"],
            ["Je wil iemand uitnodigen.", "Would you like to come to my party?"],
        ],
        ["Yours faithfully."],
        "Een gepaste reactie past bij de situatie en bij het register."),
    keuze(
        "Je begint een mail aan iemand die je niet kent met [[*Dear Sir or Madam|Hi mate]]. Je sluit die mail af met [[*Yours faithfully|Yours sincerely]].",
        "Ken je de naam niet, dan schrijf je Dear Sir or Madam en Yours faithfully. Ken je de naam wel, dan Yours sincerely."),
    sorteer(
        "Is dit een landsdeel van het Verenigd Koninkrijk?",
        ["wel", "niet"],
        [
            ["Wales", "wel"],
            ["Scotland", "wel"],
            ["Northern Ireland", "wel"],
            ["the Republic of Ireland", "niet"],
        ],
        "Het Verenigd Koninkrijk bestaat uit Engeland, Schotland, Wales en Noord-Ierland. De Republiek Ierland is een apart land."),

    # Examen
    mk("Je krijgt punten voor taakvoltooiing bij een mondelinge opdracht in het Engels. Waarop let de examinator dan?",
       ["Of je doet wat de opdracht vraagt, met alle gevraagde info",
        "Je spreekt zonder één fout in de grammatica of in de uitspraak",
        "Je gebruikt zo veel mogelijk moeilijke woorden in je antwoord",
        "Je spreekt zo lang mogelijk, ook over andere onderwerpen erbij"],
       0,
       "Taakvoltooiing kijkt of je de opdracht echt uitvoert: alles wat gevraagd is, staat in je antwoord."),

    casus(
        "Lees deze mail: 'Hi Sam, thanks for the photos of your trip to Scotland! They're great. I've never been there, but I'd love to go. Could you tell me which city you liked best and how long the train journey took? Speak soon, Jo'",
        [
            mk("Welke soort tekst schreef Jo aan Sam?",
               ["Een informele mail aan een vriend", "Een zakelijke brief aan een bedrijf", "Een persuasieve campagnetekst over reizen", "Een prescriptieve tekst met een stappenplan"],
               0,
               "'Hi', 'thanks' en 'Speak soon' tonen een informeel register tussen vrienden."),
            tabel(
                "Klopt dit volgens de mail van Jo aan Sam?",
                [
                    ("Jo is al eens in Schotland geweest.", F),
                    ("Jo stelt Sam twee vragen.", J),
                    ("Sam reisde met de trein.", J),
                ],
                "'I've never been there' zegt dat Jo er nooit was. Jo vraagt welke stad Sam het mooist vond en hoe lang de treinreis duurde."),
        ]),

    open_("Schrijf een kort antwoord van Sam aan Jo (drie à vier zinnen in het Engels). Beantwoord beide vragen uit de mail en sluit gepast af.",
          "Hi Jo, thanks for your message! I liked Edinburgh best, because the old town is beautiful. The train journey from London took about four and a half hours. You should go there next summer! Bye, Sam",
          "Een goed antwoord beantwoordt beide vragen (welke stad en hoe lang de reis duurde), gebruikt een informeel register en sluit gepast af."),
]
