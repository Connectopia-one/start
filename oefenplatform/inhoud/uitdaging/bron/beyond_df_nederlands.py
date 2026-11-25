# -*- coding: utf-8 -*-
"""Uitdaging Nederlands 🌍 Beyond dubbele finaliteit (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die alle hoofdstukken
door elkaar halen. Een zelf geschreven lezersbrief en verhaalfragment om op te
klikken, tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde en een
korte schrijfopdracht. Geen nieuwe leerstof: alles staat in de hoofdstukken
van Nederlands Beyond dubbele finaliteit.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_df_nederlands.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Nederlands"
BESTAND = "beyond-df-nederlands-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/nederlands-beyond-df-uitdaging"
BRIEF = "lezersbrief-zwembad.svg"
VERHAAL = "verhaal-noor.svg"


def zin(i, n=6):
    """Klikvak van zin i (vanaf 1), zie uitdaging/_blad.py."""
    h = 90 + n * 92 + 30
    return [2, round((90 + (i - 1) * 92) / h * 100, 1), 96, round(92 / h * 100, 1)]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Lezersbrief (prent)
    klik("Lees de lezersbrief. Klik op de zin met een drogreden: de schrijver valt de persoon aan in plaats van zijn argument.",
         BRIEF, [zin(5)],
         "Of de schepen kan zwemmen, zegt niets over de vraag of het zwembad open moet blijven. Dat is een persoonlijke aanval (op de man spelen)."),
    klik("Klik op de zin met het standpunt van de schrijver.",
         BRIEF, [zin(6)],
         "Met 'daarom' trekt de schrijver zijn conclusie: het zwembad moet openblijven."),
    klik("Klik op de zin die een controleerbaar feit geeft over de kosten.",
         BRIEF, [zin(2)],
         "Een bedrag van 400 000 euro per jaar kan je nakijken in de begroting. Het is een feit, geen mening."),
    met_prent(BRIEF, tabel(
        "Welke functie heeft het signaalwoord?",
        [
            ("Toch (zin 3)", "Tegenstelling"),
            ("want (zin 3)", "Reden"),
            ("Bovendien (zin 4)", "Opsomming"),
            ("Daarom (zin 6)", "Conclusie"),
        ],
        "Toch zet iets tegenover het vorige, want geeft een reden, bovendien voegt een argument toe en daarom leidt een besluit in.",
        kolommen=["Tegenstelling", "Reden", "Opsomming", "Conclusie"])),
    met_prent(BRIEF, mk(
        "Wat is het doel van deze lezersbrief?",
        ["Overtuigen", "Informeren", "Vermaken", "Instrueren"],
        0,
        "De schrijver geeft argumenten en vraagt de gemeenteraad iets te doen: hij wil overtuigen.")),

    # Verhaal (prent)
    klik("Lees het fragment. Klik op de zin met een flashback.",
         VERHAAL, [zin(5)],
         "'Twee jaar eerder' springt terug in de tijd: een terugblik of flashback."),
    klik("Klik op de zin die de ruimte (de omgeving) beschrijft.",
         VERHAAL, [zin(4)],
         "Het stormweer en de buigende bomen schetsen de omgeving en versterken de onrustige sfeer."),
    klik("Klik op de zin met directe rede.",
         VERHAAL, [zin(3)],
         "De letterlijke woorden van Amir staan tussen aanhalingstekens."),
    met_prent(VERHAAL, keuze(
        "Het verhaal wordt verteld door een [[*hij- of zij-verteller|ik-verteller]] die de gevoelens van [[*Noor|Amir]] kent. Dat zie je in zin [[*2|3|4]].",
        "De verteller spreekt over 'ze' en kent wat Noor voelt: haar hart bonst. Dat is een personale hij-verteller.")),

    # Tekstsoorten en bronnen
    tabel(
        "Welk teksttype is dit?",
        [
            ("Een handleiding bij een wasmachine", "Prescriptief"),
            ("Een nieuwsbericht over een brand", "Informatief"),
            ("Een opiniestuk over het klimaat", "Argumentatief"),
            ("Een kortverhaal", "Narratief"),
        ],
        "Prescriptieve teksten geven instructies, informatieve teksten feiten, argumentatieve teksten meningen met argumenten en narratieve teksten vertellen een verhaal.",
        kolommen=["Informatief", "Prescriptief", "Argumentatief", "Narratief"]),
    sorteer(
        "Is dit een teken dat een bron betrouwbaar is of eerder onbetrouwbaar?",
        ["Betrouwbaar", "Onbetrouwbaar"],
        [
            ["De auteur en de datum staan erbij.", "Betrouwbaar"],
            ["De titel schreeuwt in hoofdletters: SCHANDAAL!!!", "Onbetrouwbaar"],
            ["Andere nieuwsmedia brengen hetzelfde.", "Betrouwbaar"],
            ["De website is onbekend en heeft geen contactgegevens.", "Onbetrouwbaar"],
        ],
        "Check de auteur, de datum, de bron en of andere betrouwbare media hetzelfde melden."),
    keuze(
        "Als een krant schrijft 'betogers' en een andere 'relschoppers' over dezelfde groep, dan is dat [[*framing|een hyperbool|een verkleinwoord]]: de woordkeuze stuurt hoe je erover denkt.",
        "Framing is een bewuste keuze van woorden of beelden die een bepaald beeld oproept."),

    # Communicatie
    koppel(
        "Koppel het element van het communicatiemodel aan het voorbeeld. Een leerkracht stuurt een mail naar de ouders.",
        [
            ["zender", "de leerkracht"],
            ["ontvanger", "de ouders"],
            ["kanaal", "de mail"],
            ["ruis", "de mail belandt in de spam"],
        ],
        ["de schooldirecteur"],
        "De zender stuurt een boodschap via een kanaal naar een ontvanger. Ruis verstoort de communicatie."),

    # Tekstopbouw en structuur
    volgorde(
        "Zet de alinea's van een betoog in de juiste volgorde.",
        ["Inleiding met het onderwerp", "Standpunt", "Argument 1", "Argument 2", "Slot met conclusie"],
        "Een betoog leidt het onderwerp in, geeft het standpunt, onderbouwt het met argumenten en sluit af met een conclusie."),
    tabel(
        "Waar verwijst elk verwijswoord naar? « Mijn zus kocht een fiets bij een winkel in Gent. Ze is er erg blij mee, want die winkel gaf haar korting. »",
        [
            ("Ze", "mijn zus"),
            ("er (mee)", "de fiets"),
            ("die winkel", "een winkel in Gent"),
        ],
        "Verwijswoorden verwijzen terug naar iets wat eerder in de tekst staat.",
        kolommen=["mijn zus", "de fiets", "een winkel in Gent"]),
    keuze(
        "Een tekst die eerst een probleem beschrijft, daarna de oorzaken en ten slotte oplossingen, heeft een [[*probleemstructuur|verhaalstructuur|chronologische structuur]].",
        "De vaste tekststructuren helpen je een tekst sneller te begrijpen."),

    # Argumentatie
    tabel(
        "Is deze uitspraak een feit of een mening?",
        [
            ("België telt meer dan elf miljoen inwoners.", "Feit"),
            ("Ons land heeft de lekkerste frieten ter wereld.", "Mening"),
            ("Water kookt op zeeniveau bij 100 °C.", "Feit"),
            ("Huiswerk is volledig zinloos.", "Mening"),
        ],
        "Een feit kan je controleren. Een mening is een persoonlijk oordeel.",
        kolommen=["Feit", "Mening"]),
    mk("Welke drogreden zit in: « Iedereen in de klas heeft die schoenen, dus ze moeten wel goed zijn »?",
       ["Beroep op de massa", "Persoonlijke aanval", "Cirkelredenering", "Vals dilemma"],
       0,
       "Dat veel mensen iets doen of vinden, bewijst niet dat het juist of goed is."),

    # Lezen, multimedia
    keuze(
        "Als je een tekst snel doorloopt om te zien waarover hij gaat, dan [[*oriënteer|bestudeer|memoriseer]] je. Als je één bepaalde info zoekt, zoals een datum, dan [[*scan|bestudeer]] je.",
        "Oriënterend lezen geeft een eerste indruk. Zoekend lezen of scannen richt zich op één stukje informatie."),
    tabel(
        "Verbaal of non-verbaal?",
        [
            ("Een glimlach", "Non-verbaal"),
            ("Een geschreven uitnodiging", "Verbaal"),
            ("Armen kruisen tijdens een gesprek", "Non-verbaal"),
        ],
        "Verbale communicatie gebruikt woorden. Non-verbale communicatie gebeurt met gezicht, houding en gebaren.",
        kolommen=["Verbaal", "Non-verbaal"]),

    # Literatuur
    tabel(
        "Welk literair begrip past?",
        [
            ("Het hoogste punt van spanning in een verhaal", "Climax"),
            ("De boodschap of het centrale idee", "Thema"),
            ("Een verhaal dat begint midden in de actie", "In medias res"),
        ],
        "De climax is het spannendste moment, het thema is waar het verhaal eigenlijk over gaat, en in medias res betekent midden in de zaak.",
        kolommen=["Climax", "Thema", "In medias res"]),
    sorteer(
        "Fictie of non-fictie?",
        ["Fictie", "Non-fictie"],
        [
            ["een sciencefictionroman", "Fictie"],
            ["een biografie van een sporter", "Non-fictie"],
            ["een sprookje", "Fictie"],
            ["een reportage in de krant", "Non-fictie"],
        ],
        "Fictie is verzonnen, non-fictie gaat over echte mensen en gebeurtenissen."),

    # Taalvariëteit en identiteit
    keuze(
        "Op een sollicitatiegesprek gebruik je best [[*standaardtaal|tussentaal|een dialect]] en spreek je de werkgever aan met [[*u|jij]].",
        "In een formele situatie past standaardtaal en de beleefde vorm."),
    mk("Wat bedoelen we met een stereotype in taal en beeldvorming?",
       ["Een vereenvoudigd beeld van een hele groep mensen.", "Een uitdrukking die je enkel in je eigen dialect gebruikt.", "Een woord dat uit een andere taal ontleend is.", "Een zin die zowel een feit als een mening bevat."],
       0,
       "Een stereotype schept één beeld voor een hele groep, zonder rekening te houden met de verschillen tussen mensen."),

    # Spelling
    tabel(
        "Juist gespeld of niet?",
        [
            ("Hij antwoordt meteen.", J),
            ("Wordt jij morgen vijftien?", F),
            ("De beinvloede kiezers", F),
            ("Gisteren fietste ik naar school.", J),
        ],
        "Antwoordt: stam + t. Bij inversie met jij valt de t weg: word jij. Beïnvloed krijgt een trema. Fietste: 't kofschip.",
        ),
    keuze(
        "Ik [[*vind|vindt]] het boek spannend. Gisteren [[*verhuisden|verhuisde]] we naar Gent. Het [[*geschopte|geschopde]] blik lag op straat.",
        "Ik + stam zonder t. Bij we in het verleden komt er -den of -ten: verhuisden. Schoppen heeft stam schop: 't kofschip geeft -te."),
    tabel(
        "Waar komt het leesteken?",
        [
            ("Kom je mee naar de film ___", "?"),
            ("Ik heb drie huisdieren ___ een hond, een kat en een konijn.", ":"),
            ("Wat een prachtige dag ___", "!"),
        ],
        "Een vraag krijgt een vraagteken, een dubbelpunt kondigt een opsomming aan, en een uitroep krijgt een uitroepteken.",
        kolommen=["?", ":", "!"]),

    # Woordsoorten, morfologie en zinsbouw
    tabel(
        "Welke woordsoort heeft elk woord uit « De snelle hond rent vrolijk naar huis »?",
        [
            ("snelle", "Bijvoeglijk naamwoord"),
            ("rent", "Werkwoord"),
            ("vrolijk", "Bijwoord"),
            ("naar", "Voorzetsel"),
        ],
        "Snelle zegt iets over de hond, rent is de handeling, vrolijk zegt hoe hij rent, naar is een voorzetsel.",
        kolommen=["Werkwoord", "Bijvoeglijk naamwoord", "Bijwoord", "Voorzetsel"]),
    sorteer(
        "Is het woord een samenstelling of een afleiding?",
        ["Samenstelling", "Afleiding"],
        [
            ["voetbalveld", "Samenstelling"],
            ["vriendelijk", "Afleiding"],
            ["zonnebril", "Samenstelling"],
            ["onduidelijk", "Afleiding"],
        ],
        "Een samenstelling bestaat uit twee zelfstandige woorden. Een afleiding heeft een voor- of achtervoegsel zoals -lijk of on-."),
    tabel(
        "Welk zinsdeel is elk deel uit « Mijn broer gaf zijn vriendin gisteren een boek »?",
        [
            ("Mijn broer", "Onderwerp"),
            ("een boek", "Lijdend voorwerp"),
            ("zijn vriendin", "Meewerkend voorwerp"),
            ("gisteren", "Bijwoordelijke bepaling"),
        ],
        "Wie gaf? Mijn broer. Wat gaf hij? Een boek. Aan wie? Zijn vriendin. Wanneer? Gisteren.",
        kolommen=["Onderwerp", "Lijdend voorwerp", "Meewerkend voorwerp", "Bijwoordelijke bepaling"]),
    inv("Wat is het voltooid deelwoord van 'verhuizen'?",
        ["verhuisd"],
        "Stam verhuis, eindigt op s: niet in 't kofschip, dus -d: verhuisd."),

    # Semantiek
    koppel(
        "Koppel het begrip aan het voorbeeld.",
        [
            ["synoniem", "beginnen en starten"],
            ["antoniem", "warm en koud"],
            ["homoniem", "bank (zitbank of geldbank)"],
        ],
        ["fiets en fietsen"],
        "Synoniemen betekenen hetzelfde, antoniemen het tegengestelde, homoniemen klinken hetzelfde maar hebben een andere betekenis."),
    keuze(
        "« Dat kost een fortuin! » voor een broodje van 5 euro is een [[*hyperbool|eufemisme|metafoor]]. « Hij is heengegaan » voor 'hij is gestorven' is een [[*eufemisme|hyperbool|cliché]].",
        "Een hyperbool overdrijft, een eufemisme verzacht iets."),

    # Schrijven en spreken
    mk("Welke slotzin past in een formele mail aan een bedrijf?",
       ["Alvast bedankt voor uw reactie.", "Laters, en doe de groetjes!", "Oké, ciao, tot de volgende!", "Stuur maar snel iets terug, hè."],
       0,
       "In een formele mail blijf je beleefd en zakelijk en gebruik je u."),
    tabel(
        "Is dit een goede gewoonte in een gesprek?",
        [
            ("Laten uitspreken", J),
            ("Doorvragen als iets niet duidelijk is", J),
            ("Ondertussen op je gsm kijken", F),
            ("Samenvatten wat de ander zei", J),
        ],
        "Actief luisteren betekent aandacht geven, laten uitspreken, doorvragen en samenvatten."),

    keuze(
        "In « De leerlingen die te laat kwamen, moesten nablijven » is « die te laat kwamen » een [[*betrekkelijke bijzin|hoofdzin|bijwoordelijke bijzin]]. De persoonsvorm van de hoofdzin is [[*moesten|kwamen|nablijven]].",
        "De bijzin begint met het betrekkelijk voornaamwoord die en zegt iets over de leerlingen. In de hoofdzin is moesten de persoonsvorm."),
    tabel(
        "Hoort deze aanspreking of groet bij een formeel of een informeel register?",
        [
            ("Geachte mevrouw", "Formeel"),
            ("Hoi allemaal!", "Informeel"),
            ("Met vriendelijke groeten", "Formeel"),
            ("Tot straks, xx", "Informeel"),
        ],
        "Het register past zich aan aan de situatie en de ontvanger.",
        kolommen=["Formeel", "Informeel"]),
    mk("Welke titel past het best bij de lezersbrief over het zwembad?",
       ["Houd ons zwembad open", "Zwemmen is gezond voor iedereen", "De schepen en zijn zwemles", "Hoe duur is water in België?"],
       0,
       "De titel vat het standpunt samen: het zwembad moet openblijven."),
    inv("Welk woord in de zin « De eigenwijze kat sprong behendig op de tafel » is een bijwoord?",
        ["behendig"],
        "Behendig zegt hoe de kat sprong: het hoort bij het werkwoord en is een bijwoord."),

    # Schrijfopdracht
    open_("Schrijf een korte lezersbrief (5 à 7 zinnen) aan je gemeente. Je wil dat er een veilig fietspad komt naar je school. Geef je standpunt, twee argumenten en een slotzin.",
          "Geacht college van burgemeester en schepenen, Ik vraag u om een veilig fietspad aan te leggen naar onze school. Elke dag fietsen meer dan tweehonderd leerlingen langs een drukke weg zonder fietspad. Er gebeurden het voorbije jaar al drie ongevallen. Bovendien zullen meer ouders hun kinderen met de fiets laten gaan als het veilig is, wat minder autoverkeer geeft. Ik hoop dat u dit voorstel ernstig wil bekijken. Met vriendelijke groeten, Lies Janssens",
          "Een goed antwoord heeft een formele aanspreking, een duidelijk standpunt, minstens twee argumenten met signaalwoorden, een slotzin en een beleefde afsluiting."),
]
