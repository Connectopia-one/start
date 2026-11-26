# -*- coding: utf-8 -*-
"""Ready Nederlands: Lezen en woordenschat (korte teksten begrijpen, hoofdgedachte,
tussen de regels lezen, woorden in hun zin begrijpen, synoniemen, tegenstellingen,
samenstellingen). Elke vraag brengt haar eigen stukje tekst mee. Eigen teksten."""
from vr import mk, inv, wn

TITEL = "Lezen en woordenschat"
UITLEG_1 = 'Een tekst goed lezen.'
UITLEG_2 = 'Woorden die hetzelfde of het omgekeerde betekenen.'

T1 = "Tekst: 'Elke zaterdag gaat Ruben met opa vissen aan de vijver. Opa neemt koffie mee, Ruben warme chocomelk. Vorige week vingen ze niets, maar Ruben vond het toch fijn, want opa vertelde de hele tijd grappige verhalen.' "
T2 = "Tekst: 'Egels slapen in de winter. In de herfst eten ze veel slakken, wormen en kevers. Zo maken ze een dikke laag vet. Daarna kruipen ze onder een hoop bladeren. Daar slapen ze tot de lente.' "

DEEL_1 = [
    mk(T1 + "Wanneer gaan Ruben en opa vissen?", ["elke zondag", "elke zaterdag", "elke dag", "in de vakantie"], 1, "In de eerste zin staat: elke zaterdag."),
    mk(T1 + "Wat drinkt Ruben?", ["koffie", "water", "warme chocomelk", "limonade"], 2, "Opa drinkt koffie, Ruben warme chocomelk."),
    wn(T1 + "Ruben en opa vingen vorige week veel vissen.", False, "In de tekst staat: vorige week vingen ze niets."),
    mk(T1 + "Waarom vond Ruben het toch fijn?", ["Hij ving een grote vis.", "Opa vertelde grappige verhalen.", "Het was mooi weer.", "Hij kreeg een ijsje."], 1, "Er staat: 'want opa vertelde de hele tijd grappige verhalen'."),
    wn(T1 + "Ruben vindt het gezellig bij opa.", True, "Ook al vingen ze niets, hij vond het fijn. Dat lees je tussen de regels."),
    mk(T2 + "Waarover gaat de tekst vooral?", ["over slakken", "over de winterslaap van egels", "over de lente", "over bladeren"], 1, "De hele tekst vertelt hoe egels zich klaarmaken voor de winter en slapen."),
    mk(T2 + "Waarom eten egels veel in de herfst?", ["om sneller te lopen", "om een laag vet te maken", "omdat ze dan honger hebben", "om slakken weg te halen"], 1, "Er staat: zo maken ze een dikke laag vet."),
    inv(T2 + "Tot wanneer slapen egels? Tot de ___.", "lente", "In de laatste zin staat: tot de lente."),
    wn(T2 + "Egels slapen in de winter in een boom.", False, "Ze kruipen onder een hoop bladeren."),
    mk("In de zin 'Na de lange wandeling was Mila uitgeput' betekent uitgeput ...", ["heel blij", "heel moe", "heel boos", "heel snel"], 1, "Na een lange wandeling ben je moe. Uitgeput betekent heel moe."),
    mk("In de zin 'De taart was verrukkelijk, iedereen wou nog een stuk' betekent verrukkelijk ...", ["heel lekker", "heel groot", "te zoet", "heel oud"], 0, "Iedereen wou nog een stuk, dus de taart was heel lekker."),
    inv("Wat is het tegenovergestelde van 'groot'? ___", "klein", "Groot en klein zijn tegenstellingen."),
    mk("Welk woord betekent hetzelfde als 'snel'?", ["traag", "vlug", "luid", "zwaar"], 1, "Snel en vlug betekenen hetzelfde: het zijn synoniemen."),
    wn("'Lachen' en 'huilen' zijn synoniemen.", False, "Ze betekenen net het omgekeerde. Het zijn tegenstellingen."),
    mk("Welke samenstelling maak je met 'tand' en 'borstel'?", ["borsteltand", "tandborstel", "tandenborstelen", "tandarts"], 1, "Tand + borstel = tandborstel."),
    inv("Wat is het tegenovergestelde van 'open'? ___", ["dicht", "toe", "gesloten"], "Open en dicht (of toe) zijn tegenstellingen."),
    mk("In de zin 'Het hondje rilde van de kou' betekent rillen ...", ["blaffen", "beven", "springen", "slapen"], 1, "Van de kou ga je beven. Rillen betekent beven."),
    wn("'Mooi' en 'prachtig' betekenen ongeveer hetzelfde.", True, "Prachtig is heel mooi. Het zijn synoniemen."),
    mk("Welk woord past niet in de rij: appel, peer, wortel, banaan?", ["appel", "peer", "wortel", "banaan"], 2, "Een wortel is een groente, de andere zijn fruit."),
    wn("'Zonnebril' is een samenstelling van 'zon' en 'bril'.", True, "Zon + bril = zonnebril. Er komt een tussenletter n bij."),
]

T3 = "Tekst: 'Vandaag is het de verjaardag van Lotte. Ze wordt negen. Haar vriendin Amira komt als eerste aan, met een cadeautje in roze papier. In het pakje zit een boek over paarden. Lotte springt een gat in de lucht.' "
T4 = "Mededeling op de schoolpoort: 'Op vrijdag 12 maart is er geen school. De juffen en meesters volgen dan een opleiding. De opvang is wel open van 7 tot 18 uur.' "

DEEL_2 = [
    mk(T3 + "Hoe oud wordt Lotte?", ["acht", "negen", "tien", "zeven"], 1, "Er staat: ze wordt negen."),
    mk(T3 + "Wat zit er in het pakje?", ["een pop", "een boek over paarden", "een paard", "roze papier"], 1, "In het pakje zit een boek over paarden. Het roze papier is de verpakking."),
    wn(T3 + "Amira komt als laatste aan.", False, "Er staat: ze komt als eerste aan."),
    mk(T3 + "Wat betekent 'Lotte springt een gat in de lucht'?", ["Lotte springt op het bed.", "Lotte is heel blij.", "Lotte valt.", "Lotte is bang."], 1, "Een gat in de lucht springen betekent heel blij zijn."),
    wn(T3 + "Lotte houdt waarschijnlijk van paarden.", True, "Haar vriendin geeft een boek over paarden en Lotte is heel blij. Dat lees je tussen de regels."),
    mk(T4 + "Waarom is er geen school?", ["Het is vakantie.", "De juffen en meesters volgen een opleiding.", "De school is gesloten door sneeuw.", "Het is een feestdag."], 1, "Dat staat in de tweede zin."),
    inv(T4 + "Tot hoe laat is de opvang open? Tot ___ uur.", "18", "Er staat: van 7 tot 18 uur.", 18),
    wn(T4 + "Op 12 maart kunnen kinderen naar de opvang.", True, "De opvang is wel open."),
    mk(T4 + "Voor wie is deze mededeling vooral bedoeld?", ["voor de ouders", "voor de buren", "voor de bakker", "voor de postbode"], 0, "Ouders moeten weten dat er geen school is en dat de opvang open is."),
    mk("Wat betekent 'Hij heeft twee linkerhanden'?", ["Hij heeft twee linkse handen.", "Hij is niet handig.", "Hij is linkshandig.", "Hij is heel sterk."], 1, "Wie twee linkerhanden heeft, kan niet goed iets maken of herstellen."),
    mk("Wat betekent 'Ze is zo stil als een muis'?", ["Ze piept.", "Ze is heel stil.", "Ze is klein.", "Ze eet kaas."], 1, "Een muis maakt weinig lawaai. Zo stil als een muis betekent heel stil."),
    wn("'Iemand de les lezen' betekent dat je iemand voorleest uit een boek.", False, "Het betekent dat je iemand streng zegt wat die fout deed."),
    inv("Wat is het tegenovergestelde van 'vroeg'? ___", "laat", "Vroeg en laat zijn tegenstellingen."),
    mk("Welk woord is een synoniem van 'beginnen'?", ["stoppen", "starten", "wachten", "eindigen"], 1, "Beginnen en starten betekenen hetzelfde."),
    inv("Maak een samenstelling: regen + jas = ___", "regenjas", "Regen + jas = regenjas."),
    mk("In de zin 'De reus was enorm, hij paste niet door de deur' betekent enorm ...", ["heel groot", "heel klein", "heel lief", "heel snel"], 0, "Hij paste niet door de deur: dan is hij heel groot."),
    wn("'Dapper' en 'moedig' zijn synoniemen.", True, "Allebei betekenen ze: niet bang zijn om iets moeilijks te doen."),
    mk("Welk woord hoort bij de groep: hamer, zaag, schroevendraaier, ...?", ["vork", "tang", "pan", "lepel"], 1, "Een tang is ook gereedschap. Vork, pan en lepel gebruik je in de keuken."),
    wn("Een titel vertelt vaak waarover een tekst gaat.", True, "Lees eerst de titel. Zo weet je al een beetje wat je gaat lezen."),
    wn("Bij een moeilijk woord stop je best meteen met lezen.", False, "Lees verder: de zinnen errond helpen je vaak om het woord te begrijpen."),
]
