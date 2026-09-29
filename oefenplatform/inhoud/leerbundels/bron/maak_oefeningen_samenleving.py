# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij samenleving en economie ✨ Spark.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm: andere situaties om te beoordelen, andere bedragen om mee te rekenen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een schema
invullen). Wie hier iets bijschrijft, legt het eerst naast
`../../spark/samenleving-en-economie.json`.

Twee bundels dragen een waarschuwing. Bij eerste hulp kan een fout antwoord echt
schaden: elk antwoord hieronder volgt de richtlijnen van het Rode Kruis. En bij
"Ik leef samen met anderen" staat de prent van de speelplaats mee in de pdf; elke
vraag daarover is van die prent afgeteld. Regenereert Kim die prent, dan moeten
die vragen herschreven worden.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Samenleving en economie"
SPARK = "✨ Spark — 1ste en 2de middelbaar"
PRENTEN = pathlib.Path(__file__).resolve().parents[3] / "public" / "prenten" / "samenleving-en-economie"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een situatie: zeg niet alleen wát er misgaat, maar ook waaróm.",
    "Bij een rekenvraag: schrijf eerst de bewerking op en zet de eenheid erbij.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-ik-ben-wie-ik-ben-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Ik ben wie ik ben",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De drie lagen van je persoonlijke identiteit",
             opdracht="Schrijf bij elk gegeven welke laag het is: biologische aspecten, persoonlijke eigenschappen of familiale achtergrond.",
             oefeningen=[
                 ("rij", [("ik ben veertien jaar", "biologische aspecten"),
                          ("ik ben nogal koppig", "persoonlijke eigenschappen"),
                          ("mijn vader is verpleger", "familiale achtergrond"),
                          ("ik ben de jongste van drie", "familiale achtergrond")],
                  "Welke laag is dit?", WW),
                 ("rij", [("thuis spreken we Pools", "familiale achtergrond"),
                          ("ik ben snel afgeleid", "persoonlijke eigenschappen"),
                          ("ik ben 1 meter 62", "biologische aspecten"),
                          ("ik ben behulpzaam", "persoonlijke eigenschappen")],
                  "Welke laag is dit?", WW),
                 ("open", "Zet drie dingen over jezelf op papier, één uit elke laag. Zet er telkens bij welke laag het is.",
                  "Elk antwoord is goed zolang er één gegeven bij elke laag staat: iets over je lichaam, "
                  "leeftijd of geslacht, iets over je karakter, en iets over je gezin of thuistaal.", 5),
             ]),

        dict(kop="Identiteit of niet?",
             opdracht="Duid aan of de uitspraak iets zegt over iemands identiteit.",
             oefeningen=[
                 ("waar", "\"Hij zit sinds zijn zesde in de scouts.\" Dat zegt iets over zijn identiteit.", True),
                 ("waar", "\"Het regent vandaag de hele dag.\" Dat zegt iets over iemands identiteit.", False),
                 ("waar", "\"Zij is opgegroeid in West-Vlaanderen.\" Dat zegt iets over haar identiteit.", True),
                 ("waar", "\"De trein van 8 uur is afgeschaft.\" Dat zegt iets over iemands identiteit.", False),
             ]),

        dict(kop="Vier woorden over identiteit",
             opdracht="Vul het juiste woord in: gelaagd, dynamisch, relationeel of uniek.",
             oefeningen=[
                 ("rij", [("ze kan veranderen in de loop van je leven", "dynamisch"),
                          ("ze bestaat uit verschillende lagen", "gelaagd"),
                          ("ze krijgt vorm in je contacten met anderen", "relationeel"),
                          ("niemand heeft precies dezelfde", "uniek")],
                  "Welk woord hoort hierbij?", WW),
                 ("open", "Een meisje van elf houdt alleen van paarden. Op haar zestiende speelt ze gitaar en "
                          "geeft ze niets meer om paarden. Welk van die vier woorden zie je hier, en waarom?",
                  "Dynamisch: haar identiteit lag niet vast, ze is mee veranderd met wat ze meemaakte en "
                  "ontdekte.", 4),
             ]),

        dict(kop="Identiteit en imago",
             opdracht="",
             oefeningen=[
                 ("kort", "Hoe noem je het beeld dat anderen van jou hebben?", "je imago", W),
                 ("open", "Iemand post enkel foto's waarop hij lacht met vrienden, terwijl hij zich vaak "
                          "eenzaam voelt. Leg uit met de woorden identiteit en imago wat hier gebeurt.",
                  "Zijn imago, het beeld dat anderen van hem krijgen, klopt niet met zijn identiteit, met wie "
                  "hij echt is. Hoe groter dat verschil wordt, hoe moeilijker het wordt om zichzelf te zijn.", 5),
                 ("waar", "Je imago en je identiteit zijn altijd hetzelfde.", False),
             ]),

        dict(kop="Groepsidentiteit",
             opdracht="",
             oefeningen=[
                 ("kort", "Hoe noem je een kleinere groep binnen de samenleving met een eigen stijl?",
                  "een subcultuur", WW),
                 ("waar", "Subculturen bestaan enkel bij jongeren.", False),
                 ("rij", [("je voelt dat je ergens bij hoort", "verbondenheid"),
                          ("je steunt iemand zonder er zelf iets bij te winnen", "solidariteit"),
                          ("je deelt de wereld op in wij en zij", "wij-zij-denken"),
                          ("je behandelt iemand slechter om wie hij is", "discriminatie")],
                  "Welk woord is dit?", WW),
                 ("open", "Noem twee gevolgen die wij-zij-denken kan hebben.",
                  "Twee van deze drie: mensen buiten de eigen groep worden sneller uitgesloten, vooroordelen "
                  "over de andere groep worden sterker, en de eigen groep voelt zich hechter.", 4),
                 ("open", "Een klas verkoopt wafels om de reis van een klasgenoot te betalen die het thuis "
                          "moeilijk heeft. Welk woord past hier, en waarom?",
                  "Solidariteit: de klas steunt iemand die het nodig heeft, zonder er zelf iets bij te winnen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-ik-leef-samen-met-anderen-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Ik leef samen met anderen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Kijken naar de speelplaats",
             opdracht="De prent hieronder is dezelfde als op het scherm, maar de vragen zijn andere. Kijk eerst rustig rond voor je begint te schrijven.",
             oefeningen=[
                 ("tekst", bundel.foto(PRENTEN / "ik-leef-samen-met-anderen-deel-1.webp", breedte="100%")),
                 ("kort", "Wat ligt er naast het meisje dat alleen op de bank zit?",
                  "haar rugzak en een drinkfles", WL),
                 ("kort", "Welke kleur heeft de bal waarmee de jongens links spelen?", "zwart-wit", W),
                 ("kort", "Wat hangt er rechtsboven aan het schoolgebouw?", "een basketbalring", WW),
                 ("kort", "Wat staat er achter de jongens die voetballen?",
                  "een overdekte fietsenstalling", WL),
                 ("open", "Tel hoeveel jongens er in het groepje in het midden staan, en schrijf van elk in "
                          "één woord wat hij doet.",
                  "Vijf jongens. Eén kijkt naar de grond, één wijst en lacht, twee lachen mee, en één legt "
                  "zijn hand op de schouder van de jongen die naar de grond kijkt.", 6),
                 ("open", "Er staat een meisje bij het groepje dat niet meelacht. Wat doet zij wél, en hoe "
                          "noemen we haar rol?",
                  "Ze staat erbij met haar armen gekruist en kijkt toe zonder iets te doen. Dat is de rol van "
                  "omstaander.", 4),
                 ("teken", "Stel dat jij op deze speelplaats staat. Zet met een kruisje op de prent hierboven "
                           "waar jij naartoe zou gaan, en schrijf hieronder waarom.",
                  "Elk antwoord is goed zolang je je keuze uitlegt. Wie naar de jongen in het midden of naar "
                  "het meisje op de bank gaat, kiest voor wie het op dit moment het moeilijkst heeft.", 30),
             ]),

        dict(kop="Plagen, pesten of een meningsverschil?",
             opdracht="Schrijf bij elke situatie welk woord past.",
             oefeningen=[
                 ("rij", [("twee vrienden lachen om beurten met elkaars kapsel", "plagen"),
                          ("dezelfde jongen krijgt elke dag een scheldnaam van dezelfde groep", "pesten"),
                          ("twee leerlingen zijn het oneens over een groepswerk en zeggen dat", "een meningsverschil")],
                  "Wat is dit?", WL),
                 ("open", "Noem twee verschillen tussen plagen en pesten.",
                  "Plagen gaat over en weer, pesten gaat maar één kant op. Pesten herhaalt zich en er is een "
                  "machtsverschil, bijvoorbeeld één tegen een groep. Bij plagen vinden allebei het nog leuk.", 5),
                 ("waar", "Iets dat heel vaak gebeurt, is daarom aanvaardbaar.", False),
             ]),

        dict(kop="Woorden bij samenleven",
             opdracht="",
             oefeningen=[
                 ("rij", [("je doet mee omdat de groep het doet", "groepsdruk"),
                          ("een trainer laat een speler nooit spelen omdat die hem tegensprak", "machtsmisbruik"),
                          ("iemand wordt bewust niet uitgenodigd", "uitsluiten"),
                          ("iemand wordt minder behandeld om zijn huidskleur", "racisme")],
                  "Welk woord is dit?", WW),
                 ("kort", "Hoeveel basisemoties zijn er, en welke?",
                  "vier: blijdschap, verdriet, angst en woede", WL),
                 ("open", "Wat is een mentale grens, en waarom ligt die niet bij iedereen even ver?",
                  "Het is de grens van wat je van binnen nog aankan. Iedereen heeft andere ervaringen en een "
                  "ander karakter, dus wat voor de ene een grap is, is voor de andere te veel.", 5),
             ]),

        dict(kop="Toestemming en samenwerken",
             opdracht="",
             oefeningen=[
                 ("open", "Noem de drie voorwaarden waaraan respectvol omgaan met elkaars lichaam moet voldoen.",
                  "Toestemming: allebei akkoord en allebei goed erbij. Vrijwillig: niemand zet de ander onder "
                  "druk. Gelijkwaardigheid: er is geen machtsverschil.", 5),
                 ("waar", "Een ja die iemand alleen zegt omdat hij niet durft te weigeren, telt als toestemming.",
                  False),
                 ("open", "Noem drie kenmerken van een goede samenwerking, en schrijf bij elk hoe je ze ziet.",
                  "Drie van deze: luisteren naar elkaar, om de beurt spreken, gepaste lichaamstaal, afspraken "
                  "nakomen, hulp vragen als iets niet duidelijk is, rekening houden met de inbreng van "
                  "anderen, duidelijk en rustig communiceren.", 6),
                 ("tabel", ["vorm van diversiteit", "waarover ze gaat"],
                  [["sociale diversiteit", None], ["culturele diversiteit", None],
                   ["religieuze diversiteit", None], ["seksuele diversiteit", None]],
                  "sociaal: opleiding, werk, inkomen, gezinssituatie · cultureel: taal, gewoontes, feesten, "
                  "eten · religieus: geloof of levensbeschouwing · seksueel: wie je aantrekkelijk vindt en "
                  "hoe je jezelf beleeft", "320px"),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-eerste-hulp-bij-ongevallen-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Eerste hulp bij ongevallen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
        "Kijk je antwoord altijd na op het antwoordblad: bij eerste hulp is bijna juist niet genoeg.",
        "Wat hier staat, volgt de richtlijnen van het Rode Kruis.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
    ],
    reeksen=[
        dict(kop="De vier stappen",
             opdracht="Zet de vier stappen in de juiste volgorde en vul aan.",
             oefeningen=[
                 ("tabel", ["stap", "wat je doet"],
                  [["1", None], ["2", None], ["3", None], ["4", None]],
                  "1: zorg voor veiligheid · 2: beoordeel de toestand van het slachtoffer · "
                  "3: raadpleeg gespecialiseerde hulp · 4: verleen verdere hulp", "300px"),
                 ("open", "Waarom staat veiligheid op de eerste plaats en niet op de tweede?",
                  "Omdat je niemand kan helpen als je zelf gewond raakt. Een tweede slachtoffer maakt de "
                  "situatie alleen erger.", 4),
                 ("kort", "Welk nummer bel je in België voor een ambulance of de brandweer?", "112", W),
                 ("open", "Noem drie dingen die je zeker vertelt als je 112 belt.",
                  "Waar het gebeurd is, zo precies mogelijk. Wat er gebeurd is en hoeveel slachtoffers er "
                  "zijn. In welke toestand het slachtoffer is.", 5),
                 ("waar", "Als je 112 gebeld hebt, leg jij als eerste neer.", False),
             ]),

        dict(kop="Wat doe je?",
             opdracht="Schrijf per situatie wat je als eerste doet.",
             oefeningen=[
                 ("open", "Een fietser is gevallen op een drukke straat en blijft liggen. Het verkeer rijdt "
                          "gewoon door. Wat doe je eerst, en waarom?",
                  "Eerst de plaats veilig maken, bijvoorbeeld met een gevarendriehoek of door het verkeer te "
                  "doen stoppen. Anders loop je zelf gevaar en kan er een tweede ongeval gebeuren.", 5),
                 ("open", "Je zus reageert niet als je haar aanspreekt en schudt, maar ze ademt rustig. Wat "
                          "doe je, in twee stappen?",
                  "Je legt haar in de stabiele zijligging en je belt 112. Daarna blijf je bij haar en "
                  "controleer je of ze blijft ademen.", 5),
                 ("open", "Waarom leg je een bewusteloos slachtoffer in stabiele zijligging?",
                  "Zodat de luchtweg vrij blijft en braaksel kan weglopen in plaats van in de luchtweg te "
                  "komen.", 4),
                 ("waar", "Een slachtoffer in stabiele zijligging mag je alleen laten om iets te gaan halen.",
                  False),
                 ("waar", "Iemand die niet reageert, mag je een slokje water geven.", False),
             ]),

        dict(kop="Verslikking",
             opdracht="",
             oefeningen=[
                 ("open", "Een vriend verslikt zich in een stuk appel en hoest luid en krachtig. Wat doe je?",
                  "Je moedigt hem aan om te blijven hoesten. Hoesten is de sterkste manier om iets weg te "
                  "krijgen; je slaat of duwt dan niet.", 4),
                 ("open", "Dezelfde vriend kan plots niet meer hoesten of spreken. Wat doe je nu?",
                  "Je wisselt rugslagen en buikstoten met elkaar af, en je laat iemand 112 bellen. Rugslagen "
                  "zijn stevige slagen met de hiel van je hand tussen de schouderbladen; een buikstoot is een "
                  "stevige ruk naar binnen en naar boven onder de ribben.", 6),
                 ("waar", "Bij een baby jonger dan één jaar geef je buikstoten.", False),
             ]),

        dict(kop="Wonden en gewrichten",
             opdracht="",
             oefeningen=[
                 ("rij", [("tien tot twintig minuten lauw stromend water", "een brandwonde"),
                          ("stevig drukken met een propere doek", "een hevige bloeding"),
                          ("spoelen, ontsmetten, afdekken", "een schaafwonde"),
                          ("rust, koelen, drukverband, hoog leggen", "een verstuiking")],
                  "Bij welk ongeval hoort dit?", WW),
                 ("waar", "Kleding die aan een brandwonde vastgekleefd zit, trek je er voorzichtig af.", False),
                 ("waar", "Een koelzak leg je met een doek ertussen op de huid.", True),
                 ("open", "Noem twee symptomen van een ernstige bloeding.",
                  "Twee van deze drie: bloed dat blijft doorstromen ondanks druk, een bleke en klamme huid, "
                  "en een slachtoffer dat duizelig wordt.", 4),
                 ("open", "Wat is het verschil tussen een verstuiking en een breuk, en wat doe je als je het "
                          "niet zeker weet?",
                  "Bij een verstuiking zijn de banden rond het gewricht gerekt, bij een breuk is het bot zelf "
                  "gebroken. Bij twijfel laat je het gewricht met rust en laat je het nakijken.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-democratie-en-dictatuur-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Democratie en dictatuur",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De drie machten",
             opdracht="Vul in: wetgevende, uitvoerende of rechterlijke macht.",
             oefeningen=[
                 ("tabel", ["macht", "wie oefent ze uit?", "wat doet ze?"],
                  [["wetgevende", None, None], ["uitvoerende", None, None], ["rechterlijke", None, None]],
                  "wetgevende: het parlement, maakt en stemt de wetten · uitvoerende: de regering, brengt de "
                  "wetten in de praktijk · rechterlijke: de rechters in de rechtbanken en hoven, spreken recht", "230px"),
                 ("rij", [("een minister", "uitvoerende macht"),
                          ("een volksvertegenwoordiger", "wetgevende macht"),
                          ("een rechter", "rechterlijke macht")],
                  "Bij welke macht hoort deze persoon?", WW),
                 ("open", "Waarom zijn de drie machten van elkaar gescheiden?",
                  "Zodat ze elkaar kunnen controleren en niemand alle macht krijgt. Een macht die zichzelf "
                  "controleert, controleert niets.", 4),
             ]),

        dict(kop="Welk principe wordt geschonden?",
             opdracht="Schrijf bij elke situatie welk principe van de democratische rechtsstaat in het gedrang komt.",
             oefeningen=[
                 ("open", "Een tv-zender mag van de regering niets meer uitzenden over een schandaal binnen "
                          "die regering.",
                  "De persvrijheid. De media moeten vrij kunnen berichten, ook en juist over de macht.", 3),
                 ("open", "De zoon van een minister wordt niet vervolgd voor een diefstal, terwijl een andere "
                          "jongere dat wel wordt.",
                  "De gelijkheid voor de wet. Dezelfde wet moet voor iedereen gelden, ook voor wie macht of "
                  "geld heeft.", 3),
                 ("open", "Een regering schaft de grondwet af en schrijft zelf nieuwe basisregels.",
                  "De aanwezigheid van een grondwet. Zonder hoogste wet is er niets meer dat de macht van de "
                  "regering begrenst.", 3),
                 ("open", "Bij de verkiezingen moet iedereen luidop zeggen op wie hij stemt.",
                  "De vrije verkiezingen. Vrij wil zeggen: zonder dwang en in het geheim. Wie luidop moet "
                  "stemmen, kan onder druk gezet worden.", 4),
             ]),

        dict(kop="Democratie of dictatuur?",
             opdracht="",
             oefeningen=[
                 ("waar", "In een dictatuur worden er soms verkiezingen gehouden.", True),
                 ("waar", "In een democratie mag je vreedzaam betogen tegen de regering.", True),
                 ("waar", "In België worden rechters verkozen door de bevolking.", False),
                 ("open", "Wat is volgens jou het grootste verschil tussen een democratie en een autoritair "
                          "regime? Leg uit in twee zinnen.",
                  "In een democratie wordt de macht gecontroleerd en kan ze wisselen: wie verliest, gaat weg. "
                  "In een autoritair regime houdt één persoon of groep de macht en is er geen echte controle.", 5),
             ]),

        dict(kop="Inspraak, rechten en plichten",
             opdracht="",
             oefeningen=[
                 ("rij", [("naar school gaan tot je achttien bent", "een plicht"),
                          ("je mening mogen uiten", "een recht"),
                          ("belastingen betalen", "een plicht"),
                          ("een eerlijk proces krijgen", "een recht")],
                  "Is dit een recht of een plicht?", WW),
                 ("waar", "Inspraak betekent dat jouw voorstel altijd wordt uitgevoerd.", False),
                 ("open", "Een jeugdhuis vraagt aan zijn leden welke activiteiten er moeten komen, kiest daarna "
                          "iets heel anders en legt niet uit waarom. Waarom was dit geen echte inspraak?",
                  "De mening van de leden werd gevraagd maar telde niet mee in de beslissing, en er kwam geen "
                  "uitleg. Dan was de inspraak maar schijn.", 5),
                 ("open", "Noem twee manieren waarop een jongere van veertien toch kan meewegen op "
                          "beslissingen.",
                  "Twee van deze: zich kandidaat stellen voor de leerlingenraad, meedoen aan een jeugdraad in "
                  "de gemeente, of zijn mening geven op een inspraakmoment.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-hoe-belgie-bestuurd-wordt-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Hoe België bestuurd wordt",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vier niveaus, twee organen",
             opdracht="Vul de tabel aan met de namen van de organen.",
             oefeningen=[
                 ("tabel", ["niveau", "de raad die beslist", "het bestuur dat uitvoert"],
                  [["de gemeente", None, None], ["de provincie", None, None],
                   ["Vlaanderen", None, None], ["federaal", None, None]],
                  "gemeente: de gemeenteraad en het college van burgemeester en schepenen · provincie: de "
                  "provincieraad en de deputatie · Vlaanderen: het Vlaams Parlement en de Vlaamse Regering · "
                  "federaal: het federale parlement en de federale regering", "230px"),
                 ("kort", "Hoeveel provincies telt België?", "tien", W),
                 ("kort", "In hoeveel provincies ligt het Brussels Hoofdstedelijk Gewest?",
                  "in geen enkele", WW),
                 ("waar", "De gouverneur van een provincie wordt verkozen.", False),
             ]),

        dict(kop="Naar welk niveau ga je?",
             opdracht="Schrijf bij elke vraag welk bestuursniveau ervoor bevoegd is.",
             oefeningen=[
                 ("rij", [("je huisvuil wordt niet opgehaald", "de gemeente"),
                          ("je diploma en je schooldoelen", "de gemeenschap"),
                          ("een nieuw natuurgebied", "het gewest"),
                          ("je pensioen later", "de federale overheid")],
                  "Welk niveau?", WW),
                 ("rij", [("een provinciaal domein onderhouden", "de provincie"),
                          ("het leger", "de federale overheid"),
                          ("een bouwvergunning aanvragen", "de gemeente"),
                          ("de bibliotheek in je dorp", "de gemeente")],
                  "Welk niveau?", WW),
                 ("open", "Je vraagt een nieuwe identiteitskaart aan. Waar ga je daarvoor, en welk niveau "
                          "beheert die gegevens?",
                  "Je gaat naar het gemeentehuis van je eigen gemeente. De identiteitsgegevens zelf worden "
                  "federaal beheerd.", 4),
             ]),

        dict(kop="Gemeenschap of gewest?",
             opdracht="Denk aan de vuistregel: gaat het over mensen en taal, of over de grond?",
             oefeningen=[
                 ("rij", [("cultuur", "gemeenschap"), ("wonen", "gewest"),
                          ("welzijn en gezondheidszorg", "gemeenschap"), ("milieu", "gewest")],
                  "Gemeenschap of gewest?", WW),
                 ("rij", [("media", "gemeenschap"), ("openbaar vervoer", "gewest"),
                          ("ruimtelijke ordening", "gewest"), ("onderwijs", "gemeenschap")],
                  "Gemeenschap of gewest?", WW),
                 ("kort", "Hoeveel gemeenschappen en hoeveel gewesten telt België?",
                  "drie en drie", WW),
                 ("kort", "Hoe heet de regelgeving die het Vlaams Parlement stemt?", "een decreet", WW),
                 ("waar", "Een decreet is minder sterk dan een federale wet.", False),
             ]),

        dict(kop="Wie doet wat?",
             opdracht="",
             oefeningen=[
                 ("waar", "Je stemt rechtstreeks op de persoon die burgemeester wordt.", False),
                 ("waar", "De koning is het staatshoofd, maar hij bestuurt het land niet zelf.", True),
                 ("open", "Leg uit waarom de federale overheid niets te zeggen heeft over het Vlaamse "
                          "onderwijs.",
                  "Onderwijs is een bevoegdheid van de gemeenschappen. Elk niveau heeft zijn eigen lijst "
                  "bevoegdheden en mag daarbuiten niets beslissen.", 4),
                 ("open", "Noem drie zaken die de federale overheid regelt.",
                  "Drie van deze: justitie en de rechtbanken, defensie en het leger, asiel en migratie, de "
                  "pensioenen, de sociale zekerheid, de buitenlandse handel.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-economische-kringloop-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="De economische kringloop",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Waar begint de stroom, en waar eindigt ze?",
             opdracht="Schrijf telkens: van welke speler naar welke speler. Kies uit gezin, bedrijf en overheid.",
             oefeningen=[
                 ("rij", [("je moeder betaalt de kapper", "van het gezin naar het bedrijf"),
                          ("de bakker geeft je het brood mee", "van het bedrijf naar het gezin"),
                          ("een bedrijf betaalt belasting op zijn winst", "van het bedrijf naar de overheid"),
                          ("de overheid stort een werkloosheidsuitkering", "van de overheid naar het gezin")],
                  "Van wie naar wie loopt deze stroom?", WL),
                 ("rij", [("je vader gaat elke dag werken", "van het gezin naar het bedrijf"),
                          ("de school krijgt geld voor nieuwe boeken", "van de overheid naar de school"),
                          ("een gezin betaalt belasting op zijn inkomen", "van het gezin naar de overheid")],
                  "Van wie naar wie loopt deze stroom?", WL),
                 ("open", "Leg uit waarom er bij een goederenstroom meestal een geldstroom in de andere "
                          "richting loopt.",
                  "Wie iets krijgt, betaalt er meestal voor. Het product gaat de ene kant op en het geld de "
                  "andere; daarom draait het als een kringloop rond.", 4),
                 ("waar", "De overheid hoort niet in de economische kringloop, want ze verkoopt niets.", False),
             ]),

        dict(kop="In het bedrijf",
             opdracht="Welke kernactiviteit of afdeling is dit?",
             oefeningen=[
                 ("rij", [("bestelt nieuwe grondstoffen", "de aankoop"),
                          ("bewaart de voorraad", "het magazijn"),
                          ("maakt de reclamecampagne", "de marketing"),
                          ("houdt de inkomsten en uitgaven bij", "de boekhouding")],
                  "Welke kernactiviteit is dit?", WW),
                 ("rij", [("neemt de grote beslissingen", "de algemene directie of zaakvoerder"),
                          ("ontvangt de bezoekers", "het onthaal"),
                          ("maakt het product", "de productie"),
                          ("brengt het product bij de klant", "de verkoop")],
                  "Welke kernactiviteit is dit?", WL),
                 ("waar", "In een eenmanszaak doet één persoon vaak meerdere kernactiviteiten tegelijk.", True),
             ]),

        dict(kop="De vier sectoren",
             opdracht="Schrijf bij elk bedrijf tot welke sector het behoort.",
             oefeningen=[
                 ("rij", [("een visser", "de primaire sector"),
                          ("een chocoladefabriek", "de secundaire sector"),
                          ("een verzekeringskantoor", "de tertiaire sector"),
                          ("een openbare bibliotheek", "de quartaire sector")],
                  "Welke sector?", WW),
                 ("rij", [("een aardappelboer", "de primaire sector"),
                          ("een bouwbedrijf", "de secundaire sector"),
                          ("een taxibedrijf", "de tertiaire sector"),
                          ("een woonzorgcentrum van de gemeente", "de quartaire sector")],
                  "Welke sector?", WW),
                 ("open", "Een boer verkoopt zijn melk aan een fabriek die er kaas van maakt. Die kaas ligt "
                          "daarna in de supermarkt. Noem voor elk van de drie de sector.",
                  "De boer: de primaire sector. De fabriek: de secundaire sector. De supermarkt: de tertiaire "
                  "sector.", 4),
             ]),

        dict(kop="Goederen, diensten en bedrijven",
             opdracht="",
             oefeningen=[
                 ("rij", [("de oven van een bakkerij", "een investeringsgoed"),
                          ("een fiets die jij koopt", "een consumentengoed"),
                          ("een treinrit", "een consumentendienst"),
                          ("de bestelwagen van een loodgieter", "een investeringsgoed")],
                  "Wat is dit?", WW),
                 ("rij", [("een supermarkt", "een handelsbedrijf"),
                          ("een meubelfabriek", "een productiebedrijf"),
                          ("een kapsalon", "een dienstenbedrijf")],
                  "Wat voor soort bedrijf is dit?", WW),
                 ("waar", "Een non-profitorganisatie mag geen personeel in dienst nemen.", False),
             ]),

        dict(kop="De inkomsten en uitgaven van een gezin",
             opdracht="",
             oefeningen=[
                 ("rij", [("het maandloon van je moeder", "terugkerend"),
                          ("de erfenis van een oudtante", "toevallig"),
                          ("het groeipakket", "terugkerend"),
                          ("de opbrengst van een rommelmarkt", "toevallig")],
                  "Terugkerend of toevallig inkomen?", WW),
                 ("rij", [("de huur van het appartement", "een vaste uitgave"),
                          ("de boodschappen van de week", "een variabele uitgave"),
                          ("de fiets die gestolen wordt", "een onvoorziene uitgave"),
                          ("een nieuwe zetel na tien jaar", "een uitzonderlijke uitgave")],
                  "Welke soort uitgave?", WL),
                 ("open", "Leg uit wat het verschil is tussen een onvoorziene en een uitzonderlijke uitgave.",
                  "Een onvoorziene uitgave zie je helemaal niet aankomen, zoals een wasmachine die stukgaat. "
                  "Een uitzonderlijke uitgave is groot en zeldzaam, maar je weet dat ze er ooit aankomt, dus "
                  "je kan ervoor sparen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-overheid-in-de-economie-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="De overheid in de economie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Inkomst of uitgave?",
             opdracht="Schrijf bij elk gegeven of het een inkomst of een uitgave van de overheid is, en welke.",
             oefeningen=[
                 ("rij", [("de btw op een paar schoenen", "een inkomst"),
                          ("het loon van een leerkracht", "een uitgave"),
                          ("de belasting op een bedrijfswinst", "een inkomst"),
                          ("de aanleg van een fietspad", "een uitgave")],
                  "Inkomst of uitgave?", WW),
                 ("rij", [("de politie betalen", "veiligheid"),
                          ("een sociale woonwijk vernieuwen", "huisvesting en infrastructuur"),
                          ("een bibliotheek ondersteunen", "recreatie, sport en cultuur"),
                          ("een natuurgebied beheren", "milieubescherming")],
                  "Onder welke uitgave valt dit?", WL),
                 ("kort", "Welke belasting betaal je elk jaar omdat je een auto hebt?",
                  "de wegenbelasting", WW),
                 ("waar", "Het btw-tarief is op alle producten hetzelfde.", False),
             ]),

        dict(kop="Rekenen met de cijfers van de overheid",
             opdracht="Schrijf de bewerking op en zet de eenheid erbij.",
             oefeningen=[
                 ("kort", "Een gemeente ontvangt 12 miljoen euro en geeft 15 miljoen euro uit. Hoe groot is "
                          "het tekort?", "3 miljoen euro", WW),
                 ("kort", "Van elke 100 euro gaat er 25 euro naar sociale bescherming. Hoeveel procent is dat?",
                  "25 procent", W),
                 ("kort", "Een overheid geeft 200 miljoen euro uit, waarvan 40 miljoen aan veiligheid. "
                          "Hoeveel procent is dat?", "20 procent", W),
                 ("open", "Wat gebeurt er als een overheid jaar na jaar meer uitgeeft dan ze ontvangt?",
                  "Ze moet lenen, haar schuld groeit, en op die schuld betaalt ze rente. Dat rentegeld kan ze "
                  "daarna niet meer aan iets anders besteden.", 5),
             ]),

        dict(kop="Sociale ongelijkheid",
             opdracht="",
             oefeningen=[
                 ("rij", [("iemand krijgt geen job om zijn afkomst", "discriminatie"),
                          ("een kind heeft thuis geen rustige plek om te werken", "onderwijs en kansen om te leren"),
                          ("iemand is al jaren chronisch ziek", "gezondheid"),
                          ("een gezin kan geen sportclub betalen", "inkomen en rijkdom")],
                  "Welke oorzaak van sociale ongelijkheid?", WL),
                 ("open", "Leg in je eigen woorden uit wat sociale ongelijkheid is.",
                  "Dat mensen in een samenleving niet dezelfde kansen en middelen hebben, bijvoorbeeld in "
                  "inkomen, gezondheid, opleiding of macht.", 4),
                 ("waar", "Ook de wetten en regels van een overheid kunnen sociale ongelijkheid veroorzaken.",
                  True),
             ]),

        dict(kop="De sociale zekerheid",
             opdracht="Schrijf bij elke uitkering of ze aanvullend of vervangend is.",
             oefeningen=[
                 ("rij", [("het rustpensioen", "een vervangingsuitkering"),
                          ("het groeipakket", "een aanvullende uitkering"),
                          ("de ziekte-uitkering", "een vervangingsuitkering"),
                          ("een sociaal tarief voor elektriciteit", "een aanvullende uitkering")],
                  "Aanvullend of vervangend?", WL),
                 ("rij", [("het leefloon", "een vervangingsuitkering"),
                          ("de tegemoetkoming voor medische kosten", "een aanvullende uitkering"),
                          ("de arbeidsongevallenuitkering", "een vervangingsuitkering")],
                  "Aanvullend of vervangend?", WL),
                 ("open", "Leg het solidariteitsprincipe van de sociale zekerheid uit in twee zinnen.",
                  "Wie kan, draagt bij; wie het nodig heeft, wordt geholpen. Je krijgt dus niet per se terug "
                  "wat je zelf betaalde, en dat is precies de bedoeling.", 5),
                 ("waar", "De sociale zekerheid wordt volledig door de overheid alleen betaald.", False),
                 ("open", "Noem twee manieren waarop de overheid sociale ongelijkheid kleiner maakt.",
                  "Twee van deze: uitkeringen voor wie zijn inkomen verliest, onderwijs dat voor iedereen "
                  "toegankelijk is, en sociale tarieven voor wie weinig verdient.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-ik-beheer-mijn-financien-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Ik beheer mijn financiën",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Reëel of gecreëerd?",
             opdracht="Schrijf bij elke behoefte of ze reëel of gecreëerd is.",
             oefeningen=[
                 ("rij", [("schoenen die passen", "reëel"),
                          ("de nieuwste gsm terwijl de jouwe werkt", "gecreëerd"),
                          ("een dak boven je hoofd", "reëel"),
                          ("hetzelfde jasje als je vriendin", "gecreëerd")],
                  "Reële of gecreëerde behoefte?", WW),
                 ("open", "Noem drie dingen die je koopgedrag kunnen beïnvloeden.",
                  "Drie van deze: reclame en influencers, wat je vrienden hebben of vinden, een korting of "
                  "een aanbod dat bijna stopt, het merk, de verpakking, je gewoonte, je humeur.", 4),
                 ("open", "Een webshop toont een aftellende klok van vijf minuten bij een aanbod. Wat wil de "
                          "verkoper daarmee bereiken?",
                  "Hij wil je onder tijdsdruk zetten zodat je snel beslist en niet meer nadenkt of je het "
                  "product echt nodig hebt.", 4),
             ]),

        dict(kop="Budget en sparen",
             opdracht="Schrijf de bewerking op.",
             oefeningen=[
                 ("kort", "Je krijgt 60 euro per maand en geeft er 38 euro van uit. Hoeveel spaar je?",
                  "22 euro", W),
                 ("kort", "Je wil een spelconsole van 240 euro en spaart 20 euro per maand. Hoeveel maanden "
                          "duurt dat?", "twaalf maanden", WW),
                 ("kort", "Je spaart 15 euro per maand. Hoeveel heb je na anderhalf jaar?", "270 euro", W),
                 ("open", "Waarom is het verstandig om ook te sparen als je niets bepaalds wil kopen?",
                  "Dan heb je een buffer voor onvoorziene uitgaven, zoals een fiets die stuk is. Zonder buffer "
                  "moet je daarvoor lenen, en lenen kost rente.", 5),
             ]),

        dict(kop="Lenen",
             opdracht="",
             oefeningen=[
                 ("kort", "Je leent 2000 euro en betaalt in totaal 2300 euro terug. Wat is de totale rente?",
                  "300 euro", W),
                 ("kort", "Je leende 1200 euro en hebt er al 800 euro van afbetaald. Hoe groot is de nog "
                          "openstaande schuld?", "400 euro", W),
                 ("rij", [("hoelang je erover doet", "de looptijd"),
                          ("het percentage dat het lenen kost", "de rentevoet"),
                          ("wat je elke maand overmaakt", "het maandelijks afbetalingsbedrag"),
                          ("het geleende bedrag plus de totale rente", "de totale terugbetaling")],
                  "Welk onderdeel van een lening is dit?", WL),
                 ("waar", "Een lening met een langere looptijd kost in totaal meestal meer.", True),
                 ("open", "Noem twee risico's van te veel lenen.",
                  "Twee van deze: je kan je afbetalingen niet meer volgen, je betaalt steeds meer rente, en je "
                  "kan in een schuldenspiraal terechtkomen waarbij je leent om af te betalen.", 4),
             ]),

        dict(kop="Waar en waarmee je betaalt",
             opdracht="",
             oefeningen=[
                 ("rij", [("je zet er eerst geld op", "de prepaidkaart"),
                          ("het geld gaat meteen van je rekening", "de debetkaart"),
                          ("je betaalt pas later", "de kredietkaart"),
                          ("je stuurt het geld zelf weg", "de overschrijving")],
                  "Welk betaalmiddel is dit?", WW),
                 ("kort", "Hoeveel dagen bedenktijd heb je in principe bij een online aankoop?",
                  "veertien dagen", WW),
                 ("open", "Noem drie dingen waaraan je kan zien of een onbekende webshop betrouwbaar is.",
                  "Drie van deze: er staat een adres en een telefoonnummer op de site, de prijs is niet "
                  "verdacht veel lager dan elders, en het webadres begint met https en is juist gespeld.", 5),
                 ("waar", "Een particulier die op sociale media iets verkoopt, geeft je dezelfde garantie als "
                          "een winkel.", False),
             ]),

        dict(kop="Fraude",
             opdracht="",
             oefeningen=[
                 ("open", "Je krijgt een sms dat je bankkaart geblokkeerd is en dat je via een link je "
                          "gegevens moet bevestigen. Wat doe je, en wat doe je zeker niet?",
                  "Je klikt zeker niet op de link en je vult nergens je gegevens in. Je contacteert zelf je "
                  "bank, via de app of het telefoonnummer dat je al kende.", 5),
                 ("open", "Noem twee signalen waaraan je bedrog bij een betaling herkent.",
                  "Twee van deze: je moet betalen buiten het systeem van de website om, er wordt haast op "
                  "gezet, of er wordt naar je pincode of je codes gevraagd.", 4),
                 ("open", "Er is geld van je rekening verdwenen. Schrijf in de juiste volgorde op wat je doet.",
                  "Eerst je kaart laten blokkeren, dan je bank verwittigen, en daarna aangifte doen bij de "
                  "politie. Zonder aangifte kan je bank je meestal niet vergoeden.", 5),
                 ("waar", "Aangifte doen bij de politie na fraude is zinloos.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-digitaal-communiceren-en-bestanden-beheren-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Digitaal communiceren en bestanden beheren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke vorm van digitaal communiceren?",
             opdracht="",
             oefeningen=[
                 ("rij", [("je stelt een vraag en anderen antwoorden eronder, per onderwerp", "een forum"),
                          ("iemand schrijft er zijn eigen stukken op", "een blogwebsite"),
                          ("je vergadert met beeld en geluid", "een online meeting"),
                          ("korte berichtjes met een snel antwoord", "chatten")],
                  "Wat is dit?", WW),
                 ("open", "Wanneer kies je een e-mail en niet een chatbericht? Noem twee redenen.",
                  "Als je iets formeel wil vragen, en als het bijgehouden moet worden. Een mail kan ook "
                  "bijlagen meenemen.", 4),
             ]),

        dict(kop="Een e-mail schrijven",
             opdracht="Schrijf hieronder een korte mail aan je titularis om te vragen of je je taak een dag later mag indienen.",
             oefeningen=[
                 ("open", "Onderwerpregel:", "Kort en concreet, bijvoorbeeld: uitstel taak aardrijkskunde.", 1),
                 ("open", "Aanhef:", "Geachte mevrouw of Geachte meneer, of Beste met de naam erbij.", 1),
                 ("open", "Inhoud: schrijf je vraag in twee of drie zinnen.",
                  "Zeg wie je bent en over welke taak het gaat, vraag het uitstel, en geef kort je reden.", 5),
                 ("open", "Slotgroet en ondertekening:",
                  "Met vriendelijke groeten, en daaronder je voornaam en je familienaam, eventueel met je "
                  "klas erbij.", 2),
                 ("kort", "In welk veld zet je iemand zodat de andere ontvangers zijn adres niet zien?",
                  "BCC", W),
                 ("waar", "Een bericht volledig in hoofdletters typen wordt gelezen als roepen.", True),
             ]),

        dict(kop="Netjes online",
             opdracht="",
             oefeningen=[
                 ("waar", "In een videogesprek zet je je microfoon uit als je niet spreekt.", True),
                 ("waar", "Je mag een foto van een klasgenoot online zetten zonder het te vragen.", False),
                 ("open", "Je bent kwaad over een bericht in de klasgroep. Waarom is het beter om even te "
                          "wachten met antwoorden?",
                  "Een bericht dat je uit kwaadheid stuurt, blijft staan en kan doorgestuurd worden. Na een "
                  "tijdje schrijf je meestal iets anders, en meestal iets beters.", 5),
                 ("open", "Noem twee dingen die je doet vóór een online meeting begint.",
                  "Twee van deze: je camera en microfoon testen, een rustige plek en een neutrale achtergrond "
                  "kiezen, en enkele minuten vroeger inloggen.", 4),
             ]),

        dict(kop="Mappen en bestanden",
             opdracht="",
             oefeningen=[
                 ("rij", [("de boomstructuur van je schijven en mappen", "het navigatievenster"),
                          ("de gegevens van het bestand dat je koos", "het detailvenster"),
                          ("het programma waarin je alles beheert", "de verkenner")],
                  "Welk onderdeel is dit?", WW),
                 ("rij", [(".docx", "een Word-document"), (".xlsx", "een Excel-rekenblad"),
                          (".pdf", "een pdf"), (".jpg", "een foto")],
                  "Wat voor bestand is dit?", WW),
                 ("waar", "Bij kopiëren blijft het origineel staan, bij verplaatsen niet.", True),
                 ("waar", "Een bestand herbenoemen verandert ook de inhoud.", False),
                 ("open", "Bedenk een logische mappenstructuur van drie lagen voor je schoolwerk, en schrijf "
                          "ze op.",
                  "Elk antwoord is goed zolang het van algemeen naar specifiek gaat, bijvoorbeeld School, dan "
                  "het vak, dan het schooljaar of het thema.", 4),
                 ("open", "Waarom schrijf je een datum in een bestandsnaam best als 2027-03-08 en niet als "
                          "8-3-2027?",
                  "Met jaar-maand-dag sorteren je bestanden vanzelf op chronologische volgorde. Met de dag "
                  "vooraan loopt die volgorde door elkaar.", 4),
             ]),

        dict(kop="Uploaden, downloaden en een back-up",
             opdracht="",
             oefeningen=[
                 ("rij", [("je zet je taak op het leerplatform", "uploaden"),
                          ("je haalt een werkblad van de schoolsite", "downloaden"),
                          ("je zet je foto's op een externe schijf", "een back-up maken")],
                  "Wat doe je?", WW),
                 ("waar", "Een reservekopie op dezelfde computer als het origineel beschermt je even goed.",
                  False),
                 ("open", "Noem twee voordelen en één nadeel van cloudopslag.",
                  "Voordelen: je geraakt aan je bestanden van op elk toestel, ze blijven bestaan als je laptop "
                  "stukgaat, en je kan een map delen. Nadeel: zonder internetverbinding geraak je er niet aan.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-word-excel-powerpoint-en-veilig-online-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Word, Excel, PowerPoint en veilig online",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Word: welke soort opmaak?",
             opdracht="Schrijf bij elk gegeven: tekenopmaak, alineaopmaak of paginaopmaak.",
             oefeningen=[
                 ("rij", [("cursief", "tekenopmaak"), ("de regelafstand", "alineaopmaak"),
                          ("de marges", "paginaopmaak"), ("de tekstkleur", "tekenopmaak")],
                  "Welke soort opmaak?", WW),
                 ("rij", [("inspringen", "alineaopmaak"), ("de afdrukstand", "paginaopmaak"),
                          ("doorhalen", "tekenopmaak"), ("de uitlijning", "alineaopmaak")],
                  "Welke soort opmaak?", WW),
                 ("kort", "Welke tekenopmaak gebruik je voor de 2 in m2, dus kleiner en hoger?",
                  "superscript", WW),
                 ("open", "Leg uit wat het verschil is tussen een koptekst en een voettekst.",
                  "Een koptekst staat bovenaan elke pagina, een voettekst onderaan. Allebei worden ze op elke "
                  "pagina herhaald.", 3),
                 ("waar", "Een alinea eindigt waar je op Enter duwt.", True),
                 ("open", "Waarom stuur je een afgewerkt document best door als pdf?",
                  "Dan blijft de opmaak bij iedereen hetzelfde en kan niemand er zomaar iets in veranderen.", 3),
             ]),

        dict(kop="Excel",
             opdracht="",
             oefeningen=[
                 ("rij", [("één vakje", "een cel"), ("A1 tot A10", "een bereik"),
                          ("één tabblad onderaan", "een werkblad"), ("het bestand zelf", "een werkmap")],
                  "Wat is dit?", WW),
                 ("kort", "Hoe schrijf je het celadres van de cel in kolom D en rij 7?", "D7", W),
                 ("kort", "Met welke formule tel je alles van B2 tot B12 op?", "=SOM(B2:B12)", WW),
                 ("kort", "Met welk teken vermenigvuldig je in Excel?", "het sterretje", WW),
                 ("waar", "Een formule in Excel begint altijd met een gelijkheidsteken.", True),
                 ("open", "Noem drie getalnotaties die je aan een cel kan geven.",
                  "Drie van deze: valuta, percentage, een aantal decimalen, of datum en tijd.", 3),
             ]),

        dict(kop="PowerPoint",
             opdracht="",
             oefeningen=[
                 ("open", "Schrijf de drie regels van het KISS-principe op.",
                  "Maximaal zeven regels per dia, maximaal zeven woorden per regel, en een duidelijk leesbaar "
                  "lettertype van meestal 14 punt.", 4),
                 ("open", "Waarom zet je niet je hele tekst op een dia, ook al vergeet je dan niets?",
                  "Dan begint je publiek te lezen in plaats van te luisteren. Op de dia staan steekwoorden; de "
                  "uitleg komt van jou.", 4),
             ]),

        dict(kop="Ongepast gedrag op het internet",
             opdracht="Schrijf bij elke omschrijving het juiste woord.",
             oefeningen=[
                 ("rij", [("iemands adres en telefoonnummer online zetten", "doxing"),
                          ("iemand publiek vernederen", "shaming"),
                          ("privéberichten van iemand rondsturen", "exposing"),
                          ("vals nieuws als echt verspreiden", "fake news")],
                  "Welk woord is dit?", WW),
                 ("rij", [("iemand collectief uitsluiten na een uitspraak", "canceling"),
                          ("een volwassene die online het vertrouwen van een kind zoekt", "grooming"),
                          ("berichten die aanzetten tot haat", "haatberichten")],
                  "Welk woord is dit?", WW),
                 ("open", "Iemand die je alleen online kent, vraagt je om een foto van jezelf in ondergoed en "
                          "belooft dat niemand ze te zien krijgt. Wat doe je, in drie stappen?",
                  "Niet sturen. Het gesprek stoppen en die persoon blokkeren. Het vertellen aan een volwassene "
                  "die je vertrouwt. Zo'n belofte kan niemand houden.", 5),
                 ("waar", "Een intieme foto van iemand anders doorsturen is strafbaar, ook als je die zelf "
                          "gekregen hebt.", True),
                 ("open", "Iemand stuurt je al een week kwetsende berichten. Wat doe je, en waarom neem je "
                          "eerst een schermafdruk?",
                  "Je maakt een schermafdruk als bewijs, want de berichten kunnen verdwijnen. Daarna meld je "
                  "het bij het platform en vertel je het aan een volwassene die je vertrouwt.", 5),
             ]),

        dict(kop="Internetfraude en wachtwoorden",
             opdracht="",
             oefeningen=[
                 ("rij", [("via een e-mail", "phishing"), ("via een sms", "smishing"),
                          ("via een QR-code", "quishing"), ("via een telefoongesprek", "vishing")],
                  "Hoe heet deze vorm van internetfraude?", WW),
                 ("open", "Iemand belt je op en zegt dat hij van je bank is en je code nodig heeft. Wat doe je?",
                  "Je geeft nooit een code door aan de telefoon. Je legt op en belt zelf terug naar een nummer "
                  "van de bank dat je al kende.", 4),
                 ("open", "Schrijf de zes regels van een sterk wachtwoord op.",
                  "Minstens 8 karakters lang, maximaal 24 karakters lang, minstens één hoofdletter, minstens "
                  "één kleine letter, minstens één cijfer, en minstens één teken.", 6),
                 ("rij", [("zomer2027", "te zwak: geen hoofdletter en geen teken"),
                          ("Fiets!7roos", "sterk genoeg"),
                          ("ABCDEFGH", "te zwak: geen kleine letter, geen cijfer, geen teken")],
                  "Voldoet dit wachtwoord aan de regels?", WL),
                 ("open", "Wat is tweestapsverificatie, en waarom is ze zo sterk?",
                  "Naast je wachtwoord geef je nog een tweede bewijs, zoals een code op je gsm. Zelfs wie je "
                  "wachtwoord kent, geraakt er dan niet in zonder je toestel.", 5),
             ]),
    ],
)
