# -*- coding: utf-8 -*-
"""Tweedegraadsfuncties en de transformaties van hun grafiek.

Het onderdeel "Tweedegraadsfuncties" van de analysefiche G1. De fiche vraagt
twee dingen: van voorschrift naar grafiek en terug, en de vier transformaties
van de grafiek van x kwadraat kunnen benoemen en uitvoeren.

Deel 1 is de parabool zelf: top, nulwaarden, symmetrieas, bereik.
Deel 2 zijn de vier transformaties en wat ze met de kenmerken doen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe heet de grafiek van een tweedegraadsfunctie?",
        opties=["een parabool", "een hyperbool", "een sinusoïde", "een rechte lijn"],
        antwoord=0,
        uitleg="De grafiek van één gedeeld door x heet een hyperbool, die van een eerstegraadsfunctie een rechte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer spreek je van een dalparabool?",
        opties=[
            "als de coëfficiënt van x kwadraat positief is",
            "als de coëfficiënt van x kwadraat negatief is",
            "als de constante term van de functie positief is",
            "als de functie twee verschillende nulwaarden heeft",
        ],
        antwoord=0,
        uitleg="Alleen het teken van a bepaalt de opening. Bij een negatieve a krijg je een bergparabool met een maximum.",
    ),
    dict(
        type="invultekst",
        vraag="Neem x kwadraat min zes x plus vijf. Wat is de x-coördinaat van de top? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg="De top ligt bij min b gedeeld door twee a, dus zes gedeeld door twee, wat drie geeft.",
    ),
    dict(
        type="waarofniet",
        vraag="De symmetrieas van een parabool gaat altijd door haar top.",
        antwoord=True,
        uitleg="Ze is de verticale rechte door de top, en die legt de twee takken precies op elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de discriminant van a x kwadraat plus b x plus c?",
        opties=[
            "b kwadraat min vier a c",
            "b kwadraat plus vier a c",
            "vier a c min b kwadraat",
            "a kwadraat min vier b c",
        ],
        antwoord=0,
        uitleg="Het teken van die uitkomst beslist over het aantal reële nulwaarden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel nulwaarden heeft een tweedegraadsfunctie met discriminant nul?",
        opties=["één", "twee", "geen", "oneindig veel"],
        antwoord=0,
        uitleg="De parabool raakt de x-as dan precies in haar top, zonder erdoorheen te gaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een parabool kan de verticale as twee keer snijden.",
        antwoord=False,
        uitleg="Voor x gelijk aan nul is er maar één functiewaarde, namelijk c. Elke functiegrafiek snijdt de y-as hoogstens één keer.",
    ),
    dict(
        type="invultekst",
        vraag="Neem x kwadraat min zes x plus vijf. Wat is de y-coördinaat van de top? Schrijf het getal.",
        antwoord=["-4", "min 4"],
        uitleg="Vul drie in: negen min achttien plus vijf is min vier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn de nulwaarden van x kwadraat min zes x plus vijf?",
        opties=[
            "één en vijf",
            "min één en min vijf",
            "twee en drie",
            "nul en zes",
        ],
        antwoord=0,
        uitleg="Je zoekt twee getallen met som zes en product vijf. De ontbinding is x min één maal x min vijf.",
    ),
    dict(
        type="waarofniet",
        vraag="Als een parabool twee nulwaarden heeft, ligt de x van de top precies in het midden ertussen.",
        antwoord=True,
        uitleg="De symmetrieas staat midden tussen de twee snijpunten met de x-as. Het gemiddelde van de nulwaarden geeft dus de top.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een dalparabool heeft als top het punt drie en min vier. Wat is haar bereik?",
        opties=[
            "alle getallen vanaf min vier",
            "alle getallen tot en met min vier",
            "alle getallen vanaf het getal drie",
            "alle reële getallen zonder uitzondering",
        ],
        antwoord=0,
        uitleg="Bij een dalparabool is de top het laagste punt, dus min vier is de kleinste functiewaarde en alles erboven komt voor.",
    ),
    dict(
        type="invultekst",
        vraag="Waar snijdt x kwadraat min zes x plus vijf de verticale as? Schrijf de y-waarde.",
        antwoord=["5", "vijf"],
        uitleg="Vul nul in voor x: enkel de constante term vijf blijft over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vergelijking heeft de symmetrieas van een parabool met top in het punt twee en zeven?",
        opties=[
            "x is gelijk aan twee",
            "y is gelijk aan zeven",
            "x is gelijk aan zeven",
            "y is gelijk aan twee",
        ],
        antwoord=0,
        uitleg="De symmetrieas is verticaal, dus ze heeft een vergelijking van de vorm x is een getal, en dat getal is de x van de top.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bergparabool heeft altijd een minimum.",
        antwoord=False,
        uitleg="Een bergparabool opent naar beneden, dus haar top is een maximum. Ze heeft helemaal geen kleinste waarde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een voorschrift in de vorm a maal x min p, in het kwadraat, plus q. Wat lees je daar meteen uit af?",
        opties=[
            "de coördinaten van de top zijn p en q",
            "de coördinaten van de top zijn min p en q",
            "de nulwaarden van de functie zijn p en q",
            "de symmetrieas heeft als vergelijking y is q",
        ],
        antwoord=0,
        uitleg="Dat heet de topvorm. Let op het minteken in de haakjes: x min drie geeft top in drie, niet in min drie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel punten heb je minstens nodig om één parabool vast te leggen?",
        opties=["drie", "twee", "vier", "één"],
        antwoord=0,
        uitleg="Er zijn drie onbekende coëfficiënten a, b en c, dus je hebt drie vergelijkingen nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe groter de absolute waarde van a, hoe smaller de parabool.",
        antwoord=True,
        uitleg="Een grote a rekt de grafiek verticaal uit, waardoor ze steiler en dus smaller oogt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel reële nulwaarden heeft een tweedegraadsfunctie met een negatieve discriminant? Schrijf het cijfer.",
        antwoord=["0", "nul", "geen"],
        uitleg="De parabool ligt dan volledig boven of volledig onder de x-as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de top van min x kwadraat plus vier x?",
        opties=[
            "het punt twee en vier",
            "het punt vier en twee",
            "het punt min twee en vier",
            "het punt twee en min vier",
        ],
        antwoord=0,
        uitleg="Min b op twee a is min vier gedeeld door min twee, dus twee. Invullen geeft min vier plus acht, dus vier.",
    ),
    dict(
        type="meerkeuze",
        vraag="De hoogte van een opgegooide bal volgt een bergparabool. Wat stelt de top voor?",
        opties=[
            "het hoogste punt van de baan",
            "het moment waarop de bal landt",
            "de hoogte waarop de bal vertrok",
            "de snelheid waarmee de bal vertrok",
        ],
        antwoord=0,
        uitleg="De top van een bergparabool is het maximum. De landing is de tweede nulwaarde en de beginhoogte lees je af op de verticale as.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat doet de grafiek van f van x plus drie, vergeleken met die van f?",
        opties=[
            "ze schuift drie eenheden omhoog",
            "ze schuift drie eenheden omlaag",
            "ze schuift drie eenheden naar rechts",
            "ze wordt drie keer verticaal uitgerekt",
        ],
        antwoord=0,
        uitleg="Wat buiten de functie bij de uitkomst komt, werkt verticaal. Wat binnen de haakjes bij x komt, werkt horizontaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de grafiek van f van x min twee, vergeleken met die van f?",
        opties=[
            "ze schuift twee eenheden naar rechts",
            "ze schuift twee eenheden naar links",
            "ze schuift twee eenheden naar beneden",
            "ze wordt twee keer verticaal samengedrukt",
        ],
        antwoord=0,
        uitleg="Een min binnen de haakjes schuift naar rechts. Dat voelt omgekeerd aan, en net daar gaat het meestal mis.",
    ),
    dict(
        type="invultekst",
        vraag="Je gaat van x kwadraat naar x kwadraat min vijf. Hoeveel eenheden schuift de grafiek omlaag? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg="De hele grafiek zakt vijf eenheden, dus ook de top.",
    ),
    dict(
        type="waarofniet",
        vraag="De grafiek van f van x plus drie, met de drie binnen de haakjes, ligt drie eenheden naar links.",
        antwoord=True,
        uitleg="Binnen de haakjes werkt alles omgekeerd: plus schuift naar links, min schuift naar rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke transformatie hoort bij min f van x?",
        opties=[
            "een spiegeling om de horizontale as",
            "een spiegeling om de verticale as",
            "een verschuiving van één naar beneden",
            "een spiegeling om de eerste bissectrice",
        ],
        antwoord=0,
        uitleg="Elke functiewaarde wisselt van teken, dus wat boven de x-as lag, komt er even ver onder te liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke transformatie hoort bij drie maal f van x?",
        opties=[
            "een verticale uitrekking met factor drie",
            "een horizontale uitrekking met factor drie",
            "een verschuiving van drie naar boven toe",
            "een verschuiving van drie naar rechts toe",
        ],
        antwoord=0,
        uitleg="Alle functiewaarden worden verdrievoudigd, dus de grafiek wordt driemaal zo hoog uitgerekt vanaf de x-as.",
    ),
    dict(
        type="waarofniet",
        vraag="De grafiek van twee maal x kwadraat is breder dan die van x kwadraat.",
        antwoord=False,
        uitleg="Ze is net smaller: elke functiewaarde verdubbelt, dus de parabool loopt sneller omhoog.",
    ),
    dict(
        type="invultekst",
        vraag="Neem x min vier, in het kwadraat, plus één. Wat is de x-coördinaat van de top? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg="In de topvorm lees je de top rechtstreeks af: vier en één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke transformatie laat de nulwaarden van een functie onveranderd?",
        opties=[
            "een verticale uitrekking met een factor",
            "een verschuiving naar boven met drie",
            "een verschuiving naar rechts met twee",
            "een verschuiving naar beneden met één",
        ],
        antwoord=0,
        uitleg="Nul maal een factor blijft nul, dus de snijpunten met de x-as blijven staan. Elke verschuiving verplaatst ze wel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verticale verschuiving verandert het bereik van een functie.",
        antwoord=True,
        uitleg="Alle functiewaarden schuiven mee op, dus de verzameling van de waarden schuift evenveel op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke transformaties brengen je van x kwadraat naar x plus één, in het kwadraat, min drie?",
        opties=[
            "één naar links en drie naar beneden",
            "één naar rechts en drie naar beneden",
            "één naar links en drie naar boven",
            "drie naar links en één naar beneden",
        ],
        antwoord=0,
        uitleg="Plus één binnen de haakjes schuift naar links, min drie erbuiten schuift omlaag. De top komt op min één en min drie.",
    ),
    dict(
        type="invultekst",
        vraag="Neem x min twee, in het kwadraat, plus zeven. Wat is de kleinste functiewaarde? Schrijf het getal.",
        antwoord=["7", "zeven"],
        uitleg="Een kwadraat is minstens nul, dus de kleinste waarde is zeven, bereikt in x gelijk aan twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je spiegelt een dalparabool om de horizontale as. Wat krijg je?",
        opties=[
            "een bergparabool met een maximum",
            "een dalparabool die hoger ligt",
            "dezelfde parabool, maar smaller",
            "een rechte door de oude top",
        ],
        antwoord=0,
        uitleg="Het teken van a draait om, dus de opening keert en het minimum wordt een maximum.",
    ),
    dict(
        type="waarofniet",
        vraag="Een horizontale verschuiving verandert het domein van een tweedegraadsfunctie.",
        antwoord=False,
        uitleg="Het domein van elke tweedegraadsfunctie is heel R, en dat blijft zo na verschuiven. Bij een wortelfunctie zou het wel veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie transformaties brengen je van x kwadraat naar twee maal x min één, in het kwadraat, plus drie?",
        opties=[
            "één naar rechts, verticaal uitrekken met twee, drie omhoog",
            "één naar links, verticaal uitrekken met twee, drie omhoog",
            "twee naar rechts, verticaal uitrekken met één, drie omhoog",
            "één naar rechts, spiegelen om de x-as, drie naar beneden",
        ],
        antwoord=0,
        uitleg="De top komt op één en drie, en de factor twee maakt de parabool smaller.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schuift een parabool twee omhoog. Wat gebeurt er met haar tekenverloop?",
        opties=[
            "het kan veranderen, want de nulwaarden verschuiven",
            "het blijft precies hetzelfde als daarvoor",
            "het keert overal om van teken",
            "het verdwijnt, want er zijn geen nulwaarden meer",
        ],
        antwoord=0,
        uitleg="Een dalparabool die net onder de as lag, kan er helemaal boven komen. Dan is ze overal positief en zijn de nulwaarden weg.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verticale verschuiving laat de symmetrieas van een parabool op haar plaats.",
        antwoord=True,
        uitleg="Alleen de hoogte verandert. De x van de top blijft dezelfde, dus ook de verticale symmetrieas.",
    ),
    dict(
        type="invultekst",
        vraag="Neem twee maal x min één, in het kwadraat, plus drie. Wat is de y-coördinaat van de top? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg="De factor twee verandert de ligging van de top niet, alleen de breedte van de parabool.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verloopt de linkertak van een gewone dalparabool?",
        opties=[
            "ze daalt, met een afnemende daling",
            "ze daalt, met een toenemende daling",
            "ze stijgt, met een toenemende stijging",
            "ze stijgt, met een afnemende stijging",
        ],
        antwoord=0,
        uitleg="Links van de top gaat de grafiek omlaag, maar steeds minder steil, tot ze in de top even vlak loopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een parabool heeft haar top in vier en twee en gaat door het punt vijf en vijf. Welk voorschrift past?",
        opties=[
            "drie maal x min vier, in het kwadraat, plus twee",
            "drie maal x plus vier, in het kwadraat, plus twee",
            "x min vier, in het kwadraat, plus twee",
            "drie maal x min vier, in het kwadraat, min twee",
        ],
        antwoord=0,
        uitleg="Begin met de topvorm en vul het extra punt in: vijf min vier is één, in het kwadraat één, dus a plus twee is vijf en a is drie.",
    ),
]
