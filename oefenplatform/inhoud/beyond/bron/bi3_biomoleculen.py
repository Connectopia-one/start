# -*- coding: utf-8 -*-
"""Biomoleculen: sachariden, lipiden en proteïnen — 🌍 Beyond, biologie.

Deel 1 gaat over de sachariden en de lipiden: de bouwstenen, de indeling, de
bindingen en de manier waarop hun bouw hun functie verklaart. Deel 2 gaat over
de proteïnen, van het aminozuur tot de vier structuurniveaus, en over de
opbouw- en afbraakreacties die voor alle drie de stofklassen gelden.

De fiche vraagt telkens hoe de structuur bijdraagt tot de functie. Daarom
koppelt bijna elke vraag een bouwkenmerk aan een taak in de cel, en staat er
niet alleen een rijtje namen. Structuurformules tekenen kan hier niet, dus
wordt er naar de bouw in woorden gevraagd.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn monosachariden?",
        opties=[
            "glucose, fructose en galactose",
            "lactose, maltose en sacharose",
            "zetmeel, cellulose en glycogeen",
            "glycerol, vetzuur en cholesterol",
        ],
        antwoord=0,
        uitleg="Een monosacharide is één suikerring. Twee ervan samen vormen een "
        "disacharide, veel ervan een polysacharide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit welke twee monosachariden bestaat lactose?",
        opties=[
            "glucose en galactose",
            "glucose en fructose",
            "glucose en glucose",
            "fructose en galactose",
        ],
        antwoord=0,
        uitleg="Lactose is de melksuiker. Sacharose is glucose met fructose, maltose is "
        "twee keer glucose.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de binding tussen twee suikerringen?",
        antwoord=[
            "glycosidische binding",
            "glycosidisch",
            "een glycosidische binding",
        ],
        uitleg="Die binding ontstaat bij een condensatiereactie, waarbij er water "
        "vrijkomt. Bij de hydrolyse wordt er weer water gebruikt om ze te breken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij een condensatiereactie?",
        opties=[
            "twee bouwstenen koppelen en er komt water vrij",
            "een molecule valt uiteen met behulp van water",
            "een molecule neemt zuurstof op uit de lucht",
            "twee bouwstenen wisselen hun atomen uit",
        ],
        antwoord=0,
        uitleg="Opbouwen gebeurt met condensatie, afbreken met hydrolyse. Dat geldt voor "
        "sachariden, lipiden en proteïnen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de reactie waarbij een molecule met behulp van water gesplitst wordt?",
        antwoord=["hydrolyse", "hydrolysereactie", "een hydrolyse"],
        uitleg="Hydro is water, lyse is splitsen. In de darm worden zo zetmeel, vetten en "
        "eiwitten tot hun bouwstenen herleid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke polysachariden slaan energie op? Kruis alles aan wat juist is.",
        opties=[
            "zetmeel bij planten",
            "glycogeen bij dieren",
            "cellulose in de celwand",
            "chitine in een insectenschild",
        ],
        antwoord=[0, 1],
        uitleg="Zetmeel en glycogeen zijn reservestoffen met vertakte ketens, die snel weer "
        "af te breken zijn. Cellulose en chitine geven juist stevigheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is cellulose geschikt als bouwstof van een celwand?",
        opties=[
            "de rechte ketens liggen als kabels naast elkaar",
            "de vertakte ketens zijn snel af te breken",
            "de ringen lossen makkelijk op in water",
            "de ketens zijn kort en heel beweeglijk",
        ],
        antwoord=0,
        uitleg="De rechte ketens vormen met waterstofbruggen stevige vezels. Daardoor houdt "
        "een plantencel haar vorm, ook onder druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan een mens cellulose niet verteren?",
        opties=[
            "hij mist het enzym dat die binding splitst",
            "cellulose is te groot om door te slikken",
            "cellulose lost op in het maagzuur",
            "cellulose bevat geen enkele energie",
        ],
        antwoord=0,
        uitleg="De binding in cellulose is anders gericht dan die in zetmeel. Onverteerd "
        "blijft cellulose als vezel nuttig: ze verkort de transittijd door de darm.",
    ),
    dict(
        type="waarofniet",
        vraag="Zetmeel bestaat uit amylose en amylopectine.",
        antwoord=True,
        uitleg="Amylose is een lange spiraal, amylopectine is sterk vertakt. Samen vormen "
        "ze de zetmeelkorrels in een aardappel of een graankorrel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen snelle en trage suikers?",
        opties=[
            "snelle suikers komen sneller in het bloed",
            "snelle suikers bevatten meer energie per gram",
            "trage suikers bevatten geen glucose",
            "trage suikers worden niet verteerd",
        ],
        antwoord=0,
        uitleg="Een monosacharide hoeft niet meer gesplitst te worden en is er meteen. Een "
        "polysacharide moet eerst afgebroken worden, en dat spreidt de aanvoer.",
    ),
    dict(
        type="waarofniet",
        vraag="Glucose heeft in opgeloste vorm een ring van zes atomen, fructose een van vijf.",
        antwoord=True,
        uitleg="Glucose sluit tot een zesring, fructose tot een vijfring. Daarom reageren "
        "ze niet op dezelfde manier, al hebben ze dezelfde brutoformule.",
    ),
    dict(
        type="invultekst",
        vraag="Uit welke twee soorten bouwstenen bestaat een triglyceride?",
        antwoord=[
            "glycerol en vetzuren",
            "glycerol en vetzuur",
            "vetzuren en glycerol",
        ],
        uitleg="Eén glycerolmolecule draagt drie vetzuren. Bij het vormen van elke binding "
        "komt er een molecule water vrij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor een onverzadigd vetzuur? Kruis alles aan wat juist is.",
        opties=[
            "het heeft één of meer dubbele bindingen",
            "zijn keten heeft daardoor een knik",
            "het bevat geen enkel koolstofatoom",
            "het is bij kamertemperatuur altijd vast",
        ],
        antwoord=[0, 1],
        uitleg="Een dubbele binding geeft een knik in de staart. Daardoor liggen de ketens "
        "losser en is zo'n vet bij kamertemperatuur meestal vloeibaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is olie vloeibaar en boter vast bij kamertemperatuur?",
        opties=[
            "de geknikte ketens van olie stapelen minder goed",
            "olie bevat meer water dan boter",
            "boter bestaat niet uit vetzuren",
            "olie heeft kortere glycerolmoleculen",
        ],
        antwoord=0,
        uitleg="Onverzadigde vetzuren hebben knikken en passen slecht op elkaar. Verzadigde "
        "ketens liggen recht en stapelen tot een vaste massa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke functies hebben lipiden in het lichaam? Kruis alles aan wat juist is.",
        opties=[
            "energie opslaan in vetweefsel",
            "warmte vasthouden als isolatielaag",
            "zuurstof vervoeren in het bloed",
            "het DNA in de kern verpakken",
        ],
        antwoord=[0, 1],
        uitleg="Vet levert per gram ruim dubbel zoveel energie als suiker, isoleert en "
        "beschermt. Zuurstof vervoeren doet hemoglobine, een proteïne.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een fosfolipide geschikt om een membraan te vormen?",
        opties=[
            "de kop is hydrofiel en de staarten zijn hydrofoob",
            "de hele molecule stoot water af",
            "de hele molecule trekt water aan",
            "ze bevat geen vetzuren maar wel suikers",
        ],
        antwoord=0,
        uitleg="In water keren de staarten zich naar elkaar toe en de koppen naar buiten. "
        "Zo vormt zich vanzelf een dubbellaag.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een molecule die water afstoot?",
        antwoord=["hydrofoob", "apolair", "hydrofobe"],
        uitleg="Hydrofoob betekent watervrezend en gaat samen met apolair. Hydrofiel of "
        "polair is het omgekeerde.",
    ),
    dict(
        type="waarofniet",
        vraag="Cholesterol is een sacharide en komt vooral in de celwand van planten voor.",
        antwoord=False,
        uitleg="Cholesterol is een steroïde, dus een lipide, en zit in het celmembraan van "
        "dierlijke cellen. Het houdt dat membraan soepel en is de grondstof voor onder meer "
        "de geslachtshormonen.",
    ),
    dict(
        type="waarofniet",
        vraag="Vitaminen die in vet oplossen, kunnen in het lichaam niet opgeslagen worden.",
        antwoord=False,
        uitleg="Juist die vitaminen, zoals A, D, E en K, worden in het vetweefsel en in de "
        "lever bewaard. Daardoor kan er ook te veel van opstapelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom levert vet per gram meer energie dan suiker?",
        opties=[
            "de ketens zijn sterker gereduceerd, met meer waterstof",
            "vet bevat meer zuurstof dan suiker",
            "vet lost beter op in het bloed",
            "vet wordt sneller afgebroken dan suiker",
        ],
        antwoord=0,
        uitleg="Bij de verbranding leveren de koolstof-waterstofbindingen de energie. Een "
        "vetzuurketen heeft er per gram meer dan een suikerring.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke groepen heeft elk aminozuur gemeenschappelijk?",
        opties=[
            "een aminogroep en een carboxylgroep",
            "een hydroxylgroep en een fosfaatgroep",
            "twee aminogroepen naast elkaar",
            "een suikerring en een stikstofbase",
        ],
        antwoord=0,
        uitleg="Alle aminozuren hebben dezelfde kern. Alleen hun restgroep verschilt, en "
        "die bepaalt hun eigenschappen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk deel van een aminozuur verschilt van aminozuur tot aminozuur?",
        antwoord=["restgroep", "de restgroep", "zijgroep"],
        uitleg="Een polaire restgroep trekt water aan, een apolaire stoot het af, en een "
        "ioniserende draagt een lading. Dat stuurt de plooiing van het hele eiwit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet de binding tussen twee aminozuren?",
        opties=[
            "een peptidebinding",
            "een glycosidische binding",
            "een waterstofbrug",
            "een disulfidebinding",
        ],
        antwoord=0,
        uitleg="Die binding ontstaat bij een condensatiereactie tussen de carboxylgroep van "
        "het ene en de aminogroep van het andere aminozuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de primaire structuur van een eiwit?",
        opties=[
            "de volgorde van de aminozuren",
            "de spiraal van de keten",
            "de ruimtelijke vorm van het geheel",
            "het aantal subeenheden samen",
        ],
        antwoord=0,
        uitleg="De primaire structuur volgt rechtstreeks uit het gen. Alle verdere "
        "plooiing komt uit die volgorde voort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen horen bij de secundaire structuur? Kruis alles aan wat juist is.",
        opties=[
            "de α-helix",
            "de ß-plaat",
            "de keten van subeenheden",
            "de volgorde van de aminozuren",
        ],
        antwoord=[0, 1],
        uitleg="De helix en de plaat worden door waterstofbruggen vastgehouden. Ze ontstaan "
        "tussen delen van dezelfde keten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bindingen houden de tertiaire structuur vast? Kruis alles aan wat juist is.",
        opties=[
            "disulfidebindingen tussen restgroepen",
            "ionbindingen tussen geladen restgroepen",
            "peptidebindingen tussen de aminozuren",
            "glycosidische bindingen tussen suikerringen",
        ],
        antwoord=[0, 1],
        uitleg="Peptidebindingen vormen de keten zelf en horen bij de primaire structuur. "
        "De plooiing in de ruimte komt van zwakkere bindingen tussen de restgroepen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de structuur van een eiwit dat uit meerdere ketens bestaat?",
        antwoord=[
            "quaternaire structuur",
            "quaternair",
            "de quaternaire structuur",
        ],
        uitleg="Hemoglobine heeft vier subeenheden en dus een quaternaire structuur. Niet "
        "elk eiwit heeft dat niveau.",
    ),
    dict(
        type="waarofniet",
        vraag="Een eiwit dat door verhitting zijn vorm verliest, is gedenatureerd.",
        antwoord=True,
        uitleg="De zwakke bindingen breken en de keten rolt open. Het wit van een gebakken "
        "ei wordt daardoor niet meer doorzichtig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werkt een gedenatureerd enzym niet meer?",
        opties=[
            "het actief centrum heeft zijn vorm verloren",
            "de aminozuren zijn uit de keten verdwenen",
            "de peptidebindingen zijn allemaal verbroken",
            "het enzym is in suiker omgezet",
        ],
        antwoord=0,
        uitleg="De volgorde van de aminozuren blijft dezelfde, maar de ruimtelijke vorm "
        "niet. Zonder die vorm past het substraat er niet meer in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eiwitten zorgen voor de samentrekking van een spier?",
        opties=[
            "actine en myosine",
            "keratine en collageen",
            "hemoglobine en aquaporine",
            "insuline en amylase",
        ],
        antwoord=0,
        uitleg="De twee soorten draden schuiven langs elkaar. Daardoor wordt de spier "
        "korter en dikker.",
    ),
    dict(
        type="waarofniet",
        vraag="Collageen is het eiwit dat haren en nagels hun hardheid geeft.",
        antwoord=False,
        uitleg="Dat is keratine, dat vol disulfidebindingen zit en daardoor hard en "
        "onoplosbaar is. Collageen geeft stevigheid aan huid, pezen en bot.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het kanaaleiwit dat water door het celmembraan laat?",
        antwoord=["aquaporine", "aquaporines", "een aquaporine"],
        uitleg="Het is een kanaaleiwit dat precies op water past. Daardoor gaat water veel "
        "sneller door het membraan dan louter door diffusie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke functies vervullen proteïnen in een cel? Kruis alles aan wat juist is.",
        opties=[
            "reacties versnellen als enzym",
            "ziekteverwekkers herkennen als antilichaam",
            "het membraan als dubbellaag vormen",
            "op lange termijn energie opslaan",
        ],
        antwoord=[0, 1],
        uitleg="Enzymen, antilichamen, transporteiwitten, transcriptiefactoren en "
        "steunweefsel zijn alle proteïnen. Het membraan en de energiereserve zijn werk van "
        "lipiden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een transcriptiefactor is een proteïne die de genexpressie mee stuurt.",
        antwoord=True,
        uitleg="Hij bindt op het DNA bij de promotor. Zo beslist een eiwit mee welke genen "
        "gelezen worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bepaalt de volgorde van de aminozuren de werking van een eiwit?",
        opties=[
            "de restgroepen sturen de plooiing en dus de vorm",
            "de volgorde bepaalt hoeveel water het eiwit bevat",
            "de volgorde bepaalt in welk orgaan het eiwit zit",
            "de volgorde bepaalt hoeveel energie het levert",
        ],
        antwoord=0,
        uitleg="Polaire en apolaire restgroepen zoeken elk hun plaats ten opzichte van "
        "water. Daaruit volgt de driedimensionale vorm, en die vorm doet het werk.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén veranderd aminozuur kan de werking van een heel eiwit bederven.",
        antwoord=False,
        uitleg="Dat kan, maar het hoeft niet. Zit de verandering in het actief centrum of "
        "raakt ze de plooiing, dan is het erg; elders verandert er vaak niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe worden proteïnen in de darm afgebroken?",
        opties=[
            "met hydrolyse tot losse aminozuren",
            "met condensatie tot langere ketens",
            "met verhitting tot vetzuren",
            "met vergisting tot melkzuur",
        ],
        antwoord=0,
        uitleg="Water splitst de peptidebindingen, en enzymen versnellen dat. De vrije "
        "aminozuren gaan daarna door de darmwand het bloed in.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een keten van heel veel aminozuren?",
        antwoord=["polypeptide", "een polypeptide", "polypeptideketen"],
        uitleg="Twee aminozuren vormen een dipeptide, drie een tripeptide. Vanaf een lange "
        "keten spreekt men van een polypeptide, en geplooid van een proteïne.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uiteinden heeft een polypeptideketen?",
        opties=[
            "een N-terminus en een C-terminus",
            "een 5'- en een 3'-einde",
            "twee carboxylgroepen",
            "een kop en een staart van vetzuren",
        ],
        antwoord=0,
        uitleg="Aan de ene kant blijft een vrije aminogroep over, aan de andere een vrije "
        "carboxylgroep. Het ribosoom bouwt van de N- naar de C-terminus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben polysachariden, lipiden en proteïnen gemeenschappelijk?",
        opties=[
            "ze worden met condensatie gevormd en met hydrolyse gesplitst",
            "ze bestaan alle drie uit aminozuren",
            "ze lossen alle drie goed op in water",
            "ze dienen alle drie enkel als energievoorraad",
        ],
        antwoord=0,
        uitleg="Opbouwen geeft telkens water af, afbreken verbruikt telkens water. Daarin "
        "lijken de drie stofklassen volledig op elkaar.",
    ),
]
