# -*- coding: utf-8 -*-
"""De leerbundels voor wetenschap en techniek, categorie Start."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel
tabel = bundel.tabel

VAK = "Wetenschap en techniek"
BUNDELS = {}

BUNDELS["biologie-leven-en-ecologie"] = dict(
    vak=VAK, titel="Biologie: leven en ecologie",
    onder="Planten, dieren, je eigen lichaam, en hoe alles met elkaar samenhangt.",
    secties=[
        dict(kop="Wat leeft, en wat niet", blokken=[
            ("p", "Iets leeft als het aan alle vijf de kenmerken voldoet: het <strong>groeit</strong>, het <strong>voedt zich</strong>, het <strong>ademt</strong>, het <strong>plant zich voort</strong> en het <strong>reageert op zijn omgeving</strong>."),
            ("weetje", "Een vlam groeit, verbruikt zuurstof en beweegt, maar plant zich niet voort. Daarom leeft vuur niet, hoe levend het er ook uitziet."),
        ]),
        dict(kop="Een plant van dichtbij", blokken=[
            ("fig", svg.plantdelen(340), "Elk deel van de plant heeft zijn eigen taak."),
            ("fig", tabel(["Deel", "Waarvoor het dient"], [
                ["wortel", "water en voedingsstoffen opnemen, en de plant vasthouden"],
                ["stengel", "alles rechthouden en het water naar boven brengen"],
                ["blad", "zonlicht opvangen en voedsel maken"],
                ["bloem", "zaadjes maken, met hulp van insecten of de wind"],
            ]), None),
            ("p", "In het blad maakt de plant zelf haar voedsel uit licht, water en koolstofdioxide. Daarbij komt zuurstof vrij — precies wat wij inademen."),
        ]),
        dict(kop="Voedselketens", blokken=[
            ("p", "In de natuur eet alles van iets anders. Zo'n rij noem je een voedselketen, en ze begint altijd bij een plant."),
            ("fig", svg.stappen(["Gras|maakt zelf voedsel", "Konijn|eet planten", "Vos|eet dieren"]),
             "De pijl wijst naar wie eet. Gras → konijn → vos."),
            ("p", "Verdwijnt één schakel, dan voelt de hele keten dat. Zonder konijnen vindt de vos minder eten, en groeit het gras ongestoord door."),
        ]),
        dict(kop="Je eigen lichaam", blokken=[
            ("fig", tabel(["Stelsel", "Wat het doet", "Belangrijkste organen"], [
                ["ademhaling", "zuurstof binnen, koolstofdioxide buiten", "longen, luchtpijp"],
                ["bloedsomloop", "zuurstof en voedsel rondbrengen", "hart, bloedvaten"],
                ["spijsvertering", "voedsel afbreken tot bruikbare stoffen", "maag, darmen"],
                ["skelet en spieren", "rechthouden en bewegen", "botten, spieren, gewrichten"],
                ["zenuwstelsel", "alles aansturen en waarnemen", "hersenen, zenuwen"],
            ]), "Je hart klopt ongeveer 100 000 keer per dag, zonder dat je eraan denkt."),
        ]),
        dict(kop="Groeien en veranderen", blokken=[
            ("p", "Sommige dieren veranderen volledig van vorm tijdens hun leven. Dat heet een <strong>gedaanteverwisseling</strong>."),
            ("fig", svg.stappen(["Eitje", "Rups", "Pop", "Vlinder"], kleur=svg.AMBER),
             "Bij een kikker gaat het net zo: eitje, dikkopje, kikker."),
        ]),
        dict(kop="Zorg dragen voor de natuur", blokken=[
            ("p", "Een <strong>ecosysteem</strong> is alles wat in één gebied samenleeft: de planten, de dieren, de bodem, het water en het weer. Die hangen allemaal aan elkaar vast."),
            ("p", "Daarom heeft wat één soort overkomt, gevolgen voor de rest. Verdwijnen de bijen, dan worden veel planten niet meer bestoven, en dus komen er ook minder vruchten."),
        ]),
    ],
    onthoud=[
        "Leven betekent: groeien, voeden, ademen, voortplanten en reageren.",
        "De plant maakt in haar bladeren zelf voedsel uit licht.",
        "Een voedselketen begint altijd bij een plant.",
        "De pijl in een voedselketen wijst naar wie eet.",
        "In een ecosysteem hangt alles aan elkaar vast.",
    ])

BUNDELS["chemie-stoffen-en-mengsels"] = dict(
    vak=VAK, titel="Chemie: stoffen en mengsels",
    onder="Waaruit dingen bestaan, hoe ze van vorm veranderen en hoe je een mengsel weer uit elkaar haalt.",
    secties=[
        dict(kop="Drie toestanden", blokken=[
            ("p", "Alles om je heen bestaat uit piepkleine deeltjes. Hoe die deeltjes liggen, bepaalt of een stof vast, vloeibaar of gasvormig is."),
            ("fig", svg.deeltjes(470), "Dezelfde deeltjes, alleen anders geordend."),
            ("p", "Water is daar het mooiste voorbeeld van: als ijs is het vast, als water vloeibaar en als waterdamp een gas. Het blijft telkens water."),
        ]),
        dict(kop="Van de ene toestand naar de andere", blokken=[
            ("fig", tabel(["Verandering", "Hoe het heet", "Wanneer"], [
                ["vast → vloeibaar", "smelten", "ijs in je hand"],
                ["vloeibaar → vast", "stollen of bevriezen", "water in de diepvries"],
                ["vloeibaar → gas", "verdampen", "een plas die opdroogt"],
                ["gas → vloeibaar", "condenseren", "damp op een koude ruit"],
            ]), "Water bevriest bij 0 °C en kookt bij 100 °C."),
            ("weetje", "Bij al die veranderingen blijft de stof zelf dezelfde. Er komt of gaat alleen warmte bij."),
        ]),
        dict(kop="Mengsels", blokken=[
            ("p", "Meng je twee stoffen, dan blijven het twee stoffen. Soms zie je dat nog (zand in water), soms niet (suiker in water)."),
            ("fig", tabel(["Soort mengsel", "Voorbeeld", "Zie je de delen nog?"], [
                ["oplossing", "suiker in water", "nee"],
                ["troebel mengsel", "zand in water", "ja, het zakt naar beneden"],
                ["mengsel van vaste stoffen", "muesli", "ja"],
                ["mengsel van gassen", "lucht", "nee"],
            ]), "Lucht is een mengsel: vooral stikstof, en ongeveer een vijfde zuurstof."),
        ]),
        dict(kop="Een mengsel scheiden", blokken=[
            ("p", "Omdat de stoffen in een mengsel zichzelf blijven, kan je ze er weer uit halen. Welke manier werkt, hangt af van wat er in zit."),
            ("fig", tabel(["Manier", "Waarvoor", "Voorbeeld"], [
                ["zeven", "grote en kleine stukken scheiden", "pasta uit kookwater"],
                ["filteren", "een vaste stof uit een vloeistof", "koffiefilter"],
                ["indampen", "een opgeloste stof terugwinnen", "zout uit zeewater"],
                ["bezinken", "zwaardere deeltjes laten zakken", "modder in een emmer"],
                ["magneet", "ijzer uit een mengsel halen", "ijzervijlsel uit zand"],
            ]), None),
        ]),
        dict(kop="Veilig werken", blokken=[
            ("p", "Sommige stoffen zijn gevaarlijk. Op de verpakking staan daarom waarschuwingstekens: een vlam voor brandbaar, een doodshoofd voor giftig, een druppel die inbijt voor bijtend."),
            ("p", "Mengen wat je niet kent, is nooit slim. Ook doodgewone producten uit de badkamer kunnen samen een schadelijk gas vormen."),
        ]),
    ],
    onthoud=[
        "Vast, vloeibaar en gas: dezelfde deeltjes, anders geordend.",
        "Smelten, stollen, verdampen, condenseren.",
        "Water bevriest bij 0 °C en kookt bij 100 °C.",
        "In een mengsel blijft elke stof zichzelf.",
        "Zeven, filteren, indampen, bezinken en de magneet scheiden een mengsel.",
        "Meng nooit iets waarvan je het etiket niet gelezen hebt.",
    ])

BUNDELS["natuurkunde-energie-en-krachten"] = dict(
    vak=VAK, titel="Natuurkunde: energie en krachten",
    onder="Wat dingen doet bewegen, waar energie vandaan komt, en hoe stroom, licht en geluid werken.",
    secties=[
        dict(kop="Krachten", blokken=[
            ("p", "Een kracht is een duw of een trek. Je ziet een kracht nooit zelf, wel wat ze doet: iets gaat bewegen, stoppen, sneller gaan of van vorm veranderen."),
            ("fig", tabel(["Kracht", "Wat je ervan merkt"], [
                ["zwaartekracht", "alles valt naar beneden"],
                ["wrijving", "een bal rolt uit en stopt"],
                ["spierkracht", "jij duwt of trekt zelf"],
                ["magnetische kracht", "een magneet trekt ijzer aan"],
                ["veerkracht", "een elastiek springt terug"],
            ]), "Zonder wrijving zou je niet kunnen stappen — en ook niet kunnen remmen."),
        ]),
        dict(kop="De hefboom", blokken=[
            ("p", "Met een hefboom til je iets zwaars met minder kracht. Hoe verder je van het steunpunt duwt, hoe makkelijker het gaat."),
            ("fig", svg.hefboom(400), "Een wip, een kruiwagen, een schaar en een flesopener zijn allemaal hefbomen."),
            ("p", "Je wint kracht, maar je verliest afstand: je moet je kant van de hefboom veel verder naar beneden duwen."),
        ]),
        dict(kop="Energie", blokken=[
            ("p", "Energie is wat nodig is om iets te laten gebeuren. Ze gaat nooit verloren, ze verandert alleen van vorm."),
            ("fig", svg.stappen(["Zon|licht", "Zonnepaneel|elektriciteit", "Lamp|licht en warmte"], kleur=svg.AMBER),
             "Bij elke omzetting gaat een deel als warmte weg. Daarom wordt een lamp warm."),
            ("fig", tabel(["Hernieuwbaar", "Niet hernieuwbaar"], [
                ["zon, wind, water", "steenkool, aardolie, aardgas"],
                ["raakt niet op", "raakt op, en geeft CO₂ bij verbranden"],
            ]), None),
        ]),
        dict(kop="Elektriciteit", blokken=[
            ("p", "Stroom loopt alleen door een <strong>gesloten kring</strong>. Zit er ergens een onderbreking, dan gebeurt er niets."),
            ("fig", svg.stroomkring(380), "De schakelaar opent of sluit de kring. Open kring, geen licht."),
            ("p", "Metalen <strong>geleiden</strong> stroom, dus die gebruik je in de draden. Plastic, rubber en hout doen dat niet: dat zijn <strong>isolatoren</strong>, en die zitten er net rond als bescherming."),
            ("weetje", "Stroom uit het stopcontact is levensgevaarlijk. Proeven doe je uitsluitend met een batterij."),
        ]),
        dict(kop="Licht en geluid", blokken=[
            ("p", "Licht gaat in rechte lijnen. Komt er iets voor te staan, dan krijg je een schaduw. Op een spiegel kaatst licht terug onder dezelfde hoek."),
            ("p", "Geluid ontstaat door <strong>trillingen</strong> en heeft lucht, water of een vaste stof nodig om zich voort te planten. In het luchtledige hoor je niets."),
            ("weetje", "Licht gaat veel sneller dan geluid. Daarom zie je de bliksem eerst en hoor je de donder pas daarna."),
        ]),
    ],
    onthoud=[
        "Een kracht is een duw of een trek.",
        "Zonder wrijving kan je niet stappen en niet remmen.",
        "Bij een hefboom win je kracht en verlies je afstand.",
        "Energie gaat niet verloren, ze verandert van vorm.",
        "Stroom loopt alleen door een gesloten kring.",
        "Licht gaat in rechte lijnen, geluid is trilling.",
    ])

BUNDELS["techniek-ontwerpen-en-maken"] = dict(
    vak=VAK, titel="Techniek: ontwerpen en maken",
    onder="Van een probleem naar iets dat werkt — en waarom het zelden in één keer lukt.",
    secties=[
        dict(kop="De ontwerpcyclus", blokken=[
            ("p", "Techniek begint nooit bij een idee, maar bij een probleem. Daarna doorloop je telkens dezelfde vijf stappen — en na de laatste begin je vaak opnieuw."),
            ("fig", svg.ontwerpcyclus(380), "Dat het na het testen terugkeert naar het begin, is geen mislukking. Zo hoort het."),
            ("p", "Werkt je eerste versie niet, dan heb je iets geleerd wat je vooraf niet kon weten. Dat is precies waarvoor het testen dient."),
        ]),
        dict(kop="Materiaal kiezen", blokken=[
            ("p", "Elk materiaal heeft eigenschappen die het geschikt of ongeschikt maken. Je kiest op basis van wat je voorwerp moet kunnen."),
            ("fig", tabel(["Materiaal", "Sterk punt", "Zwak punt"], [
                ["hout", "sterk, makkelijk te bewerken", "rot in water"],
                ["metaal", "heel sterk, geleidt stroom", "zwaar, kan roesten"],
                ["kunststof", "licht, goedkoop, roest niet", "slecht voor het milieu"],
                ["glas", "doorzichtig", "breekt makkelijk"],
                ["textiel", "soepel, licht", "scheurt, houdt niet tegen"],
            ]), "Een fietsframe uit glas zou doorzichtig zijn, maar één keer bruikbaar."),
        ]),
        dict(kop="Constructies stevig maken", blokken=[
            ("p", "De <strong>driehoek</strong> is de stevigste vorm die er is: hij kan niet vervormen zonder dat er een zijde breekt. Een vierkant kan wel scheeftrekken."),
            ("p", "Daarom zie je driehoeken in bruggen, kraanarmen, daken en steigers. Een schuine balk in een vierkant zetten maakt er twee driehoeken van, en dus iets dat stevig staat."),
        ]),
        dict(kop="Beweging doorgeven", blokken=[
            ("fig", tabel(["Overbrenging", "Waar je het ziet", "Wat het doet"], [
                ["tandwielen", "een klok, een boormachine", "draaien in elkaar, tegengestelde richting"],
                ["ketting", "een fiets", "draaien in dezelfde richting, over afstand"],
                ["riem", "een wasmachine", "zachter en stiller dan een ketting"],
                ["katrol", "een takel", "tillen met minder kracht"],
            ]), "Een klein tandwiel dat een groot aandrijft, draait sneller maar met minder kracht."),
        ]),
        dict(kop="Veilig en netjes werken", blokken=[
            ("fig", tabel(["Regel", "Waarom"], [
                ["meet twee keer, zaag één keer", "je kan er niets weer aanplakken"],
                ["klem je werkstuk vast", "een bewegend stuk hout is gevaarlijk"],
                ["bril op bij zagen of boren", "splinters komen recht op je af"],
                ["ruim op terwijl je bezig bent", "op een volle tafel gebeuren de ongelukken"],
            ]), None),
        ]),
        dict(kop="Techniek en de wereld", blokken=[
            ("p", "Elke uitvinding lost iets op en brengt iets nieuws mee. De auto maakte afstanden klein, maar bracht files en uitstoot. De smartphone bracht alles binnen handbereik, en tegelijk een scherm waar je moeilijk van wegkijkt."),
            ("p", "Wie iets ontwerpt, denkt dus verder dan of het werkt: wat kost het aan grondstoffen, hoe lang gaat het mee, en wat gebeurt ermee als het kapot is?"),
        ]),
    ],
    onthoud=[
        "Techniek begint bij een probleem, niet bij een idee.",
        "Testen en verbeteren horen bij het ontwerpen.",
        "Kies je materiaal op basis van wat het moet kunnen.",
        "De driehoek is de stevigste vorm.",
        "Tandwielen, ketting, riem en katrol geven beweging door.",
        "Meet twee keer, zaag één keer.",
    ])

if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)
