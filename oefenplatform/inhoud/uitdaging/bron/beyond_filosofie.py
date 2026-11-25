# -*- coding: utf-8 -*-
"""Uitdaging Filosofie en recht 🌍 Beyond (25 november 2026), in de vormen van
het examen van de Examencommissie: 40 vragen die filosofie, ethiek,
argumentatieleer en recht door elkaar halen. Casussen, tabellen,
keuzelijsten, koppelen, sorteren, volgorde, vier klikvragen op twee zelf
getekende prenten en een open vraag. Geen nieuwe leerstof: alles staat in de
hoofdstukken van Filosofie en recht Beyond.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_filosofie.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Filosofie en recht"
BESTAND = "beyond-filosofie-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/filosofie-beyond-uitdaging"
PIRAMIDE = "gerechtelijke-piramide.svg"
REDENERINGEN = "vier-redeneringen.svg"
# klikvakken: zie maak_prenten_beyond_filosofie.py
CASSATIE = [33.5, 14.3, 33.0, 17.1]
VREDEGERECHT = [2.0, 73.2, 47.3, 17.1]
KAART_C = [3.0, 57.1, 46.0, 39.3]
KAART_D = [51.0, 57.1, 46.0, 39.3]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # De gerechtelijke piramide (prent)
    klik("Bekijk de gerechtelijke piramide. Klik op het rechtscollege dat enkel nagaat of het recht juist is toegepast, en niet opnieuw naar de feiten kijkt.",
         PIRAMIDE, [CASSATIE],
         "Het Hof van Cassatie staat bovenaan. Het oordeelt niet opnieuw over de feiten, maar kijkt na of de rechters de wet juist hebben toegepast."),
    klik("Je huisbaas houdt je huurwaarborg onterecht in. Klik op het rechtscollege waar je met dit huurgeschil terechtkunt.",
         PIRAMIDE, [VREDEGERECHT],
         "Het vredegerecht behandelt huurgeschillen, burenhinder en kleine geldsommen."),
    met_prent(PIRAMIDE, keuze(
        "De uitspraak van een rechtbank heet een [[*vonnis|arrest|dagvaarding]]. De uitspraak van een hof heet een [[*arrest|vonnis|proces-verbaal]].",
        "Rechtbanken spreken vonnissen uit, hoven arresten. Een dagvaarding roept iemand voor de rechter, ze is geen uitspraak.")),
    met_prent(PIRAMIDE, tabel(
        "Klopt dit over de piramide?",
        [
            ("Tegen een uitspraak van het hof van assisen bestaat geen gewoon hoger beroep.", J),
            ("Wanbedrijven komen voor het vredegerecht.", F),
            ("De materiële bevoegdheid gaat over de aard van de zaak.", J),
            ("Een hof van beroep behandelt een zaak opnieuw.", J),
        ],
        "Bij assisen oordeelde een jury al over de feiten, dus blijft enkel cassatie over. Wanbedrijven gaan naar de correctionele rechtbank. De territoriale bevoegdheid gaat over de plaats.")),
    met_prent(PIRAMIDE, mk(
        "Een werknemer wordt ontslagen en vindt de reden onterecht. Bij welke rechtbank begint zijn zaak?",
        ["bij de politierechtbank", "bij de arbeidsrechtbank", "bij het Hof van Cassatie", "bij het hof van assisen"],
        1,
        "Geschillen over werk, ontslag en sociale zekerheid horen bij de arbeidsrechtbank.")),

    # Vier redeneringen (prent)
    klik("Bekijk de vier redeneringen. Klik op de geldige redenering die het consequens ontkent.",
         REDENERINGEN, [KAART_D],
         "D zegt: het ijs is niet dik, dus het vriest niet. Je ontkent het consequens en besluit tot de ontkenning van het antecedens: een modus tollens. Die is geldig."),
    klik("Klik op de ongeldige redenering die het antecedens ontkent.",
         REDENERINGEN, [KAART_C],
         "C zegt: het vriest niet, dus het ijs is niet dik. Maar het ijs kan ook dik zijn om een andere reden, bijvoorbeeld na een vorstperiode die net voorbij is. Een ontkenning van het antecedens is ongeldig."),
    met_prent(REDENERINGEN, tabel(
        "Is elke redenering over de vijver geldig of ongeldig?",
        [
            ("A", "Geldig"),
            ("B", "Ongeldig"),
            ("C", "Ongeldig"),
            ("D", "Geldig"),
        ],
        "Geldig zijn de modus ponens (A) en de modus tollens (D). De bevestiging van het consequens (B) en de ontkenning van het antecedens (C) zijn ongeldig.",
        kolommen=["Geldig", "Ongeldig"])),
    met_prent(REDENERINGEN, mk(
        "Hoe heet de redeneervorm van B?",
        ["de modus ponens", "de bevestiging van het consequens", "de ontkenning van het antecedens", "de modus tollens"],
        1,
        "B bevestigt het consequens (het ijs is dik) en besluit tot het antecedens (het vriest). Dat is ongeldig: het ijs kan ook om een andere reden dik zijn.")),
    met_prent(REDENERINGEN, keuze(
        "In de eerste zin van elke kaart is 'het vriest' het [[*antecedens|consequens|besluit]].",
        "Het antecedens gaat vooraf: het staat na 'als'. Het consequens is wat volgt als het antecedens waar is.")),

    # Casus: een dilemma in het ziekenhuis
    casus(
        "Een arts heeft vijf patiënten die elk dringend een ander orgaan nodig hebben. In de wachtzaal zit een gezonde bezoeker. Met zijn organen zou de arts de vijf kunnen redden.",
        [
            mk("Waarom is dit voor de gevolgenethiek een lastig voorbeeld?",
               ["Omdat de gevolgenethiek enkel naar regels kijkt en nooit naar gevolgen.", "Omdat een optelsom de ene kan opofferen voor de vijf.", "Omdat de gevolgenethiek zegt dat de arts eerst voor zichzelf moet zorgen.", "Omdat de gevolgenethiek niet over leven en dood wil oordelen."],
               1,
               "Wie enkel het totale geluk telt, komt uit bij vijf levens tegen één. Dat een minderheid zo geofferd kan worden, is een bekend bezwaar tegen de gevolgenethiek."),
            keuze(
                "Volgens Kant mag de arts de bezoeker [[*niet|wel]] gebruiken, want je mag een mens nooit louter als [[*middel|doel]] behandelen.",
                "De plichtethiek van Kant kijkt niet naar de afweging van gevolgen. Een mens heeft een waardigheid die je niet mag inruilen."),
            koppel(
                "Welke ethische vraag hoort bij elke benadering?",
                [
                    ["Wat levert het meeste geluk op voor zoveel mogelijk mensen?", "gevolgenethiek"],
                    ["Welke plicht geldt hier, wat de gevolgen ook zijn?", "plichtethiek"],
                    ["Wat zou een goede, rechtvaardige arts doen?", "deugdethiek"],
                    ["Wat heeft de concrete mens die voor me staat nodig?", "zorgethiek"],
                ],
                ["moreel relativisme", "determinisme"],
                "Elke normatieve benadering stelt een andere kernvraag: gevolgen, plicht, karakter of de concrete relatie."),
            tabel(
                "Klopt dit over dit dilemma?",
                [
                    ("Elke mogelijke keuze kost hier iets van waarde.", J),
                    ("Een moreel universalist vindt dat het antwoord van land tot land mag verschillen.", F),
                    ("Zonder vrije wil kan je de arts moeilijk verantwoordelijk stellen.", J),
                ],
                "Bij een moreel dilemma verlies je altijd iets. Een universalist gelooft net in regels die overal gelden. De vrije wil is een basisbegrip van de ethiek."),
        ],
    ),

    # Casus: een gestolen fiets
    casus(
        "Tom wordt door de politie betrapt terwijl hij een fiets steelt aan het station. De eigenaar wil zijn schade vergoed zien.",
        [
            volgorde(
                "Zet de stappen van een mogelijke strafprocedure in de juiste volgorde.",
                ["De politie maakt een proces-verbaal op.", "De procureur leidt het opsporingsonderzoek.", "Tom wordt gedagvaard.", "Het onderzoek ter terechtzitting vindt plaats.", "De rechter spreekt een vonnis uit."],
                "Het proces-verbaal gaat naar het parket. De procureur onderzoekt de zaak en kan Tom dagvaarden. Daarna volgt het proces in de rechtszaal en tot slot het vonnis."),
            mk("Diefstal is een wanbedrijf. Voor welke rechtbank komt Tom?",
               ["voor de correctionele rechtbank", "voor het vredegerecht van zijn gemeente", "voor het hof van assisen", "voor de arbeidsrechtbank"],
               0,
               "Wanbedrijven, de middelzware misdrijven, gaan naar de correctionele rechtbank."),
            inv("Hoe heet de eigenaar van de fiets als hij zich bij het strafproces aansluit om zijn schade terug te krijgen? De ... partij",
                ["burgerlijke"],
                "Het slachtoffer dat zich aansluit bij een strafproces om zijn schade vergoed te zien, is de burgerlijke partij."),
            tabel(
                "Klopt dit over de zaak van Tom?",
                [
                    ("Het parket kan beslissen om de zaak te seponeren.", J),
                    ("Een krant mag Tom al een dief noemen voor het vonnis valt.", F),
                    ("Tom heeft recht op een advocaat die hem bijstaat.", J),
                ],
                "Seponeren betekent dat het parket niet verder vervolgt. Het vermoeden van onschuld geldt tot het vonnis. Iedereen heeft recht op een eerlijk proces, met een advocaat."),
        ],
    ),

    # Casus: beroepsgeheim
    casus(
        "Een leerling vertelt aan een medewerker van het CLB dat zijn oom hem geregeld slaat en dat het vanavond weer dreigt te gebeuren.",
        [
            mk("Wat moet de medewerker hier doen?",
               ["Zwijgen, want het beroepsgeheim gaat altijd voor alles.", "Het gevaar melden, want hier geldt de meldingsplicht.", "Het verhaal doorvertellen aan de hele klas.", "Wachten tot de leerling zelf naar de politie stapt."],
               1,
               "Het beroepsgeheim beschermt wie hulp zoekt. Maar als iemand in ernstig en dreigend gevaar is, weegt de meldingsplicht zwaarder."),
            keuze(
                "De regels voor het gedrag van een beroepsgroep heten samen de [[*deontologie|grondwet|deugdethiek]]. Wie ze schendt, kan gesanctioneerd worden door zijn [[*beroepsorde of werkgever|vrederechter|parlement]].",
                "Een deontologische code legt vast hoe iemand in een beroep moet handelen, zoals de plicht tot geheimhouding."),
        ],
    ),

    # Casus: ruzie over een haag
    casus(
        "Twee buren maken al maanden ruzie over een haag die te hoog is. Ze willen geen dure rechtszaak.",
        [
            tabel(
                "Bemiddeling of arbitrage?",
                [
                    ("Een neutrale derde helpt de buren zelf tot een akkoord te komen.", "Bemiddeling"),
                    ("Een neutrale derde hakt de knoop door en beslist.", "Arbitrage"),
                    ("De buren houden de beslissing helemaal in eigen hand.", "Bemiddeling"),
                ],
                "Bij bemiddeling beslissen de partijen zelf. Bij arbitrage beslist de arbiter.",
                kolommen=["Bemiddeling", "Arbitrage"]),
            mk("Een van de buren wil eerst gratis kort advies over zijn rechten. Waar kan hij terecht?",
               ["bij het Hof van Cassatie", "bij een wetswinkel", "bij de correctionele rechtbank", "bij de gerechtsdeurwaarder"],
               1,
               "In een wetswinkel en bij de juridische eerstelijnsbijstand krijg je gratis een eerste uitleg over je rechten."),
        ],
    ),

    # Losse vragen door elkaar
    koppel(
        "Welke filosoof hoort bij elke stelling?",
        [
            ["Het lichaam en de denkende geest zijn twee aparte substanties.", "Descartes"],
            ["De mens is een machine; voor zijn denken is geen aparte ziel nodig.", "La Mettrie"],
            ["Het zijnde is één en onveranderlijk, verandering is schijn.", "Parmenides"],
            ["Een uitspraak is wetenschappelijk als ze weerlegd kan worden.", "Popper"],
        ],
        ["Bentham", "Tronto"],
        "Descartes is dualist, La Mettrie materialist, Parmenides monist, Popper bedacht het falsificatiecriterium."),
    sorteer(
        "Wijst deze manier van kennen eerder naar het rationalisme of naar het empirisme?",
        ["Rationalisme", "Empirisme"],
        [
            ["Je twijfelt aan alles tot je één zekerheid vindt en bouwt van daaruit verder.", "Rationalisme"],
            ["Je herhaalt een proef twintig keer en noteert wat je ziet.", "Empirisme"],
            ["Je leidt uit een algemene regel af wat er in één geval moet gebeuren.", "Rationalisme"],
            ["Je trekt uit veel losse waarnemingen een algemene regel.", "Empirisme"],
        ],
        "Rationalisten vertrouwen op het verstand en de deductie. Empiristen laten alle kennis bij de ervaring beginnen en werken inductief."),
    mk("Welke uitspraak is volgens Popper wetenschappelijk?",
       ["Alle metalen zetten uit als je ze verwarmt.", "Er komt binnenkort iets belangrijks op je pad.", "Alles wat gebeurt, heeft een diepere zin.", "Sommige mensen hebben soms een beetje geluk."],
       0,
       "Een wetenschappelijke uitspraak sluit iets uit, zodat een waarneming ze kan weerleggen. Eén metaal dat niet uitzet, zou de eerste uitspraak falsifiëren. De andere sluiten niets uit."),
    tabel(
        "Klopt dit over wetenschap en pseudowetenschap?",
        [
            ("Een theorie bijstellen na nieuw onderzoek is een teken van wetenschap.", J),
            ("Falsifieerbaar betekent dat een theorie fout is.", F),
            ("Bevestigingen vind je ook voor een theorie die niet klopt.", J),
        ],
        "Falsifieerbaar betekent dat een theorie fout zou kúnnen blijken. Daarom zoekt een goede wetenschapper net naar tegenspraak."),
    volgorde(
        "Zet deze denkers over vrijheid en determinisme in de tijd, van oud naar nieuw.",
        ["Democritus", "de Stoïcijnen", "Schopenhauer", "Sartre"],
        "Democritus en de Stoïcijnen leefden in de oudheid (Democritus eerst). Schopenhauer schreef in de 19de eeuw, Sartre in de 20ste eeuw."),
    mk("Hoe laat Frankfurt vrijheid en een wereld vol oorzaken samengaan?",
       ["Je handelt vrij als je je verlangen ook wíl hebben.", "Hij noemt de vrije wil een bedenksel om schuld toe te wijzen.", "Hij legt de vrijheid in je houding tegenover het lot.", "Hij zegt dat alles vastligt en vrijheid dus schijn is."],
       0,
       "Bij Frankfurt handel je vrij als je je verlangen ook wíl hebben, ook al heeft dat verlangen oorzaken. Zo verzoent hij vrijheid en determinisme. Nietzsche noemt de vrije wil een bedenksel, de Stoïcijnen leggen vrijheid in je houding."),
    keuze(
        "Voor Aristoteles is moed een deugd die in het midden ligt tussen [[*lafheid|vriendelijkheid|rechtvaardigheid]] en [[*overmoed|gierigheid|bescheidenheid]].",
        "Een deugd ligt tussen een tekort en een overdaad. Te weinig moed is lafheid, te veel is overmoed."),
    koppel(
        "Welke drogreden herken je in elke uitspraak van een leerling?",
        [
            ["Iedereen in mijn klas spiekt, dus zo erg is het niet.", "beroep op de massa"],
            ["Jij wil een strengere verkeerswet? Dus jij wil dat niemand nog met de auto mag rijden.", "stroman"],
            ["Ofwel stop je met gamen, ofwel slaag je nooit.", "valse tweedeling"],
            ["Deze krant liegt nooit, want dat schrijft de krant zelf.", "cirkelredenering"],
        ],
        ["modus ponens", "hellend vlak"],
        "Wat veel mensen doen, is daarom niet juist. Een stroman vervormt het standpunt van de ander. Een valse tweedeling laat maar twee mogelijkheden over. Een cirkelredenering veronderstelt wat ze moet bewijzen."),
    tabel(
        "Welke macht is het?",
        [
            ("het parlement dat een wet stemt", "Wetgevend"),
            ("de regering die de wet uitvoert", "Uitvoerend"),
            ("de rechter die de wet toepast op een geschil", "Rechterlijk"),
        ],
        "De scheiding der machten voorkomt dat alle macht bij één instantie ligt. De drie machten houden elkaar in evenwicht.",
        kolommen=["Wetgevend", "Uitvoerend", "Rechterlijk"]),
    mk("Waarom staat de grondwet boven de gewone wetten?",
       ["Omdat ze ouder is dan elke andere wet in het land.", "Omdat ook de wetgever eraan gebonden is.", "Omdat de koning ze alleen kan veranderen.", "Omdat de rechter haar mag negeren als hij dat wil."],
       1,
       "In een rechtsstaat is ook de overheid aan het recht gebonden. De grondwet legt de regels vast die zelfs de wetgever moet volgen."),
    mk("'Mensen streven naar geluk, dus geluk is de maatstaf van goed handelen.' Welke kritiek geeft Hume op zo'n redenering?",
       ["Uit hoe iets is, volgt niet zomaar hoe het moet zijn.", "Geluk kan je niet meten en dus nooit als maatstaf gebruiken.", "Enkel plichten tellen, geluk niet.", "Dieren streven ook naar geluk."],
       0,
       "Hume wijst op de sprong van 'is' naar 'ought': een feit over wat mensen doen, bewijst nog niet wat ze moeten doen."),
    keuze(
        "Bij Tronto hoort bij de fase zorgen om de morele kwaliteit [[*betrokkenheid|bekwaamheid|verantwoordelijkheid]] en bij de fase zorg verlenen de kwaliteit [[*bekwaamheid|betrokkenheid|verantwoordelijkheid]].",
        "Eerst merk je dat iemand zorg nodig heeft (betrokkenheid). Daarna neem je de zorg op je (verantwoordelijkheid) en verleen je ze met kennis van zaken (bekwaamheid)."),
    mk("Waarin verschilt Schopenhauer van Epicurus als het over geluk gaat?",
       ["Voor Schopenhauer is geluk hoogstens een tijdelijk ontbreken van gemis.", "Voor Schopenhauer is geluk een blijvende toestand die je met oefening kan leren.", "Epicurus zoekt geluk in zoveel mogelijk verlangens tegelijk.", "Epicurus ziet geluk enkel als een beloning na de dood."],
       0,
       "Epicurus zoekt geluk in rust en eenvoud: beperk je verlangens. Schopenhauer is somberder: geluk is enkel even geen gemis."),
    tabel(
        "Universalisme of relativisme?",
        [
            ("Martelen is overal en altijd verkeerd.", "Universalisme"),
            ("Wat goed is, hangt af van de cultuur waarin je leeft.", "Relativisme"),
            ("Mensenrechten gelden voor elke mens, waar ook ter wereld.", "Universalisme"),
        ],
        "Een universalist gelooft in morele regels die voor iedereen gelden. Een relativist laat het oordeel afhangen van de cultuur of de tijd.",
        kolommen=["Universalisme", "Relativisme"]),
    inv("Je ziet honderd keer dat water bij 100 graden kookt en besluit dat water altijd bij 100 graden kookt. Hoe heet die redenering, van losse gevallen naar een algemene regel? Antwoord met één woord.",
        ["inductie", "een inductie"],
        "Inductie gaat van losse waarnemingen naar een algemene regel. Deductie gaat de andere kant op."),
    mk("Wat maakt een verklaring van de natuurfilosofen anders dan een mythe?",
       ["Ze gebruikt argumenten die anderen kunnen betwisten.", "Ze vertelt over helden en hun avonturen op zee.", "Ze verklaart alles met de wil van de oppergod.", "Ze wordt enkel mondeling van generatie op generatie doorgegeven."],
       0,
       "Mythen verklaren met goden en bovennatuurlijke krachten. De natuurfilosofen zochten een verklaring die je met argumenten kon verdedigen en betwisten. Daarom zie je hen als het begin van de westerse filosofie."),
    tabel(
        "Hoort deze zaak bij het burgerlijk recht of bij het strafrecht?",
        [
            ("Twee buren eisen van elkaar een schadevergoeding voor een omgevallen muur.", "Burgerlijk recht"),
            ("Iemand pleegt een inbraak in een winkel.", "Strafrecht"),
            ("Een huurder en een verhuurder zijn het oneens over de huurprijs.", "Burgerlijk recht"),
            ("Een bestuurder rijdt dronken een fietser aan.", "Strafrecht"),
        ],
        "Burgerlijk recht regelt geschillen tussen burgers: de eiser neemt het initiatief. Strafrecht vervolgt misdrijven namens de samenleving, via het openbaar ministerie. Bij de dronken bestuurder kan het slachtoffer daarnaast ook burgerlijke partij worden.",
        kolommen=["Burgerlijk recht", "Strafrecht"]),
    open_("Heeft de mens een vrije wil? Neem een standpunt in en steun het op één filosoof uit de lessen. Geef ook een tegenargument.",
          "Ik denk dat we vrij zijn in de zin van Frankfurt: ik handel vrij als ik mijn verlangen ook wil hebben, ook al heeft het oorzaken. Een tegenargument komt van Schopenhauer: achter elke keuze zit een wil die je niet zelf koos.",
          "Een goed antwoord kiest een standpunt, verwijst juist naar een filosoof en neemt een tegenargument ernstig."),
]
