"""Steekproeven, samenhang en causaliteit — pittig (🌍 Beyond, wiskunde basis)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

S_GRAF = venster("steekproeven-ijsjes", 10, 34, 0, 320, 2, 20)
DAGEN = [(14, 55), (15, 70), (17, 85), (18, 260), (19, 105), (20, 125), (22, 140), (23, 150),
         (25, 175), (26, 170), (28, 205), (29, 215), (31, 240), (32, 250)]
UITSCHIETER = (18, 260)

GRAFIEKEN = [
    dict(naam=S_GRAF, titel="Temperatuur en verkochte ijsjes op 14 dagen",
         punten=[(x, y, "") for x, y in DAGEN], xlabel="°C", ylabel="ijsjes", ijk_x=2, ijk_y=40),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvraag en vragen over samenhang") for g in GRAFIEKEN]


VRAGEN = [
    klik(
        "Klik op de dag die duidelijk niet in het patroon past.",
        f"{S_GRAF}.svg",
        [punt_zone(S_GRAF, *UITSCHIETER, 30)],
        "Bij 18 °C werden 260 ijsjes verkocht, veel meer dan op de andere koele dagen. Zo'n uitschieter heeft vaak een eigen verklaring, bijvoorbeeld een feest in de buurt.",
    ),
    met_prent(f"{S_GRAF}.svg", mk(
        "Welke samenhang toont het spreidingsdiagram, als je de uitschieter even weglaat?",
        [
            "Geen samenhang: de punten liggen verspreid zonder richting",
            "Een negatieve samenhang: hoe warmer, hoe minder ijsjes",
            "Een positieve samenhang: hoe warmer, hoe meer ijsjes",
            "Een samenhang die enkel geldt boven 25 °C",
        ],
        2,
        "De punten lopen van linksonder naar rechtsboven.",
    )),
    met_prent(f"{S_GRAF}.svg", mk(
        "Een krant merkt dat er op dezelfde dagen ook meer mensen verdrinken, en kopt: 'IJsjes eten is gevaarlijk bij het zwemmen.' Wat is er aan de hand?",
        [
            "Wie ijs eet, krijgt krampen en verdrinkt daardoor vaker in het water",
            "Verdrinkingen zorgen voor meer verkochte ijsjes",
            "De warmte doet allebei stijgen: een derde variabele",
            "Er is geen samenhang: de krant heeft zich gewoon verteld",
        ],
        2,
        "Op warme dagen eten mensen meer ijs en gaan ze meer zwemmen. De temperatuur zit achter beide.",
    )),
    mk(
        "Een onderzoeker bevraagt 400 Vlaamse 17-jarigen over hoeveel ze slapen. Wat is de populatie?",
        ["De 400 bevraagde jongeren", "Alle Vlaamse 17-jarigen", "Alle Vlamingen", "De jongeren die het minst slapen"],
        1,
        "De populatie is de hele groep waarover je iets wil weten. De 400 zijn de steekproef.",
    ),
    mk(
        "Een school meet bij 50 leerlingen hoe lang ze naar school fietsen. Wat is de variabele?",
        ["De 50 leerlingen", "Alle leerlingen van de school", "De fietstijd naar school", "Het gemiddelde van de 50 tijden"],
        2,
        "De variabele is wat je bij elk element meet.",
    ),
    sorteer(
        "Is de steekproef aselect of niet?",
        ["Aselect", "Niet aselect"],
        [
            ["Een computer loot 100 nummers uit de leerlingenlijst", "Aselect"],
            ["De eerste 100 leerlingen die 's morgens binnenkomen", "Niet aselect"],
            ["Een oproep op sociale media: wie wil, vult de enquête in", "Niet aselect"],
            ["Elke leerling krijgt een nummer en je trekt 100 nummers uit een trommel", "Aselect"],
            ["Je bevraagt je vrienden en hun vrienden", "Niet aselect"],
            ["Uit elke klas loot je 4 leerlingen", "Aselect"],
        ],
        "Aselect betekent dat toeval de keuze maakt, niet de onderzoeker of de deelnemer.",
    ),
    koppel(
        "Koppel de soort steekproef aan de beschrijving.",
        [
            ["Enkelvoudig aselecte steekproef", "Elke groep van n elementen heeft evenveel kans om gekozen te worden"],
            ["Vrijwillige respons", "Wie wil, reageert"],
            ["Opportunistische steekproef", "Je neemt wie gemakkelijk te bereiken is"],
            ["Vertekende steekproef", "Een deel van de populatie is stelselmatig te veel of te weinig vertegenwoordigd"],
        ],
        ["Je bevraagt de hele populatie"],
        "Alleen bij toeval als kiezer krijg je een eerlijke kans voor iedereen.",
    ),
    tabel(
        "Juist of fout over steekproeven?",
        [
            ("Een grotere aselecte steekproef verkleint de steekproeffout.", J),
            ("Een enkelvoudig aselecte steekproef bevat nooit een steekproeffout.", F),
            ("Bij een aselecte steekproef maakt het toeval de keuze, niet de onderzoeker.", J),
            ("Een steekproef van 10 % van de populatie is altijd representatief.", F),
        ],
        "Toeval geeft altijd wat schommeling, maar minder bij een grotere steekproef. Representatief hangt af van hoe je kiest, niet van welk deel je neemt.",
    ),
    mk(
        "Welke van deze fouten is een niet-steekproeffout?",
        [
            "In een aselecte steekproef zitten door het lot toevallig wat meer meisjes dan jongens",
            "De vraag is suggestief gesteld: 'Bent u ook tegen die dure plannen?'",
            "Het resultaat wijkt door toeval 2 % af van de echte waarde in de hele populatie",
            "Een tweede aselecte steekproef geeft een iets ander resultaat",
        ],
        1,
        "Een niet-steekproeffout komt niet door het toeval van de keuze, maar door de manier van vragen, meten of verwerken.",
    ),
    keuze(
        "Een steekproef is [[*representatief|vertekend|groot]] als ze de populatie goed weerspiegelt. Door [[*randomisatie|vrijwillige respons|selectie]] laat je het toeval kiezen wie erin komt.",
        "Randomisatie betekent: het toeval beslist.",
    ),
    mk(
        "Een tv-programma vraagt kijkers te sms'en of ze voor een nieuwe wet zijn. 80 % sms't 'ja'. Waarom zegt dat weinig over alle Belgen?",
        [
            "Omdat een percentage van 80 % veel te hoog is om nog geloofwaardig te zijn",
            "Omdat enkel wie kijkt én een sterke mening heeft, de moeite neemt om te reageren",
            "Omdat een sms'je geld kost, zodat jongeren die geen beltegoed hebben wegvallen",
            "Omdat de steekproef te groot is",
        ],
        1,
        "Wie reageert, kiest zichzelf. Kijkers en mensen met een uitgesproken mening zijn oververtegenwoordigd.",
    ),
    mk(
        "Een gemeente bevraagt mensen aan een bushalte over het openbaar vervoer. Waarom is dat geen goede steekproef voor alle inwoners?",
        [
            "Wie aan de halte staat, rijdt vaker met de bus dan gemiddeld",
            "Aan een bushalte staan te weinig mensen",
            "Mensen die op een bus wachten, antwoorden nooit eerlijk op vragen van onbekenden",
            "Een bushalte is geen officiële plaats",
        ],
        0,
        "Autorijders en fietsers komen bijna niet in de steekproef: ze is vertekend.",
    ),
    volgorde(
        "Zet de stappen van een enkelvoudig aselecte steekproef in de goede volgorde.",
        [
            "Maak een lijst van alle elementen van de populatie",
            "Geef elk element een nummer",
            "Laat een toevalsgenerator n verschillende nummers kiezen",
            "Bevraag of meet de gekozen elementen",
        ],
        "Zonder volledige lijst kan niet iedereen evenveel kans krijgen.",
    ),
    mk(
        "Vijf klassen trekken elk een enkelvoudig aselecte steekproef van 50 leerlingen uit dezelfde school en berekenen hoeveel procent ontbijt. Ze vinden 62 %, 58 %, 66 %, 60 % en 64 %. Wat toont dat?",
        [
            "Vier klassen hebben fout gerekend",
            "Het echte percentage is zeker 62 %",
            "Een steekproef van 50 is altijd vertekend",
            "De variabiliteit van steekproeven: elk resultaat schommelt door toeval",
        ],
        3,
        "Verschillende aselecte steekproeven geven verschillende uitkomsten rond de echte waarde.",
    ),
    sorteer(
        "Wat verklaart de samenhang het best?",
        ["Causaliteit", "Omgekeerde causaliteit", "Derde variabele", "Toeval"],
        [
            ["Wie meer uren oefent op de piano, speelt beter", "Causaliteit"],
            ["Wie veel sport, voelt zich fitter", "Causaliteit"],
            ["Leerlingen die bijles volgen, halen lagere punten", "Omgekeerde causaliteit"],
            ["Mensen die pijnstillers nemen, hebben vaker hoofdpijn", "Omgekeerde causaliteit"],
            ["Kinderen met grotere voeten lezen beter", "Derde variabele"],
            ["In jaren met meer verkochte zonnebrillen zijn er meer bosbranden", "Derde variabele"],
            ["Het aantal films van een acteur per jaar loopt gelijk met het aantal verdrinkingen in zwembaden", "Toeval"],
            ["Het aantal piraten daalde terwijl de aarde opwarmde", "Toeval"],
        ],
        "Lage punten leiden tot bijles, hoofdpijn tot pijnstillers. Leeftijd zit achter voetmaat en lezen, zonnig droog weer achter zonnebrillen en bosbranden.",
    ),
    mk(
        "Peiling A bevraagt 100 000 vrijwillige deelnemers via een website. Peiling B is een enkelvoudig aselecte steekproef van 1000 personen. Welke is betrouwbaarder?",
        [
            "Peiling A, want met honderd keer meer deelnemers valt elke vertekening weg",
            "Ze zijn even betrouwbaar",
            "Peiling B, want vrijwillige respons blijft vertekend",
            "Dat kan je niet zeggen zonder de resultaten",
        ],
        2,
        "Een grotere steekproef verkleint toevalsschommelingen, maar lost een vertekening niet op.",
    ),
    tabel(
        "Juist of fout over samenhang en causaliteit?",
        [
            ("Een samenhang kan louter toeval zijn.", J),
            ("Een sterke samenhang in een kleine steekproef is altijd betrouwbaar.", F),
            ("Ook als de ene variabele de andere echt beïnvloedt, kan er nog een derde variabele meespelen.", J),
            ("Bij causaliteit maakt het niet uit welke variabele oorzaak is en welke gevolg.", F),
        ],
        "In een kleine steekproef kan toeval een sterke samenhang geven. Oorzaak en gevolg omdraaien is een andere uitspraak.",
    ),
    mk(
        "'Wie veel op sociale media zit, voelt zich vaker eenzaam. Sociale media maken dus eenzaam.' Welke andere verklaring is mogelijk?",
        [
            "Sociale media maken iedereen eenzaam",
            "Er is geen samenhang, want eenzaamheid kan je niet meten met een enquête",
            "De steekproef was te groot, waardoor kleine verschillen te sterk doorwegen",
            "Wie zich eenzaam voelt, zoekt meer contact via sociale media",
        ],
        3,
        "Misschien loopt het pijltje andersom: eenzaamheid leidt tot meer schermtijd.",
    ),
    sleep(
        "In een [[spreidingsdiagram]] zet je per element een punt met twee waarden. Gaan grote waarden van de ene variabele samen met kleine waarden van de andere, dan is de samenhang [[negatief]]. Een punt dat ver van het patroon ligt, heet een [[uitschieter]].",
        ["histogram", "positief", "steekproeffout"],
        "Elke stip is één element, bijvoorbeeld één dag of één persoon.",
    ),
    mk(
        "Wat is de steekproeffout?",
        [
            "Een rekenfout die de onderzoeker maakt bij het verwerken van alle antwoorden achteraf",
            "Een vraag die zo onduidelijk gesteld is dat een deel van de mensen ze verkeerd begrijpt",
            "Een afwijking van de echte populatiewaarde, door het toeval van de keuze",
            "Een steekproef die niet representatief is",
        ],
        2,
        "Ook een perfect aselecte steekproef wijkt door toeval wat af van de populatie.",
    ),
    inv(
        "In een enkelvoudig aselecte steekproef van 200 leerlingen zeggen 58 leerlingen dat ze dagelijks sporten. Welk percentage schat je voor de hele school?",
        "29",
        r"\(\frac{58}{200} = 0{,}29\), dus ongeveer \(29\) %.",
    ),
    open_(
        "Leg uit waarom vrijwillige respons meestal tot een vertekende steekproef leidt.",
        "Wie zelf kiest om te reageren, verschilt vaak van wie niet reageert: die mensen hebben meer tijd, meer interesse of een sterkere mening. Zo zijn sommige groepen oververtegenwoordigd en weerspiegelt de steekproef de populatie niet.",
        "Wie reageert, is geen toevallige groep.",
    ),
    mk(
        "Een gemeente wil weten wat alle inwoners van een nieuw park vinden. Welke steekproef is het best?",
        [
            "De bezoekers van het park op zondag",
            "Een oproep op de website van de gemeente, zodat iedereen kan reageren",
            "De leden van de gemeenteraad",
            "Een aselecte steekproef uit het bevolkingsregister",
        ],
        3,
        "Enkel de lijst van alle inwoners geeft iedereen evenveel kans. Parkbezoekers zijn vooral fans van het park.",
    ),
    mk(
        "Bij een onderzoek naar slaap en schoolresultaten antwoordt 40 % van de gekozen leerlingen niet. Waarom is dat een probleem?",
        [
            "Wie niet antwoordt, kan anders slapen of presteren dan wie wel antwoordt",
            "Er blijven te weinig antwoorden over om te rekenen",
            "Het maakt niets uit, want de steekproef was aselect",
            "Omdat 40 % meer is dan de steekproeffout",
        ],
        0,
        "Ook bij een aselecte keuze kan non-respons een vertekening geven: een niet-steekproeffout.",
    ),
    mk(
        "'Kinderen die ontbijten, halen betere punten.' Wat mag je uit zo'n samenhang besluiten?",
        [
            "Ontbijten zorgt zeker voor betere punten, want de samenhang is duidelijk",
            "Betere punten zorgen voor ontbijt",
            "Er is samenhang, maar de oorzaak ken je niet",
            "Er is geen verband, want punten hangen enkel af van studeren",
        ],
        2,
        "Een derde variabele zoals de thuissituatie kan beide beïnvloeden. Om causaliteit aan te tonen heb je een experiment met randomisatie nodig.",
    ),
    mk(
        "Je vindt in een steekproef een samenhang die louter toeval is. Wat gebeurt er meestal als je een nieuwe aselecte steekproef neemt?",
        [
            "De samenhang wordt nog sterker, omdat je nu meer gegevens hebt",
            "De samenhang verdwijnt of is veel zwakker",
            "Je vindt precies dezelfde samenhang",
            "De samenhang draait om",
        ],
        1,
        "Toeval herhaalt zich niet op dezelfde manier. Een echte samenhang komt wel telkens terug.",
    ),
    mk(
        "Een onderzoeker meet bij 30 leerlingen de schermtijd en de slaapduur. Hoeveel variabelen onderzoekt hij?",
        ["Eén: de leerlingen", "Twee", "Dertig, één per leerling", "Zestig: twee metingen keer dertig leerlingen"],
        1,
        "Een variabele is een kenmerk dat je bij elk element meet: hier schermtijd en slaapduur.",
    ),
    casus(
        "Een onderzoeker wil weten of energiedrank de reactiesnelheid verbetert. Van 60 vrijwilligers kiest elk zelf: energiedrank of water. Daarna doen ze een reactietest. De energiedrinkers reageren gemiddeld sneller.",
        [
            mk(
                "Wat is het grootste probleem van deze opzet?",
                [
                    "60 deelnemers zijn er veel te veel om nog een duidelijk verschil te kunnen zien",
                    "Water en energiedrank smaken anders",
                    "De deelnemers kozen zelf hun groep",
                    "Een reactietest meet niets",
                ],
                2,
                "Zonder toeval bij de verdeling kan je het verschil niet zomaar aan de drank toeschrijven.",
            ),
            mk(
                "Welke verborgen variabele kan het resultaat mee verklaren?",
                [
                    "De kleur en de vorm van het blikje waaruit de deelnemers dronken",
                    "Gamers kiezen misschien vaker energiedrank",
                    "Het totale aantal deelnemers dat aan de proef meedeed",
                    "De naam van de test",
                ],
                1,
                "Een kenmerk dat samenhangt met de keuze én met de reactiesnelheid, vertroebelt de vergelijking.",
            ),
            mk(
                "Hoe pak je dit onderzoek beter aan?",
                [
                    "Nog meer vrijwilligers zelf laten kiezen, zodat de groepen groter worden",
                    "Enkel gamers laten meedoen",
                    "Het lot laten bepalen wie wat drinkt",
                    "De snelste deelnemers energiedrank geven om het effect beter te zien",
                ],
                2,
                "Door randomisatie zijn andere verschillen gemiddeld gelijk verdeeld over beide groepen.",
            ),
        ],
    ),
]
