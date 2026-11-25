# -*- coding: utf-8 -*-
"""Uitdaging Geschiedenis 🌍 Beyond doorstroom (25 november 2026), in de vormen
van het examen van de Examencommissie: 40 vragen die alle hoofdstukken door
elkaar halen, van 1815 tot vandaag. Een zelf geschreven (verzonnen)
dagboekfragment en een lijst van gebeurtenissen om op te klikken, tabellen,
keuzelijsten, slepen, koppelen, sorteren, volgorde en een korte schrijfopdracht.
Geen nieuwe leerstof: alles staat in de hoofdstukken van Geschiedenis Beyond
doorstroom.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_geschiedenis.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Geschiedenis"
BESTAND = "beyond-geschiedenis-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/geschiedenis-beyond-uitdaging"
DAGBOEK = "dagboek-1846.svg"
LIJST = "gebeurtenissen-20ste-eeuw.svg"


def zin(i, n=6):
    """Klikvak van regel i (vanaf 1), zie uitdaging/_blad.py."""
    h = 90 + n * 92 + 30
    return [2, round((90 + (i - 1) * 92) / h * 100, 1), 96, round(92 / h * 100, 1)]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Dagboek (prent)
    klik("Lees het dagboekfragment. Klik op de zin die een mening is en geen feit.",
         DAGBOEK, [zin(4)],
         "'Hardvochtige gierigaards' is een oordeel over alle bazen. De andere zinnen beschrijven wat ze meemaakt, hoort of hoopt."),
    klik("Klik op de zin die over kinderarbeid gaat.",
         DAGBOEK, [zin(2)],
         "Een meisje van negen werkt in de spinnerij. Kinderarbeid was in de 19de eeuw gewoon en werd in België pas in 1889 beperkt."),
    klik("Klik op de zin die past bij de crisis van de jaren 1845-1847 in Vlaanderen.",
         DAGBOEK, [zin(3)],
         "De aardappelziekte en mislukte graanoogsten veroorzaakten honger in Vlaanderen. Dat verergerde de armoede van de vlasarbeiders."),
    met_prent(DAGBOEK, tabel(
        "Klopt dit over het dagboek?",
        [
            ("Het is een primaire bron als het echt in 1846 geschreven zou zijn.", J),
            ("Zin 5 wijst op de eerste stappen naar arbeidersorganisaties.", J),
            ("De schrijfster heeft volgens de tekst stemrecht.", F),
            ("Uit zin 1 blijkt dat er al een wettelijke achturendag was.", F),
        ],
        "Een getuigenis uit de tijd zelf is een primaire bron. Vakbonden waren nog verboden, gewone arbeiders hadden geen stemrecht (cijnskiesrecht), en ze werkte vijftien uur per dag.")),
    met_prent(DAGBOEK, mk(
        "Hoe gebruik je dit fragment best als historicus?",
        ["Als één getuigenis die je vergelijkt met andere bronnen.", "Als volledig betrouwbaar bewijs over alle arbeiders in België.", "Als waardeloos, omdat de schrijfster een mening geeft.", "Als bewijs dat alle fabrieksbazen echt gierig waren."],
        0,
        "Een getuigenis is waardevol maar persoonlijk. Je toetst ze aan andere bronnen voor je algemene besluiten trekt.")),

    # Gebeurtenissen (prent)
    klik("Klik op de gebeurtenis die het eerst plaatsvond.",
         LIJST, [zin(2)],
         "De Oktoberrevolutie vond plaats in 1917, de beurskrach in 1929, Jalta in 1945, Rome in 1957, Congo in 1960 en de val van de Muur in 1989."),
    klik("Klik op de gebeurtenis die hoort bij de dekolonisatie.",
         LIJST, [zin(4)],
         "Congo werd op 30 juni 1960 onafhankelijk van België."),
    klik("Klik op de gebeurtenis die het begin is van de Europese Economische Gemeenschap.",
         LIJST, [zin(6)],
         "Het Verdrag van Rome (1957) richtte de EEG op, met België als een van de zes stichtende landen."),
    met_prent(LIJST, volgorde(
        "Zet de gebeurtenissen van de lijst in chronologische volgorde.",
        ["De Russische Oktoberrevolutie", "De beurskrach van Wall Street", "De conferentie van Jalta", "Het Verdrag van Rome", "De onafhankelijkheid van Congo", "De val van de Berlijnse Muur"],
        "1917, 1929, 1945, 1957, 1960, 1989.")),

    # Referentiekader en 19de eeuw
    tabel(
        "In welke periode hoort dit?",
        [
            ("Het Congres van Wenen", "19de eeuw"),
            ("De Koude Oorlog", "20ste eeuw"),
            ("De Belgische Revolutie", "19de eeuw"),
            ("De Brexit", "21ste eeuw"),
        ],
        "Wenen 1815 en de Belgische Revolutie 1830 vallen in de 19de eeuw, de Koude Oorlog 1947-1991 in de 20ste, de Brexit 2020 in de 21ste.",
        kolommen=["19de eeuw", "20ste eeuw", "21ste eeuw"]),
    keuze(
        "Na de val van Napoleon bracht het Congres van Wenen de [[*restauratie|revolutie|dekolonisatie]]. De Zuidelijke Nederlanden werden toen samengevoegd met het noorden onder koning [[*Willem I|Leopold I|Napoleon III]].",
        "De grootmachten herstelden in 1815 de oude vorsten. Het Verenigd Koninkrijk der Nederlanden onder Willem I bestond tot de Belgische Revolutie van 1830."),
    sorteer(
        "Hoort dit kenmerk bij het liberalisme of bij het socialisme van de 19de eeuw?",
        ["Liberalisme", "Socialisme"],
        [
            ["Vrije markt met weinig overheid", "Liberalisme"],
            ["Collectief bezit van productiemiddelen", "Socialisme"],
            ["Individuele vrijheid en eigendom staan voorop", "Liberalisme"],
            ["Klassenstrijd tussen arbeiders en kapitalisten", "Socialisme"],
        ],
        "Liberalen wilden vrijheid en een kleine overheid. Socialisten wilden de positie van de arbeiders verbeteren, desnoods door de productiemiddelen gemeenschappelijk te maken."),
    mk("Waarom was de sociale kwestie in de 19de eeuw zo dringend?",
       ["Industrialisatie bracht lange werkdagen, lage lonen en ellendige woningen.", "Arbeiders hadden al stemrecht maar gebruikten het bijna nooit in de praktijk.", "De fabrieken stonden vooral op het platteland, ver van de steden en havens.", "De adel weigerde nog langer te investeren in nieuwe stoommachines."],
       0,
       "De snelle industrialisatie trok mensen naar de steden, waar ze onder zware omstandigheden werkten en woonden zonder sociale bescherming."),

    # Imperialisme
    tabel(
        "Klopt dit over Congo?",
        [
            ("Congo was eerst persoonlijk bezit van koning Leopold II.", J),
            ("België nam Congo in 1908 over als kolonie.", J),
            ("Onder de Vrijstaat werd rubber gewonnen met dwangarbeid.", J),
            ("Congo werd na de Eerste Wereldoorlog een Duitse kolonie.", F),
        ],
        "Leopold II bezat de Onafhankelijke Congostaat van 1885 tot 1908. Na internationale kritiek op misbruiken werd het een Belgische kolonie."),
    keuze(
        "Na de Opiumoorlogen moest China havens openen voor westerse handelaars. Die verdragen noemt men de [[*ongelijke verdragen|vredesverdragen van Versailles]].",
        "China moest onder dwang handelsvoordelen en grondgebied afstaan, zoals Hongkong aan Groot-Brittannië."),

    # WOI en Rusland
    koppel(
        "Koppel de oorzaak van de Eerste Wereldoorlog aan het voorbeeld.",
        [
            ["militarisme", "een wapenwedloop tussen Duitsland en Groot-Brittannië"],
            ["allianties", "Triple Entente tegenover Centrale Mogendheden"],
            ["nationalisme", "Slavische volkeren die los willen van Oostenrijk-Hongarije"],
            ["directe aanleiding", "de moord op Franz Ferdinand in Sarajevo"],
        ],
        ["de beurskrach van 1929"],
        "Langetermijnoorzaken bouwden spanning op; de moord in Sarajevo in 1914 deed de oorlog uitbreken. De beurskrach volgde pas later."),
    mk("Wat gebeurde er in Rusland in oktober 1917?",
       ["De bolsjewieken onder Lenin namen de macht over.", "De tsaar won de oorlog tegen Duitsland en Oostenrijk.", "Rusland werd een parlementaire monarchie zoals Groot-Brittannië.", "Stalin werd verkozen tot president in vrije verkiezingen."],
       0,
       "Na de val van de tsaar in februari namen de bolsjewieken in oktober de macht. Rusland stapte daarna uit de oorlog."),

    # Interbellum en WOII
    tabel(
        "Kenmerk van welk regime?",
        [
            ("Leiderscultus rond Mussolini en corporatisme", "Fascisme"),
            ("Rassenleer en het idee van Lebensraum", "Nationaalsocialisme"),
            ("Collectivisatie van de landbouw en vijfjarenplannen", "Stalinisme"),
        ],
        "Alle drie waren totalitaire regimes, maar met een andere ideologie: fascistisch Italië, nazi-Duitsland en de Sovjet-Unie onder Stalin.",
        kolommen=["Fascisme", "Nationaalsocialisme", "Stalinisme"]),
    keuze(
        "De crisis van de jaren 1930 begon met de beurskrach in [[*New York|Londen|Berlijn]] in 1929. In Duitsland hielp de massawerkloosheid de [[*nazi's|liberalen|monarchisten]] aan de macht.",
        "Wall Street stortte in oktober 1929 in. Wanhoop en werkloosheid maakten extreme partijen populair; Hitler werd in 1933 rijkskanselier."),
    volgorde(
        "Zet deze stappen naar en tijdens de Tweede Wereldoorlog in de juiste volgorde.",
        ["Hitler wordt rijkskanselier", "Duitsland valt Polen binnen", "Duitsland valt België binnen", "Landing in Normandië", "Capitulatie van Duitsland"],
        "1933, september 1939, mei 1940, juni 1944, mei 1945."),
    mk("Wat bedoelt men met de Holocaust?",
       ["De systematische moord op de Joden door nazi-Duitsland.", "De bombardementen op Duitse steden door de geallieerden.", "De verdrijving van Duitsers uit Oost-Europa na de oorlog.", "Het proces tegen nazileiders in Neurenberg na de oorlog."],
       0,
       "De Holocaust of Shoah was de industrieel georganiseerde genocide op zes miljoen Joden, naast vervolging van Roma, gehandicapten en anderen."),

    # Koude Oorlog en Europa
    sorteer(
        "Hoort dit bij het Westblok of bij het Oostblok?",
        ["Westblok", "Oostblok"],
        [
            ["NAVO", "Westblok"],
            ["Warschaupact", "Oostblok"],
            ["Marshallplan", "Westblok"],
            ["Comecon", "Oostblok"],
        ],
        "Het Westen onder leiding van de VS had de NAVO en het Marshallplan. Het Oostblok onder de Sovjet-Unie had het Warschaupact en de Comecon."),
    keuze(
        "De Cubacrisis van [[*1962|1948|1989]] bracht de wereld dicht bij een kernoorlog. De Berlijnse Muur werd gebouwd in [[*1961|1945|1975]].",
        "In 1962 stonden de VS en de Sovjet-Unie oog in oog over raketten op Cuba. De Muur verdeelde Berlijn van 1961 tot 1989."),
    tabel(
        "Klopt dit over de Verenigde Naties?",
        [
            ("De VN werden opgericht in 1945.", J),
            ("De Veiligheidsraad heeft vijf permanente leden met vetorecht.", J),
            ("De VN vervingen de Volkenbond.", J),
            ("Elke lidstaat heeft vetorecht in de Veiligheidsraad.", F),
        ],
        "Enkel de VS, Rusland, China, Frankrijk en het Verenigd Koninkrijk hebben een veto."),

    # België na 1945
    koppel(
        "Koppel het Belgische begrip aan de uitleg.",
        [
            ["Koningskwestie", "conflict over de terugkeer van Leopold III"],
            ["Schoolstrijd", "ruzie over geld voor katholieke en officiële scholen"],
            ["staatshervorming", "België wordt stap voor stap een federale staat"],
        ],
        ["de onafhankelijkheid van 1830"],
        "Na 1945 verdeelden de Koningskwestie en de Schoolstrijd het land. Vanaf 1970 volgden staatshervormingen naar gemeenschappen en gewesten."),
    mk("Sinds welke staatshervorming is België in de grondwet een federale staat?",
       ["Die van 1993", "Die van 1830", "Die van 1970", "Die van 2014"],
       0,
       "In 1993 staat in artikel 1 van de grondwet dat België een federale staat is, samengesteld uit gemeenschappen en gewesten."),

    # Dekolonisatie en vandaag
    keuze(
        "India werd in [[*1947|1960|1918]] onafhankelijk na een geweldloze strijd onder leiding van [[*Gandhi|Mandela|Lumumba]].",
        "Gandhi voerde burgerlijke ongehoorzaamheid tegen de Britten. Bij de onafhankelijkheid werd Brits-Indië gesplitst in India en Pakistan."),

    # China
    tabel(
        "Welke leider hoort bij deze periode in China?",
        [
            ("De Grote Sprong Voorwaarts en de Culturele Revolutie", "Mao Zedong"),
            ("Economische hervormingen en openstelling vanaf 1978", "Deng Xiaoping"),
            ("Het project van de Nieuwe Zijderoute", "Xi Jinping"),
        ],
        "Mao leidde de Volksrepubliek van 1949 tot 1976, Deng opende de economie, Xi startte het Belt and Road-initiatief.",
        kolommen=["Mao Zedong", "Deng Xiaoping", "Xi Jinping"]),

    # Israël-Palestina
    tabel(
        "Klopt dit over de Israëlisch-Palestijnse kwestie?",
        [
            ("De staat Israël werd uitgeroepen in 1948.", J),
            ("In 1967 bezette Israël onder meer de Westelijke Jordaanoever en Gaza.", J),
            ("De Oslo-akkoorden van de jaren 1990 maakten een definitief einde aan het conflict.", F),
        ],
        "Na de Zesdaagse Oorlog van 1967 bezette Israël nieuwe gebieden. De Oslo-akkoorden zorgden voor Palestijns zelfbestuur, maar het conflict bleef."),

    # Denken en kunst
    tabel(
        "Welke kunststroming herken je?",
        [
            ("Lichtspel en snelle toetsen, buiten geschilderd", "Impressionisme"),
            ("Droombeelden en onlogische combinaties, zoals bij Magritte", "Surrealisme"),
            ("Objecten opgebouwd uit geometrische vlakken, zoals bij Picasso", "Kubisme"),
            ("Alledaagse reclamebeelden en strips, zoals bij Warhol", "Pop-art"),
        ],
        "Elke stroming reageerde op haar tijd: licht en indruk, het onbewuste, nieuwe vormen, en de consumptiemaatschappij.",
        kolommen=["Impressionisme", "Kubisme", "Surrealisme", "Pop-art"]),
    keuze(
        "De feministische golf die vooral stemrecht voor vrouwen eiste, heet de [[*eerste|tweede]] golf. In België kregen vrouwen algemeen stemrecht bij de nationale verkiezingen in [[*1948|1919|1893]].",
        "De eerste golf streed voor politieke rechten. Belgische vrouwen stemden voor het eerst bij parlementsverkiezingen in 1949, na de wet van 1948."),
    mk("Wat is een kenmerk van de romantiek in de 19de eeuw?",
       ["Aandacht voor gevoel, natuur en het nationale verleden.", "Strakke regels en het voorbeeld van de Grieks-Romeinse oudheid.", "Kunst die enkel uit kleurvlakken en rechte lijnen bestaat.", "Massaproductie van kunst met reclamebeelden en strips."],
       0,
       "De romantiek reageerde op de rede van de Verlichting met gevoel, verbeelding en interesse voor de eigen geschiedenis, zoals in De Leeuw van Vlaanderen."),

    # Bronnen en beeldvorming
    sorteer(
        "Is dit een primaire of een secundaire bron over de Eerste Wereldoorlog?",
        ["Primaire bron", "Secundaire bron"],
        [
            ["Een brief van een soldaat uit de loopgraven in 1916", "Primaire bron"],
            ["Een handboek geschiedenis uit 2020", "Secundaire bron"],
            ["Een propagandaaffiche uit 1915", "Primaire bron"],
            ["Een documentaire uit 2014 over de IJzer", "Secundaire bron"],
        ],
        "Primaire bronnen ontstonden in de tijd zelf. Secundaire bronnen zijn later gemaakt door mensen die over die tijd schrijven."),
    mk("Een affiche uit 1914 toont Duitse soldaten als monsters. Wat zegt dat vooral?",
       ["Hoe de maker de vijand wilde voorstellen om steun te krijgen.", "Hoe Duitse soldaten er echt uitzagen in augustus 1914.", "Dat alle Belgen in 1914 dezelfde mening over Duitsland hadden.", "Dat de affiche na de oorlog gemaakt werd door historici."],
       0,
       "Propaganda vertelt veel over de bedoeling van de maker en het beeld dat hij wilde verspreiden, minder over hoe het echt was."),
    keuze(
        "Als je zegt dat de vrouwen in 1830 'achterlijk' waren omdat ze niet stemden, beoordeel je het verleden met normen van nu. Dat heet [[*anachronistisch denken|bronnenkritiek|periodiseren]].",
        "Historisch denken vraagt dat je het verleden begrijpt vanuit zijn eigen tijd en normen."),

    inv("In welk jaar brak in Brussel de opstand uit die tot de Belgische onafhankelijkheid leidde?",
        ["1830"],
        "In augustus en september 1830 kwamen Brusselaars in opstand tegen Willem I. Leopold I werd in 1831 de eerste koning."),
    mk("Waarom zagen veel Duitsers het Verdrag van Versailles als een vernedering?",
       ["Het moest de oorlogsschuld aanvaarden, gebied afstaan en betalen.", "Duitsland kreeg zijn kolonies terug maar mocht geen eigen keizer meer kiezen.", "Duitsland moest samen met Oostenrijk-Hongarije een nieuwe staat vormen.", "Duitsland werd verplicht om meteen lid te worden van het Warschaupact."],
       0,
       "Artikel 231 legde de oorlogsschuld bij Duitsland. Gebiedsverlies, een klein leger en zware herstelbetalingen voedden later het nationalisme."),
    keuze(
        "Met het Marshallplan gaven de [[*Verenigde Staten|Sovjet-Unie]] na 1945 economische hulp aan [[*West-Europa|Oost-Europa|China]].",
        "De VS wilden de wederopbouw steunen en zo vermijden dat West-Europese landen communistisch werden."),
    tabel(
        "Was dit een gevolg van de Tweede Wereldoorlog?",
        [
            ("De oprichting van de Verenigde Naties", J),
            ("De verdeling van Duitsland in bezettingszones", J),
            ("Het ontstaan van België als onafhankelijk land", F),
            ("De Russische Revolutie", F),
        ],
        "De VN en de verdeling van Duitsland volgden op 1945. België bestaat sinds 1830 en de Russische Revolutie was in 1917."),

    # Schrijfopdracht
    open_("Vergelijk de situatie van een Belgische arbeider in 1850 met die in 1960. Noem in 4 à 6 zinnen minstens drie veranderingen en verklaar ze.",
          "In 1850 werkte een arbeider vaak meer dan twaalf uur per dag, ook kinderen werkten mee, en er was geen sociale zekerheid. In 1960 was er de achturendag of minder, kinderarbeid was verboden en er bestond sociale zekerheid met werkloosheidsuitkering, pensioen en ziekteverzekering. Arbeiders hadden ook stemrecht gekregen. Die veranderingen kwamen door de strijd van vakbonden en socialistische en christelijke arbeidersbewegingen, door het algemeen stemrecht en door het sociaal pact van 1944.",
          "Een goed antwoord noemt minstens drie veranderingen (werkuren, kinderarbeid, sociale zekerheid, stemrecht, lonen) en verklaart ze met arbeidersbewegingen, vakbonden, stemrecht of het sociaal pact."),
]
