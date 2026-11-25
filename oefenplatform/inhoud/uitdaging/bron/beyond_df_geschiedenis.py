# -*- coding: utf-8 -*-
"""Uitdaging Geschiedenis 🌍 Beyond dubbele finaliteit (25 november 2026), in
de vormen van het examen van de Examencommissie: 40 vragen die alle
hoofdstukken door elkaar halen, van 1815 tot vandaag. Een zelf geschreven
(verzonnen) soldatenbrief en een lijst met Belgische gebeurtenissen om op te
klikken, tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde en een
korte schrijfopdracht. Geen nieuwe leerstof: alles staat in de hoofdstukken
van Geschiedenis Beyond dubbele finaliteit.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_df_geschiedenis.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Geschiedenis"
BESTAND = "beyond-df-geschiedenis-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/geschiedenis-beyond-df-uitdaging"
BRIEF = "brief-ijzer-1916.svg"
BELGIE = "gebeurtenissen-belgie.svg"


def zin(i, n=6):
    """Klikvak van regel i (vanaf 1), zie uitdaging/_blad.py."""
    h = 90 + n * 92 + 30
    return [2, round((90 + (i - 1) * 92) / h * 100, 1), 96, round(92 / h * 100, 1)]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Soldatenbrief (prent)
    klik("Lees de brief. Klik op de zin die een vooroordeel bevat.",
         BRIEF, [zin(5)],
         "'Allemaal laffe barbaren' is een veralgemening over een hele groep. Dat is een mening, beïnvloed door de oorlogspropaganda."),
    klik("Klik op de zin die verwijst naar de onderwaterzetting van de IJzervlakte.",
         BRIEF, [zin(2)],
         "In oktober 1914 werden de sluizen bij Nieuwpoort geopend. Het water hield de Duitse opmars aan de IJzer tegen."),
    klik("Klik op de zin die past bij de taalgrieven van Vlaamse soldaten.",
         BRIEF, [zin(4)],
         "Veel Vlaamse soldaten begrepen de Franse bevelen slecht. Die frustratie voedde de Frontbeweging."),
    met_prent(BRIEF, tabel(
        "Klopt dit over de brief?",
        [
            ("De brief toont hoe een soldaat de oorlog zelf beleefde.", J),
            ("Zin 6 toont dat de soldaat een lange oorlog verwachtte.", F),
            ("Een brief uit 1916 zou een primaire bron zijn.", J),
            ("De brief bewijst hoe alle Belgische soldaten dachten.", F),
        ],
        "Een brief is een persoonlijke getuigenis uit de tijd zelf. Hij hoopt juist op een snel einde. Eén brief zegt niets over alle soldaten.")),
    met_prent(BRIEF, mk(
        "Waarom moet je voorzichtig zijn met wat soldaten in brieven naar huis schreven?",
        ["Brieven werden gecensureerd en ze wilden hun familie geruststellen.", "Soldaten mochten van het leger enkel over het weer en het eten schrijven.", "Brieven uit de oorlog werden pas na 1950 opgeschreven door historici.", "Soldaten schreven altijd in het Duits, waardoor veel verloren ging."],
        0,
        "Het leger las brieven na en schrapte gevoelige informatie. Veel soldaten verzwegen ook de ergste dingen voor hun familie.")),

    # Belgische gebeurtenissen (prent)
    klik("Klik op de oudste gebeurtenis.",
         BELGIE, [zin(2)],
         "De Belgische Revolutie vond plaats in 1830. Daarna volgen 1914, 1919, 1950, 1960 en 1993."),
    klik("Klik op de gebeurtenis die volgde op de Eerste Wereldoorlog en de politieke rechten van arbeiders vergrootte.",
         BELGIE, [zin(1)],
         "In 1919 kregen alle mannen vanaf 21 jaar één stem. Vóór die tijd hadden rijkere en geschoolde mannen meer stemmen."),
    klik("Klik op de gebeurtenis die het land rond 1950 diep verdeelde.",
         BELGIE, [zin(6)],
         "De Koningskwestie draaide rond de terugkeer van Leopold III na de Tweede Wereldoorlog. In 1951 deed hij afstand van de troon."),
    met_prent(BELGIE, volgorde(
        "Zet de gebeurtenissen van de lijst in chronologische volgorde.",
        ["De Belgische Revolutie", "De Duitse inval in België in de Eerste Wereldoorlog", "Algemeen enkelvoudig stemrecht voor mannen", "De Koningskwestie", "De onafhankelijkheid van Congo", "België wordt een federale staat"],
        "1830, 1914, 1919, rond 1950, 1960 en 1993.")),

    # Referentiekader en samenlevingen
    tabel(
        "In welk domein van de samenleving hoort dit?",
        [
            ("De invoering van het stemrecht", "Politiek"),
            ("De bouw van spoorwegen en fabrieken", "Economie"),
            ("Het ontstaan van de arbeidersklasse", "Sociaal"),
            ("Nieuwe kunststromingen zoals het impressionisme", "Cultuur"),
        ],
        "Historici delen het verleden in domeinen in: politiek, economie, sociaal en cultureel.",
        kolommen=["Politiek", "Economie", "Sociaal", "Cultuur"]),
    keuze(
        "Na de nederlaag van Napoleon herstelde het Congres van Wenen in [[*1815|1830|1789]] de macht van de [[*vorsten|arbeiders|kolonies]].",
        "In 1815 tekenden de grootmachten in Wenen een nieuwe kaart van Europa en herstelden ze de oude vorstenhuizen."),
    tabel(
        "Liberalisme of nationalisme?",
        [
            ("Een volk met een eigen taal en cultuur wil een eigen staat.", "Nationalisme"),
            ("Vrijheid van meningsuiting en een grondwet", "Liberalisme"),
            ("De eenmaking van Italië en Duitsland", "Nationalisme"),
            ("Een vrije markt zonder veel overheid", "Liberalisme"),
        ],
        "Liberalen streden voor vrijheid en grondrechten. Nationalisten wilden dat elk volk een eigen staat kreeg.",
        kolommen=["Liberalisme", "Nationalisme"]),

    # België en industrialisatie
    keuze(
        "Na de opstand van [[*1830|1815|1848]] werd België een [[*constitutionele monarchie|republiek|dictatuur]] met Leopold I als eerste koning.",
        "De grondwet van 1831 beperkte de macht van de koning. Leopold I legde de eed af in 1831."),
    tabel(
        "Eerste of tweede industriële revolutie?",
        [
            ("Stoommachine en steenkool", "Eerste"),
            ("Elektriciteit en de verbrandingsmotor", "Tweede"),
            ("Mechanische weefgetouwen", "Eerste"),
            ("Chemische industrie en staal op grote schaal", "Tweede"),
        ],
        "De eerste industriële revolutie draaide op stoom en steenkool. De tweede, vanaf het einde van de 19de eeuw, bracht elektriciteit, olie en chemie.",
        kolommen=["Eerste", "Tweede"]),
    sorteer(
        "Welke stroming hoort bij deze uitspraak?",
        ["Marxisme", "Sociaaldemocratie", "Christendemocratie"],
        [
            ["Arbeiders moeten de macht grijpen met een revolutie.", "Marxisme"],
            ["We verbeteren de positie van arbeiders via verkiezingen en wetten.", "Sociaaldemocratie"],
            ["Werkgevers en werknemers moeten samenwerken volgens de christelijke waarden.", "Christendemocratie"],
        ],
        "Marx wilde een revolutie. Sociaaldemocraten kozen voor hervormingen via het parlement. Christendemocraten volgden de sociale leer van de Kerk (Rerum Novarum)."),
    mk("Waarom kwamen er in de 19de eeuw zo veel arbeiders naar de steden?",
       ["Ze zochten werk in de nieuwe fabrieken.", "Ze kregen er gratis een huis van de koning.", "De landbouw verdween volledig uit België.", "Ze wilden er vooral studeren aan de universiteit."],
       0,
       "Door de industrialisatie was er werk in de fabrieken, terwijl er op het platteland vaak armoede was."),

    # Imperialisme en Congo
    tabel(
        "Klopt dit over het imperialisme?",
        [
            ("Europese landen zochten grondstoffen en afzetmarkten.", J),
            ("Op de Conferentie van Berlijn verdeelden Europeanen Afrika onder elkaar.", J),
            ("Afrikaanse leiders beslisten mee op de Conferentie van Berlijn.", F),
        ],
        "In 1884-1885 verdeelden Europese landen Afrika zonder dat Afrikanen er iets over te zeggen hadden."),
    keuze(
        "De Congo-Vrijstaat was van 1885 tot [[*1908|1960|1830]] het persoonlijke bezit van koning [[*Leopold II|Albert I|Leopold I]].",
        "Na kritiek op de misbruiken bij de rubberwinning nam de Belgische staat Congo in 1908 over."),

    # Wereldoorlogen
    koppel(
        "Koppel het begrip aan de uitleg.",
        [
            ["loopgravenoorlog", "lange frontlinie waar legers jaren tegenover elkaar lagen"],
            ["Verdrag van Versailles", "vrede van 1919 met zware voorwaarden voor Duitsland"],
            ["Volkenbond", "internationale organisatie om oorlog te voorkomen na 1918"],
        ],
        ["de verdeling van Berlijn"],
        "De Eerste Wereldoorlog was vooral een loopgravenoorlog. Na de oorlog volgden het Verdrag van Versailles en de Volkenbond."),
    tabel(
        "Welk totalitair regime?",
        [
            ("Hitler, rassenleer en de Jodenvervolging", "Nazi-Duitsland"),
            ("Stalin, vijfjarenplannen en de goelag", "Sovjet-Unie"),
            ("Mussolini en de zwarthemden", "Fascistisch Italië"),
        ],
        "Totalitaire regimes controleerden alles: politiek, economie, media en het privéleven.",
        kolommen=["Nazi-Duitsland", "Sovjet-Unie", "Fascistisch Italië"]),
    mk("Wat was een kenmerk van het totalitarisme?",
       ["Eén partij controleert alles en duldt geen kritiek.", "Er zijn veel partijen en vrije verkiezingen.", "De pers mag de regering vrij bekritiseren.", "De macht is verdeeld over drie onafhankelijke machten."],
       0,
       "In een totalitaire staat is er één partij en één leider. Oppositie, vrije pers en vrije verkiezingen bestaan niet."),
    volgorde(
        "Zet in de juiste volgorde.",
        ["Beurskrach van Wall Street", "Hitler komt aan de macht", "Duitsland valt Polen binnen", "De Holocaust in de vernietigingskampen", "Bevrijding van de kampen"],
        "1929, 1933, 1939, vooral 1942-1944, 1945."),

    # China, Koude Oorlog en Europa
    keuze(
        "In 1949 riep [[*Mao Zedong|Deng Xiaoping|Sun Yat-sen]] de Volksrepubliek China uit. Vanaf 1978 opende [[*Deng Xiaoping|Mao Zedong]] de economie voor buitenlandse bedrijven.",
        "Mao maakte China communistisch. Deng hervormde de economie, wat China tot een wereldmacht maakte."),
    sorteer(
        "Hoort dit bij het Westen of bij het Oostblok tijdens de Koude Oorlog?",
        ["Westen", "Oostblok"],
        [
            ["Verenigde Staten", "Westen"],
            ["Sovjet-Unie", "Oostblok"],
            ["NAVO", "Westen"],
            ["Warschaupact", "Oostblok"],
        ],
        "Het kapitalistische Westen onder leiding van de VS stond tegenover het communistische Oostblok onder de Sovjet-Unie."),
    tabel(
        "Klopt dit over de Europese eenmaking?",
        [
            ("België was een van de zes stichtende landen van de EEG.", J),
            ("De euro werd ingevoerd als munt in 2002.", J),
            ("Alle landen van Europa zijn lid van de Europese Unie.", F),
        ],
        "In 1957 stichtten zes landen de EEG. De euromunten en -biljetten kwamen er in 2002. Landen zoals Noorwegen en Zwitserland zijn geen lid."),
    mk("Waarom startte de Europese samenwerking na 1945?",
       ["Om oorlog te voorkomen en de economie te versterken.", "Om samen kolonies in Afrika te veroveren en te besturen.", "Om de Verenigde Staten economisch te verslaan en in te halen.", "Om één Europese koning aan te stellen voor alle landen."],
       0,
       "Landen die economisch van elkaar afhangen, voeren minder snel oorlog. De EGKS (1951) bracht kolen en staal samen."),

    # Dekolonisatie en België na 1945
    keuze(
        "Congo werd onafhankelijk op 30 juni [[*1960|1945|1975]]. De eerste premier was [[*Patrice Lumumba|Mobutu|Leopold II]].",
        "Lumumba hield bij de onafhankelijkheid een scherpe toespraak. Hij werd in 1961 vermoord."),
    tabel(
        "Welke breuklijn in de Belgische politiek?",
        [
            ("Ruzie over de financiering van katholieke en officiële scholen", "Levensbeschouwelijk"),
            ("Ruzie tussen werkgevers en vakbonden over lonen", "Sociaaleconomisch"),
            ("Ruzie tussen Vlamingen en Franstaligen over taal", "Communautair"),
        ],
        "De drie klassieke breuklijnen zijn levensbeschouwelijk, sociaaleconomisch en communautair.",
        kolommen=["Levensbeschouwelijk", "Sociaaleconomisch", "Communautair"]),
    keuze(
        "In België kregen vrouwen in 1948 [[*stemrecht|het recht om te werken]] bij nationale verkiezingen. De tweede feministische golf in de jaren 1960-1970 streed onder meer voor [[*gelijk loon|het recht op stemmen]].",
        "Na het stemrecht ging de strijd verder over gelijk loon, anticonceptie en gelijke kansen."),

    # Kunst, bronnen en beeldvorming
    tabel(
        "Welke stap van een kunstanalyse is dit?",
        [
            ("Wat zie je? Kleuren, vormen, personages.", "Beschrijven"),
            ("Wat betekent het werk en wat wil de kunstenaar zeggen?", "Interpreteren"),
            ("In welke tijd en stroming past het werk?", "Situeren"),
        ],
        "Je beschrijft eerst wat je ziet, situeert het werk in zijn tijd en interpreteert dan de betekenis.",
        kolommen=["Beschrijven", "Situeren", "Interpreteren"]),
    sorteer(
        "Is deze bron eerder betrouwbaar of minder betrouwbaar over de slag aan de IJzer?",
        ["Eerder betrouwbaar", "Minder betrouwbaar"],
        [
            ["Een legerrapport van de dag zelf, met plaatsen en uren", "Eerder betrouwbaar"],
            ["Een propagandaaffiche die de vijand belachelijk maakt", "Minder betrouwbaar"],
            ["Verschillende dagboeken die hetzelfde vertellen", "Eerder betrouwbaar"],
            ["Een verhaal dat een opa vijftig jaar later navertelt", "Minder betrouwbaar"],
        ],
        "Een bron is betrouwbaarder als ze dicht bij de gebeurtenis staat, weinig belang heeft om te overdrijven en bevestigd wordt door andere bronnen."),
    mk("Wat bedoel je met standplaatsgebondenheid?",
       ["Je tijd, land en opvoeding kleuren hoe je het verleden ziet.", "Een historicus moet altijd op dezelfde plaats blijven wonen.", "Een bron is pas geldig als ze op de plaats zelf gevonden werd.", "Een standbeeld mag niet van zijn plaats worden weggehaald."],
       0,
       "Iedereen kijkt vanuit zijn eigen achtergrond. Daarom vergelijk je verschillende standpunten."),

    # Extra
    inv("In welk jaar eindigde de Tweede Wereldoorlog in Europa?",
        ["1945"],
        "Duitsland capituleerde op 8 mei 1945."),
    keuze(
        "De Berlijnse Muur viel in [[*1989|1961|1945]]. Twee jaar later viel ook de [[*Sovjet-Unie|Europese Unie|NAVO]] uiteen.",
        "De val van de Muur in 1989 luidde het einde van de Koude Oorlog in. In 1991 hield de Sovjet-Unie op te bestaan."),
    mk("Wat was de Rerum Novarum (1891)?",
       ["Een tekst van de paus over de sociale kwestie en de rechten van arbeiders.", "Een vredesverdrag tussen België en Nederland na de Belgische Revolutie.", "De eerste Belgische wet die kinderarbeid volledig verbood in alle sectoren.", "Een manifest van Karl Marx dat opriep tot een wereldwijde revolutie."],
       0,
       "Paus Leo XIII vroeg rechtvaardige lonen en erkende het recht van arbeiders om zich te verenigen. Het werd de basis van de christelijke arbeidersbeweging."),

    tabel(
        "Waar of niet waar over de Holocaust?",
        [
            ("De nazi's vermoordden ongeveer zes miljoen Joden.", J),
            ("Ook Roma en mensen met een handicap werden vervolgd.", J),
            ("De Holocaust gebeurde vooral in West-Europa, in Frankrijk en België.", F),
        ],
        "De meeste vernietigingskampen lagen in bezet Polen. Joden uit heel Europa, ook uit België via de Dossinkazerne in Mechelen, werden erheen gedeporteerd."),
    mk("Wat was het doel van de Verenigde Naties bij de oprichting in 1945?",
       ["De vrede en de veiligheid in de wereld bewaren.", "Een Europese munt invoeren voor alle lidstaten.", "De kolonies in Afrika samen besturen en uitbreiden.", "Een militair bondgenootschap tegen de Sovjet-Unie."],
       0,
       "De VN wilden een nieuwe wereldoorlog voorkomen, samenwerking bevorderen en de mensenrechten beschermen."),
    keuze(
        "Kinderarbeid onder de [[*12|16|6]] jaar werd in België verboden door de wet van 1889. Die wet kwam er na de [[*arbeidersopstanden van 1886|Belgische Revolutie van 1830]].",
        "Na de zware stakingen en rellen van 1886 kwamen de eerste sociale wetten, zoals het verbod op kinderarbeid onder 12 jaar."),
    koppel(
        "Koppel de persoon aan wat hij deed.",
        [
            ["Leopold II", "bezat de Congo-Vrijstaat"],
            ["Karl Marx", "schreef het Communistisch Manifest"],
            ["Winston Churchill", "Britse premier tijdens de Tweede Wereldoorlog"],
        ],
        ["riep de Volksrepubliek China uit"],
        "Leopold II bezat Congo, Marx schreef in 1848 het Communistisch Manifest en Churchill leidde Groot-Brittannië in de Tweede Wereldoorlog. Mao riep de Volksrepubliek uit."),

    # Schrijfopdracht
    open_("Leg in 4 à 6 zinnen uit waarom België na 1970 stap voor stap een federale staat werd. Gebruik minstens twee begrippen uit de les.",
          "Na 1945 groeiden de spanningen tussen Vlamingen en Franstaligen, de communautaire breuklijn. Vlaanderen wilde meer zelfbestuur over taal en cultuur, Wallonië wilde zelf zijn economie in handen nemen omdat de oude industrie er in crisis was. Daarom volgden vanaf 1970 staatshervormingen. Er kwamen gemeenschappen voor taal en cultuur en gewesten voor economie en ruimte. Sinds 1993 staat in de grondwet dat België een federale staat is.",
          "Een goed antwoord noemt de communautaire spanningen, de verschillende wensen van Vlaanderen en Wallonië, de staatshervormingen vanaf 1970 met gemeenschappen en gewesten, en 1993 als federale staat."),
]
