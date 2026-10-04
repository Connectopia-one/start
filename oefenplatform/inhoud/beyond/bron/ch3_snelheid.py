# -*- coding: utf-8 -*-
"""Reactiesnelheid, botsingsmodel en energiediagram — 🌍 Beyond, chemie.

Deel 1 gaat over wat reactiesnelheid is en hoe je ze meet: als verandering van
een concentratie per tijdseenheid of als het aantal effectieve botsingen, met de
concentratie-tijdgrafiek erbij, en over het botsingsmodel met de effectieve en
de elastische botsing en de Boltzmannverdeling. Deel 2 gaat over het
energiediagram met de activeringsenergie, het geactiveerd complex en de
reactie-energie, over de vier factoren die de snelheid beïnvloeden, en over de
snelheidsvergelijking met de orde van een reactie.

Een grafiek staat in een vraag op het scherm niet. Daarom beschrijven de vragen
wat er in zo'n diagram te zien is, en vragen ze wat je eruit afleidt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe druk je de snelheid van een reactie uit?",
        opties=[
            "als de verandering van een concentratie per tijdseenheid",
            "als de hoeveelheid product die in totaal ontstaat",
            "als het aantal mol reagens dat je in de beker doet",
            "als de temperatuur waarbij de reactie op gang komt",
        ],
        antwoord=0,
        uitleg="De eenheid is dus mol per liter per seconde. Je kan ook het aantal "
        "effectieve botsingen per tijdseenheid nemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een effectieve botsing?",
        opties=[
            "een botsing met genoeg energie en de juiste stand om te reageren",
            "een botsing waarbij de deeltjes gewoon van elkaar afketsen",
            "een botsing tussen twee deeltjes van dezelfde soort stof",
            "een botsing die de temperatuur van het mengsel doet stijgen",
        ],
        antwoord=0,
        uitleg="Allebei de voorwaarden moeten kloppen. Een botsing die er niet aan "
        "voldoet, is elastisch: de deeltjes ketsen af en er gebeurt niets.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een botsing waarbij de deeltjes afketsen zonder te reageren?",
        antwoord=["elastisch", "elastische botsing", "niet-effectief"],
        uitleg="Ze heet ook een niet-effectieve botsing. Verreweg de meeste botsingen in "
        "een mengsel zijn van dat soort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden zet je in een concentratie-tijdgrafiek? Kruis alles aan wat juist is.",
        opties=[
            "de tijd op de horizontale as",
            "de concentratie op de verticale as",
            "de snelheid op de verticale as",
            "de temperatuur op de horizontale as",
        ],
        antwoord=[0, 1],
        uitleg="Op de horizontale as komt wat je niet zelf verandert maar laat lopen: de "
        "tijd. De steilheid van de kromme is dan de snelheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Een reactie verloopt in het begin meestal het snelst.",
        antwoord=True,
        uitleg="Dan is de concentratie van de reagentia het hoogst, dus botsen de "
        "deeltjes het vaakst. Naar het einde toe vlakt de kromme af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan je uit de steilheid van een concentratie-tijdgrafiek afleiden?",
        opties=[
            "de snelheid van de reactie op dat ogenblik",
            "de activeringsenergie van de reactie",
            "de totale hoeveelheid product die zal ontstaan",
            "de temperatuur waarbij gemeten is",
        ],
        antwoord=0,
        uitleg="Een steile kromme betekent dat de concentratie snel verandert, en dus een "
        "hoge snelheid. Een vlakke kromme betekent een trage reactie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de Boltzmannverdeling zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze toont hoe de energie over de deeltjes verdeeld is",
            "bij een hogere temperatuur schuift ze naar rechts",
            "ze toont de energie van het geactiveerd complex",
            "ze geldt enkel voor deeltjes in een vaste stof",
        ],
        antwoord=[0, 1],
        uitleg="Niet alle deeltjes hebben dezelfde energie. Bij een hogere temperatuur "
        "komen er meer deeltjes boven de activeringsenergie uit.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je de reactiesnelheid uit?",
        antwoord=["mol/(L·s)", "mol/L/s", "mol/Ls"],
        uitleg="Het is een concentratieverandering per tijd. Daarom staat de mol per "
        "liter in de teller en de seconde in de noemer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom reageert een poeder sneller dan één groot stuk van dezelfde stof?",
        opties=[
            "een poeder heeft een veel groter contactoppervlak",
            "een poeder heeft een hogere temperatuur dan een blok",
            "een poeder heeft een hogere concentratie per gram",
            "een poeder heeft een kleinere activeringsenergie",
        ],
        antwoord=0,
        uitleg="Dat is de verdelingsgraad. Hoe fijner verdeeld, hoe meer deeltjes kunnen "
        "botsen op hetzelfde ogenblik.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factoren maken een reactie sneller? Kruis alles aan wat juist is.",
        opties=[
            "een hogere concentratie van de reagentia",
            "een fijnere verdeling van een vaste stof",
            "een lagere temperatuur van het mengsel",
            "een grotere hoeveelheid oplosmiddel erbij",
        ],
        antwoord=[0, 1],
        uitleg="Meer deeltjes per volume of meer contactoppervlak betekent meer "
        "botsingen. Verdunnen of afkoelen doet het omgekeerde.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een hogere temperatuur botsen de deeltjes alleen vaker, maar niet harder.",
        antwoord=False,
        uitleg="Ze botsen vaker én met meer energie. Dat tweede weegt het zwaarst, want "
        "daardoor raken veel meer botsingen boven de activeringsenergie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom versnelt licht sommige reacties?",
        opties=[
            "het licht levert de energie om een binding te verbreken",
            "het licht verhoogt de concentratie van de reagentia",
            "het licht verkleint het contactoppervlak van de stoffen",
            "het licht werkt als katalysator die zelf verbruikt wordt",
        ],
        antwoord=0,
        uitleg="Daarom staat zuurstofwater in een donkere fles en begint de radicalaire "
        "substitutie van een alkaan onder uv-licht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een katalysator met de snelheid van een reactie?",
        opties=[
            "hij verlaagt de activeringsenergie, zodat meer botsingen effectief zijn",
            "hij verhoogt de temperatuur van het hele reactiemengsel",
            "hij verhoogt de concentratie van de reagentia in de beker",
            "hij verandert de energie die bij de reactie vrijkomt",
        ],
        antwoord=0,
        uitleg="De reactie loopt over een lagere drempel. Het verschil in energie tussen "
        "begin en einde blijft precies hetzelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een katalysator zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "hij wordt tijdens de reactie niet verbruikt",
            "hij verlaagt de activeringsenergie",
            "hij verandert de reactie-energie",
            "hij komt in de reactievergelijking als reagens",
        ],
        antwoord=[0, 1],
        uitleg="Hij doet mee en komt er weer uit. Daarom schrijft men hem boven de pijl "
        "en niet links in de vergelijking.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een katalysator die in een levend organisme werkt?",
        antwoord=["enzym", "biokatalysator", "een enzym"],
        uitleg="Enzymen zijn eiwitten die één reactie veel sneller laten verlopen, bij de "
        "temperatuur van het lichaam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werkt een enzym maar op één soort stof?",
        opties=[
            "de vorm van zijn actieve plaats past op één soort molecule",
            "een enzym kan maar één keer per dag in actie komen",
            "een enzym heeft voor elke stof een andere temperatuur nodig",
            "een enzym bindt enkel moleculen met dezelfde massa",
        ],
        antwoord=0,
        uitleg="Dat heet de specificiteit. Verandert de vorm door hitte of een scheve pH, "
        "dan werkt het enzym niet meer.",
    ),
    dict(
        type="waarofniet",
        vraag="Een katalysator wordt bij de reactie opgebruikt.",
        antwoord=False,
        uitleg="Hij neemt deel en komt daarna onveranderd terug. Daarom kan een kleine "
        "hoeveelheid heel veel reactie op gang brengen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verdubbelt de concentratie van één reagens. Wat verwacht je bij een reactie van eerste orde in die stof?",
        opties=[
            "de snelheid verdubbelt",
            "de snelheid blijft gelijk",
            "de snelheid wordt vier keer groter",
            "de snelheid halveert",
        ],
        antwoord=0,
        uitleg="Bij eerste orde is de snelheid recht evenredig met die concentratie. Bij "
        "tweede orde zou ze vier keer groter worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een reactie kan niet verlopen als de deeltjes elkaar nooit raken.",
        antwoord=True,
        uitleg="Dat is de kern van het botsingsmodel. Daarom roer je, verwarm je of maal "
        "je een stof fijn: om de botsingen te helpen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschijnsel dat een fijn verdeelde stof sneller reageert?",
        antwoord=["verdelingsgraad", "de verdelingsgraad", "verdeling"],
        uitleg="Hoe fijner de verdeling, hoe groter het contactoppervlak. Daarom is "
        "meelstof in een silo zo gevaarlijk.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat stelt de activeringsenergie in een energiediagram voor?",
        opties=[
            "de energie die nodig is om de reactie op gang te brengen",
            "de energie die bij de reactie vrijkomt als warmte",
            "de energie van de reactieproducten samen",
            "het verschil in energie tussen begin en einde",
        ],
        antwoord=0,
        uitleg="Ze is de hoogte van de berg die de deeltjes over moeten. Het verschil "
        "tussen begin en einde is de reactie-energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het geactiveerd complex?",
        opties=[
            "de onstabiele toestand op de top van het energiediagram",
            "het reactieproduct dat als eerste gevormd wordt",
            "de katalysator die tijdelijk aan het reagens bindt",
            "het mengsel van alle reagentia voor de reactie start",
        ],
        antwoord=0,
        uitleg="Op die top zijn de oude bindingen half verbroken en de nieuwe half "
        "gevormd. Het complex bestaat maar heel kort.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een reactie waarbij energie vrijkomt?",
        antwoord=["exotherm", "exo-energetisch", "exothermisch"],
        uitleg="De producten liggen dan lager dan de reagentia. Een endo-energetische "
        "reactie neemt energie op en de producten liggen hoger.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een energiediagram liggen de producten lager dan de reagentia. Wat weet je dan?",
        opties=[
            "de reactie is exo-energetisch en zet energie vrij",
            "de reactie is endo-energetisch en neemt energie op",
            "de reactie heeft een hoge activeringsenergie nodig",
            "de reactie verloopt heel snel bij kamertemperatuur",
        ],
        antwoord=0,
        uitleg="Over de snelheid zegt dat niets: ook een exo-energetische reactie kan een "
        "hoge drempel hebben, zoals het verbranden van hout.",
    ),
    dict(
        type="waarofniet",
        vraag="Een exo-energetische reactie verloopt altijd snel.",
        antwoord=False,
        uitleg="De reactie-energie en de activeringsenergie zijn twee verschillende "
        "dingen. Benzine geeft veel energie, maar heeft toch een vlam nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een endo-energetische reactie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de producten liggen hoger in energie dan de reagentia",
            "de omgeving koelt tijdens de reactie af",
            "de producten liggen lager in energie dan de reagentia",
            "de omgeving warmt tijdens de reactie op",
        ],
        antwoord=[0, 1],
        uitleg="Zo'n reactie haalt haar energie uit de omgeving. Een koudepakje in de "
        "sportzaal werkt op dat principe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bepaal je de reactie-energie uit een energiediagram?",
        opties=[
            "als het verschil in energie tussen producten en reagentia",
            "als de hoogte van de top boven de reagentia",
            "als de hoogte van de top boven de producten",
            "als de som van de energie van alle stoffen samen",
        ],
        antwoord=0,
        uitleg="Is dat verschil negatief, dan komt er energie vrij. De twee hoogtes tot "
        "de top zijn de activeringsenergie van de heen- en de terugreactie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een katalysator in een energiediagram zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de top van de berg komt lager te liggen",
            "het begin- en eindpunt blijven op dezelfde hoogte",
            "het eindpunt komt lager te liggen",
            "de reactie-energie wordt kleiner",
        ],
        antwoord=[0, 1],
        uitleg="Een katalysator verandert de weg, niet de bestemming. Daarom blijft de "
        "reactie-energie precies gelijk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de top van de berg in een energiediagram?",
        antwoord=["geactiveerd complex", "het geactiveerd complex", "geactiveerde complex"],
        uitleg="Daar is de energie het hoogst. De hoogte van die top boven de reagentia "
        "is de activeringsenergie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet de snelheidsvergelijking van een eenstapsreactie A + B → C uit?",
        opties=[
            "v is k maal [A] maal [B]",
            "v is k maal [A] plus [B]",
            "v is k gedeeld door [A] maal [B]",
            "v is k maal [C] gedeeld door [A]",
        ],
        antwoord=0,
        uitleg="Bij een eenstapsreactie zijn de exponenten gelijk aan de coëfficiënten "
        "van de vergelijking. Bij meerdere stappen moet je ze meten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de totale orde van een reactie met snelheidsvergelijking v is k maal [A]² maal [B]?",
        opties=[
            "drie",
            "twee",
            "een",
            "zes",
        ],
        antwoord=0,
        uitleg="Tel de exponenten op: 2 plus 1 is 3. De orde in A is twee en die in B is "
        "een.",
    ),
    dict(
        type="waarofniet",
        vraag="De orde van een reagens in de snelheidsvergelijking volgt bij een meerstapsreactie uit meetresultaten.",
        antwoord=True,
        uitleg="Enkel bij een eenstapsreactie mag je de coëfficiënten gebruiken. Anders "
        "meet je wat er met de snelheid gebeurt als je één concentratie verandert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verdubbelt [A] en de snelheid wordt vier keer groter. Welke orde heeft A?",
        opties=[
            "tweede orde",
            "eerste orde",
            "nulde orde",
            "derde orde",
        ],
        antwoord=0,
        uitleg="Twee tot de macht twee is vier. Bij eerste orde zou de snelheid gewoon "
        "verdubbelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Blijft de snelheid gelijk als je [B] verdubbelt, dan is de reactie van nulde orde in B.",
        antwoord=True,
        uitleg="De exponent van [B] is dan nul, en alles tot de macht nul is één. Zo'n "
        "stof komt niet voor in de snelheidsbepalende stap.",
    ),
    dict(
        type="invultekst",
        vraag="Welke letter staat in de snelheidsvergelijking voor de snelheidsconstante?",
        antwoord=["k", "de k"],
        uitleg="Die constante hangt af van de temperatuur en van de katalysator, niet van "
        "de concentraties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eenheid heeft de snelheidsconstante bij een reactie van eerste orde?",
        opties=[
            "per seconde",
            "mol per liter per seconde",
            "liter per mol per seconde",
            "mol per seconde",
        ],
        antwoord=0,
        uitleg="De eenheid van k volgt uit de vergelijking: links staat mol/(L·s), en "
        "[A] levert al mol/L. Dus blijft er 1/s over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de snelheidsconstante k zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze wordt groter bij een hogere temperatuur",
            "haar eenheid hangt af van de orde van de reactie",
            "ze wordt groter bij een hogere concentratie",
            "haar eenheid is altijd mol per liter per seconde",
        ],
        antwoord=[0, 1],
        uitleg="De concentraties staan al apart in de vergelijking. k zelf hangt af van "
        "de temperatuur, de katalysator en de reactie zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Een katalysator laat de waarde van de snelheidsconstante onveranderd.",
        antwoord=False,
        uitleg="Door de lagere activeringsenergie wordt k juist groter. De orde van de "
        "reactie kan daarbij ook veranderen, want de weg is een andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat voedsel langer goed in de koelkast?",
        opties=[
            "bij een lagere temperatuur verlopen de reacties van bederf trager",
            "bij een lagere temperatuur stoppen alle reacties volledig",
            "bij een lagere temperatuur werkt elk enzym veel sneller",
            "bij een lagere temperatuur is er minder zuurstof aanwezig",
        ],
        antwoord=0,
        uitleg="Minder deeltjes raken boven de activeringsenergie, dus minder effectieve "
        "botsingen. Stoppen doen ze niet, vandaar een houdbaarheidsdatum.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de energie die een botsing minstens moet hebben om te kunnen reageren?",
        antwoord=["activeringsenergie", "de activeringsenergie", "activeringsdrempel"],
        uitleg="Alles eronder geeft een elastische botsing. Een katalysator verlaagt juist "
        "die drempel.",
    ),
]
