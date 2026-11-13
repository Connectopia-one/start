"""De gerechtelijke piramide: rechtbanken en hoven — pittig (🌍 Beyond, filosofie en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, s_vak, GROEN, LICHT

# Prent: de piramide met enkel de hoven en rechtbanken die de gewone hoofdstukken noemen.
VAKKEN = {
    "cassatie": (380, 92, 240, 66, "Hof van Cassatie"),
    "beroep": (225, 212, 250, 66, "Hof van beroep"),
    "assisen": (525, 212, 250, 66, "Hof van Assisen"),
    "eerste": (95, 342, 300, 78, "Rechtbank van eerste aanleg"),
    "arbeid": (410, 342, 200, 78, "Arbeidsrechtbank"),
    "onderneming": (625, 342, 280, 78, "Ondernemingsrechtbank"),
    "vrede": (210, 482, 260, 72, "Vredegerecht"),
    "politie": (530, 482, 260, 72, "Politierechtbank"),
}


def _piramide():
    d = ['<polygon points="500,62 40,600 960,600" fill="#f4f1e6" stroke="#b9b29c" stroke-width="2"/>']
    for x, y, w, h, t in VAKKEN.values():
        d.append(s_vak(x, y, w, h, vul=LICHT, rand=GROEN, dikte=3, rond=14))
        d.append(s_tekst(x + w / 2, y + h / 2 + 7, t, 20, vet=True))
    return d


def zone(k):
    x, y, w, h, _ = VAKKEN[k]
    return pix_zone(x, y, w, h)


PRENTEN_EIGEN = [dict(naam="gerechtelijke-piramide", titel="De gerechtelijke piramide (vereenvoudigd)", eigen=_piramide)]
P = "gerechtelijke-piramide.svg"

VRAGEN = [
    klik("Twee buren hebben ruzie over een overhangende boom. Klik op de rechter die hier materieel bevoegd is.", P, [zone("vrede")],
         "Burenhinder, huur en kleine geldsommen horen bij het vredegerecht, de rechter die het dichtst bij het dagelijks leven staat."),
    klik("Een bestuurder rijdt door het rood en veroorzaakt een ongeval. Klik op de bevoegde rechtbank.", P, [zone("politie")],
         "De politierechtbank is de rechtbank voor het verkeer, niet de rechtbank van de politie."),
    klik("Een werknemer betwist zijn ontslag. Klik op de bevoegde rechtbank.", P, [zone("arbeid")],
         "Alles tussen werkgever en werknemer, en geschillen over sociale zekerheid, horen bij de arbeidsrechtbank."),
    klik("Een bedrijf gaat failliet. Klik op de bevoegde rechtbank.", P, [zone("onderneming")],
         "Faillissementen en geschillen tussen ondernemingen horen bij de ondernemingsrechtbank."),
    klik("Twee ouders scheiden en zijn het niet eens over het onderhoudsgeld. Klik op de rechtbank waarvan de familierechtbank een afdeling is.", P, [zone("eerste")],
         "De familierechtbank is een afdeling van de rechtbank van eerste aanleg, net als de correctionele, de jeugd-, de burgerlijke en de strafuitvoeringsrechtbank."),
    klik("Iemand wordt beschuldigd van een moord. Klik op het hof dat met een volksjury oordeelt.", P, [zone("assisen")],
         "Het Hof van Assisen behandelt de zwaarste misdaden, met twaalf gezworenen."),
    klik("Een partij is het niet eens met het vonnis van de rechtbank van eerste aanleg en wil dat de feiten en het recht opnieuw bekeken worden. Klik op waar ze naartoe gaat.", P, [zone("beroep")],
         "In beroep komen de feiten en het recht opnieuw aan bod. Het hof van beroep spreekt een arrest uit."),
    klik("Klik op het hof dat enkel nakijkt of het recht juist werd toegepast, en niet of de feiten kloppen.", P, [zone("cassatie")],
         "Het Hof van Cassatie staat bovenaan en is geen derde aanleg: het kijkt enkel naar de toepassing van het recht."),
    sorteer(
        "Welke rechter of rechtbank is materieel bevoegd?",
        ["Vredegerecht", "Politierechtbank", "Arbeidsrechtbank", "Ondernemingsrechtbank"],
        [
            ("Een huurder en een verhuurder ruziën over de huurwaarborg.", "Vredegerecht"),
            ("Een fietser en een auto botsen op een kruispunt.", "Politierechtbank"),
            ("Iemand krijgt zijn werkloosheidsuitkering geweigerd.", "Arbeidsrechtbank"),
            ("Twee firma's ruziën over een onbetaalde factuur voor een grote levering.", "Ondernemingsrechtbank"),
        ],
        "Huur: vredegerecht. Verkeer: politierechtbank. Werk en sociale zekerheid: arbeidsrechtbank. Ondernemingen onderling: ondernemingsrechtbank.",
    ),
    sorteer(
        "Bij welke afdeling van de rechtbank van eerste aanleg hoort deze zaak?",
        ["Correctioneel", "Familie", "Jeugd", "Strafuitvoering"],
        [
            ("Een inbraak in een winkel, een wanbedrijf", "Correctioneel"),
            ("Een vechtpartij met verwondingen", "Correctioneel"),
            ("Een scheiding met ruzie over de kinderen", "Familie"),
            ("Een veertienjarige in een zorgwekkende situatie thuis", "Jeugd"),
            ("Een gedetineerde vraagt een voorwaardelijke vrijlating", "Strafuitvoering"),
        ],
        "Wanbedrijven: correctioneel. Gezin: familie. Minderjarigen: jeugd. Hoe een straf verder uitgevoerd wordt: strafuitvoering.",
    ),
    tabel(
        "Gaat het hier om de territoriale of om de materiële bevoegdheid?",
        [
            ("Het is een huurgeschil, dus het vredegerecht.", "Materieel"),
            ("De verweerder woont in Genk, dus het kanton Genk.", "Territoriaal"),
            ("Het is een verkeersongeval, dus de politierechtbank.", "Materieel"),
            ("Het misdrijf gebeurde in Antwerpen, dus een rechtbank daar.", "Territoriaal"),
        ],
        "Materieel: de aard en de omvang van de zaak. Territoriaal: de plaats, doorgaans de woonplaats van de verweerder of de plaats van het misdrijf.",
        kolommen=["Materieel", "Territoriaal"],
    ),
    casus(
        "Sara uit Hasselt verhuurt een appartement aan Jonas, die ook in Hasselt woont. Jonas betaalt al drie maanden geen huur. Sara wil haar geld terug en wil dat Jonas vertrekt.",
        [
            mk("Welke rechter is materieel bevoegd?",
               ["De politierechtbank", "Het vredegerecht", "Het hof van beroep", "De ondernemingsrechtbank"], 1,
               "Huurgeschillen horen bij het vredegerecht."),
            mk("Welke vraag beantwoord je met de territoriale bevoegdheid?",
               ["Of het een huurzaak of een verkeerszaak is",
                "In welk kanton of welke plaats de zaak thuishoort",
                "Of Jonas schuldig is",
                "Hoeveel huur Jonas moet betalen"], 1,
               "Eerst wat voor zaak het is (materieel), dan waar ze thuishoort (territoriaal). Hier is dat het kanton Hasselt."),
            mk("De vrederechter geeft Sara gelijk. Jonas is het daar niet mee eens. Wat kan hij doen?",
               ["Meteen naar het Hof van Cassatie stappen om zijn verhaal opnieuw te doen",
                "In beroep gaan, binnen de wettelijke termijn",
                "Wachten zo lang hij wil en dan in beroep gaan",
                "Niets, tegen een vrederechter is nooit iets mogelijk"], 1,
               "Tegen een vonnis kan je in beroep gaan, maar enkel binnen een korte wettelijke termijn."),
        ],
    ),
    volgorde(
        "Zet van onder naar boven in de piramide.",
        ["Een rechtbank", "Het hof van beroep", "Het Hof van Cassatie"],
        "Breed onderaan met veel rechtbanken, en één Hof van Cassatie bovenaan.",
    ),
    tabel(
        "Juist of fout over beroep en cassatie?",
        [
            ("In beroep komen de feiten en het recht opnieuw aan bod.", J),
            ("Het Hof van Cassatie behandelt de feiten opnieuw.", F),
            ("Het Hof van Cassatie verbreekt een arrest en stuurt de zaak naar een ander hof.", J),
            ("Tegen een uitspraak van het Hof van Assisen bestaat er een gewoon beroep.", F),
            ("Een hof spreekt een arrest uit, een rechtbank een vonnis.", J),
        ],
        "Beroep is een tweede volledige behandeling. Cassatie kijkt enkel naar het recht. Na assisen blijft enkel cassatie over.",
        kolommen=["Juist", "Fout"],
    ),
    keuze(
        "Een rechtbank spreekt een [[*vonnis|arrest]] uit, een hof een [[*arrest|vonnis]]. Het Hof van Cassatie is [[*geen|wel een]] derde aanleg.",
        "Vonnis bij een rechtbank, arrest bij een hof. Cassatie kijkt enkel naar de toepassing van het recht.",
    ),
    mk(
        "Na een uitspraak van het Hof van Assisen blijft enkel cassatie over. Wat is daar de reden van?",
        ["Omdat assisenzaken te weinig voorkomen om een beroep te organiseren",
         "Omdat een jury van burgers al over de feiten oordeelde",
         "Omdat de beklaagde altijd vrijgesproken wordt",
         "Omdat het Hof van Assisen boven het Hof van Cassatie staat"],
        1,
        "Een jury van burgers oordeelde al over de feiten. De weg die overblijft, is cassatie, en die gaat over het recht.",
    ),
    mk(
        "Iemand eist 3000 euro terug van een kennis die het geleende geld niet teruggeeft. Wie is materieel bevoegd?",
        ["Het vredegerecht", "De politierechtbank", "Het Hof van Cassatie", "De arbeidsrechtbank"],
        0,
        "Kleine geldsommen tot 5000 euro gaan naar de vrederechter.",
    ),
    mk(
        "Wat doet het Hof van Cassatie als het vindt dat een hof van beroep het recht verkeerd toepaste?",
        ["Het spreekt zelf een nieuwe straf uit",
         "Het verbreekt het arrest en verwijst de zaak naar een ander hof",
         "Het hoort alle getuigen opnieuw en beslist dan zelf over de feiten",
         "Het laat het arrest gewoon staan"],
        1,
        "Cassatie verbreekt en verwijst. Een ander hof behandelt de zaak dan opnieuw.",
    ),
    mk(
        "Wat is juist over het Hof van Assisen?",
        ["Het is een vaste rechtbank met dezelfde rechters voor elke zaak",
         "Het wordt per zaak samengesteld, met twaalf gezworenen",
         "Het behandelt verkeersovertredingen",
         "Het oordeelt zonder burgers"],
        1,
        "Het Hof van Assisen is geen vaste rechtbank: het wordt per zaak samengesteld en twaalf burgers zetelen als gezworenen.",
    ),
    mk(
        "Waarom geldt er een korte termijn om in beroep te gaan?",
        ["Zodat een zaak niet eindeloos open blijft en er rechtszekerheid is",
         "Zodat de rechtbank minder dossiers in haar archief moet bewaren",
         "Omdat beroep enkel voor rijke mensen bedoeld is",
         "Omdat het Hof van Cassatie dat zo vraagt"],
        0,
        "Na de termijn staat de uitspraak vast. Iedereen weet dan waar hij aan toe is.",
    ),
    tabel(
        "Juist of fout over de rechtbank van eerste aanleg?",
        [
            ("De jeugdrechtbank is een afdeling van de rechtbank van eerste aanleg.", J),
            ("De politierechtbank is een afdeling van de rechtbank van eerste aanleg.", F),
            ("De correctionele rechtbank behandelt wanbedrijven.", J),
            ("De strafuitvoeringsrechtbank beslist of iemand schuldig is.", F),
            ("De familierechtbank is een aparte rechtbank naast de rechtbank van eerste aanleg.", F),
            ("De burgerlijke rechtbank behandelt geschillen tussen burgers die niet bij een andere rechter horen.", J),
        ],
        "Vijf afdelingen: burgerlijk, correctioneel, familie, jeugd en strafuitvoering. De politierechtbank staat er los van, op het niveau van het vredegerecht.",
        kolommen=["Juist", "Fout"],
    ),
    koppel(
        "Verbind elk hof of elke rechtbank met wat het doet.",
        [
            ("Hof van beroep", "Bekijkt feiten en recht een tweede keer"),
            ("Hof van Cassatie", "Kijkt enkel na of het recht juist werd toegepast"),
            ("Hof van Assisen", "Oordeelt met gezworenen over de zwaarste misdaden"),
            ("Vredegerecht", "Regelt huur, burenhinder en kleine geldsommen"),
        ],
        ["Beslist over de woonplaats van de verweerder"],
        "Elke trede van de piramide heeft haar eigen taak.",
    ),
    sleep(
        "Een rechtbank spreekt een [[vonnis]] uit. Wie het daar niet mee eens is, kan binnen de [[termijn]] in [[beroep]] gaan. Het hof spreekt dan een [[arrest]] uit.",
        ["cassatie", "gezworene"],
        "Vonnis, beroep binnen de termijn, arrest.",
    ),
    inv(
        "Hoeveel gezworenen zetelen er in het Hof van Assisen?",
        ["12", "twaalf"],
        "Twaalf burgers worden per zaak uitgeloot als gezworene.",
    ),
    keuze(
        "Een verkeersongeval gaat naar de [[*politierechtbank|correctionele rechtbank]]. Een faillissement gaat naar de [[*ondernemingsrechtbank|arbeidsrechtbank]].",
        "Verkeer: politierechtbank. Ondernemingen: ondernemingsrechtbank.",
    ),
    tabel(
        "Juist of fout over bevoegdheid?",
        [
            ("Om de juiste rechter te vinden, kijk je naar de aard van de zaak en naar de plaats.", J),
            ("De materiële bevoegdheid hangt af van waar de partijen wonen.", F),
            ("Een zaak van 4000 euro kan naar het vredegerecht.", J),
            ("Elke burger mag zelf kiezen bij welke rechter hij gaat.", F),
        ],
        "Materieel: aard en omvang. Territoriaal: plaats. Je kiest de rechter niet zelf.",
        kolommen=["Juist", "Fout"],
    ),
    volgorde(
        "Zet de stappen van een zaak die tot in cassatie gaat in de juiste volgorde.",
        ["Vonnis van de rechtbank", "Beroep binnen de termijn", "Arrest van het hof van beroep", "Voorziening bij het Hof van Cassatie"],
        "Eerst de rechtbank, dan het hof van beroep, en pas daarna kan cassatie volgen.",
    ),
    inv(
        "Hoe heet de bevoegdheid die bepaalt welke rechtbank bevoegd is volgens de plaats? De ... bevoegdheid",
        ["territoriale", "territoriaal"],
        "Territoriaal gaat over de plaats, materieel over de aard en de omvang van de zaak.",
    ),
]
