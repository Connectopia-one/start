"""Standen, domein en stad — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="domein.svg", zelf=True,
         wat="Schema van een domein: A een groot veld met voren, B smalle stroken met elk een huisje, C bos, D molen en oven.",
         vragen="klikvraag herendiensten, koppelvraag B, C en D"),
    dict(bestand="stad.svg", zelf=True,
         wat="Schema van een middeleeuwse stad binnen een muur aan een rivier: A hoge toren, B lange hal op de markt, C kerk met kruis.",
         vragen="klikvraag op de rivier, koppelvraag A, B en C"),
    dict(bestand="tijdlijn-1000-1500.svg", zelf=True,
         wat="Tijdlijn van 1000 tot 1500, een groot streepje om de honderd jaar, een klein om de tien jaar.",
         vragen="klikvragen op de 11de eeuw en op het jaar van de pest"),
    dict(bestand="drie-standen-miniatuur.webp", zelf=False,
         wat="Middeleeuwse miniatuur met een geestelijke, een ridder en een boer naast elkaar, uit het 13de-eeuwse handschrift Li livres dou santé (British Library, Sloane 2435).",
         waar="Wikimedia Commons, zoek op 'Cleric-Knight-Workman' (publiek domein).",
         vragen="tabelvraag over de prent als bron"),
    dict(bestand="pest-doornik.webp", zelf=False,
         wat="Miniatuur uit de kroniek van Gilles Li Muisis (rond 1350): inwoners van Doornik begraven pestslachtoffers.",
         waar="Wikimedia Commons, zoek op 'Burying Plague Victims of Tournai' (publiek domein).",
         vragen="tabelvraag over de gevolgen van de pest"),
]

TL = "tijdlijn-1000-1500.svg"

VRAGEN = [
    # --- de drie standen
    tabel(
        "Klopt elke uitspraak over de middeleeuwse standensamenleving?",
        [
            ("Je geboorte bepaalde bijna helemaal welk leven je kreeg.", J),
            ("Een boer die hard werkte, klom gewoonlijk op tot de adel.", F),
            ("De voorrechten gingen over van ouder op kind.", J),
            ("De adel had stemrecht bij verkiezingen.", F),
        ],
        "Niet je verdienste maar je geboorte bepaalde je plaats, en de voorrechten waren erfelijk. Van sociale mobiliteit was nauwelijks sprake. Verkiezingen bestonden niet.",
    ),
    koppel(
        "Welke taak hoort volgens de middeleeuwse voorstelling bij elke stand?",
        [["de geestelijkheid", "bidden"], ["de adel", "strijden"], ["de derde stand", "werken"]],
        ["handel drijven"],
        "De geestelijkheid bad voor het zielenheil van allen, de adel beschermde met het zwaard, en de derde stand werkte en onderhield de twee andere. Handel drijven was geen taak in deze driedeling.",
    ),
    met_prent(
        "drie-standen-miniatuur.webp",
        tabel(
            "Bekijk de miniatuur uit een 13de-eeuws handschrift met drie figuren naast elkaar. Klopt elke uitspraak?",
            [
                ("De prent toont dat elke stand een eigen taak had.", J),
                ("Wie zulke voorstellingen maakte, stond er zelf meestal bovenaan in.", J),
                ("De prent bewijst dat de boeren tevreden waren met hun plaats.", F),
                ("De prent is waarschijnlijk gemaakt door een boer uit de derde stand.", F),
            ],
            "De driedeling werd opgeschreven en verbeeld door geestelijken. Een prent toont hoe zij de samenleving zagen, niet wat de boeren ervan vonden.",
        ),
    ),
    sorteer(
        "Was dit een voorrecht van de adel of niet?",
        ["Voorrecht van de adel", "Geen voorrecht van de adel"],
        [
            ["eigen rechtspraak over de bewoners van zijn domein", "Voorrecht van de adel"],
            ["vrijstelling van bepaalde belastingen", "Voorrecht van de adel"],
            ["het recht om te jagen in de heerlijke bossen", "Voorrecht van de adel"],
            ["stemrecht bij de verkiezing van de koning", "Geen voorrecht van de adel"],
        ],
        "Rechtspraak, minder belastingen en het jachtrecht waren voorrechten van de adel. Verkiezingen bestonden niet.",
    ),
    mk(
        "Waarom bleef de ongelijkheid tussen de standen zo lang bestaan?",
        [
            "Ze gold als door God gewild en de voorrechten waren erfelijk",
            "De derde stand had zelf gestemd voor een wet die de adel beschermde",
            "De koning betaalde de boeren een vergoeding zodat ze niet protesteerden",
            "Er waren te weinig mensen in de derde stand om in opstand te komen",
        ],
        0,
        "De ordening werd voorgesteld als door God gewild, en wie ze in vraag stelde, ging in tegen de Kerk. Bovendien gingen de voorrechten over van ouder op kind.",
    ),
    mk(
        "In welke maatschappelijke domeinen situeer je de standensamenleving? (meerdere antwoorden)",
        ["Het sociale domein", "Het politieke domein", "Het culturele domein", "Het maritieme domein"],
        [0, 1, 2],
        "Ze bepaalt wie waar staat (sociaal) en wie mag beslissen (politiek), en de Kerk levert de rechtvaardiging (cultureel). Maritiem is geen maatschappelijk domein maar een ruimtebegrip.",
    ),
    mk(
        "Waarom vielen de joden buiten de middeleeuwse driedeling?",
        [
            "Het was een christelijk beeld van een christelijke samenleving",
            "Ze woonden allemaal buiten Europa en kwamen er enkel om te handelen",
            "Ze hoorden bij de adel en hadden dus een eigen, hogere plaats",
            "De Kerk had hen een vierde stand gegeven met eigen rechten en taken",
        ],
        0,
        "De driedeling ging uit van een samenleving waarin iedereen christen was. Wie dat niet was, kreeg er geen plaats in.",
    ),
    # --- het domein
    klik(
        "Bekijk het schema van een domein. Klik op het deel waar een horige zijn herendiensten deed.",
        "domein.svg", [[30.0, 32.3, 32.0, 64.5]],
        "Herendiensten deed een horige op het vroonland, het deel dat de heer voor zichzelf liet bewerken. In het schema is dat het grote veld A.",
    ),
    dict(
        **koppel(
            "Bekijk het schema van een domein. Wat gebeurde er op elke plaats met een letter?",
            [
                ["B", "hier bewerkte een boer een eigen hoeve"],
                ["C", "hier mocht enkel de heer jagen"],
                ["D", "hier betaalde men een heffing om graan te malen of brood te bakken"],
            ],
            ["hier werd de handelswaar gekeurd"],
            "B is het hoevenland, verdeeld onder de boeren. C zijn de bossen van de heer. Bij D staan de molen en de oven, waar men moest betalen. Waren keuren deed men in de lakenhalle van een stad, niet op een domein.",
        ),
        afbeelding_url="/examenvormen/geschiedenis-boost/domein.svg",
    ),
    tabel(
        "Klopt elke uitspraak over een horige?",
        [
            ("Hij was niet vrij om het domein te verlaten.", J),
            ("Zijn heer kon hem verkopen zoals een slaaf.", F),
            ("Hij had een eigen hoeve.", J),
            ("Hij moest een deel van zijn oogst afstaan.", J),
            ("Hij diende als ridder in het leger van de koning.", F),
        ],
        "Een horige zat vast aan het domein, maar was geen slaaf en had een eigen hoeve. Hij gaf een deel van de oogst af. In het leger van de koning dienen hoorde niet bij zijn plichten.",
    ),
    mk(
        "Wat betekent het dat een domein zelfvoorzienend was?",
        [
            "Bijna alles wat men nodig had, werd er zelf gemaakt",
            "De heer kocht alles op de markt van de dichtstbijzijnde stad",
            "Het domein kreeg elk jaar voedsel en kleding van de koning",
            "De boeren verkochten bijna hun hele oogst aan kooplui van ver",
        ],
        0,
        "Voedsel, kleding en gereedschap kwamen van het domein zelf. Er werd weinig gekocht en weinig verkocht.",
    ),
    # --- landbouw en handel
    sleep(
        "Naast het drieslagstelsel kwamen in de middeleeuwen ook de [[keerploeg]] en het [[haam]] op. Met dat laatste trekt een paard met zijn [[schouders]] in plaats van met zijn keel.",
        ["kunstmest", "poten", "dorsmachine"],
        "De keerploeg en het haam zijn middeleeuwse vernieuwingen. Met het haam trekt een paard met zijn schouders. Kunstmest komt pas in de 19de eeuw.",
    ),
    mk(
        "Waarom leverde het drieslagstelsel meer op dan het oudere tweeslagstelsel?",
        [
            "Er lag maar een derde braak in plaats van de helft",
            "Het braakland werd elk jaar met kunstmest bemest",
            "De boeren hoefden geen herendiensten meer te doen",
            "Er werd voortaan het hele jaar door op elk veld gezaaid",
        ],
        0,
        "Bij twee delen rust de helft van de grond, bij drie delen maar een derde. Zo is er meer grond in gebruik.",
    ),
    mk(
        "Hoe hangt de vooruitgang in de landbouw samen met de groei van de steden?",
        [
            "Meer voedsel liet de bevolking groeien en niet iedereen moest nog boer zijn",
            "De boeren verhuisden naar de stad omdat er op het land niets meer groeide",
            "De koning verbood landbouw buiten de muren, dus ging iedereen in de stad wonen",
            "Steden werden gebouwd op de velden die door de nieuwe ploegen vrijkwamen",
        ],
        0,
        "Meer voedsel leidde tot een groeiende bevolking. Omdat er een overschot was, kon een deel van de mensen iets anders doen dan voedsel produceren.",
    ),
    sorteer(
        "Verhandelde men dit vooral op de lokale markt of vooral over lange afstand?",
        ["Lokale markt", "Lange afstand"],
        [
            ["voedsel", "Lokale markt"],
            ["gereedschap", "Lokale markt"],
            ["specerijen", "Lange afstand"],
            ["zijde", "Lange afstand"],
            ["edelmetaal", "Lange afstand"],
        ],
        "Dagelijkse dingen verhandelde men dichtbij. Kostbare waren kwamen van ver.",
    ),
    mk(
        "Waarom loonde handel over lange afstand vooral voor waren zoals zijde en specerijen?",
        [
            "Vervoer was traag en duur, dus moest de vracht licht en veel waard zijn",
            "Zwaar graan mocht volgens de Kerk niet buiten het eigen graafschap",
            "Zijde en specerijen bederven niet, en dat was de enige reden",
            "Alleen edelen mochten handel drijven, en zij kochten geen gewone waren",
        ],
        0,
        "Vervoer kostte veel tijd en geld. Dat loonde enkel voor wat veel waarde in weinig gewicht had.",
    ),
    # --- de steden
    klik(
        "Klik op de tijdlijn op de eeuw waarin de steden in West-Europa weer opbloeien.",
        TL, [[5.0, 25, 17.5, 55]],
        "Vanaf de 11de eeuw, dus vanaf het jaar 1000, bloeien de steden weer op.",
    ),
    klik(
        "Bekijk het schema van een middeleeuwse stad. Klik op wat het best verklaart waarom de stad juist op deze plek groeide.",
        "stad.svg", [[0, 84, 100, 16]],
        "De rivier. Water was de goedkoopste manier om zware vracht te vervoeren: een schip draagt veel meer dan een kar.",
    ),
    dict(
        **koppel(
            "Bekijk het schema van de stad. Waarvoor diende elk gebouw met een letter?",
            [
                ["A", "bewaarplaats van de stedelijke privileges"],
                ["B", "handelswaar verhandelen en keuren"],
                ["C", "centrum van het godsdienstige leven"],
            ],
            ["woning van de graaf"],
            "A is het belfort, B de lakenhalle, C de kathedraal. De graaf woonde niet in een van deze gebouwen.",
        ),
        afbeelding_url="/examenvormen/geschiedenis-boost/stad.svg",
    ),
    tabel(
        "Wat regelde een ambacht of gilde? Klopt elke uitspraak?",
        [
            ("wie het beroep mocht uitoefenen", J),
            ("de kwaliteit van het geleverde werk", J),
            ("de opleiding tot meester", J),
            ("de belastingen van het hele graafschap", F),
        ],
        "Een ambacht regelde de toegang tot het beroep, de kwaliteit en de opleiding. De belastingen van het graafschap waren de zaak van de vorst.",
    ),
    volgorde(
        "Zet de stappen naar een eigen werkplaats in de juiste volgorde.",
        ["leerjongen", "gezel", "meesterproef", "meester"],
        "Je begon als leerjongen, werd gezel, legde een meesterproef af en werd dan meester.",
    ),
    inv(
        "Hoe heet een oorkonde waarin een vorst een stad stadsrechten geeft? Antwoord met één woord.",
        ["keure", "een keure", "de keure"],
        "Zo'n oorkonde met stadsrechten heet een keure.",
    ),
    mk(
        "Waarom gaf een vorst een stad privileges?",
        [
            "Hij had geld nodig, en de stad kon ervoor betalen",
            "De paus verplichtte elke vorst om zijn steden vrij te laten",
            "Hij wilde zelf in de stad wonen en een markt beginnen",
            "De boeren van het platteland vroegen het hem op hun knieën",
        ],
        0,
        "De vorst had geld nodig en de stad had geld. In ruil kreeg ze eigen rechtspraak, eigen bestuur en het recht op een markt.",
    ),
    keuze(
        "Op het domein betaalde men vaak [[*in natura|met munten]], in de stad steeds vaker [[*met geld|in graan]]. Uit het werk van de [[*wisselaars|ridders|monniken]] groeit later het bankwezen. De geldeconomie situeer je vooral in het [[*economische|culturele|politieke]] domein.",
        "Op het domein betaalde men in dagen werk en in graan, in de stad met munten. Wisselaars, krediet en boekhouding komen op, en daaruit groeit het bankwezen. Dat is in de eerste plaats economisch.",
    ),
    sleep(
        "Een kleine groep rijke koopmansfamilies, de [[patriciërs]], bestuurde de stad. Daartegen kwamen de [[ambachten]] in opstand, en in de Vlaamse steden kregen ze een plaats in het stadsbestuur.",
        ["horigen", "bisschoppen", "ridders"],
        "Binnen de muren was niet iedereen gelijk. De patriciërs bestuurden, de ambachten kwamen in opstand en veroverden een plaats in het bestuur.",
    ),
    # --- de pest
    klik(
        "Klik op de tijdlijn op het jaar waarin de pest West-Europa begint te treffen.",
        TL, [[63.8, 25, 3.5, 55]],
        "Vanaf 1347 sterft op enkele jaren tijd naar schatting een derde van de bevolking.",
    ),
    met_prent(
        "pest-doornik.webp",
        tabel(
            "Bekijk de miniatuur van inwoners van Doornik die slachtoffers van de pest begraven. Wat waren de gevolgen van de pest? Klopt elke uitspraak?",
            [
                ("De lonen stegen.", J),
                ("Er kwam veel grond leeg te liggen.", J),
                ("Er waren plots te veel arbeiders.", F),
                ("De bevolking groeide sneller dan ooit.", F),
            ],
            "Doordat zoveel mensen stierven, werd arbeid schaars. Daarom stegen de lonen en kwam grond leeg te liggen. De bevolking kromp.",
        ),
    ),
    # --- stad en platteland
    casus(
        "Jan woont met zijn ouders op een domein. Op een dag trekt hij naar de stad en gaat er werken als leerjongen bij een wever. Hij blijft er wonen. Zijn broer blijft op het land en verkoopt elke week graan op de stadsmarkt.",
        [
            mk(
                "Volgens het spreekwoord 'stadslucht maakt vrij' kon Jan zijn horigheid kwijtraken. Na hoe lang meestal?",
                ["een jaar en een dag", "een week", "zeven jaar", "pas na zijn dood"],
                0,
                "Wie lang genoeg in de stad verbleef, meestal een jaar en een dag, kon zijn horigheid kwijtraken.",
            ),
            tabel(
                "Stad en platteland waren met elkaar verweven. Klopt elke uitspraak?",
                [
                    ("De stad haalde haar nieuwe inwoners van het platteland.", J),
                    ("De stad haalde haar voedsel van het platteland.", J),
                    ("Stedelijke burgers kochten grond buiten de muren.", J),
                    ("Het platteland bestuurde de stad.", F),
                ],
                "Jan en zijn broer tonen het allebei: mensen en voedsel gingen van het land naar de stad. Burgers kochten grond buiten de muren. Het bestuur ging net andersom.",
            ),
            open_(
                "Is de groei van de steden een verandering of een continuïteit? Leg uit in twee of drie zinnen.",
                "Het is een verandering. Er ontstaat een nieuwe groep die rijk is zonder adellijk te zijn, en de oude driedeling had daar geen plaats voor. Ook betaalt men in de stad met geld in plaats van in natura.",
                "Een goed antwoord kiest voor verandering en noemt iets wat echt nieuw is, zoals rijke burgers buiten de drie standen.",
            ),
        ],
    ),
]
