"""Kunst en cultuur: een kunstwerk analyseren — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

_W = "Staat al op het platform (Beyond doorstroom)."
PRENTEN = [
    dict(bestand="romantiek-friedrich.webp", zelf=False, wat="Caspar David Friedrich, 'Wandelaar boven de nevelzee' (1818).", waar=_W, vragen="stroming herkennen"),
    dict(bestand="realisme-courbet.webp", zelf=False, wat="Gustave Courbet, 'De steenkappers' (1849).", waar=_W, vragen="kenmerken realisme"),
    dict(bestand="impressionisme-monet.webp", zelf=False, wat="Claude Monet, 'Impressie, opkomende zon' (1872).", waar=_W, vragen="stroming herkennen"),
    dict(bestand="expressionisme-munch.webp", zelf=False, wat="Edvard Munch, 'De schreeuw' (1893).", waar=_W, vragen="stroming herkennen"),
    dict(bestand="abstract-kandinsky.webp", zelf=False, wat="Wassily Kandinsky, 'Compositie VII' (1913).", waar=_W, vragen="abstracte kunst"),
    dict(bestand="artnouveau-mucha.webp", zelf=False, wat="Affiche van Alfons Mucha.", waar=_W, vragen="art nouveau"),
    dict(bestand="millet-arenleesters.webp", zelf=False, wat="Jean-François Millet, 'De arenleesters' (1857).", waar=_W, vragen="analyse in stappen"),
    dict(bestand="justitiepaleis-brussel.webp", zelf=False, wat="Het Justitiepaleis in Brussel (1866-1883).", waar=_W, vragen="een gebouw als bron"),
]

VRAGEN = [
    # --- werkwijze
    volgorde(
        "Zet de stappen van een kunstanalyse in een goede volgorde.",
        ["Beschrijven wat je werkelijk ziet", "Vormkenmerken: kleur, lijn, compositie en materiaal", "Functie en opdrachtgever", "De context: tijd en samenleving", "Besluiten wat het werk vertelt"],
        "Eerst vaststellen, dan verklaren. Wie met zijn mening begint, ziet de helft niet meer.",
    ),
    tabel(
        "Bij welke vraag van de analyse hoort elke opmerking?",
        [
            ("Het licht valt op de figuur in het midden.", "Vormkenmerken"),
            ("Het hing in een kerk boven het altaar.", "Functie"),
            ("Een rijke bankier betaalde het werk.", "Opdrachtgever"),
            ("Het werd gemaakt in de tijd van de industriële revolutie.", "Context"),
        ],
        "Vorm, functie, opdrachtgever en context: elk een andere vraag.",
        kolommen=["Vormkenmerken", "Functie", "Opdrachtgever", "Context"],
    ),
    mk(
        "Waarom begin je een analyse beter niet met je mening?",
        [
            "Je ziet dan de helft niet meer",
            "Een mening is in de geschiedenis altijd verboden",
            "De opdrachtgever wil je mening niet kennen",
            "Een kunstwerk heeft nooit een betekenis",
        ],
        0,
        "Wie met zijn mening begint, zoekt in het werk alleen de bevestiging van wat hij al dacht.",
    ),
    casus(
        "Een historicus vindt een geschilderd portret uit 1880: een fabrikant in zijn salon, met boekenkasten, zware meubels, een gouden horlogeketting en een raam met uitzicht op zijn fabriek.",
        [
            mk(
                "Wat wilde de fabrikant met dit portret vooral tonen?",
                [
                    "Zijn rijkdom en zijn stand",
                    "Hoe arm de arbeiders in zijn fabriek waren",
                    "Dat hij liever op het platteland woonde",
                    "Dat hij een groot schilder was",
                ],
                0,
                "Boeken, meubels, kledij en de fabriek in het raam zijn geen toeval.",
            ),
            tabel(
                "Waarvoor is dit portret een goede bron?",
                [
                    ("Hoe een rijke burger gezien wilde worden", J),
                    ("De smaak van de burgerij rond 1880", J),
                    ("De werkomstandigheden in zijn fabriek", F),
                ],
                "Een kunstwerk is vooral een bron over de ideeën en de smaak van zijn eigen tijd.",
            ),
        ],
    ),
    mk(
        "Een schilderij uit 1890 toont een veldslag uit 1302. Waarom is het geen betrouwbaar verslag van die slag?",
        [
            "Het werd veel later gemaakt, met een bedoeling",
            "Schilderijen tonen altijd precies wat er gebeurde",
            "In 1890 bestond er nog geen verf",
            "De slag van 1302 heeft nooit plaatsgevonden",
        ],
        0,
        "De maker kiest wat hij toont en wie groot in beeld komt. Het zegt meer over 1890 dan over 1302.",
    ),
    met_prent("justitiepaleis-brussel.webp", tabel(
        "Bekijk het Justitiepaleis in Brussel, gebouwd tussen 1866 en 1883. Wat kun je uit dit gebouw afleiden?",
        [
            ("De jonge staat wilde macht en grootsheid tonen.", J),
            ("Er was veel geld en techniek voor nodig.", J),
            ("Ook een gebouw kun je als bron lezen.", J),
            ("Het werd gebouwd als kleine, eenvoudige woning.", F),
        ],
        "Je leest er materiaal, stijl en de bedoeling van de bouwer uit.",
    )),
    # --- stijlen 19de eeuw
    met_prent("romantiek-friedrich.webp", mk(
        "Caspar David Friedrich schilderde dit in 1818: een eenzame figuur kijkt uit over een overweldigende natuur. Bij welke stroming hoort het?",
        ["Romantiek", "Realisme", "Impressionisme", "Abstracte kunst"],
        0,
        "Gevoel, verbeelding en ontzag voor de natuur: typisch romantiek.",
    )),
    met_prent("realisme-courbet.webp", tabel(
        "Gustave Courbet, De steenkappers, 1849. Welke kenmerken van het realisme herken je?",
        [
            ("Gewone mensen bij zwaar werk", J),
            ("Geen opsmuk: versleten kleren en vermoeide houdingen", J),
            ("Een droomwereld met onlogische combinaties", F),
        ],
        "Het realisme bracht het leven van arbeiders en boeren in beeld, wat toen nieuw was.",
    )),
    met_prent("impressionisme-monet.webp", mk(
        "Claude Monet, Impressie, opkomende zon, 1872. Waar gaat dit werk vooral over?",
        [
            "Licht en kleur op het moment van kijken",
            "Een nauwkeurige kaart van de haven",
            "Het harde werk van havenarbeiders",
            "Een droom zonder herkenbare vormen",
        ],
        0,
        "Losse, zichtbare toetsen geven de indruk van één moment.",
    )),
    casus(
        "Jean-François Millet, De arenleesters, 1857. Drie vrouwen rapen gebukt de laatste aren op een geoogst veld. Op de achtergrond ligt een grote oogst.",
        [
            met_prent("millet-arenleesters.webp", mk(
                "Bij welke stroming hoort dit werk?",
                ["Realisme", "Romantiek", "Expressionisme", "Art nouveau"],
                0,
                "Arme vrouwen bij zwaar werk, zonder opsmuk: realisme.",
            )),
            tabel(
                "Welke vragen helpen om dit werk in zijn context te plaatsen?",
                [
                    ("Hoe leefden arme plattelandsvrouwen rond 1850?", J),
                    ("Waarom vonden sommige rijke kijkers dit onderwerp storend?", J),
                    ("Welke kleur had de verf in de tube?", F),
                ],
                "Context gaat over tijd en samenleving. Het contrast tussen de grote oogst en de arme vrouwen zegt iets over die samenleving.",
            ),
        ],
    ),
    sorteer(
        "Welke stroming hoort bij elk kenmerk?",
        ["Romantiek", "Realisme", "Impressionisme"],
        [
            ["het eigen verleden en de eigen taal", "Romantiek"],
            ["arbeid zonder opsmuk", "Realisme"],
            ["licht op één moment", "Impressionisme"],
            ["gevoel en verbeelding", "Romantiek"],
            ["een zichtbare toets", "Impressionisme"],
            ["het leven van boeren", "Realisme"],
        ],
        "Drie stijlen van de negentiende eeuw, elk met een eigen blik.",
    ),
    mk(
        "Waarom kun je zeggen dat de romantiek het nationalisme voedde?",
        [
            "Ze gaf aandacht aan eigen taal en verleden",
            "Ze toonde enkel abstracte vormen",
            "Ze schilderde vooral fabrieken",
            "Ze werd verboden door de nationalisten",
        ],
        0,
        "Een gedeeld verleden en een eigen taal gaven de natie een verhaal.",
    ),
    tabel(
        "Welke kunstvormen waren nieuw in de negentiende en twintigste eeuw?",
        [
            ("De fotografie", J),
            ("De film", J),
            ("Fresco's", F),
            ("Glasramen", F),
        ],
        "Fresco's en glasramen bestonden al eeuwen.",
    ),
    # --- architectuur
    met_prent("artnouveau-mucha.webp", mk(
        "Deze affiche van Alfons Mucha heeft sierlijke, golvende lijnen en plantmotieven. Welke Belgische architect staat voor dezelfde stijl in Brussel?",
        ["Victor Horta", "René Magritte", "Pieter Bruegel", "Jan van Eyck"],
        0,
        "Art nouveau, in Duitsland jugendstil: gebogen lijnen, ijzer en glas.",
    )),
    tabel(
        "Welke uitspraken over nieuwe bouwmaterialen kloppen?",
        [
            ("Staal en gewapend beton kwamen uit de industrie.", J),
            ("Glas in grote vlakken maakte grote hallen en stations mogelijk.", J),
            ("De Eiffeltoren en later wolkenkrabbers werden zo mogelijk.", J),
            ("Ze werden al in de middeleeuwen gebruikt voor kathedralen.", F),
        ],
        "Nieuwe materialen maakten nieuwe bouwstijlen mogelijk.",
    ),
    keuze(
        "De art nouveau is de bouwstijl rond [[*1900|1800|1950]] met gebogen lijnen, [[*ijzer en glas|marmer en goud|hout en riet]]. In Duitsland heet ze [[*jugendstil|romantiek|realisme]].",
        "Victor Horta was er in Brussel een meester van.",
    ),
    # --- 20ste eeuw
    met_prent("expressionisme-munch.webp", mk(
        "Edvard Munch, De schreeuw, 1893. De figuur is vervormd en de lucht onnatuurlijk gekleurd. Welke stroming kondigt dit aan?",
        ["Expressionisme", "Impressionisme", "Realisme", "Romantiek"],
        0,
        "Het gevoel wordt sterker dan de juiste weergave.",
    )),
    met_prent("abstract-kandinsky.webp", tabel(
        "Wassily Kandinsky, Compositie VII, 1913. Welke uitspraken kloppen?",
        [
            ("Je herkent niets uit de werkelijkheid.", J),
            ("Kleur en vorm zijn zelf het onderwerp.", J),
            ("Het werk beeldt een landschap nauwkeurig af.", F),
        ],
        "Abstracte kunst geeft niets herkenbaars weer.",
    )),
    sorteer(
        "Impressionisme of expressionisme?",
        ["Impressionisme", "Expressionisme"],
        [
            ["licht op één moment", "Impressionisme"],
            ["vervormde vormen", "Expressionisme"],
            ["overdreven kleuren om een gevoel te tonen", "Expressionisme"],
            ["een zichtbare, lichte toets in de buitenlucht", "Impressionisme"],
        ],
        "De ene toont wat het oog ziet, de andere wat de kunstenaar voelt.",
    ),
    mk(
        "Je vergelijkt een realistisch werk uit 1870 met een abstract werk uit 1930. Wat is het grootste verschil?",
        [
            "Het eerste toont mensen, het tweede vorm en kleur",
            "Het eerste is een foto, het tweede een film",
            "Het eerste is abstract, het tweede realistisch",
            "Er is geen verschil, beide zijn landschappen",
        ],
        0,
        "Van het gewone leven zonder opsmuk naar kleur en vorm als onderwerp.",
    ),
    inv(
        "Welke Belgische kunstenaar werd wereldberoemd met surrealistische schilderijen?",
        ["René Magritte", "Magritte", "Rene Magritte"],
        "Magritte maakte werken waarin gewone dingen op onverwachte manieren samenkomen.",
    ),
    # --- kunst en macht
    casus(
        "Een schilderij uit de Sovjet-Unie van 1935 toont sterke, lachende arbeiders bij een hoogoven. In de verte rookt een nieuwe fabriek. De kunstenaar kreeg de opdracht van de staat.",
        [
            mk(
                "Hoe lees je dit werk het best?",
                [
                    "Als kunst in dienst van het regime",
                    "Als een eerlijke foto van het werk in de fabriek",
                    "Als kritiek van een vrije kunstenaar op Stalin",
                    "Als abstracte kunst zonder boodschap",
                ],
                0,
                "Het socialistisch realisme was een voorgeschreven stijl die arbeid verheerlijkte.",
            ),
            tabel(
                "Welke uitspraken over kunst in totalitaire regimes kloppen?",
                [
                    ("Stijl en inhoud werden voorgeschreven.", J),
                    ("De nazi's noemden kunst die ze afwezen 'ontaard'.", J),
                    ("In 1937 hielden de nazi's een spottentoonstelling.", J),
                    ("Kunstenaars waren er volledig vrij.", F),
                ],
                "Kunst werd propaganda. Wat niet in de lijn lag, werd uit de musea gehaald.",
            ),
        ],
    ),
    open_(
        "Waarom schreven totalitaire regimes de kunstenaars voor wat en hoe ze moesten maken? Geef een voorbeeld.",
        "Totalitaire regimes wilden het denken van hun burgers beheersen. Kunst werd daarom propaganda, met een voorgeschreven stijl en inhoud. In de Sovjet-Unie moest het socialistisch realisme de arbeid en de plannen van het regime verheerlijken. In nazi-Duitsland werd kunst die het regime afwees 'ontaard' genoemd en uit de musea gehaald, met in 1937 een spottentoonstelling.",
    ),
    open_(
        "Leg uit waarom een historicus een kunstwerk altijd naast andere bronnen legt.",
        "Een kunstwerk is gemaakt met een bedoeling, vaak in opdracht, en soms veel later dan wat het toont. Het zegt veel over de ideeën en de smaak van zijn eigen tijd, maar is geen betrouwbaar verslag. Door het naast andere bronnen te leggen, toets je wat het werk wel en niet kan aantonen.",
    ),
    tabel(
        "Waarom doet het materiaal mee in de analyse?",
        [
            ("Marmer, beton of staal vragen geld en techniek.", J),
            ("Het materiaal kan iets zeggen over de opdrachtgever.", J),
            ("Het materiaal zegt nooit iets over de tijd.", F),
        ],
        "Wie in marmer laat bouwen, toont macht en rijkdom.",
    ),
    mk(
        "Welk verband zie je tussen kunst en samenleving in de twintigste eeuw?",
        [
            "Kunst volgde de breuken van haar tijd",
            "Kunst stond volledig los van de samenleving",
            "Kunst werd enkel nog in kerken gemaakt",
            "Kunst verdween door de film",
        ],
        0,
        "Oorlog, techniek, stad en massamedia zijn er allemaal in terug te vinden.",
    ),
    sleep(
        "De manier waarop de delen over het vlak verdeeld zijn, heet de [[compositie]]. Wie het werk betaalt, is de [[opdrachtgever]]. De tijd en samenleving errond vormen de [[context]].",
        ["functie", "techniek"],
        "Drie begrippen uit de werkwijze.",
    ),
]
