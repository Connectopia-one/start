# -*- coding: utf-8 -*-
"""Pittige vragen bij "Krachten en stevigheid in een constructie" (✨ Spark, techniek).

Dezelfde leerstof als deel 1 en deel 2, toegepast op nieuwe voorwerpen en
constructies, met misvattingen over sterkte, stijfheid en stabiliteit.
"""

VRAGEN = [
    dict(
        type="meerkeuze",
        vraag="Bij een hangbrug hangt het wegdek aan kabels, en die kabels hangen aan hoge torens. Welke kracht werkt er vooral in de kabels en welke in de torens?",
        opties=[
            "Trek in de kabels, druk in de torens",
            "Druk in de kabels, trek in de torens",
            "Trek in de kabels en ook trek in de torens",
            "Torsie in de kabels, buiging in de torens",
        ],
        antwoord=0,
        uitleg="Het wegdek hangt aan de kabels en trekt ze uit elkaar: trekkracht. De torens dragen dat gewicht van boven, net als de pilaren van een brug: drukkracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kiest materialen voor een speeltuin: de kettingen van een schommel en de zuilen die een klimrek dragen. Welke keuze is het best?",
        opties=[
            "Staal voor de kettingen, beton of steen voor de zuilen",
            "Beton voor de kettingen, glas voor de zuilen van het rek",
            "Glas voor de kettingen, staal voor de zuilen van het rek",
            "Steen voor de kettingen, glas voor de zuilen van het rek",
        ],
        antwoord=0,
        uitleg="De kettingen krijgen trekkracht, en daarvoor is staal goed. De zuilen krijgen drukkracht, en daar kunnen beton en steen veel van verdragen. Beton en glas zijn slecht in trek, dus die horen niet in een ketting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een klasgenoot zegt: 'Mijn toren van blokken is heel sterk, er breekt niets aan, dus kan hij ook niet omvallen.' Wat is er fout aan die redenering?",
        opties=[
            "Sterk en stabiel zijn twee verschillende dingen",
            "Een toren van blokken kan nooit sterk zijn, wat je ook doet",
            "Stabiel betekent dat er niets breekt, dus hij heeft gelijk",
            "Een sterke toren valt juist altijd sneller om dan een zwakke",
        ],
        antwoord=0,
        uitleg="Sterkte zegt dat er niets breekt, stabiliteit zegt dat het niet omvalt. Een constructie kan sterk zijn en toch omvallen, bijvoorbeeld als ze hoog en smal is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tafel staat stevig en wiebelt niet. Leg je er een stapel boeken op, dan buigt het tafelblad flink door, maar het breekt niet. Welke eigenschap schiet tekort?",
        opties=[
            "De stijfheid",
            "De stabiliteit",
            "De sterkte",
            "Geen enkele, de tafel is in orde",
        ],
        antwoord=0,
        uitleg="De tafel valt niet om, dus de stabiliteit is in orde. Het blad breekt niet, dus het is sterk genoeg. Maar het vervormt veel onder belasting, en dat betekent dat de stijfheid tekortschiet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je bouwt voor een schoolproject een brug uit rietjes, met vierkante vakken. Als je er zijwaarts tegen duwt, trekt elk vak scheef. Wat helpt het best?",
        opties=[
            "In elk vak een schuin rietje tussen twee hoeken zetten",
            "Dikkere rietjes nemen en de vierkante vakken zo laten",
            "De vierkante vakken nog een stuk groter maken dan nu",
            "Extra plakband rond elke hoek van de vakken draaien",
        ],
        antwoord=0,
        uitleg="Een rechthoek of vierkant van losse staven trekt makkelijk scheef. Met een schuine staaf tussen twee hoeken maak je er twee driehoeken van, en een driehoek vervormt niet. Dikkere rietjes veranderen niets aan de vorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wringt een natte handdoek uit door de twee uiteinden in tegengestelde richting te draaien. Welke kracht werkt er op de handdoek?",
        opties=[
            "Een torsiekracht",
            "Een drukkracht",
            "Een buigkracht",
            "Alleen een trekkracht",
        ],
        antwoord=0,
        uitleg="Je verdraait de handdoek om zijn as, en verdraaien is torsie. Het lijkt misschien op samendrukken omdat er water uit komt, maar samendrukken is druk, en dat doe je hier niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke situaties gaat het vooral om een trekkracht? (meerdere antwoorden mogelijk)",
        opties=[
            "Een sleepkabel tussen een auto en een wagen met pech",
            "De ketting van een schommel waarop iemand zit",
            "De poten van een stoel waarop iemand zit",
            "Een sleutel die je in het slot omdraait",
            "Een duikplank met iemand op het uiteinde",
        ],
        antwoord=[0, 1],
        uitleg="De sleepkabel en de schommelketting worden uit elkaar getrokken: trekkracht. De stoelpoten worden samengedrukt (druk), de sleutel wordt verdraaid (torsie) en de duikplank buigt door (buiging).",
    ),
    dict(
        type="meerkeuze",
        vraag="Een hoge, smalle kast kiept makkelijk om. Wat maakt haar stabieler? (meerdere antwoorden mogelijk)",
        opties=[
            "De voet van de kast breder maken",
            "De zwaarste spullen onderaan zetten",
            "Een schuine lat achteraan tussen twee hoeken zetten",
            "De zwaarste dozen op de bovenste plank zetten",
            "Er bovenop nog een extra plank met spullen bijzetten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een brede voet, een laag zwaartepunt en schuine balken tussen de hoeken maken een constructie stabieler. Zware spullen of een extra plank bovenaan brengen het zwaartepunt omhoog, en dat maakt ze juist minder stabiel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over gewapend beton kloppen? (meerdere antwoorden mogelijk)",
        opties=[
            "Het staal erin vangt de trekkracht op",
            "Het beton zelf kan veel drukkracht verdragen",
            "Het verdraagt meer trekkracht dan gewoon beton",
            "Het is beton met staven staal erin",
            "Het staal zit erin om het beton lichter te maken",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Beton kan veel druk aan maar weinig trek. Daarom steekt er staal in, dat de trekkracht opvangt; zo verdraagt gewapend beton meer trek dan gewoon beton. Lichter wordt het er niet van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet met één blad papier een brug maken tussen twee boeken, en die brug moet een potlood dragen. Wat doe je het best met het blad?",
        opties=[
            "Het tot een harmonica plooien",
            "Het zo plat en strak mogelijk leggen",
            "Het eerst nat maken zodat het zwaarder wordt",
            "Het in vier stukken scheuren en die op elkaar leggen",
        ],
        antwoord=0,
        uitleg="Plooien maken een plaat stijver, net zoals bij een golfplaat. Een vlak blad buigt meteen door, maar een geplooid blad van hetzelfde papier draagt ineens wel iets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een oude brug van steen overspant met een boog een brede rivier. Waarom lukt dat?",
        opties=[
            "De boog leidt het gewicht naar de zijkanten weg",
            "Steen kan heel veel trekkracht verdragen",
            "De boog brengt het zwaartepunt van de brug hoger",
            "In een boog werkt er helemaal geen enkele kracht",
        ],
        antwoord=0,
        uitleg="Een boog leidt het gewicht naar de zijkanten weg en kan zo een grote opening overspannen. Dat steen goed is in trek, is een misvatting: net als beton is steen vooral goed in druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="De arm van een bouwkraan tilt een last op. Welke kracht werkt er vooral op die arm, en uit welke vorm is hij meestal opgebouwd?",
        opties=[
            "Buigkracht, en hij is opgebouwd uit driehoeken",
            "Torsiekracht, en hij is opgebouwd uit rechthoeken",
            "Drukkracht, en hij is opgebouwd uit grote bogen",
            "Buigkracht, en hij is opgebouwd uit losse rechthoeken",
        ],
        antwoord=0,
        uitleg="Een kraanarm met een last eraan buigt door: buigkracht. Om niet te vervormen is hij opgebouwd uit driehoeken. Losse rechthoeken zouden juist scheeftrekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je draait de dop van een fles los. Welke kracht oefen je vooral uit op die dop?",
        opties=[
            "Een torsiekracht",
            "Een trekkracht",
            "Een buigkracht",
            "Een drukkracht",
        ],
        antwoord=0,
        uitleg="Je draait de dop rond om zijn as, net zoals een schroef met een schroevendraaier. Verdraaien is torsie. Je trekt de dop er niet af en je drukt hem niet samen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een boekenrek dat bijna niet doorbuigt, kan ook niet omvallen.",
        antwoord=False,
        uitleg="Bijna niet doorbuigen is stijfheid, niet omvallen is stabiliteit. Dat zijn twee verschillende dingen: een stijf maar hoog en smal rek kan nog altijd omkiepen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plank die je over een beekje legt en waarop je in het midden gaat staan, krijgt een buigkracht te verwerken.",
        antwoord=True,
        uitleg="Dat is dezelfde situatie als een plank op twee steunen met iets zwaars in het midden. De plank buigt door, dus werkt er een buigkracht.",
    ),
    dict(
        type="waarofniet",
        vraag="Een staaf van glas is een goede keuze om een zware lamp aan het plafond op te hangen.",
        antwoord=False,
        uitleg="Een lamp die aan iets hangt, trekt eraan: trekkracht. Glas is broos en dus een slechte keuze voor trek. Staal past daar veel beter.",
    ),
    dict(
        type="waarofniet",
        vraag="Zet je in een rechthoekig frame één schuine balk van de ene hoek naar de overstaande hoek, dan bestaat het frame uit twee driehoeken.",
        antwoord=True,
        uitleg="De schuine balk deelt de rechthoek in twee driehoeken. Daarom trekt het frame daarna niet meer scheef: een driehoek houdt zijn vorm.",
    ),
    dict(
        type="invultekst",
        vraag="Je draait met een sleutel een slot open. De kracht op de sleutel is een ___kracht. Antwoord met één woord.",
        antwoord="torsie",
        uitleg="De sleutel wordt om zijn as verdraaid, en verdraaien heet torsie. Het is dus een torsiekracht, net zoals bij een schroevendraaier.",
    ),
    dict(
        type="invultekst",
        vraag="Een tent scheurt bij storm nergens en buigt nauwelijks door, maar waait toch helemaal om. Welke eigenschap schiet tekort? Antwoord met één woord.",
        antwoord="stabiliteit",
        uitleg="Niets scheurt, dus de sterkte is in orde. Ze buigt nauwelijks, dus de stijfheid ook. Omvallen gaat over stabiliteit.",
    ),
    dict(
        type="invultekst",
        vraag="Een balk van gewoon beton scheurt als er een grote trekkracht op komt. Welk materiaal stop je erin om dat op te vangen? Antwoord met één woord.",
        antwoord="staal",
        uitleg="Beton kan veel druk aan maar weinig trek. Met staven staal erin wordt het gewapend beton: het staal vangt de trekkracht op.",
    ),
]
