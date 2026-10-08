# -*- coding: utf-8 -*-
"""De p-waarde, het significantieniveau en de twee soorten fouten.

Het tweede deel van de hypothesetoets: rekenen en besluiten. De fiche vraagt
hier letterlijk "Je berekent de p-waarde met ICT", dus het rekenwerk mag met
de rekenapps. Wat een kind zelf moet kunnen, is het besluit nemen én het
besluit uitleggen in de taal van de opgave.

De vier dingen die hier altijd fout gaan, en daarom staan ze als vraag:
  1. De p-waarde omdraaien: ze is de kans op de data als H0 waar is, niet de
     kans dat H0 waar is. Dat is niet hetzelfde en het verschil is wezenlijk.
  2. H0 niet verwerpen lezen als H0 bewijzen. Een toets bewijst nooit iets;
     ze vindt tegenbewijs of ze vindt het niet.
  3. Significant verwarren met belangrijk. Een piepklein verschil wordt
     significant bij een grote steekproef.
  4. De type I-fout en de type II-fout verwisselen. De fiche noemt ze beide
     bij naam en vraagt "Je berekent de kans op het onterecht verwerpen van
     de nulhypothese": dat is alfa.

Deel 1 is de p-waarde en het significantieniveau.
Deel 2 is het besluit en de twee soorten fouten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de p-waarde bij een hypothesetoets?",
        opties=[
            "de kans op een resultaat dat minstens zo extreem is als H0 waar is",
            "de kans dat de nulhypothese waar is",
            "de kans dat je besluit juist is",
            "de kans dat de alternatieve hypothese in werkelijkheid waar is",
        ],
        antwoord=0,
        uitleg="Dat onderscheid is cruciaal: je rekent in de wereld waar H0 geldt en kijkt hoe vreemd je data daar zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het significantieniveau alfa?",
        opties=[
            "de grens waaronder je de nulhypothese verwerpt",
            "de kans dat de nulhypothese waar is",
            "de p-waarde die je uit je data berekent",
            "het aantal standaardafwijkingen van het gemiddelde",
        ],
        antwoord=0,
        uitleg="Je kiest alfa vooraf, meestal nul komma nul vijf. Is de p-waarde kleiner, dan verwerp je H0.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer verwerp je de nulhypothese?",
        opties=[
            "als de p-waarde kleiner is dan of gelijk aan alfa",
            "als de p-waarde groter is dan alfa",
            "als de p-waarde groter is dan nul komma vijf",
            "als de p-waarde gelijk is aan nul",
        ],
        antwoord=0,
        uitleg="Klein p betekent: zulke data zijn heel onwaarschijnlijk als H0 waar is. Dan twijfel je aan H0.",
    ),
    dict(
        type="waarofniet",
        vraag="Een p-waarde van nul komma nul drie leidt bij alfa gelijk aan nul komma nul vijf tot het verwerpen van H0.",
        antwoord=True,
        uitleg="Nul komma nul drie is kleiner dan nul komma nul vijf, dus je verwerpt H0.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een p-waarde van nul komma twaalf bij alfa gelijk aan nul komma nul vijf. Wat besluit je?",
        opties=[
            "je verwerpt H0 niet, er is te weinig bewijs tegen",
            "je verwerpt H0, want nul komma twaalf is groter dan nul komma nul vijf",
            "je besluit dat H0 waar is",
            "je moet een nieuwe steekproef nemen met een ander alfa",
        ],
        antwoord=0,
        uitleg="Te weinig bewijs is niet hetzelfde als geen effect. Je kan enkel zeggen dat je het niet aangetoond hebt.",
    ),
    dict(
        type="invultekst",
        vraag="Welk significantieniveau wordt het vaakst gebruikt? Geef het getal als decimaal.",
        antwoord=["0,05", "0.05"],
        uitleg="Nul komma nul vijf, of vijf procent. Soms wordt nul komma nul één gebruikt als men strenger wil zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kleinere p-waarde betekent sterker bewijs tegen de nulhypothese.",
        antwoord=True,
        uitleg="Hoe kleiner p, hoe vreemder je data zijn in de wereld van H0.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een p-waarde van nul komma nul nul één?",
        opties=[
            "zulke data komen in één op de duizend gevallen voor als H0 waar is",
            "de kans dat H0 waar is, bedraagt een duizendste",
            "de kans dat je besluit fout is, bedraagt een duizendste",
            "het verschil is duizend keer zo groot als verwacht",
        ],
        antwoord=0,
        uitleg="Dat is heel sterk bewijs tegen H0. Maar het blijft een uitspraak over de data, niet over de waarheid van H0.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker kiest alfa pas nadat hij de p-waarde kent. Waarom mag dat niet?",
        opties=[
            "dan kan hij alfa zo kiezen dat zijn gewenste besluit uitkomt",
            "dan wordt de p-waarde automatisch te groot",
            "dan mag hij de rekenapp niet meer gebruiken",
            "dan moet hij een tweezijdige toets nemen",
        ],
        antwoord=0,
        uitleg="Alfa hoort vast te staan vóór je rekent, net zoals de richting van H1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is alfa gelijk aan nul komma nul één strenger dan alfa gelijk aan nul komma nul vijf?",
        opties=[
            "je hebt sterker bewijs nodig voor je H0 verwerpt",
            "je verwerpt H0 dan sneller",
            "je steekproef moet dan kleiner zijn",
            "je moet dan altijd een eenzijdige toets gebruiken",
        ],
        antwoord=0,
        uitleg="De drempel ligt lager, dus de p-waarde moet nog kleiner zijn. Je verwerpt H0 dan minder snel.",
    ),
    dict(
        type="waarofniet",
        vraag="De p-waarde kan groter zijn dan één als het gevonden verschil heel groot is.",
        antwoord=False,
        uitleg="Nooit. Ze is een kans, dus altijd tussen nul en één. Krijg je meer dan één, dan is er iets fout ingetikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling schrijft: de p-waarde is nul komma nul vier, dus er is vier procent kans dat H0 waar is. Wat is er mis?",
        opties=[
            "de p-waarde is de kans op de data als H0 waar is, niet de kans dat H0 waar is",
            "de p-waarde moet in procent uitgedrukt worden en niet als decimaal",
            "vier procent is te weinig om een besluit op te baseren",
            "er is niets mis, dat is de juiste lezing van een p-waarde",
        ],
        antwoord=0,
        uitleg="De twee kansen zijn verschillende dingen. Dit is de meest gemaakte fout in heel de statistiek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een rechtszijdige toets vind je x met een streepje gelijk aan 52, terwijl H0 mu gelijk aan 50 stelt. Hoe bereken je de p-waarde?",
        opties=[
            "als de kans op een steekproefgemiddelde van 52 of meer onder H0",
            "als de kans op een steekproefgemiddelde van precies 52 onder H0",
            "als de kans op een steekproefgemiddelde van 50 of meer onder H0",
            "als het verschil tussen 52 en 50 gedeeld door 50",
        ],
        antwoord=0,
        uitleg="Minstens zo extreem betekent bij een rechtszijdige toets: dit resultaat of hoger.",
    ),
    dict(
        type="invultekst",
        vraag="Welke Griekse letter staat voor het significantieniveau? Eén woord.",
        antwoord=["alfa", "alpha", "α"],
        uitleg="Alfa, meestal gelijk aan nul komma nul vijf.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een tweezijdige toets vergelijk je de p-waarde met alfa gedeeld door twee.",
        antwoord=False,
        uitleg="Nee. De p-waarde van een tweezijdige toets telt beide staarten mee en wordt met alfa zelf vergeleken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoek met honderdduizend deelnemers vindt een verschil van nul komma één procent met een p-waarde van nul komma nul nul één. Wat besluit je?",
        opties=[
            "het verschil is significant maar praktisch misschien onbelangrijk",
            "het verschil is groot en belangrijk, want p is heel klein",
            "het verschil bestaat niet, want nul komma één procent is te klein",
            "de p-waarde is fout berekend bij zo'n grote steekproef",
        ],
        antwoord=0,
        uitleg="Bij een enorme steekproef wordt bijna elk verschil significant. Significant en belangrijk zijn twee verschillende vragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de p-waarde volgens de vakfiche?",
        opties=[
            "met de rekenapps, maar je noteert wel je werkwijze en je redenering",
            "met de hand, want ICT is bij dit leerdoel niet toegelaten",
            "door de vuistregel van achtenzestig procent toe te passen",
            "door het aantal extreme waarden in je steekproef te tellen",
        ],
        antwoord=0,
        uitleg="De fiche zegt: je berekent de p-waarde met ICT. Maar bij een open vraag moet je alle tussenstappen uitschrijven.",
    ),
    dict(
        type="waarofniet",
        vraag="Een p-waarde van precies nul komma nul vijf bij alfa gelijk aan nul komma nul vijf leidt tot het verwerpen van H0.",
        antwoord=True,
        uitleg="De afspraak is kleiner dan of gelijk aan alfa. Op de grens verwerp je dus.",
    ),
    dict(
        type="invultekst",
        vraag="Verwerp je H0 als de p-waarde groter is dan alfa? Antwoord met ja of nee.",
        antwoord=["nee", "neen"],
        uitleg="Dan verwerp je H0 niet. Dat betekent niet dat H0 bewezen is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee onderzoeken vinden hetzelfde verschil, maar het ene heeft n gelijk aan dertig en het andere n gelijk aan drieduizend. Wat verwacht je van de p-waarden?",
        opties=[
            "die van het grote onderzoek is kleiner",
            "die van het kleine onderzoek is kleiner",
            "ze zijn gelijk, want het verschil is hetzelfde",
            "dat valt niet te zeggen zonder het significantieniveau",
        ],
        antwoord=0,
        uitleg="Een grotere steekproef heeft minder spreiding, dus hetzelfde verschil valt daar veel sterker op.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een type I-fout?",
        opties=[
            "de nulhypothese verwerpen terwijl ze waar is",
            "de nulhypothese niet verwerpen terwijl ze fout is",
            "de alternatieve hypothese verkeerd formuleren",
            "de p-waarde met het verkeerde alfa vergelijken",
        ],
        antwoord=0,
        uitleg="Je roept een effect dat er niet is. De kans daarop is precies alfa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een type II-fout?",
        opties=[
            "de nulhypothese niet verwerpen terwijl ze fout is",
            "de nulhypothese verwerpen terwijl ze waar is",
            "een eenzijdige toets gebruiken waar een tweezijdige hoort",
            "de voorwaarden van het formularium niet controleren",
        ],
        antwoord=0,
        uitleg="Je mist een effect dat er wel is. Dat gebeurt vooral bij een kleine steekproef.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de kans op een type I-fout?",
        opties=["gelijk aan alfa", "gelijk aan de p-waarde", "gelijk aan één min alfa", "altijd nul komma vijf"],
        antwoord=0,
        uitleg="Daarom vraagt de fiche: je berekent de kans op het onterecht verwerpen van de nulhypothese. Dat is alfa.",
    ),
    dict(
        type="waarofniet",
        vraag="H0 niet verwerpen betekent dat H0 bewezen is.",
        antwoord=False,
        uitleg="Nooit. Je hebt enkel te weinig bewijs gevonden. Een toets bewijst geen nulhypothese.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een medische test zegt dat een gezonde patiënt ziek is. Welke fout is dat?",
        opties=[
            "een type I-fout, als H0 zegt dat de patiënt gezond is",
            "een type II-fout, als H0 zegt dat de patiënt gezond is",
            "geen van beide, dat is een meetfout",
            "een type I-fout, maar enkel als de test tweezijdig is",
        ],
        antwoord=0,
        uitleg="H0 wordt verworpen terwijl ze waar was. Dat heet in de geneeskunde een valspositief resultaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rookmelder gaat niet af terwijl er brand is. Welke fout is dat?",
        opties=[
            "een type II-fout, als H0 zegt dat er geen brand is",
            "een type I-fout, als H0 zegt dat er geen brand is",
            "geen van beide, dat is een defect",
            "een type II-fout, maar enkel als alfa klein is",
        ],
        antwoord=0,
        uitleg="H0 wordt niet verworpen terwijl ze fout was. Je mist het effect.",
    ),
    dict(
        type="waarofniet",
        vraag="Kleiner alfa kiezen verkleint de kans op een type I-fout maar vergroot de kans op een type II-fout.",
        antwoord=True,
        uitleg="Strenger zijn betekent minder valse alarmen en meer gemiste effecten. Je kan niet allebei verkleinen zonder een grotere steekproef.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verklein je de kans op allebei de soorten fouten tegelijk?",
        opties=[
            "door een grotere steekproef te nemen",
            "door alfa groter te maken",
            "door alfa kleiner te maken",
            "door van tweezijdig naar eenzijdig over te gaan",
        ],
        antwoord=0,
        uitleg="Alleen meer gegevens helpen op allebei de fronten. Aan alfa draaien verschuift enkel het ene naar het andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker verwerpt H0 en schrijft: de nieuwe methode werkt beter. Wat moet hij er nog bij zeggen?",
        opties=[
            "op welk significantieniveau hij dat besluit neemt",
            "hoeveel kans er is dat H0 waar is",
            "welk besluit hij liever had gekregen",
            "dat zijn besluit met zekerheid klopt",
        ],
        antwoord=0,
        uitleg="Zonder alfa is een besluit niet te beoordelen. De fiche vraagt ook dat je je keuze verklaart.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het onterecht verwerpen van de nulhypothese? Geef het soort fout.",
        antwoord=["type I-fout", "type 1-fout", "type I"],
        uitleg="Een type I-fout, met kans alfa.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij alfa gelijk aan nul komma nul vijf verwerp je gemiddeld één op de twintig keer een nulhypothese die waar is.",
        antwoord=True,
        uitleg="Nul komma nul vijf is een twintigste. Daarom is één significant resultaat nog geen zekerheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een team toetst twintig verschillende verbanden op alfa gelijk aan nul komma nul vijf en vindt er één significant. Wat zeg je?",
        opties=[
            "dat ene resultaat kan goed toeval zijn, want bij twintig toetsen verwacht je er één",
            "dat ene resultaat is daardoor nog sterker bewezen",
            "ze hadden alfa groter moeten nemen om meer te vinden",
            "twintig toetsen op dezelfde data mag altijd",
        ],
        antwoord=0,
        uitleg="Hoe meer je toetst, hoe meer valse alarmen. Dat heet het probleem van het meervoudig toetsen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe formuleer je een besluit na een toets correct?",
        opties=[
            "op het niveau van vijf procent is er voldoende bewijs dat het gemiddelde hoger is",
            "het is bewezen dat het gemiddelde hoger is",
            "de nulhypothese heeft vijf procent kans om waar te zijn",
            "het verschil is zeker geen toeval",
        ],
        antwoord=0,
        uitleg="Noem het significantieniveau, zeg bewijs en niet bewezen, en vertaal het terug naar de taal van de opgave.",
    ),
    dict(
        type="waarofniet",
        vraag="Een type I-fout en een type II-fout kunnen bij dezelfde toets tegelijk gebeuren.",
        antwoord=False,
        uitleg="H0 is waar of ze is fout, niet allebei. Dus maar één van de twee fouten kan zich voordoen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een gerechtelijk proces is H0 dat de verdachte onschuldig is. Wat is dan een type I-fout?",
        opties=[
            "een onschuldige wordt schuldig verklaard",
            "een schuldige wordt door de rechter vrijgesproken",
            "het proces wordt uitgesteld",
            "de verdachte bekent zonder bewijs",
        ],
        antwoord=0,
        uitleg="Daarom stelt het recht alfa heel klein: liever een schuldige vrij dan een onschuldige in de cel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is H0 niet verwerpen iets anders dan H0 aanvaarden?",
        opties=[
            "het kan ook aan een te kleine steekproef liggen in plaats van aan de waarheid van H0",
            "H0 aanvaarden mag enkel bij een tweezijdige toets",
            "H0 aanvaarden vraagt een p-waarde groter dan nul komma vijf",
            "er is geen verschil, het zijn twee manieren om hetzelfde te zeggen",
        ],
        antwoord=0,
        uitleg="Geen bewijs vinden is geen bewijs van geen effect. Dat onderscheid wordt op het examen nagekeken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het onterecht niet verwerpen van de nulhypothese? Geef het soort fout.",
        antwoord=["type II-fout", "type 2-fout", "type II"],
        uitleg="Een type II-fout: je mist een effect dat er wel is.",
    ),
    dict(
        type="waarofniet",
        vraag="Een significant resultaat zegt hoe groot het effect is.",
        antwoord=False,
        uitleg="Het zegt enkel dat het verschil moeilijk aan toeval toe te schrijven is. Voor de grootte heb je het verschil zelf nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fabrikant wil vermijden dat hij een goede partij afkeurt. Wat doet hij met alfa?",
        opties=[
            "hij maakt alfa kleiner",
            "hij maakt alfa groter",
            "hij laat alfa op nul komma vijf staan",
            "hij kiest alfa gelijk aan de p-waarde",
        ],
        antwoord=0,
        uitleg="Een goede partij afkeuren is hier de type I-fout, en die kans is alfa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker meldt: p is nul komma nul zeven, dus er is geen verschil. Wat zou je hem zeggen?",
        opties=[
            "zeg liever dat er te weinig bewijs is, een verschil kan er wel degelijk zijn",
            "hij heeft gelijk, boven nul komma nul vijf is er zeker geen verschil",
            "hij moet alfa op nul komma één zetten zodat het toch significant wordt",
            "hij moet de toets tweezijdig maken om een verschil te vinden",
        ],
        antwoord=0,
        uitleg="Nul komma nul zeven is zwak bewijs, niet geen bewijs. Mogelijk was de steekproef gewoon te klein.",
    ),
]
