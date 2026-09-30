# -*- coding: utf-8 -*-
"""De vragen voor "Standen, domein en stad" (🚀 Boost doorstroom, geschiedenis).

Uit de vakfiche, leerinhouden middeleeuwen: de gelaagde samenleving met de drie
standen en hun rechten en plichten, de agrarische samenleving met het domein
als zelfvoorzienend systeem en de landbouwvernieuwingen, en de stedelijke
samenleving met ambachten en gilden, de geldeconomie, de politieke
zelfstandigheid van de stad, de ongelijkheid in de stad en de pest.

Deel 1 gaat over de standen en het platteland. Deel 2 over de stad.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie standen kende de middeleeuwse samenleving?",
        opties=[
            "de geestelijkheid, de adel en de derde stand",
            "de koningen, de ridders en de boeren",
            "de rijken, de middenstand en de armen",
            "de vrijen, de horigen en de slaven",
        ],
        antwoord=0,
        uitleg="Wie bidt, wie strijdt en wie werkt. Die driedeling is een voorstelling van de samenleving, opgeschreven door de eerste stand zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke taak hoorde volgens de standenleer bij de geestelijkheid?",
        opties=["bidden", "strijden", "werken", "handel drijven"],
        antwoord=0,
        uitleg="De eerste stand bad voor het zielenheil van allen, de tweede beschermde met het zwaard, de derde voedde de twee andere.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de stand van wie werkte en de twee andere standen moest onderhouden?",
        antwoord="de derde stand",
        uitleg="Daar zat verreweg het grootste deel van de bevolking in: boeren, en later ook ambachtslui en handelaars.",
    ),
    dict(
        type="waarofniet",
        vraag="In welke stand je geboren werd, bepaalde bijna helemaal welk leven je kreeg.",
        antwoord=True,
        uitleg="Geboorte, niet verdienste, bepaalde je plaats. Dat is precies wat een standensamenleving onderscheidt van een samenleving met sociale mobiliteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rechten had de adel die de derde stand niet had?",
        opties=[
            "eigen rechtspraak over de bewoners van het domein",
            "vrijstelling van bepaalde belastingen",
            "het recht om te jagen in de heerlijke bossen",
            "het recht om te stemmen bij verkiezingen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Verkiezingen bestonden niet. De drie andere voorrechten hielden de ongelijkheid juist in stand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bleef de sociale ongelijkheid in de middeleeuwen zo lang bestaan?",
        opties=[
            "de ordening werd als door God gewild voorgesteld, en de voorrechten waren erfelijk",
            "iedereen in de samenleving was even arm, dus er viel eenvoudigweg niets te verdelen",
            "de koning had elke verandering aan de bestaande ordening bij wet verboden",
            "er woonden veel te weinig mensen om er samen iets aan te kunnen veranderen",
        ],
        antwoord=0,
        uitleg="Wie de ordening in vraag stelde, ging in tegen de wil van God zoals de Kerk die verkondigde. En erfelijke voorrechten verplaatsen zich niet vanzelf.",
    ),
    dict(
        type="waarofniet",
        vraag="De standensamenleving bleef de hele middeleeuwen door precies dezelfde.",
        antwoord=False,
        uitleg="Met de groei van de steden komt er een groep bij die rijk is zonder adellijk te zijn. De driedeling blijft in woorden bestaan, maar klopt steeds minder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een domein in de agrarische samenleving?",
        opties=[
            "het grondbezit van een heer, met vroonland en hoevenland",
            "een stad met een eigen bestuur en een eigen rechtspraak",
            "een kloosterorde die volgens een eigen regel leeft",
            "een markt in de stad waar men vee en graan verhandelde",
        ],
        antwoord=0,
        uitleg="Het vroonland bewerkte de heer voor zichzelf, met de verplichte arbeid van zijn boeren; het hoevenland verdeelde hij onder de boeren zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat het domein zelfvoorzienend was?",
        opties=[
            "bijna alles wat men nodig had, werd er zelf geproduceerd",
            "de heer betaalde alles wat er nodig was uit zijn eigen zak",
            "de boeren op het domein hoefden geen enkele belasting te betalen",
            "er werd op het hele domein enkel graan en verder niets verbouwd",
        ],
        antwoord=0,
        uitleg="Voedsel, kleding, gereedschap: het meeste kwam van het domein zelf. Er werd weinig gekocht en weinig verkocht.",
    ),
    dict(
        type="waarofniet",
        vraag="Horigen waren slaven die verkocht konden worden.",
        antwoord=False,
        uitleg="Een horige was niet vrij om te vertrekken, maar hij was ook geen eigendom. Hij had een eigen hoeve en gaf een deel van zijn opbrengst af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke landbouwvernieuwing komt pas eeuwen later, en hoort dus niet in de middeleeuwen thuis?",
        opties=[
            "de kunstmest",
            "het drieslagstelsel",
            "de keerploeg",
            "het haam",
        ],
        antwoord=0,
        uitleg="Kunstmest komt pas in de 19de eeuw. De drie andere verhogen de opbrengst per stuk grond wel al in de middeleeuwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het drieslagstelsel?",
        opties=[
            "de grond wordt in drie delen verdeeld: wintergraan, zomergraan en braak",
            "de boeren werken elke week drie dagen op het vroonland van de heer",
            "de oogst wordt in drie gelijke delen verdeeld: heer, boer en Kerk",
            "er wordt drie keer per jaar geoogst, in de lente, de zomer en de herfst",
        ],
        antwoord=0,
        uitleg="Tegenover het oudere tweeslagstelsel ligt er zo maar een derde braak in plaats van de helft. Meer grond in gebruik, dus meer voedsel.",
    ),
    dict(
        type="waarofniet",
        vraag="Meer voedsel leidde tot een groeiende bevolking, en die groei maakte steden mogelijk.",
        antwoord=True,
        uitleg="Niet iedereen moest nog voedsel produceren. Wie overbleef, kon naar de stad en daar een ambacht uitoefenen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het deel van de grond dat een jaar niet bewerkt wordt om te herstellen?",
        antwoord="braakland",
        uitleg="Zonder kunstmest is rust de enige manier om de bodem zijn vruchtbaarheid terug te geven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat verhandelde men op de lokale markt, en wat over lange afstand?",
        opties=[
            "lokaal vooral voedsel en gereedschap, over lange afstand vooral dure en lichte waren",
            "lokaal vooral specerijen en zijde, over lange afstand vooral graan en brandhout",
            "lokaal precies dezelfde waren als over lange afstand, alleen in kleinere hoeveelheden",
            "lokaal vooral zijde en edelmetaal, over lange afstand vooral groenten en melk",
        ],
        antwoord=0,
        uitleg="Vervoer was traag en duur, dus loonde het alleen voor waren met veel waarde in weinig gewicht: specerijen, zijde, edelmetaal, later laken.",
    ),
    dict(
        type="waarofniet",
        vraag="De vooruitgang in de landbouw en de groei van de handel staan los van elkaar.",
        antwoord=False,
        uitleg="Pas wanneer er een overschot is, valt er iets te verkopen. Meer landbouwopbrengst is dus de voorwaarde voor meer handel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verplichtingen had een horige tegenover zijn heer?",
        opties=[
            "herendiensten op het vroonland",
            "een deel van de oogst afstaan",
            "tol en heffingen betalen bij molen en oven",
            "elk jaar in het leger van de koning dienen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Legerdienst hoorde bij de tweede stand. De drie andere zijn de gewone lasten van een horige, en ze maakten hem afhankelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke maatschappelijke domeinen situeer je de standensamenleving?",
        opties=[
            "het sociale domein",
            "het politieke domein",
            "het culturele domein",
            "het maritieme domein",
        ],
        antwoord=[0, 1, 2],
        uitleg="Maritiem is een ruimtebegrip, geen domein. De standen bepalen wie waar staat, wie mag beslissen, en de Kerk geeft er de rechtvaardiging voor.",
    ),
    dict(
        type="waarofniet",
        vraag="Een minderheidsgroep zoals de joden viel buiten de driedeling van de standen.",
        antwoord=True,
        uitleg="De driedeling was een christelijk beeld van een christelijke samenleving. Wie er niet in paste, kreeg een aparte en vaak kwetsbare positie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de voorstelling van de drie standen zelf een bron die je kritisch moet bekijken?",
        opties=[
            "ze is opgeschreven door geestelijken, die er zelf bovenaan in staan",
            "ze is pas in de 19de eeuw bedacht, lang na de middeleeuwen zelf",
            "ze werd door de tijdgenoten zelf nooit geloofd of ernstig genomen",
            "ze is niet in het Latijn geschreven maar in een latere volkstaal",
        ],
        antwoord=0,
        uitleg="Wie de ordening beschrijft, beschrijft meteen zijn eigen plaats erin. Dat is standplaatsgebondenheid in haar zuiverste vorm.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke factoren dragen bij tot de heropbloei van de steden vanaf de 11de eeuw?",
        opties=[
            "een groeiende bevolking door betere landbouw",
            "meer veiligheid, waardoor handel over langere afstand kon",
            "de ligging aan een rivier, een weg of een kruispunt",
            "de uitvinding van de stoommachine en van de spoorweg",
        ],
        antwoord=[0, 1, 2],
        uitleg="De stoommachine komt pas in de 18de eeuw. De drie andere verklaren wel waarom steden opnieuw groeiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ontstonden veel steden aan een rivier?",
        opties=[
            "water was de goedkoopste manier om zware vracht te vervoeren",
            "een rivier was voor een stad veruit de makkelijkste grens om te verdedigen",
            "rivierwater was in die tijd overal zuiver en veilig drinkwater voor iedereen",
            "de koning verplichtte elke nieuwe stad aan een rivier gebouwd te worden",
        ],
        antwoord=0,
        uitleg="Een schip vervoert veel meer dan een kar, en het hoeft geen slechte wegen te trotseren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de vereniging van ambachtslui van hetzelfde beroep in een middeleeuwse stad?",
        antwoord="het ambacht",
        uitleg="Ze bepaalde wie het beroep mocht uitoefenen, hoe goed het werk moest zijn en soms ook wat het mocht kosten. Men spreekt ook van een gilde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat regelde een ambacht of gilde niet?",
        opties=[
            "de belastingen van het hele graafschap",
            "wie het beroep in de stad mocht uitoefenen",
            "de kwaliteit van het geleverde werk",
            "de opleiding van leerjongen tot meester",
        ],
        antwoord=0,
        uitleg="Belastingen van het graafschap waren de zaak van de vorst. De drie andere zaken regelde het ambacht binnen de stadsmuren wel.",
    ),
    dict(
        type="waarofniet",
        vraag="Iedereen kon zomaar meester worden in een ambacht.",
        antwoord=False,
        uitleg="Je doorliep eerst jaren als leerjongen en gezel, je maakte een meesterproef, en je had geld nodig voor een eigen werkplaats. Zonen van meesters kwamen er veel makkelijker in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het ontstaan van een geldeconomie?",
        opties=[
            "goederen en arbeid worden steeds vaker met geld betaald in plaats van in natura",
            "iedereen in de stad en op het platteland krijgt voortaan precies evenveel geld",
            "de koning laat geen munten meer slaan en verbiedt het gebruik van muntgeld",
            "men ruilt helemaal niets meer en iedereen maakt alles voor zichzelf alleen",
        ],
        antwoord=0,
        uitleg="Op het domein betaalde men in dagen werk en in graan. In de stad betaalt men in munten, en dat maakt handel over grotere afstand mogelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Met de geldeconomie komen er ook wisselaars, kredietvormen en boekhouding op.",
        antwoord=True,
        uitleg="Wie met munten uit tien streken werkt, heeft iemand nodig die ze omrekent. Uit dat beroep groeit het bankwezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kregen steden politieke zelfstandigheid?",
        opties=[
            "ze kochten of verkregen privileges van hun vorst",
            "ze versloegen de koning in een oorlog en dwongen het af",
            "de paus in Rome schonk ze die zelfstandigheid bij oorkonde",
            "ze riepen zichzelf zonder meer uit tot een eigen koninkrijk",
        ],
        antwoord=0,
        uitleg="Een vorst had geld nodig; een stad had geld. In ruil kreeg ze eigen rechtspraak, eigen bestuur en het recht op een markt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het document waarin een vorst de rechten van een stad vastlegde?",
        antwoord="een keure",
        uitleg="Zo'n oorkonde met stadsrechten legde zwart op wit vast wat de stad zelf mocht regelen. Men spreekt ook van een privilege.",
    ),
    dict(
        type="waarofniet",
        vraag="Binnen de stadsmuren waren alle inwoners gelijk.",
        antwoord=False,
        uitleg="Een kleine groep rijke koopmansfamilies, de patriciërs, bestuurde de stad. De ambachtslui en de armen hadden lang niets te zeggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waartoe leidde de politieke ongelijkheid in de steden?",
        opties=[
            "tot opstanden van de ambachten tegen de patriciërs",
            "tot de volledige afschaffing van alle ambachten in de stad",
            "tot het vertrek van alle handelaars naar het platteland",
            "tot het einde van de stadsrechten die de vorst gegeven had",
        ],
        antwoord=0,
        uitleg="In de Vlaamse steden veroverden de ambachten in de 14de eeuw een plaats in het stadsbestuur, vaak na gewelddadige conflicten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gebouwen horen bij een middeleeuwse stad, en waarvoor dienden ze?",
        opties=[
            "het belfort, als toren van de stedelijke vrijheid en bewaarplaats van de privileges",
            "de lakenhalle, om handelswaar te verhandelen en te keuren",
            "de kathedraal, als centrum van het godsdienstige leven",
            "het kasteel van de koning, als zetel van het rijksbestuur",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een koninklijk kasteel hoorde niet bij de stad maar bij de vorst, en stond er vaak juist buiten of tegenover.",
    ),
    dict(
        type="waarofniet",
        vraag="Het belfort was het wereldlijke tegenbeeld van de kerktoren: het luidde de klok van de stad en bewaarde haar oorkonden.",
        antwoord=True,
        uitleg="Wie het belfort zag, zag de vrijheid van de stad zelf. De kerktoren ernaast stond voor een heel andere macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer trof de pest West-Europa het hardst?",
        opties=[
            "in het midden van de 14de eeuw",
            "in het midden van de 11de eeuw",
            "in het midden van de 16de eeuw",
            "in het midden van de 18de eeuw",
        ],
        antwoord=0,
        uitleg="Vanaf 1347 sterft op enkele jaren tijd naar schatting een derde van de bevolking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen had de pest voor de samenleving?",
        opties=[
            "arbeid werd schaars, dus stegen de lonen",
            "sommige groepen, zoals de joden, kregen de schuld en werden vervolgd",
            "veel grond kwam leeg te liggen",
            "de bevolking groeide sneller dan ooit",
        ],
        antwoord=[0, 1, 2],
        uitleg="De bevolking kromp juist, en het duurde meer dan een eeuw voor ze zich herstelde.",
    ),
    dict(
        type="waarofniet",
        vraag="Stad en platteland stonden in de middeleeuwen volledig los van elkaar.",
        antwoord=False,
        uitleg="De stad at wat het platteland teelde, en het platteland kocht wat de stad maakte. Bovendien kwamen de nieuwe stadsbewoners van het land.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke band tussen stad en platteland bestond er net níét?",
        opties=[
            "het platteland bestuurde de stad",
            "de stad haalde haar voedsel van het platteland",
            "het platteland kocht laken in de stad",
            "stedelingen kochten grond buiten de muren",
        ],
        antwoord=0,
        uitleg="Het bestuur ging net de andere kant op: rijke stedelingen kochten heerlijkheden op het platteland en kregen er zeggenschap.",
    ),
    dict(
        type="waarofniet",
        vraag="Stadslucht maakt vrij: wie lang genoeg in de stad verbleef, kon zijn horigheid kwijtraken.",
        antwoord=True,
        uitleg="Veel steden kenden die regel, meestal na een jaar en een dag. Ze maakte van de stad een uitweg voor wie op het domein vastzat.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk maatschappelijk domein hoort het ontstaan van de geldeconomie in de eerste plaats thuis?",
        opties=[
            "het economische domein",
            "het culturele domein",
            "het politieke domein",
            "het sociale domein",
        ],
        antwoord=0,
        uitleg="Het gaat over hoe men betaalt, produceert en handelt. Dat de gevolgen ook sociaal en politiek waren, spreekt dat niet tegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men de groei van de steden een verandering en niet zomaar een continuïteit?",
        opties=[
            "omdat er een nieuwe groep ontstaat die rijk is zonder adellijk te zijn",
            "omdat werkelijk alle boeren het platteland verlieten en naar de stad trokken",
            "omdat de adel als stand in die eeuwen volledig van het toneel verdween",
            "omdat de Kerk haar invloed op het dagelijkse leven toen helemaal verloor",
        ],
        antwoord=0,
        uitleg="De standenleer had geen plaats voor rijke kooplui. Juist die groep zet de oude ordening onder druk.",
    ),
]
