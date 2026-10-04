# -*- coding: utf-8 -*-
"""Mutaties, mutagenen en kanker — 🌍 Beyond, biologie.

Deel 1 gaat over de genmutaties: substitutie, deletie en insertie, wat ze met
de aminozuurvolgorde doen, welke mutagenen ze kunnen veroorzaken, en wanneer
een mutatie erfelijk is. Deel 2 gaat over de chromosoom- en genoommutaties en
over de rol van mutaties bij het ontstaan van kanker.

De fiche vraagt dat de leerling bij gegeven informatie over een mutatie
uitlegt of en hoe die de aminozuursequentie verandert. Daarom staan er in
deel 1 vier vragen waarin een korte sequentie met en zonder de mutatie
vergeleken moet worden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een mutatie?",
        opties=[
            "een blijvende verandering in het DNA",
            "een tijdelijke verandering in de genexpressie",
            "een fout in het aflezen van het mRNA",
            "een verandering in de vorm van een eiwit",
        ],
        antwoord=0,
        uitleg="Een mutatie zit in de letters van het DNA zelf en gaat bij elke celdeling "
        "mee. Verandert alleen de leesbaarheid, dan is het epigenetica.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor een geïnduceerde mutatie? Kruis alles aan wat juist is.",
        opties=[
            "ze komt door een invloed van buitenaf",
            "straling of een gifstof kan ze veroorzaken",
            "ze ontstaat vanzelf bij het kopiëren van het DNA",
            "ze zit altijd in een geslachtscel",
        ],
        antwoord=[0, 1],
        uitleg="Een geïnduceerde mutatie komt van een mutageen, zoals straling of een "
        "gifstof. Een kopieerfout die vanzelf blijft staan, heet een spontane mutatie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een stof of een straling die mutaties veroorzaakt?",
        antwoord=["mutageen", "een mutageen", "mutagenen"],
        uitleg="Röntgenstraling, UV-licht, vrije radicalen en benzopyreen uit tabaksrook "
        "zijn mutagenen. Ze beschadigen het DNA rechtstreeks of via tussenstoffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke invloeden zijn mutagenen? Kruis alles aan wat juist is.",
        opties=[
            "UV-straling van de zon",
            "benzopyreen uit tabaksrook",
            "zuurstof uit de ingeademde lucht",
            "water uit de kraan",
        ],
        antwoord=[0, 1],
        uitleg="Ioniserende en UV-straling, vrije radicalen, nitrieten en nitrosaminen "
        "beschadigen het DNA. Gewone lucht en water doen dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe beschadigt UV-straling het DNA?",
        opties=[
            "twee naast elkaar liggende basen plakken aan elkaar",
            "het hele chromosoom breekt daardoor in twee losse stukken",
            "de kern verliest haar membraan",
            "de histonen worden gemethyleerd",
        ],
        antwoord=0,
        uitleg="UV doet twee thyminen aan elkaar binden. Zo'n knik stoort de replicatie en "
        "kan na een slechte herstelling een mutatie geven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een puntmutatie?",
        opties=[
            "een verandering in één nucleotide",
            "een verandering in één heel chromosoom",
            "een verandering in het aantal chromosomen",
            "een verandering in het hele genoom",
        ],
        antwoord=0,
        uitleg="Bij een puntmutatie gaat het om één plaats in het DNA. Een substitutie, een "
        "deletie of een insertie van één nucleotide zijn alle drie puntmutaties.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een mutatie waarbij één base door een andere vervangen wordt?",
        antwoord=["substitutie", "een substitutie", "vervanging"],
        uitleg="Bij een substitutie blijft het aantal nucleotiden gelijk. Daarom verschuift "
        "het leesraam niet en verandert hoogstens één aminozuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een deletie van één nucleotide meestal erger dan een substitutie?",
        opties=[
            "het leesraam verschuift en alle codons erna veranderen",
            "er verdwijnt meteen een heel chromosoom",
            "de cel kan dan niet meer delen",
            "het DNA kan dan niet meer gekopieerd worden door de cel",
        ],
        antwoord=0,
        uitleg="Nucleotiden worden per drie gelezen. Valt er één weg, dan schuift alles op "
        "en klopt het hele eiwit vanaf dat punt niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gen leest AUG GCU UCA. Door een substitutie wordt het AUG GCC UCA. Wat verandert er?",
        opties=[
            "waarschijnlijk niets aan het eiwit",
            "het eiwit wordt een aminozuur korter",
            "het eiwit wordt een aminozuur langer",
            "alle aminozuren erna veranderen",
        ],
        antwoord=0,
        uitleg="GCU en GCC geven hetzelfde aminozuur, want de code is gedegenereerd. Zo'n "
        "mutatie heet een stille mutatie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een mutatie die het eiwit niet verandert?",
        antwoord=["stille mutatie", "stil", "een stille mutatie"],
        uitleg="Omdat verschillende codons hetzelfde aminozuur geven, blijft het eiwit soms "
        "gelijk. Daarnaast bestaan er verliesmutaties en winstmutaties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een substitutie maakt van een gewoon codon een stopcodon. Wat gebeurt er?",
        opties=[
            "het eiwit wordt te vroeg afgebroken en is te kort",
            "het eiwit wordt een flink stuk langer dan het normaal is",
            "het eiwit verandert maar in één aminozuur",
            "er verandert niets aan het eiwit",
        ],
        antwoord=0,
        uitleg="Op een stopcodon laat het ribosoom los. De keten stopt daar, en zo'n kort "
        "eiwit werkt meestal niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een verliesmutatie en een winstmutatie?",
        opties=[
            "bij een winstmutatie doet het eiwit iets meer of iets nieuws",
            "bij een winstmutatie verdwijnt er een stuk DNA",
            "bij een verliesmutatie komt er juist een gen bij in het DNA",
            "er is geen verschil tussen de twee",
        ],
        antwoord=0,
        uitleg="Een verliesmutatie legt een eiwit stil of verzwakt het. Een winstmutatie "
        "maakt het juist actiever, en dat kan even schadelijk zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke mutatie is schadelijk voor het organisme.",
        antwoord=False,
        uitleg="Veel mutaties zijn stil of onschadelijk, en een enkele keer geeft er een "
        "een voordeel. Zonder mutaties zou er geen variatie en dus geen evolutie zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is een mutatie erfelijk?",
        opties=[
            "als ze in een geslachtscel zit",
            "als ze in een lichaamscel zit",
            "als ze door straling komt",
            "als ze het eiwit verandert",
        ],
        antwoord=0,
        uitleg="Alleen wat in een eicel of een zaadcel zit, gaat naar het kind. Een mutatie "
        "in een huidcel blijft bij die persoon.",
    ),
    dict(
        type="waarofniet",
        vraag="Een mutatie in een huidcel door zonlicht wordt aan de kinderen doorgegeven.",
        antwoord=False,
        uitleg="Een huidcel is een lichaamscel. De mutatie gaat mee naar haar dochtercellen "
        "in de huid, maar niet naar de volgende generatie.",
    ),
    dict(
        type="invultekst",
        vraag="Bij welke aandoening is één aminozuur in het hemoglobine vervangen, waardoor de rode bloedcellen van vorm veranderen?",
        antwoord=["sikkelcelanemie", "sikkelcelziekte", "sikkelcelarmoede"],
        uitleg="Eén substitutie verandert één aminozuur, en daardoor plooit het hemoglobine "
        "anders. De rode bloedcellen krijgen dan hun sikkelvorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke aandoeningen komen van een genmutatie? Kruis alles aan wat juist is.",
        opties=[
            "mucoviscidose",
            "de ziekte van Huntington",
            "het syndroom van Klinefelter",
            "het syndroom van Down",
        ],
        antwoord=[0, 1],
        uitleg="Mucoviscidose en Huntington komen van een fout in één gen. Klinefelter en "
        "Down komen van een chromosoom te veel, dus van een genoommutatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een cel heeft enzymen die beschadigd DNA kunnen herstellen.",
        antwoord=True,
        uitleg="Herstelenzymen vinden en repareren de meeste schade. Pas wat ontsnapt of "
        "verkeerd hersteld wordt, blijft als mutatie staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom veroorzaken vrije radicalen schade aan het DNA?",
        opties=[
            "ze reageren met de basen en beschadigen ze",
            "ze knippen de chromosomen in stukken",
            "ze binden op de histonen",
            "ze vervangen de suikers van het DNA door gewone ribose",
        ],
        antwoord=0,
        uitleg="Een vrij radicaal is heel reactief en grijpt het eerste wat het tegenkomt "
        "aan. Zit dat in de kern, dan is dat vaak het DNA.",
    ),
    dict(
        type="waarofniet",
        vraag="Een insertie van drie nucleotiden laat het leesraam ongemoeid.",
        antwoord=True,
        uitleg="Drie nucleotiden zijn precies één codon. Er komt dus één aminozuur bij, "
        "maar de rest van het eiwit blijft kloppen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een chromosoommutatie?",
        opties=[
            "een verandering in de bouw van een chromosoom",
            "een verandering in één nucleotide",
            "een verandering in het aantal chromosomen",
            "een verandering in de genexpressie",
        ],
        antwoord=0,
        uitleg="Bij een chromosoommutatie verdwijnt, verdubbelt, draait of verhuist er een "
        "stuk. Het aantal chromosomen blijft meestal gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij een inversie?",
        opties=[
            "een stuk chromosoom komt omgekeerd terug",
            "een stuk chromosoom verdwijnt",
            "een stuk gaat naar een ander chromosoom",
            "het chromosoom wordt verdubbeld",
        ],
        antwoord=0,
        uitleg="Bij een inversie breekt een stuk los en wordt het andersom teruggeplaatst. "
        "De genen zijn er nog, maar in de omgekeerde volgorde.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het overgaan van een stuk chromosoom naar een niet-homoloog chromosoom?",
        antwoord=["translocatie", "een translocatie"],
        uitleg="Bij een translocatie verhuist een stuk naar een heel ander chromosoom. Het "
        "Philadelphiachromosoom is daarvan het bekendste voorbeeld.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Philadelphiachromosoom hoort bij het syndroom van Down.",
        antwoord=False,
        uitleg="Het hoort bij een vorm van leukemie. Een translocatie tussen chromosoom 9 "
        "en 22 maakt daar een gen dat de cel ongeremd laat delen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een genoommutatie?",
        opties=[
            "een verandering in het aantal chromosomen",
            "een verandering in de bouw van een chromosoom",
            "een verandering in één codon",
            "een verandering in de verpakking van het DNA",
        ],
        antwoord=0,
        uitleg="Bij een genoommutatie is er een chromosoom te veel of te weinig. Dat komt "
        "bijna altijd door een fout bij de meiose.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de fout bij de meiose waarbij twee chromosomen niet uit elkaar gaan?",
        antwoord=["non-disjunctie", "nondisjunctie", "non disjunctie"],
        uitleg="Door een non-disjunctie krijgt de ene gameet een chromosoom te veel en de "
        "andere een te weinig. Bevrucht zo'n gameet, dan heeft het kind een trisomie of een "
        "monosomie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een trisomie en een monosomie?",
        opties=[
            "bij een trisomie zijn er drie in plaats van twee",
            "bij een monosomie zijn er drie in plaats van twee",
            "bij een trisomie ontbreekt er een chromosoom",
            "er is geen verschil tussen de twee",
        ],
        antwoord=0,
        uitleg="Tri is drie, mono is één. Trisomie 21 betekent drie keer chromosoom 21, het "
        "syndroom van Turner één enkel X-chromosoom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke aandoeningen komen van een afwijkend aantal chromosomen? Kruis alles aan wat juist is.",
        opties=[
            "het syndroom van Down",
            "het syndroom van Turner",
            "sikkelcelanemie",
            "de ziekte van Huntington",
        ],
        antwoord=[0, 1],
        uitleg="Down is trisomie 21 en Turner is één X in plaats van twee. Sikkelcelanemie "
        "en Huntington zitten in één gen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het geval waarbij niet alle cellen van een persoon dezelfde chromosomenfout hebben?",
        antwoord=["mozaïcisme", "mozaicisme", "mozaïek"],
        uitleg="Als de fout pas na de bevruchting ontstaat, draagt maar een deel van de "
        "cellen ze. De verschijnselen zijn dan vaak milder.",
    ),
    dict(
        type="waarofniet",
        vraag="Een karyogram laat een genoommutatie zien, maar een genmutatie niet.",
        antwoord=True,
        uitleg="Een chromosoom te veel of te weinig valt op een karyogram meteen op. Eén "
        "veranderde base is daar niet op te zien; daarvoor is een DNA-onderzoek nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is carcinogenese?",
        opties=[
            "het geleidelijk ontstaan van kanker",
            "het herstellen van beschadigd DNA",
            "het stilleggen van een gen",
            "het delen van een gezonde cel",
        ],
        antwoord=0,
        uitleg="Kanker ontstaat niet door één mutatie maar door een opeenstapeling ervan. "
        "Daarom duurt het meestal jaren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een proto-oncogen?",
        opties=[
            "een gezond gen dat de celdeling aanstuurt",
            "een gen dat de celdeling afremt",
            "een gen dat alleen in tumoren voorkomt",
            "een gen zonder enige functie",
        ],
        antwoord=0,
        uitleg="Een proto-oncogen is een normaal gen voor groei en deling. Gaat het door "
        "een mutatie te hard werken, dan wordt het een oncogen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een tumorsuppressorgen? Kruis alles aan wat juist is.",
        opties=[
            "het legt de celcyclus stil bij schade",
            "het laat een beschadigde cel afsterven",
            "het versnelt de celdeling",
            "het verlengt de telomeren van de cel",
        ],
        antwoord=[0, 1],
        uitleg="Een tumorsuppressorgen remt af en keurt het DNA. Valt dat gen uit, dan "
        "blijft een beschadigde cel gewoon doordelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat moet er misgaan voor een cel een kankercel wordt? Kruis alles aan wat juist is.",
        opties=[
            "een gen voor groei gaat te hard werken",
            "een gen dat de deling afremt valt uit",
            "de cel verliest al haar chromosomen",
            "de cel stopt met eiwitten te maken",
        ],
        antwoord=[0, 1],
        uitleg="Een oncogen dat aanstaat en een tumorsuppressorgen dat uitvalt werken in "
        "dezelfde richting. Meestal zijn er meerdere van die fouten nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de uiteinden van een chromosoom, die bij elke deling korter worden?",
        antwoord=["telomeren", "telomeer", "de telomeren"],
        uitleg="Telomeren beschermen de uiteinden en slijten bij elke deling af. Daardoor "
        "kan een gewone cel zich maar een beperkt aantal keer delen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom blijft een kankercel zich eindeloos delen?",
        opties=[
            "ze zet haar telomerasegen weer aan",
            "ze heeft meer chromosomen dan normaal",
            "ze heeft geen controlepunten meer nodig",
            "ze deelt zonder haar DNA te kopiëren",
        ],
        antwoord=0,
        uitleg="Telomerase bouwt de telomeren weer op. Daardoor vervalt de natuurlijke "
        "limiet op het aantal delingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tumor laat nieuwe bloedvaten naar zich toe groeien.",
        antwoord=True,
        uitleg="Dat heet angiogenese. Zonder eigen aanvoer van zuurstof en voeding kan een "
        "gezwel niet groot worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt een angiogeneseremmer als behandeling?",
        opties=[
            "hij belet de tumor nieuwe bloedvaten te maken",
            "hij doodt alle delende cellen in het lichaam",
            "hij herstelt het beschadigde DNA",
            "hij verlengt de telomeren van gezonde cellen",
        ],
        antwoord=0,
        uitleg="Zonder nieuwe vaten krijgt de tumor te weinig voeding en groeit hij niet "
        "verder. Dat is gerichter dan een behandeling die elke delende cel treft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan genrepressie bij een behandeling tegen kanker helpen?",
        opties=[
            "een te actief gen wordt gericht stilgelegd",
            "alle genen van de cel worden stilgelegd",
            "het ontbrekende gen wordt teruggeplaatst",
            "de telomeren worden verlengd",
        ],
        antwoord=0,
        uitleg="Met bijvoorbeeld een klein RNA wordt het mRNA van een oncogen "
        "tegengehouden. De cel maakt dat eiwit dan niet meer en deelt trager.",
    ),
    dict(
        type="waarofniet",
        vraag="Kanker ontstaat meestal uit één enkele mutatie in één cel.",
        antwoord=False,
        uitleg="Er zijn meerdere mutaties nodig in dezelfde cellijn, vaak over jaren. "
        "Daarom stijgt de kans op kanker met de leeftijd.",
    ),
]
