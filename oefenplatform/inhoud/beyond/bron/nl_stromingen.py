# -*- coding: utf-8 -*-
"""Literaire stromingen van de middeleeuwen tot nu — 🌍 Beyond, Nederlands.

Naast de termenlijst van de vakfiches geschreven, die de stromingen ordent
per periode: middeleeuwen, vroegmoderne tijd, moderne tijd en hedendaagse
tijd. Deel 1 loopt van de middeleeuwen tot en met de romantiek en het
realisme, deel 2 van de Tachtigers tot vandaag.

Er worden geen boektitels of auteursnamen aan kenmerken gekoppeld die niet
op de lijst van de fiche staan; de vragen gaan over de kenmerken zelf.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt de hoofse literatuur van de middeleeuwen?",
        opties=[
            "de verheven liefde voor een onbereikbare vrouw",
            "de spot met het gezag van de kerk",
            "de nauwkeurige beschrijving van armoede",
            "de weergave van de gedachtestroom van een ik",
        ],
        antwoord=0,
        uitleg="De ridder dient zijn dame zonder haar ooit te krijgen. Die verheven, onvervulde liefde is de kern van het hoofse ideaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stromingen horen bij de middeleeuwen?",
        opties=[
            "de voorhoofse literatuur",
            "de hoofse literatuur",
            "de rederijkers",
            "de romantiek",
        ],
        antwoord=[0, 1, 2],
        uitleg="De romantiek hoort bij de moderne tijd, rond 1800. De drie andere zijn middeleeuws.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de leden van de stedelijke dichtersgilden aan het einde van de middeleeuwen? Antwoord met één woord.",
        antwoord=["rederijkers"],
        uitleg="Zij organiseerden wedstrijden, schreven refreinen en speelden toneel in de steden.",
    ),
    dict(
        type="waarofniet",
        vraag="De renaissance greep terug naar de klassieke oudheid.",
        antwoord=True,
        uitleg="Renaissance betekent wedergeboorte: men nam de vormen en de idealen van Grieken en Romeinen weer op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stromingen horen bij de vroegmoderne tijd?",
        opties=[
            "de renaissance",
            "de barok",
            "de verlichting",
            "het naturalisme",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het naturalisme is negentiende-eeuws. De drie andere horen bij de vroegmoderne tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt de barok?",
        opties=[
            "overvloed, beweging en de vergankelijkheid van alles",
            "soberheid en een voorkeur voor heel korte zinnen",
            "nauwkeurig verslag van de werkelijkheid",
            "spel met de vorm en de typografie",
        ],
        antwoord=0,
        uitleg="Pracht en praal naast het besef dat alles voorbijgaat: die spanning is het hart van de barok.",
    ),
    dict(
        type="waarofniet",
        vraag="De verlichting stelde de rede en het eigen denken centraal.",
        antwoord=True,
        uitleg="Niet het gezag van kerk of vorst maar het eigen verstand moest uitmaken wat waar is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt de romantiek?",
        opties=[
            "gevoel, verbeelding en het verlangen naar het verre",
            "de koele vaststelling van maatschappelijke feiten",
            "de navolging van de klassieke regels van de oudheid",
            "de weergave van vluchtige indrukken van het moment",
        ],
        antwoord=0,
        uitleg="Tegenover de rede van de verlichting zette de romantiek het gevoel, de natuur, het verleden en het onbereikbare.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt het realisme?",
        opties=[
            "de werkelijkheid weergeven zoals ze is",
            "de werkelijkheid mooier maken dan ze is",
            "de werkelijkheid volledig negeren",
            "de werkelijkheid in verzen navertellen",
        ],
        antwoord=0,
        uitleg="Het realisme kijkt naar het gewone leven van gewone mensen, zonder opsmuk.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stroming zette gevoel en verbeelding tegenover de rede van de verlichting? Antwoord met één woord.",
        antwoord=["romantiek"],
        uitleg="De romantiek vierde het gevoel, de natuur en het onbereikbare verlangen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het naturalisme gaat ervan uit dat afkomst en omgeving het lot van een mens bepalen.",
        antwoord=True,
        uitleg="Erfelijkheid en milieu drukken het personage in een richting waaruit het niet ontsnapt. Daarom lopen zulke romans vaak slecht af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken horen bij het naturalisme?",
        opties=[
            "de hoofdfiguur is vaak nerveus of zwak",
            "taboeonderwerpen worden niet vermeden",
            "erfelijkheid en milieu sturen het verhaal",
            "de werkelijkheid wordt verheerlijkt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Verheerlijken is net wat het naturalisme niet doet. Het kijkt koel en soms genadeloos.",
    ),
    dict(
        type="waarofniet",
        vraag="Realisme en naturalisme zijn precies hetzelfde.",
        antwoord=False,
        uitleg="Het naturalisme gaat verder: het verklaart de mens uit erfelijkheid en milieu, en kiest daarbij vaak de donkerste kant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de voorhoofse en de hoofse literatuur?",
        opties=[
            "de voorhoofse is ruwer, de hoofse verfijnder",
            "de voorhoofse is jonger dan de hoofse",
            "de voorhoofse werd enkel in kloosters geschreven",
            "de voorhoofse bestond enkel uit toneelteksten",
        ],
        antwoord=0,
        uitleg="De voorhoofse verhalen draaien om strijd en trouw; de hoofse brengen daar het verfijnde liefdesideaal bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gedicht uit welke periode zou je verwachten dat het de vergankelijkheid van het aardse leven bezingt met rijke beelden?",
        opties=[
            "de barok",
            "de verlichting",
            "het realisme",
            "het modernisme",
        ],
        antwoord=0,
        uitleg="Rijkdom van beeld naast het besef dat alles stof wordt: dat is barok.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stroming begint en eindigt op een scherp af te lijnen jaartal.",
        antwoord=False,
        uitleg="Stromingen overlappen elkaar jarenlang. Eén schrijver kan zelfs in twee stromingen tegelijk passen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stroming legde de nadruk op de rede, de wetenschap en het eigen oordeel? Antwoord met één woord.",
        antwoord=["verlichting"],
        uitleg="Zij bereidde de politieke omwentelingen van het einde van de achttiende eeuw mee voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een roman over een arbeidersgezin dat ondanks alle pogingen niet uit de armoede raakt, met veel aandacht voor ziekte en drank. Welke stroming?",
        opties=[
            "het naturalisme",
            "de romantiek",
            "de renaissance",
            "het postmodernisme",
        ],
        antwoord=0,
        uitleg="Milieu en erfelijkheid die het lot bepalen, en taboes die niet geschuwd worden: dat is het naturalisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig om de kenmerken van een stroming te kennen?",
        opties=[
            "je plaatst een tekst dan in zijn eigen tijd",
            "je weet dan meteen of de tekst goed is",
            "je hoeft de tekst dan niet meer te lezen",
            "je kent dan de naam van de schrijver",
        ],
        antwoord=0,
        uitleg="Een tekst wordt begrijpelijker als je weet tegen welke achtergrond en tegen welke voorgangers hij geschreven is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een middeleeuws verhaal over Karel de Grote en zijn ridders hoort bij welke traditie?",
        opties=[
            "de voorhoofse literatuur",
            "de hoofse literatuur",
            "de rederijkerskunst",
            "de barok",
        ],
        antwoord=0,
        uitleg="De Karelepiek draait om strijd, trouw en leenheerschap, niet om het verfijnde liefdesideaal.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de Tachtigers?",
        opties=[
            "kunst om de kunst en de kracht van het individu",
            "de verheerlijking van de machine en de stad",
            "het volledig loslaten van elke vorm van beeld",
            "de terugkeer naar de klassieke versmaat",
        ],
        antwoord=0,
        uitleg="Hun leuze was dat kunst de allerindividueelste expressie van de allerindividueelste emotie moest zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt het impressionisme in de literatuur?",
        opties=[
            "de weergave van vluchtige zintuiglijke indrukken",
            "de nauwkeurige analyse van maatschappelijke klassen",
            "het spel met verwijzingen naar andere teksten",
            "het strak volgen van een vaste versvorm",
        ],
        antwoord=0,
        uitleg="Niet het ding zelf maar de indruk die het maakt, op dat ene moment, in dat ene licht.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stroming drukt innerlijke gevoelens uit door de werkelijkheid te vervormen? Antwoord met één woord.",
        antwoord=["expressionisme"],
        uitleg="Kleuren, vormen en taal worden overdreven om een innerlijke toestand naar buiten te persen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het symbolisme werkt met beelden die naar een diepere, niet rechtstreeks te benoemen werkelijkheid verwijzen.",
        antwoord=True,
        uitleg="Het symbool suggereert in plaats van te benoemen. Daarom blijven zulke gedichten vaak meerduidig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stromingen horen bij de moderne tijd?",
        opties=[
            "het expressionisme",
            "het existentialisme",
            "de nieuwe zakelijkheid",
            "het postmodernisme",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het postmodernisme hoort bij de hedendaagse tijd. De drie andere staan bij de moderne tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt de nieuwe zakelijkheid?",
        opties=[
            "een nuchtere, onopgesmukte stijl",
            "een overvloed aan beeldspraak",
            "een voortdurende verwijzing naar mythen",
            "een strikte navolging van de sonnetvorm",
        ],
        antwoord=0,
        uitleg="Kort, feitelijk en zonder sentiment: de taal van het verslag eerder dan die van het gedicht.",
    ),
    dict(
        type="waarofniet",
        vraag="Het existentialisme gaat ervan uit dat de mens zijn eigen betekenis moet maken.",
        antwoord=True,
        uitleg="Er is geen vooraf gegeven zin; de mens is vrij en daardoor ook verantwoordelijk. Dat levert vaak zwaarmoedige literatuur op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt de Vijftigers?",
        opties=[
            "associatie en experiment met taal en vorm",
            "strikte navolging van de klassieke versmaat",
            "een nauwgezette weergave van de werkelijkheid",
            "een terugkeer naar het middeleeuwse rijm",
        ],
        antwoord=0,
        uitleg="Zij braken met de regels van spelling, grammatica en vorm, en lieten beelden vrij op elkaar inwerken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het surrealisme?",
        opties=[
            "een stroming die het droombeeld en het onbewuste verkent",
            "een stroming die de werkelijkheid zo precies mogelijk afbeeldt",
            "een stroming die enkel over het landleven schrijft",
            "een stroming die de klassieke oudheid navolgt",
        ],
        antwoord=0,
        uitleg="Beelden uit de droom worden naast elkaar gezet zonder dat er logica aan te pas komt.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stroming vierde de levenskracht, de energie en het lichaam? Antwoord met één woord.",
        antwoord=["vitalisme"],
        uitleg="Vitaal betekent levenskrachtig. Snelheid, sport en jeugd horen bij het beeld dat het vitalisme oproept.",
    ),
    dict(
        type="waarofniet",
        vraag="Avant-garde is een verzamelnaam voor stromingen die bewust met de traditie breken.",
        antwoord=True,
        uitleg="Avant-garde betekent voorhoede: wie vooroploopt en eerst de gebaande wegen verlaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt het magisch-realisme?",
        opties=[
            "het wonderlijke dringt de gewone wereld binnen",
            "het verhaal speelt volledig in een droomwereld",
            "de werkelijkheid wordt wetenschappelijk verklaard",
            "het verhaal bestaat enkel uit dialogen",
        ],
        antwoord=0,
        uitleg="De wereld is herkenbaar en alledaags, en toch gebeurt er iets wat niet kan, zonder dat iemand ervan opkijkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken horen bij het postmodernisme?",
        opties=[
            "twijfel aan één grote waarheid",
            "spel met verwijzingen naar andere teksten",
            "het doorbreken van de illusie van het verhaal",
            "het geloof in de vooruitgang van de wetenschap",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het geloof in de grote vooruitgang is net wat het postmodernisme in twijfel trekt.",
    ),
    dict(
        type="waarofniet",
        vraag="Het neorealisme keert zich af van het alledaagse en zoekt juist het wonderlijke op.",
        antwoord=False,
        uitleg="Het doet net het omgekeerde: na jaren van experiment keerde de blik terug naar de gewone dingen, in eenvoudige taal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de neoromantiek?",
        opties=[
            "een hernieuwde aandacht voor gevoel en verbeelding",
            "een terugkeer naar de klassieke oudheid",
            "een stroming die enkel in het theater voorkomt",
            "een stroming die de wetenschap verheerlijkt",
        ],
        antwoord=0,
        uitleg="Neo betekent nieuw: het is de romantische houding die in een latere tijd opnieuw opduikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt het relationisme?",
        opties=[
            "de aandacht gaat naar de band tussen mensen",
            "de aandacht gaat naar de vorm van de zin",
            "de aandacht gaat naar de politiek van de dag",
            "de aandacht gaat naar het landschap",
        ],
        antwoord=0,
        uitleg="Niet het grote verhaal maar de betrekkingen tussen mensen onderling staan er centraal.",
    ),
    dict(
        type="invultekst",
        vraag="Welke hedendaagse stroming laat het wonderlijke gebeuren in een gewone wereld? Vul aan: het magisch-...",
        antwoord=["realisme"],
        uitleg="Het onmogelijke gebeurt, en de personages vinden het de normaalste zaak van de wereld.",
    ),
    dict(
        type="waarofniet",
        vraag="Een schrijver kan maar kenmerken van één stroming tegelijk gebruiken.",
        antwoord=False,
        uitleg="Stromingen zijn hulpmiddelen om te ordenen, geen hokjes. Eén tekst kan gerust kenmerken van twee stromingen dragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een roman waarin de verteller plots zegt dat hij het verhaal zelf verzint. Bij welke stroming past dat?",
        opties=[
            "het postmodernisme",
            "het naturalisme",
            "de romantiek",
            "het impressionisme",
        ],
        antwoord=0,
        uitleg="De illusie van het verhaal wordt opzettelijk doorbroken. Dat is een typisch postmodern procedé.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een gedicht vol ongewone woordcombinaties, zonder hoofdletters en met gebroken zinsbouw. Bij welke groep past dat het best?",
        opties=[
            "de Vijftigers",
            "de Tachtigers",
            "de rederijkers",
            "de nieuwe zakelijkheid",
        ],
        antwoord=0,
        uitleg="De Vijftigers experimenteerden juist met taal, stijl, spelling en grammatica, en werkten sterk associatief.",
    ),
]
