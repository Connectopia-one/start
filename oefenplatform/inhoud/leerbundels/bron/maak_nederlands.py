# -*- coding: utf-8 -*-
"""De leerbundels voor Nederlands, categorie Start (5de en 6de leerjaar)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel
tabel = bundel.tabel

VAK = "Nederlands"
BUNDELS = {}

BUNDELS["lezen"] = dict(
    vak=VAK, titel="Lezen",
    onder="Een tekst begrijpen, de hoofdgedachte vinden en niet verdrinken in de details.",
    secties=[
        dict(kop="Lees in drie rondes", blokken=[
            ("p", "Een tekst één keer van begin tot eind lezen werkt zelden. Wie goed leest, gaat er meerdere keren doorheen, telkens met een andere bedoeling."),
            ("fig", svg.stappen(["Kijk rond|titel, tussentitels,|afbeeldingen",
                                 "Lees door|van begin tot eind,|zonder te stoppen",
                                 "Lees gericht|zoek het antwoord|op je vraag"]),
             "De eerste ronde duurt tien seconden en scheelt achteraf het meeste tijd."),
            ("p", "Weet je vooraf wat je zoekt, dan hoef je de tekst niet helemaal te onthouden. Lees dus eerst de vragen, en pas daarna de tekst."),
        ]),
        dict(kop="Hoe een tekst in elkaar zit", blokken=[
            ("fig", svg.tekstopbouw([
                ("Titel", "waarover gaat het", 1),
                ("Inleiding", "het onderwerp, en waarom het je aanbelangt", 1.3),
                ("Middenstuk", "één gedachte per alinea", 2.2),
                ("Slot", "de conclusie of de samenvatting", 1.2),
            ]), "Elke alinea heeft één kerngedachte, en die staat meestal in de eerste of de laatste zin."),
            ("p", "Zoek je de <strong>hoofdgedachte</strong> van een hele tekst, kijk dan naar de titel, de inleiding en het slot samen. Die drie zeggen het bijna altijd."),
        ]),
        dict(kop="Signaalwoorden", blokken=[
            ("p", "Sommige woorden verklappen wat er komt. Herken je ze, dan lees je sneller en juister."),
            ("fig", tabel(["Signaalwoord", "Wat er komt"], [
                ["want, omdat, daardoor", "een reden of een gevolg"],
                ["maar, toch, hoewel", "een tegenstelling"],
                ["eerst, daarna, ten slotte", "een volgorde"],
                ["bijvoorbeeld, zoals", "een voorbeeld"],
                ["kortom, dus, samengevat", "een conclusie"],
            ]), "Zie je kortom staan, dan komt de kern van de tekst eraan."),
        ]),
        dict(kop="Soorten teksten", blokken=[
            ("fig", tabel(["Soort", "Waarvoor dient hij", "Voorbeeld"], [
                ["informatief", "iets uitleggen", "een lesbladzijde, een artikel"],
                ["verhalend", "iets vertellen", "een boek, een kortverhaal"],
                ["instructief", "iets laten doen", "een recept, een handleiding"],
                ["overtuigend", "je van iets overtuigen", "reclame, een opiniestuk"],
            ]), "Weet je de soort, dan weet je ook wat je moet zoeken."),
            ("weetje", "Bij een overtuigende tekst is de vraag altijd: <em>wie</em> zegt dit, en wat heeft die eraan? Reclame vertelt zelden het volledige verhaal."),
        ]),
        dict(kop="Een woord dat je niet kent", blokken=[
            ("p", "Sla niet meteen iets op. Lees eerst de zin ervoor en erna: vaak staat de betekenis er gewoon bij, of kan je ze raden uit de rest."),
            ("p", "Helpt dat niet, kijk dan of je stukken van het woord herkent. In <em>onbereikbaar</em> zitten <em>on</em> (niet), <em>bereiken</em> en <em>baar</em> (kan): iets dat je niet kan bereiken."),
        ]),
    ],
    onthoud=[
        "Kijk eerst rond in de tekst voor je begint te lezen.",
        "Lees de vragen voor je de tekst leest.",
        "Elke alinea heeft één kerngedachte.",
        "Titel, inleiding en slot geven samen de hoofdgedachte.",
        "Signaalwoorden verklappen wat er komt.",
        "Raad een onbekend woord eerst uit de zin eromheen.",
    ])

BUNDELS["schrijven"] = dict(
    vak=VAK, titel="Schrijven",
    onder="Van een leeg blad naar een tekst die iemand anders begrijpt.",
    secties=[
        dict(kop="Schrijven in vier stappen", blokken=[
            ("fig", svg.stappen(["Denk|voor wie schrijf je?|wat wil je zeggen?",
                                 "Orden|zet je ideeën|in een volgorde",
                                 "Schrijf|in één ruk,|zonder te schaven",
                                 "Herlees|nu pas verbeter je"]),
             "Schrijven en verbeteren tegelijk doen is het moeilijkste wat er is. Doe het apart."),
            ("p", "Wie vastloopt, is meestal aan het schrijven en verbeteren tegelijk. Schrijf eerst alles op, hoe lelijk ook. Verbeteren komt daarna."),
        ]),
        dict(kop="De opbouw van je tekst", blokken=[
            ("fig", svg.tekstopbouw([
                ("Inleiding", "waarover gaat het, en waarom", 1.2),
                ("Midden", "je punten, één per alinea", 2.2),
                ("Slot", "wat je onthouden wil zien", 1.2),
            ]), "Nieuwe gedachte? Nieuwe alinea. Dat is de hele regel."),
            ("p", "Gebruik verbindingswoorden om je lezer mee te nemen: <em>eerst, daarna, bovendien, toch, ten slotte</em>."),
        ]),
        dict(kop="Leestekens", blokken=[
            ("fig", tabel(["Teken", "Wanneer"], [
                ["punt .", "einde van een zin"],
                ["komma ,", "een korte pauze, of bij een opsomming"],
                ["vraagteken ?", "einde van een vraag"],
                ["uitroepteken !", "bij een uitroep — spaarzaam gebruiken"],
                ["dubbelpunt :", "er komt een opsomming of een uitleg"],
                ["aanhalingstekens „ ”", "iemand zegt iets letterlijk"],
            ]), "Een hoofdletter na een punt, en ook bij namen, landen en talen."),
        ]),
        dict(kop="Werkwoorden schrijven", blokken=[
            ("p", "De meeste schrijffouten zitten in de werkwoorden. Twee regels lossen er al heel veel op."),
            ("kader", "<p style='margin:0 0 5px'><strong>Tegenwoordige tijd.</strong> Ik: de stam. Jij, hij, zij, het: stam + t. "
                      "Vraag je iets met <em>jij</em> erachter, dan valt die t weg: <em>Loop jij mee?</em></p>"
                      "<p style='margin:0'><strong>Verleden tijd.</strong> Eindigt de stam op een letter uit <strong>'t kofschip</strong> "
                      "(t, k, f, s, ch, p — en x), dan wordt het <strong>-te</strong>. Anders <strong>-de</strong>. "
                      "Werken → werkte. Horen → hoorde.</p>"),
            ("weetje", "Twijfel je tussen -d of -t op het einde? Zet het woord in het meervoud. <em>Hij wordt</em> → <em>zij worden</em>, dus met een d."),
        ]),
        dict(kop="Herlezen", blokken=[
            ("p", "Lees je tekst hardop. Struikel je over een zin, dan struikelt je lezer er ook over. Dat is de snelste test die er is."),
            ("fig", tabel(["Kijk na", "Vraag jezelf af"], [
                ["de opbouw", "staat alles in een logische volgorde?"],
                ["de zinnen", "zijn er zinnen die te lang zijn?"],
                ["de werkwoorden", "klopt elke d en t?"],
                ["de hoofdletters", "begint elke zin ermee?"],
                ["de lezer", "begrijpt iemand die er niets van weet dit?"],
            ]), None),
        ]),
    ],
    onthoud=[
        "Schrijven en verbeteren zijn twee aparte stappen.",
        "Nieuwe gedachte, nieuwe alinea.",
        "Tegenwoordige tijd: ik = stam, jij/hij/zij = stam + t.",
        "'t kofschip beslist tussen -te en -de.",
        "Twijfel over d of t? Zet het in het meervoud.",
        "Lees je tekst hardop na.",
    ])

BUNDELS["spreken-en-luisteren"] = dict(
    vak=VAK, titel="Spreken en luisteren",
    onder="Iets vertellen zodat anderen het volgen, en luisteren zodat je het onthoudt.",
    secties=[
        dict(kop="Een spreekbeurt opbouwen", blokken=[
            ("fig", svg.tekstopbouw([
                ("Begin", "zeg waarover je het gaat hebben, en waarom het boeiend is", 1.4),
                ("Midden", "drie punten, niet meer", 1.8),
                ("Einde", "herhaal je belangrijkste punt en bedank je publiek", 1.4),
            ]), "Drie punten onthoudt je publiek. Zeven punten onthoudt niemand, jezelf inbegrepen."),
            ("p", "Schrijf je spreekbeurt niet woord voor woord uit. Maak een kaartje met steekwoorden: dan kijk je naar je publiek in plaats van naar je blad."),
        ]),
        dict(kop="Hoe je klinkt", blokken=[
            ("fig", tabel(["Doe dit", "Waarom"], [
                ["spreek trager dan je denkt", "van de zenuwen ga je vanzelf te snel"],
                ["las stiltes in", "een pauze geeft je publiek tijd om te volgen"],
                ["kijk rond", "dan luistert iedereen mee"],
                ["sta stil", "heen en weer lopen leidt af"],
                ["spreek luid genoeg", "vraag vooraf of ze je achteraan horen"],
            ]), None),
            ("weetje", "Zenuwachtig zijn gaat niet weg door te oefenen, maar je wordt er wel beter in ondanks de zenuwen. Ook ervaren sprekers hebben hartkloppingen."),
        ]),
        dict(kop="Goed luisteren", blokken=[
            ("p", "Luisteren is niet hetzelfde als stil zijn. Wie goed luistert, is actief bezig."),
            ("fig", svg.stappen(["Kijk|naar wie spreekt", "Vang|de kern, niet elk woord", "Vraag|als je iets mist"]),
             "Noteer enkel steekwoorden. Alles opschrijven betekent dat je niet meer luistert."),
        ]),
        dict(kop="Een gesprek voeren", blokken=[
            ("fig", tabel(["In een gesprek", "Hoe dat klinkt"], [
                ["laat uitspreken", "wacht tot de ander klaar is"],
                ["vraag door", "Hoe bedoel je dat precies?"],
                ["vat samen", "Dus als ik het goed begrijp…"],
                ["geef je mening beleefd", "Ik zie dat anders, want…"],
                ["geef toe als je iets niet weet", "Dat weet ik niet, ik zoek het op."],
            ]), "Doorvragen is het verschil tussen praten en een gesprek voeren."),
        ]),
        dict(kop="Formeel en informeel", blokken=[
            ("p", "Tegen een vriend praat je anders dan tegen een directeur. Dat is geen onbeleefdheid, dat is aanvoelen waar je bent."),
            ("p", "Bij iemand die je niet kent: <strong>u</strong>, volledige zinnen, geen afkortingen. Bij vrienden mag alles losser. Twijfel je, begin dan formeel; naar beneden bijstellen is makkelijker dan omgekeerd."),
        ]),
    ],
    onthoud=[
        "Drie punten in een spreekbeurt, niet meer.",
        "Werk met steekwoorden, niet met een uitgeschreven tekst.",
        "Spreek trager dan je denkt en las stiltes in.",
        "Luisteren is actief: vang de kern en vraag door.",
        "Laat de ander uitspreken.",
        "Twijfel je over u of je? Begin formeel.",
    ])

BUNDELS["taalsysteem-en-taalgebruik"] = dict(
    vak=VAK, titel="Taalsysteem en taalgebruik",
    onder="Woordsoorten, zinsdelen en de spellingregels die je het vaakst nodig hebt.",
    secties=[
        dict(kop="Woordsoorten", blokken=[
            ("fig", tabel(["Soort", "Wat het doet", "Voorbeeld"], [
                ["zelfstandig naamwoord", "noemt een ding, dier of persoon", "hond, school, Lien"],
                ["werkwoord", "zegt wat er gebeurt", "lopen, zijn, denken"],
                ["bijvoeglijk naamwoord", "zegt hoe iets is", "groot, rood, stil"],
                ["lidwoord", "staat voor een naamwoord", "de, het, een"],
                ["voornaamwoord", "vervangt een naamwoord", "ik, jij, hem, dit"],
                ["voorzetsel", "zegt waar of wanneer", "op, in, onder, na"],
            ]), "Een goede test voor een werkwoord: kan je er ik, jij of wij voor zetten?"),
        ]),
        dict(kop="De zin uit elkaar halen", blokken=[
            ("fig", svg.zinsdelen([
                ("De grote hond", "onderwerp", "#2f5d50"),
                ("blaft", "persoonsvorm", "#c17f2b"),
                ("in de tuin", "bepaling", "#3b6ea5"),
            ], 470), "Wie of wat blaft? De grote hond. Dat is het onderwerp."),
            ("kader", "<p style='margin:0 0 4px'><strong>De persoonsvorm vinden:</strong> maak van de zin een vraag. "
                      "Het werkwoord dat dan vooraan springt, is de persoonsvorm. <em>Blaft de grote hond in de tuin?</em></p>"
                      "<p style='margin:0'><strong>Het onderwerp vinden:</strong> vraag <em>wie of wat</em> + de persoonsvorm.</p>"),
        ]),
        dict(kop="Werkwoordspelling", blokken=[
            ("fig", svg.stappen(["Zoek de stam|hele werkwoord min -en",
                                 "Welke tijd?|nu of vroeger",
                                 "Pas de regel toe|stam + t, of -te/-de"], kleur=svg.AMBER),
             "Werken → stam werk. Nu: ik werk, jij werkt. Vroeger: ik werkte."),
            ("p", "<strong>'t kofschip</strong>: eindigt de stam op t, k, f, s, ch of p (en ook x), dan wordt de verleden tijd <strong>-te</strong>. In alle andere gevallen <strong>-de</strong>."),
            ("weetje", "De t van <em>jij werkt</em> valt weg als jij <em>achter</em> het werkwoord staat: <em>Werk jij vandaag?</em> Dat is de fout die het vaakst gemaakt wordt."),
        ]),
        dict(kop="Meervoud en verkleinwoord", blokken=[
            ("fig", tabel(["Regel", "Voorbeeld"], [
                ["meestal -en", "boek → boeken"],
                ["soms -s", "tafel → tafels, meisje → meisjes"],
                ["klinker verdubbelt niet", "raam → ramen"],
                ["medeklinker verdubbelt wel", "pot → potten"],
                ["verkleinwoord", "boek → boekje, raam → raampje"],
            ]), "Of het -en of -s wordt, hoor je meestal: zeg het luidop."),
        ]),
        dict(kop="Hoofdletters", blokken=[
            ("p", "Een hoofdletter krijg je aan het begin van een zin, bij namen van mensen, bij landen, steden en talen, en bij feestdagen."),
            ("p", "Géén hoofdletter bij dagen en maanden — dat is net het verschil met het Engels. Bij ons: maandag, december. In het Engels: Monday, December."),
        ]),
    ],
    onthoud=[
        "Werkwoord? Zet er ik, jij of wij voor.",
        "Persoonsvorm vinden: maak van de zin een vraag.",
        "Onderwerp vinden: wie of wat + de persoonsvorm.",
        "'t kofschip beslist tussen -te en -de.",
        "Staat jij achter het werkwoord, dan valt de t weg.",
        "Dagen en maanden krijgen in het Nederlands géén hoofdletter.",
    ])

BUNDELS["literatuur"] = dict(
    vak=VAK, titel="Literatuur",
    onder="Verhalen en gedichten: hoe ze gebouwd zijn en waarom dat werkt.",
    secties=[
        dict(kop="De spanningsboog", blokken=[
            ("p", "Bijna elk verhaal volgt dezelfde lijn. Herken je die, dan zie je meteen waar je in een boek zit."),
            ("fig", svg.spanningsboog(470), "De spanning loopt op tot het hoogtepunt en zakt daarna snel."),
            ("p", "Het hoogtepunt komt meestal laat in het verhaal, niet in het midden. Daarna wil je als lezer nog maar één ding weten: hoe loopt het af?"),
        ]),
        dict(kop="Wie vertelt het verhaal?", blokken=[
            ("fig", tabel(["Verteller", "Hoe je het merkt", "Wat dat doet"], [
                ["ik-verteller", "het verhaal zegt ik", "je kruipt in het hoofd van één personage"],
                ["hij- of zij-verteller", "het verhaal zegt hij of zij", "je ziet meer dan één personage"],
            ]), "Een ik-verteller weet niet alles — en vertelt soms iets anders dan wat er echt gebeurde."),
        ]),
        dict(kop="Soorten verhalen", blokken=[
            ("fig", tabel(["Genre", "Waaraan je het herkent"], [
                ["avontuur", "een reis, gevaar, een doel dat bereikt moet worden"],
                ["fantasy", "een wereld met eigen regels, magie"],
                ["sciencefiction", "toekomst, techniek die nog niet bestaat"],
                ["detective", "een raadsel dat opgelost moet worden"],
                ["historisch verhaal", "speelt in een echt verleden"],
                ["realistisch verhaal", "zou echt kunnen gebeuren"],
            ]), None),
            ("p", "Een <strong>sprookje</strong>, een <strong>fabel</strong> (met dieren die praten) en een <strong>mythe</strong> zijn oude verhaalvormen. Ze werden eerst verteld en pas later opgeschreven."),
        ]),
        dict(kop="Gedichten", blokken=[
            ("p", "Een gedicht zegt met weinig woorden veel. De vorm doet mee: waar de regel eindigt, waar een wit staat, hoe het klinkt."),
            ("fig", tabel(["Woord", "Wat het betekent"], [
                ["strofe", "een groepje regels, met wit ertussen"],
                ["rijm", "regels die op dezelfde klank eindigen"],
                ["beeldspraak", "iets zeggen door het met iets anders te vergelijken"],
                ["vergelijking", "de zon brandt <em>als</em> een oven"],
                ["metafoor", "de zon is een oven — zonder als"],
            ]), "Niet elk gedicht rijmt. Rijm is een keuze, geen voorwaarde."),
        ]),
        dict(kop="Praten over een boek", blokken=[
            ("p", "Zeggen dat een boek leuk was, zegt nog niets. Zeg <em>waarom</em>: over het verhaal, over een personage, of over hoe het geschreven is."),
            ("fig", tabel(["In plaats van", "Zeg liever"], [
                ["het was spannend", "ik wist tot de laatste bladzijde niet hoe het zou aflopen"],
                ["saai", "er gebeurde te weinig in de eerste honderd bladzijden"],
                ["het hoofdpersonage was leuk", "ik herkende mezelf in hoe zij twijfelde"],
            ]), "Zo wordt je mening iets waar iemand anders ook wat aan heeft."),
        ]),
    ],
    onthoud=[
        "Elk verhaal heeft een begin, een probleem, een hoogtepunt en een einde.",
        "Het hoogtepunt komt laat, niet in het midden.",
        "Een ik-verteller weet niet alles.",
        "Een fabel heeft dieren die praten, een mythe komt uit een oude cultuur.",
        "Een vergelijking gebruikt als, een metafoor niet.",
        "Zeg altijd waarom je iets goed of slecht vond.",
    ])

if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)
