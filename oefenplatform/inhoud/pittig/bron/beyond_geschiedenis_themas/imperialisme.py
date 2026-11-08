"""Modern imperialisme, Congo en China — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, met_prent

PRENTEN = [
    dict(bestand="afrika-1914.webp", zelf=False,
         wat="Kaart van Afrika in 1914, met de koloniën per Europese mogendheid in een eigen kleur. Ethiopië en Liberia moeten als zelfstandig te zien zijn.",
         waar="Wikimedia Commons, zoek 'Africa 1914 colonial map' (veel kaarten in het publieke domein).",
         vragen="kaartvraag over de verdeling van Afrika"),
    dict(bestand="rubber-coils.webp", zelf=False,
         wat="De spotprent 'In the Rubber Coils' uit het Britse blad Punch van 1906 (Edward Linley Sambourne): een slang met het hoofd van Leopold II wurgt een Congolese man. Publiek domein.",
         waar="Wikimedia Commons, zoek 'In the Rubber Coils Punch 1906'.",
         vragen="casus over de kritiek op de Congo-Vrijstaat"),
]

VRAGEN = [
    tabel(
        "Welke technische middelen maakten het modern imperialisme mogelijk?",
        [
            ("Repeteergeweren en mitrailleurs", J),
            ("Stoomschepen die rivieren op konden varen", J),
            ("Kinine als bescherming tegen malaria", J),
            ("Vliegtuigen om het binnenland te verkennen", F),
        ],
        "Wapens, stoomschepen en kinine gaven Europa de voorsprong. Vooral kinine opende het Afrikaanse binnenland. Vliegtuigen speelden rond 1880 nog geen rol.",
    ),
    sorteer(
        "Bij welk motief van het modern imperialisme hoort elke uitspraak?",
        ["Economisch", "Politiek", "Cultureel"],
        [
            ["Onze fabrieken hebben goedkope grondstoffen nodig.", "Economisch"],
            ["We moeten nieuwe kopers vinden voor onze producten.", "Economisch"],
            ["Een land zonder koloniën telt niet mee onder de grote mogendheden.", "Politiek"],
            ["Deze haven is een strategisch punt op de route naar Azië.", "Politiek"],
            ["Wij brengen de beschaving naar andere volkeren.", "Cultureel"],
        ],
        "Grondstoffen en afzetmarkten zijn economisch, prestige en strategische punten politiek. Het idee dat Europa beschaving bracht, is een cultureel motief.",
    ),
    mk(
        "Een historicus noemt de jaren na 1880 een wedloop om Afrika. Wat bedoelt hij daarmee?",
        [
            "Ze bezetten gebieden uit schrik dat een andere mogendheid hen voor was",
            "De Afrikaanse volkeren vroegen zelf om zo snel mogelijk bezet te worden",
            "Er werd een echte race tussen ontdekkingsreizigers ingericht, voor een prijs",
            "De koloniën werden in enkele maanden verdeeld en daarna nooit meer veranderd",
        ],
        0,
        "Rond 1880 begon Europa in enkele decennia bijna heel Afrika te bezetten, omdat elke mogendheid vreesde de boot te missen.",
    ),
    mk(
        "Het sociaal darwinisme paste het idee van de strijd om het bestaan toe op volkeren. Waarvoor werd het gebruikt?",
        [
            "Om overheersing van andere volkeren goed te praten",
            "Om de afschaffing van alle koloniën te eisen",
            "Om aan te tonen dat alle volkeren gelijk zijn",
            "Om de arbeiders in Europa tot staking aan te zetten",
        ],
        0,
        "Het sociaal darwinisme deed alsof sterkere volkeren vanzelf over zwakkere mochten heersen. Zo werd het een rechtvaardiging voor het imperialisme.",
    ),
    mk(
        "Missionarissen in de koloniën waren tegelijk hulpverleners en een arm van het koloniale bestel. Wat betekent dat?",
        [
            "Ze bouwden scholen en hielpen mensen, maar verspreidden tegelijk het geloof en de waarden van de kolonisator",
            "Ze werkten in het geheim tegen de koloniale overheid en steunden overal de gewapende opstanden van de bevolking",
            "Ze waren eigenlijk soldaten van het koloniale leger die zich als priesters verkleedden om dorpen te bespieden",
            "Ze hielden zich alleen bezig met de handel in rubber en ivoor, en kwamen nooit in een school of ziekenhuis",
        ],
        0,
        "Hun hulp was echt, maar ze droegen ook mee het koloniale project. Zo'n dubbele rol vraagt om meerdere perspectieven.",
    ),
    keuze(
        "Op de Conferentie van Berlijn van [[*1884 en 1885|1815|1914]] spraken de Europese mogendheden af dat je een gebied werkelijk moest [[*bezetten en besturen|kopen en verkopen|in kaart brengen]] om er aanspraak op te maken.",
        "Berlijn legde de spelregels vast. Wie een stuk Afrika wilde, moest er effectief aanwezig zijn.",
    ),
    met_prent("afrika-1914.webp", tabel(
        "Bekijk de kaart van Afrika in 1914. Welke uitspraken kan je met de kaart en je kennis staven?",
        [
            ("Vrijwel heel Afrika was onder Europese mogendheden verdeeld.", J),
            ("Ethiopië en Liberia bleven zelfstandig.", J),
            ("De grenzen volgden overal de woongebieden van de Afrikaanse volkeren.", F),
            ("Congo was in 1914 een kolonie van de Belgische staat.", J),
        ],
        "Tegen 1914 was bijna alles verdeeld, behalve Ethiopië en Liberia. Veel grenzen lijken met een lat getrokken: ze volgden Europese afspraken, niet de bestaande samenlevingen. Congo was sinds 1908 Belgisch Congo.",
    ), volgt=True),
    tabel(
        "Een Afrikaanse historica somt de erfenis van de koloniale bezetting op. Welke punten noemt ze terecht?",
        [
            ("Grenzen die dwars door volkeren liepen", J),
            ("Een economie afgestemd op uitvoer naar Europa", J),
            ("Gezagsstructuren die door de kolonisator vervangen werden", J),
            ("Een einde aan elke vorm van ongelijkheid", F),
        ],
        "Grenzen, economie en bestuur werden naar Europese noden hertekend. Ongelijkheid nam daardoor net toe.",
    ),
    koppel(
        "Welke mogendheid breidde uit in welk gebied in Azië?",
        [
            ["Groot-Brittannië", "Indië"],
            ["Frankrijk", "Indochina"],
            ["Nederland", "De Indische archipel"],
            ["De Verenigde Staten", "De Filipijnen"],
        ],
        ["Congo"],
        "Ook buiten Afrika werd verdeeld: Indië, Indochina, de Indische archipel, en na 1898 de Filipijnen voor de Verenigde Staten.",
    ),
    mk(
        "Wat hadden Japan en Rusland gemeen in het tijdperk van het modern imperialisme?",
        [
            "Ze breidden zelf uit in Azië, Japan na zijn snelle modernisering en Rusland over land tot aan de Stille Oceaan",
            "Ze werden allebei door Europese mogendheden volledig gekoloniseerd en verloren zo hun zelfstandigheid en eigen bestuur",
            "Ze bleven allebei volledig buiten het imperialisme en hadden geen enkele interesse in de gebieden van Azië",
            "Ze vochten samen met het Chinese keizerrijk tegen alle westerse handelaars en wonnen die lange strijd",
        ],
        0,
        "Japan moderniseerde vanaf de Meiji-restauratie van 1868 en werd zelf een koloniale macht. Rusland breidde over land uit naar het oosten.",
    ),
    tabel(
        "Juist of fout? Lees elke uitspraak over de Congo-Vrijstaat.",
        [
            ("De Vrijstaat was tussen 1885 en 1908 het persoonlijke bezit van Leopold II.", J),
            ("De Vrijstaat was een kolonie van de Belgische staat.", F),
            ("Stanley verkende het gebied en sloot verdragen met lokale leiders.", J),
            ("De Vrijstaat verdiende vooral geld met koffie en katoen.", F),
        ],
        "Congo was eerst van Leopold II zelf. Het geld kwam vooral uit rubber en ivoor. Pas in 1908 nam de Belgische staat over.",
    ),
    volgorde(
        "Zet in de juiste volgorde.",
        ["De Conferentie van Berlijn begint", "De Congo-Vrijstaat wordt opgericht", "Morel en Casement voeren campagne tegen het bewind", "De Belgische staat neemt Congo over"],
        "1884, 1885, rond 1900, en 1908.",
    ),
    casus(
        "Bekijk de spotprent uit het Britse blad Punch van 1906. Een slang met het hoofd van Leopold II heeft zich rond een Congolese man gewonden. Het onderschrift luidt: In the Rubber Coils.",
        [
            met_prent("rubber-coils.webp", mk(
                "Waarop doelt de tekenaar met de rubberen slang?",
                ["Op het rubberregime dat de bevolking verstikte", "Op de handel in ivoor met Europa", "Op de spoorlijnen die Leopold liet aanleggen", "Op de missiescholen in Congo"],
                0,
                "Dorpen moesten vaste hoeveelheden rubber leveren en werden zwaar gestraft bij te weinig. De slang beeldt dat systeem uit.",
            ), volgt=True),
            tabel(
                "Welke uitspraken over deze bron kloppen?",
                [
                    ("Ze hoort bij de internationale kritiek op de Congo-Vrijstaat rond 1900.", J),
                    ("Ze is een primaire bron voor wie die kritiek onderzoekt.", J),
                    ("De maker wilde Leopold II bij de lezers populair maken.", F),
                    ("Omdat het een spotprent is, is ze waardeloos voor een historicus.", F),
                ],
                "De prent toont hoe men in Groot-Brittannië over Leopold II dacht. Een spotprent is gekleurd, maar daarom niet onbruikbaar: ze is een uitstekende bron over de kritiek.",
            ),
            mk(
                "Welk gevolg had de internationale campagne waartoe deze prent behoorde?",
                ["De Belgische staat nam de kolonie in 1908 over", "Leopold II kreeg er in 1908 nog meer gebied bij", "Congo werd in 1908 een onafhankelijke staat", "Groot-Brittannië bezette Congo in 1908"],
                0,
                "Onder druk van Morel, Casement en schrijvers als Mark Twain en Arthur Conan Doyle werd de Vrijstaat in 1908 Belgisch Congo.",
            ),
        ],
    ),
    mk(
        "Een leerling moet het rubberregime uitleggen aan een klasgenoot. Welke uitleg is juist?",
        [
            "Dorpen moesten vaste hoeveelheden rubber leveren, met zware straffen en gijzeling van vrouwen en kinderen",
            "Congolezen kregen per kilo rubber een eerlijk loon dat hoger lag dan in Europa, en kozen zelf of ze werkten",
            "Alleen Europese arbeiders mochten rubber tappen; de Congolese bevolking werd daar volledig van uitgesloten",
            "Rubber werd vrij verhandeld op de lokale markten, zonder enige tussenkomst of controle van de Vrijstaat",
        ],
        0,
        "Quota, straffen en gijzelingen: daardoor nam de bevolking sterk af door geweld, honger en ziekte.",
    ),
    sorteer(
        "Welke rol speelde elke macht in de koloniale drie-eenheid van Belgisch Congo?",
        ["Staat", "Kerk", "Bedrijven"],
        [
            ["Ambtenaren en een leger", "Staat"],
            ["Missies en scholen", "Kerk"],
            ["Mijnen en plantages", "Bedrijven"],
            ["Koper uit Katanga ontginnen", "Bedrijven"],
        ],
        "Staat, kerk en grote bedrijven bestuurden samen. De mijnen in Katanga leverden onder meer koper.",
    ),
    mk(
        "Wat betekent paternalisme in het koloniale bestuur van Belgisch Congo, en hoe zag je dat in het onderwijs?",
        [
            "Men behandelde de bevolking als op te voeden kinderen; het onderwijs bleef vooral lager onderwijs",
            "Men liet de bevolking volledig zelf beslissen; het onderwijs werd overal universitair, gratis en verplicht",
            "Men verbood elke vorm van onderwijs in Congo, ook bij de missies, tot aan de onafhankelijkheid in 1960",
            "Men stuurde alle Congolese kinderen naar scholen in België om er hun hele opleiding te volgen",
        ],
        0,
        "Paternalisme is opvoeden van bovenaf. Daarom waren er bij de onafhankelijkheid zo weinig Congolese universitair geschoolden.",
    ),
    keuze(
        "Belgisch Congo leverde onder meer koper uit [[*Katanga|Kivu|Leopoldstad]], diamant en [[*uranium|steenkool|katoen]].",
        "Katanga was de rijkste mijnprovincie. Het uranium uit Congo kreeg later een grote strategische waarde.",
    ),
    mk(
        "De beeldvorming over Leopold II in België ging van koning-bouwer naar een veel kritischer blik. Wat betekent dat?",
        [
            "De feiten zijn niet veranderd, wel de vragen die men stelt en de bronnen die men laat spreken",
            "Historici hebben ontdekt dat Leopold II in werkelijkheid nooit iets met Congo te maken had",
            "De feiten over de Congo-Vrijstaat zijn achteraf door nieuwe historici verzonnen",
            "Een kritische blik betekent dat men in België niets meer over hem mag zeggen",
        ],
        0,
        "Beeldvorming verandert door nieuwe vragen en nieuwe bronnen, zoals Congolese stemmen. Dat is iets anders dan de feiten veranderen.",
    ),
    tabel(
        "In de 19de eeuw kampte China met binnenlandse problemen. Welke horen daarbij?",
        [
            ("Een sterk groeiende bevolking op te weinig grond", J),
            ("Wijdverspreide corruptie in het bestuur", J),
            ("Grote opstanden zoals die van de Taiping", J),
            ("Een tekort aan steden en handelaars", F),
        ],
        "Bevolkingsdruk, corruptie en opstanden verzwakten de Qing-dynastie van binnenuit.",
    ),
    mk(
        "Waarover ging de Opiumoorlog met Groot-Brittannië?",
        [
            "Over de Britse handel in opium die China wilde stoppen",
            "Over de Chinese handel in thee die Groot-Brittannië verbood",
            "Over de verdeling van Afrika tussen China en Europa",
            "Over de opstand van de Taiping tegen de keizer",
        ],
        0,
        "China wilde de opiumhandel stoppen, de Britten wilden doorgaan. Na de nederlaag moest China bij het Verdrag van Nanking van 1842 Hongkong afstaan.",
    ),
    inv(
        "Welke stad moest China in 1842 bij het Verdrag van Nanking afstaan aan Groot-Brittannië?",
        "Hongkong",
        "Hongkong ging naar Groot-Brittannië. Zo'n verdrag heet ongelijk, omdat het enkel China verplichtingen oplegde.",
    ),
    sorteer(
        "Hoort het kenmerk bij het imperialisme in Congo of in China?",
        ["Congo", "China"],
        [
            ["Volledige bezetting en rechtstreeks bestuur", "Congo"],
            ["Invloedssferen van verschillende mogendheden", "China"],
            ["Ongelijke verdragen", "China"],
            ["Eerst het persoonlijke bezit van een koning", "Congo"],
            ["Formeel bleef het een keizerrijk", "China"],
        ],
        "Twee vormen van hetzelfde imperialisme: Congo werd volledig bezet, China bleef formeel zelfstandig maar werd in invloedssferen verdeeld.",
    ),
    mk(
        "Een invloedssfeer is een lichtere vorm van overheersing dan een kolonie. Waarom?",
        [
            "De mogendheid maakt er de dienst uit zonder het gebied zelf te besturen",
            "De mogendheid bestuurt het gebied rechtstreeks met eigen ambtenaren",
            "De bevolking kiest er zelf een Europese koning als staatshoofd",
            "Er is geen enkele buitenlandse invloed op handel of politiek",
        ],
        0,
        "In een invloedssfeer heeft een buitenlandse mogendheid veel macht over handel en politiek, maar het land bestuurt zichzelf formeel nog.",
    ),
    mk(
        "Welk gevolg hadden de westerse contacten op lange termijn voor het Chinese keizerrijk?",
        [
            "Het gezag van de keizer verzwakte, en in 1912 viel het rijk",
            "Het keizerrijk werd sterker en veroverde delen van Europa",
            "China werd in 1912 een Britse kolonie zoals Indië",
            "Het keizerrijk sloot alle havens en had geen contact meer",
        ],
        0,
        "Nederlagen, ongelijke verdragen en opstanden ondermijnden de Qing-dynastie. In 1912 kwam er een einde aan het keizerrijk.",
    ),
    sorteer(
        "Welke aard van intercultureel contact herken je in elke situatie?",
        ["Gewelddadig contact", "Uitbuiting", "Cultuurdominantie"],
        [
            ["Britse schepen beschieten Chinese havens in de Opiumoorlog", "Gewelddadig contact"],
            ["Congolese dorpen moeten zonder loon rubber leveren", "Uitbuiting"],
            ["Missiescholen leren kinderen dat de Europese cultuur de hoogste is", "Cultuurdominantie"],
            ["Ongelijke verdragen leggen enkel China verplichtingen op", "Uitbuiting"],
        ],
        "Oorlog is gewelddadig contact. Werk en grondstoffen afnemen zonder eerlijke tegenprestatie is uitbuiting. De eigen cultuur als hogere opleggen is cultuurdominantie.",
    ),
    open_(
        "Vergelijk het imperialisme in Congo met dat in China. Geef één gelijkenis en twee verschillen.",
        "Gelijkenis: in beide gevallen haalden westerse mogendheden economisch voordeel uit een ander gebied en verloor de lokale bevolking zeggenschap. Verschillen: Congo werd volledig bezet en rechtstreeks bestuurd, eerst door Leopold II en daarna door de Belgische staat. China bleef formeel een keizerrijk, maar werd in invloedssferen verdeeld en moest ongelijke verdragen tekenen.",
    ),
    sleep(
        "Dat koloniale grenzen met een [[lat]] getrokken lijken, betekent dat ze Europese [[afspraken]] volgden en geen bestaande samenlevingen. Een gebied waar een mogendheid de dienst uitmaakt zonder het te besturen, is een [[invloedssfeer]].",
        ["rivier", "volksraadpleging", "kolonie"],
        "Grenzen volgden de onderhandelingstafel in Europa. Een invloedssfeer is lichter dan een kolonie.",
    ),
    tabel(
        "Waarom bleef China formeel een keizerrijk, maar was het toch niet echt zelfstandig? Juist of fout?",
        [
            ("Mogendheden maakten er in invloedssferen de dienst uit zonder het land te besturen.", J),
            ("Ongelijke verdragen legden China verplichtingen op die het Westen niet had.", J),
            ("China werd net als Congo volledig bezet en rechtstreeks bestuurd.", F),
            ("De keizer verloor door de westerse contacten aan gezag.", J),
        ],
        "China bleef op papier zelfstandig, maar invloedssferen en ongelijke verdragen hielden het onder westerse druk. Congo werd wel volledig bezet.",
    ),
]
