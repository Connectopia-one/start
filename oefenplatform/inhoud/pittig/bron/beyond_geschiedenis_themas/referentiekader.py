"""Het historisch referentiekader — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik

PRENTEN = [
    dict(bestand="tijdlijn-1750-2030.svg", zelf=True,
         wat="Tijdlijn van 1750 tot 2030, een streepje om de tien jaar, jaartallen om de vijftig jaar.",
         vragen="klikvragen op 1789 en 1945"),
]

VRAGEN = [
    # --- de drie assen en de periodes
    tabel(
        "Een leerling legt een gebeurtenis op het historisch referentiekader. Welke van deze stappen horen bij een van de drie assen?",
        [
            ("Ze zoekt uit in welke periode de gebeurtenis valt.", J),
            ("Ze bepaalt of het om iets lokaals, nationaals of mondiaals gaat.", J),
            ("Ze kijkt of het vooral politiek, sociaal, economisch of cultureel is.", J),
            ("Ze bewijst met het kader dat de gebeurtenis echt zo gebeurd is.", F),
        ],
        "De eerste drie stappen horen elk bij een as. Het kader ordent, maar bewijst niets over wat er gebeurd is.",
    ),
    volgorde(
        "Zet deze gebeurtenissen in de volgorde van de periodes waarin ze vallen, van oud naar jong.",
        ["Columbus steekt de oceaan over", "De Franse Revolutie breekt uit", "Het Congres van Wenen vergadert", "De Tweede Wereldoorlog eindigt", "De Berlijnse Muur valt"],
        "1492, 1789, 1814-1815, 1945 en 1989.",
    ),
    klik(
        "Klik op de tijdlijn op het scharnierpunt waarmee de moderne tijd begint.",
        "tijdlijn-1750-2030.svg",
        [[14.0, 25, 6.2, 55]],
        "De moderne tijd begint in het westerse kader met de Franse Revolutie van 1789, net voor het streepje van 1790.",
    ),
    klik(
        "Klik op de tijdlijn op het scharnierpunt waarmee de hedendaagse tijd begint.",
        "tijdlijn-1750-2030.svg",
        [[62.7, 25, 6.2, 55]],
        "1945, het einde van de Tweede Wereldoorlog, net voor het streepje van 1950.",
    ),
    mk(
        "Waarom laat men de hedendaagse tijd niet beginnen met het einde van de Eerste Wereldoorlog?",
        [
            "Omdat de machtsverhoudingen pas na de volgende oorlog ingrijpend verschoven",
            "Omdat er na 1945 in Europa nergens nog oorlog gevoerd werd",
            "Omdat de Eerste Wereldoorlog buiten Europa niet gevoeld werd",
            "Omdat er van voor 1945 bijna geen geschreven bronnen bewaard zijn",
        ],
        0,
        "Het kader kiest een later scharnierpunt, omdat de wereldorde pas dan grondig veranderde. Dat er nadien geen oorlog meer was of dat bronnen ontbreken, klopt niet.",
    ),
    keuze(
        "De Reformatie valt in de [[*vroegmoderne tijd|moderne tijd|middeleeuwen]], want die periode loopt van de [[*16de tot de 18de eeuw|14de tot de 15de eeuw|19de tot de 20ste eeuw]].",
        "De vroegmoderne tijd begint met 1492 en loopt tot het einde van de 18de eeuw. De Reformatie, in de 16de eeuw, valt daar middenin.",
    ),
    keuze(
        "Situeer de Franse Revolutie. In de tijd is ze het scharnierpunt naar de [[*moderne tijd|vroegmoderne tijd|hedendaagse tijd]]. In de ruimte is ze in de eerste plaats [[*West-Europees|maritiem|ruraal]]. Bij de domeinen hoort ze vooral in het [[*politieke|economische|culturele]] domein.",
        "Ze opent de moderne tijd. Ze speelt zich af in Frankrijk, in West-Europa, en gaat in de eerste plaats over wie de macht heeft: politiek.",
    ),
    # --- structuurbegrippen van de tijd
    koppel(
        "Welk structuurbegrip van de tijd past bij elke zin van een historicus?",
        [
            ["De boeren in deze streek werkten eeuwenlang op dezelfde manier.", "Continuïteit"],
            ["In 1989 eindigde met één klap de deling van Europa.", "Breuk"],
            ["Dezelfde fabrieken kwamen in Engeland vroeger op gang dan elders.", "Ongelijktijdigheid"],
            ["Ik deel de 19de en 20ste eeuw in drie stukken met elk een naam.", "Periodisering"],
        ],
        ["Chronologie"],
        "Iets dat lang hetzelfde blijft is continuïteit; een scherpe onderbreking is een breuk. Dezelfde ontwikkeling die elders later komt, is ongelijktijdigheid. Stukken met een naam maken is periodiseren; chronologie zet alleen in volgorde.",
    ),
    mk(
        "Een leerling schrijft: \"Ik gebruik de chronologie om aan te tonen dat het een mondiale gebeurtenis was.\" Wat loopt er mis?",
        [
            "Chronologie hoort bij de tijd en zegt niets over waar iets zich afspeelde",
            "Chronologie hoort bij de maatschappelijke domeinen en niet bij de tijd",
            "Mondiaal is geen structuurbegrip, het juiste woord is continentaal",
            "Er loopt niets mis, chronologie situeert ook in de ruimte",
        ],
        0,
        "Chronologie ordent in de tijd. Om te tonen dat iets mondiaal was, heb je structuurbegrippen van de ruimte nodig.",
    ),
    tabel(
        "Gelijktijdig of ongelijktijdig? Lees elke situatie.",
        [
            ("In hetzelfde jaar 1830 wordt België onafhankelijk en rijdt in Engeland een nieuwe spoorlijn, zonder dat het ene met het andere te maken heeft.", "Gelijktijdig"),
            ("De industrialisatie komt in Engeland eerst op gang, en pas later in andere landen.", "Ongelijktijdig"),
            ("Vlaanderen bleef landelijk terwijl Wallonië al volop industrialiseerde.", "Ongelijktijdig"),
            ("In 1968 protesteren studenten in Parijs en valt in België Leuven Vlaams.", "Gelijktijdig"),
        ],
        "Gelijktijdigheid is dat twee dingen in dezelfde periode gebeuren, ook als ze niets met elkaar te maken hebben. Ongelijktijdigheid is dat dezelfde ontwikkeling elders vroeger of later komt.",
        kolommen=["Gelijktijdig", "Ongelijktijdig"],
    ),
    sleep(
        "Een plotse en diepe omslag heet een [[revolutie]], een geleidelijke verandering een [[evolutie]]. Afspreken vanaf welk punt je de jaren telt, heet [[tijdrekening]].",
        ["continuïteit", "chronologie", "duur"],
        "Revolutie en evolutie verschillen in tempo. Tijdrekening is de afspraak over het beginpunt van de jaartelling.",
    ),
    # --- ruimte
    sorteer(
        "Bij welke structuurbegrippen van de ruimte hoort elk voorbeeld?",
        ["Stedelijk", "Ruraal", "Maritiem"],
        [
            ["Een fabrieksstad met overvolle beluiken", "Stedelijk"],
            ["Boeren die met de werkmanstrein naar de fabriek sporen, maar thuis op het platteland wonen", "Ruraal"],
            ["Een havenstad die leeft van de handel over zee", "Maritiem"],
            ["Een dorp waar bijna iedereen van de landbouw leeft", "Ruraal"],
        ],
        "Stedelijk gaat over de stad, ruraal over het platteland, maritiem over de zee. De werkmanstrein liet arbeiders net op het platteland blijven wonen.",
    ),
    mk(
        "Australië ligt op de wereldkaart helemaal in het oosten, en toch noemt men het een westers land. Wat leer je daaruit over het begrip westers?",
        [
            "Het wijst ook op een manier van samenleven, met eigen instellingen, mensbeeld en economie",
            "Het wijst enkel op landen die ten westen van de nulmeridiaan liggen op de kaart",
            "Het is een begrip uit de tijd, geen begrip uit de ruimte, en hoort bij chronologie",
            "Het is een fout van de kaartenmakers die men nooit heeft rechtgezet",
        ],
        0,
        "Westers zegt niet alleen iets over een plaats, maar ook over hoe een samenleving georganiseerd is.",
    ),
    # --- domeinen
    sorteer(
        "In welk maatschappelijk domein situeer je elke gebeurtenis in de eerste plaats?",
        ["Politiek", "Sociaal", "Economisch", "Cultureel"],
        [
            ["Het Congres van Wenen tekent nieuwe grenzen", "Politiek"],
            ["Arbeiders richten vakbonden op", "Sociaal"],
            ["De Sovjet-Unie start de vijfjarenplannen", "Economisch"],
            ["Hendrik Conscience schrijft De Leeuw van Vlaanderen", "Cultureel"],
            ["Het algemeen enkelvoudig stemrecht wordt ingevoerd", "Politiek"],
        ],
        "Grenzen en stemrecht zijn politiek, vakbonden sociaal, de planeconomie economisch. Een roman hoort bij taal en letteren, dus cultureel.",
    ),
    mk(
        "Een propaganda-affiche van Stalin prijst de stijgende productie van staal aan en toont hem als vader van het volk. In welke domeinen situeer je de affiche? (meerdere antwoorden)",
        ["Het politieke domein", "Het culturele domein", "Het economische domein", "In geen enkel domein, want het is maar een affiche"],
        [0, 1, 2],
        "Ze verheerlijkt het bewind (politiek), gebruikt beeldtaal en een wereldbeeld (cultureel) en prijst productiecijfers aan (economisch). Een gebeurtenis of bron hoort niet altijd bij precies één domein.",
    ),
    # --- wat een periodisering is
    tabel(
        "Een periode bakent men af... Welke uitspraken kloppen?",
        [
            ("met een selectie van kenmerken en gebeurtenissen.", J),
            ("met een symbolische begin- en einddatum.", J),
            ("achteraf, als constructie.", J),
            ("op het moment zelf, door wie toen leefde.", F),
        ],
        "Wie in 1492 leefde, wist niet dat de middeleeuwen bijna voorbij waren. Een periode is een constructie achteraf, met een gekozen begin- en einddatum.",
    ),
    mk(
        "Waarom heet 1492 een symbolische begindatum?",
        [
            "De datum staat voor een verandering die in werkelijkheid veel langer duurde",
            "Alles in Europa veranderde precies in dat ene jaar, van de ene dag op de andere",
            "Niemand weet nog zeker in welk jaar Columbus de oceaan overstak",
            "Het jaar werd door de paus gekozen als nieuw beginpunt van de tijdrekening",
        ],
        0,
        "Een symbolische datum is een herkenbaar ijkpunt voor een lange verandering, niet het moment waarop alles in één keer omsloeg.",
    ),
    koppel(
        "Welke blik verraadt elke keuze?",
        [
            ["Een handboek behandelt de 19de eeuw enkel aan de hand van Europese staten.", "Ruimtelijk beperkte blik"],
            ["Men kiest het Congres van Wenen als scharnierpunt voor de hele wereld.", "Eurocentrische blik"],
        ],
        ["Meerdere perspectieven", "Verstopte morele maatstaf"],
        "Het handboek kijkt maar naar een stuk van de wereld. Wenen als wereldscharnier neemt Europa als maatstaf. Meerdere perspectieven is net wat in beide ontbreekt.",
    ),
    mk(
        "Wat is het probleem als een tekst de middeleeuwen de donkere eeuwen noemt?",
        [
            "In de naam zit al een oordeel, nog voor je iets onderzocht hebt",
            "De middeleeuwen hebben in werkelijkheid maar enkele decennia geduurd",
            "Uit de middeleeuwen zijn geen geschreven bronnen bewaard gebleven",
            "Donker is een structuurbegrip van de ruimte en niet van de tijd",
        ],
        0,
        "De naam draagt een morele maatstaf mee. Een periodisering is altijd een keuze van wie ze maakt, en hier kleurt die keuze het beeld al vooraf.",
    ),
    inv(
        "Hoe heet de blik waarbij je de eigen groep als maatstaf voor de rest neemt? (één woord)",
        "etnocentrisch",
        "Een etnocentrische blik meet anderen af aan de eigen groep. Neem je Europa als maatstaf, dan spreek je van eurocentrisch.",
    ),
    # --- andere periodiseringen
    mk(
        "China deelt zijn verleden in volgens dynastieën. Wat volgt daaruit?",
        [
            "Het volgt hetzelfde principe met andere kenmerken, en is dus niet verkeerd",
            "Het is een foute indeling, want ze valt niet samen met de zeven westerse periodes",
            "Het is geen periodisering, want dynastieën zijn een politiek en geen tijdsbegrip",
            "Het bewijst dat China geen eigen geschiedenis had vóór de komst van Europeanen",
        ],
        0,
        "Elke periodisering bakent af met een selectie van kenmerken. China kiest andere kenmerken dan het Westen, en dat maakt ze niet fout.",
    ),
    tabel(
        "Welke uitspraken over scharnierpunten kloppen?",
        [
            ("Een scharnierpunt is een gebeurtenis die de overgang vormt tussen twee periodes.", J),
            ("Een scharnierpunt in Europa is ook overal elders in de wereld een scharnierpunt.", F),
            ("De boekdrukkunst kan een scharnierpunt zijn, ook al is ze niet politiek.", J),
            ("Een scharnierpunt ligt altijd in het politieke domein.", F),
        ],
        "Scharnierpunten liggen niet enkel in de politiek: ook de boekdrukkunst en de industrialisering tellen. En wat in Europa een breuk is, is dat elders niet altijd.",
    ),
    open_(
        "Een vriend zegt: \"De westerse indeling in zeven periodes is gewoon hoe de geschiedenis in elkaar zit.\" Weerleg dat met twee argumenten.",
        "Een periodisering is een constructie achteraf: wie toen leefde, wist niet dat er een periode eindigde. Bovendien is ze een keuze van wie ze maakt. China deelt zijn verleden bijvoorbeeld in volgens dynastieën, en een scharnierpunt in Europa is dat niet overal ter wereld. Het kader is een hulpmiddel, geen natuurwet.",
    ),
    casus(
        "Een handboek uit een ander land deelt de geschiedenis in volgens de regeringen van zijn eigen koningen. De 19de eeuw begint er in 1830 en eindigt in 1909. Het boek spreekt nergens over de Franse Revolutie.",
        [
            mk(
                "Welke conclusie mag je hieruit trekken?",
                [
                    "Het boek periodiseert met andere kenmerken: wie periodiseert, kiest wat belangrijk is",
                    "Het boek bevat een fout, want de 19de eeuw loopt altijd van 1801 tot 1900",
                    "Het boek bewijst dat de Franse Revolutie nooit heeft plaatsgevonden",
                    "Het boek gebruikt geen periodisering maar enkel een chronologie",
                ],
                0,
                "Elke periodisering is een keuze. Dit boek kiest de eigen koningen als grens. Dat toont wat de maker belangrijk vindt.",
            ),
            keuze(
                "Dat het boek de Franse Revolutie weglaat, wijst op een [[*ruimtelijk beperkte|chronologische|maritieme]] blik, en kan leiden tot een gebrek aan [[*meerdere perspectieven|scharnierpunten|tijdrekening]].",
                "Wie enkel naar de eigen staat kijkt, ziet maar een stuk van de wereld en hoort de stemmen van anderen niet.",
            ),
            mk(
                "Welke vraag stel je het best eerst als historicus bij dit boek?",
                [
                    "Wie maakte deze indeling, en waarom kiest hij net die grenzen?",
                    "Welk jaar is het juiste begin van de 19de eeuw, 1801 of 1830?",
                    "Hoeveel bladzijden telt het boek, en is het dus betrouwbaar?",
                    "Waarom staat het boek niet in de zeven westerse periodes?",
                ],
                0,
                "Een periodisering zegt iets over wie ze maakt. Daarom vraag je naar de maker en zijn keuze, niet naar de juiste grens.",
            ),
        ],
    ),
    mk(
        "Een historicus kiest het Congres van Wenen als scharnierpunt in plaats van de Franse Revolutie. Welke periode wordt in zijn indeling daardoor iets langer?",
        [
            "De vroegmoderne tijd",
            "De moderne tijd",
            "De hedendaagse tijd",
            "De middeleeuwen",
        ],
        0,
        "Wenen (1814-1815) komt na 1789. Schuift het einde van de vroegmoderne tijd op, dan wordt die periode langer en de moderne tijd korter.",
    ),
    tabel(
        "Een leerling legt de industrialisering op het referentiekader. Welke beweringen zijn juist?",
        [
            ("Ze raakte niet enkel de economie, maar ook de verhoudingen tussen sociale groepen.", J),
            ("In Engeland kwam ze vroeger op gang dan in Vlaanderen, en dat is ongelijktijdigheid.", J),
            ("Omdat ze geleidelijk verliep, kan je ze enkel een breuk noemen.", F),
            ("Ze begon pas in de hedendaagse tijd, na 1945.", F),
        ],
        "Een geleidelijke verandering is net geen breuk. De industrialisering raakte ook het sociale domein, denk aan de klassenmaatschappij, en begon al in de moderne tijd.",
    ),
    sleep(
        "Het referentiekader ordent in [[tijd]], [[ruimte]] en maatschappelijke domeinen. Het is een [[hulpmiddel]], geen natuurwet.",
        ["bewijs", "chronologie", "wet"],
        "Drie assen, en het kader ordent zonder iets te bewijzen.",
    ),
    mk(
        "Een leerling zegt: \"De val van de Berlijnse Muur is continuïteit, want daarna bleef Europa bestaan.\" Wat is de beste reactie?",
        [
            "Het is verandering: de deling van Europa eindigde ermee",
            "Het klopt, want continuïteit betekent dat een land blijft bestaan",
            "Het is ongelijktijdigheid, want de Muur viel niet overal tegelijk",
            "Het is chronologie, want het gaat om een jaartal",
        ],
        0,
        "Continuïteit is wat in grote lijnen hetzelfde blijft. Met 1989 kwam er net een einde aan de deling van Europa: verandering.",
    ),
]
