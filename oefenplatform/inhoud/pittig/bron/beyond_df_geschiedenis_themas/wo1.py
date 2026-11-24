"""De Eerste Wereldoorlog en de Vrede van Versailles — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="remember-belgium.webp", zelf=False,
         wat="Britse wervingsaffiche 'Remember Belgium - Enlist To-Day' (1915).",
         waar="Staat al op het platform (Beyond doorstroom).",
         vragen="casus over propaganda"),
    dict(bestand="tijdlijn-1750-2030.svg", zelf=True,
         wat="Dezelfde tijdlijn als bij het referentiekader.",
         vragen="klikvraag op 1917"),
]

VRAGEN = [
    # --- oorzaken
    sorteer(
        "Oorzaak of aanleiding van de Eerste Wereldoorlog?",
        ["Oorzaak", "Aanleiding"],
        [
            ["de bondgenootschappen die Europa in twee kampen verdeelden", "Oorzaak"],
            ["de wapenwedloop tussen de grote legers", "Oorzaak"],
            ["de moord in Sarajevo in juni 1914", "Aanleiding"],
            ["het nationalisme", "Oorzaak"],
            ["de wedloop om kolonies", "Oorzaak"],
        ],
        "Oorzaken bouwen jarenlang spanning op, de aanleiding is de vonk. Eén oorzaak alleen verklaart niets.",
    ),
    mk(
        "Hoe kon één moord in Sarajevo binnen vijf weken half Europa in oorlog brengen?",
        [
            "Door de bondgenootschappen werden andere landen meegesleurd",
            "De moordenaar was een Duitse generaal die de oorlog verklaarde",
            "Sarajevo was de hoofdstad van Frankrijk",
            "De moord gebeurde tijdens een conferentie van alle mogendheden",
        ],
        0,
        "Europa was in twee kampen verdeeld. Wie een bondgenoot aanviel, kreeg het hele kamp tegen zich.",
    ),
    mk(
        "Waarom heette de Balkan het kruitvat van Europa?",
        [
            "Mogendheden botsten er over hetzelfde gebied",
            "Er stonden de grootste wapenfabrieken van Europa",
            "Het was het enige gebied waar buskruit gemaakt werd",
            "De Balkan was een Britse kolonie vol wapenopslag",
        ],
        0,
        "Het Ottomaanse rijk viel er terug, en Rusland en Oostenrijk-Hongarije wilden er allebei invloed.",
    ),
    # --- België
    casus(
        "Op 2 augustus 1914 vraagt Duitsland aan België om zijn leger vrij door te laten. België weigert. Op 4 augustus valt het Duitse leger binnen.",
        [
            mk(
                "Waarom wilde Duitsland door België trekken?",
                [
                    "Om Frankrijk snel te verslaan",
                    "Om Congo van België over te nemen",
                    "Om de Belgische havens aan Rusland te geven",
                    "Omdat België Duitsland de oorlog had verklaard",
                ],
                0,
                "Het plan was om Frankrijk snel te verslaan via een omweg door België, waar de Franse verdediging zwakker was.",
            ),
            tabel(
                "Wat waren de gevolgen van de Belgische weigering?",
                [
                    ("Groot-Brittannië kwam in de oorlog.", J),
                    ("Het Belgische leger verzette zich tegen de inval.", J),
                    ("België vocht voortaan aan de kant van Duitsland.", F),
                    ("De neutraliteit beschermde België tegen de inval.", F),
                ],
                "Groot-Brittannië had de Belgische neutraliteit gewaarborgd. Die waarborg hield de inval niet tegen.",
            ),
        ],
    ),
    tabel(
        "Hoe kon een klein stukje België onbezet blijven?",
        [
            ("Het front kwam in het najaar van 1914 tot stilstand achter de IJzer.", J),
            ("De Belgen zetten de vlakte onder water met de sluizen bij Nieuwpoort.", J),
            ("De koning en het leger bleven in dat onbezette stuk.", J),
            ("De regering bleef in Brussel en bestuurde het hele land.", F),
        ],
        "Het water hield de Duitsers tegen. De regering week uit naar Frankrijk.",
    ),
    mk(
        "Waarom duurde de oorlog in het westen vier jaar in plaats van enkele maanden?",
        [
            "De verdediging was sterker dan de aanval",
            "De legers weigerden te vechten in de winter",
            "Er waren nog geen geweren of kanonnen",
            "Alle soldaten waren naar de kolonies vertrokken",
        ],
        0,
        "Machinegeweer, prikkeldraad en zwaar geschut maakten een aanval over open terrein bijna onmogelijk.",
    ),
    tabel(
        "Welke wapens horen bij de Eerste Wereldoorlog?",
        [
            ("Gifgas", J),
            ("De mitrailleur", J),
            ("De tank", J),
            ("De atoombom", F),
            ("De raket", F),
        ],
        "Atoombom en raket horen bij de volgende oorlog.",
    ),
    keuze(
        "Bij [[*Ieper|Luik|Antwerpen]] werd in april 1915 voor het eerst op grote schaal gifgas gebruikt. Daarom heet mosterdgas ook [[*yperiet|nitraat|dynamiet]].",
        "Yperiet komt van Ieper, dat bijna volledig verwoest werd.",
    ),
    # --- totale oorlog
    tabel(
        "Welke kenmerken van een totale oorlog herken je?",
        [
            ("Fabrieken maken wapens in plaats van gewone producten.", J),
            ("De staat regelt de verdeling van voedsel.", J),
            ("De pers wordt gecensureerd.", J),
            ("Enkel soldaten aan het front merken iets van de oorlog.", F),
        ],
        "In een totale oorlog wordt de hele samenleving ingezet, en is ook de burgerbevolking een doelwit.",
    ),
    casus(
        "Bekijk de Britse affiche uit 1915. Een soldaat staat voor een brandend dorp. Bovenaan staat: Remember Belgium. Onderaan: Enlist to-day, dat betekent: neem vandaag dienst.",
        [
            met_prent("remember-belgium.webp", keuze(
                "Dit is [[*propaganda|een neutraal verslag|een vredesverdrag]]: de affiche stelt de eigen zaak mooi voor en de vijand lelijk. Ze richt zich op [[*jonge Britse mannen|Duitse soldaten|Belgische boeren]].",
                "Een wervingsaffiche wil mensen overtuigen om dienst te nemen.",
            )),
            mk(
                "Waarom gebruikte een Britse affiche het lot van België?",
                [
                    "De inval in het neutrale België wekte woede",
                    "België was in 1915 een Britse kolonie in Europa",
                    "Groot-Brittannië had België in 1914 zelf aangevallen",
                    "Belgische soldaten vochten enkel in Engeland",
                ],
                0,
                "Groot-Brittannië was in de oorlog gegaan om de Belgische neutraliteit. Dat verhaal moest jonge mannen overtuigen.",
            ),
            tabel(
                "Mag je deze besluiten trekken uit de affiche?",
                [
                    ("De Britse regering wilde soldaten werven.", "Mag"),
                    ("Elk Belgisch dorp is in 1914 afgebrand.", "Mag niet"),
                    ("De affiche toont hoe men de oorlog wilde laten zien.", "Mag"),
                ],
                "Propaganda is een slechte bron over wat er precies gebeurde, maar een goede over wat men wilde laten geloven.",
                kolommen=["Mag", "Mag niet"],
            ),
        ],
    ),
    tabel(
        "Welke uitspraken over de vrouwen tijdens de Eerste Wereldoorlog kloppen?",
        [
            ("Ze namen in de fabrieken het werk van de soldaten over.", J),
            ("Ze werkten in hospitalen en hulpdiensten.", J),
            ("Ze kregen in België tijdens de oorlog stemrecht.", F),
            ("Hun werk versterkte na de oorlog het pleidooi voor hun rechten.", J),
        ],
        "Stemrecht kregen ze tijdens de oorlog niet, maar hun werk telde mee in het debat erna.",
    ),
    sorteer(
        "Bezet België of het front aan de IJzer?",
        ["Bezet België", "IJzerfront"],
        [
            ["sluikpers", "Bezet België"],
            ["deportatie van werklozen naar Duitsland", "Bezet België"],
            ["Flamenpolitik", "Bezet België"],
            ["Frontbeweging", "IJzerfront"],
            ["loopgraven met modder en ratten", "IJzerfront"],
        ],
        "Achter het front leefde men onder de bezetter. Aan de IJzer leefden de soldaten in de loopgraven.",
    ),
    koppel(
        "Welk begrip over de Eerste Wereldoorlog hoort bij elke omschrijving?",
        [
            ["De bezetter steunt Vlaamse eisen om België te verdelen.", "Flamenpolitik"],
            ["Iemand die met die politiek van de bezetter meewerkte", "Activist"],
            ["Vlaamse soldaten eisen gelijkheid voor hun taal in het leger.", "Frontbeweging"],
            ["Kranten die in het geheim gedrukt worden", "Sluikpers"],
        ],
        ["Propaganda", "Mandaat"],
        "Vier begrippen uit België tijdens de oorlog.",
    ),
    mk(
        "Waarom ontstond in bezet België de sluikpers?",
        [
            "Er was geen vrije pers meer",
            "De Belgische regering verbood alle kranten in Frankrijk",
            "Papier was gratis tijdens de oorlog",
            "De Duitse bezetter vroeg zelf om nieuwe kranten",
        ],
        0,
        "Onder de bezetter waren er geen vrije verkiezingen en geen vrije pers. Wie toch wilde schrijven, deed het in het geheim.",
    ),
    # --- einde
    klik(
        "Klik op de tijdlijn op het jaar waarin de Verenigde Staten in de oorlog kwamen en in Rusland een revolutie uitbrak.",
        "tijdlijn-1750-2030.svg",
        [[54.0, 25, 6.2, 55]],
        "1917, net vóór het streepje van 1920.",
    ),
    tabel(
        "Waarom was 1917 een keerpunt?",
        [
            ("De Verenigde Staten kwamen aan de kant van de Entente.", J),
            ("Rusland verdween door een revolutie uit de oorlog.", J),
            ("Duitsland tekende in 1917 de vrede van Versailles.", F),
        ],
        "In hetzelfde jaar kwam er een sterke bondgenoot bij en viel er een weg. Versailles volgde pas in 1919.",
    ),
    volgorde(
        "Zet deze gebeurtenissen over de Eerste Wereldoorlog in chronologische volgorde.",
        ["De moord in Sarajevo", "De Duitse inval in België", "Gifgas bij Ieper", "De wapenstilstand", "Het Verdrag van Versailles"],
        "Juni 1914, 4 augustus 1914, april 1915, 11 november 1918 en 1919.",
    ),
    casus(
        "Een Duitse krant schrijft in 1920: \"Het dictaat van Versailles is een schande. Duitsland werd niet gehoord, en nu moet het alleen de schuld dragen en betalen.\"",
        [
            mk(
                "Waarom spreekt de krant van een dictaat?",
                [
                    "Duitsland mocht niet onderhandelen, enkel tekenen",
                    "Het verdrag werd geschreven door een Duitse dictator",
                    "Het verdrag werd in Berlijn gedicteerd aan Frankrijk",
                    "Duitsland had het verdrag zelf voorgesteld",
                ],
                0,
                "Het woord zelf is al politiek: het zegt dat het verdrag opgelegd werd en dus niet rechtsgeldig zou zijn.",
            ),
            tabel(
                "Welke voorwaarden van Versailles bedoelt de krant met 'de schuld dragen en betalen'?",
                [
                    ("het artikel dat Duitsland de schuld van de oorlog gaf", J),
                    ("de herstelbetalingen voor de aangerichte schade", J),
                    ("de oprichting van de Volkenbond", F),
                ],
                "Op het schuldartikel steunden de herstelbetalingen.",
            ),
            mk(
                "Wat leer je als historicus vooral uit deze bron?",
                [
                    "Hoe het verdrag in Duitsland werd ervaren",
                    "Wat er precies in alle artikels van het verdrag stond",
                    "Hoe Frankrijk over het verdrag dacht",
                    "Dat het verdrag nooit getekend werd",
                ],
                0,
                "De bron toont de wrok die later politiek gebruikt werd.",
            ),
        ],
    ),
    tabel(
        "Wat legde het Verdrag van Versailles aan Duitsland op?",
        [
            ("Enkel nog een klein leger", J),
            ("De kolonies verdeeld als mandaatgebied", J),
            ("De Elzas en Lotharingen naar Frankrijk", J),
            ("Het Rijnland naar Frankrijk", F),
        ],
        "Het Rijnland bleef Duits, maar zonder leger.",
    ),
    keuze(
        "België kreeg na de oorlog [[*Eupen en Malmedy|de Elzas en Lotharingen|het Rijnland]] en het mandaat over [[*Ruanda-Urundi|Katanga|Egypte]].",
        "Eupen en Malmedy werden Belgisch. Ruanda-Urundi was een Duitse kolonie die als mandaatgebied aan België kwam.",
    ),
    mk(
        "Waarom was de Volkenbond van bij het begin zwak?",
        [
            "De Verenigde Staten werden nooit lid",
            "Hij had zijn zetel in Duitsland, het verliezende land",
            "Hij had het grootste leger van de wereld",
            "Hij werd al in 1919 opgeheven",
        ],
        0,
        "De Amerikaanse senaat weigerde het verdrag. Zonder de VS en zonder eigen leger had de Volkenbond weinig macht.",
    ),
    tabel(
        "Hoe veranderde de kaart van Europa door de Eerste Wereldoorlog?",
        [
            ("Het Oostenrijks-Hongaarse rijk verdween.", J),
            ("Er kwamen nieuwe staten zoals Polen en Tsjechoslowakije.", J),
            ("De nieuwe staten hadden vaak minderheden binnen hun grenzen.", J),
            ("Het Duitse keizerrijk werd groter.", F),
        ],
        "Vier keizerrijken verdwenen. De nieuwe grenzen schiepen nieuwe minderheden.",
    ),
    inv(
        "Op welke dag wordt in België nog elk jaar de wapenstilstand herdacht?",
        ["11 november", "11/11", "elf november"],
        "Op 11 november 1918 zwegen de wapens.",
    ),
    open_(
        "Leg uit hoe het Verdrag van Versailles een bron van latere problemen werd.",
        "Duitsland mocht niet onderhandelen, kreeg in het schuldartikel de schuld van de oorlog en moest herstelbetalingen doen. Het verloor gebied en kolonies en mocht maar een klein leger hebben. Dat liet wrok na, die later politiek gebruikt werd. Ook de nieuwe staten met minderheden en een zwakke Volkenbond zonder de VS maakten de vrede broos.",
    ),
    open_(
        "Leg uit waarom je voor de Eerste Wereldoorlog beter van meerdere oorzaken spreekt dan van één schuldige.",
        "Bondgenootschappen verdeelden Europa in twee kampen, er was een wapenwedloop, het nationalisme zette volken tegen elkaar op, en de wedloop om kolonies maakte de mogendheden rivalen. De spanningen op de Balkan en de moord in Sarajevo waren de vonk. Pas samen verklaren ze waarom een moord tot een wereldoorlog leidde.",
    ),
]
