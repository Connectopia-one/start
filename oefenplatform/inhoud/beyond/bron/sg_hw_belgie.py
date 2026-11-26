# -*- coding: utf-8 -*-
"""Humane wetenschappen: de Belgische staat en zijn bestuursniveaus.

Het tweede van zes thema's over politieke wetenschappen, enkel voor humane
wetenschappen (fiche 3DDO, onderdeel "Belgische politiek"). Zie
sg_hw_democratie.py voor de achtergrond.

De lijstjes staan letterlijk in de fiche:

    staatsvormen: unitaire staat, federale staat, confederale staat
    bestuursniveaus: federale overheid, regionale overheid (gemeenschappen en
        gewesten), provincies, gemeenten
    de evolutie van unitaire naar federale staat aan de hand van de
        staatshervormingen
    wetgevende en uitvoerende macht per bestuursniveau: samenstelling
        (oppositie, coalitie), functies, bevoegdheden, werking
    controleorganen bij bevoegdheids- en belangenconflicten: Grondwettelijk
        Hof, Hof van Cassatie, Raad van State

Deel 1 zijn de staatsvormen, de staatshervormingen en de bestuursniveaus.
Deel 2 zijn de parlementen en regeringen per niveau, coalitie en oppositie,
en de controleorganen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een unitaire staat?",
        opties=[
            "een staat waarin één centrale overheid alle belangrijke beslissingen neemt",
            "een staat waarin deelstaten eigen parlementen en regeringen hebben",
            "een samenwerking van onafhankelijke staten die zelf bijna alles regelen",
            "een staat die geen grondwet heeft en geen eigen parlement kiest",
        ],
        antwoord=0,
        uitleg="In een unitaire staat ligt de macht bij één centrale overheid. België was zo'n staat van 1830 tot de staatshervormingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een federale staat?",
        opties=[
            "een staat met een centrale overheid en deelstaten die elk eigen bevoegdheden hebben",
            "een staat waarin enkel de hoofdstad beslist over alles wat in het land gebeurt",
            "een losse samenwerking van landen die elk volledig onafhankelijk blijven",
            "een staat die bestuurd wordt door een vorst zonder enig parlement ernaast",
        ],
        antwoord=0,
        uitleg="In een federale staat is de macht verdeeld tussen het federale niveau en de deelstaten. Elk niveau beslist zelfstandig over zijn eigen bevoegdheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een confederale staat?",
        opties=[
            "een verbond van zelfstandige staten die enkel enkele taken samen regelen",
            "een staat met één centrale regering die alle wetten voor het land maakt",
            "een staat waarin de gemeenten de enige bestuurslaag zijn die er bestaat",
            "een staat met een koning als staatshoofd en een verkozen parlement",
        ],
        antwoord=0,
        uitleg="In een confederatie houden de deelstaten de meeste macht. Ze spreken af om enkele zaken samen te doen, zoals defensie of een munt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is België vandaag?",
        opties=["een federale staat", "een unitaire staat", "een confederale staat", "een theocratie"],
        antwoord=0,
        uitleg="Sinds de staatshervorming van 1993 staat in het eerste artikel van de grondwet dat België een federale staat is, met gemeenschappen en gewesten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werd België van een unitaire een federale staat?",
        opties=[
            "stap voor stap, via een reeks staatshervormingen sinds 1970",
            "in één keer, bij de onafhankelijkheid van België in 1830",
            "door een beslissing van de Europese Unie na de Tweede Wereldoorlog",
            "door een volksraadpleging waarin de burgers voor federalisme kozen",
        ],
        antwoord=0,
        uitleg="Sinds 1970 waren er zes staatshervormingen. Elke keer kregen de gemeenschappen en gewesten meer bevoegdheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke spanningen lagen vooral aan de basis van de staatshervormingen?",
        opties=[
            "de tegenstellingen tussen Nederlandstaligen en Franstaligen, in taal en economie",
            "de tegenstellingen tussen de kustprovincies en de provincies in het binnenland",
            "de ruzie tussen België en Nederland over de grenzen van de twee landen",
            "de wens van de Europese Unie om alle lidstaten federaal te maken",
        ],
        antwoord=0,
        uitleg="Vlamingen wilden meer zelfbestuur voor hun taal en cultuur, Walen meer economische zelfstandigheid. Die verschillende eisen leidden tot gemeenschappen en gewesten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn bestuursniveaus in België?",
        opties=[
            "de federale overheid",
            "de gemeenschappen en de gewesten",
            "de provincies",
            "de gemeenten",
            "de Europese Raad",
            "de vakbonden",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="België heeft vier bestuursniveaus: federaal, regionaal (gemeenschappen en gewesten), provinciaal en gemeentelijk. De Europese Raad is een instelling van de EU en vakbonden zijn belangengroepen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie gemeenschappen heeft België?",
        opties=[
            "de Vlaamse, de Franse en de Duitstalige Gemeenschap",
            "de Vlaamse, de Waalse en de Brusselse Gemeenschap",
            "de Nederlandse, de Franse en de Europese Gemeenschap",
            "de Vlaamse, de Waalse en de Duitstalige Gemeenschap",
        ],
        antwoord=0,
        uitleg="De gemeenschappen zijn gebaseerd op taal: Nederlands, Frans en Duits. Vlaams, Waals en Brussels Hoofdstedelijk zijn de namen van de gewesten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie gewesten heeft België?",
        opties=[
            "het Vlaamse, het Waalse en het Brusselse Hoofdstedelijke Gewest",
            "het Vlaamse, het Franse en het Duitstalige Gewest",
            "het Nederlandstalige, het Franstalige en het tweetalige Gewest",
            "het noordelijke, het zuidelijke en het oostelijke Gewest",
        ],
        antwoord=0,
        uitleg="De gewesten zijn gebaseerd op grondgebied: Vlaanderen, Wallonië en Brussel. Het Duitse taalgebied ligt in het Waals Gewest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarover beslissen de gemeenschappen vooral?",
        opties=[
            "over zaken die met personen te maken hebben, zoals onderwijs en cultuur",
            "over zaken die met grondgebied te maken hebben, zoals wegen en ruimtelijke ordening",
            "over defensie, buitenlandse zaken en de nationale munt van het land",
            "over de straffen die een rechter mag opleggen bij een misdrijf",
        ],
        antwoord=0,
        uitleg="Gemeenschappen hebben persoonsgebonden bevoegdheden, zoals onderwijs, cultuur, taalgebruik en een groot deel van welzijn en gezondheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarover beslissen de gewesten vooral?",
        opties=[
            "over grondgebonden zaken, zoals milieu en ruimtelijke ordening",
            "over zaken die met personen te maken hebben, zoals onderwijs en cultuur",
            "over het leger, de buitenlandse politiek en de sociale zekerheid",
            "over de benoeming van rechters en de werking van de rechtbanken",
        ],
        antwoord=0,
        uitleg="Gewesten hebben grondgebonden bevoegdheden, zoals economie, ruimtelijke ordening, milieu, wonen, landbouw en openbare werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bevoegdheid ligt bij de federale overheid?",
        opties=["defensie", "het onderwijs", "de ruimtelijke ordening", "het afvalbeleid van een gemeente"],
        antwoord=0,
        uitleg="De federale overheid blijft bevoegd voor zaken die het hele land aangaan, zoals defensie, justitie, buitenlandse zaken, financiën en de sociale zekerheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een school in Gent wil weten welke eindtermen haar leerlingen moeten halen. Welk bestuursniveau legt die vast?",
        opties=["de Vlaamse Gemeenschap", "de federale overheid", "de provincie Oost-Vlaanderen", "de stad Gent"],
        antwoord=0,
        uitleg="Onderwijs is een bevoegdheid van de gemeenschappen. Voor een Nederlandstalige school in Vlaanderen is dat de Vlaamse Gemeenschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf in Namen vraagt een milieuvergunning aan voor een nieuwe fabriekshal. Welke overheid bepaalt de regels voor die milieuvergunning?",
        opties=["het Waals Gewest", "de Franse Gemeenschap", "de federale overheid", "de Europese Commissie"],
        antwoord=0,
        uitleg="Milieu is een grondgebonden bevoegdheid en dus een zaak van het gewest waar de fabriek staat: het Waals Gewest.",
    ),
    dict(
        type="invultekst",
        vraag="Een staat waarin de macht verdeeld is tussen een centrale overheid en deelstaten, heet een ... staat.",
        antwoord=["federale"],
        uitleg="Federaal komt van foedus, verbond. België is sinds 1993 officieel een federale staat.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Duitstalige gebied in het oosten van België heeft een eigen gemeenschap, maar geen eigen gewest.",
        antwoord=True,
        uitleg="De Duitstalige Gemeenschap regelt onder meer onderwijs en cultuur. Voor de gewestbevoegdheden hoort het gebied bij het Waals Gewest.",
    ),
    dict(
        type="waarofniet",
        vraag="België is een federale staat sinds de onafhankelijkheid in 1830.",
        antwoord=False,
        uitleg="In 1830 begon België als unitaire staat. Pas door de staatshervormingen sinds 1970 werd het een federale staat.",
    ),
    dict(
        type="waarofniet",
        vraag="In Vlaanderen werken de Vlaamse Gemeenschap en het Vlaams Gewest met één parlement en één regering.",
        antwoord=True,
        uitleg="Vlaanderen heeft de instellingen van gemeenschap en gewest samengevoegd. Er is één Vlaams Parlement en één Vlaamse Regering.",
    ),
    dict(
        type="waarofniet",
        vraag="In een confederale staat heeft de centrale overheid meer macht dan in een unitaire staat.",
        antwoord=False,
        uitleg="Het omgekeerde klopt: in een unitaire staat heeft de centrale overheid de meeste macht, in een confederatie de deelstaten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zet deze staatsvormen van de meest naar de minst centrale macht.",
        opties=[
            "unitair, federaal, confederaal",
            "federaal, unitair, confederaal",
            "confederaal, federaal, unitair",
            "unitair, confederaal, federaal",
        ],
        antwoord=0,
        uitleg="Een unitaire staat heeft één sterk centrum, een federale staat deelt de macht, en in een confederatie houden de deelstaten bijna alles zelf.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke instelling oefent op het federale niveau de wetgevende macht uit?",
        opties=[
            "het federale parlement, met de Kamer en de Senaat",
            "de federale regering, met de eerste minister",
            "het Grondwettelijk Hof in Brussel",
            "de Raad van State in Brussel",
        ],
        antwoord=0,
        uitleg="Het federale parlement bestaat uit de Kamer van Volksvertegenwoordigers en de Senaat. De Kamer is de belangrijkste en telt 150 leden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke instelling is op het Vlaamse niveau de uitvoerende macht?",
        opties=["de Vlaamse Regering", "het Vlaams Parlement", "de provincieraad", "de Kamer van Volksvertegenwoordigers"],
        antwoord=0,
        uitleg="De Vlaamse Regering voert de decreten van het Vlaams Parlement uit. Het parlement maakt de regels en controleert de regering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke organen besturen een gemeente?",
        opties=[
            "de gemeenteraad en het college van burgemeester en schepenen",
            "de provincieraad en de deputatie met de gouverneur",
            "de Kamer en de Senaat met hun twee voorzitters",
            "het vredegerecht en de politierechtbank van de eigen stad",
        ],
        antwoord=0,
        uitleg="De gemeenteraad is de verkozen raad die beslist over de regels van de gemeente. Het college van burgemeester en schepenen voert ze uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke organen besturen een provincie?",
        opties=[
            "de provincieraad en de deputatie, met de gouverneur",
            "de gemeenteraad en het college van burgemeester en schepenen",
            "het Vlaams Parlement en de Vlaamse Regering",
            "de Raad van State en het Grondwettelijk Hof",
        ],
        antwoord=0,
        uitleg="De provincieraad wordt verkozen. De deputatie voert het beleid uit, en de gouverneur vertegenwoordigt er ook de hogere overheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een coalitie?",
        opties=[
            "een groep partijen die samen een meerderheid vormen en regeren",
            "de groep partijen in het parlement die niet in de regering zit",
            "een vergadering van alle burgemeesters uit één en dezelfde provincie",
            "een conflict tussen twee bestuursniveaus over een bevoegdheid",
        ],
        antwoord=0,
        uitleg="In België haalt één partij bijna nooit alleen de meerderheid. Daarom sluiten meerdere partijen een akkoord en vormen ze samen een coalitie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de oppositie?",
        opties=[
            "de partijen in het parlement die niet in de regering zitten",
            "de partijen die samen de regering vormen en een akkoord sloten",
            "de burgers die bij de verkiezingen niet gaan stemmen",
            "de rechters die een uitspraak van een lagere rechtbank vernietigen",
        ],
        antwoord=0,
        uitleg="De oppositie controleert de regering kritisch, stelt vragen en doet andere voorstellen. Dat is een belangrijke taak in een democratie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn taken van een parlement?",
        opties=[
            "wetten of decreten maken en goedkeuren",
            "de regering controleren",
            "de begroting goedkeuren",
            "vonnissen uitspreken in strafzaken",
            "de burgemeesters van alle gemeenten benoemen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een parlement maakt regels, controleert de regering en keurt de begroting goed. Vonnissen zijn werk voor rechters.",
    ),
    dict(
        type="meerkeuze",
        vraag="In het Vlaams Parlement stelt een parlementslid van de oppositie een kritische vraag aan de minister van Onderwijs over het lerarentekort. Welke functie van het parlement zie je hier?",
        opties=[
            "de controle op de regering",
            "het maken van een decreet",
            "het goedkeuren van de begroting",
            "het uitspreken van een vonnis",
        ],
        antwoord=0,
        uitleg="Door vragen te stellen, houdt het parlement de regering in het oog. Dat is de controlefunctie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet een regel die het Vlaams Parlement goedkeurt?",
        opties=["een decreet", "een wet", "een ordonnantie", "een vonnis"],
        antwoord=0,
        uitleg="Het federale parlement maakt wetten, het Vlaams Parlement decreten en het Brussels Parlement ordonnanties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet het Grondwettelijk Hof?",
        opties=[
            "het toetst wetten en decreten aan de grondwet en de bevoegdheidsverdeling",
            "het behandelt als hoogste rechtbank alle strafzaken met een volksjury",
            "het maakt nieuwe wetten als het parlement daar zelf niet uit raakt",
            "het telt alle stemmen na de verkiezingen en maakt de officiële uitslag bekend",
        ],
        antwoord=0,
        uitleg="Het Grondwettelijk Hof kan een wet, decreet of ordonnantie vernietigen als die de grondrechten schendt of als een overheid buiten haar bevoegdheid ging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de Raad van State?",
        opties=[
            "advies geven over ontwerpen van wetten en onwettige overheidsbeslissingen vernietigen",
            "de feiten van een strafzaak opnieuw beoordelen na een uitspraak in beroep",
            "de regering vormen als de partijen geen akkoord vinden na de verkiezingen",
            "de koning vervangen als staatshoofd wanneer hij zelf niet meer kan regeren",
        ],
        antwoord=0,
        uitleg="De Raad van State geeft juridisch advies over ontwerpen van regels. Een burger kan er ook terecht tegen een onwettige beslissing van een overheid, zoals een vergunning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet het Hof van Cassatie?",
        opties=[
            "nagaan of rechters de wet juist toepasten, zonder de feiten te herbekijken",
            "nagaan of een wet in overeenstemming is met de grondwet van België",
            "advies geven aan het parlement over een nieuw ontwerp van wet of decreet",
            "de straf bepalen voor de zwaarste misdaden, met een volksjury",
        ],
        antwoord=0,
        uitleg="Het Hof van Cassatie is het hoogste hof van de gewone rechtbanken. Het kijkt enkel of het recht juist werd toegepast en de regels van de procedure gevolgd zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vereniging vindt dat een nieuw Vlaams decreet de vrijheid van onderwijs uit de grondwet schendt. Waar kan ze vragen om het decreet te vernietigen?",
        opties=["bij het Grondwettelijk Hof", "bij het Hof van Cassatie", "bij het vredegerecht", "bij de Europese Raad"],
        antwoord=0,
        uitleg="Enkel het Grondwettelijk Hof kan een decreet toetsen aan de grondwet en het vernietigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een buurtcomité vindt dat de gemeente een bouwvergunning gaf zonder de regels te volgen. Bij welk controleorgaan kan het die beslissing aanvechten?",
        opties=["bij de Raad van State", "bij het Grondwettelijk Hof", "bij het Hof van Cassatie", "bij de Kamer van Volksvertegenwoordigers"],
        antwoord=0,
        uitleg="De Raad van State kan beslissingen van een overheid vernietigen als ze onwettig zijn. Het Grondwettelijk Hof gaat over wetten en decreten, niet over vergunningen.",
    ),
    dict(
        type="invultekst",
        vraag="De partijen in het parlement die niet in de regering zitten, vormen samen de ...",
        antwoord=["oppositie"],
        uitleg="De oppositie controleert en bekritiseert de regering, en kan zelf voorstellen indienen.",
    ),
    dict(
        type="invultekst",
        vraag="Het controleorgaan dat wetten en decreten toetst aan de grondwet, heet het ... Hof.",
        antwoord=["Grondwettelijk", "grondwettelijk"],
        uitleg="Het Grondwettelijk Hof heette vroeger het Arbitragehof, omdat het vooral bevoegdheidsconflicten tussen de overheden beslechtte.",
    ),
    dict(
        type="waarofniet",
        vraag="In België vormt meestal één partij alleen de federale regering.",
        antwoord=False,
        uitleg="Door het kiesstelsel van evenredige vertegenwoordiging haalt één partij bijna nooit de meerderheid. Er is dus bijna altijd een coalitie nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk bestuursniveau in België heeft een orgaan dat regels maakt en een orgaan dat ze uitvoert.",
        antwoord=True,
        uitleg="Federaal zijn dat parlement en regering, in Vlaanderen het Vlaams Parlement en de Vlaamse Regering, in de provincie de provincieraad en de deputatie, en in de gemeente de gemeenteraad en het college.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Hof van Cassatie beoordeelt opnieuw of een verdachte de feiten echt gepleegd heeft.",
        antwoord=False,
        uitleg="Het Hof van Cassatie oordeelt niet over de feiten. Het kijkt alleen of de wet en de procedure juist werden toegepast.",
    ),
    dict(
        type="waarofniet",
        vraag="Een parlement kan een regering wegsturen als die het vertrouwen van de meerderheid verliest.",
        antwoord=True,
        uitleg="Een regering heeft het vertrouwen van de meerderheid in het parlement nodig. Zonder dat vertrouwen moet ze opstappen.",
    ),
]
