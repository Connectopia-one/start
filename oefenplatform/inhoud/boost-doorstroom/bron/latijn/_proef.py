# -*- coding: utf-8 -*-
import sys, json
import pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parents[3]))
from uitdaging.bron._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_

LATIJN = """Gallia est omnis divisa in partes tres, quarum unam incolunt Belgae, aliam Aquitani, tertiam qui ipsorum lingua Celtae, nostra Galli appellantur. Hi omnes lingua, institutis, legibus inter se differunt. Gallos ab Aquitanis Garumna flumen, a Belgis Matrona et Sequana dividit. Horum omnium fortissimi sunt Belgae, propterea quod a cultu atque humanitate provinciae longissime absunt, minimeque ad eos mercatores saepe commeant atque ea quae ad effeminandos animos pertinent important, proximique sunt Germanis, qui trans Rhenum incolunt, quibuscum continenter bellum gerunt. Qua de causa Helvetii quoque reliquos Gallos virtute praecedunt, quod fere cotidianis proeliis cum Germanis contendunt, cum aut suis finibus eos prohibent aut ipsi in eorum finibus bellum gerunt. Eorum una pars, quam Gallos obtinere dictum est, initium capit a flumine Rhodano, continetur Garumna flumine, Oceano, finibus Belgarum, attingit etiam ab Sequanis et Helvetiis flumen Rhenum, vergit ad septentriones. Belgae ab extremis Galliae finibus oriuntur, pertinent ad inferiorem partem fluminis Rheni, spectant in septentrionem et orientem solem. Aquitania a Garumna flumine ad Pyrenaeos montes et eam partem Oceani quae est ad Hispaniam pertinet; spectat inter occasum solis et septentriones."""

VRAGEN = [
    mk("In hoeveel delen verdeelt Caesar Gallië in de eerste zin?",
       ["twee delen", "drie delen", "vier delen", "vijf delen"], 1,
       "Gallia est omnis divisa in partes tres: Gallië is in zijn geheel verdeeld in drie delen."),
    koppel("Koppel elk volk aan wat Caesar erover zegt.",
           [["Belgae", "wonen het verst van de provincie en zijn de dappersten"],
            ["Aquitani", "wonen tussen de Garonne en de Pyreneeën"],
            ["Celtae", "heten bij de Romeinen Galli"],
            ["Helvetii", "vechten bijna dagelijks met de Germanen"]],
           ["wonen in de Romeinse provincie"],
           "Caesar stelt de drie volken voor en zegt van de Helvetii dat ze de andere Galliërs in dapperheid overtreffen."),
    mk("Determineer divisa in Gallia est omnis divisa.",
       ["participium perfectum passief, nom. vrouwelijk enkelvoud",
        "participium praesens actief, nominativus vrouwelijk enkelvoud",
        "perfectum indicativus actief, derde persoon enkelvoud",
        "participium perfectum passief, ablativus vrouwelijk enkelvoud"], 0,
       "Divisa komt van dividere, verdelen, en hoort bij Gallia. Je kan est divisa lezen als een perfectum passief (is verdeeld), of divisa als een naamwoordelijk deel bij est (is verdeeld, toestand). Allebei is goed: de vorm blijft een participium perfectum passief."),
    mk("Naar welk woord verwijst quarum in quarum unam incolunt Belgae?",
       ["naar Gallia", "naar partes", "naar Belgae", "naar tres"], 1,
       "Quarum is een genitivus meervoud vrouwelijk. Het verwijst naar partes: waarvan de Belgen er één bewonen."),
    mk("Wat betekent nostra in qui ipsorum lingua Celtae, nostra Galli appellantur?",
       ["in onze taal, dus in het Latijn", "door onze eigen Romeinse soldaten",
        "in ons land, dus overal in Italië", "volgens onze eigen Romeinse wetten"], 0,
       "Bij nostra moet je lingua aanvullen uit ipsorum lingua: in hun eigen taal heten ze Kelten, in de onze Galliërs."),
    mk("In welke naamval staan lingua, institutis, legibus in Hi omnes lingua, institutis, legibus inter se differunt?",
       ["nominativus", "accusativus", "ablativus", "dativus"], 2,
       "Het is een ablativus van betrekking: ze verschillen van elkaar wat taal, instellingen en wetten betreft."),
    koppel("Koppel de Latijnse naam aan de rivier van vandaag.",
           [["Garumna", "Garonne"], ["Matrona", "Marne"], ["Sequana", "Seine"], ["Rhodanus", "Rhône"]],
           ["Maas", "Loire"],
           "Garonne, Marne, Seine en Rhône vormen de grenzen die Caesar noemt. Ook de Rijn (Rhenus) komt in de tekst voor."),
    inv("Fortissimi is een overtreffende trap. Van welk bijvoeglijk naamwoord? Geef de nominativus mannelijk enkelvoud.",
        ["fortis"], "Fortis, dapper. Fortior is de vergrotende trap, fortissimus de overtreffende."),
    tabel("Klopt dit volgens Caesar? Waarom zijn de Belgen de dappersten?",
          [("Ze wonen het verst van de beschaving van de provincie.", J),
           ("Ze drijven veel handel met Romeinse kooplui.", F),
           ("Ze wonen dicht bij de Germanen en vechten voortdurend met hen.", J),
           ("Ze hebben dezelfde wetten als de Romeinen.", F)],
          "Caesar zegt net dat er zelden kooplui bij hen komen. Zo komen er ook geen luxeproducten die de geest verwekelijken."),
    mk("Welk verband leggen de woorden propterea quod?",
       ["een tegenstelling", "een oorzaak", "een doel", "een voorwaarde"], 1,
       "Propterea quod betekent omdat. Wat volgt, verklaart waarom de Belgen de dappersten zijn."),
    mk("Wat betekent ad effeminandos animos?",
       ["om de geesten te verwekelijken", "om de vrouwen van de stam te beschermen",
        "om de soldaten extra moed te geven", "tegen de zielen van de gestorven doden"], 0,
       "Ad met een gerundivum drukt een doel uit. Het gaat om luxe die mensen week en minder strijdlustig maakt."),
    mk("Welke provincie bedoelt Caesar met provinciae?",
       ["Hispania, het Iberische schiereiland ten zuiden van de Pyreneeën", "Gallia Narbonensis, in het zuiden van Gallië",
        "Germania aan de overkant van de Rijn, in het oosten", "Britannia, het eiland aan de overkant van de zee"], 1,
       "De provincia was het zuiden van Gallië dat al Romeins was. De naam leeft voort in de Provence."),
    keuze("Quibuscum is hetzelfde als [[*cum quibus|cum quo|quibus cum illis]]. Het verwijst naar de [[*Germanen|Belgen|kooplui]].",
          "In Latijn plakt cum vaak achter een betrekkelijk voornaamwoord: quibuscum, met wie. De Belgen voeren voortdurend oorlog met de Germanen."),
    mk("Waarom overtreffen ook de Helvetii de andere Galliërs in dapperheid?",
       ["ze wonen het dichtst bij de Romeinse provincie", "ze vechten bijna dagelijks met de Germanen",
        "ze hebben de beste wapens van heel Gallië", "ze zijn het grootste volk van Gallië"], 1,
       "Quod fere cotidianis proeliis cum Germanis contendunt: omdat ze bijna dagelijks slag leveren met de Germanen."),
    koppel("Koppel de Latijnse uitdrukking aan de windrichting.",
           [["septentriones", "noorden"], ["orientem solem", "oosten"], ["occasum solis", "westen"]],
           ["zuiden"],
           "Septentriones zijn de zeven ossen, de sterren van de Grote Beer in het noorden. Oriens sol is de opgaande zon, occasus solis de ondergang."),
    sorteer("Van welk Latijns woord uit de tekst komen deze moderne woorden?",
            ["lingua", "flumen", "cotidianus", "humanitas"],
            [["langue", "lingua"], ["language", "lingua"], ["fleuve", "flumen"], ["quotidien", "cotidianus"], ["humanité", "humanitas"]],
            "Veel Franse en Engelse woorden gaan terug op het Latijn. Bij fleuve viel de m weg. Quotidien gaat terug op de latere spelling quotidianus, met qu in plaats van c."),
    mk("In welke naamval staat partes in in partes tres?",
       ["nominativus meervoud", "accusativus meervoud", "ablativus meervoud", "genitivus enkelvoud"], 1,
       "In met de accusativus duidt een richting of een verdeling aan: in drie delen."),
    mk("Caesar noemt de Belgen de dappersten van alle Galliërs. Welk effect heeft dat voor zijn eigen verhaal?",
       ["zijn latere overwinning op hen lijkt des te groter",
        "het toont dat hij de Belgen als trouwe bondgenoten wil winnen",
        "het verklaart waarom hij nooit zelf tegen de Belgen ten strijde trok",
        "het is een verdoken klacht over zijn eigen zwakke en slecht getrainde leger"], 0,
       "De Commentarii zijn ook propaganda. Hoe sterker de vijand, hoe groter de verdienste van de overwinnaar."),
    tabel("Klopt dit over Caesar en zijn werk?",
          [("Caesar leefde in de eerste eeuw voor Christus.", J),
           ("Caesar schrijft in De bello Gallico over zichzelf in de derde persoon.", J),
           ("Caesar vormde het eerste triumviraat met Augustus en Marcus Antonius.", F),
           ("De bello Gallico is een gedicht in hexameters.", F)],
          "Het eerste triumviraat was met Pompeius en Crassus. De bello Gallico is een verslag in proza, een commentarius."),
    open_("Leg in je eigen woorden uit hoe Caesar verklaart dat sommige volken dapperder zijn dan andere.",
          "Volgens Caesar maakt luxe uit de beschaafde wereld mensen week. Wie ver van de provincie woont, krijgt weinig handelaars en luxe, en wie voortdurend moet vechten met buren zoals de Germanen, blijft hard en dapper.",
          "Caesar legt het verband tussen afstand tot de beschaving, handel en voortdurende oorlog."),
]

LEESTEKST_BELGAE = """De Belgen in de ogen van Caesar

Wanneer Julius Caesar in 58 voor Christus als proconsul naar Gallië trekt, kent hij de volken in het noorden nauwelijks. Met Belgae bedoelt hij een groep stammen tussen de Seine, de Marne en de Rijn. Dat is dus niet hetzelfde als het België van vandaag: hun gebied liep tot diep in het huidige Noord-Frankrijk. Wat wij vandaag over de Belgen weten, komt grotendeels uit zijn eigen verslag, De bello Gallico. Dat maakt het boeiend, maar ook verraderlijk: Caesar is niet alleen ooggetuige, hij is ook veldheer en politicus die thuis in Rome indruk wil maken.

Al in de eerste zin van zijn werk noemt hij de Belgen de dappersten van alle Galliërs. Hij geeft er een verklaring bij: ze wonen het verst van de Romeinse provincie, er komen zelden handelaars met luxegoederen, en ze vechten voortdurend met de Germanen aan de overkant van de Rijn. Volgens Caesar stammen de meeste Belgen ook zelf van Germanen af.

In het tweede jaar van de oorlog sluiten de Belgische stammen een bondgenootschap tegen Rome. Enkel de Remi, rond het huidige Reims, kiezen de kant van Caesar en vertellen hem hoeveel krijgers elke stam kan leveren. Aan de rivier de Sabis komt het tot een harde slag tegen de Nerviërs. Caesar beschrijft hoe zijn legioenen even op de rand van een nederlaag staan en hoe hij zelf een schild grijpt en vooraan gaat staan. De Nerviërs vechten zo dapper dat Caesar hun moed uitdrukkelijk prijst.

Enkele jaren later lokt Ambiorix, koning van de Eburonen, een Romeins legioen in de val. De bevelhebbers Sabinus en Cotta zijn het oneens over wat ze moeten doen. Sabinus haalt zijn zin: het legioen verlaat het veilige kamp, valt in een hinderlaag en wordt grotendeels vernietigd. Caesar neemt daarna wraak en laat het gebied van de Eburonen verwoesten.

Wie Caesar leest, moet dus goed opletten. Hij prijst de dapperheid van zijn vijanden, maar dat maakt zijn eigen overwinningen des te groter. En wanneer het misloopt, zoals bij Sabinus, legt hij de schuld graag bij iemand anders.

Bronnen: Caesar, De bello Gallico I, 1 (de Belgen de dappersten); II, 1-4 (bondgenootschap, de Remi, Germaanse afkomst); II, 15-28 (de Nerviërs en de slag aan de Sabis); V, 24-37 (Ambiorix, Sabinus en Cotta); VI, 29-43 (wraak op de Eburonen)."""

LEESVRAGEN = [
    mk("Waarom moet je volgens de tekst opletten wanneer je Caesar leest over de Belgen?",
       ["hij schreef zijn verslag pas honderd jaar na de feiten op papier",
        "hij wil als veldheer en politicus indruk maken in Rome",
        "hij kende zelf geen Latijn en liet alles door slaven vertalen",
        "hij was nooit zelf in Gallië geweest en schreef alles over"], 1,
       "Caesar is ooggetuige, maar ook iemand met belangen: zijn verslag dient ook zijn eigen naam."),
    mk("Welke Belgische stam koos de kant van Caesar?",
       ["de Nerviërs", "de Eburonen", "de Remi", "de Aquitani"], 2,
       "De Remi, rond het huidige Reims, gaven Caesar zelfs informatie over de andere stammen."),
    tabel("Klopt dit volgens de leestekst?",
          [("Caesar prijst de moed van de Nerviërs.", J),
           ("Ambiorix was koning van de Remi.", F),
           ("Bij de slag aan de Sabis stond het Romeinse leger even op de rand van een nederlaag.", J),
           ("Volgens Caesar stammen de meeste Belgen van de Grieken af.", F)],
          "Ambiorix was koning van de Eburonen. Caesar schrijft dat de meeste Belgen van Germanen afstammen."),
    mk("Wat bedoelt Caesar met Belgae?",
       ["de inwoners van het huidige België, binnen de grenzen van nu", "een groep stammen in het noorden van Gallië",
        "alle volken ten oosten van de Rijn, tot aan de Elbe", "de Romeinse kolonisten in het noorden van Gallië"], 1,
       "Caesar gebruikt Belgae voor de stammen tussen Seine, Marne en Rijn. Hun gebied valt niet samen met het België van vandaag."),
    mk("Hoe stelt Caesar de nederlaag van Sabinus en Cotta voor?",
       ["als een fout van hemzelf als opperbevelhebber", "als schuld van de bevelhebbers ter plaatse",
        "als een eervolle overwinning op de Eburonen", "als de schuld van de verraderlijke Remi"], 1,
       "Caesar was er zelf niet bij. Hij legt de oorzaak bij de bevelhebbers ter plaatse, en vooral bij Sabinus, die doordrukte dat het legioen het veilige kamp zou verlaten."),
    open_("Leg met een voorbeeld uit de tekst uit waarom De bello Gallico ook propaganda is.",
          "Caesar prijst de dapperheid van de Belgen en de Nerviërs. Hoe sterker de vijand, hoe groter zijn eigen overwinning lijkt. Bij de slag aan de Sabis toont hij zichzelf als held die vooraan gaat vechten.",
          "Noem een concreet voorbeeld uit de tekst en leg uit wat Caesar ermee wint: meer aanzien in Rome."),
]

if __name__ == "__main__":
    print(len(VRAGEN), len(LEESVRAGEN))
