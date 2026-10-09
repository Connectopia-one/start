# -*- coding: utf-8 -*-
"""Van brutoloon naar nettoloon.

Het tweede thema uit "ik ga werken". De fiche vraagt hier drie dingen:

  1. de stappen van brutoloon naar nettoloon, en dat apart voor arbeiders,
     bedienden en studenten
  2. het doel van de bedrijfsvoorheffing en van de sociale zekerheidsbijdrage
  3. hoe de gezinssituatie de bedrijfsvoorheffing beïnvloedt

De volgorde van de stappen is de kern, en ze is voor iedereen dezelfde:

    brutoloon
      min de sociale zekerheidsbijdrage   ->  belastbaar loon
      min de bedrijfsvoorheffing          ->  nettoloon

Wat verschilt, is wat er in die twee stappen gebeurt:

    bediende   de bijdrage wordt op het brutoloon berekend
    arbeider   de bijdrage wordt op 108 procent van het brutoloon berekend,
               een oude regel uit de tijd dat arbeiders per dag betaald werden
    student    binnen het studentencontract enkel een solidariteitsbijdrage,
               en geen bedrijfsvoorheffing

Dit thema houdt het bij die structuur en bij de bedoeling van elke inhouding.
Exacte tarieven en schijven staan er bewust niet in: die veranderen, en de
fiche vraagt ze niet.

Deel 1 is de stappen en de twee inhoudingen.
Deel 2 is arbeiders, bedienden en studenten, en de gezinssituatie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het brutoloon?",
        opties=[
            "het loon voor er iets van afgehouden wordt",
            "het bedrag dat op je rekening komt",
            "het loon na de sociale bijdrage maar voor de belasting",
            "het loon plus de bijdrage van je werkgever",
        ],
        antwoord=0,
        uitleg="Bruto is het startbedrag. Netto is wat er na alle inhoudingen overblijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het nettoloon?",
        opties=[
            "het bedrag dat je werkelijk op je rekening krijgt",
            "het loon voor er iets van afgehouden wordt",
            "het loon plus je vakantiegeld",
            "het bedrag waarop je belasting berekend wordt",
        ],
        antwoord=0,
        uitleg="Netto is het eindpunt van de berekening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt er als eerste van het brutoloon afgetrokken?",
        opties=[
            "de sociale zekerheidsbijdrage",
            "de bedrijfsvoorheffing",
            "de gemeentebelasting",
            "de btw",
        ],
        antwoord=0,
        uitleg="Eerst de sociale bijdrage, en wat overblijft is het belastbaar loon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet het bedrag dat overblijft na de sociale zekerheidsbijdrage?",
        opties=[
            "het belastbaar loon",
            "het nettoloon",
            "het brutoloon",
            "het vakantiegeld",
        ],
        antwoord=0,
        uitleg="Op dat bedrag wordt daarna de bedrijfsvoorheffing berekend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt er als tweede van je loon afgetrokken?",
        opties=[
            "de bedrijfsvoorheffing",
            "de sociale zekerheidsbijdrage",
            "de accijnzen",
            "de onroerende voorheffing",
        ],
        antwoord=0,
        uitleg="Die wordt op het belastbaar loon berekend en levert het nettoloon op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het doel van de sociale zekerheidsbijdrage?",
        opties=[
            "de sociale zekerheid mee financieren",
            "de belastingen van volgend jaar vooruitbetalen",
            "de kosten van de werkgever dekken",
            "het vakantiegeld opbouwen",
        ],
        antwoord=0,
        uitleg="Ze gaat naar de RSZ, die er onder meer pensioenen en uitkeringen mee betaalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het doel van de bedrijfsvoorheffing?",
        opties=[
            "een voorschot op je personenbelasting",
            "een bijdrage aan de sociale zekerheid",
            "een vergoeding voor je werkgever",
            "een premie voor je pensioen",
        ],
        antwoord=0,
        uitleg="Voorheffing betekent vooraf geheven. Bij de belastingaangifte wordt afgerekend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heet het een voorheffing?",
        opties=[
            "ze wordt vooraf geheven, in de plaats van pas bij de aangifte",
            "ze wordt enkel geheven bij wie vooruit betaalt",
            "ze wordt voor het brutoloon berekend",
            "ze gaat voor op alle andere belastingen",
        ],
        antwoord=0,
        uitleg="Zo moet je niet alles in één keer bijbetalen na je aangifte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je werkgever houdt te veel bedrijfsvoorheffing in. Wat gebeurt er dan?",
        opties=[
            "je krijgt het verschil terug na je belastingaangifte",
            "het geld is definitief weg",
            "het wordt het jaar erna van je loon afgetrokken",
            "je werkgever stort het zelf terug",
        ],
        antwoord=0,
        uitleg="Daarom is het een voorschot: bij de aangifte wordt de echte belasting berekend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welk document vind je de berekening van bruto naar netto terug?",
        opties=[
            "de loonfiche",
            "de arbeidsovereenkomst",
            "het arbeidsreglement",
            "het rekeninguittreksel",
        ],
        antwoord=0,
        uitleg="De fiche noemt de loonfiche uitdrukkelijk als mogelijk bronmateriaal op het examen.",
    ),
    dict(
        type="waarofniet",
        vraag="De bedrijfsvoorheffing wordt vóór de sociale zekerheidsbijdrage afgetrokken.",
        antwoord=False,
        uitleg="Omgekeerd: eerst de sociale bijdrage, dan pas de bedrijfsvoorheffing.",
    ),
    dict(
        type="waarofniet",
        vraag="De sociale zekerheidsbijdrage gaat naar de sociale zekerheid en niet naar de belastingen.",
        antwoord=True,
        uitleg="Ze financiert mee de pensioenen, de ziekteverzekering en de werkloosheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Het belastbaar loon is hetzelfde als het nettoloon.",
        antwoord=False,
        uitleg="Het belastbaar loon staat ertussenin: na de sociale bijdrage, voor de bedrijfsvoorheffing.",
    ),
    dict(
        type="waarofniet",
        vraag="De bedrijfsvoorheffing is een voorschot op de personenbelasting.",
        antwoord=True,
        uitleg="Bij de aangifte wordt het verschil bijbetaald of teruggestort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen zitten er tussen brutoloon en nettoloon?",
        opties=[
            "de sociale zekerheidsbijdrage aftrekken",
            "het belastbaar loon bepalen",
            "de bedrijfsvoorheffing aftrekken",
            "de btw aftrekken",
        ],
        antwoord=[0, 1, 2],
        uitleg="De btw zit in de prijs van wat je koopt en heeft niets met je loon te maken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het loon voor er iets van afgehouden wordt?",
        antwoord=["brutoloon", "het brutoloon", "bruto"],
        uitleg="Het eindpunt na alle inhoudingen is het nettoloon.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de inhouding die een voorschot is op je personenbelasting?",
        antwoord=["bedrijfsvoorheffing", "de bedrijfsvoorheffing"],
        uitleg="Ze wordt berekend op je belastbaar loon.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het bedrag tussen de sociale bijdrage en de bedrijfsvoorheffing in? Vul aan: het ... loon.",
        antwoord=["belastbaar", "belastbare"],
        uitleg="Op dat bedrag wordt de bedrijfsvoorheffing berekend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand verdient 2.400 euro bruto. Na de sociale bijdrage blijft er 2.086 euro over en na de bedrijfsvoorheffing 1.720 euro. Wat is het belastbaar loon?",
        opties=["2.086 euro", "2.400 euro", "1.720 euro", "314 euro"],
        antwoord=0,
        uitleg="Het belastbaar loon is wat overblijft na de sociale bijdrage en voor de belasting.",
    ),
    dict(
        type="meerkeuze",
        vraag="En hoeveel bedraagt in dat voorbeeld de bedrijfsvoorheffing?",
        opties=["366 euro", "314 euro", "680 euro", "1.720 euro"],
        antwoord=0,
        uitleg="2.086 min 1.720 is 366 euro.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Op welk bedrag wordt de sociale zekerheidsbijdrage van een bediende berekend?",
        opties=[
            "op zijn brutoloon",
            "op 108 procent van zijn brutoloon",
            "op zijn nettoloon",
            "op zijn belastbaar loon",
        ],
        antwoord=0,
        uitleg="Bij een bediende is het gewoon het brutoloon. De regel met 108 procent geldt voor arbeiders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welk bedrag wordt de sociale zekerheidsbijdrage van een arbeider berekend?",
        opties=[
            "op 108 procent van zijn brutoloon",
            "op zijn brutoloon",
            "op zijn nettoloon",
            "op 92 procent van zijn brutoloon",
        ],
        antwoord=0,
        uitleg="Een oude regel uit de tijd dat arbeiders per dag of per uur betaald werden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat houdt een werkgever in op het loon van een student met een studentencontract?",
        opties=[
            "enkel een solidariteitsbijdrage",
            "de gewone sociale zekerheidsbijdrage",
            "de bedrijfsvoorheffing en de gewone bijdrage",
            "niets, een student krijgt altijd bruto gelijk aan netto",
        ],
        antwoord=0,
        uitleg="Binnen het studentencontract geldt een lagere bijdrage in plaats van de gewone.",
    ),
    dict(
        type="meerkeuze",
        vraag="Betaalt een student met een studentencontract bedrijfsvoorheffing?",
        opties=[
            "nee, binnen het studentencontract niet",
            "ja, net als een bediende",
            "ja, maar aan een lager tarief",
            "enkel in de zomermaanden",
        ],
        antwoord=0,
        uitleg="Daarom ligt het verschil tussen bruto en netto bij een student veel kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ligt het nettoloon van een student dicht bij zijn brutoloon?",
        opties=[
            "er gaat enkel een solidariteitsbijdrage af en geen bedrijfsvoorheffing",
            "een student krijgt van de overheid een premie bovenop zijn uurloon",
            "een student werkt altijd deeltijds en betaalt daarom minder",
            "een student krijgt de ingehouden belasting meteen op zijn loon terug",
        ],
        antwoord=0,
        uitleg="De twee gewone inhoudingen vallen voor een groot deel weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat beïnvloedt volgens de fiche de hoogte van de bedrijfsvoorheffing?",
        opties=[
            "de gezinssituatie van de werknemer",
            "de sector waarin het bedrijf werkt",
            "het aantal jaren dat je al bij de werkgever bent",
            "de grootte van het bedrijf",
        ],
        antwoord=0,
        uitleg="De fiche vraagt uitdrukkelijk uit te leggen hoe de gezinssituatie de berekening beïnvloedt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee mensen verdienen hetzelfde bruto, maar de ene heeft twee kinderen ten laste. Wat verwacht je?",
        opties=[
            "die met kinderen ten laste houdt netto meer over",
            "die met kinderen ten laste houdt netto minder over",
            "ze houden allebei precies evenveel over",
            "het verschil zit in de sociale bijdrage",
        ],
        antwoord=0,
        uitleg="Kinderen ten laste verlagen de bedrijfsvoorheffing, dus het nettoloon ligt hoger.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar zit het verschil tussen die twee collega's in de berekening?",
        opties=[
            "in de bedrijfsvoorheffing",
            "in de sociale zekerheidsbijdrage",
            "in het brutoloon",
            "in het vakantiegeld",
        ],
        antwoord=0,
        uitleg="De sociale bijdrage hangt niet van je gezin af, de voorheffing wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Betaalt alleen de werknemer een bijdrage aan de RSZ?",
        opties=[
            "nee, de werkgever betaalt er bovenop een eigen bijdrage",
            "ja, enkel de werknemer draagt bij aan de sociale zekerheid",
            "ja, maar de overheid betaalt die bijdrage achteraf terug",
            "nee, enkel de werkgever betaalt een bijdrage aan de RSZ",
        ],
        antwoord=0,
        uitleg="Daarom kost een werknemer zijn werkgever meer dan zijn brutoloon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de loonkost voor een werkgever?",
        opties=[
            "het brutoloon plus zijn eigen bijdrage aan de RSZ",
            "het nettoloon van de werknemer",
            "het brutoloon min de bedrijfsvoorheffing",
            "het belastbaar loon",
        ],
        antwoord=0,
        uitleg="De werkgeversbijdrage komt bovenop het bruto en staat niet op de rekening van de werknemer.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een arbeider wordt de sociale bijdrage op 108 procent van het brutoloon berekend.",
        antwoord=True,
        uitleg="Bij een bediende gewoon op het brutoloon.",
    ),
    dict(
        type="waarofniet",
        vraag="Een student met een studentencontract betaalt de gewone sociale zekerheidsbijdrage.",
        antwoord=False,
        uitleg="Binnen het studentencontract geldt een solidariteitsbijdrage, die lager ligt.",
    ),
    dict(
        type="waarofniet",
        vraag="De gezinssituatie verandert de sociale zekerheidsbijdrage.",
        antwoord=False,
        uitleg="Ze verandert de bedrijfsvoorheffing. De sociale bijdrage staat los van je gezin.",
    ),
    dict(
        type="waarofniet",
        vraag="De werkgever betaalt bovenop het brutoloon nog een eigen bijdrage aan de RSZ.",
        antwoord=True,
        uitleg="Daarom is de loonkost hoger dan het brutoloon dat op je contract staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt er voor een student met een studentencontract?",
        opties=[
            "er gaat een solidariteitsbijdrage af",
            "er gaat geen bedrijfsvoorheffing af",
            "zijn netto ligt dicht bij zijn bruto",
            "hij betaalt dezelfde bijdrage als een bediende",
        ],
        antwoord=[0, 1, 2],
        uitleg="De laatste is net het verschil: een student betaalt niet de gewone bijdrage.",
    ),
    dict(
        type="invultekst",
        vraag="Op hoeveel procent van het brutoloon wordt de sociale bijdrage van een arbeider berekend? Antwoord met een getal.",
        antwoord=["108"],
        uitleg="Een oude regel uit de tijd dat arbeiders per dag betaald werden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de lagere bijdrage die een student binnen zijn studentencontract betaalt?",
        antwoord=["solidariteitsbijdrage", "de solidariteitsbijdrage"],
        uitleg="Ze komt in de plaats van de gewone sociale zekerheidsbijdrage.",
    ),
    dict(
        type="invultekst",
        vraag="Welke inhouding verandert mee met je gezinssituatie?",
        antwoord=["bedrijfsvoorheffing", "de bedrijfsvoorheffing"],
        uitleg="Kinderen ten laste verlagen ze, en dus stijgt je nettoloon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een arbeider en een bediende hebben allebei 2.000 euro bruto. Wie betaalt de hoogste sociale bijdrage?",
        opties=[
            "de arbeider, want bij hem rekent men op 108 procent",
            "de bediende, want hij verdient meer per uur",
            "allebei evenveel",
            "dat hangt af van hun gezinssituatie",
        ],
        antwoord=0,
        uitleg="Het percentage is hetzelfde, maar het bedrag waarop gerekend wordt, ligt bij de arbeider hoger.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat er op een loonfiche zowel een bedrag voor de RSZ als een voor de belasting?",
        opties=[
            "het zijn twee verschillende inhoudingen met een ander doel",
            "het is twee keer hetzelfde, maar anders berekend",
            "de RSZ gaat naar de werkgever en de belasting naar de staat",
            "de belasting is een correctie op de RSZ",
        ],
        antwoord=0,
        uitleg="De RSZ financiert de sociale zekerheid, de voorheffing is een voorschot op je personenbelasting.",
    ),
]
