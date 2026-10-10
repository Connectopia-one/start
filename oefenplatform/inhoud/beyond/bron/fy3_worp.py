# -*- coding: utf-8 -*-
"""De horizontale worp — 🌍 Beyond, fysica.

Deel 1 gaat over het onafhankelijkheidsbeginsel: de horizontale beweging is
een ERB en de verticale een vrije val, en die twee weten niets van elkaar.
Daar hoort de vorm van de baan bij, en de klassieke proef waarbij een kogel
die je laat vallen en een kogel die je wegschiet samen de grond raken. Deel 2
is het rekenwerk: valtijd, dracht, hoogteverlies en de snelheid onderweg, en
wat er verandert als je de hoogte of de beginsnelheid wijzigt.

Alle oefeningen rekenen zonder luchtweerstand, zoals de formules van de fiche.
De vragen zeggen dat er ook bij, want in het echt maakt de lucht wel degelijk
een verschil.

De formules staan in gewone wiskundige notatie, tussen \\( en \\). Daarom
staan de teksten hier in rauwe strings: r"\\(x = v_{0}\\,t\\)".
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt het onafhankelijkheidsbeginsel bij een horizontale worp?",
        opties=[
            "de horizontale en de verticale beweging beïnvloeden elkaar niet",
            "de horizontale beweging wordt door de val afgeremd",
            "de verticale beweging gaat sneller als je harder werpt",
            "de twee bewegingen beginnen pas na elkaar te lopen",
        ],
        antwoord=0,
        uitleg=r"Je mag ze dus apart uitrekenen: \(x = v_{0}\,t\) horizontaal en "
        r"\(y = \tfrac{1}{2}g\,t^{2}\) verticaal. De tijd \(t\) is het enige dat ze gemeen "
        r"hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat voor beweging is het horizontale deel van een horizontale worp?",
        opties=[
            r"een ERB, met \(x = v_{0}\,t\)",
            r"een EVRB, met \(x = \tfrac{1}{2}a\,t^{2}\)",
            r"een vertraagde beweging, met \(a < 0\)",
            r"een cirkelbeweging, met constante \(\lvert v \rvert\)",
        ],
        antwoord=0,
        uitleg=r"Zonder luchtweerstand werkt er horizontaal geen kracht, dus blijft "
        r"\(v_{x} = v_{0}\) constant. Verticaal is het wel een vrije val.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat voor beweging is het verticale deel van een horizontale worp?",
        opties=[
            r"een vrije val met \(v_{0y} = 0\)",
            r"een vrije val met een grote \(v_{0y}\)",
            r"een ERB omlaag, met \(v_{y}\) constant",
            r"een beweging met een groeiende \(a\)",
        ],
        antwoord=0,
        uitleg=r"Je werpt precies horizontaal, dus is de verticale beginsnelheid nul en "
        r"geldt \(v_{y} = g\,t\). De zwaartekracht doet de rest.",
    ),
    dict(
        type="invultekst",
        vraag="Welke vorm heeft de baan van een horizontale worp?",
        antwoord=["parabool", "een parabool", "parabolisch"],
        uitleg=r"Vul \(t = \dfrac{x}{v_{0}}\) in \(y = \tfrac{1}{2}g\,t^{2}\) in: dat geeft "
        r"\(y = \dfrac{g}{2v_{0}^{2}}\,x^{2}\), de vergelijking van een parabool. Met "
        r"luchtweerstand wordt de baan achteraan wat steiler.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee kogels vertrekken tegelijk van dezelfde hoogte: de ene valt gewoon, de andere wordt horizontaal weggeschoten. Welke raakt eerst de grond?",
        opties=[
            "ze raken de grond op hetzelfde ogenblik",
            "de kogel die gewoon valt, want die gaat recht omlaag",
            "de weggeschoten kogel, want die heeft meer snelheid",
            "dat hangt af van hoe zwaar elke kogel is",
        ],
        antwoord=0,
        uitleg=r"De verticale beweging is bij allebei dezelfde vrije val, met dezelfde "
        r"\(t = \sqrt{\dfrac{2h}{g}}\). De horizontale snelheid verandert daar niets aan.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De valtijd bij een horizontale worp hangt af van \(v_{0}\).",
        antwoord=False,
        uitleg=r"Ze hangt enkel af van de hoogte en van \(g\): "
        r"\(t = \sqrt{\dfrac{2h}{g}}\). Een grotere \(v_{0}\) maakt de worp wel verder, niet "
        r"langer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de valtijd bij een horizontale worp af? Kruis alles aan wat juist is.",
        opties=[
            r"van de hoogte \(h\)",
            r"van de valversnelling \(g\)",
            r"van de beginsnelheid \(v_{0}\)",
            r"van de massa \(m\)",
        ],
        antwoord=[0, 1],
        uitleg=r"De valtijd volgt uit \(h = \tfrac{1}{2}g\,t^{2}\), dus "
        r"\(t = \sqrt{\dfrac{2h}{g}}\). Noch \(v_{0}\) noch \(m\) staat daarin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de horizontale snelheid tijdens de vlucht, zonder luchtweerstand?",
        opties=[
            r"ze blijft \(v_{x} = v_{0}\)",
            "ze wordt steeds kleiner",
            "ze wordt steeds groter",
            "ze wordt nul op het einde",
        ],
        antwoord=0,
        uitleg=r"Horizontaal werkt er geen kracht, dus \(a_{x} = 0\). De verticale snelheid "
        r"\(v_{y} = g\,t\) groeit ondertussen wel gestaag aan.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De verticale snelheid groeit elke seconde met ongeveer \(9{,}81\) m/s aan.",
        antwoord=True,
        uitleg=r"Dat is precies \(g\), want \(v_{y} = g\,t\). De horizontale snelheid blijft "
        r"ondertussen onveranderd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je de snelheid van het voorwerp op een bepaald ogenblik tijdens de vlucht?",
        opties=[
            r"\(v = \sqrt{v_{x}^{2} + v_{y}^{2}}\)",
            r"\(v = v_{x} + v_{y}\)",
            r"\(v = \max(v_{x},\, v_{y})\)",
            r"\(v = v_{x} \cdot v_{y}\)",
        ],
        antwoord=0,
        uitleg=r"De twee staan loodrecht op elkaar, dus gebruik je Pythagoras. Gewoon "
        r"optellen mag enkel bij vectoren met dezelfde richting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe staat de snelheidsvector van het voorwerp halverwege de vlucht?",
        opties=[
            "schuin omlaag, raaklijnig aan de baan",
            "recht omlaag, want de val overheerst",
            "recht vooruit, want de worp was horizontaal",
            "schuin omhoog, tot aan het hoogste punt",
        ],
        antwoord=0,
        uitleg=r"De snelheid is altijd raaklijnig aan de baan. De hoek volgt uit "
        r"\(\tan\alpha = \dfrac{v_{y}}{v_{x}}\), en die wordt steiler naarmate \(v_{y}\) "
        r"groeit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de horizontale afstand die een voorwerp bij een worp aflegt?",
        antwoord=["dracht", "de dracht", "worpafstand"],
        uitleg=r"Ze is \(x = v_{0}\,t = v_{0}\sqrt{\dfrac{2h}{g}}\). Werp je van twee keer zo "
        r"hoog, dan wordt ze maar \(\sqrt{2}\) keer zo groot.",
    ),
    dict(
        type="waarofniet",
        vraag="Zonder luchtweerstand komt een zwaarder voorwerp bij dezelfde worp even ver als een lichter voorwerp.",
        antwoord=True,
        uitleg=r"De massa \(m\) staat in geen enkele formule van de worp. In het echt valt "
        r"een pingpongbal wel korter dan een golfbal, en dat komt door de lucht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom valt een pingpongbal in het echt korter dan de formules voorspellen?",
        opties=[
            "de luchtweerstand remt hem horizontaal af",
            "zijn kleine massa maakt de zwaartekracht groter",
            "hij draait rond zijn as en verliest zo hoogte",
            "de formules gelden enkel voor zware voorwerpen",
        ],
        antwoord=0,
        uitleg=r"De formules van de fiche rekenen met \(a_{x} = 0\), dus zonder "
        r"luchtweerstand. Bij een licht voorwerp met veel oppervlak is dat verschil het "
        r"grootst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kracht werkt er tijdens de vlucht op het voorwerp, zonder luchtweerstand?",
        opties=[
            r"enkel \(F_{z} = m\,g\), recht omlaag",
            r"\(F_{z}\) en een kracht vooruit",
            "enkel een kracht langs de baan",
            "er werkt geen enkele kracht meer",
        ],
        antwoord=0,
        uitleg=r"De hand die werpt, heeft het voorwerp al losgelaten. Er is dus geen kracht "
        r"meer die het vooruit duwt; het blijft gewoon doorbewegen met \(v_{0}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheid is bij de horizontale en de verticale beweging dezelfde?",
        opties=[
            r"de tijd \(t\)",
            r"de snelheid \(v\)",
            r"de versnelling \(a\)",
            r"de afgelegde weg \(s\)",
        ],
        antwoord=0,
        uitleg=r"Daarom haal je de valtijd uit \(h = \tfrac{1}{2}g\,t^{2}\) en gebruik je "
        r"diezelfde \(t\) in \(x = v_{0}\,t\). De tijd is de brug tussen de twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een horizontale worp zijn juist? Kruis alles aan wat juist is.",
        opties=[
            r"de baan is de parabool \(y = \dfrac{g}{2v_{0}^{2}}x^{2}\)",
            r"\(v_{x}\) blijft constant",
            r"\(v_{y}\) blijft constant",
            r"\(\vec{a}\) wijst langs de baan",
        ],
        antwoord=[0, 1],
        uitleg=r"\(\vec{a}\) wijst altijd recht omlaag, ook als het voorwerp schuin vooruit "
        r"beweegt. En \(v_{y} = g\,t\) groeit juist aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Het voorwerp raakt bij een horizontale worp loodrecht de grond.",
        antwoord=False,
        uitleg=r"Het heeft nog altijd zijn \(v_{x}\), dus komt het schuin aan onder een hoek "
        r"met \(\tan\alpha = \dfrac{v_{y}}{v_{x}}\). Enkel bij \(v_{0} = 0\) valt het recht "
        r"omlaag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vliegtuig laat een pakket vallen. Waar komt het pakket terecht ten opzichte van het vliegtuig?",
        opties=[
            "recht onder het vliegtuig, als dat zijn koers aanhoudt",
            "ver achter het vliegtuig, want het verliest zijn snelheid",
            "ver voor het vliegtuig, want het valt sneller vooruit",
            "op de plaats waar het vliegtuig losliet, recht omlaag",
        ],
        antwoord=0,
        uitleg=r"Het pakket houdt \(v_{x} = v_{0}\) van het vliegtuig. Vanuit de piloot "
        r"gezien valt het dus gewoon recht naar beneden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het beginsel dat de horizontale en de verticale beweging los van elkaar verlopen?",
        antwoord=["onafhankelijkheidsbeginsel", "onafhankelijkheid", "het onafhankelijkheidsbeginsel"],
        uitleg=r"Daardoor mag je elke richting apart behandelen, met \(x = v_{0}\,t\) en "
        r"\(y = \tfrac{1}{2}g\,t^{2}\). De tijd is het enige dat ze delen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Een bal wordt horizontaal weggeschoten van \(20\) m hoog. Hoe lang duurt de val? Neem \(g = 9{,}81\ \text{m/s}^{2}\).",
        opties=[
            r"\(2{,}02\) s",
            r"\(4{,}08\) s",
            r"\(1{,}43\) s",
            r"\(20{,}4\) s",
        ],
        antwoord=0,
        uitleg=r"\(t = \sqrt{\dfrac{2h}{g}} = \sqrt{\dfrac{40}{9{,}81}} = 2{,}02\) s. De "
        r"beginsnelheid doet er niet toe.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Die bal vertrok met \(15\) m/s. Hoe ver komt hij?",
        opties=[
            r"\(30{,}3\) m",
            r"\(15{,}1\) m",
            r"\(60{,}6\) m",
            r"\(7{,}6\) m",
        ],
        antwoord=0,
        uitleg=r"De dracht is \(x = v_{0}\,t = 15 \times 2{,}02 = 30{,}3\) m. Reken altijd "
        r"eerst de valtijd uit.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe groot is \(v_{y}\) van die bal op het ogenblik dat hij de grond raakt?",
        opties=[
            r"\(19{,}8\) m/s",
            r"\(15{,}0\) m/s",
            r"\(9{,}81\) m/s",
            r"\(24{,}8\) m/s",
        ],
        antwoord=0,
        uitleg=r"\(v_{y} = g\,t = 9{,}81 \times 2{,}02 = 19{,}8\) m/s. Samen met de \(15\) "
        r"m/s horizontaal geeft dat \(v = \sqrt{19{,}8^{2} + 15^{2}} = 24{,}8\) m/s.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat gebeurt er met de dracht als je \(v_{0}\) verdubbelt, bij dezelfde hoogte?",
        opties=[
            "ze wordt twee keer zo groot",
            "ze wordt vier keer zo groot",
            "ze blijft precies even groot",
            r"ze wordt \(\sqrt{2}\) keer zo groot",
        ],
        antwoord=0,
        uitleg=r"De valtijd verandert niet, en \(x = v_{0}\,t\). De dracht is dus recht "
        r"evenredig met \(v_{0}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de dracht als je de hoogte verviervoudigt, bij dezelfde beginsnelheid?",
        opties=[
            "ze wordt twee keer zo groot",
            "ze wordt vier keer zo groot",
            "ze wordt zestien keer zo groot",
            "ze blijft precies even groot",
        ],
        antwoord=0,
        uitleg=r"In \(t = \sqrt{\dfrac{2h}{g}}\) staat \(h\) onder een wortel, dus vier keer "
        r"hoger is twee keer zo lang vallen. De dracht volgt die valtijd.",
    ),
    dict(
        type="waarofniet",
        vraag="De dracht is recht evenredig met de hoogte waarvan je werpt.",
        antwoord=False,
        uitleg=r"Ze is evenredig met \(\sqrt{h}\), want \(x = v_{0}\sqrt{\dfrac{2h}{g}}\). "
        r"Met \(v_{0}\) is ze wel recht evenredig.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een kogel verlaat een tafel van \(1{,}25\) m hoog met \(4{,}0\) m/s. Hoe ver van de tafel komt hij neer? Neem \(g = 10\ \text{m/s}^{2}\).",
        opties=[
            r"\(2{,}0\) m",
            r"\(4{,}0\) m",
            r"\(1{,}0\) m",
            r"\(5{,}0\) m",
        ],
        antwoord=0,
        uitleg=r"\(t = \sqrt{\dfrac{2 \times 1{,}25}{10}} = 0{,}50\) s, dus "
        r"\(x = 4{,}0 \times 0{,}50 = 2{,}0\) m.",
    ),
    dict(
        type="invultekst",
        vraag="Welke verticale beginsnelheid heeft een voorwerp bij een horizontale worp?",
        antwoord=["nul", "0", "nul m/s"],
        uitleg=r"Je werpt immers precies horizontaal, dus \(v_{0y} = 0\). Daardoor is de "
        r"verticale beweging een gewone vrije val.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel hoogte verliest een bal die horizontaal met \(10\) m/s vertrekt, na \(20\) m horizontaal? Neem \(g = 10\ \text{m/s}^{2}\).",
        opties=[
            r"\(20\) m",
            r"\(10\) m",
            r"\(40\) m",
            r"\(5{,}0\) m",
        ],
        antwoord=0,
        uitleg=r"Na \(20\) m horizontaal is \(t = \dfrac{20}{10} = 2{,}0\) s verlopen, dus "
        r"\(y = \tfrac{1}{2} \times 10 \times 4{,}0 = 20\) m.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee ballen die van dezelfde hoogte horizontaal vertrekken met een verschillende snelheid, raken de grond tegelijk.",
        antwoord=True,
        uitleg=r"De valtijd \(t = \sqrt{\dfrac{2h}{g}}\) hangt enkel van de hoogte af. De "
        r"snellere bal komt alleen veel verder terecht.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een voetbal wordt van een klif van \(45\) m horizontaal weggetrapt en komt \(60\) m verder neer. Hoe groot was \(v_{0}\)? Neem \(g = 10\ \text{m/s}^{2}\).",
        opties=[
            r"\(20\) m/s",
            r"\(60\) m/s",
            r"\(15\) m/s",
            r"\(30\) m/s",
        ],
        antwoord=0,
        uitleg=r"\(t = \sqrt{\dfrac{90}{10}} = 3{,}0\) s, dus "
        r"\(v_{0} = \dfrac{60}{3{,}0} = 20\) m/s.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden heb je nodig om de dracht te berekenen? Kruis alles aan wat juist is.",
        opties=[
            r"de hoogte \(h\)",
            r"de beginsnelheid \(v_{0}\)",
            r"de massa \(m\)",
            r"de werphoek \(\alpha\)",
        ],
        antwoord=[0, 1],
        uitleg=r"Samen met \(g\) volstaan die twee: \(x = v_{0}\sqrt{\dfrac{2h}{g}}\). Bij "
        r"een horizontale worp is de hoek per definitie nul.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe groot is \(v\) van een voorwerp dat bij het neerkomen \(12\) m/s horizontaal en \(16\) m/s verticaal beweegt?",
        opties=[
            r"\(20\) m/s",
            r"\(28\) m/s",
            r"\(4{,}0\) m/s",
            r"\(192\) m/s",
        ],
        antwoord=0,
        uitleg=r"\(v = \sqrt{12^{2} + 16^{2}} = \sqrt{400} = 20\) m/s. Gewoon optellen mag "
        r"niet, want de twee staan loodrecht op elkaar.",
    ),
    dict(
        type="waarofniet",
        vraag="De snelheid van een voorwerp bij een horizontale worp wordt tijdens de vlucht steeds groter.",
        antwoord=True,
        uitleg=r"\(v_{x}\) blijft gelijk, maar \(v_{y} = g\,t\) groeit aan, dus wordt "
        r"\(v = \sqrt{v_{x}^{2} + v_{y}^{2}}\) groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mik je bij het werpen over een grote afstand hoger dan het doel?",
        opties=[
            "het voorwerp verliest onderweg hoogte door de val",
            "de lucht duwt het voorwerp onderweg omlaag",
            "het voorwerp wordt onderweg vanzelf zwaarder",
            "de horizontale snelheid neemt onderweg toe",
        ],
        antwoord=0,
        uitleg=r"Het hoogteverlies is \(y = \dfrac{g}{2v_{0}^{2}}\,x^{2}\), dus het gaat met "
        r"het kwadraat van de horizontale afstand. Hoe verder het doel, hoe hoger je moet "
        r"richten.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bal rolt van een tafel van \(0{,}80\) m hoog. Hoe lang duurt het voor hij de grond raakt? Neem \(g = 10\ \text{m/s}^{2}\).",
        opties=[
            r"\(0{,}40\) s",
            r"\(0{,}80\) s",
            r"\(0{,}16\) s",
            r"\(1{,}6\) s",
        ],
        antwoord=0,
        uitleg=r"\(t = \sqrt{\dfrac{2 \times 0{,}80}{10}} = \sqrt{0{,}16} = 0{,}40\) s.",
    ),
    dict(
        type="waarofniet",
        vraag="Het hoogteverlies bij een horizontale worp is recht evenredig met de horizontale afstand zelf.",
        antwoord=False,
        uitleg=r"Het gaat met het kwádraat van die afstand, want "
        r"\(y = \dfrac{g}{2v_{0}^{2}}\,x^{2}\): twee keer zo ver is vier keer zo veel "
        r"hoogteverlies. Dat is net wat de baan tot een parabool maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee identieke ballen rollen van dezelfde tafel, de ene twee keer zo snel als de andere. Wat verschilt er?",
        opties=[
            "enkel de dracht, en die is dubbel zo groot",
            "enkel de valtijd, en die is dubbel zo lang",
            "zowel de dracht als de valtijd verdubbelt",
            "er verandert helemaal niets aan de val",
        ],
        antwoord=0,
        uitleg=r"De valtijd hangt enkel van \(h\) af. De snellere bal legt in diezelfde tijd "
        r"het dubbele af, want \(x = v_{0}\,t\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangen de valtijd en de dracht van een horizontale worp af? Kruis alles aan wat juist is.",
        opties=[
            r"de valtijd hangt enkel van \(h\) af",
            r"de dracht hangt van \(v_{0}\) af",
            r"de dracht hangt ook van \(h\) af",
            r"de valtijd hangt van \(v_{0}\) af",
        ],
        antwoord=[0, 1, 2],
        uitleg=r"\(h\) bepaalt hoe lang het voorwerp onderweg is, en in die tijd schuift het "
        r"met \(v_{0}\) op: \(x = v_{0}\sqrt{\dfrac{2h}{g}}\). Daarom reken je altijd eerst "
        r"de valtijd uit.",
    ),
    dict(
        type="invultekst",
        vraag="Welke grootheid moet je eerst uitrekenen om een horizontale worp op te lossen?",
        antwoord=["de valtijd", "valtijd", "de tijd"],
        uitleg=r"Ze volgt uit \(t = \sqrt{\dfrac{2h}{g}}\). Daarna reken je met die tijd de "
        r"dracht en de snelheden uit.",
    ),
]
