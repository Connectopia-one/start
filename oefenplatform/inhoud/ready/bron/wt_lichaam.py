# -*- coding: utf-8 -*-
"""Ready wetenschap en techniek: Mijn lichaam (zintuigen, skelet en spieren, hart en
longen, gezond leven: voeding, beweging, slaap, hygiëne). Doelen einde 4de leerjaar."""
from vr import mk, inv, wn

TITEL = "Mijn lichaam"
UITLEG_1 = "Je vijf zintuigen, je botten en spieren."
UITLEG_2 = "Hart, longen en gezond leven."

DEEL_1 = [
    mk("Met welk zintuig proef je?", ["neus", "tong", "oor", "huid"], 1, "Met je tong proef je zoet, zout, zuur en bitter."),
    inv("Hoeveel zintuigen heb je? ___", "5", "Zien, horen, ruiken, proeven en voelen: vijf zintuigen.", 5),
    mk("Met welk zintuig hoor je een vogel fluiten?", ["ogen", "oren", "neus", "tong"], 1, "Geluid vang je op met je oren."),
    mk("Welk zintuig gebruik je om te voelen of water warm is?", ["je huid", "je ogen", "je oren", "je neus"], 0, "Met je huid voel je warm en koud, zacht en ruw."),
    wn("Als je verkouden bent, proef je minder goed.", True, "Ruiken en proeven werken samen. Met een verstopte neus proef je minder."),
    wn("Je mag recht in de zon kijken, dat is goed voor je ogen.", False, "Recht in de zon kijken kan je ogen beschadigen."),
    mk("Wat beschermt je hersenen?", ["je ribben", "je schedel", "je knie", "je ruggengraat"], 1, "De schedel is een harde doos van bot rond je hersenen."),
    mk("Wat beschermen je ribben?", ["je hart en longen", "je voeten", "je oren", "je tanden"], 0, "De ribben vormen een kooi rond je hart en longen."),
    inv("Al je botten samen noem je je ___. (s...)", ["skelet", "geraamte"], "Het skelet geeft je lichaam stevigheid en vorm."),
    wn("Spieren zorgen ervoor dat je kan bewegen.", True, "Spieren trekken aan je botten. Zo kan je lopen, springen en zwaaien."),
    mk("Hoe heet de plaats waar twee botten samenkomen en je kan buigen?", ["een gewricht", "een spier", "een pees", "een nagel"], 0, "Je knie, elleboog en schouder zijn gewrichten."),
    wn("Een baby heeft geen botten.", False, "Een baby heeft wel botten. Ze zijn nog zacht en groeien mee."),
    mk("Waarom is het goed om veel te bewegen?", ["Je spieren en botten worden sterker.", "Je wordt er moe van en dat is altijd slecht.", "Je hebt dan geen eten meer nodig.", "Je groeit er niet meer van."], 0, "Bewegen maakt je spieren, botten en hart sterker."),
    mk("Wat is de ruggengraat?", ["een rij botjes in je rug", "een spier in je buik", "een bot in je arm", "een deel van je schedel"], 0, "De ruggengraat bestaat uit veel kleine wervels op elkaar."),
    inv("Met je ___ zie je kleuren en vormen.", ["ogen", "oog"], "Je ogen vangen licht op."),
    wn("Je huid is ook een zintuig.", True, "Met je huid voel je, dus het is een zintuig."),
    mk("Waarom draag je een fietshelm?", ["om je hoofd te beschermen als je valt", "om sneller en verder te fietsen dan je vrienden", "tegen de regen", "omdat het mooi staat"], 0, "Een helm beschermt je schedel en hersenen."),
    wn("Luide muziek kan je oren beschadigen.", True, "Te luid geluid kan je gehoor voor altijd beschadigen."),
    mk("Met welk zintuig merk je dat er iets aanbrandt in de keuken?", ["je neus", "je tong", "je oren", "je vingers"], 0, "Je ruikt de brandgeur met je neus."),
    wn("Botten kunnen niet breken.", False, "Botten zijn stevig, maar bij een harde val kunnen ze breken. Ze groeien dan weer aan elkaar."),
]

DEEL_2 = [
    mk("Wat doet je hart?", ["Het pompt bloed door je lichaam.", "Het maakt nieuwe lucht voor je longen.", "Het verteert je eten.", "Het laat je denken."], 0, "Je hart is een spier die bloed rondpompt."),
    mk("Waarmee adem je?", ["maag", "longen", "lever", "hart"], 1, "Met je longen adem je zuurstof in."),
    wn("Na het lopen klopt je hart sneller.", True, "Je spieren hebben dan meer zuurstof nodig, dus pompt je hart sneller."),
    inv("Je voelt je hartslag aan je ___. (p...)", ["pols", "polsen"], "Leg twee vingers tegen de binnenkant van je pols."),
    mk("Welk eten is goed om veel van te eten?", ["groenten en fruit", "chips met een sausje", "snoep", "frisdrank"], 0, "Groenten en fruit geven je vitaminen."),
    wn("Water is de beste dorstlesser.", True, "Water heeft geen suiker en lest je dorst het best."),
    mk("Hoe lang slaapt een kind van 9 jaar best per nacht?", ["4 uur", "6 uur", "ongeveer 10 uur", "15 uur"], 2, "Kinderen hebben ongeveer 9 tot 11 uur slaap nodig."),
    wn("Je moet je handen wassen voor je eet en na het toiletbezoek.", True, "Zo spoel je bacteriën en virussen weg."),
    mk("Hoe vaak poets je best je tanden?", ["één keer per week", "twee keer per dag", "nooit", "enkel bij de tandarts"], 1, "Poets 's morgens en 's avonds, twee minuten."),
    wn("Snoep is goed voor je tanden.", False, "Suiker zorgt net voor gaatjes in je tanden."),
    mk("Waar gaat je eten eerst naartoe nadat je het doorgeslikt hebt?", ["naar je longen", "naar je maag", "naar je hart", "naar je hoofd"], 1, "Via de slokdarm gaat het naar je maag."),
    inv("Als je niest, hou je best je ___ voor je mond of nies je in je elleboog. (h...)", ["hand", "handen"], "Zo verspreid je minder ziektekiemen. In je elleboog is het nog beter."),
    wn("Frisdrank is gezonder dan water.", False, "Frisdrank bevat veel suiker. Water is gezonder."),
    mk("Wat doe je als je je gesneden hebt en het bloedt een beetje?", ["de wonde schoonmaken en een pleister erop", "er zand op doen", "niets zeggen en gewoon verder spelen met vuile handen", "de wonde openkrabben"], 0, "Spoel de wonde, ontsmet ze en plak er een pleister op."),
    mk("Waarom is ontbijten belangrijk?", ["Je krijgt energie voor de dag.", "Dan hoef je de hele dag niet meer te drinken.", "Dan word je moe.", "Het is niet belangrijk."], 0, "Na een lange nacht heeft je lichaam energie nodig."),
    wn("Voor een gezond lichaam heb je enkel goed eten nodig, bewegen hoeft niet.", False, "Gezond leven is gezond eten, veel bewegen én genoeg slapen."),
    inv("Lucht met zuurstof adem je in via je neus en je ___.", ["mond"], "Je ademt in via je neus of mond, en de lucht gaat naar je longen."),
    mk("Wat is een gezond tussendoortje?", ["een appel", "een zak chips", "een reep chocolade", "een blikje cola"], 0, "Fruit is een gezond tussendoortje."),
    wn("Te lang naar een scherm kijken voor het slapengaan kan je slaap verstoren.", True, "Het licht van een scherm houdt je wakker. Leg het een uur voor je gaat slapen weg."),
    wn("Je bloed blijft altijd op dezelfde plaats in je lichaam.", False, "Je bloed stroomt de hele tijd rond door je bloedvaten."),
]
