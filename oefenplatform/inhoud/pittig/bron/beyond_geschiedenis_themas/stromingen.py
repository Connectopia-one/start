"""Denkstromingen en kunststromingen van de 19de en 20ste eeuw — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

_KUNST = "Wikimedia Commons, zoek op de titel en de schilder. Publiek domein (de maker is meer dan 70 jaar dood). Neem liefst de versie van Google Art Project of van het museum zelf."

PRENTEN = [
    dict(bestand="abolitie-medaillon.webp", zelf=False,
         wat="Het medaillon van Josiah Wedgwood uit 1787: een geknielde man in ketenen met de tekst 'Am I not a man and a brother?'.",
         waar="Wikimedia Commons, zoek op 'Am I not a man and a brother medallion'. Publiek domein.",
         vragen="bronvraag: abolitionistische ideeën herkennen"),
    dict(bestand="slavenschip-brookes.webp", zelf=False,
         wat="De bekende tekening van het slavenschip Brookes (1788): bovenaanzicht van het schip vol mensen naast elkaar.",
         waar="Wikimedia Commons, zoek op 'Slave ship Brookes 1788'. Publiek domein.",
         vragen="bronvraag over doel en doelpubliek van de abolitionisten"),
    dict(bestand="eugenetica-boom.webp", zelf=False,
         wat="Het logo van het tweede internationale eugeneticacongres van 1921: een boom met wortels zoals 'biology', 'genetics' en de tekst 'Eugenics is the self direction of human evolution'.",
         waar="Wikimedia Commons, zoek op 'Eugenics congress logo 1921'. Publiek domein.",
         vragen="bronvraag: hoe eugenetica zich als wetenschap voorstelt"),
    dict(bestand="romantiek-friedrich.webp", zelf=False,
         wat="Caspar David Friedrich, 'Wandelaar boven de nevelzee' (1818).",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
    dict(bestand="realisme-courbet.webp", zelf=False,
         wat="Gustave Courbet, 'De steenkappers' (1849). Het origineel ging verloren in 1945, een zwart-witfoto of kleurenreproductie is goed.",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
    dict(bestand="impressionisme-monet.webp", zelf=False,
         wat="Claude Monet, 'Impressie, opkomende zon' (1872).",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
    dict(bestand="kubisme-gris.webp", zelf=False,
         wat="Juan Gris, 'Portret van Pablo Picasso' (1912). Werk van Picasso zelf is nog niet vrij, dat van Gris wel.",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
    dict(bestand="expressionisme-munch.webp", zelf=False,
         wat="Edvard Munch, 'De schreeuw' (1893), de geschilderde versie.",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
    dict(bestand="artnouveau-mucha.webp", zelf=False,
         wat="Een affiche van Alfons Mucha, bijvoorbeeld 'Job' (1896) of 'Gismonda' (1894).",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
    dict(bestand="abstract-kandinsky.webp", zelf=False,
         wat="Wassily Kandinsky, 'Compositie VII' (1913).",
         waar=_KUNST, vragen="welke kunststroming, kenmerken herkennen"),
]
# Surrealisme: Magritte, Dalí en Ernst zijn nog niet vrij. Die werken komen er als beschrijving in tekst, zoals bij popart.

VRAGEN = [
    # ------------------------------------------------ abolitionisme
    tabel(
        "Juist of fout? De opkomst van het abolitionisme.",
        [
            ("De beweging wilde de slavenhandel en de slavernij afschaffen.", J),
            ("Ze ontstond eind 18de eeuw, onder meer bij Britse quakers en andere christenen.", J),
            ("Ideeën uit de Verlichting over gelijkheid van alle mensen gaven haar argumenten.", J),
            ("Ze werd gesteund door de meeste plantage-eigenaars in het Caribisch gebied.", F),
        ],
        "Plantage-eigenaars verdienden aan slavernij en waren de grootste tegenstanders. De abolitionisten combineerden christelijke en verlichte argumenten.",
    ),
    met_prent("abolitie-medaillon.webp", mk(
        "Welk abolitionistisch idee benoem je in dit medaillon uit 1787?",
        [
            "Een tot slaaf gemaakte is een mens, gelijk aan wie naar hem kijkt",
            "Slaven moeten beter betaald worden voor hun werk op de plantages",
            "Slavernij is enkel aanvaardbaar als de eigenaar christen is",
            "Afrikanen moeten zelf hun eigen koloniën in Amerika kunnen stichten",
        ],
        0,
        "De vraag Ben ik geen mens en een broeder? doet een beroep op gelijkheid en op het christelijke idee van broederschap.",
    ), volgt=True),
    met_prent("slavenschip-brookes.webp", tabel(
        "Juist of fout? Abolitionisten verspreidden deze tekening van een slavenschip in duizenden exemplaren.",
        [
            ("Ze wilden het grote publiek tonen hoe onmenselijk het transport was.", J),
            ("De tekening werd gebruikt om steun te winnen voor petities aan het parlement.", J),
            ("Ze was bedoeld als reclame voor de reders van het schip.", F),
            ("Een tekening als deze is een bron over de strategie van de abolitionisten.", J),
        ],
        "Beeld was een krachtig wapen: zonder een woord te lezen begreep iedereen hoe mensen als vracht werden gestapeld.",
    ), volgt=True),
    sorteer(
        "Wie gebruikte dit argument rond 1800: een abolitionist of een voorstander van de slavernij?",
        ["Abolitionist", "Voorstander"],
        [
            ["Alle mensen zijn door God gelijk geschapen", "Abolitionist"],
            ["Niemand kan eigendom zijn van een ander mens", "Abolitionist"],
            ["Zonder slavenarbeid gaat de suikerhandel en dus onze welvaart ten onder", "Voorstander"],
            ["De plantage-eigenaars hebben recht op hun wettige bezit", "Voorstander"],
        ],
        "Morele en religieuze argumenten stonden tegenover economische belangen en eigendomsrecht.",
    ),
    volgorde(
        "Zet deze stappen naar het einde van de slavernij in de juiste volgorde.",
        [
            "Groot-Brittannië verbiedt de slavenhandel",
            "Groot-Brittannië schaft de slavernij in zijn koloniën af",
            "Nederland schaft de slavernij af in Suriname en de Antillen",
            "Na een burgeroorlog wordt de slavernij in de Verenigde Staten afgeschaft",
        ],
        "1807, 1833, 1863 en 1865. Eerst werd de handel verboden, pas daarna de slavernij zelf.",
    ),
    casus(
        "Een Brits pamflet uit 1791: Wie suiker uit West-Indië eet, eet het bloed van onze broeders. Laat de suiker staan tot de handel in mensen stopt. Ook de vrouwen in huis kunnen zo iets doen.",
        [
            mk(
                "Welk middel stellen de makers voor?",
                [
                    "Een boycot van producten die door slaven gemaakt zijn",
                    "Een gewapende opstand op de plantages in West-Indië",
                    "Het opkopen van slaven om ze daarna vrij te laten",
                    "Een verbod op elke vorm van handel met Amerika",
                ],
                0,
                "Door geen suiker te kopen, wilden ze de handel economisch raken. Zo konden ook mensen zonder stemrecht meedoen.",
            ),
            keuze(
                "Het pamflet richt zich tot [[*gewone gezinnen|plantage-eigenaars|slavenhandelaars]]. Dat het ook de vrouwen aanspreekt, toont dat het doelpubliek [[*breder|smaller|buitenlands]] was dan de kiezers.",
                "Vrouwen hadden geen stemrecht, maar beslisten wel wat er thuis gekocht werd. Ze speelden een grote rol in de beweging.",
            ),
        ],
    ),
    # ------------------------------------------------ sociaal darwinisme en eugenetica
    mk(
        "Herbert Spencer bedacht de uitdrukking survival of the fittest. Hoe gebruikten sociaal darwinisten dat idee?",
        [
            "Ze pasten de strijd om het bestaan uit de natuur toe op mensen, klassen en volkeren",
            "Ze wilden zieken en armen extra beschermen tegen de natuur",
            "Ze toonden aan dat alle volkeren even sterk zijn",
            "Ze bewezen dat dieren en mensen niets met elkaar te maken hebben",
        ],
        0,
        "Zo leek armoede of overheersing natuurlijk. Darwin zelf schreef over planten en dieren, niet over samenlevingen.",
    ),
    tabel(
        "Waarom is het sociaal darwinisme geen goede wetenschap? Juist of fout?",
        [
            ("Het past een biologische theorie zomaar toe op samenlevingen.", J),
            ("Het gaat ervan uit dat wie rijk of machtig is, ook biologisch beter is.", J),
            ("Het werd gebruikt om ongelijkheid goed te praten.", J),
            ("Het steunde op proeven die later perfect herhaald konden worden.", F),
        ],
        "Het is een ideologie in een wetenschappelijk jasje: het leidt uit macht af dat iemand beter is.",
    ),
    met_prent("eugenetica-boom.webp", mk(
        "Dit is het logo van een internationaal congres uit 1921. Hoe stelt de eugenetica zich hier voor?",
        [
            "Als een wetenschap die steunt op vele andere wetenschappen",
            "Als een oude volkswijsheid die van generatie op generatie doorgegeven wordt",
            "Als een religieuze beweging met een eigen geloofsleer",
            "Als een kunststroming die de natuur wil afbeelden",
        ],
        0,
        "De wortels van de boom zijn vakken zoals biologie, geneeskunde en statistiek. Zo wilde de beweging gezag uitstralen.",
    ), volgt=True),
    sorteer(
        "Hoort de maatregel bij positieve of negatieve eugenetica?",
        ["Positief: gewenste mensen aanmoedigen", "Negatief: ongewenste mensen tegenhouden"],
        [
            ["Wedstrijden voor het gezondste gezin", "Positief: gewenste mensen aanmoedigen"],
            ["Premies voor gezinnen met veel kinderen uit de gewenste groep", "Positief: gewenste mensen aanmoedigen"],
            ["Gedwongen sterilisatie van mensen met een beperking", "Negatief: ongewenste mensen tegenhouden"],
            ["Huwelijksverboden voor mensen met bepaalde ziektes", "Negatief: ongewenste mensen tegenhouden"],
        ],
        "Beide vormen gingen ervan uit dat de staat mag bepalen wie kinderen krijgt.",
    ),
    tabel(
        "Juist of fout? De eugenetica in de praktijk.",
        [
            ("De Brit Francis Galton bedacht het woord eugenetica eind 19de eeuw.", J),
            ("In de Verenigde Staten werden tienduizenden mensen gedwongen gesteriliseerd.", J),
            ("Ook in Zweden gebeurden gedwongen sterilisaties, tot in de jaren zeventig.", J),
            ("De eugenetica bleef beperkt tot nazi-Duitsland.", F),
        ],
        "Eugenetica was rond 1920 in veel landen populair, ook in democratieën. Nazi-Duitsland voerde ze het verst door.",
    ),
    open_(
        "Leg uit hoe het sociaal darwinisme en de eugenetica de weg mee vrijmaakten voor de rassenpolitiek van de nazi's.",
        "Het sociaal darwinisme leerde dat volkeren en rassen in een strijd verwikkeld zijn waarin de sterkste mag winnen. De eugenetica voegde eraan toe dat de staat het erfelijk materiaal van een volk moet verbeteren door te bepalen wie kinderen mag krijgen. De nazi's namen beide over: ze steriliseerden en vermoordden mensen met een beperking en voerden een rassenpolitiek die leidde tot de Holocaust.",
    ),
    # ------------------------------------------------ kunststromingen met een prent
    met_prent("romantiek-friedrich.webp", mk(
        "Caspar David Friedrich schilderde dit in 1818. Bij welke kunststroming hoort het?",
        ["Romantiek", "Realisme", "Impressionisme", "Kubisme"],
        0,
        "Een eenzame figuur tegenover een overweldigende natuur, vol gevoel en mysterie: typisch romantiek.",
    ), volgt=True),
    met_prent("realisme-courbet.webp", tabel(
        "Gustave Courbet, De steenkappers, 1849. Welke kenmerken van het realisme herken je?",
        [
            ("Gewone mensen bij zwaar werk als onderwerp.", J),
            ("Geen verfraaiing: versleten kleren en vermoeide houdingen.", J),
            ("Een droomwereld met onlogische combinaties.", F),
            ("Een groot formaat, dat vroeger voor helden en heiligen bedoeld was.", J),
        ],
        "Courbet gaf arbeiders het formaat van een historiestuk. Veel critici vonden dat toen schandalig.",
    ), volgt=True),
    met_prent("impressionisme-monet.webp", mk(
        "Een criticus spotte in 1874 met de titel van dit schilderij van Claude Monet. Zijn spotnaam werd de naam van een hele stroming. Welke?",
        ["Impressionisme", "Expressionisme", "Romantiek", "Surrealisme"],
        0,
        "De titel is Impressie, opkomende zon. Een indruk van licht op één moment, met losse toetsen geschilderd.",
    ), volgt=True),
    met_prent("kubisme-gris.webp", mk(
        "Juan Gris schilderde dit portret van een bevriende kunstenaar in 1912. Bij welke kunststroming hoort het?",
        ["Kubisme", "Art nouveau", "Realisme", "Romantiek"],
        0,
        "Het gezicht is in hoekige vlakken opgedeeld en van meerdere kanten tegelijk bekeken.",
    ), volgt=True),
    met_prent("expressionisme-munch.webp", mk(
        "Edvard Munch, De schreeuw, 1893. Van welke stroming geldt hij als een belangrijke voorloper?",
        ["Expressionisme", "Impressionisme", "Kubisme", "Art nouveau"],
        0,
        "De vervormde figuur en de golvende, onnatuurlijk gekleurde lucht tonen geen werkelijkheid maar een gevoel van angst.",
    ), volgt=True),
    met_prent("artnouveau-mucha.webp", mk(
        "Alfons Mucha maakte deze affiche in Parijs, eind 19de eeuw. Bij welke stroming hoort ze?",
        ["Art nouveau", "Kubisme", "Abstracte kunst", "Realisme"],
        0,
        "Sierlijke, golvende lijnen, haren als ranken en plantmotieven, en dat op een affiche: kunst in het dagelijks leven.",
    ), volgt=True),
    met_prent("abstract-kandinsky.webp", tabel(
        "Wassily Kandinsky, Compositie VII, 1913. Vergelijk met het werk van Piet Mondriaan: enkel rechte zwarte lijnen en vlakken in rood, geel, blauw en wit. Juist of fout?",
        [
            ("Geen van beide toont een herkenbare voorstelling.", J),
            ("Kandinsky werkt met vrije, bewegende vormen, Mondriaan met strakke geometrie.", J),
            ("Beide willen met kleur, lijn en vorm alleen iets uitdrukken.", J),
            ("Beide schilderen een landschap zoals het er in werkelijkheid uitziet.", F),
        ],
        "Twee wegen binnen de abstracte kunst: lyrisch en vrij bij Kandinsky, geometrisch en streng bij Mondriaan.",
    ), volgt=True),
    # ------------------------------------------------ kunststromingen zonder prent
    tabel(
        "Juist of fout? De romantiek.",
        [
            ("Romantici stelden gevoel en verbeelding boven het verstand.", J),
            ("Ze grepen graag terug naar de middeleeuwen en de eigen nationale geschiedenis.", J),
            ("Ze wilden alles zo wetenschappelijk en nuchter mogelijk afbeelden.", F),
            ("Het nationalisme van de 19de eeuw vond er veel inspiratie in.", J),
        ],
        "De romantiek was een reactie op de Verlichting: niet de rede, maar het gevoel, het verleden en het eigen volk stonden centraal.",
    ),

    sorteer(
        "Hoort het kenmerk eerder bij het impressionisme of bij het expressionisme?",
        ["Impressionisme", "Expressionisme"],
        [
            ["De indruk van licht en kleur op één moment vastleggen", "Impressionisme"],
            ["Buiten schilderen, in de open lucht", "Impressionisme"],
            ["Het innerlijke gevoel van de kunstenaar uitdrukken", "Expressionisme"],
            ["Vervormde figuren en felle, onnatuurlijke kleuren", "Expressionisme"],
        ],
        "De namen lijken op elkaar, maar het zijn bijna tegengestelden: indruk van buiten tegenover uitdrukking van binnen.",
    ),
    mk(
        "Welke uitvindingen maakten het impressionisme mee mogelijk?",
        [
            "Verf in tubes om buiten te schilderen en de fotografie",
            "De boekdrukkunst en het olieverf",
            "Elektrisch licht in het atelier en de film",
            "De computer en de digitale camera",
        ],
        0,
        "Met verf in tubes kon je naar buiten. En sinds de fotografie hoefde een schilder niet meer alles precies na te bootsen.",
    ),
    mk(
        "Waarom past het realisme goed bij de tijd waarin het ontstond?",
        [
            "Door de industrialisatie kwamen arbeiders en hun zware leven in beeld",
            "Kunstenaars vluchtten in dromen en het onderbewuste na een wereldoorlog",
            "De eerste foto's van de maan toonden een nieuwe wereld",
            "Koningen bestelden steeds meer portretten van zichzelf als held",
        ],
        0,
        "Het realisme groeide in de tijd van de sociale kwestie en de revolutiejaren rond 1848.",
    ),
    tabel(
        "Juist of fout? Het surrealisme.",
        [
            ("André Breton schreef in 1924 het eerste manifest van het surrealisme.", J),
            ("De surrealisten lieten zich inspireren door de theorieën van Freud over dromen en het onderbewuste.", J),
            ("Salvador Dalí schilderde smeltende klokken in een droomlandschap.", J),
            ("Surrealisten schilderden altijd volledig abstract, zonder herkenbare dingen.", F),
        ],
        "Surrealisten schilderden net vaak heel herkenbare dingen, maar in onmogelijke combinaties.",
    ),
    mk(
        "Een Belgische schilder maakte een zeer precies geschilderde pijp, met eronder de zin Dit is geen pijp. Wat wilde hij tonen?",
        [
            "Een schilderij van een pijp is zelf geen pijp, maar een voorstelling",
            "Dat roken ongezond is en verboden moest worden",
            "Dat hij niet goed genoeg kon tekenen om een pijp na te maken",
            "Dat het schilderij eigenlijk een landschap voorstelt",
        ],
        0,
        "René Magritte speelt met het verschil tussen beeld en werkelijkheid. Dat verwarrende spel is typisch voor zijn surrealisme.",
    ),
    koppel(
        "Bij welke stroming hoort deze Belgische kunstenaar?",
        [
            ["Victor Horta, die in Brussel huizen bouwde met ijzeren ranken en gebogen lijnen", "Art nouveau"],
            ["Constantin Meunier, die mijnwerkers en dokwerkers in brons goot", "Realisme"],
            ["Constant Permeke, die boeren en vissers in grove vormen en donkere kleuren schilderde", "Expressionisme"],
            ["Paul Delvaux, die slaapwandelende vrouwen in stille, droomachtige stations schilderde", "Surrealisme"],
        ],
        ["Kubisme"],
        "Ook in België waren alle grote stromingen vertegenwoordigd. Horta en Magritte zijn er wereldberoemd door.",
    ),
    sleep(
        "Het kubisme begon rond 1907 met Pablo Picasso en Georges [[Braque]]. Ze toonden een onderwerp van [[meerdere]] kanten tegelijk en braken het op in [[geometrische]] vlakken.",
        ["Monet", "één", "golvende"],
        "Niet wat het oog op één moment ziet, maar wat je van een ding weet, van alle kanten.",
    ),
    keuze(
        "De art nouveau houdt van [[*golvende|strakke|hoekige]] lijnen en motieven uit de [[*plantenwereld|machinebouw|geometrie]]. Ze was niet alleen schilderkunst, maar ook [[*architectuur en meubels|film en fotografie|muziek en theater]].",
        "Een totaalkunst: van gevel tot deurklink in dezelfde stijl.",
    ),
    open_(
        "Kies één van de kunstwerken uit dit hoofdstuk. Noem de stroming en leg met drie kenmerken uit waarom het werk daarbij hoort.",
        "Bijvoorbeeld De steenkappers van Courbet hoort bij het realisme: het toont gewone arbeiders, zonder iets mooier te maken dan het is, en op een groot formaat dat vroeger voor helden bedoeld was. Of Impressie, opkomende zon van Monet: impressionisme door het licht op één moment, de losse zichtbare toetsen en het schilderen van een indruk in plaats van details.",
    ),
]
