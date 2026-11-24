"""Literaire stromingen van de middeleeuwen tot nu — pittig (🌍 Beyond doorstroom, Nederlands).

De fragmenten zijn zelf geschreven in de trant van een stroming; ze worden
aan geen enkele schrijver toegeschreven.
"""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    tabel(
        "Bij welke periode hoort elke stroming?",
        [
            ("de rederijkers", "Middeleeuwen"),
            ("de barok", "Vroegmoderne tijd"),
            ("het naturalisme", "Moderne tijd"),
            ("het magisch-realisme", "Hedendaagse tijd"),
        ],
        "De termenlijst ordent de stromingen in vier periodes.",
        kolommen=["Middeleeuwen", "Vroegmoderne tijd", "Moderne tijd", "Hedendaagse tijd"],
    ),
    volgorde(
        "Zet deze stromingen in chronologische volgorde.",
        ["De hoofse literatuur", "De renaissance", "De verlichting", "De romantiek", "De Vijftigers"],
        "Van de middeleeuwen via de vroegmoderne tijd naar de twintigste eeuw.",
    ),
    casus(
        "Lees het fragment.\n\n"
        "\"In de krocht achter de fabriek woonde het gezin Peeters met zeven kinderen in twee kamers. De vader dronk, zoals zijn vader voor hem had gedronken. "
        "Marie, de oudste, hoestte al sinds de winter. Ze wist dat ze nooit zou wegraken uit deze straat. Niemand raakte hier ooit weg.\"",
        [
            mk(
                "Bij welke stroming past dit fragment het best?",
                ["Het naturalisme", "De romantiek", "De hoofse literatuur", "Het surrealisme"],
                0,
                "Milieu en erfelijkheid bepalen het lot, en ziekte en drank worden niet geschuwd.",
            ),
            tabel(
                "Welke kenmerken van die stroming zie je?",
                [
                    ("Het milieu houdt de personages gevangen.", J),
                    ("Een gebrek wordt van vader op zoon doorgegeven.", J),
                    ("Het verhaal loopt waarschijnlijk goed af.", F),
                    ("Er is veel aandacht voor ziekte.", J),
                ],
                "Het naturalisme kijkt koel en soms genadeloos.",
            ),
            keuze(
                "Het verschil met het realisme: het naturalisme [[*verklaart de mens uit erfelijkheid en milieu|verheerlijkt het platteland|zoekt het wonderlijke op]].",
                "Het realisme toont de werkelijkheid; het naturalisme gaat verder.",
            ),
        ],
    ),
    casus(
        "Lees het fragment.\n\n"
        "\"O maan, die eenzaam boven de ruïne zweeft, neem mij mee naar het land waar mijn hart al zo lang verblijft! "
        "Hier, tussen de koude stenen van de stad, sterft mijn ziel. Ginds, voorbij de bergen, wacht het verloren paradijs.\"",
        [
            mk(
                "Bij welke stroming past dit het best?",
                ["De romantiek", "De verlichting", "De nieuwe zakelijkheid", "Het naturalisme"],
                0,
                "Gevoel, natuur, het verleden en het verlangen naar het verre.",
            ),
            tabel(
                "Welke romantische kenmerken herken je?",
                [
                    ("verlangen naar het verre en onbereikbare", J),
                    ("sterk gevoel", J),
                    ("een ruïne uit het verleden", J),
                    ("nuchtere, feitelijke taal", F),
                ],
                "Nuchtere taal hoort bij de nieuwe zakelijkheid.",
            ),
        ],
    ),
    koppel(
        "Welke stroming hoort bij elk kenmerk?",
        [
            ["Overvloed, beweging en vergankelijkheid", "Barok"],
            ["Rede, wetenschap en eigen oordeel", "Verlichting"],
            ["Terugkeer naar de klassieke oudheid", "Renaissance"],
            ["Stedelijke dichtersgilden met wedstrijden", "Rederijkers"],
        ],
        ["Vitalisme", "Relationisme"],
        "Vier stromingen van de middeleeuwen en de vroegmoderne tijd.",
    ),
    casus(
        "Lees het gedicht.\n\n"
        "de trein om acht uur twee.\n"
        "koffie in een kartonnen beker.\n"
        "de man naast mij leest de krant.\n"
        "het regent. wij zwijgen.",
        [
            mk(
                "Bij welke stroming past deze stijl het best?",
                ["De nieuwe zakelijkheid", "De barok", "De romantiek", "De voorhoofse literatuur"],
                0,
                "Kort, feitelijk en zonder sentiment: de taal van het verslag.",
            ),
            tabel(
                "Klopt dit over het gedicht uit deze stroming?",
                [
                    ("De taal is onopgesmukt.", J),
                    ("Er staan veel uitroepen van gevoel in.", F),
                    ("Alledaagse dingen worden nuchter opgesomd.", J),
                ],
                "Geen opsmuk, geen grote gevoelens.",
            ),
        ],
    ),
    casus(
        "Lees het fragment.\n\n"
        "\"Toen grootmoeder stierf, begonnen alle klokken in het dorp achteruit te lopen. Niemand vond dat vreemd. De bakker stelde zijn oven gewoon wat vroeger in, "
        "en de pastoor las de mis van de dag ervoor.\"",
        [
            mk(
                "Welke stroming herken je?",
                ["Het magisch-realisme", "Het naturalisme", "De verlichting", "De voorhoofse literatuur"],
                0,
                "Het onmogelijke gebeurt in een gewone wereld, en niemand kijkt ervan op.",
            ),
            keuze(
                "Wat het fragment typisch maakt: [[*de personages vinden het wonder normaal|alles wordt logisch verklaard|het speelt in een droom]].",
                "Bij surrealisme is het een droomwereld; bij magisch-realisme blijft de wereld herkenbaar.",
            ),
        ],
    ),
    sorteer(
        "Voorhoofs of hoofs?",
        ["Voorhoofs", "Hoofs"],
        [
            ["strijd, trouw en leenheerschap", "Voorhoofs"],
            ["de verheven liefde voor een onbereikbare dame", "Hoofs"],
            ["de verhalen rond Karel de Grote", "Voorhoofs"],
            ["het verfijnde liefdesideaal van de ridder", "Hoofs"],
        ],
        "De voorhoofse verhalen zijn ruwer, de hoofse verfijnder.",
    ),
    tabel(
        "Klopt dit over stromingen?",
        [
            ("Stromingen overlappen elkaar jarenlang.", J),
            ("Eén tekst kan kenmerken van twee stromingen dragen.", J),
            ("Een stroming eindigt op een scherp jaartal.", F),
            ("Ze helpen een tekst in zijn tijd te plaatsen.", J),
        ],
        "Stromingen zijn hulpmiddelen om te ordenen, geen hokjes.",
    ),
    casus(
        "Lees het fragment.\n\n"
        "\"Ik ben de verteller van dit verhaal, en eerlijk gezegd weet ik nog niet hoe het afloopt. Misschien laat ik Eva sterven. Misschien niet. "
        "Kies jij maar, lezer. Het is tenslotte maar een boek.\"",
        [
            mk(
                "Bij welke stroming past dat?",
                ["Het postmodernisme", "Het realisme", "De romantiek", "Het magisch-realisme"],
                0,
                "De illusie van het verhaal wordt opzettelijk doorbroken.",
            ),
            tabel(
                "Welke postmoderne kenmerken herken je?",
                [
                    ("het doorbreken van de illusie", J),
                    ("twijfel aan één vaste waarheid", J),
                    ("het geloof in de grote vooruitgang", F),
                ],
                "Het postmodernisme trekt net dat geloof in twijfel.",
            ),
        ],
    ),
    mk(
        "Een gedicht beschrijft hoe het licht één ochtend over een vijver trilt, kleur na kleur, zonder te zeggen wat de vijver is of betekent. Welke stroming?",
        ["Het impressionisme", "Het expressionisme", "Het existentialisme", "De verlichting"],
        0,
        "Niet het ding zelf, maar de vluchtige indruk op dat ene moment.",
    ),
    tabel(
        "Impressionisme of expressionisme?",
        [
            ("vluchtige zintuiglijke indrukken", "Impressionisme"),
            ("de werkelijkheid vervormen om een innerlijk gevoel te tonen", "Expressionisme"),
            ("een schreeuwende rode lucht boven een angstige stad", "Expressionisme"),
        ],
        "Indruk van buiten tegenover uitdrukking van binnen.",
        kolommen=["Impressionisme", "Expressionisme"],
    ),
    keuze(
        "Een roman over een man die beseft dat zijn leven geen vooraf gegeven zin heeft en die zelf moet kiezen, past bij het [[*existentialisme|vitalisme|classicisme]].",
        "De mens is vrij en daardoor ook verantwoordelijk.",
    ),
    mk(
        "Een gedicht vol snelheid, sport, jeugd en levenskracht. Welke stroming?",
        ["Het vitalisme", "De barok", "Het relationisme", "Het symbolisme"],
        0,
        "Vitaal betekent levenskrachtig.",
    ),
    sleep(
        "De Tachtigers stelden [[kunst]] om de kunst en de kracht van het [[individu]] centraal. De Vijftigers werkten met [[associatie]] en experiment.",
        ["rede", "zakelijkheid"],
        "Twee groepen die elk met hun voorgangers braken.",
    ),
    tabel(
        "Hoort het bij de avant-garde?",
        [
            ("bewust breken met de traditie", J),
            ("de voorhoede die eerst de gebaande wegen verlaat", J),
            ("de oude regels zo trouw mogelijk volgen", F),
        ],
        "Avant-garde betekent voorhoede.",
    ),
    mk(
        "Een roman draait volledig om de band tussen een moeder en haar dochter, en hoe die verandert. Welke hedendaagse stroming past?",
        ["Het relationisme", "Het naturalisme", "De barok", "Het existentialisme"],
        0,
        "De betrekkingen tussen mensen onderling staan centraal.",
    ),
    casus(
        "Lees het fragment.\n\n"
        "\"Wat is ons leven? Een bloem die bloeit bij dageraad en 's avonds al verwelkt. Goud, paleizen, roem: stof, rook, schaduw. "
        "Zelfs de machtigste vorst rust ooit onder dezelfde koude steen als de bedelaar.\"",
        [
            mk(
                "Uit welke stroming lijkt deze klacht over het leven te komen?",
                ["De barok", "De verlichting", "Het vitalisme", "Het neorealisme"],
                0,
                "Rijkdom van beeld naast het besef dat alles stof wordt.",
            ),
            keuze(
                "Het centrale thema is de [[*vergankelijkheid|vooruitgang|levenskracht]].",
                "Pracht en praal naast het besef dat alles voorbijgaat.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over het symbolisme?",
        [
            ("Het suggereert in plaats van te benoemen.", J),
            ("Gedichten blijven vaak meerduidig.", J),
            ("Het beschrijft enkel nuchter wat je ziet.", F),
        ],
        "Het symbool verwijst naar een diepere werkelijkheid.",
    ),
    mk(
        "Na jaren van experiment schrijft een dichter weer over een kopje thee en een fiets in eenvoudige taal. Welke stroming?",
        ["Het neorealisme", "Het surrealisme", "De barok", "Het expressionisme"],
        0,
        "De blik keert terug naar de gewone dingen.",
    ),
    tabel(
        "Surrealisme of magisch-realisme?",
        [
            ("Beelden uit de droom staan zonder logica naast elkaar.", "Surrealisme"),
            ("In een gewoon dorp gebeurt iets onmogelijks.", "Magisch-realisme"),
            ("Het onbewuste wordt verkend.", "Surrealisme"),
        ],
        "Het surrealisme verkent de droom; het magisch-realisme blijft in een herkenbare wereld.",
        kolommen=["Surrealisme", "Magisch-realisme"],
    ),
    inv(
        "De stroming die rond 1800 gevoel en verbeelding boven de rede stelde, heet de ... Antwoord met één woord.",
        ["romantiek", "de romantiek"],
        "De romantiek reageerde op de verlichting.",
    ),
    open_(
        "Kies twee stromingen die elkaar tegenspraken, bijvoorbeeld de verlichting en de romantiek. Leg uit waarin ze verschillen.",
        "De verlichting stelde de rede, de wetenschap en het eigen oordeel centraal. De romantiek zette daar het gevoel, de verbeelding, de natuur en het verlangen naar het verre en het verleden tegenover.",
    ),
]
