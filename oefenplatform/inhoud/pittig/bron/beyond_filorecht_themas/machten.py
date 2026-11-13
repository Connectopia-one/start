"""De scheiding der machten en de rechterlijke macht — pittig (🌍 Beyond, filosofie en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, s_vak, GROEN, LICHT

# Prent: vijf Belgische instellingen, zonder te zeggen welke macht ze zijn.
VAKKEN = {
    "parlement": (60, 120, 260, 120, "Parlement"),
    "regering": (370, 120, 260, 120, "Regering"),
    "hoven": (680, 120, 260, 120, "Hoven en rechtbanken"),
    "gwh": (170, 380, 290, 120, "Grondwettelijk Hof"),
    "rvs": (540, 380, 290, 120, "Raad van State"),
}


def _instellingen():
    d = []
    for x, y, w, h, t in VAKKEN.values():
        d.append(s_vak(x, y, w, h, vul=LICHT, rand=GROEN, dikte=3, rond=18))
        d.append(s_tekst(x + w / 2, y + h / 2 + 8, t, 21 if len(t) > 16 else 24, vet=True))
    return d


def zone(k):
    x, y, w, h, _ = VAKKEN[k]
    return pix_zone(x, y, w, h)


PRENTEN_EIGEN = [dict(naam="machten-instellingen", titel="Vijf Belgische instellingen", eigen=_instellingen)]
P = "machten-instellingen.svg"

VRAGEN = [
    klik("Klik op de instelling die de wetten maakt.", P, [zone("parlement")],
         "Het parlement is de wetgevende macht: het maakt de wetten en controleert de regering."),
    klik("Klik op de instelling die de wetten uitvoert.", P, [zone("regering")],
         "De regering en haar administratie zijn de uitvoerende macht."),
    klik("Klik op de instelling die de wet toepast op een concreet geschil tussen twee buren.", P, [zone("hoven")],
         "De hoven en rechtbanken zijn de rechterlijke macht: ze spreken recht in een concrete zaak."),
    klik("Klik op de instelling die nagaat of een wet in overeenstemming is met de grondwet.", P, [zone("gwh")],
         "Het Grondwettelijk Hof toetst wetten aan de grondwet. Zo staat ook de wetgever onder toezicht."),
    klik("Een burger vindt een beslissing van een minister onrechtmatig en wil ze laten vernietigen. Klik op de instelling waar hij terechtkan.", P, [zone("rvs")],
         "De Raad van State kan beslissingen van het bestuur nakijken en vernietigen."),
    klik("Klik op de instelling die de regering controleert met vragen en met haar stem over de begroting.", P, [zone("parlement")],
         "Het parlement controleert de regering. Zonder zijn steun geraakt een regering niet aan haar geld en haar wetten."),
    tabel(
        "Bij welke macht hoort deze instelling of taak?",
        [
            ("De wetten maken", "Wetgevend"),
            ("Een vonnis vellen in een diefstalzaak", "Rechterlijk"),
            ("Een nieuwe wet in de praktijk brengen", "Uitvoerend"),
            ("De regering controleren", "Wetgevend"),
            ("De hoven en rechtbanken", "Rechterlijk"),
            ("De ministers en hun administratie", "Uitvoerend"),
        ],
        "Wetgevend: de parlementen maken wetten en controleren de regering. Uitvoerend: de regeringen voeren uit. Rechterlijk: de hoven en rechtbanken spreken recht.",
        kolommen=["Wetgevend", "Uitvoerend", "Rechterlijk"],
    ),
    keuze(
        "De scheiding der machten werd in de [[*18de|16de]] eeuw uitgewerkt door [[*Montesquieu|Descartes|Kant]]. Ze voorkomt dat [[*alle macht in dezelfde handen|het parlement in één gebouw]] terechtkomt.",
        "Montesquieu werkte de gedachte uit in de eeuw van de Verlichting. Macht die zichzelf controleert, controleert niets.",
    ),
    casus(
        "Bron: een fictief land, Ardonië. De president maakt de wetten zelf per decreet. Zijn ministers voeren ze uit. Wie het niet eens is, kan naar de rechtbank, maar de rechters worden door de president benoemd en kunnen door hem op elk moment ontslagen worden.",
        [
            mk("Wat mankeert er in Ardonië?",
               ["Er zijn te weinig ministers om alle wetten uit te voeren",
                "De drie machten liggen in feite bij één persoon",
                "Er bestaat geen enkele rechtbank in het land",
                "De rechters zijn te streng voor de burgers"], 1,
               "De president maakt de wetten, stuurt de uitvoering en houdt de rechters in zijn hand. Er is geen scheiding der machten."),
            mk("Waarom is de rechtbank in Ardonië geen echt tegengewicht?",
               ["Omdat de rechters er niet genoeg gestudeerd hebben",
                "Wie ontslagen kan worden, oordeelt niet vrij",
                "Omdat burgers er niet naar de rechtbank mogen gaan",
                "Omdat er geen wetten zijn om toe te passen"], 1,
               "Een rechter die zijn plaats kan verliezen door een onwelkom vonnis, is geen onafhankelijke rechter."),
            mk("Welke Belgische regel zou dit probleem voorkomen?",
               ["Dat rechters voortaan door de bevolking verkozen worden",
                "Een vaste benoeming via een onafhankelijke instelling",
                "Dat de minister van Justitie de vonnissen nakijkt",
                "Dat het parlement de rechters mag afzetten"], 1,
               "In België lopen benoemingen via een onafhankelijke instelling die op bekwaamheid selecteert, en zijn rechters vast benoemd."),
        ],
    ),
    sorteer(
        "Is dit een voorbeeld van controle en evenwicht, of een schending van de scheiding der machten?",
        ["Controle en evenwicht", "Schending"],
        [
            ("Het parlement stemt de begroting van de regering weg.", "Controle en evenwicht"),
            ("Het Grondwettelijk Hof vernietigt een wet die tegen de grondwet ingaat.", "Controle en evenwicht"),
            ("De Raad van State vernietigt een vergunning die onwettig werd toegekend.", "Controle en evenwicht"),
            ("Een minister belt een rechter om een zware straf te vragen.", "Schending"),
            ("De regering weigert een vonnis uit te voeren dat haar niet past.", "Schending"),
            ("Het parlement stemt een wet die één lopende rechtszaak in het voordeel van één partij beslecht.", "Schending"),
        ],
        "De machten houden elkaar binnen hun grenzen met de middelen die het systeem hun geeft. Een macht die het werk van een andere overneemt of negeert, schendt de scheiding.",
    ),
    mk(
        "Iemand zegt: \"De drie machten hebben niets met elkaar te maken.\" Wat klopt daar niet aan?",
        ["Ze zitten wel degelijk allemaal in afzonderlijke steden",
         "Ze houden elkaar in het oog en werken op elkaar in",
         "Omdat de machten elkaar nooit mogen ontmoeten of spreken",
         "Omdat er eigenlijk maar één macht is"],
        1,
        "Het parlement controleert de regering, de rechter toetst het bestuur. Elkaar in het oog houden hoort bij het ontwerp.",
    ),
    mk(
        "Een regering klaagt dat het parlement \"alles vertraagt\" met vragen en onderzoeken. Hoe kijk je daar vanuit de scheiding der machten naar?",
        ["De regering heeft gelijk: een goed bestuur moet zo snel mogelijk gaan",
         "Die traagheid is geen fout maar een bedoeling: ze begrenst de macht",
         "Het parlement mag de regering eigenlijk niet controleren",
         "De rechter moet de vragen van het parlement verbieden"],
        1,
        "De scheiding der machten bestaat om macht te begrenzen, niet om bestuur te versnellen.",
    ),
    tabel(
        "Juist of fout over de rechterlijke macht in België?",
        [
            ("Rechters worden door de bevolking verkozen.", F),
            ("Een rechter moet zijn vonnis motiveren.", J),
            ("De minister van Justitie mag een rechter zeggen welke straf hij oplegt.", F),
            ("Een vaste benoeming beschermt de onafhankelijkheid van de rechter.", J),
            ("Een rechter mag zelf nieuwe wetten schrijven.", F),
        ],
        "Rechters worden benoemd via een onafhankelijke instelling, vast benoemd, en motiveren hun vonnis. Ze passen de wet toe en schrijven ze niet.",
        kolommen=["Juist", "Fout"],
    ),
    casus(
        "Een rechter veroordeelt een bekende zakenman. In zijn vonnis legt hij op vier bladzijden uit welke bewijzen hij gebruikte en waarom hij de argumenten van de verdediging niet volgde.",
        [
            mk("Waarom moet de rechter zijn vonnis zo motiveren?",
               ["Om te tonen hoeveel hij over het recht weet",
                "Zodat iedereen kan nagaan waarop zijn beslissing berust",
                "Omdat een vonnis van minder dan vier bladzijden ongeldig is",
                "Omdat de minister dat zo gevraagd heeft"], 1,
               "Een gemotiveerd vonnis is te controleren en in beroep aan te vechten. Dat hoort bij een eerlijk proces."),
            mk("Wat kan de zakenman doen als hij het niet eens is?",
               ["In beroep gaan bij een hogere rechter",
                "De minister vragen om het vonnis te schrappen",
                "Het parlement vragen om een wet die zijn zaak beslecht",
                "Het vonnis gewoon negeren"], 0,
               "De weg tegen een vonnis is het beroep, niet het negeren en niet de politiek."),
        ],
    ),
    sleep(
        "Het [[parlement]] maakt de wetten. De [[regering]] voert ze uit. De [[hoven]] en rechtbanken spreken recht. Zo heeft elke macht middelen om de andere binnen hun grenzen te houden: dat heet controle en [[evenwicht]].",
        ["koning", "pers", "gemeente"],
        "Drie taken, drie plaatsen, en een wederzijdse rem.",
    ),
    mk(
        "Een partij stelt voor om rechters voortaan te laten verkiezen. Welk bezwaar past?",
        ["Er zouden niet genoeg kandidaten zijn voor alle rechtbanken van het land",
         "Wie stemmen moet halen, wordt afhankelijk van wat populair is",
         "Omdat het parlement de rechters liever zelf kiest",
         "Omdat verkiezingen te veel geld kosten"],
        1,
        "Een rechter moet ook een impopulair vonnis kunnen vellen. Daarom loopt zijn benoeming via een onafhankelijke instelling.",
    ),
    casus(
        "Bron: een krantenbericht. \"Het Grondwettelijk Hof heeft een deel van een nieuwe wet vernietigd. Volgens het Hof schond de wet het gelijkheidsbeginsel uit de grondwet. De regering betreurt de uitspraak, maar zal de wet aanpassen.\"",
        [
            mk("Welke macht wordt hier gecontroleerd?",
               ["De rechterlijke macht", "De wetgevende macht", "De uitvoerende macht", "Geen enkele macht"], 1,
               "Het Hof toetst een wet, en wetten zijn het werk van het parlement: de wetgevende macht."),
            mk("Wat toont de reactie van de regering?",
               ["Dat de regering het Hof kan negeren als ze dat zelf wil",
                "Dat ze de uitspraak aanvaardt, ook al bevalt ze haar niet",
                "Dat het Hof eigenlijk bij de regering hoort",
                "Dat de regering de rechters zal ontslaan"], 1,
               "Een uitspraak volgen die je niet bevalt, is precies hoe controle en evenwicht hoort te werken."),
            keuze("Zo staat ook de [[*wetgever|rechter]] onder toezicht: een meerderheid in het parlement kan niet [[*alles|niets]] in een wet zetten wat ze wil.",
                  "Het Grondwettelijk Hof begrenst de wetgever met de grondwet."),
        ],
    ),
    tabel(
        "Welke macht oefent deze controle uit?",
        [
            ("Vragen stellen aan een minister", "Wetgevend"),
            ("Een wet toetsen aan de grondwet", "Rechterlijk toezicht"),
            ("Een onwettige vergunning vernietigen", "Rechterlijk toezicht"),
            ("De begroting goedkeuren of verwerpen", "Wetgevend"),
        ],
        "Het parlement controleert de regering met vragen en de begroting. Het Grondwettelijk Hof en de Raad van State toetsen wetten en bestuursbeslissingen aan het recht.",
        kolommen=["Wetgevend", "Rechterlijk toezicht"],
    ),
    mk(
        "Welke uitleg past bij het begrip controle en evenwicht?",
        ["Dat de drie machten precies even groot en even sterk moeten zijn",
         "Dat de regering de twee andere machten mag besturen",
         "Elke macht kan de andere binnen hun grenzen houden",
         "Dat de machten elk om beurt een jaar regeren"],
        2,
        "Geen gelijke grootte, maar een wederzijdse rem: controleren, toetsen, weigeren.",
    ),
    sorteer(
        "Bij welke macht hoort deze persoon?",
        ["Wetgevend", "Uitvoerend", "Rechterlijk"],
        [
            ("Een volksvertegenwoordiger", "Wetgevend"),
            ("Een minister", "Uitvoerend"),
            ("Een rechter in een rechtbank van eerste aanleg", "Rechterlijk"),
            ("Een raadsheer in een hof van beroep", "Rechterlijk"),
        ],
        "Volksvertegenwoordigers zitten in het parlement, ministers in de regering, rechters en raadsheren in de hoven en rechtbanken.",
    ),
    mk(
        "De minister van Justitie organiseert het gerecht. Wat mag hij níet?",
        ["Geld vrijmaken voor nieuwe rechtbanken",
         "Een rechter zeggen hoe hij in een zaak moet oordelen",
         "Een wetsontwerp over het gerecht indienen bij het parlement",
         "Vragen van het parlement beantwoorden"],
        1,
        "Hij organiseert justitie als dienst, maar raakt nooit aan het oordeel zelf.",
    ),
    tabel(
        "Juist of fout over de scheiding der machten?",
        [
            ("Ze is een van de principes van een democratische rechtsstaat.", J),
            ("Ze bestaat om bestuur sneller te maken.", F),
            ("Een macht die zichzelf controleert, is een goed tegengewicht.", F),
            ("Het parlement heeft twee taken: wetten maken en de regering controleren.", J),
        ],
        "De scheiding der machten begrenst macht. Macht die zichzelf controleert, controleert niets.",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        "Welk hof toetst in België of een wet in overeenstemming is met de grondwet? Het ... Hof",
        ["Grondwettelijk", "grondwettelijk", "Grondwettelijk Hof"],
        "Het Grondwettelijk Hof houdt ook de wetgever binnen de grenzen van de grondwet.",
    ),
    sleep(
        "De [[Raad van State]] kan beslissingen van het bestuur vernietigen. Het [[Grondwettelijk Hof]] toetst wetten aan de grondwet. Zo is niet alleen de burger, maar ook de [[overheid]] aan het recht gebonden.",
        ["Senaat", "koning", "minister"],
        "Twee instellingen die het bestuur en de wetgever binnen de grenzen van het recht houden.",
    ),
    inv(
        "Wetten maken, wetten uitvoeren en recht spreken liggen in verschillende handen. Hoe heet dat principe? De ... der machten",
        ["scheiding"],
        "De scheiding der machten is een van de principes van de democratische rechtsstaat.",
    ),
]
