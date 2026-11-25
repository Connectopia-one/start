"""De volwassene en de oudere — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_volwassenen: uiterlijke en inwendige veroudering, primair en
secundair verouderen, wat toeneemt en afneemt in de hersenen,
ouderdomsvergeetachtigheid en dementie, en de levensgebeurtenissen van
volwassenen en ouderen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik

STRAAT = ("Lees de situatie.\n\n"
          "Opa Jef (78) vindt soms de naam van een buur niet meteen, maar die schiet hem later te binnen. Hij kookt nog zelf en doet zijn eigen boodschappen. "
          "Zijn buurvrouw Maria (80) vergeet de laatste maanden waar ze woont, laat het gas aan en herkent haar kleinkinderen niet altijd.")

HILDE = ("Lees de situatie.\n\n"
         "Hilde (52) heeft twee tieners thuis en gaat elke avond langs bij haar vader, die sinds een val hulp nodig heeft bij het wassen. "
         "Ze slaapt slecht en heeft vaak hoofdpijn. Haar oudste zoon is na zijn studies net weer thuis komen wonen.")

VRAGEN = [
    sorteer("Uiterlijke of inwendige veroudering?", ["uiterlijk", "inwendig"],
            [("rimpels", "uiterlijk"), ("de nieren werken minder goed", "inwendig"), ("grijze haren", "uiterlijk"), ("de longen nemen minder zuurstof op", "inwendig"), ("een krommere rug", "uiterlijk"), ("een tragere spijsvertering", "inwendig")],
            "Uiterlijke veroudering zie je, inwendige veroudering zit in de organen."),
    sorteer("Primair of secundair verouderen?", ["primair", "secundair"],
            [("grijze haren krijgen", "primair"), ("longschade door jarenlang roken", "secundair"), ("trager reageren met de jaren", "primair"), ("een huid vol zonneschade na veel zonnebanken", "secundair"), ("minder spierkracht door het ouder worden", "primair"), ("overgewicht door weinig te bewegen", "secundair")],
            "Primair overkomt iedereen; secundair hangt samen met leefstijl, ziekte en omgeving."),
    casus(STRAAT, [
        tabel("Wat past het best?",
              [("opa Jef", "ouderdomsvergeetachtigheid"), ("buurvrouw Maria", "mogelijk dementie"), ("een studente die na een drukke dag haar sleutels kwijt is", "geen van beide")],
              "Vergeetachtigheid hindert het dagelijkse leven niet, dementie wel.", ["ouderdomsvergeetachtigheid", "mogelijk dementie", "geen van beide"]),
        mk("Wat is het belangrijkste verschil tussen Jef en Maria?",
           ["bij Maria lukt het dagelijkse leven niet meer", "Maria is twee jaar ouder dan Jef", "Jef heeft meer vrienden dan Maria in de straat", "bij Jef gaat het geheugen sneller achteruit dan bij Maria"],
           0, "Bij dementie gaan de hersenen blijvend achteruit en gaat het dagelijkse leven eraan."),
        keuze("Jef denkt misschien trager, maar heeft wel [[*meer overzicht en levenservaring|een snellere reactietijd|een hoger rekentempo]].", "Wat aan tempo verloren gaat, vangt ervaring op."),
    ]),
    tabel("Neemt dit toe of af bij het ouder worden?",
          [("woordenschat", "neemt toe"), ("reactiesnelheid", "neemt af"), ("levenswijsheid", "neemt toe"), ("rekensnelheid", "neemt af"), ("overzicht", "neemt toe")],
          "Ouder worden is niet alleen achteruitgang.", ["neemt toe", "neemt af"]),
    koppel("Koppel de levensgebeurtenis aan de uitleg.",
           [("boemerangkinderen", "ze komen na het uithuizen terug wonen"), ("legenestsyndroom", "het gemis als de kinderen vertrokken zijn"), ("sandwichgeneratie", "zorgen voor je kinderen en je ouders tegelijk"), ("midlifecrisis", "twijfel aan werk en keuzes rond de middenleeftijd")],
           ["de babytijd"],
           "Vier levensgebeurtenissen van de volwassene."),
    tabel("Hoort deze levensgebeurtenis vooral bij de volwassene of bij de oudere?",
          [("gezinsvorming", "volwassene"), ("pensionering", "oudere"), ("een midlifecrisis", "volwassene"), ("het verlies van een partner", "oudere"), ("kleinkinderen krijgen", "oudere")],
          "Gezinsvorming en een midlifecrisis horen bij de volwassene.", ["volwassene", "oudere"]),
    casus(HILDE, [
        keuze("Hilde hoort bij de [[*sandwichgeneratie|peergroep|boemerangkinderen]].", "Ze zit tussen twee generaties die zorg vragen."),
        mk("Hoe noem je de oudste zoon van Hilde?",
           ["een boemerangkind", "een mantelzorger", "een gepensioneerde", "een sandwichkind"],
           0, "Hij was het huis uit en komt terug."),
        keuze("Haar slechte slaap en hoofdpijn kunnen komen door [[*langdurige stress|haar pensionering|het legenestsyndroom]].", "Langdurige stress maakt ziek."),
        keuze("Hilde heeft het extra zwaar omdat ze voor [[*twee generaties|één baby|haar collega's]] zorgt.", "Haar kinderen en haar vader."),
    ]),
    tabel("Helpt dit een oudere die naar een woonzorgcentrum verhuist?",
          [("zijn eigen foto's en zetel meenemen", J), ("zelf mee kiezen welke kamer hij krijgt", J), ("al zijn spullen achterlaten", F), ("meteen al zijn gewoonten omgooien", F), ("bezoek krijgen van familie", J)],
          "Eigen spullen, mee beslissen en bezoek maken de stap draaglijker."),
    mk("Een pas gepensioneerde man voelt zich verloren. Waarom vooral?",
       ["het vaste ritme van zijn werk valt weg", "hij heeft plots veel te veel geld om uit te geven", "hij krijgt meteen dementie", "hij moet nu elke dag werken"],
       0, "De dagindeling moet opnieuw opgebouwd worden."),
    keuze("Iemand die rond zijn vijfenveertigste zijn werk en zijn keuzes in vraag stelt, zit in een [[*midlifecrisis|groeispurt|legenestsyndroom]].", "Twijfel rond de middenleeftijd."),
    inv("Hoe noem je het verwerken van een verlies? Eén woord.", ["rouw", "rouwen", "het rouwen"], "Rouw."),
    tabel("Klopt dit over rouw en eenzaamheid?",
          [("Rouw verloopt bij iedereen anders.", J), ("Een oudere kan eenzaam worden doordat vrienden wegvallen.", J), ("Rouwen duurt altijd precies één jaar.", F), ("Eenzaamheid komt bij ouderen bijna nooit voor.", F)],
          "Rouwen is heel persoonlijk, in tempo en in vorm."),
    keuze("Verouderen begint al in de [[*vroege volwassenheid|late volwassenheid|kleutertijd]].", "Je merkt er dan alleen nog weinig van."),
    mk("Welke verandering in de motoriek hoort bij een oudere?",
       ["een minder zeker evenwicht", "een grijpreflex die terugkomt", "een snellere reactietijd", "een plotse groeispurt"],
       0, "Trager bewegen, minder kracht en een minder zeker evenwicht."),
    sleep("Het verouderen dat bij iedereen gebeurt, heet [[primair]] verouderen. Het verouderen door leefstijl, ziekte en omgeving heet [[secundair]] verouderen. Dat laatste kan je deels [[vermijden]].",
          ["inwendig", "versnellen"],
          "Wie gezond leeft, beperkt het secundaire verouderen."),
    keuze("Wie stopt met roken, beperkt vooral het [[*secundair|primair]] verouderen.", "Roken hoort bij de leefstijl."),
    mk("Een vrouw van 58 is verdrietig omdat haar jongste dochter net op kot is vertrokken en het huis stil is. Wat is dat?",
       ["het legenestsyndroom", "een midlifecrisis", "dementie", "de sandwichgeneratie van haar familie"],
       0, "Het gemis en de leegte als de kinderen het huis uit zijn."),
    tabel("Ouderdomsvergeetachtigheid of dementie?",
          [("je weet even een woord niet", "vergeetachtigheid"), ("je verdwaalt in je eigen straat", "dementie"), ("je vergeet een afspraak en herinnert het je later", "vergeetachtigheid"), ("je kan je niet meer zelf aankleden", "dementie")],
          "Kijk of het dagelijkse leven nog lukt.", ["vergeetachtigheid", "dementie"]),
    keuze("Bij dementie gaan de hersenen [[*blijvend|tijdelijk|helemaal niet]] achteruit.", "Het is een ziekte, geen gewone vergeetachtigheid."),
    mk("Welke lichamelijke verandering hoort bij een volwassene van vijftig?",
       ["zijn zicht en gehoor gaan traag achteruit", "hij wordt nog elk jaar een paar centimeter langer", "zijn babyreflexen komen terug", "zijn spierkracht neemt elk jaar sterk toe"],
       0, "Groeien in de lengte is gestopt; de rest gaat traag achteruit."),
    inv("Hoe noem je het moment waarop iemand door zijn leeftijd stopt met werken? Eén woord.", ["pensionering", "pensioen", "het pensioen", "de pensionering"], "De pensionering."),
    keuze("Samenwonen, trouwen of kinderen krijgen noem je [[*gezinsvorming|pensionering|stagnatie]].", "Een eigen gezin beginnen."),
    keuze("Een oudere die niet meer zelf kan koken en hulp nodig heeft, wordt [[*afhankelijk|onafhankelijk|jonger]].", "Hij heeft anderen nodig voor dagelijkse dingen."),
    mk("Waarom wordt de wereld van een oudere soms kleiner?",
       ["vrienden, collega's en een partner vallen weg", "hij leert elke dag heel veel nieuwe mensen kennen in de buurt", "zijn huis wordt letterlijk kleiner", "hij heeft geen woordenschat meer"],
       0, "Daardoor kan eenzaamheid ontstaan."),
    open_("Je werkt in een woonzorgcentrum. Een nieuwe bewoner is net verhuisd en zit stil op zijn kamer. Geef twee dingen die je kan doen om hem te helpen wennen.",
          "Ik vraag hem welke spullen van thuis hij nog graag op zijn kamer wil, zoals foto's. En ik laat hem mee beslissen over zijn dagindeling, bijvoorbeeld wanneer hij wil eten of wandelen."),
]
