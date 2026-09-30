# -*- coding: utf-8 -*-
"""De vragen voor "Van Rome naar de Franken" (🚀 Boost doorstroom, geschiedenis).

Uit de vakfiche, leerinhouden middeleeuwen, westerse samenleving: de
vroegmiddeleeuwse samenleving met de Germaanse volksverhuizingen, het einde van
het West-Romeinse Rijk, de versmelting van Germaanse, Romeinse en christelijke
gewoonten, en daarna de Franken: ontstaan, groei en versnippering van hun rijk,
de evolutie van de koninklijke macht bij Merovingers en Karolingers, het
Frankische erfrecht, verdeeldheid en eenheid, de band tussen politiek en
godsdienst, en de culturele heropleving aan het hof.

Deel 1 gaat over het einde van Rome en de migraties. Deel 2 over de twee
Frankische dynastieën.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke oorzaken van de Germaanse migraties waren extern, dus van buiten de Germaanse wereld?",
        opties=[
            "de druk van de Hunnen uit het oosten",
            "de rijkdom en het klimaat van het Romeinse rijk als aantrekkingskracht",
            "de verzwakte grensverdediging van Rome",
            "de groei van de Germaanse bevolking",
        ],
        antwoord=[0, 1, 2],
        uitleg="De bevolkingsgroei kwam uit de Germaanse samenlevingen zelf en is dus een interne oorzaak. De drie andere lagen buiten hun invloed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt bedoeld met interne oorzaken van de Germaanse migraties?",
        opties=[
            "redenen binnen de Germaanse samenlevingen zelf, zoals bevolkingsgroei en gebrek aan landbouwgrond",
            "oorlogen die binnen het Romeinse Rijk gevoerd werden tussen keizers en tegenkeizers onderling",
            "de verplaatsing van de hoofdstad van het Romeinse Rijk van Rome naar Constantinopel",
            "beslissingen van de Romeinse keizer over wie er binnen de grenzen mocht komen wonen",
        ],
        antwoord=0,
        uitleg="Intern en extern gaan over het gezichtspunt: intern is wat binnen de groep zelf speelde.",
    ),
    dict(
        type="invultekst",
        vraag="In welk jaar valt volgens de symbolische datering het West-Romeinse Rijk?",
        antwoord="476",
        uitleg="In 476 zet Odoaker de laatste West-Romeinse keizer af. Het is een afgesproken markering, geen dag waarop alles veranderde.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Oost-Romeinse Rijk viel samen met het West-Romeinse Rijk.",
        antwoord=False,
        uitleg="Het Oost-Romeinse of Byzantijnse Rijk bleef nog bijna duizend jaar bestaan, tot de val van Constantinopel in 1453.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemen historici de val van Rome liever een proces dan een gebeurtenis?",
        opties=[
            "omdat het gezag over meer dan een eeuw stukje bij beetje wegviel",
            "omdat er uit die jaren geen enkele geschreven bron bewaard gebleven is",
            "omdat niemand vandaag nog weet wanneer het precies gebeurd is",
            "omdat de Romeinen het in hun eigen geschriften ook al zo noemden",
        ],
        antwoord=0,
        uitleg="Belastingen, legers en bestuur verdwenen geleidelijk. Het jaartal 476 vat dat samen, maar vertelt het niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie tradities versmelten in de vroege middeleeuwen tot één nieuwe cultuur?",
        opties=[
            "de Germaanse, de Romeinse en de christelijke",
            "de Griekse, de Romeinse en de Arabische",
            "de Keltische, de Germaanse en de Byzantijnse",
            "de christelijke, de joodse en de islamitische",
        ],
        antwoord=0,
        uitleg="Germaans gewoonterecht, Romeins bestuur en schrift, en het christelijke geloof groeien samen tot de basis van middeleeuws West-Europa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke Romeinse erfenis blijft in de vroege middeleeuwen doorwerken?",
        opties=[
            "het Latijn als taal van kerk en bestuur",
            "het wegennet",
            "de indeling in bisdommen naar Romeinse steden",
            "het gekozen keizerschap door het volk",
        ],
        antwoord=[0, 1, 2],
        uitleg="De Romeinse keizer werd niet door het volk gekozen, dus dat kon ook niet doorleven. De drie andere zijn wel blijvende sporen.",
    ),
    dict(
        type="waarofniet",
        vraag="Na de val van Rome viel West-Europa uiteen in kleinere, zwak bestuurde koninkrijken.",
        antwoord=True,
        uitleg="Dat uiteenvallen is juist het kenmerk van de vroege middeleeuwen. Pas met Karel de Grote komt er even weer eenheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Migratie is in deze periode zowel een sociaal als een politiek verschijnsel.",
        antwoord=True,
        uitleg="Ze verandert wie waar woont en tot welke groep men behoort, en ze verandert wie er heerst. Dus beide domeinen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar wonen de Franken oorspronkelijk?",
        opties=[
            "langs de benedenloop van de Rijn",
            "in Noord-Afrika",
            "op het Iberisch schiereiland",
            "in Zuid-Italië",
        ],
        antwoord=0,
        uitleg="Vanuit het Rijngebied breiden ze zuidwaarts uit over Gallië, het latere Frankrijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke dynastie regeert als eerste over het Frankische rijk?",
        opties=[
            "de Merovingers",
            "de Karolingers",
            "de Capetingers",
            "de Ottonen",
        ],
        antwoord=0,
        uitleg="De Merovingers komen eerst, met Clovis als bekendste koning. De Karolingers nemen het later over.",
    ),
    dict(
        type="invultekst",
        vraag="Welke Frankische koning laat zich rond 500 dopen en bindt zo zijn macht aan de katholieke Kerk?",
        antwoord="Clovis",
        uitleg="Door katholiek te worden, en niet ariaans zoals andere Germaanse koningen, krijgt Clovis de steun van de Gallo-Romeinse bevolking en van de bisschoppen.",
    ),
    dict(
        type="waarofniet",
        vraag="De doop van Clovis had enkel gevolgen op godsdienstig vlak.",
        antwoord=False,
        uitleg="Ze was ook een politieke zet: ze leverde hem de steun van de bisschoppen en van de katholieke bevolking van Gallië op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat houdt het Frankische erfrecht in?",
        opties=[
            "het rijk wordt bij de dood van de koning onder zijn zonen verdeeld",
            "de oudste zoon erft het hele rijk, zijn broers krijgen niets",
            "de adel kiest na elke koning zelf wie de volgende wordt",
            "het rijk gaat bij de dood van de koning naar de Kerk over",
        ],
        antwoord=0,
        uitleg="Het rijk was persoonlijk bezit van de koning, en bezit verdeel je onder je kinderen. Dat is de kern van het probleem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gevolg had dat erfrecht voor de koninklijke macht?",
        opties=[
            "het rijk viel telkens opnieuw uiteen in kleinere delen",
            "de koning werd bij elke nieuwe generatie machtiger dan zijn vader",
            "de Kerk kreeg het bestuur van het hele rijk stilaan in handen",
            "het rijk bleef eeuwenlang precies even groot en even sterk",
        ],
        antwoord=0,
        uitleg="Elke verdeling verzwakte het geheel, en de delen vochten elkaar aan. Eenheid en verdeeldheid wisselden elkaar daardoor voortdurend af.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de Franken wisselden periodes van eenheid en verdeeldheid elkaar af.",
        antwoord=True,
        uitleg="Telkens als één koning alle delen in handen kreeg, was er even eenheid; bij zijn dood begon de verdeling opnieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men de laatste Merovingische koningen?",
        opties=[
            "de vadsige koningen, omdat de echte macht bij de hofmeiers lag",
            "de heilige koningen, omdat ze allemaal heilig verklaard werden",
            "de boerenkoningen, omdat ze zelf het land bewerkten",
            "de zeekoningen, omdat ze een vloot bouwden",
        ],
        antwoord=0,
        uitleg="De bijnaam komt uit latere bronnen, geschreven door aanhangers van de Karolingers. Dat maakt hem meteen een mooi voorbeeld van standplaatsgebondenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was een hofmeier?",
        opties=[
            "de hoogste ambtenaar aan het hof, die in naam van de koning bestuurde",
            "de bisschop van de hoofdstad, die de koning moest kronen",
            "een boer die het koninklijke domein bewerkte en de opbrengst afgaf",
            "de aanvoerder van de troepen die de paus in Rome beschermden",
        ],
        antwoord=0,
        uitleg="Wie die functie bekleedde, hield het leger en het bestuur in handen. De Karolingers klommen langs die weg naar de troon.",
    ),
    dict(
        type="waarofniet",
        vraag="De Germaanse migraties verliepen overal en altijd gewelddadig.",
        antwoord=False,
        uitleg="Sommige groepen vestigden zich als bondgenoot of als soldaat binnen het rijk. Andere kwamen wel met geweld binnen. Het beeld hangt af van de bron die je leest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat de Franken een gemengde samenleving vormden?",
        opties=[
            "Germaanse en Gallo-Romeinse gewoonten bestonden naast elkaar en vermengden zich",
            "iedereen in het rijk sprak vanaf het begin één en dezelfde taal",
            "er woonden van elke bevolkingsgroep precies evenveel mensen in het rijk",
            "de koning was zelf half Romein en half Frank, van vaders- en moederszijde",
        ],
        antwoord=0,
        uitleg="In het zuiden bleef veel Romeins, in het noorden overwoog het Germaanse. De versmelting verliep niet overal even ver.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke dynastie volgt de Merovingers op?",
        opties=[
            "de Karolingers",
            "de Capetingers",
            "de Habsburgers",
            "de Ottonen",
        ],
        antwoord=0,
        uitleg="Pepijn de Korte, hofmeier en zoon van Karel Martel, laat zich in 751 tot koning kronen. Zijn familie heet naar zijn zoon Karel de Grote.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom liet Pepijn de Korte zich door de paus zalven?",
        opties=[
            "om zijn machtsovername godsdienstig te laten bevestigen",
            "omdat de wet van de Franken dat bij elke kroning voorschreef",
            "omdat hij naast koning ook zelf priester wilde worden",
            "omdat de Merovingers voor hem dat ook altijd zo gedaan hadden",
        ],
        antwoord=0,
        uitleg="Hij greep de macht van een andere familie af. De zalving maakte van die greep een door God gewilde daad. Politiek en godsdienst versterken elkaar hier.",
    ),
    dict(
        type="invultekst",
        vraag="In welk jaar wordt Karel de Grote tot keizer gekroond?",
        antwoord="800",
        uitleg="Op kerstdag van het jaar 800 kroont paus Leo III hem in Rome. Daarmee komt de keizerstitel terug naar het westen.",
    ),
    dict(
        type="waarofniet",
        vraag="De keizerskroning van Karel de Grote versterkte de band tussen de Frankische macht en de Kerk.",
        antwoord=True,
        uitleg="De paus gaf gezag aan de keizer, en de keizer gaf bescherming aan de paus. Die wederzijdse afhankelijkheid werkt eeuwen door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe hield Karel de Grote toezicht op zijn uitgestrekte rijk?",
        opties=[
            "met graven die een gouw bestuurden",
            "met rondreizende controleurs, de missi dominici",
            "met wetten en richtlijnen die hij liet opschrijven",
            "met een vast parlement dat de wetten stemde",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een gekozen parlement bestond nog niet. De drie andere zijn wel de middelen waarmee hij bestuurde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was een gouw?",
        opties=[
            "een bestuurlijk gebied onder leiding van een graaf",
            "een belasting op alle handel binnen het rijk",
            "een kloosterorde met een eigen regel en eigen kloosters",
            "een soort wapen dat de Frankische ruiters gebruikten",
        ],
        antwoord=0,
        uitleg="De graaf sprak er recht, inde er de belastingen en riep er het leger op. Hij deed dat in naam van de koning.",
    ),
    dict(
        type="waarofniet",
        vraag="De graven bleven altijd trouwe uitvoerders van de koninklijke wil.",
        antwoord=False,
        uitleg="Naarmate het centrale gezag verzwakte, gingen graven hun gebied als eigen bezit beschouwen en hun ambt aan hun kinderen doorgeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt bedoeld met de culturele heropleving aan het Frankische hof?",
        opties=[
            "de school aan het hof in Aken, de kopieerwerkplaatsen en het nieuwe, leesbare schrift",
            "de bouw van grote gotische kathedralen met spitsbogen in alle steden van het rijk",
            "de uitvinding van de boekdrukkunst met losse letters, waardoor boeken goedkoper werden",
            "de heropening van de Romeinse theaters en badhuizen in de steden van Gallië",
        ],
        antwoord=0,
        uitleg="Men noemt dat de Karolingische renaissance. De gotiek en de drukkunst komen veel later.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stad was de hoofdplaats van Karel de Grote?",
        antwoord="Aken",
        uitleg="Daar bouwde hij zijn paleis en zijn paltskapel, en daar stond de hofschool.",
    ),
    dict(
        type="waarofniet",
        vraag="De Karolingische renaissance bereikte de gewone boerenbevolking nauwelijks.",
        antwoord=True,
        uitleg="Lezen en schrijven bleven het werk van een kleine groep geestelijken en hovelingen. Op het platteland veranderde er weinig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er bij het Verdrag van Verdun in 843?",
        opties=[
            "het rijk werd onder drie kleinzonen van Karel de Grote verdeeld",
            "de Franken sloten een blijvende vrede met de Arabieren in Spanje",
            "de paus kreeg het bestuur over het hele Frankische rijk in handen",
            "de keizerstitel werd afgeschaft en nooit meer aan iemand gegeven",
        ],
        antwoord=0,
        uitleg="Lodewijk de Vrome liet drie zonen na, en het Frankische erfrecht deed de rest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Is het Verdrag van Verdun een voorbeeld van eenheid of van verdeeldheid?",
        opties=[
            "van verdeeldheid, want één rijk werd drie rijken",
            "van eenheid, want de drie broers bleven samenwerken",
            "van eenheid, want de grenzen werden voor het eerst vastgelegd",
            "van geen van beide, want er veranderde niets",
        ],
        antwoord=0,
        uitleg="De verdeling van 843 ligt aan de basis van het latere Frankrijk en Duitsland. Het middendeel werd eeuwenlang betwist gebied.",
    ),
    dict(
        type="waarofniet",
        vraag="Uit de verdeling van Verdun groeien de latere koninkrijken Frankrijk en Duitsland.",
        antwoord=True,
        uitleg="West-Francië en Oost-Francië worden Frankrijk en het Duitse Rijk. Het middenrijk van Lotharius valt uiteen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke aanvallen troffen het rijk in de 9de en 10de eeuw?",
        opties=[
            "de invallen van de Noormannen",
            "de invallen van de Hongaren",
            "de invallen van de Saracenen",
            "de invallen van de Mongolen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De Mongolen bereiken Europa pas in de 13de eeuw en komen niet tot in het Frankische kerngebied. De drie andere golven vallen wel in deze eeuwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gevolg hadden die invallen voor de macht in het rijk?",
        opties=[
            "de bevolking zocht bescherming bij de lokale heer, wat het centrale gezag verzwakte",
            "de koning werd juist machtiger, omdat hij de verdediging van het hele rijk leidde",
            "de paus nam het wereldlijke bestuur van het rijk voor enkele tientallen jaren over",
            "de steden namen samen de verdediging van het hele rijk op zich, met eigen legers",
        ],
        antwoord=0,
        uitleg="Wie een burcht en soldaten had, kon beschermen. Dat maakte van de lokale heer de echte macht, en van de koning vaak niet veel meer dan een naam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Vergelijk de koninklijke macht onder de Merovingers en onder de Karolingers. Wat klopt?",
        opties=[
            "onder de Karolingers werd ze eerst sterker, om daarna opnieuw te verbrokkelen",
            "ze was onder de Merovingers altijd sterker dan onder de Karolingers na hen",
            "ze bleef bij de twee geslachten precies even groot, van begin tot einde",
            "ze was bij allebei volledig in handen van de paus, die de koning aanstelde",
        ],
        antwoord=0,
        uitleg="Karel de Grote bouwde een centraal bestuur uit, maar het erfrecht, de invallen en de macht van de graven ondergroeven dat weer.",
    ),
    dict(
        type="waarofniet",
        vraag="De titel van keizer gaf Karel de Grote rechtstreekse macht over heel Europa.",
        antwoord=False,
        uitleg="De titel gaf vooral aanzien en een godsdienstige rechtvaardiging. Buiten zijn eigen rijk had hij er niets aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke maatschappelijke domeinen situeer je de zalving van een koning door de paus?",
        opties=[
            "het politieke domein",
            "het culturele domein",
            "het economische domein",
            "het sociale domein",
        ],
        antwoord=[0, 1],
        uitleg="Het gaat om macht, dus politiek, en om godsdienst, en die hoort bij het culturele domein.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de Franken waren politiek en godsdienst twee gescheiden werelden.",
        antwoord=False,
        uitleg="Clovis, Pepijn en Karel gebruiken alle drie de Kerk om hun macht te onderbouwen, en de Kerk gebruikt hen om zich te beschermen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de vraag of Karel de Grote de vader van Europa is, een historische vraag en geen feitenvraag?",
        opties=[
            "omdat het antwoord afhangt van wat je onder Europa verstaat en welke bronnen je kiest",
            "omdat er over Karel de Grote zelf geen enkele geschreven bron bewaard gebleven is",
            "omdat niemand vandaag nog met zekerheid weet in welke eeuw hij geleefd heeft",
            "omdat de vraag over de toekomst van Europa gaat en niet over het verleden ervan",
        ],
        antwoord=0,
        uitleg="Zo'n vraag beantwoord je met argumenten uit bronnen, die je tegen elkaar afweegt. Er is geen enkel getal dat ze beslecht.",
    ),
]
