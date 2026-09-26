# -*- coding: utf-8 -*-
"""De vragen voor "Cellen, weefsels en organen" (✨ Spark, natuurwetenschappen).

Uit de vakfiche, deel biologie, "Samenhang organisatieniveaus": de leerling
herkent en benoemt de organisatieniveaus in een plantaardig en een dierlijk
organisme, rangschikt ze volgens toenemende of afnemende complexiteit, benoemt
weefsels, organen en orgaanstelsels, benoemt de celonderdelen en legt hun
functie uit, en legt de verschillen en gelijkenissen tussen een plantaardige
en een dierlijke cel uit.

Deel 1 blijft bij herkennen en benoemen. Deel 2 vraagt vergelijken, ordenen en
uitleggen waarom: waarom een wortelcel geen bladgroenkorrels heeft, waarom een
spiercel veel mitochondriën heeft, wat er ontbreekt als een niveau wegvalt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waaruit is elk levend wezen opgebouwd?",
        opties=["Uit cellen", "Uit atomen alleen", "Uit organen alleen"],
        antwoord=0,
        uitleg="De cel is de basiseenheid van het leven. Alles wat leeft, van een bacterie tot een olifant, is uit cellen opgebouwd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zet van klein naar groot: cel, orgaan, stelsel, weefsel. Welke rij klopt?",
        opties=[
            "cel – weefsel – orgaan – stelsel",
            "cel – orgaan – weefsel – stelsel",
            "weefsel – cel – orgaan – stelsel",
        ],
        antwoord=0,
        uitleg="De organisatieniveaus gaan van eenvoudig naar ingewikkeld: celonderdelen, cellen, weefsels, organen, stelsels en ten slotte het hele organisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een weefsel?",
        opties=[
            "Een groep cellen van dezelfde soort die samen één taak doen",
            "Eén cel met een heel bijzondere vorm",
            "Een groep organen die samenwerken",
        ],
        antwoord=0,
        uitleg="Cellen van dezelfde soort die samen dezelfde taak uitvoeren, vormen een weefsel. Verschillende weefsels samen vormen een orgaan.",
    ),
    dict(
        type="invultekst",
        vraag="Verschillende organen die samen één grote taak doen, vormen samen een ___.",
        antwoord=["stelsel", "orgaanstelsel"],
        uitleg="Mond, slokdarm, maag en darmen vormen samen het spijsverteringsstelsel. Een stelsel heet ook een orgaanstelsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk celonderdeel zit de erfelijke informatie van de cel?",
        opties=["In de celkern", "In het cytoplasma", "In de vacuole"],
        antwoord=0,
        uitleg="De celkern bevat het erfelijk materiaal en stuurt van daaruit alles wat in de cel gebeurt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke celonderdelen vind je in een plantaardige cel, maar niet in een dierlijke cel?",
        opties=[
            "De celwand",
            "De bladgroenkorrels",
            "De celkern",
            "Het celmembraan",
        ],
        antwoord=[0, 1],
        uitleg="Een plantaardige cel heeft een stevige celwand en meestal bladgroenkorrels en een grote vacuole. De celkern en het celmembraan heeft elke cel, ook een dierlijke.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet het celmembraan?",
        opties=[
            "Het regelt wat er in en uit de cel gaat",
            "Het maakt suikers met zonlicht",
            "Het bewaart de erfelijke informatie",
        ],
        antwoord=0,
        uitleg="Het celmembraan is het dunne vlies rond de cel. Het laat sommige stoffen door en andere niet, en regelt zo de uitwisseling met de omgeving.",
    ),
    dict(
        type="invultekst",
        vraag="In het celonderdeel ___ gebeurt de celademhaling, waarbij de cel energie vrijmaakt.",
        antwoord=["mitochondrion", "mitochondriën", "mitochondrie"],
        uitleg="In de mitochondriën wordt glucose verbrand met zuurstof. Ze worden daarom de energiecentrales van de cel genoemd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een vacuole in een plantencel?",
        opties=[
            "Ze slaat water en voedingsstoffen op",
            "Ze vangt het zonlicht op",
            "Ze deelt de cel in tweeën",
        ],
        antwoord=0,
        uitleg="De vacuole is een blaas vol vocht. Ze slaat water, voedings- en afvalstoffen op en houdt de cel door de druk van dat vocht stevig.",
    ),
    dict(
        type="waarofniet",
        vraag="Bladgroenkorrels vangen zonlicht op.",
        antwoord=True,
        uitleg="Bladgroenkorrels of chloroplasten bevatten bladgroen. Dat vangt zonlicht op voor de fotosynthese, en geeft het blad meteen ook zijn groene kleur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het cytoplasma?",
        opties=[
            "De vloeistof in de cel waarin de celonderdelen liggen",
            "De harde buitenkant van een plantencel",
            "Het onderdeel dat zonlicht opvangt",
        ],
        antwoord=0,
        uitleg="Het cytoplasma is het gelei-achtige vocht in de cel. De celonderdelen liggen erin, en veel stofomzettingen gebeuren erin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn weefsels bij de mens?",
        opties=["Spierweefsel", "Zenuwweefsel", "De maag", "Het hart"],
        antwoord=[0, 1],
        uitleg="Spierweefsel en zenuwweefsel zijn weefsels. De maag en het hart zijn organen: ze bestaan uit verschillende weefsels samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk van deze is een orgaan van een plant?",
        opties=["Het blad", "Het dekweefsel", "De bladgroenkorrel"],
        antwoord=0,
        uitleg="Wortel, stengel, blad en bloem zijn de organen van een plant. Dekweefsel is een weefsel en een bladgroenkorrel is een celonderdeel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bacterie is een eencellig organisme.",
        antwoord=True,
        uitleg="Een eencellig organisme bestaat uit één enkele cel die alles zelf doet. Een mens is meercellig: zijn cellen hebben elk een eigen taak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk stelsel zorgt ervoor dat zuurstof in je bloed komt?",
        opties=["Het ademhalingsstelsel", "Het spijsverteringsstelsel", "Het uitscheidingsstelsel"],
        antwoord=0,
        uitleg="Het ademhalingsstelsel haalt zuurstof uit de lucht en geeft koolstofdioxide af. Het transportstelsel brengt die zuurstof daarna naar alle cellen.",
    ),
    dict(
        type="invultekst",
        vraag="Het stelsel dat je lichaam rechtop houdt en je organen beschermt, is het ___.",
        antwoord=["beenderstelsel", "skelet"],
        uitleg="Het beenderstelsel of skelet draagt je lichaam, beschermt je hersenen, hart en longen, en geeft de spieren een aanhechtingspunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee stelsels heeft een plant volgens de vakfiche?",
        opties=[
            "Een transportstelsel",
            "Een voortplantingsstelsel",
            "Een ademhalingsstelsel",
            "Een zenuwstelsel",
        ],
        antwoord=[0, 1],
        uitleg="Een plant heeft een transportstelsel, dat water en suikers verplaatst, en een voortplantingsstelsel, de bloem. Zenuwen en longen heeft ze niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Het hart is een weefsel.",
        antwoord=False,
        uitleg="Het hart is een orgaan. Het bestaat uit spierweefsel, zenuwweefsel en bloedvaten samen, en die weefsels bestaan elk uit cellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee bekijk je cellen die je met het blote oog niet ziet?",
        opties=["Met een microscoop", "Met een dynamometer", "Met een maatcilinder"],
        antwoord=0,
        uitleg="Een lichtmicroscoop vergroot sterk genoeg om cellen te zien. Een loep of een binoculair vergroot minder en gebruik je voor grotere dingen, zoals een insect.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dierlijke cel heeft een celwand.",
        antwoord=False,
        uitleg="Alleen plantencellen (en bacteriën en schimmels) hebben een celwand. Een dierlijke cel heeft enkel een celmembraan en is daardoor buigzamer van vorm.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Zet van groot naar klein: orgaan, cel, organisme, weefsel, stelsel. Welke rij klopt?",
        opties=[
            "organisme – stelsel – orgaan – weefsel – cel",
            "organisme – orgaan – stelsel – weefsel – cel",
            "stelsel – organisme – orgaan – cel – weefsel",
        ],
        antwoord=0,
        uitleg="Van afnemende complexiteit: het hele organisme, dan zijn stelsels, daarin de organen, daarin de weefsels, en die bestaan uit cellen met celonderdelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een spiercel heeft veel meer mitochondriën dan een huidcel. Waarom?",
        opties=["Omdat een spier veel energie nodig heeft om samen te trekken", "Omdat een spiercel zonlicht moet opvangen om energie te kunnen maken", "Omdat een spiercel groter moet worden"],
        antwoord=0,
        uitleg="Mitochondriën maken energie vrij uit glucose. Een cel die veel arbeid levert, zoals een spiercel of een hartcel, heeft er daarom veel nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een cel uit de wortel van een plant geen bladgroenkorrels?",
        opties=[
            "Omdat er in de grond geen licht komt",
            "Omdat een wortel geen cellen heeft",
            "Omdat de wortel geen water opneemt",
        ],
        antwoord=0,
        uitleg="Bladgroenkorrels werken alleen met licht. In de donkere bodem heeft fotosynthese geen zin, dus wortelcellen hebben ze niet. Bladcellen zitten er vol mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke celonderdelen hebben een plantaardige én een dierlijke cel allebei?",
        opties=["Celkern", "Cytoplasma", "Mitochondriën", "Celwand"],
        antwoord=[0, 1, 2],
        uitleg="Celkern, celmembraan, cytoplasma en mitochondriën vind je in allebei. Alleen de celwand, de bladgroenkorrels en de grote vacuole zijn typisch plantaardig.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plantencel kan zowel bladgroenkorrels als mitochondriën hebben.",
        antwoord=True,
        uitleg="Een bladcel maakt met haar bladgroenkorrels suikers, en verbrandt met haar mitochondriën een deel van die suikers weer. Een plant ademt dus ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een plant die te weinig water krijgt, gaat slap hangen. Welk celonderdeel verklaart dat?",
        opties=["De vacuole, die leegloopt en dus minder druk geeft", "De celkern, die krimpt zodra er te weinig water binnenkomt", "Het mitochondrion, dat stopt"],
        antwoord=0,
        uitleg="Een volle vacuole duwt de cel van binnenuit tegen de celwand en houdt de plant stevig. Loopt ze leeg, dan verdwijnt die druk en hangt de plant slap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat een boom rechtop en zakt hij niet in elkaar, terwijl een dier een skelet nodig heeft?",
        opties=["Omdat elke plantencel een stevige celwand heeft", "Omdat planten veel minder wegen dan dieren van dezelfde grootte", "Omdat planten geen cellen hebben"],
        antwoord=0,
        uitleg="De celwand van cellulose maakt elke plantencel stevig. Miljoenen stevige cellen samen dragen de hele boom. Dieren lossen dat op met beenderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij het niveau 'weefsel'?",
        opties=["Huidweefsel", "Transportweefsel van een plant", "De nier", "De stengel"],
        antwoord=[0, 1],
        uitleg="Huidweefsel en transportweefsel zijn weefsels. De nier en de stengel zijn organen, want daarin werken verschillende weefsels samen.",
    ),
    dict(
        type="invultekst",
        vraag="Het weefsel dat bij een plant water en suikers vervoert, heet het ___.",
        antwoord=["transportweefsel", "vaatweefsel"],
        uitleg="Het transportweefsel loopt als buisjes door wortel, stengel en blad. Het dekweefsel is de beschermlaag aan de buitenkant.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke cel van een meercellig organisme doet precies hetzelfde werk.",
        antwoord=False,
        uitleg="In een meercellig organisme zijn de cellen gespecialiseerd: een zenuwcel geeft signalen door, een rode bloedcel vervoert zuurstof. Net daardoor kan het lichaam meer dan een eencellige.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker ziet onder de microscoop een cel met een celwand, een grote vacuole en groene korrels. Wat is het?",
        opties=[
            "Een cel uit een blad",
            "Een cel uit een spier",
            "Een rode bloedcel",
        ],
        antwoord=0,
        uitleg="Celwand plus vacuole plus bladgroenkorrels wijst op een plantencel, en de groene korrels wijzen op een deel dat licht krijgt: een blad.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stelsels van de mens werken samen om zuurstof en voedingsstoffen tot in je tenen te krijgen?",
        opties=[
            "Het ademhalingsstelsel",
            "Het spijsverteringsstelsel",
            "Het transportstelsel",
            "Het beenderstelsel",
        ],
        antwoord=[0, 1, 2],
        uitleg="De longen halen zuurstof binnen, de darmen de voedingsstoffen, en het bloed brengt allebei tot bij elke cel. Geen enkel stelsel redt dat alleen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met een cel als haar celkern zou verdwijnen?",
        opties=["Ze kan zich niet meer delen en verliest haar aansturing", "Ze zou een stevige celwand krijgen, net als een plantencel", "Ze zou meer energie maken"],
        antwoord=0,
        uitleg="De celkern bewaart het erfelijk materiaal en stuurt de cel aan. Zonder kern valt die aansturing weg en kan de cel zich niet meer vermenigvuldigen.",
    ),
    dict(
        type="invultekst",
        vraag="Een organisme dat uit één enkele cel bestaat, noem je ___.",
        antwoord=["eencellig", "eencellige"],
        uitleg="Bij een eencellig organisme doet die ene cel alles: voeding opnemen, energie maken, afval kwijtraken en zich voortplanten.",
    ),
    dict(
        type="waarofniet",
        vraag="Het celmembraan laat alle stoffen zomaar door.",
        antwoord=False,
        uitleg="Het celmembraan is selectief: het kiest wat binnen mag en wat buiten blijft. Zo houdt de cel haar samenstelling in de hand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rij hoort volledig bij hetzelfde organisatieniveau?",
        opties=[
            "Maag, hart, longen, nieren",
            "Maag, spierweefsel, cel, hart",
            "Celkern, maag, longen",
        ],
        antwoord=0,
        uitleg="Maag, hart, longen en nieren zijn alle vier organen. In de andere rijen staan niveaus door elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een dierlijke cel kloppen?",
        opties=[
            "Ze heeft een celmembraan",
            "Ze heeft mitochondriën",
            "Ze heeft bladgroenkorrels",
            "Ze heeft een celwand",
        ],
        antwoord=[0, 1],
        uitleg="Elke dierlijke cel heeft een celmembraan en mitochondriën. Bladgroenkorrels en een celwand heeft ze niet, want ze maakt geen suikers met licht en wordt gesteund door een skelet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een orgaan bestaat uit verschillende weefsels.",
        antwoord=True,
        uitleg="De maag bijvoorbeeld heeft spierweefsel om te kneden, een slijmvlies aan de binnenkant en zenuwweefsel dat alles aanstuurt.",
    ),
    dict(
        type="invultekst",
        vraag="Het celonderdeel dat bij een plant zorgt voor stevigheid en bescherming, is de ___.",
        antwoord="celwand",
        uitleg="De celwand ligt rond het celmembraan en is gemaakt van cellulose. Hij is stevig en laat water en opgeloste stoffen door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bekijk je een stukje ui onder een microscoop en niet met een loep?",
        opties=["Omdat een loep te weinig vergroot om cellen te zien", "Omdat een microscoop geen licht van buitenaf nodig heeft", "Omdat een loep enkel voor planten dient"],
        antwoord=0,
        uitleg="Kies je meetinstrument naar de nauwkeurigheid die je nodig hebt. Een loep vergroot enkele keren, een lichtmicroscoop honderden keren, en pas dan zie je afzonderlijke cellen.",
    ),
]
