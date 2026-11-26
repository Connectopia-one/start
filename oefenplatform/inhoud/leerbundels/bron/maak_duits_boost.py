# -*- coding: utf-8 -*-
"""Leerbundels, oefenbundels en uitlegbladen voor Duits 🚀 Boost doorstroom.

Gebaseerd op de vakfiche `2027_Duits_2MT` (richting moderne talen, ERK A2
voor lezen, A1+ voor schrijven). Enkel het schriftelijke deel: lezen,
schrijven, schriftelijke interactie, woordenschat en grammatica. Luisteren,
spreken en de gesprekken vragen geluid en een gesprekspartner; achteraan elke
bundel staat daarom een kleine opdracht om luidop te oefenen.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof met andere vragen. Kim uploadt de bundel dus twee
keer. De bundels dekken de vragen van `../../boost-doorstroom/bron/de_*.py`,
met dezelfde woorden.
"""
import sys, pathlib, re, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Duits"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel
W = "130px"
WW = "200px"

BUNDELS = {}
OEFENBUNDELS = {}
UITLEGBLADEN = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Schrijf Duitse zelfstandige naamwoorden altijd met een hoofdletter en met hun lidwoord.",
    "Twijfel je? Kijk eerst in je leerbundel, en probeer het daarna nog eens zonder.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]


def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def luidop(tekst):
    return ("kader", "<p><strong>Luidop oefenen.</strong> " + tekst + "</p>")


def thema(titel, onder, secties, onthoud, reeksen, uitleg):
    k = slug(titel) + "-boost-doorstroom"
    BUNDELS[k] = dict(vak=VAK, niveau=BOOST, titel=titel, onder=onder, secties=secties, onthoud=onthoud,
                      hoofdstukken=[f"{titel} — deel 1", f"{titel} — deel 2"])
    OEFENBUNDELS["oefenbundel-" + k] = dict(vak=VAK, niveau=BOOST, titel=titel,
                                           onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
                                           hoe=HOE, reeksen=reeksen)
    UITLEGBLADEN["oefenbundel-" + k] = dict(reeksen=uitleg)


# ═════════════════════════ 1. Een Duitse tekst lezen
thema(
    "Een Duitse tekst lezen",
    "Onderwerp, hoofdgedachte, hoofdpunten en informatie zoeken, en woorden afleiden uit de context.",
    [
        dict(kop="Vier vragen bij elke tekst", blokken=[
            ("p", tabel(["Wat zoek je?", "Hoe zeg je het?", "Voorbeeld (rommelmarkt in Aken)"], [
                ["het onderwerp", "in één of enkele woorden: waarover gaat het?", "een tweedehandsmarkt"],
                ["de hoofdgedachte", "in één zin: wat is de belangrijkste boodschap?", "op de rommelmarkt koop je goedkoop en gooi je minder weg"],
                ["de hoofdpunten", "alles wat de hoofdgedachte ondersteunt", "de spullen zijn goedkoop; men gooit minder weg"],
                ["de informatie die je nodig hebt", "een los gegeven: een uur, een prijs, een plaats", "de markt eindigt om 14 uur"],
            ])),
            ("kader", "<strong>Hoofdzaak of bijzaak?</strong> Een voorbeeld of een detail (een kleur, een uur) "
                      "licht een hoofdpunt toe, maar is zelf geen hoofdzaak."),
        ]),
        dict(kop="Lezen met een plan", blokken=[
            ("p", "<ol><li>Lees de <strong>titel</strong> en kijk naar de foto: waarover zal het gaan? "
                  "<em>Fünf Tipps für einen gesunden Schlaf</em> gaat over beter slapen.</li>"
                  "<li>Lees de vraag, dan pas de tekst. Zo weet je wat je zoekt.</li>"
                  "<li>Zoek de plaats in de tekst. Let op kleine woorden: <em>nicht ..., sondern ...</em> "
                  "(niet ..., maar ...), <em>nur</em> (alleen), <em>jeden ersten Samstag im Monat</em> "
                  "(elke eerste zaterdag van de maand), <em>unter 6 Jahren</em> (jonger dan zes).</li></ol>"),
        ]),
        dict(kop="Een woord afleiden", blokken=[
            ("p", "Niet elk woord moet je opzoeken. Bepaal eerst of het woord belangrijk is. Vaak verraadt de "
                  "zin errond de betekenis:"),
            ("p", tabel(["Je leest", "Dus betekent het woord"], [
                ["Der Kühlschrank ist <strong>leer</strong>. Wir müssen einkaufen.", "leeg"],
                ["Meine Oma ist <strong>krank</strong>. Der Arzt kommt heute.", "ziek (das Krankenhaus: het ziekenhuis)"],
                ["Der Zug hat 20 Minuten <strong>Verspätung</strong>.", "vertraging (spät: laat)"],
                ["Die <strong>Bremsen</strong> sind neu (bij een fiets te koop).", "de remmen"],
                ["Wir bauen eine neue <strong>Rutsche</strong> (in een zwembad).", "de glijbaan"],
            ])),
        ]),
        dict(kop="Woorden die je vaak leest", blokken=[
            ("p", tabel(["Duits", "Nederlands", "Duits", "Nederlands"], [
                ["der Flohmarkt", "de rommelmarkt", "geschlossen", "gesloten"],
                ["billig", "goedkoop", "verboten", "verboden"],
                ["wegwerfen", "weggooien", "dürfen", "mogen"],
                ["meistens", "meestal", "wieder", "opnieuw"],
                ["das Gleis", "het spoor", "die Durchsage", "het omroepbericht"],
                ["der Zustand", "de staat (in goede staat)", "abends", "'s avonds"],
            ])),
            luidop("Lees een kort tekstje van deze bundel hardop voor. Vertel daarna in het Nederlands in twee zinnen waarover het ging."),
        ]),
    ],
    ["Onderwerp: enkele woorden. Hoofdgedachte: één zin.",
     "Hoofdpunten ondersteunen de hoofdgedachte; details zijn bijzaken.",
     "Lees eerst de vraag, zoek dan de plaats in de tekst.",
     "Leid een woord af uit de context voor je het opzoekt."],
    [
        dict(kop="Woorden uit de teksten", opdracht="Wat betekent het woord?", oefeningen=[
            ("rij", [("billig", "goedkoop"), ("geschlossen", "gesloten"), ("verboten", "verboden"), ("meistens", "meestal")], None, W),
            ("rij", [("die Verspätung", "de vertraging"), ("das Gleis", "het spoor"), ("abends", "'s avonds"), ("wieder", "opnieuw")], None, W),
        ]),
        dict(kop="Lezen", opdracht="Lees het tekstje en antwoord.", oefeningen=[
            ("tekst", "<p><em>Die Bibliothek ist ab Montag wieder offen. Neu: Am Samstag ist sie bis 17 Uhr geöffnet. "
                      "Schüler leihen Bücher gratis. Für DVDs zahlt man einen Euro.</em></p>"),
            ("kort", "Wat is het onderwerp in enkele woorden?", "de openingsuren en regels van de bibliotheek", WW),
            ("kort", "Tot hoe laat is de bibliotheek op zaterdag open?", "tot 17 uur", W),
            ("waar", "Leerlingen betalen een euro per boek.", False),
            ("waar", "Voor een dvd betaal je een euro.", True),
        ]),
        dict(kop="Afleiden", opdracht="Wat betekent het vetgedrukte woord? Kijk naar de zin.", oefeningen=[
            ("kort", "Es ist kalt. Zieh deine <strong>Jacke</strong> an!", "de jas", W),
            ("kort", "Ich habe <strong>Durst</strong>. Hast du Wasser?", "dorst", W),
            ("open", "Waarom zoek je best niet elk onbekend woord meteen op?", "Je hebt niet genoeg tijd, en vaak kan je het woord afleiden uit de zin of is het niet belangrijk om de tekst te begrijpen.", 2),
        ]),
    ],
    [
        dict(aanpak="Leer zulke woorden in een rijtje en zeg ze luidop.", waarom=[None, "Spät is laat: Verspätung is wat te laat is."]),
        dict(aanpak="Lees eerst de vraag, zoek dan de plaats in de tekst.",
             waarom=[None, None, "Schüler leihen Bücher gratis: boeken zijn gratis.", None]),
        dict(aanpak="Wat past in de zin? Een jas trek je aan als het koud is.", waarom=[None, None, None]),
    ],
)

# ═════════════════════════ 2. Tekstsoorten
thema(
    "Tekstsoorten, signaalwoorden en verwijswoorden",
    "De vijf soorten teksten, het communicatiemodel, signaalwoorden en verwijswoorden zoals er en sie.",
    [
        dict(kop="Vijf soorten teksten", blokken=[
            ("p", tabel(["Soort", "Wat doet de tekst?", "Voorbeelden"], [
                ["informatief", "geeft informatie over een onderwerp", "krantenartikel, stukje uit een leerboek, mail aan een klant"],
                ["persuasief", "wil je overtuigen of beïnvloeden", "reclame, campagne tegen te snel rijden, flyer van een fitnesscentrum"],
                ["opiniërend", "iemand geeft zijn mening (<em>Ich finde ..., Meiner Meinung nach ...</em>)", "recensie, hotelbeoordeling, reactie op sociale media"],
                ["prescriptief", "zegt wat of hoe je iets moet doen", "recept, instructiefilmpje, schoolreglement, <em>Bitte nicht rauchen!</em>"],
                ["narratief", "vertelt gebeurtenissen als een verhaal", "vlog, reisverslag, podcast, getuigenis over een eerste werkdag"],
            ])),
        ]),
        dict(kop="Het communicatiemodel", blokken=[
            ("p", "Stel drie vragen: <strong>van wie</strong> is de tekst, <strong>voor wie</strong> is hij bedoeld, "
                  "en <strong>waarom</strong> is hij gemaakt? Een mail die begint met <em>Sehr geehrte Frau Weber</em> "
                  "is voor een volwassene die de schrijver niet goed kent. Een flyer met <em>Der erste Monat ist gratis!</em> "
                  "wil nieuwe klanten lokken. Titel, tussentitels, vetgedrukte woorden en beelden helpen je voorspellen "
                  "waarover een tekst gaat."),
        ]),
        dict(kop="Signaalwoorden", blokken=[
            ("p", tabel(["Verband", "Signaalwoorden", "Betekenis"], [
                ["opsomming en keuze", "und, auch, oder", "en, ook, of"],
                ["tegenstelling", "aber, trotzdem, nicht ..., sondern ...", "maar, toch, niet ..., maar ..."],
                ["reden", "denn, weil", "want, omdat"],
                ["gevolg", "deshalb, also", "daarom, dus"],
                ["volgorde", "zuerst, dann, danach, zum Schluss", "eerst, dan, daarna, tot slot"],
                ["voorbeeld", "zum Beispiel (z.B.)", "bijvoorbeeld"],
            ])),
            ("kader", "<strong>Valse vriend:</strong> <em>also</em> betekent dus, niet ook. Ook is <em>auch</em>."),
        ]),
        dict(kop="Verwijswoorden", blokken=[
            ("p", "Een voornaamwoord verwijst terug naar een woord uit een vorige zin. Het geslacht van dat woord "
                  "bepaalt welk voornaamwoord je gebruikt, ook bij dingen."),
            ("p", tabel(["Zin 1", "Zin 2", "Verwijst naar"], [
                ["Meine Schwester heißt Mia.", "<strong>Sie</strong> ist zwölf.", "Mia"],
                ["Ich habe einen neuen Hund.", "<strong>Er</strong> heißt Bello.", "der Hund"],
                ["Das ist mein Fahrrad.", "<strong>Es</strong> ist ganz neu.", "das Fahrrad"],
                ["Die Lehrerin gibt den Schülern ein Buch.", "<strong>Sie</strong> lesen es zu Hause.", "de leerlingen (meervoud: lesen)"],
            ])),
            luidop("Lees de signaalwoorden uit de tabel hardop en maak met elk een korte zin."),
        ]),
    ],
    ["Informatief, persuasief, opiniërend, prescriptief, narratief.",
     "Communicatiemodel: van wie, voor wie, waarom?",
     "Aber en trotzdem: tegenstelling. Denn en weil: reden. Deshalb: gevolg.",
     "Also is dus, auch is ook.",
     "Het geslacht van het woord bepaalt er, sie of es."],
    [
        dict(kop="Tekstsoorten", opdracht="Welke soort tekst is het?", oefeningen=[
            ("rij", [("een recept voor soep", "prescriptief"), ("een reclame voor schoenen", "persuasief"),
                     ("een blog over je reis", "narratief"), ("een recensie van een film", "opiniërend")], None, W),
            ("kies", "Der Rhein ist 1 233 Kilometer lang. Welke soort?", ["informatief", "narratief", "persuasief"], 0),
        ]),
        dict(kop="Signaalwoorden", opdracht="Vul het juiste signaalwoord in.", oefeningen=[
            ("kort", "Es regnet. ... nehme ich den Bus. (daarom)", "Deshalb", W),
            ("kort", "Ich esse gern Pizza, ... keine Pasta. (maar)", "aber", W),
            ("kort", "... öffnest du die Packung. (eerst)", "Zuerst", W),
            ("kort", "Ich bleibe zu Hause, ... ich bin krank. (want)", "denn", W),
        ]),
        dict(kop="Verwijswoorden", opdracht="Naar wie of wat verwijst het vetgedrukte woord?", oefeningen=[
            ("kort", "Ich habe einen Bruder. <strong>Er</strong> heißt Tim.", "de broer (Tim)", WW),
            ("kort", "Die Jacke ist schön. <strong>Sie</strong> ist blau.", "de jas", WW),
            ("waar", "Also betekent ook.", False),
        ]),
    ],
    [
        dict(aanpak="Vraag je af wat de tekst wil doen: informeren, overtuigen, een mening geven, uitleggen hoe het moet of vertellen.",
             waarom=[None, "Alleen feiten, geen mening of oproep: informatief."]),
        dict(aanpak="Kijk welk verband er tussen de twee delen is: gevolg, tegenstelling, volgorde of reden.",
             waarom=["Na deshalb staat de persoonsvorm meteen: deshalb nehme ich.", None, None, "Na denn blijft de gewone woordvolgorde."]),
        dict(aanpak="Zoek het woord in de zin ervoor met hetzelfde geslacht en getal.", waarom=["Der Bruder is mannelijk: er.", "Die Jacke is vrouwelijk: sie.", "Also is dus. Ook is auch."]),
    ],
)

# ═════════════════════════ 3. Schrijven
thema(
    "Schrijven en schriftelijke interactie",
    "Aanspreken en groeten, bedanken, uitnodigen en je verontschuldigen, een mail of zoekertje opbouwen en je mening geven.",
    [
        dict(kop="Du of Sie?", blokken=[
            ("p", tabel(["", "Een vriend(in)", "Een volwassene die je niet goed kent"], [
                ["aanspreking", "Lieber Jonas, / Liebe Emma, / Hallo Lisa,", "Sehr geehrter Herr Schulz, / Sehr geehrte Frau Becker,"],
                ["vorm", "du: Kannst du mir helfen?", "Sie (hoofdletter): Können Sie mir helfen?"],
                ["slot", "Bis bald! / Liebe Grüße / Tschüss!", "Mit freundlichen Grüßen / Freundliche Grüße"],
            ])),
            ("kader", "Bij <em>Sie</em> staat het werkwoord in het meervoud: <em>können Sie</em>. "
                      "<em>Herr</em> is mannelijk: <em>sehr geehrter Herr</em>; bij een vrouw: <em>sehr geehrte Frau</em>."),
        ]),
        dict(kop="Vaste formules", blokken=[
            ("p", tabel(["Situatie", "Duits", "Antwoord"], [
                ["bedanken", "Vielen Dank! / Danke schön!", "Gern geschehen! / Bitte!"],
                ["verontschuldigen", "Entschuldigung! / Das tut mir leid.", "Kein Problem! / Das macht nichts."],
                ["uitnodigen", "Ich lade dich zu meiner Party ein.", "Ich komme gern! / Leider kann ich nicht kommen."],
                ["voorstellen", "Wollen wir ...? / Hast du Lust, ... zu ...?", "Gute Idee! / Ich gehe lieber ins Kino."],
                ["groeten", "Guten Morgen! / Guten Abend! / Wie geht's?", "Danke, gut. Und dir?"],
                ["afscheid", "Tschüss! / Auf Wiedersehen! / Bis nächste Woche!", ""],
                ["wensen", "Alles Gute zum Geburtstag! / Gute Besserung! / Gute Reise!", ""],
            ])),
        ]),
        dict(kop="Een mail of zoekertje opbouwen", blokken=[
            ("p", "<ol><li><strong>Aanspreking</strong>: Sehr geehrte Frau ..., / Liebe ...,</li>"
                  "<li><strong>Wie ben je?</strong> Ich heiße Noor und bin 16 Jahre alt.</li>"
                  "<li><strong>Waarom schrijf je?</strong> Ich suche einen Ferienjob im Juli.</li>"
                  "<li><strong>Je vragen</strong>: Wann beginnt die Arbeit? Wie viel verdient man pro Stunde? Wo ...?</li>"
                  "<li><strong>Bedanking</strong>: Vielen Dank im Voraus für Ihre Antwort.</li>"
                  "<li><strong>Groet</strong>: Mit freundlichen Grüßen, Noor</li></ol>"),
            ("p", "Een <strong>zoekertje</strong> geeft alles wat de lezer moet weten: wat je verkoopt, de staat, de prijs en hoe ze je bereiken."),
            ("p", tabel(["Vraagwoord", "Betekenis"], [["wann", "wanneer"], ["wo", "waar"], ["wer", "wie"], ["wie", "hoe"], ["was", "wat"], ["wie viel", "hoeveel"]])),
        ]),
        dict(kop="Je mening geven en vertellen", blokken=[
            ("p", "<em>Ich finde, dass Sport wichtig ist. Meiner Meinung nach ... Ich bin der Meinung, dass ...</em> "
                  "Na <em>dass</em> staat de persoonsvorm achteraan. Een tip geef je met een imperativus: "
                  "<em>Iss jeden Tag Obst!</em> De weg uitleggen: <em>Gehen Sie geradeaus und dann links.</em>"),
            ("p", "Vertel je wat gebeurd is, zoals in een verslag over je stage, dan gebruik je het Perfekt: "
                  "<em>Am ersten Tag habe ich die Kollegen kennengelernt.</em>"),
            ("kader", "<strong>Op het examen</strong> mag je een online woordenboek en een spellingcontrole gebruiken. "
                      "Lees je tekst na: is hij duidelijk en gepast, en respecteer je de lengte? Zit je vast, zeg het "
                      "dan anders met woorden die je wel kent."),
            luidop("Speel met iemand thuis een kort gesprek: je nodigt de ander uit, de ander weigert beleefd en stelt iets anders voor."),
        ]),
    ],
    ["Onbekende volwassene: Sie, Sehr geehrte(r), Mit freundlichen Grüßen.",
     "Vriend: du, Liebe(r), Liebe Grüße.",
     "Mail: aanspreking, wie ben je, waarom, vragen, bedanking, groet.",
     "Wer is wie, wie is hoe, wo is waar.",
     "Na dass en weil staat de persoonsvorm achteraan."],
    [
        dict(kop="Du of Sie?", opdracht="Vul aan.", oefeningen=[
            ("kort", "Mail aan meneer Braun: Sehr ... Herr Braun,", "geehrter", W),
            ("kort", "Mail aan je vriendin Sara: ... Sara,", "Liebe", W),
            ("kort", "Beleefd slot: Mit ... Grüßen", "freundlichen", W),
        ]),
        dict(kop="Reageren", opdracht="Wat zeg je?", oefeningen=[
            ("rij", [("iemand is jarig", "Alles Gute zum Geburtstag!"), ("iemand is ziek", "Gute Besserung!"),
                     ("iemand bedankt je", "Gern geschehen!"), ("iemand zegt sorry", "Kein Problem!")], None, WW),
            ("kort", "Wie ... es dir? (hoe gaat het met je?)", "geht", W),
        ]),
        dict(kop="Schrijven", opdracht="Schrijf in het Duits.", oefeningen=[
            ("open", "Stel jezelf voor in twee zinnen: je naam, je leeftijd en waar je woont.", "Ich heiße Lotte und bin 16 Jahre alt. Ich wohne in Gent.", 2),
            ("open", "Vraag in een mail beleefd wanneer het werk begint en hoeveel je per uur verdient.", "Wann beginnt die Arbeit? Wie viel verdient man pro Stunde?", 2),
            ("open", "Geef je mening over huiswerk in één zin met dass.", "Ich finde, dass Hausaufgaben wichtig sind.", 2),
        ]),
    ],
    [
        dict(aanpak="Een volwassene die je niet goed kent: Sie en een beleefde aanspreking.",
             waarom=["Herr is mannelijk: geehrter.", "Sara is een meisje: Liebe.", None]),
        dict(aanpak="Leer de vaste formules als een rijtje vraag en antwoord.", waarom=[None, None]),
        dict(aanpak="Gebruik zinnen uit de leerbundel als model.",
             waarom=["Je leeftijd zeg je met sein: ich bin 16 Jahre alt.", "Bij Sie blijft de vraag beleefd.", "Na dass staat sind achteraan."]),
    ],
)

# ═════════════════════════ 4. Ik, familie, lichaam, kleding
thema(
    "Woordvelden: ik, mijn familie, mijn lichaam en kleding",
    "Persoonlijke gegevens, familie, landen en talen, gevoelens, lichaam en gezondheid, kleding, kleuren en materialen.",
    [
        dict(kop="Persoonlijke gegevens en familie", blokken=[
            ("p", tabel(["Duits", "Nederlands", "Duits", "Nederlands"], [
                ["der Vorname", "de voornaam", "die Eltern", "de ouders"],
                ["der Nachname, Familienname", "de familienaam", "die Großeltern", "de grootouders"],
                ["der Wohnort", "de woonplaats", "die Geschwister", "de broers en zussen"],
                ["das Geburtsdatum", "de geboortedatum", "die Tante, der Onkel", "de tante, de oom"],
                ["die Telefonnummer", "het telefoonnummer", "der Sohn, die Tochter", "de zoon, de dochter"],
                ["verheiratet", "getrouwd", "der Cousin", "de neef"],
                ["geschieden", "gescheiden", "der Nachbar", "de buur (geen familie)"],
            ])),
            ("p", "Je leeftijd zeg je met <em>sein</em>: <em>Ich bin 16 Jahre alt.</em> Een vraag: <em>Wie ist deine Telefonnummer?</em>"),
        ]),
        dict(kop="Landen en talen", blokken=[
            ("p", tabel(["Land", "Inwoner", "Taal"], [
                ["Belgien", "der Belgier", "Niederländisch, Französisch, Deutsch"],
                ["Deutschland", "der Deutsche", "Deutsch"],
                ["Österreich", "der Österreicher", "Deutsch"],
                ["die Schweiz", "der Schweizer", "Deutsch, Französisch, Italienisch, Rätoromanisch"],
                ["Frankreich", "der Franzose, die Französin", "Französisch"],
                ["die Niederlande (meervoud)", "der Niederländer", "Niederländisch"],
            ])),
            ("p", "<em>Ich komme aus Belgien</em>: ik kom uit België. <em>Ich wohne in den Niederlanden.</em>"),
        ]),
        dict(kop="Gevoelens", blokken=[
            ("p", tabel(["Duits", "Nederlands"], [
                ["froh, glücklich", "blij, gelukkig"], ["traurig", "verdrietig"], ["müde", "moe"],
                ["böse, wütend", "boos"], ["nervös, ängstlich", "zenuwachtig, angstig"], ["Angst haben", "bang zijn"],
                ["sich freuen auf", "uitkijken naar"], ["langweilig", "saai"],
            ])),
        ]),
        dict(kop="Lichaam en gezondheid", blokken=[
            ("p", tabel(["Duits", "Nederlands", "Duits", "Nederlands"], [
                ["der Kopf", "het hoofd", "das Auge", "het oog"],
                ["der Bauch", "de buik", "das Ohr", "het oor"],
                ["der Rücken", "de rug", "die Hand, die Hände", "de hand"],
                ["das Bein", "het been", "das Knie", "de knie"],
                ["Kopfschmerzen", "hoofdpijn", "das Fieber", "de koorts"],
                ["der Arzt, der Zahnarzt", "de dokter, de tandarts", "die Apotheke", "de apotheek"],
                ["die Nase, der Mund", "de neus, de mond", "die Tabletten", "de pillen"],
            ])),
        ]),
        dict(kop="Kleding, kleuren, vormen en materialen", blokken=[
            ("p", tabel(["Kleding", "", "Kleuren", "", "Materiaal en vorm", ""], [
                ["die Hose", "de broek", "rot", "rood", "das Holz", "het hout"],
                ["das Hemd", "het hemd", "grün", "groen", "das Leder", "het leder"],
                ["die Jacke", "de jas", "gelb", "geel", "die Baumwolle", "het katoen"],
                ["der Rock", "de rok", "braun", "bruin", "das Metall", "het metaal"],
                ["das Kleid", "het kleed", "blau", "blauw", "der Kreis", "de cirkel"],
                ["die Schuhe, die Socken", "schoenen, kousen", "weiß, schwarz", "wit, zwart", "das Quadrat", "het vierkant"],
                ["die Brille, die Tasche, der Gürtel", "bril, tas, riem", "grau", "grijs", "das Dreieck", "de driehoek"],
            ])),
            ("p", "In de winkel: <em>Haben Sie die Schuhe auch in Größe 39?</em> (maat 39)"),
            luidop("Beschrijf jezelf in vier zinnen: je naam, je leeftijd, je familie en wat je vandaag draagt."),
        ]),
    ],
    ["Ich bin 16 Jahre alt: leeftijd met sein.",
     "Die Geschwister: broers en zussen. Der Nachbar is geen familie.",
     "Braun is bruin, blau is blauw. Das Auge is het oog, das Ohr het oor.",
     "Die Niederlande is meervoud: in den Niederlanden."],
    [
        dict(kop="Familie en gegevens", opdracht="Vertaal.", oefeningen=[
            ("rij", [("de ouders", "die Eltern"), ("de tante", "die Tante"), ("de buur", "der Nachbar"), ("de voornaam", "der Vorname")], None, W),
            ("kort", "Ich ... 15 Jahre alt.", "bin", W),
        ]),
        dict(kop="Lichaam en gevoelens", opdracht="Wat betekent het?", oefeningen=[
            ("rij", [("der Bauch", "de buik"), ("das Auge", "het oog"), ("das Fieber", "de koorts"), ("traurig", "verdrietig")], None, W),
            ("waar", "Ich habe Angst betekent ik heb honger.", False),
        ]),
        dict(kop="Kleding en kleuren", opdracht="Vertaal.", oefeningen=[
            ("rij", [("de broek", "die Hose"), ("de jas", "die Jacke"), ("groen", "grün"), ("wit", "weiß")], None, W),
            ("kies", "Een tafel aus Holz is van ...", ["hout", "metaal", "glas"], 0),
        ]),
    ],
    [
        dict(aanpak="Leer elk zelfstandig naamwoord met zijn lidwoord.", waarom=[None, "Leeftijd met sein, niet met haben."]),
        dict(aanpak="Maak een tekening van een lichaam en schrijf de Duitse woorden erbij.", waarom=[None, "Angst haben is bang zijn. Honger is Hunger."]),
        dict(aanpak="Let op de umlaut en de ß: grün, weiß.", waarom=[None, "Das Holz: het hout."]),
    ],
)

# ═════════════════════════ 5. Thuis, eten, winkelen, media
thema(
    "Woordvelden: thuis, eten, winkelen en media",
    "De woning en de meubels, de dag, voorwerpen, eten en drinken, winkels, hoeveelheden, prijzen en multimedia.",
    [
        dict(kop="De woning", blokken=[
            ("p", tabel(["Kamers", "", "Meubels en toestellen", ""], [
                ["die Küche", "de keuken", "der Tisch, der Stuhl", "de tafel, de stoel"],
                ["das Wohnzimmer", "de woonkamer", "der Schrank", "de kast"],
                ["das Schlafzimmer", "de slaapkamer", "das Sofa, die Lampe", "de zetel, de lamp"],
                ["das Badezimmer", "de badkamer", "der Kühlschrank, der Herd", "de koelkast, het fornuis"],
                ["die Wohnung", "het appartement", "der Staubsauger", "de stofzuiger"],
                ["im dritten Stock", "op de derde verdieping", "die Treppe, der Aufzug", "de trap, de lift"],
                ["das Bett", "het bed", "der Kleiderschrank", "de kleerkast"],
                ["die Dusche", "de douche", "die Badewanne", "het bad"],
            ])),
        ]),
        dict(kop="De dag en de media", blokken=[
            ("p", tabel(["Duits", "Nederlands", "Duits", "Nederlands"], [
                ["aufstehen (ich stehe auf)", "opstaan", "das Handy", "de gsm"],
                ["frühstücken", "ontbijten", "eine Nachricht schicken", "een bericht sturen"],
                ["sich die Zähne putzen", "de tanden poetsen", "anrufen (ich rufe an)", "opbellen"],
                ["aufräumen", "opruimen", "herunterladen / hochladen", "downloaden / uploaden"],
                ["fernsehen", "televisie kijken", "der Bildschirm", "het scherm"],
                ["der Schlüssel", "de sleutel", "die Tastatur", "het toetsenbord"],
            ])),
        ]),
        dict(kop="Eten en drinken", blokken=[
            ("p", tabel(["Duits", "Nederlands", "Duits", "Nederlands"], [
                ["das Brot, das Brötchen", "het brood, het broodje", "das Obst", "het fruit (Apfel, Banane)"],
                ["die Milch, die Butter", "de melk, de boter", "das Gemüse", "de groenten (Gurke, Zwiebel, Karotte)"],
                ["der Käse, das Ei", "de kaas, het ei", "die Kartoffel", "de aardappel"],
                ["das Fleisch, der Fisch", "het vlees, de vis", "der Saft, der Tee", "het sap, de thee"],
                ["die Tasse", "de kop", "die Speisekarte", "de menukaart"],
                ["der Kuchen", "de taart", "die Rechnung", "de rekening"],
                ["die Erdbeere", "de aardbei", "der Löffel", "de lepel"],
                ["die Nudeln", "de pasta", "die Wurst", "de worst"],
            ])),
        ]),
        dict(kop="Winkels, hoeveelheden en prijzen", blokken=[
            ("p", tabel(["Winkel", "Wat koop je er?"], [
                ["die Bäckerei", "brood"], ["die Metzgerei", "vlees"], ["die Apotheke", "medicijnen"], ["der Supermarkt", "van alles"],
            ])),
            ("p", "<em>Was kostet das?</em> 3,50 € lees je als <em>drei Euro fünfzig</em>. <em>Ich hätte gern ein Kilo Äpfel.</em> "
                  "Ein Kilo = 1000 Gramm, ein Liter = 1000 Milliliter, eine Flasche (fles), eine Dose (blik), ein Stück (stuk)."),
            ("p", "Getallen: eerst de eenheden. <em>siebenundzwanzig</em> = 27, <em>hundertachtzig</em> = 180, "
                  "<em>dreizehn</em> = 13, <em>dreißig</em> = 30."),
            luidop("Speel winkeltje: vraag in het Duits naar de prijs van drie dingen en zeg de prijzen hardop."),
        ]),
    ],
    ["Der Kühlschrank: de koelkast. Der Tisch is de tafel, der Stuhl de stoel.",
     "Obst is fruit, Gemüse zijn groenten.",
     "Die Rechnung, bitte! Was kostet das?",
     "Eerst de eenheden: siebenundzwanzig = 27."],
    [
        dict(kop="Thuis", opdracht="Vertaal.", oefeningen=[
            ("rij", [("de keuken", "die Küche"), ("de kast", "der Schrank"), ("de sleutel", "der Schlüssel"), ("de trap", "die Treppe")], None, W),
            ("kort", "Ich ... um 7 Uhr auf. (opstaan)", "stehe", W),
        ]),
        dict(kop="Eten en winkelen", opdracht="Vul in of vertaal.", oefeningen=[
            ("rij", [("de melk", "die Milch"), ("de aardappel", "die Kartoffel"), ("het fruit", "das Obst"), ("de rekening", "die Rechnung")], None, W),
            ("kort", "Was ... das? (hoeveel kost dat?)", "kostet", W),
            ("kies", "Waar koop je medicijnen?", ["in der Apotheke", "in der Bäckerei", "in der Metzgerei"], 0),
        ]),
        dict(kop="Getallen", opdracht="Schrijf in cijfers.", oefeningen=[
            ("rij", [("vierundvierzig", "44"), ("hundertzwanzig", "120"), ("dreizehn", "13"), ("dreißig", "30")], None),
        ]),
    ],
    [
        dict(aanpak="Leer de woorden per kamer: wat staat er in de keuken, in de slaapkamer?", waarom=[None, "Aufstehen is scheidbaar: auf gaat naar achteren."]),
        dict(aanpak="Zet een woord altijd met lidwoord in je geheugen.", waarom=[None, None, None]),
        dict(aanpak="Lees het Duitse getal van achter naar voor: eerst de eenheden.", waarom=["Vier-und-vierzig."]),
    ],
)

# ═════════════════════════ 6. School, werk, vrije tijd, reizen, weer
thema(
    "Woordvelden: school, werk, vrije tijd, reizen en weer",
    "School en instructietaal, beroepen, sport en hobby's, vervoer en reizen, het weer, de kalender, feesten en het uur.",
    [
        dict(kop="School en instructietaal", blokken=[
            ("p", tabel(["Duits", "Nederlands", "Opdracht", "Wat doe je?"], [
                ["das Fach", "het vak", "Kreuze ... an.", "kruis aan"],
                ["die Stunde", "het lesuur", "Ergänze ...", "vul aan"],
                ["die Pause", "de speeltijd", "Ordne zu.", "koppel wat samen hoort"],
                ["die Hausaufgaben", "het huiswerk", "Lies den Text.", "lees de tekst"],
                ["der Lehrer, die Lehrerin", "de leraar, de lerares", "Unterstreiche ...", "onderstreep"],
                ["das Zeugnis", "het rapport", "Übersetze ...", "vertaal"],
                ["Mathe, Erdkunde, Biologie", "wiskunde, aardrijkskunde, biologie", "Beantworte die Fragen.", "beantwoord de vragen"],
            ])),
        ]),
        dict(kop="Beroepen", blokken=[
            ("p", tabel(["Beroep", "Wat doet die persoon?"], [
                ["der Koch, die Köchin", "kookt"], ["der Kellner, die Kellnerin", "bedient in een restaurant"],
                ["der Arzt, die Ärztin", "verzorgt zieken"], ["die Krankenpflegerin", "werkt in het ziekenhuis (das Krankenhaus)"],
                ["der Mechaniker", "herstelt auto's in de garage (die Werkstatt)"], ["der Verkäufer, die Verkäuferin", "verkoopt in een winkel"],
            ])),
            ("p", "<em>Was willst du werden?</em> Wat wil je worden? <em>Ich möchte Ärztin werden.</em>"),
        ]),
        dict(kop="Vrije tijd en sport", blokken=[
            ("p", "<em>schwimmen</em> (zwemmen), <em>tauchen</em> (duiken), <em>reiten</em> (paardrijden), <em>klettern</em> (klimmen), "
                  "<em>wandern</em> (wandelen), <em>ins Kino gehen</em> (naar de film gaan). <em>Ich spiele gern Tennis.</em> "
                  "Een instrument zonder lidwoord: <em>Ich spiele Klavier, ich spiele Gitarre.</em>"),
        ]),
        dict(kop="Vervoer en reizen", blokken=[
            ("p", tabel(["Duits", "Nederlands", "Duits", "Nederlands"], [
                ["der Zug", "de trein", "der Bahnhof", "het station"],
                ["die Straßenbahn", "de tram", "der Flughafen", "de luchthaven"],
                ["das Flugzeug", "het vliegtuig", "die Fahrkarte", "het vervoerbewijs"],
                ["das (Fahr)rad", "de fiets", "hin und zurück", "heen en terug"],
                ["zu Fuß gehen", "te voet gaan", "der Reisepass, der Koffer", "het paspoort, de koffer"],
                ["das Zelt", "de tent", "die Jugendherberge", "de jeugdherberg"],
            ])),
            ("p", "<em>Ich fahre mit dem Bus</em> (mit + datief). <em>Die Ferien</em> is de vakantie, <em>die Feiertage</em> de feestdagen."),
        ]),
        dict(kop="Weer, kalender en uur", blokken=[
            ("p", tabel(["Weer", "", "Seizoenen en feesten", ""], [
                ["Es regnet.", "Het regent.", "der Frühling, der Sommer", "de lente, de zomer"],
                ["Es schneit.", "Het sneeuwt.", "der Herbst, der Winter", "de herfst, de winter"],
                ["Die Sonne scheint.", "De zon schijnt.", "Weihnachten", "Kerstmis"],
                ["Es ist heiß / kalt.", "Het is heet / koud.", "Ostern", "Pasen"],
                ["Es ist windig.", "Het waait.", "Silvester", "oudejaarsavond"],
            ])),
            ("p", "Dagen: Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag. "
                  "Maanden: Januar, Februar, März, April, Mai, Juni, Juli, August, September, Oktober, November, Dezember."),
            ("p", tabel(["Duits", "Uur"], [
                ["Es ist halb acht.", "7.30 uur"], ["Viertel nach drei", "3.15 uur"], ["Viertel vor acht", "7.45 uur"], ["um 20 Uhr", "om 8 uur 's avonds"],
            ])),
            ("p", "Plaats: <em>neben</em> (naast), <em>hinter</em> (achter), <em>gegenüber</em> (tegenover). <em>Zu Hause</em> is thuis, <em>nach Hause</em> naar huis."),
            luidop("Vertel hardop wat je gisteren na school deed, met het uur erbij."),
        ]),
    ],
    ["Instructietaal: ankreuzen, ergänzen, zuordnen, unterstreichen.",
     "Mit dem Zug, mit dem Rad, zu Fuß.",
     "Die Ferien: de vakantie. Halb acht: 7.30 uur.",
     "Zu Hause: thuis. Nach Hause: naar huis."],
    [
        dict(kop="School en werk", opdracht="Wat betekent het?", oefeningen=[
            ("rij", [("Kreuze an.", "kruis aan"), ("Ergänze.", "vul aan"), ("die Hausaufgaben", "het huiswerk"), ("der Kellner", "de ober")], None, W),
            ("kort", "Ich möchte Arzt ... (worden)", "werden", W),
        ]),
        dict(kop="Reizen en weer", opdracht="Vertaal.", oefeningen=[
            ("rij", [("de trein", "der Zug"), ("het station", "der Bahnhof"), ("de tent", "das Zelt"), ("het paspoort", "der Reisepass")], None, W),
            ("kort", "Ich fahre ... dem Bus. (met)", "mit", W),
            ("waar", "Es ist heiß betekent het is koud.", False),
        ]),
        dict(kop="Het uur", opdracht="Schrijf het uur in cijfers.", oefeningen=[
            ("rij", [("halb neun", "8.30"), ("Viertel nach zwei", "2.15"), ("Viertel vor fünf", "4.45"), ("um 18 Uhr", "18.00")], None),
        ]),
    ],
    [
        dict(aanpak="Herken de instructietaal: dan weet je op een toets meteen wat je moet doen.", waarom=[None, "Werden: worden."]),
        dict(aanpak="Leer vervoermiddelen samen met mit dem of mit der.", waarom=[None, "Mit neemt een datief.", "Heiß is heet."]),
        dict(aanpak="Halb negen is zoals in het Nederlands half negen: een half uur voor negen.", waarom=[None]),
    ],
)

# ═════════════════════════ 7. Lidwoorden, meervoud, naamvallen
thema(
    "Lidwoorden, meervoud en naamvallen",
    "Der, die, das, het meervoud, de vier naamvallen, kein en nicht, en samenstellingen.",
    [
        dict(kop="Drie geslachten", blokken=[
            ("p", tabel(["", "mannelijk", "vrouwelijk", "onzijdig", "meervoud"], [
                ["bepaald", "der Tisch", "die Lampe", "das Buch", "die Bücher"],
                ["onbepaald", "ein Tisch", "eine Lampe", "ein Buch", "(geen lidwoord) Bücher"],
                ["ontkennend", "kein Tisch", "keine Lampe", "kein Buch", "keine Bücher"],
            ])),
            ("kader", "<strong>Leer elk woord met zijn lidwoord.</strong> Het Duitse geslacht is vaak anders dan in het "
                      "Nederlands: <em>der Tisch</em> (de tafel), <em>das Mädchen</em> (het meisje, onzijdig door -chen), "
                      "<em>die Sonne</em>, <em>der Mond</em>. Woorden op -ung, -heit, -keit zijn vrouwelijk: <em>die Zeitung</em>."),
        ]),
        dict(kop="Het meervoud", blokken=[
            ("p", tabel(["Uitgang", "Voorbeeld"], [
                ["-e", "der Hund → die Hunde"], ["-e met umlaut", "die Hand → die Hände"],
                ["-er met umlaut", "das Buch → die Bücher, das Haus → die Häuser"],
                ["-(e)n", "die Lampe → die Lampen, die Frau → die Frauen"],
                ["-s", "das Auto → die Autos, das Handy → die Handys"],
                ["niets (soms umlaut)", "der Lehrer → die Lehrer, der Apfel → die Äpfel"],
            ])),
            ("p", "In het meervoud is het lidwoord altijd <em>die</em>."),
        ]),
        dict(kop="Vier naamvallen", blokken=[
            ("p", tabel(["Naamval", "Functie", "Vraag", "Voorbeeld"], [
                ["Nominativ", "onderwerp", "wer? was?", "<strong>Der Hund</strong> bellt."],
                ["Akkusativ", "lijdend voorwerp", "wen? was?", "Ich sehe <strong>den Hund</strong>."],
                ["Dativ", "meewerkend voorwerp", "wem?", "Ich gebe <strong>dem Hund</strong> Wasser."],
                ["Genitiv", "bezit", "wessen?", "das Auto <strong>des Lehrers</strong>"],
            ])),
            ("p", tabel(["", "mannelijk", "vrouwelijk", "onzijdig", "meervoud"], [
                ["Nominativ", "der / ein", "die / eine", "das / ein", "die"],
                ["Akkusativ", "<strong>den / einen</strong>", "die / eine", "das / ein", "die"],
                ["Dativ", "dem / einem", "der / einer", "dem / einem", "den (+ -n)"],
                ["Genitiv", "des / eines (+ -s)", "der / einer", "des / eines (+ -s)", "der"],
            ])),
            ("kader", "Alleen bij mannelijke woorden verandert de Akkusativ: <em>der</em> wordt <em>den</em>, "
                      "<em>ein</em> wordt <em>einen</em>. Na <em>es gibt</em> en <em>haben</em> volgt de Akkusativ: "
                      "<em>Ich habe einen Bruder.</em>"),
        ]),
        dict(kop="Kein of nicht?", blokken=[
            ("p", "<em>Kein</em> ontkent een zelfstandig naamwoord zonder lidwoord of met <em>ein</em>: "
                  "<em>Ich habe keinen Hund. Ich trinke keine Milch.</em> <em>Nicht</em> ontkent de rest: een werkwoord, "
                  "een bijvoeglijk naamwoord of een woord met <em>der/die/das</em>: <em>Ich schwimme nicht. Das ist nicht teuer.</em>"),
        ]),
        dict(kop="Samenstellingen", blokken=[
            ("p", "Het laatste woord bepaalt het lidwoord en de betekenis: <em>das Haus + die Tür = die Haustür</em> "
                  "(de voordeur), <em>der Kühlschrank</em>, <em>das Fahrrad</em>. Je schrijft het als één woord."),
            luidop("Wijs tien voorwerpen in je kamer aan en zeg ze met het juiste lidwoord."),
        ]),
    ],
    ["Leer elk woord met der, die of das.",
     "Meervoud: altijd die.",
     "Akkusativ mannelijk: den, einen, keinen.",
     "Kein bij een naamwoord, nicht bij de rest.",
     "Bij een samenstelling telt het laatste woord."],
    [
        dict(kop="Der, die of das?", opdracht="Schrijf het lidwoord.", oefeningen=[
            ("rij", [("... Tisch", "der"), ("... Lampe", "die"), ("... Buch", "das"), ("... Mädchen", "das")], None),
            ("rij", [("... Zeitung", "die"), ("... Hund", "der"), ("... Auto", "das"), ("... Haustür", "die")], None),
        ]),
        dict(kop="Meervoud", opdracht="Schrijf het meervoud.", oefeningen=[
            ("rij", [("das Buch", "die Bücher"), ("die Lampe", "die Lampen"), ("das Auto", "die Autos"), ("die Hand", "die Hände")], None, W),
        ]),
        dict(kop="Naamvallen en ontkenning", opdracht="Vul in.", oefeningen=[
            ("kort", "Ich sehe ... Hund. (de)", "den", W),
            ("kort", "Ich habe ... Bruder. (een)", "einen", W),
            ("kort", "Ich gebe ... Mutter Blumen. (de)", "der", W),
            ("kort", "Ich habe ... Zeit. (geen)", "keine", W),
            ("kort", "Das Wasser ist ... kalt. (niet)", "nicht", W),
        ]),
    ],
    [
        dict(aanpak="Leer het geslacht samen met het woord. Let op -chen (onzijdig) en -ung (vrouwelijk).", waarom=["Mädchen eindigt op -chen.", "Bij een samenstelling telt het laatste woord: die Tür."]),
        dict(aanpak="Er is geen vaste regel: leer het meervoud mee.", waarom=[None]),
        dict(aanpak="Zoek eerst de functie in de zin: onderwerp, lijdend of meewerkend voorwerp.",
             waarom=["Lijdend voorwerp, mannelijk: den.", "Na haben: Akkusativ.", "Meewerkend voorwerp, vrouwelijk: der.", "Zeit heeft geen lidwoord: kein, vrouwelijk keine.", "Kalt is een bijvoeglijk naamwoord: nicht."]),
    ],
)

# ═════════════════════════ 8. Voornaamwoorden
thema(
    "Voornaamwoorden: persoonlijk, bezittelijk, aanwijzend en vragend",
    "Ich, mich, mir; mein en dein; dieser; wer, wen, wem, was, wo en welcher.",
    [
        dict(kop="Persoonlijke voornaamwoorden", blokken=[
            ("p", tabel(["Nominativ", "Akkusativ", "Dativ", "Nederlands"], [
                ["ich", "mich", "mir", "ik, mij"], ["du", "dich", "dir", "jij, jou"], ["er", "ihn", "ihm", "hij, hem"],
                ["sie", "sie", "ihr", "zij, haar"], ["es", "es", "ihm", "het"], ["wir", "uns", "uns", "wij, ons"],
                ["ihr", "euch", "euch", "jullie"], ["sie / Sie", "sie / Sie", "ihnen / Ihnen", "zij / u"],
            ])),
            ("p", "<em>Ich liebe dich</em> (Akkusativ). <em>Kannst du mir helfen?</em> (helfen + Dativ). "
                  "<em>Wie geht es dir?</em> <em>Das gefällt mir.</em>"),
        ]),
        dict(kop="Bezittelijke voornaamwoorden", blokken=[
            ("p", tabel(["Persoon", "Bezit", "Voorbeeld"], [
                ["ich", "mein", "mein Bruder, meine Schwester"], ["du", "dein", "dein Hund"], ["er / es", "sein", "sein Fahrrad"],
                ["sie", "ihr", "ihre Mutter"], ["wir", "unser", "unser Haus"], ["ihr", "euer", "eure Lehrerin"],
                ["sie / Sie", "ihr / Ihr", "Ihr Name, bitte?"],
            ])),
            ("kader", "Een bezittelijk voornaamwoord krijgt dezelfde uitgangen als <em>ein</em>: <em>meine</em> bij een "
                      "vrouwelijk woord en in het meervoud, <em>meinen</em> in de Akkusativ mannelijk: <em>Ich besuche meinen Opa.</em>"),
        ]),
        dict(kop="Aanwijzend en vragend", blokken=[
            ("p", "<em>dieser, diese, dieses</em> (deze, dit) volgt de uitgangen van <em>der, die, das</em>: "
                  "<em>Dieser Pullover ist schön. Ich nehme diesen Pullover.</em>"),
            ("p", tabel(["Vraagwoord", "Betekenis", "Voorbeeld"], [
                ["wer?", "wie? (onderwerp)", "Wer kommt mit?"], ["wen?", "wie? (lijdend voorwerp)", "Wen besuchst du?"],
                ["wem?", "aan wie?", "Wem gehört das Buch?"], ["was?", "wat?", "Was machst du?"],
                ["wo? woher? wohin?", "waar? waarvandaan? waarheen?", "Woher kommst du?"],
                ["welcher, welche, welches?", "welk(e)?", "Welche Farbe magst du?"],
                ["warum? wann? wie?", "waarom? wanneer? hoe?", "Wie alt bist du?"],
            ])),
            ("kader", "<strong>Valse vrienden:</strong> <em>wer</em> is wie, <em>wie</em> is hoe, <em>wo</em> is waar."),
            luidop("Stel aan iemand thuis vijf vragen met telkens een ander vraagwoord."),
        ]),
    ],
    ["Mich en dich: Akkusativ. Mir en dir: Dativ.",
     "Sein bij hij, ihr bij zij.",
     "Meinen in de Akkusativ mannelijk, meine bij vrouwelijk en meervoud.",
     "Wer = wie, wie = hoe, wo = waar."],
    [
        dict(kop="Persoonlijke voornaamwoorden", opdracht="Vul in.", oefeningen=[
            ("kort", "Kannst du ... helfen? (mij)", "mir", W),
            ("kort", "Ich sehe ... morgen. (jou)", "dich", W),
            ("kort", "Das ist Tom. Ich mag ... (hem)", "ihn", W),
        ]),
        dict(kop="Bezittelijke voornaamwoorden", opdracht="Vul in.", oefeningen=[
            ("kort", "Lisa und ... Bruder. (haar)", "ihr", W),
            ("kort", "Tom und ... Schwester. (zijn)", "seine", W),
            ("kort", "Ich besuche ... Opa. (mijn)", "meinen", W),
        ]),
        dict(kop="Vraagwoorden", opdracht="Welk vraagwoord past?", oefeningen=[
            ("rij", [("... kommst du? Aus Gent.", "Woher"), ("... alt bist du?", "Wie"), ("... ist das? Mein Lehrer.", "Wer"), ("... Farbe magst du?", "Welche")], None, W),
        ]),
    ],
    [
        dict(aanpak="Vraag je af welke naamval het werkwoord vraagt.", waarom=["Helfen neemt een Dativ.", "Lijdend voorwerp: dich.", "Lijdend voorwerp, mannelijk: ihn."]),
        dict(aanpak="Kijk wie de bezitter is, en daarna naar het geslacht van wat je bezit.", waarom=["Bezitter is zij: ihr.", "Bezitter is hij, Schwester is vrouwelijk: seine.", "Akkusativ mannelijk: meinen."]),
        dict(aanpak="Let op de valse vrienden wer, wie en wo.", waarom=[None]),
    ],
)

# ═════════════════════════ 9. Präsens en Imperativ
thema(
    "Präsens en Imperativ",
    "De tegenwoordige tijd van regelmatige en onregelmatige werkwoorden, sein en haben, hulpwerkwoorden, scheidbare werkwoorden en de gebiedende wijs.",
    [
        dict(kop="Regelmatige werkwoorden", blokken=[
            ("p", tabel(["", "wohnen", "arbeiten", "sein", "haben"], [
                ["ich", "wohne", "arbeite", "bin", "habe"], ["du", "wohnst", "arbeitest", "bist", "hast"],
                ["er / sie / es", "wohnt", "arbeitet", "ist", "hat"], ["wir", "wohnen", "arbeiten", "sind", "haben"],
                ["ihr", "wohnt", "arbeitet", "seid", "habt"], ["sie / Sie", "wohnen", "arbeiten", "sind", "haben"],
            ])),
            ("p", "Stam op -t of -d krijgt een extra e: <em>du arbeitest, er findet</em>."),
        ]),
        dict(kop="Klinkerwissel bij du en er", blokken=[
            ("p", tabel(["Wissel", "Infinitief", "du", "er / sie / es"], [
                ["a → ä", "fahren, schlafen", "fährst, schläfst", "fährt, schläft"],
                ["e → i", "essen, sprechen, helfen", "isst, sprichst, hilfst", "isst, spricht, hilft"],
                ["e → ie", "lesen, sehen", "liest, siehst", "liest, sieht"],
            ])),
        ]),
        dict(kop="Hulpwerkwoorden van modaliteit", blokken=[
            ("p", tabel(["", "können", "müssen", "wollen", "dürfen", "möchten"], [
                ["ich", "kann", "muss", "will", "darf", "möchte"], ["du", "kannst", "musst", "willst", "darfst", "möchtest"],
                ["er / sie", "kann", "muss", "will", "darf", "möchte"], ["wir", "können", "müssen", "wollen", "dürfen", "möchten"],
            ])),
            ("p", "Het hoofdwerkwoord staat als infinitief achteraan: <em>Ich kann gut schwimmen.</em> "
                  "<em>Ich muss Hausaufgaben machen.</em> <em>Hier darf man nicht rauchen.</em>"),
        ]),
        dict(kop="Scheidbare werkwoorden", blokken=[
            ("p", "Bij <em>aufstehen, anrufen, einkaufen, fernsehen, mitkommen</em> gaat het voorvoegsel naar het einde: "
                  "<em>Ich stehe um 7 Uhr auf. Ruf mich morgen an!</em> Met een hulpwerkwoord blijft het werkwoord heel: "
                  "<em>Ich muss früh aufstehen.</em>"),
        ]),
        dict(kop="De gebiedende wijs (Imperativ)", blokken=[
            ("p", tabel(["Tegen wie?", "Vorm", "Voorbeeld"], [
                ["één persoon (du)", "stam, zonder du", "Komm! Mach das Fenster zu! Lies den Text! Iss!"],
                ["meer personen (ihr)", "ihr-vorm, zonder ihr", "Kommt! Macht das Fenster zu!"],
                ["beleefd (Sie)", "infinitief + Sie", "Kommen Sie bitte! Gehen Sie geradeaus!"],
                ["sein", "", "Sei ruhig! Seid ruhig! Seien Sie ruhig!"],
            ])),
            ("kader", "Bij e → i blijft de wissel in de du-imperativus: <em>lesen → Lies!</em>, <em>essen → Iss!</em>. "
                      "Bij a → ä niet: <em>fahren → Fahr!</em>"),
            luidop("Geef iemand thuis vijf korte opdrachten in het Duits, zoals Steh auf! of Mach die Tür zu!"),
        ]),
    ],
    ["Ich -e, du -st, er -t, wir -en, ihr -t, sie -en.",
     "Fahren: du fährst. Sprechen: du sprichst. Lesen: du liest.",
     "Hulpwerkwoord op plaats 2, infinitief achteraan.",
     "Scheidbaar voorvoegsel naar het einde.",
     "Imperativ: Komm! Kommt! Kommen Sie!"],
    [
        dict(kop="Vervoegen", opdracht="Vervoeg het werkwoord.", oefeningen=[
            ("rij", [("ich (wohnen)", "wohne"), ("du (arbeiten)", "arbeitest"), ("er (fahren)", "fährt"), ("du (sprechen)", "sprichst")], None, W),
            ("rij", [("ihr (sein)", "seid"), ("er (haben)", "hat"), ("sie (lesen)", "liest"), ("du (essen)", "isst")], None, W),
        ]),
        dict(kop="Hulpwerkwoorden en scheidbare werkwoorden", opdracht="Maak de zin af.", oefeningen=[
            ("kort", "Ich ... gut schwimmen. (kunnen)", "kann", W),
            ("kort", "Wir ... morgen früh aufstehen. (moeten)", "müssen", W),
            ("kort", "Ich rufe dich morgen ... (anrufen)", "an", W),
            ("waar", "In Ich muss Hausaufgaben machen staat machen achteraan.", True),
        ]),
        dict(kop="Imperativ", opdracht="Zet in de gebiedende wijs.", oefeningen=[
            ("rij", [("du: lesen", "Lies!"), ("ihr: kommen", "Kommt!"), ("Sie: warten", "Warten Sie!"), ("du: fahren", "Fahr!")], None, W),
        ]),
    ],
    [
        dict(aanpak="Zoek de stam, kijk dan of er een klinkerwissel is bij du of er.", waarom=[None, "Sein is onregelmatig: ihr seid. Essen: du isst."]),
        dict(aanpak="Het hulpwerkwoord staat op plaats 2, de infinitief helemaal achteraan.", waarom=[None, None, "Anrufen is scheidbaar: an gaat naar het einde.", None]),
        dict(aanpak="Du: stam. Ihr: ihr-vorm. Sie: infinitief en Sie.", waarom=["De e → i-wissel blijft: lies.", ]),
    ],
)

# ═════════════════════════ 10. Perfekt en Futur
thema(
    "Perfekt en Futur",
    "Vertellen wat gebeurd is met haben of sein en het voltooid deelwoord, en de toekomst met werden.",
    [
        dict(kop="Het Perfekt", blokken=[
            ("p", "Hulpwerkwoord <em>haben</em> of <em>sein</em> op plaats 2, voltooid deelwoord achteraan: "
                  "<em>Ich habe Pizza gegessen. Wir sind nach Berlin gefahren.</em>"),
            ("p", tabel(["Soort", "Vorm", "Voorbeeld"], [
                ["regelmatig", "ge + stam + t", "machen → gemacht, spielen → gespielt, arbeiten → gearbeitet"],
                ["onregelmatig", "ge + (andere) stam + en", "essen → gegessen, sehen → gesehen, schreiben → geschrieben, trinken → getrunken"],
                ["scheidbaar", "voorvoegsel + ge + ...", "einkaufen → eingekauft, aufstehen → aufgestanden"],
                ["zonder ge-", "op -ieren, be-, ver-, er-", "telefonieren → telefoniert, besuchen → besucht, verstehen → verstanden"],
            ])),
        ]),
        dict(kop="Haben of sein?", blokken=[
            ("p", tabel(["sein", "haben"], [
                ["beweging van A naar B: gehen, fahren, fliegen, kommen", "de meeste andere werkwoorden: machen, essen, lesen"],
                ["verandering van toestand: aufstehen, einschlafen", "ook bij wederkerende werkwoorden"],
                ["sein en bleiben: Ich bin zu Hause geblieben.", "Ich habe gut geschlafen."],
            ])),
            ("kader", "<em>Ich bin gewesen</em> (ik ben geweest), <em>ich habe gehabt</em> (ik heb gehad). Vaak gebruikt men "
                      "ook de korte vormen <em>ich war</em> en <em>ich hatte</em>."),
        ]),
        dict(kop="Het Futur", blokken=[
            ("p", "<em>werden</em> op plaats 2 en de infinitief achteraan: <em>Wir werden nächstes Jahr nach Italien fahren.</em>"),
            ("p", tabel(["", "werden"], [["ich", "werde"], ["du", "wirst"], ["er / sie / es", "wird"], ["wir", "werden"], ["ihr", "werdet"], ["sie / Sie", "werden"]])),
            ("p", "Heel vaak gebruikt men gewoon het Präsens met een tijdsaanduiding: <em>Morgen fahre ich nach Köln.</em>"),
            luidop("Vertel in vijf zinnen in het Perfekt wat je vorig weekend gedaan hebt."),
        ]),
    ],
    ["Perfekt: haben of sein + voltooid deelwoord achteraan.",
     "Beweging en verandering: sein.",
     "Regelmatig ge-...-t, onregelmatig ge-...-en.",
     "Futur: werden + infinitief."],
    [
        dict(kop="Voltooid deelwoord", opdracht="Schrijf het voltooid deelwoord.", oefeningen=[
            ("rij", [("machen", "gemacht"), ("essen", "gegessen"), ("einkaufen", "eingekauft"), ("besuchen", "besucht")], None, W),
            ("rij", [("schreiben", "geschrieben"), ("fahren", "gefahren"), ("telefonieren", "telefoniert"), ("trinken", "getrunken")], None, W),
        ]),
        dict(kop="Haben of sein?", opdracht="Vul de juiste vorm in.", oefeningen=[
            ("kort", "Ich ... nach Hause gegangen.", "bin", W),
            ("kort", "Wir ... einen Film gesehen.", "haben", W),
            ("kort", "Er ... um sieben Uhr aufgestanden.", "ist", W),
            ("kort", "... du gut geschlafen?", "Hast", W),
        ]),
        dict(kop="Futur", opdracht="Vul de vorm van werden in.", oefeningen=[
            ("kort", "Ich ... morgen lernen.", "werde", W),
            ("kort", "Es ... morgen regnen.", "wird", W),
            ("waar", "Wir sind nach Italien gefahren gaat over de toekomst.", False),
        ]),
    ],
    [
        dict(aanpak="Regelmatig: ge + stam + t. Onregelmatig moet je leren.", waarom=["Scheidbaar en zonder ge-: eingekauft en besucht.", "Op -ieren komt geen ge-."]),
        dict(aanpak="Beweging van A naar B of verandering van toestand: sein.", waarom=["Gehen is beweging.", None, "Aufstehen is een verandering.", None]),
        dict(aanpak="Werden staat op plaats 2, de infinitief achteraan.", waarom=[None, None, "Dat is een Perfekt: het is al gebeurd."]),
    ],
)

# ═════════════════════════ 11. Zinsbouw
thema(
    "Zinsbouw: soorten zinnen, Satzklammer en voegwoorden",
    "De persoonsvorm op plaats 2, inversie, vraagzinnen, de Satzklammer, nevenschikkende en onderschikkende voegwoorden.",
    [
        dict(kop="Plaats 2 en inversie", blokken=[
            ("p", tabel(["Plaats 1", "Plaats 2 (persoonsvorm)", "Rest"], [
                ["Ich", "spiele", "morgen Tennis."], ["Morgen", "spiele", "ich Tennis."], ["Am Wochenende", "fahren", "wir ans Meer."],
            ])),
            ("p", "Begint de zin met iets anders dan het onderwerp, dan komt het onderwerp na de persoonsvorm (inversie)."),
        ]),
        dict(kop="Soorten zinnen", blokken=[
            ("p", tabel(["Soort", "Persoonsvorm", "Voorbeeld"], [
                ["mededeling", "plaats 2", "Ich wohne in Gent."], ["vraag met vraagwoord", "plaats 2", "Wo wohnst du?"],
                ["ja-neevraag", "plaats 1", "Wohnst du in Gent?"], ["gebod", "plaats 1", "Komm her!"],
            ])),
        ]),
        dict(kop="De Satzklammer", blokken=[
            ("p", "Bestaat het gezegde uit twee delen, dan staan die als een klem rond de rest: de persoonsvorm op plaats 2, het andere deel achteraan."),
            ("p", tabel(["Persoonsvorm", "...", "Einde"], [
                ["Ich <strong>kann</strong>", "heute leider nicht", "<strong>kommen</strong>."],
                ["Wir <strong>haben</strong>", "gestern Pizza", "<strong>gegessen</strong>."],
                ["Ich <strong>stehe</strong>", "jeden Tag um sieben Uhr", "<strong>auf</strong>."],
                ["Er <strong>wird</strong>", "nächstes Jahr in Berlin", "<strong>studieren</strong>."],
            ])),
        ]),
        dict(kop="Voegwoorden", blokken=[
            ("p", tabel(["Nevenschikkend (gewone volgorde)", "Onderschikkend (persoonsvorm achteraan)"], [
                ["und (en), oder (of), aber (maar)", "weil (omdat), dass (dat)"],
                ["denn (want)", "wenn (als, wanneer), ob (of)"],
                ["sondern (maar, na een ontkenning)", "als (toen), obwohl (hoewel)"],
            ])),
            ("p", "<em>Ich bleibe zu Hause, denn ich <strong>bin</strong> krank.</em> — <em>Ich bleibe zu Hause, weil ich krank <strong>bin</strong>.</em>"),
            ("kader", "<em>Denn</em> en <em>weil</em> betekenen hetzelfde, maar na <em>weil</em> gaat de persoonsvorm naar achteren. "
                      "<em>Sondern</em> gebruik je na <em>nicht</em> of <em>kein</em>: <em>nicht heute, sondern morgen</em>."),
            luidop("Maak drie zinnen met weil over waarom je iets graag doet, en lees ze hardop."),
        ]),
    ],
    ["Persoonsvorm op plaats 2; ja-neevraag en gebod: plaats 1.",
     "Begint de zin niet met het onderwerp: inversie.",
     "Satzklammer: tweede deel van het gezegde achteraan.",
     "Weil, dass, wenn, ob, obwohl: persoonsvorm achteraan."],
    [
        dict(kop="Woordvolgorde", opdracht="Zet de woorden in de juiste volgorde.", oefeningen=[
            ("open", "morgen / ich / spiele / Tennis (begin met Morgen)", "Morgen spiele ich Tennis.", 1),
            ("open", "kann / ich / kommen / heute / nicht", "Ich kann heute nicht kommen.", 1),
            ("open", "du / in Gent / wohnst ? (ja-neevraag)", "Wohnst du in Gent?", 1),
        ]),
        dict(kop="Voegwoorden", opdracht="Kies het voegwoord en let op de volgorde.", oefeningen=[
            ("kort", "Ich lerne, ... ich morgen einen Test habe. (omdat)", "weil", W),
            ("kort", "Nicht Tee, ... Kaffee. (maar)", "sondern", W),
            ("kort", "Ich weiß, ... du recht hast. (dat)", "dass", W),
            ("open", "Verbind met weil: Ich bleibe zu Hause. Ich bin krank.", "Ich bleibe zu Hause, weil ich krank bin.", 1),
            ("waar", "Na denn gaat de persoonsvorm naar het einde van de zin.", False),
        ]),
    ],
    [
        dict(aanpak="Zoek eerst de persoonsvorm en zet die op plaats 2 (of 1 bij een ja-neevraag).", waarom=["Inversie: spiele ich.", "Satzklammer: kommen achteraan.", None]),
        dict(aanpak="Bij weil, dass en wenn: persoonsvorm achteraan.", waarom=[None, "Na nicht: sondern.", None, "Bin komt achteraan.", "Na denn blijft de gewone volgorde."]),
    ],
)

# ═════════════════════════ 12. Voorzetsels, telwoorden, bijwoorden, uitspraak
thema(
    "Voorzetsels, telwoorden, bijwoorden en uitspraak",
    "Voorzetsels met Akkusativ, Dativ of allebei, getallen en datums, bijwoorden van tijd en de Duitse klanken en spelling.",
    [
        dict(kop="Voorzetsels", blokken=[
            ("p", tabel(["Altijd Akkusativ", "Altijd Dativ", "Wechselpräpositionen"], [
                ["für (voor), ohne (zonder)", "mit (met), bei (bij)", "in, an, auf"],
                ["durch (door), gegen (tegen)", "von (van), zu (naar)", "über, unter, vor"],
                ["um (om)", "aus (uit), nach (naar, na), seit (sinds)", "hinter, neben, zwischen"],
            ])),
            ("p", "Wechselpräpositionen: <strong>waar?</strong> (plaats) → Dativ, <strong>waarheen?</strong> (beweging) → Akkusativ. "
                  "<em>Ich bin in der Schule.</em> — <em>Ich gehe in die Schule.</em>"),
            ("kader", "Samentrekkingen: <em>in dem = im, zu dem = zum, zu der = zur, an dem = am, in das = ins</em>. "
                      "Steden en landen zonder lidwoord: <em>nach Berlin, nach Spanien</em>; maar <em>in die Schweiz</em>."),
        ]),
        dict(kop="Getallen en datums", blokken=[
            ("p", tabel(["Getal", "Duits", "Getal", "Duits"], [
                ["12", "zwölf", "21", "einundzwanzig"], ["16", "sechzehn", "30", "dreißig"], ["17", "siebzehn", "100", "hundert"],
                ["20", "zwanzig", "1 000", "tausend"],
                ["1999", "neunzehnhundertneunundneunzig", "2026", "zweitausendsechsundzwanzig"],
            ])),
            ("p", "Rangtelwoorden: <em>der erste, zweite, dritte, vierte, siebte</em>, vanaf 20 met -ste: <em>der zwanzigste</em>. "
                  "Datum: <em>am 3. Mai</em> (am dritten Mai). <em>Ich habe am 12. Juni Geburtstag.</em>"),
        ]),
        dict(kop="Bijwoorden", blokken=[
            ("p", tabel(["Duits", "Nederlands", "Duits", "Nederlands"], [
                ["heute, morgen, gestern", "vandaag, morgen, gisteren", "immer, oft, manchmal, selten, nie", "altijd, vaak, soms, zelden, nooit"],
                ["jetzt, bald, später", "nu, binnenkort, later", "leider, gern, sehr", "helaas, graag, heel"],
                ["hier, dort", "hier, daar", "schon, noch", "al, nog"],
            ])),
        ]),
        dict(kop="Klanken en spelling", blokken=[
            ("p", tabel(["Schrijf je", "Klinkt als", "Voorbeeld"], [
                ["ei", "aai", "mein, Eis"], ["ie", "ie (lang)", "Liebe, spielen"], ["eu, äu", "oi", "heute, Häuser"],
                ["ü", "uu (Nederlandse u)", "Tür, müde"], ["ö", "eu", "schön, hören"], ["ä", "è", "Mädchen"],
                ["sch", "sj", "Schule"], ["st, sp aan het begin", "sjt, sjp", "Straße, Sport"], ["ch na a, o, u", "zachte g-klank", "Buch, acht"],
                ["z", "ts", "Zeit, zehn"], ["w", "Nederlandse w als in wat", "Wasser"], ["v", "f", "Vater, viel"],
            ])),
            ("p", "Na een lange klinker of een tweeklank schrijf je <em>ß</em>: <em>die Straße, heißen</em>. Na een korte klinker "
                  "<em>ss</em>: <em>der Fluss, essen</em>. Alle zelfstandige naamwoorden krijgen een hoofdletter, ook <em>Sie</em> (u)."),
            luidop("Lees de voorbeeldwoorden uit de klankentabel hardop. Let vooral op ei en ie."),
        ]),
    ],
    ["Für, ohne, durch, gegen, um: Akkusativ.",
     "Mit, bei, von, zu, aus, nach, seit: Dativ.",
     "In, an, auf ...: waar → Dativ, waarheen → Akkusativ.",
     "Eerst de eenheden: einundzwanzig.",
     "Ei klinkt als aai, ie als ie. Hoofdletter bij elk naamwoord."],
    [
        dict(kop="Voorzetsels", opdracht="Vul het lidwoord in.", oefeningen=[
            ("kort", "Das Geschenk ist für ... Vater.", "den", W),
            ("kort", "Ich fahre mit ... Bus.", "dem", W),
            ("kort", "Ich gehe in ... Schule. (waarheen?)", "die", W),
            ("kort", "Ich bin in ... Schule. (waar?)", "der", W),
            ("kort", "Wir fahren ... Berlin. (naar)", "nach", W),
        ]),
        dict(kop="Getallen", opdracht="Schrijf voluit in het Duits.", oefeningen=[
            ("rij", [("21", "einundzwanzig"), ("17", "siebzehn"), ("30", "dreißig"), ("de 3de", "der dritte")], None, WW),
        ]),
        dict(kop="Bijwoorden en spelling", opdracht="Vertaal of kies.", oefeningen=[
            ("rij", [("gisteren", "gestern"), ("altijd", "immer"), ("helaas", "leider"), ("al", "schon")], None, W),
            ("kies", "Welk woord is juist geschreven?", ["die Straße", "die strasse", "die Strase"], 0),
            ("waar", "Ei in mein klinkt zoals ie in Liebe.", False),
        ]),
    ],
    [
        dict(aanpak="Leer de drie rijtjes voorzetsels uit je hoofd.", waarom=["Für: Akkusativ.", "Mit: Dativ.", "Beweging: Akkusativ.", "Plaats: Dativ.", "Stad zonder lidwoord: nach."]),
        dict(aanpak="Eerst de eenheden, dan und, dan de tientallen.", waarom=[None]),
        dict(aanpak="Leer de bijwoorden in paren van tegenstellingen.", waarom=[None, "Naamwoord met hoofdletter, ß na de lange a.", "Ei klinkt als aai."]),
    ],
)
