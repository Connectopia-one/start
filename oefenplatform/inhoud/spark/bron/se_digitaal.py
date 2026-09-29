# -*- coding: utf-8 -*-
"""De vragen voor "Digitaal communiceren en bestanden beheren" (✨ Spark,
samenleving en economie).

Uit de vakfiche 1ste graad A-stroom, onderdeel "ik ben digitaal vaardig"
(22,5 % van het examen, het zwaarste onderdeel), eerste helft. De
kantoorprogramma's en de regels in de digitale wereld staan in [[se_office]].

Deel 1 gaat over de zes vormen van digitaal communiceren, over de onderdelen van
een e-mail, en over hoe je netjes en respectvol digitaal communiceert. Deel 2
gaat over mappen en bestanden: de Verkenner met haar vensters, een logische
mappenstructuur, een passende bestandsnaam, en uploaden, downloaden en een
back-up.

Op het examen krijg je hier schermafdrukken uit Windows 10 en Office 365 bij. Wij
kunnen die niet meegeven, dus zijn de vragen zo geschreven dat ze zonder
schermafdruk blijven kloppen. Wie hier iets bijschrijft, houdt dat vol.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn vormen van digitaal communiceren?",
        opties=[
            "E-mail",
            "Een online meeting",
            "Een forum",
            "Een brief met de post",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt zes vormen: e-mail, sociale media, fora, blogwebsites, een online meeting en chatten. Een papieren brief is niet digitaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een forum?",
        opties=[
            "Een plek online waar mensen per onderwerp vragen en antwoorden posten",
            "Een plek online waar één persoon zijn eigen stukken publiceert voor lezers",
            "Een gesprek met beeld en geluid tussen meerdere mensen",
            "Een programma waarmee je korte berichtjes stuurt",
        ],
        antwoord=0,
        uitleg="Op een forum staan de gesprekken per onderwerp bij elkaar, zodat anderen het antwoord later nog kunnen vinden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een blogwebsite?",
        opties=[
            "Een site waarop iemand regelmatig eigen stukken publiceert",
            "Een site waarop je per onderwerp vragen kan stellen aan anderen",
            "Een site waarop je met beeld en geluid kan vergaderen",
            "Een site waarop je bestanden in de cloud bewaart",
        ],
        antwoord=0,
        uitleg="Op een blog schrijft de auteur en lezen de anderen, met eventueel een reactie eronder. Op een forum zijn alle deelnemers gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Chatten gebeurt meestal met korte berichten en verwacht een snel antwoord.",
        antwoord=True,
        uitleg="Klopt. Chatten is vluchtig en snel. Een e-mail is uitgebreider en mag wat langer op een antwoord wachten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer kies je beter voor een e-mail dan voor een chatbericht?",
        opties=[
            "Als je iets formeel wil vragen en het moet worden bijgehouden",
            "Als je heel snel een kort antwoord op één vraag nodig hebt",
            "Als je met meerdere mensen tegelijk wil praten en zien",
            "Als je gewoon iets grappigs wil doorsturen naar een vriend",
        ],
        antwoord=0,
        uitleg="Een e-mail blijft staan, kan bijlagen meenemen en is geschikt voor iets officieel. Chatten is voor het snelle en het losse.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn onderdelen van een e-mail?",
        opties=[
            "De onderwerpregel",
            "De aanhef",
            "De slotgroet en de ondertekening",
            "Het paginanummer",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt: aan, CC, BCC, de onderwerpregel, de aanhef, de inhoud, de slotgroet, de ondertekening en de bijlage. Een paginanummer hoort in een document.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zet je in de onderwerpregel van een e-mail?",
        opties=[
            "Kort waar de mail over gaat",
            "Je eigen naam en je klas",
            "De volledige inhoud van je bericht",
            "Het adres van wie de mail moet krijgen",
        ],
        antwoord=0,
        uitleg="Een goede onderwerpregel is kort en concreet, zodat de ontvanger meteen ziet waarover het gaat en de mail later terugvindt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen CC en BCC?",
        opties=[
            "Bij CC zien de ontvangers elkaars adres, bij BCC niet",
            "Bij CC komt de mail sneller aan dan bij BCC",
            "Bij CC mag je maar één adres invullen, bij BCC meerdere",
            "Bij CC kan je geen bijlage meesturen, bij BCC wel",
        ],
        antwoord=0,
        uitleg="CC zet iemand zichtbaar in kopie. BCC doet dat onzichtbaar. Stuur je naar een grote groep die elkaar niet kent, gebruik dan BCC.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je stuurt een mail naar twintig mensen die elkaar niet kennen. Welk veld gebruik je?",
        opties=[
            "BCC",
            "CC",
            "Aan",
            "De onderwerpregel",
        ],
        antwoord=0,
        uitleg="Met BCC blijven de adressen verborgen. Anders geef je twintig mailadressen aan twintig onbekenden door.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bijlage is een bestand dat je met je e-mail meestuurt.",
        antwoord=True,
        uitleg="Klopt. Vergeet ze niet effectief toe te voegen, en vermeld in je tekst dat je iets meestuurt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe begin je een e-mail aan iemand die je niet kent?",
        opties=[
            "Met een nette aanhef, zoals Geachte mevrouw",
            "Met de vraag zelf, zonder aanhef",
            "Met hey, want dat klinkt meteen vriendelijker",
            "Met je eigen naam bovenaan de mail",
        ],
        antwoord=0,
        uitleg="Bij iemand die je niet kent hoort een nette aanhef. Naar een vriend mag Hallo of Hey, maar niet naar een school of een bedrijf.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bericht volledig in hoofdletters typen wordt online als roepen gelezen.",
        antwoord=True,
        uitleg="Klopt. Hoofdletters komen hard aan. Gebruik ze alleen om één woord te benadrukken, nooit voor een hele boodschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat horen bij de regels van netjes digitaal communiceren?",
        opties=[
            "Je bericht nalezen voor je het verstuurt",
            "Niet reageren in het heetst van je kwaadheid",
            "Geen kwetsende taal of scheldwoorden gebruiken",
            "Zo veel mogelijk afkortingen gebruiken in elke mail",
        ],
        antwoord=[0, 1, 2],
        uitleg="Nalezen, afkoelen en respectvol blijven zijn de basisregels. Afkortingen mogen in een chat met vrienden, maar niet in een e-mail aan een school.",
    ),
    dict(
        type="waarofniet",
        vraag="In een videogesprek laat je je microfoon altijd aanstaan, ook als je niet spreekt.",
        antwoord=False,
        uitleg="Zet je micro uit als je niet spreekt, zo hoort niemand jouw achtergrondgeluid. Aanzetten doe je als je aan het woord bent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je voor een online meeting begint?",
        opties=[
            "Je camera en je microfoon testen",
            "Een rustige plek en een neutrale achtergrond kiezen",
            "Enkele minuten vroeger inloggen",
            "Je bericht in hoofdletters klaarzetten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Testen, een rustige plek en op tijd inloggen maken een online gesprek vlot. Hoofdletters horen er niet bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bericht in een groepschat blijft binnen die groep en kan niet verder.",
        antwoord=False,
        uitleg="Iedereen in de groep kan het doorsturen of er een schermafdruk van maken. Wat je online zet, verlaat je handen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je bent kwaad over een bericht van een klasgenoot. Wat is de beste reactie?",
        opties=[
            "Even wachten en er pas later kalm op antwoorden",
            "Meteen terugschrijven zodat hij het meteen weet",
            "Het bericht in de groep zetten zodat iedereen het ziet",
            "Hem uit elke groepschat verwijderen zonder uitleg",
        ],
        antwoord=0,
        uitleg="Een bericht dat uit kwaadheid vertrekt, blijft staan. Wachten kost je niets en spaart je vaak veel.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag een foto van een klasgenoot online zetten zonder het te vragen.",
        antwoord=False,
        uitleg="Je hebt toestemming nodig voor een foto waarop iemand herkenbaar staat. Dat is niet alleen hoffelijk, het is ook de wet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee sluit je een nette e-mail af?",
        opties=[
            "Met een slotgroet en je naam eronder",
            "Met de onderwerpregel nog eens herhaald",
            "Met het mailadres van de ontvanger",
            "Met alleen een emoji als afsluiter",
        ],
        antwoord=0,
        uitleg="Een slotgroet zoals Met vriendelijke groeten, en daaronder je ondertekening met je naam. Zo weet de ontvanger zeker van wie de mail komt.",
    ),
    dict(
        type="invultekst",
        vraag="Welk veld van een e-mail gebruik je zodat de ontvangers elkaars adres niet zien, met drie letters?",
        antwoord=["bcc", "de bcc"],
        uitleg="BCC staat voor blind carbon copy. De adressen in dat veld blijven verborgen voor de andere ontvangers.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de Verkenner?",
        opties=[
            "Het programma waarmee je mappen en bestanden bekijkt en beheert",
            "Het programma waarmee je op het internet surft",
            "Het programma waarmee je een tekst typt, opmaakt en afdrukt",
            "De plek waarin verwijderde bestanden terechtkomen",
        ],
        antwoord=0,
        uitleg="In de Verkenner zie je je schijven, mappen en bestanden. Daar maak je ze, verplaats je ze en verwijder je ze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er in het navigatievenster van de Verkenner?",
        opties=[
            "De boomstructuur van je schijven en mappen",
            "De grootte en de datum van het gekozen bestand",
            "De naam die je aan een nieuwe map wil geven",
            "De lijst met programma's die openstaan",
        ],
        antwoord=0,
        uitleg="Het navigatievenster staat aan de linkerkant en toont waar je je bevindt in de mappenstructuur. Zo spring je snel van map naar map.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat toont het detailvenster?",
        opties=[
            "Extra informatie over het bestand dat je geselecteerd hebt",
            "De volledige boomstructuur van al je schijven en mappen",
            "De inhoud van elke map op je computer tegelijk",
            "De knoppen waarmee je een bestand kan afdrukken",
        ],
        antwoord=0,
        uitleg="Het detailvenster geeft onder meer het type, de grootte en de datum van het geselecteerde bestand. Zo zie je in één oogopslag waarmee je bezig bent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een bestand?",
        opties=[
            "Een verzameling gegevens met een naam en een extensie",
            "Een plaats waarin je andere gegevens kan bewaren",
            "Een programma dat je op je computer installeert",
            "Een kopie die je bewaart voor als er iets misgaat",
        ],
        antwoord=0,
        uitleg="Een bestand is één geheel met een naam, zoals verslag.docx. Een map is de plek waarin bestanden zitten.",
    ),
    dict(
        type="waarofniet",
        vraag="De extensie van een bestand zegt met welk soort bestand je te maken hebt.",
        antwoord=True,
        uitleg="Klopt. Aan .docx zie je een Word-document, aan .xlsx een Excel-rekenblad, aan .pdf een pdf en aan .jpg een foto.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een bestand kopiëren en een bestand verplaatsen?",
        opties=[
            "Bij kopiëren blijft het origineel staan, bij verplaatsen niet",
            "Bij kopiëren verdwijnt het origineel, bij verplaatsen blijft het",
            "Bij kopiëren verandert de naam, bij verplaatsen de extensie",
            "Bij kopiëren gaat het naar de prullenbak, bij verplaatsen niet",
        ],
        antwoord=0,
        uitleg="Kopiëren maakt een tweede exemplaar. Verplaatsen zet het ene exemplaar ergens anders neer.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bestand dat je verwijdert, is meteen voorgoed weg.",
        antwoord=False,
        uitleg="Het gaat eerst naar de prullenbak en kan daar nog terug. Pas als je de prullenbak leegmaakt, is het echt weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een logische mappenstructuur?",
        opties=[
            "Mappen in duidelijke lagen, van algemeen naar specifiek",
            "Alle bestanden los in één grote map, gesorteerd op naam",
            "Mappen met een nummer in de plaats van een naam",
            "Mappen die je elke maand opnieuw aanmaakt",
        ],
        antwoord=0,
        uitleg="Een goede structuur gaat van breed naar smal, bijvoorbeeld School, dan het vak, dan het schooljaar. Dan weet je altijd waar iets hoort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakt een bestandsnaam bruikbaar?",
        opties=[
            "Hij zegt waar het bestand over gaat",
            "Hij is kort en zonder rare tekens",
            "Hij gebruikt de datum in dezelfde vorm als de andere bestanden",
            "Hij bestaat uit een willekeurige reeks letters",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een naam moet zeggen wat erin zit en passen bij de afspraken van de organisatie. Zo vindt ook een collega het terug.",
    ),
    dict(
        type="waarofniet",
        vraag="Een datum in de vorm 2027-03-08 sorteert netjes op chronologische volgorde.",
        antwoord=True,
        uitleg="Klopt. Met jaar, maand en dag in die orde staan je bestanden automatisch op datum. Met 8-3-2027 loopt die volgorde door elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is uploaden?",
        opties=[
            "Een bestand van je toestel naar het internet sturen",
            "Een bestand van het internet naar je toestel halen",
            "Een bestand op je toestel naar een andere map slepen",
            "Een bestand op je toestel een nieuwe naam geven",
        ],
        antwoord=0,
        uitleg="Uploaden gaat omhoog, van jou naar een server. Downloaden gaat de andere kant op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je haalt een werkblad van de website van je school naar je laptop. Wat doe je?",
        opties=[
            "Downloaden",
            "Uploaden",
            "Een back-up maken",
            "Een bestand herbenoemen",
        ],
        antwoord=0,
        uitleg="Van het internet naar jou is downloaden. Zet je iets van jou op het internet, dan is het uploaden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een back-up?",
        opties=[
            "Een kopie op een andere plaats, voor als het origineel verloren gaat",
            "Een bestand dat je op je bureaublad klaarzet om het snel te openen",
            "Een map waarin je alle verwijderde bestanden bewaart",
            "De laatste versie van een bestand waaraan je werkt",
        ],
        antwoord=0,
        uitleg="Een back-up of reservekopie staat elders: op een externe schijf of in de cloud. Anders verlies je bij een defect alles tegelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een reservekopie op dezelfde computer als het origineel beschermt je even goed.",
        antwoord=False,
        uitleg="Als die computer stukgaat of gestolen wordt, ben je beide kwijt. Een back-up hoort op een andere plaats te staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is cloudopslag?",
        opties=[
            "Je bestanden bewaren op een server die je via het internet bereikt",
            "Je bestanden bewaren op een externe harde schijf naast je computer",
            "Je bestanden bewaren in de prullenbak van je computer",
            "Je bestanden op papier afdrukken en bijhouden in een map",
        ],
        antwoord=0,
        uitleg="OneDrive en Google Drive zijn cloudopslag. Je bestanden staan elders en je geraakt er vanaf elk toestel aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn voordelen van cloudopslag?",
        opties=[
            "Je geraakt aan je bestanden van op elk toestel",
            "Je bestanden blijven bestaan als je laptop stukgaat",
            "Je kan een map delen met iemand anders",
            "Je hebt er geen internetverbinding voor nodig",
        ],
        antwoord=[0, 1, 2],
        uitleg="Overal bij je bestanden, veilig bij een defect en makkelijk delen. Zonder internet geraak je er wel niet aan, en dat is het nadeel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bestand herbenoemen verandert de inhoud van dat bestand.",
        antwoord=False,
        uitleg="Alleen de naam verandert. De inhoud blijft precies dezelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil meerdere bestanden in één keer naar een andere map verplaatsen. Wat doe je eerst?",
        opties=[
            "Je selecteert ze allemaal samen",
            "Je geeft ze allemaal eerst een nieuwe naam",
            "Je maakt van elk bestand eerst een kopie",
            "Je zet ze een voor een in de prullenbak",
        ],
        antwoord=0,
        uitleg="Selecteren komt eerst: met de Ctrl-toets kies je losse bestanden, met de Shift-toets een hele reeks. Daarna verplaats je ze in één beweging.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee bestanden in dezelfde map mogen niet exact dezelfde naam hebben.",
        antwoord=True,
        uitleg="Klopt. In één map moet elke naam uniek zijn. In twee verschillende mappen mag dezelfde naam wel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we het programma van Windows waarmee je je mappen en bestanden beheert?",
        antwoord=["de verkenner", "verkenner"],
        uitleg="In de Verkenner zie je links het navigatievenster en kan je met het detailvenster de gegevens van een bestand bekijken.",
    ),
]
