# -*- coding: utf-8 -*-
"""Magneten en het magnetisch veld — 🌍 Beyond, fysica.

Deel 1 gaat over de magneet zelf: ferromagnetische stoffen, de weissgebieden
die het magnetisme op atomaire schaal verklaren, magnetische influentie,
demagnetiseren, het breken van een magneet, en het aardmagnetisch veld met het
kompas. Deel 2 gaat over het veld: de veldlijnenpatronen bij een staafmagneet,
een hoefijzermagneet, een rechte geleider, een lus en een spoel, de
rechterhandregel, de elektromagneet en zijn kern, en het rekenen met de
magnetische inductie.

De fiche vraagt om die patronen te tekenen; dat kan hier niet, dus vragen de
vragen naar het patroon in woorden en naar de plaats van de polen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn ferromagnetisch?",
        opties=[
            "ijzer, nikkel en cobalt",
            "koper, zilver en goud",
            "aluminium, zink en tin",
            "glas, kunststof en hout",
        ],
        antwoord=0,
        uitleg="Alleen die drie metalen en hun legeringen worden sterk door een magneet "
        "aangetrokken. Koper en aluminium zijn goede geleiders, maar niet magnetisch.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kleine gebiedjes in een ferromagnetische stof waarin de elementaire magneetjes dezelfde kant op staan?",
        antwoord=["weissgebieden", "weissgebied", "weiss-gebieden", "weiss gebieden"],
        uitleg="In een onmagnetisch stuk ijzer wijzen die gebiedjes alle kanten op. In een "
        "magneet staan ze netjes in dezelfde zin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er op atomaire schaal als een stuk ijzer gemagnetiseerd wordt?",
        opties=[
            "de weissgebieden richten zich in dezelfde zin",
            "de atomen van het ijzer schuiven dichter naar elkaar",
            "er komen extra elektronen van buitenaf in het ijzer",
            "de kernen van de ijzeratomen draaien zich volledig om",
        ],
        antwoord=0,
        uitleg="De gebiedjes die al goed staan, groeien ten koste van de andere. Samen "
        "geven ze dan één sterk veld in plaats van elkaar op te heffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar komt het magnetisme van één atoom vandaan?",
        opties=[
            "van de kringstroom en de spin van zijn elektronen",
            "van de lading van de protonen in zijn kern",
            "van het aantal neutronen dat het atoom draagt",
            "van de snelheid waarmee het hele atoom beweegt",
        ],
        antwoord=0,
        uitleg="Een bewegende lading maakt altijd een magnetisch veld. Elk elektron gedraagt "
        "zich daardoor als een piepklein magneetje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je breekt een staafmagneet in twee. Wat krijg je?",
        opties=[
            "twee kleinere magneten, elk met twee polen",
            "een stuk met enkel een noordpool en een stuk met enkel een zuidpool",
            "twee stukken die geen van beide nog magnetisch zijn",
            "één magneet en één gewoon stuk ijzer zonder veld",
        ],
        antwoord=0,
        uitleg="Elk weissgebied is zelf al een magneetje met twee polen. Je kan dus nooit "
        "een losse noordpool overhouden, hoe klein je ook breekt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een losse magnetische noordpool kan je niet maken.",
        antwoord=True,
        uitleg="Elk stukje van een magneet heeft zelf weer twee polen. Dat is het grote "
        "verschil met elektrische lading, waar een losse plus of min wel bestaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan je een permanente magneet demagnetiseren? Kruis alles aan wat juist is.",
        opties=[
            "door hem sterk op te warmen",
            "door er hard op te slaan",
            "door hem in water onder te dompelen",
            "door hem met een doek op te wrijven",
        ],
        antwoord=[0, 1],
        uitleg="Warmte en schokken brengen de weissgebieden weer door elkaar. Het veld "
        "verdwijnt dan, want de gebiedjes heffen elkaar opnieuw op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom blijft een paperclip aan een magneet hangen, ook al is hij zelf geen magneet?",
        opties=[
            "de magneet richt tijdelijk de weissgebieden in de clip",
            "de magneet geeft wat van zijn eigen lading aan de clip",
            "de magneet maakt de clip warm en daardoor kleverig",
            "de clip was altijd al zwak magnetisch van zichzelf",
        ],
        antwoord=0,
        uitleg="Dat heet magnetische influentie. Haal je de magneet weg, dan raken de "
        "gebiedjes in de clip meestal weer in de war en verdwijnt het effect.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschijnsel waarbij een magneet een stuk ijzer tijdelijk zelf magnetisch maakt?",
        antwoord=["magnetische influentie", "influentie", "inductie"],
        uitleg="Het stuk ijzer wordt dan zelf een magneet met zijn aangetrokken pool naar "
        "de magneet toe. Daarom hangt een reeks paperclips aan elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee magneten worden met hun noordpolen naar elkaar toe geschoven. Wat gebeurt er?",
        opties=[
            "ze stoten elkaar af",
            "ze trekken elkaar aan",
            "ze doen niets, want polen werken niet op elkaar in",
            "ze draaien zich samen een kwartslag",
        ],
        antwoord=0,
        uitleg="Gelijksoortige polen stoten elkaar af, ongelijksoortige trekken elkaar aan. "
        "Dat is dezelfde regel als bij elektrische lading.",
    ),
    dict(
        type="waarofniet",
        vraag="De magnetische zuidpool van de aarde ligt in de buurt van de geografische noordpool.",
        antwoord=True,
        uitleg="Anders zou de noordpool van een kompasnaald er niet naartoe wijzen. Een "
        "noordpool wordt immers door een zuidpool aangetrokken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wijst de noordpool van een kompasnaald naar het noorden?",
        opties=[
            "daar ligt de magnetische zuidpool van de aarde",
            "daar ligt de magnetische noordpool van de aarde",
            "de naald volgt de draairichting van de aarde",
            "de naald wordt door de poolster aangetrokken",
        ],
        antwoord=0,
        uitleg="Ongelijksoortige polen trekken elkaar aan. De namen noord en zuid van de "
        "aardpolen zijn magnetisch gezien dus net omgekeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een permanente magneet en een elektromagneet?",
        opties=[
            "een elektromagneet werkt alleen als er stroom loopt",
            "een elektromagneet heeft maar één pool nodig",
            "een permanente magneet trekt enkel koper aan",
            "een permanente magneet heeft een spanningsbron nodig",
        ],
        antwoord=0,
        uitleg="Zet je de stroom af, dan verdwijnt het veld van een elektromagneet. Daarom "
        "kan een schrootkraan haar last loslaten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een magneet trekt elk metaal aan.",
        antwoord=False,
        uitleg="Alleen ferromagnetische metalen zoals ijzer, nikkel en cobalt. Koper, "
        "aluminium en zilver worden niet aangetrokken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een ongemagnetiseerd stuk ijzer zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de weissgebieden wijzen alle kanten op",
            "de velden van de gebiedjes heffen elkaar op",
            "er zitten helemaal geen weissgebieden in",
            "de elektronen staan er volledig stil",
        ],
        antwoord=[0, 1],
        uitleg="De gebiedjes zijn er wel degelijk, ze staan alleen wanordelijk. Daarom kan "
        "zo'n stuk ijzer gemagnetiseerd worden en een stuk koper niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stopt een magneet met werken als je hem lang in het vuur legt?",
        opties=[
            "de warmte schudt de weissgebieden weer door elkaar",
            "het ijzer verliest bij warmte zijn elektronen",
            "het vuur neemt de polen van de magneet weg",
            "de magneet smelt en verliest daardoor zijn vorm",
        ],
        antwoord=0,
        uitleg="De atomen trillen zo hevig dat de ordening verdwijnt. Boven een bepaalde "
        "temperatuur lukt magnetiseren helemaal niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar is een staafmagneet het sterkst?",
        opties=[
            "aan de twee uiteinden",
            "precies in het midden",
            "overal even sterk langs de staaf",
            "aan de kant van de noordpool alleen",
        ],
        antwoord=0,
        uitleg="Daar komen de veldlijnen het dichtst bij elkaar. In het midden heffen de "
        "bijdragen van de twee polen elkaar grotendeels op.",
    ),
    dict(
        type="invultekst",
        vraag="Welke twee polen heeft elke magneet?",
        antwoord=["noordpool en zuidpool", "noord en zuid", "N en Z"],
        uitleg="Men schrijft ze als N en Z. Gelijksoortige polen stoten af, "
        "ongelijksoortige trekken aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een magnetische kracht werkt niet door een blad papier heen.",
        antwoord=False,
        uitleg="Ze werkt er gewoon doorheen, want het is een veldkracht en die heeft geen "
        "contact nodig. Alleen een ferromagnetische afscherming houdt het veld tegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hangen meerdere paperclips onder elkaar aan één magneet?",
        opties=[
            "elke clip wordt zelf tijdelijk een magneetje",
            "de magneet reikt met zijn veld tot onder de laatste clip",
            "de clips kleven aan elkaar door hun ruwe oppervlak",
            "de eerste clip geeft lading door aan de volgende",
        ],
        antwoord=0,
        uitleg="Door influentie krijgt elke clip zelf twee polen, en die trekt de volgende "
        "weer aan. Verder van de magneet wordt dat effect zwakker, dus houdt de reeks "
        "ergens op.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de afspraak over de zin van de magnetische veldlijnen buiten een magneet?",
        opties=[
            "ze lopen van de noordpool naar de zuidpool",
            "ze lopen van de zuidpool naar de noordpool",
            "ze lopen altijd van boven naar onder in de tekening",
            "ze lopen altijd naar de sterkste pool van de twee toe",
        ],
        antwoord=0,
        uitleg="Binnen de magneet lopen ze juist van zuid naar noord, zodat elke veldlijn "
        "een gesloten kring vormt. Elektrische veldlijnen hebben wel een begin en een "
        "einde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je het veld tussen de twee benen van een hoefijzermagneet?",
        opties=[
            "een homogeen veld",
            "een radiaal veld",
            "een dipoolveld",
            "een kringveld",
        ],
        antwoord=0,
        uitleg="De veldlijnen lopen er evenwijdig en even dicht bij elkaar. Rond een "
        "staafmagneet heb je wel een dipoolveld.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het veld rond een gewone staafmagneet?",
        antwoord=["dipoolveld", "een dipoolveld", "dipool"],
        uitleg="De lijnen vertrekken bij de noordpool en komen bij de zuidpool toe, in "
        "bogen eromheen. Tussen de benen van een hoefijzermagneet is het veld homogeen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet het magnetisch veld rond een rechte stroomvoerende draad eruit?",
        opties=[
            "als cirkels rond de draad heen",
            "als rechte lijnen evenwijdig met de draad",
            "als stervormige lijnen van de draad weg",
            "als bogen van het ene uiteinde naar het andere",
        ],
        antwoord=0,
        uitleg=r"De cirkels liggen in vlakken loodrecht op de draad. Hoe verder van de draad, "
        r"hoe verder de cirkels uit elkaar en hoe zwakker het veld: "
        r"\(B=\dfrac{\mu_{0}I}{2\pi r}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de rechterhandregel bij een rechte geleider?",
        opties=[
            "om de zin van de veldlijnen rond de draad te vinden",
            "om de grootte van het magnetisch veld te berekenen",
            "om de weerstand van de draad te bepalen",
            "om te zien welke pool het sterkst is van de twee",
        ],
        antwoord=0,
        uitleg="Je duim wijst in de conventionele stroomzin, je gekromde vingers geven de "
        "zin van de veldlijnen. Men spreekt ook van de kurkentrekkerregel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je de noordpool van een stroomvoerende spoel?",
        opties=[
            "met de rechterhand: de vingers volgen de stroom, de duim wijst naar noord",
            "met de rechterhand: de duim volgt de stroom, de vingers wijzen naar noord",
            "met de linkerhand: de duim wijst altijd naar de zuidpool toe",
            "met een kompas, want een spoel heeft zelf geen polen",
        ],
        antwoord=0,
        uitleg="Het veld van een spoel lijkt sterk op dat van een staafmagneet. Keer je de "
        "stroom om, dan wisselen de twee polen van plaats.",
    ),
    dict(
        type="waarofniet",
        vraag="Het veld binnen in een lange stroomvoerende spoel is nagenoeg homogeen.",
        antwoord=True,
        uitleg="De veldlijnen lopen er evenwijdig met de as. Buiten de spoel waaieren ze "
        "uiteen, net als bij een staafmagneet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een ijzeren kern in een elektromagneet?",
        opties=[
            "om het magnetisch veld veel sterker te maken",
            "om de stroom door de spoel te verkleinen",
            "om de spoel tegen opwarming te beschermen",
            "om de polen van de spoel om te keren",
        ],
        antwoord=0,
        uitleg="De weissgebieden in het ijzer richten zich mee en versterken het veld sterk. "
        "Daarom staat de permeabiliteit van de kern in de formule.",
    ),
    dict(
        type="invultekst",
        vraag=r"In welke eenheid druk je de magnetische inductie \(B\) uit?",
        antwoord=["tesla", "T", "de tesla"],
        uitleg=r"Het symbool van de grootheid is \(B\), dat van de eenheid \(\text{T}\). "
        r"\(1\ \text{T}\) is een heel sterk veld: dat van de aarde is ongeveer "
        r"\(5\cdot 10^{-5}\ \text{T}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat gebeurt er met \(B\) rond een rechte draad als je \(I\) verdubbelt?",
        opties=[
            "het wordt twee keer zo sterk",
            "het wordt vier keer zo sterk",
            "het blijft precies even sterk",
            "het wordt half zo sterk",
        ],
        antwoord=0,
        uitleg=r"\(B=\dfrac{\mu_{0}I}{2\pi r}\): \(B\) is recht evenredig met \(I\) en "
        r"omgekeerd evenredig met \(r\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat gebeurt er met \(B\) rond een rechte draad als je twee keer zo ver gaat staan?",
        opties=[
            "het wordt half zo sterk",
            "het wordt vier keer zo zwak",
            "het blijft precies even sterk",
            "het wordt twee keer zo sterk",
        ],
        antwoord=0,
        uitleg=r"In \(B=\dfrac{\mu_{0}I}{2\pi r}\) staat \(r\) in de noemer en geen "
        r"\(r^{2}\). Dat is anders dan bij de wet van Coulomb.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarvan hangt \(B\) binnen in een spoel af? Kruis alles aan wat juist is.",
        opties=[
            r"van het aantal windingen per meter \(\tfrac{N}{\ell}\)",
            r"van de stroom \(I\) erdoor",
            "van de lengte van de draad in meter",
            r"van de spanning \(U\) over de hele kring",
        ],
        antwoord=[0, 1],
        uitleg=r"\(B=\mu_{0}\,\dfrac{N}{\ell}\,I\). Ook de stof in de spoel telt mee, via de "
        r"permeabiliteit \(\mu\). De spanning werkt alleen onrechtstreeks, want die bepaalt "
        r"de stroom.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe dichter de magnetische veldlijnen bij elkaar liggen, hoe sterker het veld.",
        antwoord=True,
        uitleg="Dat is precies zoals bij elektrische veldlijnen. Daarom liggen de lijnen "
        "aan de polen van een magneet het dichtst op elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee stroomvoerende spoelen staan naast elkaar met hun noordpolen naar elkaar toe. Wat gebeurt er?",
        opties=[
            "ze stoten elkaar af, net als twee gewone magneten",
            "ze trekken elkaar aan, want er loopt stroom in beide",
            "ze doen niets, want een spoel heeft geen echte polen",
            "ze draaien allebei een halve slag rond hun as",
        ],
        antwoord=0,
        uitleg="Een stroomvoerende spoel gedraagt zich als een staafmagneet. Keer je in één "
        "van de twee de stroom om, dan trekken ze elkaar wel aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toepassingen berusten op een elektromagneet? Kruis alles aan wat juist is.",
        opties=[
            "een schrootkraan",
            "een elektrische deurbel",
            "een gewone zaklamp",
            "een mechanische weegschaal",
        ],
        antwoord=[0, 1],
        uitleg="Ook een relais, een automatische zekering, een luidspreker en een "
        "MRI-scanner werken zo. Wat ze gemeen hebben: het veld kan aan en uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt een schrootkraan met een elektromagneet?",
        opties=[
            "de stroom aan betekent oppakken, de stroom af betekent lossen",
            "de stroom aan betekent lossen, de stroom af betekent oppakken",
            "de kraan keert telkens de polen van de magneet om",
            "de kraan gebruikt een permanente magneet die meedraait",
        ],
        antwoord=0,
        uitleg="Dat is precies het voordeel van een elektromagneet. Een permanente magneet "
        "zou het schroot niet meer kunnen loslaten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een magnetische veldlijn heeft een begin en een einde, net als een elektrische veldlijn.",
        antwoord=False,
        uitleg="Magnetische veldlijnen zijn altijd gesloten kringen: buiten de magneet van "
        "noord naar zuid, binnenin weer terug. Dat komt doordat er geen losse polen "
        "bestaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kompasnaald gaat met haar noordpool tegen de zin van de veldlijn in staan.",
        antwoord=False,
        uitleg="Ze gaat juist mét de zin van de veldlijn staan, want de naald volgt de "
        "veldvector in dat punt. Zo kan je met kleine kompasjes het hele patroon "
        "zichtbaar maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet het veld in het midden van een stroomvoerende cirkelvormige lus eruit?",
        opties=[
            "het staat loodrecht op het vlak van de lus",
            "het ligt netjes in het vlak van de lus zelf",
            "het wijst van het midden naar de draad toe",
            "het is daar precies nul, want alles heft elkaar op",
        ],
        antwoord=0,
        uitleg="De bijdragen van alle stukjes draad versterken elkaar daar. Met de "
        "rechterhandregel vind je of het veld naar voren of naar achter wijst.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de regel waarmee je met je rechterhand de zin van een magnetisch veld vindt?",
        antwoord=["rechterhandregel", "kurkentrekkerregel", "de rechterhandregel"],
        uitleg="Bij een rechte draad wijst je duim in de stroomzin en krommen je vingers "
        "mee met de veldlijnen. Bij een spoel is het net omgekeerd.",
    ),
]
