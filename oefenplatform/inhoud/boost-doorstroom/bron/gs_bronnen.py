# -*- coding: utf-8 -*-
"""De vragen voor "Redeneren met historische bronnen".

Uit de vakfiche: de historische vraagstelling met haar criteria voor
onderzoekbaarheid, en het stappenplan van de bronnenanalyse. Soorten bronnen,
de maker in zijn context, standplaatsgebondenheid, en het beoordelen van
bruikbaarheid en betrouwbaarheid met de criteria argumentatie, interpretatie,
veralgemening, vooroordeel en stereotypering.

Deel 1 gaat over de vraag en de bron zelf. Deel 2 over bruikbaarheid,
betrouwbaarheid en het beargumenteerde antwoord.

Op het examen krijgt een leerling bronnen en een historische vraag, en voert hij
het stappenplan uit. De fiche noemt zelf twee voorbeelden: "Kan je Karel de
Grote de vader van Europa noemen?" en "Hoe bloedig is de Slag bij Hastings
verlopen?"
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waaraan moet een onderzoekbare historische vraag voldoen?",
        opties=[
            "ze is afgebakend in tijd en in ruimte",
            "ze is afgebakend binnen een of meer maatschappelijke domeinen",
            "er bestaan bronnen over, en die zijn bruikbaar",
            "ze heeft maar één mogelijk antwoord",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een vraag met maar één mogelijk antwoord is meestal geen onderzoeksvraag maar een weetje. De drie andere criteria komen uit de fiche zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk criterium ontbreekt aan de vraag 'Welke rol speelden de Arabieren in de internationale handel?'",
        opties=[
            "de afbakening in tijd",
            "de afbakening in het maatschappelijke domein",
            "het bestaan van bronnen",
            "de afbakening in ruimte",
        ],
        antwoord=0,
        uitleg="Over welke eeuw gaat het? Zonder tijdsgrens kan je de vraag niet beantwoorden; handel is al een economisch domein en de ruimte staat er ook in.",
    ),
    dict(
        type="waarofniet",
        vraag="De vraag 'Waarom gingen mensen op ontdekkingstocht?' is zonder verdere afbakening nog geen goede onderzoeksvraag.",
        antwoord=True,
        uitleg="Welke mensen, wanneer, van waaruit? Zo ruim gesteld kan je ze niet met bronnen beantwoorden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een primaire en een secundaire bron?",
        opties=[
            "een primaire bron komt uit de tijd zelf, een secundaire is er later over gemaakt",
            "een primaire bron is geschreven, een secundaire is getekend of geschilderd",
            "een primaire bron is altijd betrouwbaar, een secundaire nooit helemaal",
            "een primaire bron is kort en bondig, een secundaire lang en uitvoerig",
        ],
        antwoord=0,
        uitleg="Een dagboek uit 1789 is primair, een geschiedenisboek over 1789 secundair. Primair betekent niet automatisch beter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soort bron bestaat níét?",
        opties=[
            "de denkbeeldige bron",
            "de geschreven bron",
            "de materiële bron",
            "de audiovisuele bron",
        ],
        antwoord=0,
        uitleg="De drie andere vormen samen dekken alles wat het verleden heeft nagelaten: teksten, voorwerpen en beeld of geluid.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je iemand die een gebeurtenis zelf gezien heeft?",
        antwoord="een ooggetuige",
        uitleg="Zijn verslag staat dicht bij de feiten, maar hij zag maar één plek en had zijn eigen belangen. Nabijheid is nog geen objectiviteit.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tijdgenoot is altijd ook een ooggetuige.",
        antwoord=False,
        uitleg="Een tijdgenoot leefde in dezelfde tijd, maar was er daarom nog niet bij. Hij kan van horen zeggen schrijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wil je weten over de maker van een bron?",
        opties=[
            "wie het is: naam, beroep en afkomst",
            "welke maatschappelijke positie hij innam",
            "wie de opdracht gaf en met welk doel",
            "hoeveel hij ervoor betaald kreeg",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het bedrag ken je zelden en het helpt zelden. De drie andere brengen je wel bij zijn perspectief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent standplaatsgebondenheid?",
        opties=[
            "wie iets vertelt, doet dat vanuit zijn eigen plaats, tijd en belangen",
            "een bron mag de bewaarplaats waar ze ligt niet zomaar verlaten",
            "een bron hoort altijd bij één vaste periode en bij geen andere",
            "een historicus mag over een onderwerp maar één standpunt innemen",
        ],
        antwoord=0,
        uitleg="Een Spaanse en een Nederlandse bron over Alva zijn daar het schoolvoorbeeld van. Geen van beide liegt noodzakelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Standplaatsgebondenheid maakt een bron waardeloos.",
        antwoord=False,
        uitleg="Ze maakt hem juist interessant: je leert er de blik van de maker uit kennen. Je moet ze alleen meewegen bij wat je eruit afleidt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort níét bij stap 1 van de bronnenanalyse?",
        opties=[
            "bepalen hoeveel de bron vandaag waard is",
            "bepalen waar en wanneer ze ontstond",
            "bepalen welke soort bron het is",
            "bepalen voor wie ze gemaakt is",
        ],
        antwoord=0,
        uitleg="De veilingwaarde zegt niets over het verleden. De drie andere punten vormen de context waarin alles wat volgt gelezen moet worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij stap 1 hoort ook vaststellen welke contextgegevens ontbreken.",
        antwoord=True,
        uitleg="Een bron zonder datum of zonder bekende maker kan nog altijd bruikbaar zijn, maar je moet weten dat dat gat er is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraag je je af voor wie een bron gemaakt is?",
        opties=[
            "wie het publiek is, bepaalt mee wat er verteld en verzwegen wordt",
            "het publiek bepaalt de prijs die men voor de bron gevraagd heeft",
            "het publiek bepaalt in welke taal de bron vertaald zal worden",
            "dat heeft geen enkele invloed op wat er in de bron te lezen staat",
        ],
        antwoord=0,
        uitleg="Een verslag aan de koning klinkt anders dan een brief aan een vriend, ook als dezelfde man beide schrijft.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een bron die geen woorden gebruikt maar een voorwerp of gebouw is?",
        antwoord="een materiële bron",
        uitleg="Een muntstuk, een scherf, een belfort. Ze liegt niet met woorden, maar ze zegt ook niet vanzelf wat ze betekent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn archeologische bronnen belangrijk voor periodes met weinig geschriften?",
        opties=[
            "ze vertellen over het dagelijkse leven van mensen die zelf niet schreven",
            "ze zijn altijd volledig bewaard, zodat er niets van ontbreekt",
            "ze hebben nooit enige interpretatie nodig en spreken voor zich",
            "ze dateren zichzelf, zodat je er geen onderzoek voor hoeft te doen",
        ],
        antwoord=0,
        uitleg="Wie schreef, was een kleine minderheid. In een afvalput vind je wat er in een gewoon huishouden gegeten en gebruikt werd.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij digitale bronnen moet je ook rekening houden met ethische, sociale en legale regels.",
        antwoord=True,
        uitleg="Wie een afbeelding overneemt, vermeldt de herkomst en houdt rekening met auteursrecht. Ook privacy speelt bij recent materiaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je in stap 3 van de bronnenanalyse?",
        opties=[
            "je interpreteert de bron: je legt uit hoe context en standplaats de inhoud bepalen",
            "je zoekt de bron op in een archief of in een verzameling van bronnen",
            "je vertaalt de bron naar het Nederlands van vandaag, zin per zin",
            "je bewaart de bron op een veilige plaats zodat ze niet verloren gaat",
        ],
        antwoord=0,
        uitleg="In stap 2 lees of bekijk je de bron, in stap 3 weeg je wat je gelezen hebt, en in stap 4 formuleer je je antwoord.",
    ),
    dict(
        type="waarofniet",
        vraag="Bronnen die elkaar tegenspreken, moet je zo snel mogelijk tot één verhaal herleiden.",
        antwoord=False,
        uitleg="Juist dat verschil is informatie. Waarom vertelt de ene het anders dan de andere? Dat is vaak de interessantste vraag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vergelijk je als je verschillende bronnen naast elkaar legt?",
        opties=[
            "hun context: wanneer, waar en door wie ze gemaakt zijn",
            "hun inhoud: wat ze wel en niet vertellen",
            "hun betrouwbaarheid",
            "hun lettertype",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het lettertype helpt hooguit bij het dateren. De drie andere punten bepalen wat je uit de bronnen samen mag afleiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stelt een historicus eerst een vraag, en gaat hij pas daarna bronnen zoeken?",
        opties=[
            "zonder vraag weet je niet waarnaar je in een bron moet kijken",
            "omdat het in de wetgeving op het archiefwezen zo voorgeschreven staat",
            "omdat de bronnen anders uit het archief zouden verdwijnen",
            "omdat er anders veel te weinig bronnen over blijven om mee te werken",
        ],
        antwoord=0,
        uitleg="Dezelfde rekening van een klooster geeft een ander antwoord aan wie naar voeding vraagt dan aan wie naar arbeid vraagt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent de bruikbaarheid van een bron?",
        opties=[
            "in welke mate de bron jouw historische vraag helpt beantwoorden",
            "of de bron er mooi en verzorgd uitziet om naar te kijken",
            "of de bron oud genoeg is om als historisch te mogen gelden",
            "of de bron in het Nederlands geschreven of vertaald is",
        ],
        antwoord=0,
        uitleg="Een betrouwbare bron over een ander onderwerp is voor jouw vraag onbruikbaar. Bruikbaarheid hangt dus altijd van de vraag af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vraag je je af bij het beoordelen van de bruikbaarheid?",
        opties=[
            "geeft de bron rechtstreekse informatie over het onderwerp?",
            "geeft de bron onrechtstreekse informatie?",
            "geeft de bron een volledig, gedeeltelijk of geen antwoord?",
            "is de bron in haar eigen tijd duur geweest om te maken?",
        ],
        antwoord=[0, 1, 2],
        uitleg="De prijs staat er los van. De drie andere vragen komen letterlijk uit het stappenplan van de fiche.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bron die maar een deel van je vraag beantwoordt, is daarom nog niet waardeloos.",
        antwoord=True,
        uitleg="Je legt hem naast andere. Uit drie bronnen die elk een stuk geven, kan je samen een antwoord bouwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk criterium hoort níét in het rijtje voor de betrouwbaarheid van de inhoud?",
        opties=[
            "de lengte van de tekst",
            "de gebruikte argumentatie",
            "veralgemening",
            "vooroordeel en stereotypering",
        ],
        antwoord=0,
        uitleg="Lengte zegt niets. De vijf criteria van de fiche zijn argumentatie, interpretatie, veralgemening, vooroordeel en stereotypering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een veralgemening?",
        opties=[
            "uit één of enkele gevallen een besluit over het geheel trekken",
            "een lange tekst korter maken zonder de inhoud te veranderen",
            "een bron vertalen uit de taal waarin ze geschreven werd",
            "een jaartal afronden naar de eeuw waarin het gevallen is",
        ],
        antwoord=0,
        uitleg="Eén rijke stad staat niet voor het hele graafschap. Let op woorden als 'iedereen', 'altijd' en 'overal'.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een vast, te eenvoudig beeld van een hele groep mensen?",
        antwoord="een stereotype",
        uitleg="De luie boer, de wrede Spanjaard, de gierige koopman. Het zegt vooral iets over wie het beeld gebruikt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vooroordeel is een mening die pas gevormd wordt nadat alle feiten bekeken zijn.",
        antwoord=False,
        uitleg="Het is net het omgekeerde: de mening staat al vast voor de feiten bekeken zijn. In een bron herken je dat aan woordkeuze die oordeelt in plaats van beschrijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke elementen uit de historische context kunnen de betrouwbaarheid beïnvloeden?",
        opties=[
            "de maker hing af van de persoon over wie hij schrijft",
            "er heerste censuur",
            "de bron werd pas lang na de feiten opgeschreven",
            "de bron is bewaard in een archief",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bewaard worden in een archief zegt niets over de inhoud. De drie andere geven je wel reden tot voorzichtigheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Een secundaire bron van een historicus is altijd betrouwbaarder dan een ooggetuigenverslag.",
        antwoord=False,
        uitleg="Een historicus kan ook selecteren, interpreteren en zich vergissen. Je beoordeelt elke bron apart, niet haar soort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de redeneerwijze 'bewijs gebruiken'?",
        opties=[
            "je staaft elke uitspraak met informatie uit een bron",
            "je gelooft de eerste bron die je over het onderwerp vindt",
            "je zoekt enkel de bronnen op die je eigen gelijk bevestigen",
            "je vermeldt geen bronnen en schrijft enkel je eigen mening",
        ],
        antwoord=0,
        uitleg="Zonder bron is het een mening. Met bron is het een beargumenteerd antwoord, ook als iemand anders het anders leest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke historische redeneerwijzen zijn er?",
        opties=[
            "oorzaak en gevolg benoemen, en bedoelde van onbedoelde gevolgen onderscheiden",
            "meerdere perspectieven hanteren, en continuïteit en verandering benoemen",
            "historisch contextualiseren, actualiseren en verbanden leggen",
            "het jaartal van een bron gokken en het achteraf in een boek nakijken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Gokken is geen redeneerwijze. De drie andere antwoorden bevatten samen bijna de hele lijst uit de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een onbedoeld gevolg?",
        opties=[
            "een gevolg dat niemand nastreefde maar dat er toch kwam",
            "een gevolg dat uiteindelijk helemaal niet gebeurd is",
            "een gevolg dat men achteraf liever verzwijgt dan vertelt",
            "een gevolg waarvoor geen enkele oorzaak aan te wijzen is",
        ],
        antwoord=0,
        uitleg="Columbus zocht een weg naar Azië; wat hij veroorzaakte, was de kolonisatie van Amerika. Dat wilde niemand zo gepland hebben.",
    ),
    dict(
        type="waarofniet",
        vraag="Actualiseren betekent een verband leggen tussen het verleden en vandaag.",
        antwoord=True,
        uitleg="Je moet dan wel opletten voor anachronisme: het verleden verklaren met de maatstaf van nu is iets anders dan het ermee verbinden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de redeneerwijze waarbij je benoemt welke mensen zelf iets in gang zetten?",
        antwoord="agency",
        uitleg="Men spreekt van menselijke actoren. Het verleden overkwam mensen niet alleen, ze maakten het ook zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent historisch contextualiseren?",
        opties=[
            "een gebeurtenis of bron begrijpen vanuit de tijd waarin ze thuishoort",
            "een gebeurtenis uit het verleden in het heden van vandaag plaatsen",
            "een bron netjes in een archief opbergen met een nummer erbij",
            "een gebeurtenis zo nauwkeurig mogelijk in het juiste jaar dateren",
        ],
        antwoord=0,
        uitleg="Wie de Beeldenstorm beoordeelt zonder de honger en de vervolging van 1566 te kennen, ziet enkel vandalisme.",
    ),
    dict(
        type="waarofniet",
        vraag="Meerdere perspectieven hanteren betekent dat elk standpunt evenveel waard is.",
        antwoord=False,
        uitleg="Het betekent dat je verschillende standpunten kent en weegt. Een standpunt dat de bronnen tegenspreekt, weegt daarna lichter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe formuleer je in stap 4 een antwoord op de historische vraag?",
        opties=[
            "je kiest informatie uit de bronnen en staaft je antwoord met argumenten",
            "je vat elke bron kort samen en zet die samenvattingen onder elkaar",
            "je kiest de bron die je het beste bevalt en schrijft die gewoon over",
            "je geeft je eigen mening zonder naar de bronnen te verwijzen",
        ],
        antwoord=0,
        uitleg="Een samenvatting van de bronnen is nog geen antwoord. Je moet zeggen wat je besluit, en waarom de bronnen dat dragen.",
    ),
    dict(
        type="waarofniet",
        vraag="Op een historische vraag kan meer dan één beargumenteerd antwoord bestaan.",
        antwoord=True,
        uitleg="Of Karel de Grote de vader van Europa is, hangt af van wat je onder Europa verstaat. Wat telt, is of je antwoord door de bronnen gedragen wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt hoe bloedig de Slag bij Hastings verliep. Welke bron weegt daarbij het zwaarst?",
        opties=[
            "de bronnen samen, na vergelijking en weging van hun betrouwbaarheid",
            "het lofdicht dat een tijdgenoot op de overwinnaar geschreven heeft",
            "een roman over de slag, geschreven in onze eigen eeuw",
            "de bron die het hoogste aantal doden van allemaal noemt",
        ],
        antwoord=0,
        uitleg="Een lofdicht overdrijft met opzet. Pas als je de bronnen naast elkaar legt, kan je zeggen wat er redelijk uit volgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom volstaat het niet om één bron te gebruiken voor een antwoord?",
        opties=[
            "elke bron is standplaatsgebonden en onvolledig, samen dekken ze elkaars blinde vlekken",
            "één enkele bron is altijd door een latere kopiist vervalst of verminkt",
            "de leerkracht vraagt er nu eenmaal meer dan één voor elke opdracht",
            "één enkele bron is altijd te kort om er iets uit af te kunnen leiden",
        ],
        antwoord=0,
        uitleg="Kruisen is de kern van het vak: wat twee onafhankelijke bronnen allebei zeggen, staat sterker dan wat er in één staat.",
    ),
]
