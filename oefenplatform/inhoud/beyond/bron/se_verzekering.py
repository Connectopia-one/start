# -*- coding: utf-8 -*-
"""Verzekeringen, een schadegeval en de polis.

Het blok "ik ben verzekerd" weegt 7,5 procent en krijgt bij ons één thema.

Het leerdoel zet twee woorden naast elkaar die in het dagelijks taalgebruik
door elkaar lopen: verantwoordelijkheid en aansprakelijkheid. Verantwoordelijk
is wie het gedaan heeft. Juridisch aansprakelijk is wie er volgens de wet
voor moet opdraaien, en dat hoeft niet dezelfde te zijn: voor de schade van
een jong kind zijn de ouders aansprakelijk.

Op het examen krijg je de beschrijving van een schadegeval en haal je er de
informatie uit voor een schadeaangifte. Die velden staan in de fiche:
    de datum en het uur, de aard van de schade, de getuige, de
    verantwoordelijke, de juridisch aansprakelijke, de begunstigde

De vijf verzekeringen van de fiche:
    de autoverzekering, de verzekering bromfiets, de brandverzekering, de
    familiale verzekering, de rechtsbijstandsverzekering

En de onderdelen van een polis:
    de verzekeringsnemer, de verzekeraar, de verzekerde, de schadevergoeding,
    de franchise, de premie, het verzekerd risico

Let op het verschil tussen verzekeringsnemer en verzekerde: de nemer sluit het
contract en betaalt, de verzekerde is wie gedekt is. Vaak dezelfde persoon,
maar lang niet altijd.

Deel 1 is de verzekeringen en het schadegeval.
Deel 2 is de polis en haar onderdelen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom sluit je een verzekering af?",
        opties=[
            "om een schade te kunnen dragen die je zelf niet zou kunnen betalen",
            "om nooit meer schade te veroorzaken",
            "omdat de wet dat voor alles verplicht",
            "om een vergoeding te krijgen bij elk klein ongemak",
        ],
        antwoord=0,
        uitleg="Je betaalt een kleine premie om een groot risico niet alleen te moeten dragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen verantwoordelijk en juridisch aansprakelijk?",
        opties=[
            "verantwoordelijk is wie het deed, aansprakelijk wie er volgens de wet voor opdraait",
            "aansprakelijk is wie het deed, verantwoordelijk wie betaalt",
            "het zijn twee woorden voor hetzelfde",
            "aansprakelijk geldt enkel voor bedrijven",
        ],
        antwoord=0,
        uitleg="Bij een jong kind is het kind verantwoordelijk en zijn de ouders aansprakelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kind van zes trapt een bal door het raam van de buren. Wie is juridisch aansprakelijk?",
        opties=[
            "de ouders van het kind",
            "het kind zelf",
            "de buren",
            "niemand",
        ],
        antwoord=0,
        uitleg="Het kind is verantwoordelijk voor wat het deed, de ouders zijn aansprakelijk voor de schade.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verzekering dekt die bal door het raam van de buren?",
        opties=[
            "de familiale verzekering",
            "de brandverzekering",
            "de autoverzekering",
            "de rechtsbijstandsverzekering",
        ],
        antwoord=0,
        uitleg="De familiale dekt de schade die jij of je gezin aan iemand anders toebrengt in het dagelijks leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je woning loopt waterschade op door een brand bij de buren. Welke verzekering komt eerst in beeld?",
        opties=[
            "de brandverzekering",
            "de familiale verzekering",
            "de autoverzekering",
            "de verzekering bromfiets",
        ],
        antwoord=0,
        uitleg="De brandverzekering dekt schade aan de woning, en meer dan brand alleen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je rijdt met de auto tegen een paaltje. Welke verzekering is hier aan de orde?",
        opties=[
            "de autoverzekering",
            "de familiale verzekering",
            "de brandverzekering",
            "de rechtsbijstandsverzekering",
        ],
        antwoord=0,
        uitleg="Schade met een motorvoertuig valt nooit onder de familiale verzekering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt een advocaat nodig in een geschil na een ongeval. Welke verzekering helpt?",
        opties=[
            "de rechtsbijstandsverzekering",
            "de familiale verzekering",
            "de brandverzekering",
            "de autoverzekering",
        ],
        antwoord=0,
        uitleg="Rechtsbijstand betaalt de kosten van een juridische procedure.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vijf verzekeringen noemt de fiche?",
        opties=[
            "auto, bromfiets, brand, familiale en rechtsbijstand",
            "auto, brand, hospitalisatie, reis en familiale",
            "familiale, schuld, brand, leven en auto",
            "auto, fiets, brand, diefstal en rechtsbijstand",
        ],
        antwoord=0,
        uitleg="Een hospitalisatie- of reisverzekering staat niet in dit rijtje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens horen volgens de fiche in een schadeaangifte?",
        opties=[
            "de datum en het uur, de aard van de schade en wie aansprakelijk is",
            "enkel het bedrag van de schade, zoals de hersteller het opgeeft",
            "enkel de naam van de verzekeraar en het nummer van je polis",
            "de premie en de franchise die in je polis afgesproken staan",
        ],
        antwoord=0,
        uitleg="De fiche noemt ook de getuige, de verantwoordelijke en de begunstigde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraagt een schadeaangifte naar een getuige?",
        opties=[
            "om achteraf te kunnen vaststellen wat er precies gebeurd is",
            "om de premie voor het volgende jaar te kunnen berekenen",
            "omdat de getuige een deel van de schade mee moet betalen",
            "om de franchise van de polis achteraf te kunnen bepalen",
        ],
        antwoord=0,
        uitleg="Bij onenigheid over wie wat deed, weegt een onafhankelijke getuige zwaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Verantwoordelijk en juridisch aansprakelijk betekenen hetzelfde.",
        antwoord=False,
        uitleg="Bij een kind is het kind verantwoordelijk en zijn de ouders aansprakelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="De familiale verzekering dekt de schade die je met je auto veroorzaakt.",
        antwoord=False,
        uitleg="Daarvoor is er de autoverzekering. De familiale dekt het dagelijks leven.",
    ),
    dict(
        type="waarofniet",
        vraag="De rechtsbijstandsverzekering betaalt de kosten van een juridische procedure.",
        antwoord=True,
        uitleg="Ze staat in het rijtje van vijf naast de auto-, bromfiets-, brand- en familiale verzekering.",
    ),
    dict(
        type="waarofniet",
        vraag="De datum en het uur van een schadegeval horen in de schadeaangifte.",
        antwoord=True,
        uitleg="Ze staan vooraan in het rijtje van de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens noemt de fiche voor een schadeaangifte?",
        opties=[
            "de getuige",
            "de juridisch aansprakelijke",
            "de begunstigde",
            "het rijksregisternummer van de buren",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een rijksregisternummer staat niet in het rijtje. De datum, het uur en de aard van de schade wel.",
    ),
    dict(
        type="invultekst",
        vraag="Welke verzekering dekt de schade die jij of je gezin aan iemand anders toebrengt in het dagelijks leven?",
        antwoord=["familiale", "de familiale", "familiale verzekering"],
        uitleg="Ze staat in het rijtje van vijf en wordt het vaakst verward met de brandverzekering.",
    ),
    dict(
        type="invultekst",
        vraag="Wie is er volgens de wet verplicht de schade te vergoeden? Vul aan: de juridisch ...",
        antwoord=["aansprakelijke", "aansprakelijk"],
        uitleg="Niet noodzakelijk dezelfde persoon als wie het veroorzaakte.",
    ),
    dict(
        type="invultekst",
        vraag="Welke verzekering betaalt de kosten van een advocaat en een procedure?",
        antwoord=["rechtsbijstand", "rechtsbijstandsverzekering", "de rechtsbijstandsverzekering"],
        uitleg="Ze staat als laatste in het rijtje van vijf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een jongere rijdt met zijn bromfiets tegen een geparkeerde auto. Welke verzekering is hier aan de orde?",
        opties=[
            "de verzekering bromfiets",
            "de familiale verzekering",
            "de brandverzekering",
            "de autoverzekering van de geparkeerde wagen",
        ],
        antwoord=0,
        uitleg="Een bromfiets is een motorvoertuig, dus de familiale verzekering komt er niet aan te pas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de aard van de schade in een schadeaangifte?",
        opties=[
            "wat er precies beschadigd is en hoe",
            "het bedrag dat je terugkrijgt",
            "de naam van de verzekeraar",
            "het moment waarop het gebeurde",
        ],
        antwoord=0,
        uitleg="De datum en het uur staan er apart naast in het rijtje.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een polis?",
        opties=[
            "het contract waarin je verzekering beschreven staat",
            "het bedrag dat je jaarlijks betaalt",
            "het deel van de schade dat je zelf draagt",
            "het formulier waarmee je schade aangeeft",
        ],
        antwoord=0,
        uitleg="In de polis vind je wie verzekerd is, waartegen, en voor hoeveel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie is de verzekeringsnemer?",
        opties=[
            "wie het contract afsluit en de premie betaalt",
            "wie door de verzekering gedekt is",
            "de maatschappij die uitbetaalt",
            "wie het geld bij schade ontvangt",
        ],
        antwoord=0,
        uitleg="Dikwijls dezelfde persoon als de verzekerde, maar niet altijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie is de verzekerde?",
        opties=[
            "de persoon die door de verzekering gedekt is",
            "de persoon die het contract ondertekende",
            "de maatschappij die het risico draagt",
            "de getuige van het schadegeval",
        ],
        antwoord=0,
        uitleg="Een ouder kan de nemer zijn terwijl het kind de verzekerde is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie is de verzekeraar?",
        opties=[
            "de maatschappij die het risico draagt en uitbetaalt",
            "de persoon die het contract afsluit",
            "de makelaar die het contract verkocht",
            "de persoon die de schade veroorzaakte",
        ],
        antwoord=0,
        uitleg="Zij int de premie en betaalt de schadevergoeding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de premie?",
        opties=[
            "wat je betaalt om verzekerd te zijn",
            "wat je ontvangt bij schade",
            "het deel van de schade dat je zelf draagt",
            "een korting voor wie geen schade had",
        ],
        antwoord=0,
        uitleg="De premie gaat van jou naar de verzekeraar, de schadevergoeding de andere kant op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de franchise?",
        opties=[
            "het deel van de schade dat je zelf draagt",
            "het maximum dat de verzekeraar uitbetaalt",
            "het bedrag van je jaarlijkse premie",
            "de boete bij laattijdige aangifte",
        ],
        antwoord=0,
        uitleg="Bij 200 euro franchise en 800 euro schade krijg je 600 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt 1.500 euro schade en een franchise van 250 euro. Hoeveel betaalt de verzekeraar?",
        opties=["1.250 euro", "1.500 euro", "250 euro", "750 euro"],
        antwoord=0,
        uitleg="1.500 min 250 is 1.250 euro. De franchise draag je zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verzekerd risico?",
        opties=[
            "waartegen je precies verzekerd bent volgens de polis",
            "de kans dat je schade zal hebben",
            "het bedrag dat je zelf draagt",
            "het aantal jaren dat je verzekerd bent",
        ],
        antwoord=0,
        uitleg="Staat iets niet bij het verzekerd risico, dan is het niet gedekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie is de begunstigde?",
        opties=[
            "wie de uitbetaling ontvangt",
            "wie de premie betaalt",
            "wie het schadegeval veroorzaakte",
            "wie het contract ondertekende",
        ],
        antwoord=0,
        uitleg="De fiche noemt de begunstigde ook bij de gegevens van een schadeaangifte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bestaat een franchise?",
        opties=[
            "om kleine schades niet door de verzekering te laten lopen",
            "om de verzekeraar meer te laten verdienen aan grote schades",
            "om de premie te verhogen",
            "om de verzekerde te straffen",
        ],
        antwoord=0,
        uitleg="Daardoor blijft de premie lager voor iedereen.",
    ),
    dict(
        type="waarofniet",
        vraag="De premie is het bedrag dat je bij schade ontvangt.",
        antwoord=False,
        uitleg="De premie betaal je. Wat je ontvangt, is de schadevergoeding.",
    ),
    dict(
        type="waarofniet",
        vraag="De verzekeringsnemer en de verzekerde kunnen twee verschillende personen zijn.",
        antwoord=True,
        uitleg="Een ouder kan het contract nemen voor een kind.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hogere franchise gaat meestal samen met een lagere premie.",
        antwoord=True,
        uitleg="Je draagt meer zelf, dus de verzekeraar loopt minder risico.",
    ),
    dict(
        type="waarofniet",
        vraag="Wat niet in het verzekerd risico staat, wordt toch uitbetaald als het ernstig genoeg is.",
        antwoord=False,
        uitleg="Enkel wat in de polis als verzekerd risico staat, is gedekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderdelen van een polis noemt de fiche?",
        opties=[
            "de verzekeringsnemer",
            "de franchise",
            "het verzekerd risico",
            "de getuige",
        ],
        antwoord=[0, 1, 2],
        uitleg="De getuige hoort bij de schadeaangifte, niet bij de polis. De verzekeraar, de verzekerde, de schadevergoeding en de premie staan er wel in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt er voor de franchise?",
        opties=[
            "je draagt dat deel van de schade zelf",
            "ze staat in de polis",
            "een hogere franchise drukt meestal de premie",
            "ze wordt bovenop de schadevergoeding uitbetaald",
        ],
        antwoord=[0, 1, 2],
        uitleg="Ze wordt net van de schadevergoeding afgetrokken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het deel van de schade dat je zelf moet dragen?",
        antwoord=["franchise", "de franchise"],
        uitleg="Ze staat in je polis en drukt de premie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het bedrag dat je betaalt om verzekerd te zijn?",
        antwoord=["premie", "de premie"],
        uitleg="De premie betaal je, de schadevergoeding ontvang je.",
    ),
    dict(
        type="invultekst",
        vraag="Je hebt 900 euro schade en een franchise van 150 euro. Hoeveel krijg je uitbetaald? Antwoord met een getal.",
        antwoord=["750"],
        uitleg="900 min 150 is 750 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een moeder sluit een familiale verzekering af waarin ook haar dochter gedekt is. Wie is wie?",
        opties=[
            "de moeder is verzekeringsnemer, de dochter is verzekerde",
            "de dochter is verzekeringsnemer, de moeder is verzekerde",
            "beiden zijn verzekeraar",
            "beiden zijn begunstigde",
        ],
        antwoord=0,
        uitleg="De nemer sluit af en betaalt, de verzekerde is wie gedekt is.",
    ),
]
