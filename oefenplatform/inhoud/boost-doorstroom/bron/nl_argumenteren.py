# -*- coding: utf-8 -*-
"""De vragen voor "Argumenteren: stelling, argumentsoort en drogreden" (🚀 Boost doorstroom, Nederlands).

Uit allebei de vakfiches. Nederlands 1 vraagt dat je zelf argumenteert,
Nederlands 2 dat je een argumentatieve tekst beoordeelt. De begrippen zijn
dezelfde: feit en mening, stelling, standpunt, argument, tegenargument en
conclusie, de soorten argumentatie, en de drogredenen.

Deel 1 zet de bouwstenen neer. Deel 2 gaat over de soorten argumentatie en over
redeneringen die er goed uitzien maar niet deugen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke zin is een feit?",
        opties=[
            "De film duurt honderdtweeënveertig minuten.",
            "De film duurt veel te lang naar mijn zin.",
            "De film is de mooiste van het hele jaar.",
            "De film had nooit gemaakt mogen worden.",
        ],
        antwoord=0,
        uitleg="Een feit kan je nagaan: je kijkt de speelduur op. De drie andere zinnen geven een oordeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een stelling en een standpunt?",
        opties=[
            "de stelling staat ter discussie, het standpunt is de kant die jij kiest",
            "de stelling is een feit, het standpunt is een mening",
            "de stelling staat vooraan, het standpunt helemaal achteraan",
            "de stelling is van de schrijver, het standpunt van de lezer",
        ],
        antwoord=0,
        uitleg="'De schooldag moet later beginnen' is de stelling. Jij bent voor of tegen: dat is je standpunt.",
    ),
    dict(
        type="invultekst",
        vraag="De bewering waarover de discussie gaat, heet de ___.",
        antwoord=["stelling", "de stelling"],
        uitleg="Een goede stelling is discutabel: je kan er redelijkerwijs voor of tegen zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een feit kan je nagaan, een mening niet.",
        antwoord=True,
        uitleg="Bij een feit bestaat er een bron die uitsluitsel geeft. Een mening kan je onderbouwen, maar niet bewijzen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zinnen geven een mening?",
        opties=[
            "Die nieuwe brug is lelijk.",
            "Volgens mij komt het niet goed.",
            "Het is schandalig dat dit mag.",
            "De brug is honderd meter lang.",
        ],
        antwoord=[0, 1, 2],
        uitleg="De laatste zin geeft een meetbaar gegeven. De drie andere bevatten een oordeel of een waardewoord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een tegenargument?",
        opties=[
            "een reden die tégen de stelling pleit",
            "een reden die jouw standpunt versterkt",
            "de slotzin van een argumentatieve tekst",
            "een feit dat niemand in twijfel trekt",
        ],
        antwoord=0,
        uitleg="Een sterk betoog noemt de tegenargumenten en weerlegt ze, in plaats van ze te verzwijgen.",
    ),
    dict(
        type="invultekst",
        vraag="Wat je op het einde van je betoog uit je argumenten afleidt, is de ___.",
        antwoord=["conclusie", "de conclusie"],
        uitleg="De conclusie mag niet meer beweren dan de argumenten dragen. Anders klopt de redenering niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een mening wordt een feit zodra heel veel mensen het ermee eens zijn.",
        antwoord=False,
        uitleg="Hoeveel mensen iets vinden, verandert niets aan de vraag of het nagegaan kan worden. Dat veel mensen iets vinden is zelf wél een feit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als je een tegenargument weerlegt?",
        opties=[
            "je toont aan waarom het niet opgaat",
            "je herhaalt je eigen stelling nog eens",
            "je laat het weg uit je tekst",
            "je geeft toe dat je ongelijk hebt",
        ],
        antwoord=0,
        uitleg="Weerleggen is het tegenargument eerst eerlijk noemen en er dan een reden tegenover zetten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin kan dienen als stelling voor een debat?",
        opties=[
            "Huiswerk moet worden afgeschaft.",
            "Onze school telt achthonderd leerlingen.",
            "De les begint elke dag om half negen.",
            "Het regende gisteren de hele dag.",
        ],
        antwoord=0,
        uitleg="Alleen de eerste zin is discutabel. De drie andere zijn feiten: daar valt niet voor of tegen te zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een goed opgebouwd betoog noemt ook de argumenten van de tegenpartij.",
        antwoord=True,
        uitleg="Wie de tegenargumenten noemt en weerlegt, komt sterker over dan wie doet alsof ze niet bestaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de opbouw van een argumentatieve tekst?",
        opties=[
            "een duidelijke stelling",
            "argumenten die de stelling steunen",
            "een weerlegging van tegenargumenten",
            "een regelmatig rijmschema",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een rijmschema hoort bij poëzie. De drie andere elementen maken samen een betoog.",
    ),
    dict(
        type="invultekst",
        vraag="Een reden die tégen de stelling pleit, heet een ___.",
        antwoord=["tegenargument", "een tegenargument"],
        uitleg="Wie zijn eigen tegenargumenten kent, kan ze ook weerleggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="'De temperatuur lag gisteren zes graden boven het gemiddelde.' Wat voor uitspraak is dat?",
        opties=[
            "een feit, want je kan het opzoeken",
            "een mening, want het klinkt overdreven",
            "een stelling, want je kan het betwisten",
            "een conclusie, want het staat achteraan",
        ],
        antwoord=0,
        uitleg="Er staat geen waardeoordeel in en er bestaat een meting die uitsluitsel geeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan merk je in een tekst dat de schrijver subjectief wordt?",
        opties=[
            "aan waardewoorden zoals schitterend of belachelijk",
            "aan het gebruik van jaartallen en getallen",
            "aan de indeling in korte alinea's",
            "aan de aanwezigheid van tussentitels",
        ],
        antwoord=0,
        uitleg="Waardewoorden, uitroeptekens en woorden als 'uiteraard' verraden het oordeel van de schrijver.",
    ),
    dict(
        type="waarofniet",
        vraag="Een argument telt pas mee als er cijfers bij staan.",
        antwoord=False,
        uitleg="Cijfers zijn één soort argumentatie. Een vergelijking, een oorzaak-gevolgredenering of een deskundige kunnen even sterk zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het bij overtuigen belangrijk feiten en meningen uit elkaar te houden?",
        opties=[
            "omdat je lezer anders niet weet wat hij kan nagaan",
            "omdat meningen in een betoog verboden zijn",
            "omdat feiten altijd korter zijn dan meningen",
            "omdat je anders geen conclusie mag trekken",
        ],
        antwoord=0,
        uitleg="Een mening die als feit gepresenteerd wordt, voelt oneerlijk aan. Wie het onderscheid duidelijk maakt, wint vertrouwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden verraden meestal dat er een mening volgt?",
        opties=["volgens mij", "prachtig", "zou moeten", "in 2024"],
        antwoord=[0, 1, 2],
        uitleg="Een jaartal is een gegeven. De drie andere kondigen een oordeel of een wens aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="De stelling luidt: 'Jongeren onder de zestien mogen geen sociale media gebruiken.' Wat is een standpunt?",
        opties=[
            "Ik ben daartegen.",
            "Sociale media bestaan sinds de jaren negentig.",
            "Veel jongeren gebruiken sociale media.",
            "Sociale media zijn apps op je telefoon.",
        ],
        antwoord=0,
        uitleg="Een standpunt is de kant die je kiest. De andere zinnen zijn feiten over het onderwerp.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de reden die je geeft om je standpunt te steunen?",
        antwoord=["argument", "een argument"],
        uitleg="Eén stelling, meerdere argumenten, en op het einde een conclusie: dat is de ruggengraat van een betoog.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="'In Finland werkt dit systeem al vijftien jaar, dus het kan hier ook.' Op welke soort argumentatie steunt die zin?",
        opties=[
            "een vergelijking",
            "wetenschappelijk onderzoek",
            "cijfers en statistieken",
            "een beroep op een autoriteit",
        ],
        antwoord=0,
        uitleg="Je legt twee gevallen naast elkaar. Zo'n argument staat of valt met de vraag of de twee echt vergelijkbaar zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Uit een studie van de universiteit blijkt dat leerlingen beter presteren na acht uur slaap.' Welke soort argumentatie?",
        opties=[
            "wetenschappelijk onderzoek",
            "een vergelijking",
            "een beroep op medelijden",
            "oorzaak en gevolg",
        ],
        antwoord=0,
        uitleg="De schrijver leunt op onderzoek. Sterk, zolang je erbij zet wie het onderzoek deed en hoe groot het was.",
    ),
    dict(
        type="invultekst",
        vraag="'Acht op de tien leerlingen zegt te weinig te slapen.' Zo'n argument steunt op ___.",
        antwoord=["cijfers", "statistieken", "cijfers en statistieken"],
        uitleg="Cijfers overtuigen sterk, maar vraag altijd: hoeveel mensen zijn bevraagd, en door wie?",
    ),
    dict(
        type="waarofniet",
        vraag="Een beroep op een autoriteit is altijd een drogreden.",
        antwoord=False,
        uitleg="Een arts over gezondheid is een geldig autoriteitsargument. Het wordt pas een drogreden als de deskundige over iets anders spreekt dan zijn vak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten argumentatie noemt de vakfiche?",
        opties=[
            "argumentatie op basis van vergelijking",
            "argumentatie op basis van oorzaak en gevolg",
            "argumentatie op basis van een autoriteit",
            "argumentatie op basis van alliteratie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alliteratie is een stijlfiguur uit de poëzie. De fiche noemt ook nog onderzoek en cijfers als basis.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Jij hebt nooit gewerkt, dus over lonen moet jij zwijgen.' Wat is hier mis?",
        opties=[
            "de persoon wordt aangevallen in plaats van het argument",
            "er worden te veel cijfers gebruikt",
            "de conclusie staat te vroeg in de tekst",
            "er wordt een vergelijking gemaakt die klopt",
        ],
        antwoord=0,
        uitleg="Dat heet een persoonlijke aanval. Wie iemand is, zegt niets over de vraag of zijn argument deugt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een redenering die overtuigend klinkt maar niet deugt?",
        antwoord=["drogreden", "een drogreden", "drogredenering"],
        uitleg="Drogredenen vermijd je in je eigen tekst en herken je in die van anderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Iedereen in onze klas doet het, dus het kan geen kwaad.' Welke drogreden is dat?",
        opties=[
            "een beroep op de massa",
            "een persoonlijke aanval",
            "een cirkelredenering",
            "een vals dilemma",
        ],
        antwoord=0,
        uitleg="Dat veel mensen iets doen, bewijst niet dat het goed of veilig is.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een cirkelredenering gebruik je de stelling zelf als argument voor die stelling.",
        antwoord=True,
        uitleg="'Dit boek is goed, want het is een goed boek.' Er komt geen enkel nieuw gegeven bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Of we verbieden alle auto's, of we laten het klimaat stikken.' Welke drogreden?",
        opties=[
            "een vals dilemma",
            "een beroep op de massa",
            "een persoonlijke aanval",
            "een beroep op een autoriteit",
        ],
        antwoord=0,
        uitleg="Er worden twee uitersten voorgesteld alsof er niets tussenin bestaat. In werkelijkheid zijn er veel tussenwegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn drogredenen?",
        opties=[
            "de persoon aanvallen in plaats van zijn argument",
            "twee uitersten voorstellen alsof er niets tussen ligt",
            "de stelling herhalen als argument voor zichzelf",
            "een gevolg afleiden uit een aangetoonde oorzaak",
        ],
        antwoord=[0, 1, 2],
        uitleg="De laatste is een gewone, geldige oorzaak-gevolgredenering, zolang het verband echt aangetoond is.",
    ),
    dict(
        type="waarofniet",
        vraag="Argumenteren op basis van oorzaak en gevolg is per definitie een drogreden.",
        antwoord=False,
        uitleg="Het is een van de geldige soorten argumentatie. Het wordt pas fout als je een verband verzint dat er niet is.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de drogreden waarbij je de mening van je tegenstander verdraait tot iets wat makkelijk te weerleggen is?",
        antwoord=["stroman", "een stroman", "stropop"],
        uitleg="Je bestrijdt dan een pop van stro in plaats van wat je tegenstander werkelijk beweerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Mijn overgrootvader rookte tot zijn vijfennegentigste, dus roken is niet ongezond.' Wat is hier fout?",
        opties=[
            "uit één geval wordt een algemene regel gemaakt",
            "er wordt een deskundige geciteerd die niets weet",
            "de stelling wordt als argument voor zichzelf gebruikt",
            "er worden twee uitersten tegenover elkaar gezet",
        ],
        antwoord=0,
        uitleg="Dat heet een overhaaste veralgemening. Eén uitzondering weegt niet op tegen onderzoek bij duizenden mensen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een argument op basis van een vergelijking werkt alleen als de twee zaken echt vergelijkbaar zijn.",
        antwoord=True,
        uitleg="Een maatregel uit een land met heel andere wetten of afstanden vergelijken met het onze, maakt het argument zwak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is 'een arts zegt het' over gezondheid sterker dan 'een bekende voetballer zegt het'?",
        opties=[
            "omdat de autoriteit dan spreekt binnen zijn eigen vakgebied",
            "omdat een arts meer jaren gestudeerd heeft dan een voetballer",
            "omdat bekende mensen zelden de waarheid vertellen",
            "omdat een voetballer nooit iets over zijn lichaam weet",
        ],
        antwoord=0,
        uitleg="Een autoriteitsargument geldt alleen op het terrein waarop iemand deskundig is. Buiten dat terrein wordt het een drogreden.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Als we dit ene uitzonderingetje toestaan, eindigt het met totale chaos.' Welke drogreden?",
        opties=[
            "een glijdende schaal",
            "een cirkelredenering",
            "een beroep op de massa",
            "een persoonlijke aanval",
        ],
        antwoord=0,
        uitleg="Bij een glijdende schaal doe je alsof één kleine stap onvermijdelijk tot een ramp leidt, zonder dat aan te tonen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe maak je een argument sterker?",
        opties=[
            "je noemt erbij waar je gegeven vandaan komt",
            "je maakt je cijfers controleerbaar",
            "je weerlegt het sterkste tegenargument",
            "je zet je tekst in een groter lettertype",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het lettertype verandert niets aan de redenering. De drie andere maken je argument navolgbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarop let je als je een argumentatieve tekst beoordeelt?",
        opties=[
            "of de argumenten de conclusie echt dragen",
            "of de tekst mooi opgemaakt is",
            "of de schrijver bekend is bij het publiek",
            "of de tekst genoeg alinea's telt",
        ],
        antwoord=0,
        uitleg="Je weegt de redenering: klopt de stap van argument naar conclusie, en zijn de gegevens betrouwbaar?",
    ),
    dict(
        type="meerkeuze",
        vraag="'Sinds de nieuwe burgemeester er is, regent het meer. Hij is dus de oorzaak.' Wat is hier fout?",
        opties=[
            "na elkaar gebeuren is nog geen door elkaar veroorzaakt worden",
            "er wordt een deskundige geciteerd buiten zijn vakgebied",
            "de spreker valt de persoon aan in plaats van het argument",
            "er worden twee uitersten tegenover elkaar geplaatst",
        ],
        antwoord=0,
        uitleg="Volgorde in de tijd is geen bewijs van oorzaak. Daarvoor moet je het verband zelf aantonen.",
    ),
]
