# -*- coding: utf-8 -*-
"""Launchpad WO: ik en de anderen (gevoelens, familie, vriendschap, school, feesten, regels)."""
from lp import K, I, W
import lpprent as P

TITEL = "Ik en de anderen"
UITLEG_1 = "Gevoelens, familie en vrienden."
UITLEG_2 = "Samen op school en samen feest vieren."

DEEL_1 = [
    K("Hoe voel je je als je een cadeau krijgt?", "blij", ["bang", "boos", "verdrietig"], "Een cadeau maakt je blij.", None),
    K("Hoe voel je je als je knuffel kwijt is?", "verdrietig", ["blij", "trots", "verrast"], "Iets kwijt zijn maakt je verdrietig.", None),
    K("Hoe voel je je als iemand je speelgoed afpakt?", "boos", ["blij", "moe", "trots"], "Dat voelt niet eerlijk: je wordt boos.", None),
    K("Hoe voel je je als je eindelijk kan fietsen zonder zijwieltjes?", "trots", ["bang", "verdrietig", "boos"], "Iets nieuws kunnen maakt je trots.", None),
    K("Wat doe je als een vriendje verdrietig is?", "vragen wat er is en troosten", ["uitlachen en het aan iedereen vertellen", "weglopen", "doen alsof je het niet ziet"], "Een goede vriend helpt.", None),
    K("Wat doe je als je boos bent?", "zeggen wat er is en rustig ademen", ["slaan", "dingen kapot gooien op de grond", "heel hard roepen naar iedereen"], "Boos zijn mag, maar je doet niemand pijn.", None),
    K("Wie hoort bij je familie?", "je broer", ["de buurman", "de juf", "de bakker"], "Je broer is familie.", None),
    K("Wie is de broer van je mama?", "je oom", ["je opa", "je neef", "je papa"], "De broer van je mama of papa is je oom.", None),
    K("Wie is de zus van je papa?", "je tante", ["je oma", "je nicht", "je mama"], "De zus van je papa of mama is je tante.", None),
    W("Iedereen voelt zich soms verdrietig.", True, "Verdriet hoort bij het leven."),
    W("Boos zijn mag, slaan mag ook.", False, "Boos zijn mag, maar slaan nooit."),
    W("Elke familie is anders.", True, "Groot of klein, met één of twee ouders: elke familie is anders."),
    W("Een vriend lacht je uit als je valt.", False, "Een vriend helpt je recht."),
    W("Sorry zeggen helpt om het goed te maken.", True, "Sorry zeggen toont dat je het jammer vindt."),
    W("Alleen kinderen kunnen bang zijn.", False, "Ook volwassenen zijn soms bang."),
    W("Je mag nee zeggen als iemand je aanraakt en je dat niet wil.", True, "Jouw lichaam is van jou."),
    W("Een vriend moet altijd op jou lijken.", False, "Vrienden kunnen heel verschillend zijn."),
    I("Mama, papa, jij en je zus wonen samen. Met hoeveel zijn jullie thuis? ___", 4, "Mama, papa, jij en je zus: 4.", 4),
    K("Wat zeg je als iemand je helpt?", "dank je wel", ["ga weg", "niets", "nog eens"], "Dank je wel zeggen is beleefd.", None),
    K("Wat zeg je als je iets wil vragen?", "mag ik ... alsjeblieft?", ["geef!", "nu!", "ik wil het"], "Alsjeblieft is beleefd.", None),
]

DEEL_2 = [
    K("Wat doe je in de klas als je iets wil zeggen?", "je vinger opsteken", ["roepen", "op de bank kloppen", "weglopen"], "Dan weet de juf dat je iets wil zeggen.", None),
    K("Wie helpt je op school als je iets niet weet?", "de juf of meester", ["de buurman", "niemand", "de bakker"], "De juf of meester legt het uit.", None),
    K("Wat doe je na het spelen met de blokken?", "opruimen", ["laten liggen", "weggooien", "verstoppen"], "Samen ruimen we op.", None),
    K("Wat doe je als je samen een spel speelt?", "om de beurt spelen", ["altijd zelf eerst", "de anderen niet laten meedoen", "vals spelen"], "Om de beurt is eerlijk.", None),
    K("Welk feest vieren veel mensen in december met een kerstboom?", "Kerstmis", ["Pasen", "Halloween", "carnaval"], "Met Kerstmis zet men een kerstboom.", None),
    K("Bij welk feest zoeken kinderen eieren?", "Pasen", ["Kerstmis", "Sinterklaas", "Nieuwjaar"], "Met Pasen zoeken kinderen paaseieren.", None),
    K("Wie brengt in België op 6 december cadeautjes?", "Sinterklaas", ["de paashaas", "de kerstman", "de tandenfee"], "Sinterklaas komt op 6 december.", None),
    K("Welk feest vieren moslims na de vastenmaand?", "het Suikerfeest", ["Pasen", "Kerstmis", "Halloween"], "Na de ramadan vieren moslims het Suikerfeest.", None),
    W("In de klas wacht je je beurt.", True, "Om de beurt praten is eerlijk."),
    W("In de klas mag iedereen tegelijk roepen.", False, "Dan hoort niemand iets. Je steekt je vinger op."),
    W("Mensen vieren niet allemaal dezelfde feesten.", True, "Elke familie heeft eigen feesten."),
    W("Met Pasen komt Sinterklaas.", False, "Sinterklaas komt op 6 december."),
    W("Regels op school helpen om samen goed te leven.", True, "Zo weet iedereen wat mag."),
    W("Je mag de spullen van een ander zomaar nemen.", False, "Je vraagt het eerst."),
    W("Een verjaardag vier je elk jaar.", True, "Elk jaar op dezelfde dag."),
    W("Pesten is een grapje.", False, "Pesten doet pijn. Zeg het aan een volwassene."),
    I("In je klas zitten 10 jongens en 10 meisjes. Hoeveel kinderen zijn dat samen? ___", 20, "10 + 10 = 20.", 20),
    K("Wat doe je als iemand gepest wordt?", "het aan de juf of meester zeggen", ["meelachen met de anderen", "meedoen", "niets zeggen tegen niemand"], "Een volwassene kan helpen.", None),
    K("Waar woon je samen met heel veel mensen?", "in een gemeente of stad", ["in een kast", "in een tent helemaal alleen", "op de maan"], "In je gemeente wonen veel mensen samen.", None),
    K("Wie zorgt in je gemeente voor de straten en de school?", "de burgemeester en de gemeente", ["de tandarts", "de kapper in de winkelstraat", "je knuffel"], "Het gemeentehuis regelt veel voor iedereen.", None),
]

PRENT_1 = [
    K("Wat doen de kinderen?", "samen spelen en delen", ["ruzie maken om de blokken", "slapen", "eten"], "Ze bouwen samen met blokken en geven elkaar iets door.", None, prent=P.een("samen-delen", "lp-delen")),
    K("Wat doet de jongen?", "hij troost het meisje", ["hij lacht haar luid uit", "hij loopt weg", "hij duwt haar"], "Het meisje is gevallen. De jongen helpt haar.", None, prent=P.een("samen-troosten", "lp-sorry")),
    I("Hoeveel mensen zie je op de prent?", 4, "Papa, mama en twee kinderen: 4. De hond is geen mens.", 4, prent=P.een("samen-gezin", "lp-gezin")),
    W("Op een verjaardag word je een jaar ouder.", True, "Elk jaar op je verjaardag.", prent=P.een("samen-verjaardag", "lp-verjaardag")),
]
PRENT_2 = [
    K("Bij welk feest hoort deze boom?", "Kerstmis", ["Pasen", "Sinterklaas", "carnaval"], "Met Kerstmis zet men een kerstboom.", None, prent=P.een("samen-kerstboom", "kerstboom")),
    K("Bij welk feest horen deze eieren?", "Pasen", ["Kerstmis", "Halloween", "Nieuwjaar"], "Met Pasen zoeken kinderen paaseieren.", None, prent=P.een("samen-paaseieren", "paaseieren")),
    W("Op de prent zie je geen huisdier.", False, "Er zit een hond bij het gezin.", prent=P.een("samen-gezin-hond", "lp-gezin")),
    W("Dit is het gemeentehuis, waar de burgemeester werkt.", True, "In het gemeentehuis werkt het bestuur van de gemeente.", prent=P.een("samen-gemeentehuis", "gemeentehuis")),
]
