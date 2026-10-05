# -*- coding: utf-8 -*-
"""Een Franse tekst begrijpen: onderwerp, hoofdgedachte, hoofdpunten, gegevens.

Uit de vakfiche Frans van de 2de graad dubbele finaliteit, onderdeel "Lezen en
luisteren". Alleen het lezen: luisteren vraagt geluid.

Lezen weegt 30 % van het examen, evenveel als luisteren, en samen is dat zestig
procent. Dit is dus het zwaarste onderdeel dat je hier kan inoefenen.

Het ERK-niveau is A2. Dat betekent korte, duidelijke teksten over het dagelijkse
leven: een zoekertje, een bericht van de school, een recept, een verslagje van
een weekend, een affiche, een beoordeling. Je moet kunnen zeggen waarover een
tekst gaat, wat de belangrijkste boodschap is, welke punten die boodschap
ondersteunen, en je moet er de gegevens uit kunnen halen die je nodig hebt.

Elke leesvraag staat op een echt Frans tekstje. Een vraag over lezen zonder
tekst is geen leesvraag. De tekstjes hieronder zijn kort genoeg om op een
telefoon te lezen.

Deel 1 oefent de vier vragen van de fiche op gewone teksten: het onderwerp, de
hoofdgedachte, de hoofdpunten en losse gegevens. Deel 2 oefent het selecteren
van informatie in teksten waar je iets moet opzoeken: openingsuren, een
prijslijst, een instructie, een bericht tussen twee mensen.
"""

ANNONCE = (
    "À vendre : vélo de ville bleu, taille moyenne. Je l'ai acheté il y a deux ans et je roule "
    "très peu. Les pneus sont neufs. Prix : 95 euros. Je ne fais pas d'envoi : il faut venir le "
    "chercher à Liège, le samedi ou le dimanche."
)
ECOLE = (
    "Chers parents, le lundi 12 octobre, les cours commencent à 10 h. Les professeurs ont une "
    "réunion le matin. La garderie est ouverte à partir de 8 h pour les élèves qui prennent le "
    "bus. Le repas de midi se passe comme d'habitude."
)
RECETTE = (
    "Pour quatre personnes : coupez deux oignons et faites-les cuire cinq minutes dans un peu "
    "d'huile. Ajoutez le riz et un litre d'eau chaude. Laissez cuire vingt minutes sans "
    "couvercle. Salez à la fin, pas avant."
)
MER = (
    "Samedi, je suis allée à la mer avec ma cousine. Nous avons pris le train de 7 h 40 pour "
    "éviter le monde. Il faisait froid, mais le ciel était bleu. Nous avons marché deux heures "
    "sur la plage et nous avons mangé des frites. Le soir, j'avais mal aux jambes, mais j'étais "
    "contente."
)
ESCALADE = (
    "Tu as entre 15 et 18 ans ? Viens essayer l'escalade gratuitement le mercredi après-midi. "
    "Pas besoin de matériel : nous prêtons tout. Inscris-toi avant le 30 septembre, le groupe "
    "est limité à douze jeunes."
)
HOTEL = (
    "Hôtel correct mais bruyant. La chambre était propre et le petit-déjeuner très bon. Par "
    "contre, la fenêtre donne sur la rue et j'ai mal dormi. Pour deux nuits, ça va. Pour une "
    "semaine, je chercherais ailleurs."
)

DEEL1 = [
    # --- Le vélo à vendre : een zoekertje -------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {ANNONCE} » Waarover gaat deze tekst?",
         opties=["iemand verkoopt zijn fiets",
                 "iemand zoekt een fiets om te kopen",
                 "iemand vertelt over een fietstocht",
                 "iemand laat zijn fiets herstellen"],
         antwoord=0,
         uitleg="À vendre betekent te koop. Het onderwerp van een tekst zeg je in enkele woorden: hier verkoopt iemand een fiets."),
    dict(type="meerkeuze",
         vraag="Hetzelfde zoekertje over de fiets. Wat is de hoofdgedachte, dus de belangrijkste boodschap?",
         opties=["Deze fiets is weinig gebruikt en kost 95 euro.",
                 "Fietsen in de stad is goedkoper dan de bus nemen.",
                 "Een fiets van twee jaar oud is niets meer waard.",
                 "Nieuwe buitenbanden zijn duurder dan een fiets."],
         antwoord=0,
         uitleg="Je roule très peu betekent ik rijd er heel weinig mee. Samen met de prijs is dat waar het zoekertje om draait."),
    dict(type="invultekst",
         vraag="Nog altijd het zoekertje. Hoeveel euro kost de fiets? Schrijf alleen het getal.",
         antwoord=["95"],
         uitleg="Prix : 95 euros. Prix betekent prijs."),
    dict(type="meerkeuze",
         vraag="Welke punten over de fiets staan er letterlijk in het zoekertje?",
         opties=["De fiets is blauw.",
                 "De buitenbanden zijn nieuw.",
                 "Je moet de fiets zelf komen halen.",
                 "De fiets heeft zeven versnellingen."],
         antwoord=[0, 1, 2],
         uitleg="Vélo de ville bleu, les pneus sont neufs, il faut venir le chercher. Over versnellingen staat er niets."),
    dict(type="waarofniet",
         vraag="Volgens het zoekertje stuurt de verkoper de fiets met de post op.",
         antwoord=False,
         uitleg="Je ne fais pas d'envoi betekent ik verstuur niet. Je moet de fiets in Luik komen ophalen."),
    # --- Le message de l'école ------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit bericht van een school: « {ECOLE} » Wat is de belangrijkste boodschap?",
         opties=["De lessen beginnen die dag later dan gewoonlijk.",
                 "De school is die hele dag gesloten.",
                 "De leerlingen moeten die dag thuis blijven eten.",
                 "De bussen rijden die dag niet."],
         antwoord=0,
         uitleg="Les cours commencent à 10 h betekent de lessen beginnen om 10 uur. Dat is de boodschap; de rest legt uit waarom en hoe."),
    dict(type="invultekst",
         vraag="Hetzelfde bericht van de school. Vanaf welk uur is de opvang open? Schrijf alleen het getal.",
         antwoord=["8"],
         uitleg="La garderie est ouverte à partir de 8 h. La garderie is de opvang, à partir de betekent vanaf."),
    dict(type="meerkeuze",
         vraag="Nog het bericht van de school. Waarom beginnen de lessen later?",
         opties=["De leraren hebben die ochtend een vergadering.",
                 "Er zijn werken bezig in het schoolgebouw.",
                 "Het is een feestdag voor de hele school.",
                 "De leerlingen hebben die ochtend een uitstap."],
         antwoord=0,
         uitleg="Les professeurs ont une réunion le matin. Une réunion is een vergadering."),
    dict(type="waarofniet",
         vraag="Volgens het bericht van de school verloopt het middagmaal die dag zoals altijd.",
         antwoord=True,
         uitleg="Le repas de midi se passe comme d'habitude. Comme d'habitude betekent zoals gewoonlijk."),
    # --- La recette : prescriptieve tekst --------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit recept: « {RECETTE} » Wat doe je het eerst?",
         opties=["de uien snijden en bakken",
                 "de rijst bij het water doen",
                 "een liter water opwarmen",
                 "zout in de pan strooien"],
         antwoord=0,
         uitleg="Coupez deux oignons et faites-les cuire staat vooraan. Couper is snijden, un oignon is een ui."),
    dict(type="invultekst",
         vraag="Hetzelfde recept. Hoeveel minuten moet de rijst koken? Schrijf alleen het getal.",
         antwoord=["20"],
         uitleg="Laissez cuire vingt minutes. Vingt is twintig."),
    dict(type="waarofniet",
         vraag="Volgens het recept zout je het gerecht pas op het einde.",
         antwoord=True,
         uitleg="Salez à la fin, pas avant betekent zout op het einde, niet eerder."),
    dict(type="meerkeuze",
         vraag="Nog het recept. Voor hoeveel mensen is het bedoeld, en wat doe je met het deksel?",
         opties=["voor vier mensen, en je laat het deksel eraf",
                 "voor twee mensen, en je legt het deksel erop",
                 "voor vier mensen, en je legt het deksel erop",
                 "voor zes mensen, en je laat het deksel eraf"],
         antwoord=0,
         uitleg="Pour quatre personnes en sans couvercle. Sans betekent zonder, un couvercle is een deksel."),
    # --- Le week-end à la mer : narratieve tekst -------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit verslagje: « {MER} » Waarover gaat de tekst?",
         opties=["een daguitstap naar de zee",
                 "een verhuis naar de kust",
                 "een treinreis die misliep",
                 "een week vakantie in Frankrijk"],
         antwoord=0,
         uitleg="Samedi, je suis allée à la mer: zaterdag ben ik naar de zee geweest. Het blijft bij één dag."),
    dict(type="meerkeuze",
         vraag="Hetzelfde verslagje over de zee. Waarom namen ze de trein van 7 u 40?",
         opties=["om de drukte te vermijden",
                 "omdat er later geen trein meer was",
                 "omdat dat de goedkoopste trein was",
                 "om nog te kunnen ontbijten op de trein"],
         antwoord=0,
         uitleg="Pour éviter le monde betekent om de drukte te vermijden. Le monde is hier de mensenmassa."),
    dict(type="waarofniet",
         vraag="In het verslagje over de zee was het warm weer met een grijze lucht.",
         antwoord=False,
         uitleg="Il faisait froid, mais le ciel était bleu: het was koud, maar de lucht was blauw. Net het omgekeerde dus."),
    dict(type="meerkeuze",
         vraag="Nog het verslagje over de zee. Welke twee dingen voelde de schrijfster 's avonds?",
         opties=["Ze had pijn in haar benen.",
                 "Ze was tevreden.",
                 "Ze had spijt van de uitstap.",
                 "Ze had honger."],
         antwoord=[0, 1],
         uitleg="J'avais mal aux jambes, mais j'étais contente. Avoir mal aux jambes is pijn in de benen hebben, content zijn is tevreden zijn."),
    # --- L'affiche en l'avis ---------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees deze affiche: « {ESCALADE} » Wat wil deze tekst vooral?",
         opties=["jongeren overhalen om te komen klimmen",
                 "uitleggen hoe je veilig moet klimmen",
                 "de mening van de schrijver geven over sport",
                 "vertellen hoe een klimles verlopen is"],
         antwoord=0,
         uitleg="Viens essayer en inscris-toi zijn bevelen aan jou. Een tekst die je probeert te overtuigen, is een persuasieve tekst."),
    dict(type="invultekst",
         vraag="Dezelfde affiche. Voor hoeveel jongeren is er plaats? Schrijf alleen het getal.",
         antwoord=["12"],
         uitleg="Le groupe est limité à douze jeunes. Douze is twaalf."),
    dict(type="meerkeuze",
         vraag=f"Lees deze beoordeling van een hotel: « {HOTEL} » Wat vond de klant goed, en wat niet?",
         opties=["de kamer en het ontbijt goed, het geluid niet",
                 "het ontbijt goed, de kamer en het geluid niet",
                 "de kamer goed, het ontbijt en het geluid niet",
                 "alles goed behalve het ontbijt"],
         antwoord=0,
         uitleg="La chambre était propre en le petit-déjeuner très bon, maar par contre j'ai mal dormi door het lawaai van de straat. Par contre betekent daarentegen."),
]

BIBLIO = (
    "Bibliothèque de Namur — lundi : fermé. Mardi et jeudi : 10 h – 18 h. Mercredi : 14 h – 19 h. "
    "Vendredi : 10 h – 16 h. Samedi : 9 h – 13 h. Fermée les jours fériés."
)
PRIX = (
    "Piscine communale — entrée adulte : 4,50 €. Jeunes de moins de 18 ans : 2,50 €. Carte de "
    "dix entrées : 20 € (jeunes) ou 38 € (adultes). Location d'une serviette : 2 €. Le bonnet de "
    "bain est obligatoire et n'est pas en location."
)
SMS = (
    "Lou : Tu viens toujours demain ? — Sacha : Oui, mais je finis à 17 h, donc j'arrive vers "
    "18 h 30. — Lou : Pas de souci, on mange à 19 h. Tu peux apporter un dessert ? — Sacha : "
    "D'accord. Sucré ou des fruits ? — Lou : Des fruits, il y a déjà un gâteau."
)
MODE = (
    "Avant le premier lavage : lavez le vêtement seul, à 30 degrés. N'utilisez pas de "
    "sèche-linge. Repassez à l'envers, sur une température moyenne. En cas de tache, lavez tout "
    "de suite à l'eau froide."
)
ARTICLE = (
    "Depuis la rentrée, les élèves de deux écoles de Charleroi laissent leur téléphone dans un "
    "casier pendant les cours. Les professeurs trouvent les classes plus calmes. Certains élèves "
    "se plaignent, mais la plupart disent qu'ils se concentrent mieux. L'école va garder la règle "
    "jusqu'en juin."
)
JOB = (
    "Madame, Je vous écris au sujet de votre annonce pour un job d'été. Je suis élève en "
    "quatrième année et je cherche du travail en juillet. J'ai déjà aidé dans le magasin de mes "
    "grands-parents, donc je connais la caisse. Je suis libre du 1er au 31 juillet, sauf le "
    "week-end du 14. Pourriez-vous me dire quand je peux venir me présenter ?"
)

DEEL2 = [
    # --- Les heures d'ouverture ------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees deze openingsuren: « {BIBLIO} » Je kan alleen op woensdag. Wanneer kan je gaan?",
         opties=["in de namiddag, tussen 14 en 19 uur",
                 "in de voormiddag, tussen 10 en 18 uur",
                 "in de voormiddag, tussen 9 en 13 uur",
                 "de hele dag, van 10 tot 19 uur"],
         antwoord=0,
         uitleg="Mercredi is woensdag: 14 h – 19 h. Informatie selecteren betekent dat je alleen de regel zoekt die je nodig hebt."),
    dict(type="invultekst",
         vraag="Dezelfde openingsuren. Op welke dag van de week is de bibliotheek gesloten? Schrijf de dag in het Nederlands.",
         antwoord=["maandag"],
         uitleg="Lundi : fermé. Lundi is maandag, fermé betekent gesloten."),
    dict(type="waarofniet",
         vraag="Volgens die openingsuren kan je er op zaterdagnamiddag terecht.",
         antwoord=False,
         uitleg="Samedi : 9 h – 13 h. Om 13 uur gaat ze toe, dus in de namiddag kan je er niet meer in."),
    dict(type="meerkeuze",
         vraag="Nog die openingsuren. Op welke twee dagen gaat de bibliotheek om 10 uur open?",
         opties=["dinsdag",
                 "vrijdag",
                 "woensdag",
                 "zaterdag"],
         antwoord=[0, 1],
         uitleg="Mardi et jeudi : 10 h – 18 h en vendredi : 10 h – 16 h. Donderdag staat niet bij de keuzes, dinsdag en vrijdag wel."),
    # --- Les prix de la piscine ------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees deze prijslijst: « {PRIX} » Je bent zestien en gaat één keer zwemmen. Wat betaal je?",
         opties=["2,50 euro", "4,50 euro", "20 euro", "2 euro"],
         antwoord=0,
         uitleg="Jeunes de moins de 18 ans : 2,50 €. Moins de 18 ans betekent jonger dan achttien."),
    dict(type="invultekst",
         vraag="Dezelfde prijslijst. Hoeveel euro kost een kaart van tien beurten voor een jongere? Schrijf alleen het getal.",
         antwoord=["20"],
         uitleg="Carte de dix entrées : 20 € (jeunes). Une entrée is hier een beurt."),
    dict(type="waarofniet",
         vraag="Volgens de prijslijst kan je er een badmuts huren.",
         antwoord=False,
         uitleg="Le bonnet de bain est obligatoire et n'est pas en location: de badmuts is verplicht en is niet te huur. Alleen een handdoek kan je huren."),
    dict(type="meerkeuze",
         vraag="Nog de prijslijst van het zwembad. Twee volwassenen gaan samen één keer zwemmen en huren één handdoek. Hoeveel betalen ze?",
         opties=["11 euro", "9 euro", "6,50 euro", "13 euro"],
         antwoord=0,
         uitleg="Twee keer 4,50 euro is 9 euro, plus 2 euro voor de handdoek is 11 euro."),
    # --- La conversation --------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit gesprekje: « {SMS} » Hoe laat komt Sacha aan?",
         opties=["rond 18 u 30", "om 17 uur", "om 19 uur", "rond 17 u 30"],
         antwoord=0,
         uitleg="J'arrive vers 18 h 30. Vers betekent rond, omstreeks."),
    dict(type="meerkeuze",
         vraag="Hetzelfde gesprekje. Wat moet Sacha meebrengen, en waarom net dat?",
         opties=["fruit, omdat er al een cake is",
                 "een cake, omdat er nog geen dessert is",
                 "iets zoets, omdat Lou dat liever heeft",
                 "niets, Lou zorgt voor alles"],
         antwoord=0,
         uitleg="Des fruits, il y a déjà un gâteau: fruit, er is al een cake. Déjà betekent al."),
    dict(type="waarofniet",
         vraag="In dat gesprekje vindt Lou het geen probleem dat Sacha later komt.",
         antwoord=True,
         uitleg="Pas de souci betekent geen zorgen, geen probleem."),
    dict(type="invultekst",
         vraag="Nog dat gesprekje. Hoe laat eten ze? Schrijf alleen het getal van het uur.",
         antwoord=["19"],
         uitleg="On mange à 19 h."),
    # --- Le mode d'emploi -------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit waslabel: « {MODE} » Wat mag je niet doen?",
         opties=["het kledingstuk in de droogkast steken",
                 "het kledingstuk alleen wassen",
                 "het kledingstuk binnenstebuiten strijken",
                 "een vlek met koud water uitwassen"],
         antwoord=0,
         uitleg="N'utilisez pas de sèche-linge: gebruik geen droogkast. De drie andere dingen vraagt het label juist wel."),
    dict(type="invultekst",
         vraag="Hetzelfde waslabel. Op hoeveel graden moet je wassen? Schrijf alleen het getal.",
         antwoord=["30"],
         uitleg="Lavez le vêtement seul, à 30 degrés."),
    dict(type="waarofniet",
         vraag="Volgens dat waslabel moet je een vlek meteen met koud water uitwassen.",
         antwoord=True,
         uitleg="En cas de tache, lavez tout de suite à l'eau froide. Une tache is een vlek, tout de suite betekent onmiddellijk."),
    # --- L'article de journal ---------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit krantenstukje: « {ARTICLE} » Wat is de hoofdgedachte?",
         opties=["Twee scholen leggen de telefoons tijdens de les weg, en dat werkt.",
                 "Leerlingen in Charleroi mogen hun telefoon niet meer meebrengen.",
                 "Leraren willen dat telefoons overal verboden worden.",
                 "De regel over telefoons wordt in juni afgeschaft."],
         antwoord=0,
         uitleg="De tekst vertelt de maatregel en wat ze oplevert: rustiger klassen, en de meeste leerlingen zeggen dat ze beter opletten."),
    dict(type="meerkeuze",
         vraag="Hetzelfde krantenstukje. Welke punten staan er in de tekst?",
         opties=["De telefoons liggen tijdens de les in een kastje.",
                 "De leraren vinden de klassen rustiger.",
                 "De school houdt de regel aan tot juni.",
                 "De ouders hebben om de regel gevraagd."],
         antwoord=[0, 1, 2],
         uitleg="Un casier is een kastje, plus calmes is rustiger, jusqu'en juin is tot in juni. Over de ouders staat er niets."),
    dict(type="waarofniet",
         vraag="Volgens dat krantenstukje is elke leerling tevreden met de regel.",
         antwoord=False,
         uitleg="Certains élèves se plaignent: sommige leerlingen klagen. La plupart, de meesten, zijn wel tevreden, maar niet iedereen."),
    # --- La lettre de candidature ------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees deze mail: « {JOB} » Waarom schrijft deze leerling?",
         opties=["om te reageren op een zoekertje voor vakantiewerk",
                 "om uitleg te vragen over een cursus",
                 "om een job op te zeggen",
                 "om een winkel aan te bevelen"],
         antwoord=0,
         uitleg="Au sujet de votre annonce pour un job d'été: naar aanleiding van uw zoekertje voor een zomerjob. Au sujet de betekent over, in verband met."),
    dict(type="meerkeuze",
         vraag="Dezelfde mail. Wanneer is de leerling niet vrij?",
         opties=["het weekend van 14 juli",
                 "de eerste week van juli",
                 "elk weekend van de maand",
                 "de laatste dag van juli"],
         antwoord=0,
         uitleg="Libre du 1er au 31 juillet, sauf le week-end du 14. Sauf betekent behalve."),
]
