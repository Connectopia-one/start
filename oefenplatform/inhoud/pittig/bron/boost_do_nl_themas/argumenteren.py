"""Argumenteren: stelling, argumentsoort en drogreden — pittig (🚀 Boost doorstroom, Nederlands).

Eigen teksten en vragen strikt binnen nl_argumenteren. De eerste vragen (tot
en met BASIS) gaan enkel over feit, mening, stelling, standpunt, argument,
tegenargument en conclusie; die gebruikt ook Boost dubbele finaliteit."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik

BETOOG = ("Lees de tekst.\n\n"
          "Geef ons een fietsenstalling!\n\n"
          "Onze school moet een overdekte fietsenstalling krijgen. Nu staan meer dan tweehonderd fietsen elke dag in de regen. "
          "Natte zadels en roestige kettingen zijn het gevolg. Bovendien kiezen leerlingen vaker de auto van hun ouders als het regent, en dat zorgt voor files aan de schoolpoort. "
          "Sommigen zeggen dat zo'n stalling te duur is. Maar de stad geeft dit jaar subsidies voor fietsvoorzieningen, waardoor de school maar een klein deel zelf betaalt. "
          "Een overdekte stalling is dus een slimme keuze.")

BASIS = [
    sorteer("Feit of mening?", ["feit", "mening"],
            [("De nieuwe sporthal telt drie zalen.", "feit"), ("Die sporthal is veel te klein.", "mening"), ("De film duurde twee uur.", "feit"), ("Die film is saai.", "mening"), ("Volgens mij moet de bib langer open.", "mening"), ("De bib sluit om 18 uur.", "feit")],
            "Een feit kan je nagaan, een mening niet."),
    casus(BETOOG, [
        inv("Hoe noem je de zin 'Onze school moet een overdekte fietsenstalling krijgen'? Eén woord.", ["stelling", "de stelling"], "De bewering waarover de discussie gaat."),
        tabel("Wat is de rol van deze zin in het betoog?",
              [("Nu staan meer dan tweehonderd fietsen elke dag in de regen.", "argument"), ("Sommigen zeggen dat zo'n stalling te duur is.", "tegenargument"), ("Een overdekte stalling is dus een slimme keuze.", "conclusie")],
              "Het tegenargument wordt daarna weerlegd.", ["argument", "tegenargument", "conclusie"]),
        mk("Hoe weerlegt de schrijver het tegenargument?",
           ["met de subsidie van de stad", "door het tegenargument te verzwijgen", "door de tegenstanders uit te lachen", "met het aantal fietsen op school"],
           0, "Hij noemt het tegenargument eerlijk en zet er een reden tegenover."),
        keuze("Het signaalwoord dat de conclusie aankondigt, is [[*dus|bovendien|maar]].", "'Dus' kondigt het besluit aan."),
    ]),
    mk("Stelling: 'Gsm's horen niet thuis in de klas.' Welke zin is een standpunt?",
       ["Daar ben ik het helemaal mee eens.", "Bijna elke leerling heeft een gsm.", "Gsm's bestaan al meer dan dertig jaar.", "Sommige scholen hebben er een regel over."],
       0, "Een standpunt is de kant die je kiest."),
    tabel("Kan deze zin dienen als stelling voor een debat?",
          [("Schooluniformen moeten verplicht worden.", J), ("België heeft tien provincies.", F), ("Fastfood moet duurder worden.", J), ("Water kookt op honderd graden.", F)],
          "Een goede stelling is discutabel."),
    tabel("Klopt dit over feiten, meningen en betogen?",
          [("Een mening wordt een feit als veel mensen het ermee eens zijn.", F), ("Een goed betoog noemt ook tegenargumenten.", J), ("De conclusie mag meer beweren dan de argumenten dragen.", F)],
          "Dat veel mensen iets vinden, is zelf wel een feit, maar maakt de mening geen feit."),
    sorteer("Verraadt dit woord of deze woordgroep een mening?", ["mening", "gegeven"],
            [("prachtig", "mening"), ("in 2024", "gegeven"), ("het is onaanvaardbaar dat", "mening"), ("zou moeten", "mening"), ("vijf kilometer", "gegeven")],
            "Waardewoorden en wensen verraden een oordeel."),
    keuze("Aan waardewoorden zoals 'schitterend' of 'belachelijk' merk je dat de schrijver [[*subjectief|objectief|neutraal]] wordt.", "Ook uitroeptekens verraden een oordeel."),
]

VRAGEN = BASIS + [
    sorteer("Welke soort argumentatie is dit?", ["vergelijking", "oorzaak en gevolg", "cijfers", "wetenschappelijk onderzoek"],
            [("In Denemarken werkt dit al jaren, dus het kan hier ook.", "vergelijking"), ("Als de bus vaker rijdt, komen minder leerlingen te laat.", "oorzaak en gevolg"), ("Zeven op de tien jongeren sport te weinig.", "cijfers"), ("Een studie van de universiteit toont dat lezen het geheugen helpt.", "wetenschappelijk onderzoek")],
            "Naast deze soorten bestaat ook het beroep op een deskundige."),
    sorteer("Welke drogreden is dit?", ["persoonlijke aanval", "beroep op de massa", "vals dilemma", "glijdende schaal"],
            [("Jij rijdt zelf met de auto, dus over het klimaat moet jij zwijgen.", "persoonlijke aanval"), ("Iedereen doet het, dus het kan geen kwaad.", "beroep op de massa"), ("Of we schaffen alle toetsen af, of leerlingen blijven gestrest.", "vals dilemma"), ("Als we nu een kwartier later beginnen, beginnen we straks om de middag.", "glijdende schaal")],
            "Drogredenen klinken overtuigend maar deugen niet."),
    sorteer("Cirkelredenering, stroman of overhaaste veralgemening?", ["cirkelredenering", "stroman", "overhaaste veralgemening"],
            [("Deze app is de beste, want er is geen betere app.", "cirkelredenering"), ("Jij wil minder huiswerk? Dus jij vindt dat leerlingen niets moeten leren!", "stroman"), ("Mijn buurman is ziek geworden van dat vaccin, dus het is gevaarlijk.", "overhaaste veralgemening")],
            "Bij een stroman verdraai je de mening van de ander."),
    mk("'Een bekende voetballer zegt dat dit vitaminepil helpt tegen griep.' Waarom is dat een zwak argument?",
       ["hij spreekt buiten zijn vakgebied", "een voetballer mag geen mening hebben", "argumenten met namen zijn altijd fout", "er staan geen cijfers bij zijn uitspraak"],
       0, "Een autoriteitsargument geldt alleen binnen iemands vakgebied."),
    mk("'Sinds we een nieuwe trainer hebben, regent het tijdens elke match. Hij brengt ongeluk.' Wat is hier fout?",
       ["na elkaar is nog niet door elkaar", "de trainer wordt persoonlijk aangevallen", "er wordt een vergelijking gemaakt", "het argument steunt op cijfers"],
       0, "Volgorde in de tijd is geen bewijs van oorzaak."),
    mk("Waarom is een vergelijking met een land met heel andere wetten een zwak argument?",
       ["de twee zaken zijn niet vergelijkbaar", "vergelijkingen zijn altijd drogredenen", "landen mag je nooit met elkaar vergelijken", "er staat geen deskundige bij het argument"],
       0, "Een vergelijking werkt alleen als de twee zaken echt vergelijkbaar zijn."),
    tabel("Klopt dit over argumentatie?",
          [("Een beroep op een autoriteit is altijd een drogreden.", F), ("Oorzaak en gevolg is een geldige soort argumentatie.", J), ("Een argument telt pas mee als er cijfers bij staan.", F), ("Een cirkelredenering voegt geen nieuw gegeven toe.", J)],
          "Een arts over gezondheid is een geldig autoriteitsargument."),
    tabel("Maakt dit een argument sterker?",
          [("je bron noemen", J), ("je cijfers controleerbaar maken", J), ("het argument drie keer herhalen", F), ("een groter lettertype", F)],
          "Herhaling en lettertype veranderen niets aan de redenering."),
    casus("Lees de tekst.\n\n'De school moet de frisdrankautomaat weghalen. Uit cijfers van de gezondheidsdienst blijkt dat één op de vijf jongeren te zwaar is. Wie dat niet wil, wil blijkbaar dat al onze leerlingen ziek worden. En iedereen weet toch dat frisdrank slecht is.'", [
        keuze("Het argument over één op de vijf jongeren steunt op [[*cijfers|een vergelijking|een persoonlijke aanval]].", "Cijfers, met de bron erbij."),
        keuze("'Wie dat niet wil, wil blijkbaar dat al onze leerlingen ziek worden' is een [[*stroman|cirkelredenering|vergelijking]].", "De mening van de tegenstander wordt verdraaid."),
        keuze("'Iedereen weet toch dat ...' is een [[*beroep op de massa|beroep op een deskundige|oorzaak-gevolgredenering]].", "Dat veel mensen iets denken, bewijst niets."),
    ]),
    inv("Hoe noem je een redenering die overtuigend klinkt maar niet deugt? Eén woord.", ["drogreden", "een drogreden", "drogredenering"], "Een drogreden."),
    keuze("'Dit boek is goed, want het is een goed boek' is een [[*cirkelredenering|vals dilemma|glijdende schaal]].", "De stelling dient als argument voor zichzelf."),
    keuze("'Mijn opa rookte tot zijn negentigste, dus roken is niet ongezond' maakt uit één geval een [[*algemene regel|vergelijking|tegenargument]].", "Dat heet een overhaaste veralgemening."),
    mk("Waarop let je vooral als je een argumentatieve tekst beoordeelt?",
       ["of de argumenten de conclusie dragen", "hoeveel alinea's de tekst telt", "of de schrijver bekend is bij jongeren", "of er een mooie foto bij de tekst staat"],
       0, "Klopt de stap van argument naar conclusie, en zijn de gegevens betrouwbaar?"),
    tabel("Is dit een geldige soort argumentatie of een drogreden?",
          [("een arts die iets zegt over gezondheid", "geldig"), ("een zanger die iets zegt over medicijnen", "drogreden"), ("een gevolg afleiden uit een aangetoonde oorzaak", "geldig"), ("twee uitersten voorstellen alsof er niets tussen ligt", "drogreden")],
          "Een autoriteit telt enkel binnen zijn vakgebied.", ["geldig", "drogreden"]),
    keuze("Bij een glijdende schaal doe je alsof één kleine stap onvermijdelijk leidt tot [[*een ramp|een compromis|een feit]].", "Zonder dat aan te tonen."),
    mk("Waarom houd je feiten en meningen uit elkaar als je iemand wil overtuigen?",
       ["je lezer weet dan wat hij kan nagaan", "meningen mogen niet in een betoog staan", "feiten maken een tekst altijd korter", "anders telt je tekst geen conclusie"],
       0, "Een mening die als feit gepresenteerd wordt, voelt oneerlijk aan."),
    inv("Hoe noem je een reden die tégen de stelling pleit? Eén woord.", ["tegenargument", "een tegenargument"], "Een tegenargument."),
    open_("Bedenk een sterk argument en een tegenargument bij de stelling 'De schooldag moet later beginnen.' Weerleg daarna het tegenargument.",
          "Argument: jongeren slapen vaak te weinig en leren beter als ze uitgerust zijn. Tegenargument: dan eindigt de school later en blijft er minder tijd over voor hobby's. Weerlegging: wie uitgerust is, werkt sneller, zodat er minder huiswerk overblijft."),
]
