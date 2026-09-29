# -*- coding: utf-8 -*-
"""De vragen voor "Word, Excel, PowerPoint en veilig online" (✨ Spark,
samenleving en economie).

Uit de vakfiche 1ste graad A-stroom, onderdeel "ik ben digitaal vaardig"
(22,5 % van het examen), tweede helft. Digitaal communiceren en het beheren van
mappen en bestanden staat in [[se_digitaal]].

Deel 1 gaat over de drie kantoorprogramma's: de structuur en de opmaak in Word,
het rekenblad Excel met zijn celadressen, getalnotaties en formules, en
PowerPoint met het KISS-principe. Deel 2 gaat over de regels in de digitale
wereld: de acht vormen van ongepast gedrag, de vier vormen van internetfraude,
en hoe je je persoonlijke gegevens beschermt.

LET OP BIJ HET AANVULLEN. Twee zaken hier zijn gevoelig.

Ten eerste sexting en grooming. Die staan in de fiche en ze horen er dus bij,
maar de vragen blijven zakelijk: wat het is, waarom het gevaarlijk is, en wat je
doet. Geen enkel detail meer dan dat, en het antwoord wijst altijd naar een
vertrouwenspersoon en naar melden, nooit naar zelf oplossen.

Ten tweede de regels van een sterk wachtwoord. Die komen woordelijk uit de fiche
(minstens 8 en maximaal 24 karakters, een hoofdletter, een kleine letter, een
cijfer en een teken). Elders gelden soms andere regels; op dit examen gelden
deze. Wie hier iets bijschrijft, kijkt dat na in de fiche zelf.

Op het examen krijg je bij het Office-deel schermafdrukken uit Windows 10 en
Office 365. Wij kunnen die niet meegeven, dus zijn de vragen zo geschreven dat
ze zonder schermafdruk blijven kloppen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn structuurelementen van een tekst in Word?",
        opties=[
            "Een woord",
            "Een zin",
            "Een alinea",
            "Een cel",
        ],
        antwoord=[0, 1, 2],
        uitleg="De structuurelementen van een tekst zijn het teken, het woord, de regel, de zin, de alinea en de pagina. Een cel hoort bij Excel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een alinea?",
        opties=[
            "Een stuk tekst dat eindigt waar je op Enter duwt",
            "Een stuk tekst dat precies één regel lang is",
            "Een stuk tekst dat op één pagina moet passen",
            "Een stuk tekst dat vetgedrukt begint en eindigt",
        ],
        antwoord=0,
        uitleg="Een nieuwe alinea begint na een Enter. Alles wat Word als één alinea ziet, krijgt ook dezelfde alineaopmaak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij de tekenopmaak?",
        opties=[
            "Vet en cursief",
            "Het lettertype en de tekengrootte",
            "De tekstkleur en markeren",
            "De regelafstand van je tekst",
        ],
        antwoord=[0, 1, 2],
        uitleg="Tekenopmaak werkt op letters: lettertype, grootte, vet, cursief, onderstrepen, kleur, markeren, super- en subscript, en doorhalen. Regelafstand is alineaopmaak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil in een formule H2O het cijfer 2 kleiner en lager zetten. Welke tekenopmaak gebruik je?",
        opties=[
            "Subscript",
            "Superscript",
            "Doorhalen",
            "Markeren",
        ],
        antwoord=0,
        uitleg="Subscript zet het teken lager, superscript hoger. Denk aan H2O met subscript en aan m2 met superscript.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij de alineaopmaak?",
        opties=[
            "De regelafstand",
            "De uitlijning",
            "Het inspringen",
            "De tekengrootte",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alineaopmaak werkt op een hele alinea: regelafstand, uitlijning en inspringen. De tekengrootte hoort bij de tekenopmaak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het als een alinea uitgevuld is?",
        opties=[
            "De tekst sluit links en rechts recht aan op de marge",
            "De tekst staat mooi in het midden van de pagina",
            "De tekst schuift met de eerste regel wat naar binnen",
            "De tekst heeft meer ruimte tussen de regels gekregen",
        ],
        antwoord=0,
        uitleg="Bij uitvullen zijn beide kanten recht. Bij links uitlijnen blijft de rechterkant rafelig.",
    ),
    dict(
        type="waarofniet",
        vraag="De marges en de afdrukstand van een document horen bij de alineaopmaak.",
        antwoord=False,
        uitleg="Ze horen bij de paginaopmaak, want ze gelden voor de hele pagina. De afdrukstand is staand of liggend, en de marges zijn de witte randen rond je tekst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat komt er in een voettekst?",
        opties=[
            "Tekst die onderaan elke pagina herhaald wordt",
            "Tekst die alleen op de laatste pagina staat",
            "Tekst die je met een opsomming laat beginnen",
            "Tekst die je bovenaan elke pagina zet",
        ],
        antwoord=0,
        uitleg="Een voettekst staat onderaan op elke pagina, bijvoorbeeld het paginanummer. Bovenaan heet dat een koptekst.",
    ),
    dict(
        type="waarofniet",
        vraag="Een document opslaan als pdf zorgt ervoor dat de opmaak bij iedereen hetzelfde blijft.",
        antwoord=True,
        uitleg="Klopt. Een pdf ziet er op elk toestel hetzelfde uit en is niet zomaar aan te passen. Daarom stuur je een pdf als iets af is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een celadres in Excel?",
        opties=[
            "De kolomletter met het rijnummer, zoals B4",
            "De naam die je zelf aan een werkblad geeft",
            "Het aantal cellen dat je geselecteerd hebt",
            "Het bestand waarin je rekenblad bewaard wordt",
        ],
        antwoord=0,
        uitleg="Een celadres is de kolomletter plus het rijnummer. B4 is de cel in kolom B en rij 4.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn structuurelementen van een rekenblad?",
        opties=[
            "De cel en het celadres",
            "De rij en de kolom",
            "Het werkblad en de werkmap",
            "De alinea en de pagina",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een rekenblad bestaat uit cellen, celadressen, bereiken, rijen, kolommen, werkbladen en een werkmap. Alinea's horen bij Word.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een werkblad en een werkmap?",
        opties=[
            "Een werkmap is het bestand, een werkblad is één tabblad erin",
            "Een werkblad is het bestand, een werkmap is één tabblad erin",
            "Een werkmap is een map op je computer met rekenbladen in",
            "Een werkblad is een afdruk van een werkmap op papier",
        ],
        antwoord=0,
        uitleg="Eén Excel-bestand is een werkmap. Onderaan zie je de tabbladen: dat zijn de werkbladen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een bereik in Excel?",
        opties=[
            "Een groep cellen die bij elkaar horen, zoals A1 tot A10",
            "Het hoogste getal dat in een kolom voorkomt",
            "Het verschil tussen het grootste en het kleinste getal",
            "De breedte die een kolom maximaal kan hebben",
        ],
        antwoord=0,
        uitleg="Een bereik schrijf je met een dubbele punt: A1:A10. Zo kan je in één keer met alle cellen ertussen rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke getalnotaties kan je in Excel aan een cel geven?",
        opties=[
            "Valuta",
            "Percentage",
            "Datum en tijd",
            "Alineaopmaak",
        ],
        antwoord=[0, 1, 2],
        uitleg="Valuta, percentage, een aantal decimalen, en datum en tijd zijn getalnotaties. Alineaopmaak bestaat alleen in een tekstverwerker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke formule tel je de getallen in de cellen A1 tot A10 op?",
        opties=[
            "=SOM(A1:A10)",
            "=SOM(A1+A10)",
            "=A1:A10",
            "=TOTAAL(A1;A10)",
        ],
        antwoord=0,
        uitleg="SOM telt een heel bereik op. Elke formule in Excel begint met een gelijkheidsteken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk teken gebruikt Excel om te vermenigvuldigen?",
        opties=[
            "Het sterretje",
            "Het schuine streepje",
            "Het koppelteken",
            "De dubbele punt",
        ],
        antwoord=0,
        uitleg="Het sterretje vermenigvuldigt en het schuine streepje deelt. Met haakjes bepaal je wat eerst gerekend wordt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een formule in Excel begint altijd met een gelijkheidsteken.",
        antwoord=True,
        uitleg="Klopt. Zonder dat teken ziet Excel je formule als gewone tekst en rekent hij niets uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar houdt het KISS-principe van een presentatie rekening mee?",
        opties=[
            "Maximaal zeven regels per dia en zeven woorden per regel",
            "Maximaal zeven dia's in een hele presentatie",
            "Maximaal zeven kleuren op elke dia die je zelf maakt",
            "Maximaal zeven minuten spreken per presentatie",
        ],
        antwoord=0,
        uitleg="KISS staat voor keep it short and simple: zeven regels per dia, zeven woorden per regel, en een leesbaar lettertype van meestal 14 punt.",
    ),
    dict(
        type="waarofniet",
        vraag="Je zet in PowerPoint beter je volledige tekst op de dia, zodat je niets vergeet.",
        antwoord=False,
        uitleg="Dan leest het publiek in plaats van te luisteren. Op de dia staan steekwoorden, de uitleg komt van jou.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we in Excel de kolomletter met het rijnummer erbij, zoals B4?",
        antwoord=["het celadres", "celadres"],
        uitleg="Het celadres wijst één cel aan. Twee celadressen met een dubbele punt ertussen vormen een bereik.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zijn haatberichten?",
        opties=[
            "Berichten die aanzetten tot haat tegen een persoon of een groep",
            "Berichten die je per ongeluk naar de verkeerde persoon stuurt",
            "Berichten die je met opzet in hoofdletters typt",
            "Berichten die een bedrijf ongevraagd naar je stuurt",
        ],
        antwoord=0,
        uitleg="Haatberichten vallen iemand aan om wie hij is. Ze zijn strafbaar, ook als ze online staan en ook als ze als grap bedoeld waren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is doxing?",
        opties=[
            "Iemands privégegevens online zetten zonder toestemming",
            "Iemand volledig uitsluiten uit een groep of gesprek",
            "Iemand publiek belachelijk maken met een foto",
            "Iemand vals nieuws doorsturen over een gebeurtenis",
        ],
        antwoord=0,
        uitleg="Bij doxing wordt bijvoorbeeld iemands adres, telefoonnummer of school online gegooid. Daarmee wordt iemand kwetsbaar gemaakt in het echte leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is shaming?",
        opties=[
            "Iemand publiek vernederen of belachelijk maken",
            "Iemands adres en telefoonnummer online zetten",
            "Een vals bericht sturen om codes te bemachtigen",
            "Een volwassene die online het vertrouwen van een kind zoekt",
        ],
        antwoord=0,
        uitleg="Shaming maakt iemand te schande voor een publiek. Wat één iemand plaatst, wordt door tientallen anderen verder gedeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is exposing?",
        opties=[
            "Iets privé van iemand openbaar maken om die persoon te schaden",
            "Iets van jezelf online zetten om meer volgers te krijgen",
            "Iemand collectief uitsluiten na een uitspraak of een daad",
            "Iemand een bericht sturen dat aanzet tot haat",
        ],
        antwoord=0,
        uitleg="Bij exposing worden privéberichten of foto's rondgestuurd. Dat het echt gebeurd is, maakt het niet minder ernstig.",
    ),
    dict(
        type="waarofniet",
        vraag="Fake news is nieuws dat vals is maar als echt verspreid wordt.",
        antwoord=True,
        uitleg="Klopt. Kijk altijd wie het schrijft en of een tweede, betrouwbare bron het ook meldt voor je iets doorstuurt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is canceling?",
        opties=[
            "Iemand collectief uitsluiten of boycotten na een uitspraak of daad",
            "Iemands persoonlijke gegevens zoals zijn adres op het internet zetten",
            "Iemand een vals bericht sturen om zijn codes te bemachtigen",
            "Iemand blokkeren zodat hij je berichten niet meer kan zien",
        ],
        antwoord=0,
        uitleg="Bij canceling keert een grote groep zich tegen iemand en sluit die persoon buiten. Iemand blokkeren voor je eigen rust is iets anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is grooming?",
        opties=[
            "Een volwassene die online het vertrouwen van een kind zoekt om misbruik te maken",
            "Een volwassene die online een valse naam gebruikt om anoniem te kunnen blijven",
            "Een onbekende die je een bericht stuurt met een verdachte link erin",
            "Een bedrijf dat jouw gegevens verzamelt zonder het te melden",
        ],
        antwoord=0,
        uitleg="Bij grooming bouwt iemand eerst geduldig vertrouwen op. Voel je dat een gesprek die kant op gaat: stop het, blokkeer, en vertel het aan iemand die je vertrouwt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand die je online leerde kennen vraagt je om een intieme foto en zegt dat het tussen jullie blijft. Wat doe je?",
        opties=[
            "Niet sturen, het gesprek stoppen en het aan een vertrouwenspersoon zeggen",
            "Sturen, maar je gezicht eruit laten zodat je zeker niet herkenbaar bent",
            "Eerst een foto van die persoon vragen zodat het gelijk staat",
            "Wachten tot je die persoon in het echte leven ontmoet hebt",
        ],
        antwoord=0,
        uitleg="Zo'n belofte kan niemand houden: een foto is doorgestuurd voor je het weet. Niet sturen, stoppen, en het zeggen aan iemand die je vertrouwt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een intieme foto van iemand anders doorsturen is strafbaar, ook als je die zelf gekregen hebt.",
        antwoord=True,
        uitleg="Klopt. Zo'n beeld verder verspreiden is een misdrijf. Verwijder het en vertel het aan een volwassene die je vertrouwt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn vormen van internetfraude?",
        opties=[
            "Smishing",
            "Quishing",
            "Vishing",
            "Shaming",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vier vormen van internetfraude zijn phishing, smishing, quishing en vishing. Shaming is ongepast gedrag, geen fraude.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee probeert een bedrieger je bij smishing te vangen?",
        opties=[
            "Met een sms",
            "Met een QR-code",
            "Met een telefoongesprek",
            "Met een bericht op een forum",
        ],
        antwoord=0,
        uitleg="Smishing gaat via sms. Quishing werkt met een QR-code en vishing met een telefoongesprek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee werkt quishing?",
        opties=[
            "Met een QR-code die naar een valse website leidt",
            "Met een sms die naar een valse website leidt",
            "Met een telefoongesprek waarin naar je codes gevraagd wordt",
            "Met een mail waarin naar je codes gevraagd wordt",
        ],
        antwoord=0,
        uitleg="Bij quishing plakt iemand een valse QR-code, bijvoorbeeld over die van een parkeerautomaat. Je ziet niet waar een QR-code je brengt tot je er al bent.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij vishing krijg je een valse QR-code voorgeschoteld.",
        antwoord=False,
        uitleg="Dat is quishing. Vishing komt van voice: iemand belt je op en doet zich voor als je bank of de politie. Leg op en bel zelf terug naar een nummer dat je al kende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een mail met een link en de melding dat je pakje vastzit tot je een klein bedrag betaalt. Wat doe je?",
        opties=[
            "De mail negeren en zelf je zending nakijken bij de vervoerder",
            "Het bedrag betalen, want het is maar een paar euro",
            "Op de link klikken om te zien waar hij precies naartoe gaat",
            "Antwoorden met de vraag om welk pakje het gaat",
        ],
        antwoord=0,
        uitleg="Dit is een klassieke phishingmail. Ga altijd zelf naar de app of de site die je al kende, en klik nooit op de link in zo'n bericht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee bescherm je je persoonlijke gegevens?",
        opties=[
            "Met een sterk wachtwoord",
            "Met authenticatie of verificatie",
            "Met tweestapsverificatie",
            "Met hetzelfde wachtwoord op elke site",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een sterk wachtwoord, verificatie en tweestapsverificatie beschermen je. Eén wachtwoord voor alles doet net het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is tweestapsverificatie?",
        opties=[
            "Naast je wachtwoord geef je nog een tweede bewijs, zoals een code",
            "Je typt je wachtwoord twee keer in om typfouten te vermijden",
            "Je hebt twee verschillende wachtwoorden voor dezelfde site",
            "Je verandert je wachtwoord elke twee maanden opnieuw",
        ],
        antwoord=0,
        uitleg="Zelfs wie je wachtwoord kent, geraakt er dan niet in zonder je gsm. Daarom is het de beste bescherming die je kan aanzetten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke regels gelden voor een sterk wachtwoord?",
        opties=[
            "Minstens 8 en maximaal 24 karakters lang",
            "Minstens één hoofdletter en één kleine letter",
            "Minstens één cijfer en één teken",
            "Je voornaam en je geboortejaar erin",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche vraagt 8 tot 24 karakters, met een hoofdletter, een kleine letter, een cijfer en een teken. Je naam of je geboortejaar is net wat een bedrieger eerst probeert.",
    ),
    dict(
        type="waarofniet",
        vraag="Het wachtwoord wachtwoord123 is sterk genoeg volgens die regels.",
        antwoord=False,
        uitleg="Er zit geen hoofdletter en geen teken in, en het is een van de meest gebruikte wachtwoorden ter wereld. Dat maakt het meteen te raden.",
    ),
    dict(
        type="waarofniet",
        vraag="Als iemand je online lastigvalt, is een schermafdruk maken en het melden een goede reactie.",
        antwoord=True,
        uitleg="Klopt. Een schermafdruk is je bewijs, ook als het bericht later verdwijnt. Meld het daarna bij het platform en vertel het aan een volwassene die je vertrouwt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we het online zetten van iemands privégegevens zonder zijn toestemming?",
        antwoord=["doxing", "doxen"],
        uitleg="Bij doxing worden gegevens zoals een adres of een telefoonnummer publiek gemaakt, waardoor iemand ook buiten het internet gevaar loopt.",
    ),
]
