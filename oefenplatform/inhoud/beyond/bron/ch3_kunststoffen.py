# -*- coding: utf-8 -*-
"""Kunststoffen: polymeren en hun eigenschappen — 🌍 Beyond, chemie.

Deel 1 gaat over het maken van een kunststof: het verschil tussen een
polymerisatie of polyadditie en een polycondensatie, de monomeren van PE, PP,
PVC, PS, PTFE, PET en PA, en hoe je uit de structuur van een polymeer het
monomeer terugvindt. Deel 2 gaat over de eigenschappen: thermoplast,
thermoharder en elastomeer, de rol van crosslinks, de vervormbaarheid en de
recycleerbaarheid, en welke kunststof bij welke toepassing hoort.

De vragen noemen de kunststof met haar afkorting en haar monomeer in woorden,
want een structuurformule tekenen kan op het scherm niet.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een polymeer?",
        opties=[
            "een heel lange molecule van veel gelijke bouwstenen",
            "een mengsel van twee verschillende kunststoffen",
            "een molecule met precies twee bouwstenen",
            "een kleine molecule die kan reageren tot een keten",
        ],
        antwoord=0,
        uitleg="De bouwsteen heet het monomeer. Twee ervan samen is een dimeer, veel "
        "ervan een polymeer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor een polymerisatie of polyadditie?",
        opties=[
            "de dubbele bindingen gaan open en er komt geen bijproduct vrij",
            "er komt bij elke koppeling een molecule water vrij",
            "er wordt telkens een waterstofatoom vervangen door een groep",
            "er gaat bij elke koppeling een halogeen uit de keten",
        ],
        antwoord=0,
        uitleg="Alle atomen van de monomeren zitten in het polymeer. Bij een "
        "polycondensatie verdwijnt er telkens een kleine molecule.",
    ),
    dict(
        type="invultekst",
        vraag="Welk monomeer vormt polyetheen, PE?",
        antwoord=["etheen", "ethyleen", "eteen"],
        uitleg="De dubbele binding van etheen gaat open en de ketens koppelen aan elkaar. "
        "Zo ontstaat een lange keten van CH₂-groepen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk monomeer vormt polyvinylchloride, PVC?",
        opties=[
            "chlooretheen",
            "chloorethaan",
            "dichlooretheen",
            "chloormethaan",
        ],
        antwoord=0,
        uitleg="Chlooretheen heet ook vinylchloride, vandaar de naam. Het heeft een "
        "dubbele binding nodig om te kunnen polymeriseren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een monomeer voor een polyadditie moet een dubbele binding hebben.",
        antwoord=True,
        uitleg="Die binding gaat open en levert de twee nieuwe bindingen naar de buren. "
        "Een verzadigd alkaan kan dus niet polymeriseren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk monomeer vormt polypropeen, PP?",
        opties=[
            "propeen",
            "propaan",
            "propanol",
            "propyn",
        ],
        antwoord=0,
        uitleg="De methylgroep van propeen komt in de keten als zijgroep te hangen. "
        "Daardoor is PP steviger dan PE.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kunststoffen worden met een polycondensatie gemaakt? Kruis alles aan wat juist is.",
        opties=[
            "PET",
            "PA of nylon",
            "PE",
            "PS",
        ],
        antwoord=[0, 1],
        uitleg="Bij die twee koppelen een zuur en een alcohol of amine, met water als "
        "bijproduct. PE en PS komen van een polyadditie.",
    ),
    dict(
        type="invultekst",
        vraag="Welk bijproduct komt vrij bij een polycondensatie?",
        antwoord=["water", "H2O", "een watermolecule"],
        uitleg="Bij elke koppeling gaat er een kleine molecule uit. Daarom zit niet alle "
        "massa van de monomeren in het polymeer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk monomeer vormt polytetrafluoretheen, PTFE?",
        opties=[
            "tetrafluoretheen",
            "tetrafluorethaan",
            "difluoretheen",
            "fluormethaan",
        ],
        antwoord=0,
        uitleg="Alle vier de waterstofatomen van etheen zijn vervangen door fluor. Die "
        "stevige C-F-bindingen maken de pan antikleverig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je het monomeer terug uit de structuur van een polymeer gemaakt door polyadditie?",
        opties=[
            "je neemt het stukje dat zich herhaalt en zet de dubbele binding terug",
            "je neemt het stukje dat zich herhaalt en voegt water toe",
            "je neemt de hele keten en deelt haar massa door twee",
            "je neemt het einde van de keten met zijn zijgroepen",
        ],
        antwoord=0,
        uitleg="Zo'n herhalend stukje heet de repeterende eenheid. Bij PVC is dat "
        "CH₂-CHCl, en dus is het monomeer chlooretheen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een polyadditie zit de volledige massa van de monomeren in het polymeer.",
        antwoord=True,
        uitleg="Er gaat niets weg, dus is de atoomeconomie heel hoog. Bij een "
        "polycondensatie verlies je telkens een molecule water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk monomeer vormt polystyreen, PS?",
        opties=[
            "fenyletheen",
            "fenylethaan",
            "benzeen",
            "styraanzuur",
        ],
        antwoord=0,
        uitleg="Fenyletheen heet ook styreen: een etheenmolecule met een benzeenring "
        "eraan. Daarom hangt er aan elke tweede koolstof een ring.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over PET zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het wordt gemaakt uit een tweewaardige alcohol en een tweewaardig zuur",
            "het wordt met een polycondensatie gemaakt",
            "het wordt gemaakt uit één monomeer met een dubbele binding",
            "het wordt met een polyadditie gemaakt",
        ],
        antwoord=[0, 1],
        uitleg="De esterbindingen tussen de bouwstenen geven PET zijn naam: "
        "polyethyleentereftalaat. Daarom kan je het ook weer afbreken met water.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kleine molecule waaruit een polymeer opgebouwd wordt?",
        antwoord=["monomeer", "een monomeer", "monomeren"],
        uitleg="Mono betekent één, poly veel. Een dimeer bestaat uit twee van die "
        "bouwstenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft nylon twee verschillende monomeren nodig?",
        opties=[
            "een amidebinding ontstaat tussen een zuurgroep en een aminegroep",
            "een amidebinding ontstaat tussen twee dubbele bindingen",
            "nylon heeft een ring nodig naast een rechte keten",
            "nylon wordt gemaakt met twee katalysatoren na elkaar",
        ],
        antwoord=0,
        uitleg="Het ene monomeer brengt de COOH-groepen aan, het andere de NH₂-groepen. "
        "Bij elke koppeling gaat er water uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk reactietype gebruikt men om PE te maken?",
        opties=[
            "een polyadditie",
            "een polycondensatie",
            "een substitutie",
            "een eliminatie",
        ],
        antwoord=0,
        uitleg="De dubbele bindingen van heel veel etheenmoleculen gaan open en koppelen "
        "aan elkaar. Er komt geen bijproduct bij vrij.",
    ),
    dict(
        type="waarofniet",
        vraag="PVC en PE hebben hetzelfde monomeer.",
        antwoord=False,
        uitleg="PE komt van etheen, PVC van chlooretheen. Dat ene chlooratoom maakt de "
        "eigenschappen helemaal anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel monomeren zitten er ongeveer in één polymeerketen?",
        opties=[
            "duizenden",
            "twee of drie",
            "een tiental",
            "precies honderd",
        ],
        antwoord=0,
        uitleg="Daarom is de molaire massa van een kunststof enorm en verschilt ze van "
        "keten tot keten. Een kunststof heeft dus geen vast smeltpunt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kunststof heeft een scherp smeltpunt zoals een zout.",
        antwoord=False,
        uitleg="De ketens zijn niet alle even lang, dus smelt het materiaal over een "
        "gebied. Daarom spreekt men van een smelttraject.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kunststof zit er in de antikleeflaag van een pan?",
        antwoord=["PTFE", "teflon", "polytetrafluoretheen"],
        uitleg="De fluoratomen maken het oppervlak heel apolair, dus blijft er niets aan "
        "plakken.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor een thermoplast?",
        opties=[
            "hij wordt zacht bij verwarmen en is opnieuw te vormen",
            "hij ontleedt bij verwarmen zonder zacht te worden",
            "hij veert terug in zijn vorm na het uitrekken",
            "hij heeft heel veel crosslinks tussen de ketens",
        ],
        antwoord=0,
        uitleg="De ketens liggen los naast elkaar en kunnen bij warmte over elkaar "
        "schuiven. Daarom is een thermoplast goed te recycleren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met een thermoharder als je hem verwarmt?",
        opties=[
            "hij ontleedt of verbrandt zonder eerst te smelten",
            "hij wordt zacht en is in een nieuwe vorm te persen",
            "hij veert elastisch terug in zijn oude vorm",
            "hij lost op in het water dat eruit vrijkomt",
        ],
        antwoord=0,
        uitleg="De ketens zitten met veel crosslinks vast aan elkaar. Daardoor kunnen ze "
        "niet meer verschuiven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de bruggen tussen de ketens van een kunststof?",
        antwoord=["crosslinks", "crosslink", "dwarsverbindingen"],
        uitleg="Veel crosslinks geven een thermoharder, enkele een elastomeer en geen een "
        "thermoplast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor een elastomeer?",
        opties=[
            "hij vervormt onder een kracht en veert daarna terug",
            "hij blijft in zijn nieuwe vorm staan na het buigen",
            "hij smelt bij verwarmen tot een vloeistof",
            "hij heeft geen enkele crosslink tussen zijn ketens",
        ],
        antwoord=0,
        uitleg="Enkele crosslinks houden de ketens samen, maar laten ze toch uitrekken. "
        "Rubber is daarvan het bekendste voorbeeld.",
    ),
    dict(
        type="waarofniet",
        vraag="Een thermoplast is beter te recycleren dan een thermoharder.",
        antwoord=True,
        uitleg="Hij kan opnieuw gesmolten en gevormd worden. Een thermoharder kan alleen "
        "nog vermalen worden als vulstof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kunststof wordt gebruikt voor drankflessen?",
        opties=[
            "PET",
            "PTFE",
            "PUR",
            "PA",
        ],
        antwoord=0,
        uitleg="PET is sterk, doorzichtig en laat weinig gas door. Daarom staat de "
        "recyclagecode 1 op zo'n fles.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toepassingen passen bij PVC? Kruis alles aan wat juist is.",
        opties=[
            "buizen voor afvoer",
            "profielen voor een raam",
            "de antikleeflaag van een pan",
            "touw en visdraad",
        ],
        antwoord=[0, 1],
        uitleg="PVC is stevig en weerbestendig. De antikleeflaag is PTFE, en touw is "
        "meestal nylon.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kunststof gebruikt men voor isolatieschuim in een huis?",
        antwoord=["PUR", "polyurethaan", "PUR-schuim"],
        uitleg="Het schuim zit vol kleine gasbelletjes, en die geleiden de warmte slecht. "
        "Daardoor isoleert een dunne laag al goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een kunststof voor een tandwiel beter een thermoharder dan een thermoplast?",
        opties=[
            "hij vervormt niet als het mechanisme warm wordt",
            "hij is lichter dan een thermoplast van dezelfde maat",
            "hij is doorzichtiger dan een thermoplast",
            "hij is makkelijker te recycleren achteraf",
        ],
        antwoord=0,
        uitleg="De crosslinks houden de vorm vast, ook bij wrijvingswarmte. Een "
        "thermoplast zou zacht worden en vervormen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de structuur van een thermoplast zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de ketens liggen los naast elkaar",
            "de ketens worden enkel door intermoleculaire krachten samengehouden",
            "de ketens zitten met veel crosslinks vast",
            "de ketens zijn met atoombindingen aan elkaar geknoopt",
        ],
        antwoord=[0, 1],
        uitleg="Verwarmen verbreekt die zwakke krachten tussen de ketens, niet de "
        "bindingen in de ketens zelf. Daarom kan je het materiaal hervormen.",
    ),
    dict(
        type="waarofniet",
        vraag="Gevulkaniseerd rubber heeft geen enkele crosslink tussen zijn ketens.",
        antwoord=False,
        uitleg="Het heeft juist bruggen van zwavel, en die maken van kleverig natuurrubber "
        "een elastomeer dat terugveert. Zonder vulkanisatie zou een autoband niet "
        "bestaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kunststof zit er in een plastic zak?",
        opties=[
            "PE",
            "PET",
            "PS",
            "PA",
        ],
        antwoord=0,
        uitleg="Polyetheen is zacht, buigzaam en goedkoop. Een hardere variant ervan wordt "
        "voor flessen en emmers gebruikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men PS-schuim als verpakking?",
        opties=[
            "het is heel licht en beschermt tegen stoten",
            "het is heel sterk en kan veel gewicht dragen",
            "het laat geen enkele vloeistof door",
            "het is goed bestand tegen hoge temperatuur",
        ],
        antwoord=0,
        uitleg="Het schuim bestaat bijna volledig uit lucht. Daardoor weegt het bijna "
        "niets en vangt het schokken op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het recycleren van kunststof zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "gesorteerde, zuivere kunststof levert een beter product op",
            "een thermoplast kan opnieuw gesmolten worden",
            "een thermoharder kan opnieuw gesmolten worden",
            "gemengde kunststof levert hetzelfde resultaat als zuivere",
        ],
        antwoord=[0, 1],
        uitleg="Gemengde kunststof geeft een materiaal van mindere kwaliteit, en dat heet "
        "downcycling. Daarom is sorteren zo belangrijk.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kunststof gebruikt men voor kleding en touw?",
        antwoord=["PA", "nylon", "polyamide"],
        uitleg="De amidebindingen tussen de ketens maken de vezel sterk. Dezelfde soort "
        "binding zit in een eiwit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn microplastics een probleem?",
        opties=[
            "ze breken niet af en komen in het water en in de voedselketen terecht",
            "ze lossen op in water en maken het zuurder",
            "ze verdampen en komen zo in de lucht terecht",
            "ze reageren met zuurstof tot een giftig gas",
        ],
        antwoord=0,
        uitleg="De ketens zijn zo stabiel dat bacteriën er niet aan kunnen. Daarom blijven "
        "de deeltjes honderden jaren rondzwerven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil een voorwerp dat terugveert na het indrukken. Welke soort kunststof kies je?",
        opties=[
            "een elastomeer",
            "een thermoharder",
            "een thermoplast",
            "een polycondensaat",
        ],
        antwoord=0,
        uitleg="Enkel een elastomeer heeft net genoeg crosslinks om uit te rekken en weer "
        "samen te trekken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een thermoharder kan je na gebruik opnieuw in een andere vorm persen.",
        antwoord=False,
        uitleg="De crosslinks laten dat niet toe: hij ontleedt eerder dan dat hij zacht "
        "wordt. Alleen een thermoplast is opnieuw te vormen.",
    ),
    dict(
        type="waarofniet",
        vraag="De eigenschappen van een kunststof volgen uit de bouw van haar ketens.",
        antwoord=True,
        uitleg="De lengte van de ketens, hun zijgroepen en het aantal crosslinks bepalen "
        "of het materiaal hard, buigzaam of elastisch is.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een kunststof die bij verwarmen zacht wordt en opnieuw te vormen is?",
        antwoord=["thermoplast", "een thermoplast", "thermoplastisch"],
        uitleg="PE, PP, PET, PVC en PS horen daarbij. Een thermoharder ontleedt juist bij "
        "verwarmen.",
    ),
]
