# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Frans 🚀 Boost dubbele finaliteit.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof met andere vragen. Dezelfde pdf gaat dus bij
allebei de hoofdstukken.

Net als de vragen op het scherm dekt dit **alleen het schriftelijke Frans**:
lezen, schrijven, woordenschat en grammatica. Luisteren, spreken en de
gesprekken staan er niet in; daar heb je geluid en een gesprekspartner voor
nodig.

Het ERK-niveau is A2. Dat bepaalt de grens: présent, impératif, passé composé,
imparfait, passé récent, futur proche, futur simple en de conditionnel de
politesse. De plus-que-parfait, de subjonctif, de conditionnel als volwaardige
tijd, de betrekkelijke bijzin en de passieve vorm horen hier niet, ook niet in
een oefening.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm. Wie hier iets bijschrijft, legt het eerst naast
`../../boost-dubbele-finaliteit/frans.json` en naast de leerbundel van hetzelfde
thema in `maak_frans_df.py`.

Een leesvraag hoort op een echt Frans tekstje te staan, niet op het begrip
alleen. De leesbundels dragen daarom hun eigen tekst mee.

Op papier staan de accenten er wél gewoon op. Dat online invulantwoorden soms
zonder accenten vergeleken worden, is een toegeving aan het toetsenbord, geen
regel over hoe je het schrijft.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-dubbele-finaliteit".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

VAK = "Frans"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
NIVEAU = "-boost-dubbele-finaliteit"
VOOR = "oefenbundel-"

W = "150px"
WW = "220px"
WL = "280px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Zet de accenten erbij: op papier horen ze er gewoon op.",
    "Ken je een woord niet? Kijk eerst of het op een Nederlands of Engels woord lijkt.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

HOE_LEZEN = [
    "Lees de tekst eerst helemaal door. Je moet niet elk woord kennen.",
    "Onderstreep de woorden die je niet kent en probeer ze eerst te raden uit de zin eromheen.",
    "Kom bij elke vraag terug naar de tekst.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", DF)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS[VOOR + slug + NIVEAU] = b


# ============================================================
zet("een-franse-tekst-begrijpen",
    titel="Een Franse tekst begrijpen",
    onder="Twee teksten en {aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE_LEZEN,
    reeksen=[
        dict(kop="Texte 1", opdracht="Lees deze tekst. De vragen erna gaan alleen hierover.",
             oefeningen=[
                 ("tekst",
                  "<h3 style='margin:0 0 .4em'>Un potager sur le toit</h3>"
                  "<p>Depuis le mois de mai, il y a un potager sur le toit de l'école "
                  "technique de Charleroi. Les élèves de troisième y cultivent des tomates, "
                  "des courgettes et des herbes. Le potager fait quatre-vingts mètres carrés.</p>"
                  "<p>„Au début, personne ne croyait au projet”, raconte Monsieur Dubois, le "
                  "professeur de techniques. „Le toit était vide depuis vingt ans. Maintenant, "
                  "quinze élèves y travaillent chaque semaine, le mardi après-midi.”</p>"
                  "<p>Les légumes vont à la cuisine de l'école. La cuisinière prépare une soupe "
                  "avec les courgettes, et les tomates vont dans les sandwichs du midi. "
                  "Cependant, la récolte n'est pas encore assez grande pour toute l'école: "
                  "environ un repas sur dix contient des légumes du toit.</p>"
                  "<p>L'année prochaine, l'école va agrandir le potager. „Nous allons ajouter "
                  "des fraises”, dit un élève. „Et nous aimerions vendre nos légumes au marché "
                  "du samedi. L'argent serait pour du nouveau matériel.”</p>"),
             ]),
        dict(kop="Het onderwerp en de hoofdgedachte",
             opdracht="Antwoord in het Nederlands, tenzij er iets anders staat.",
             oefeningen=[
                 ("kort", "Schrijf het onderwerp van deze tekst in enkele woorden.",
                  "een schooltuin op het dak van een school", WL),
                 ("open", "Wat is de hoofdgedachte van de tekst? Eén zin.",
                  "Een school heeft haar lege dak omgebouwd tot een tuin die de schoolkeuken "
                  "mee bevoorraadt, en wil die volgend jaar uitbreiden.", 3),
                 ("kort", "Hoe groot is de tuin?", "tachtig vierkante meter", W),
                 ("kort", "Op welke dag werken de leerlingen in de tuin?",
                  "op dinsdagnamiddag", W),
                 ("kort", "Hoeveel leerlingen werken er elke week?", "vijftien", W),
             ]),
        dict(kop="De hoofdpunten",
             opdracht="Zoek de gegevens in de tekst terug.",
             oefeningen=[
                 ("open", "Noem drie dingen die in de tuin gekweekt worden.",
                  "Tomaten, courgettes en kruiden.", 2),
                 ("open", "Wat gebeurt er met de oogst? Geef twee dingen uit de tekst.",
                  "De oogst gaat naar de schoolkeuken: de kokkin maakt soep van de courgettes "
                  "en de tomaten gaan in de sandwiches van de middag.", 3),
                 ("open", "Welk voorbehoud maakt de tekst bij het succes?",
                  "De oogst is nog niet groot genoeg voor de hele school: ongeveer één maaltijd "
                  "op tien bevat legumes van het dak.", 3),
                 ("open", "Welke twee plannen heeft de school voor volgend jaar?",
                  "De tuin uitbreiden met aardbeien, en de legumes verkopen op de "
                  "zaterdagmarkt om nieuw materiaal te kopen.", 3),
                 ("waar", "Volgens de tekst geloofde iedereen van het begin in het project.",
                  False),
             ]),
        dict(kop="Woorden raden uit de tekst",
             opdracht="Gebruik de zin eromheen. Sla je woordenboek pas daarna open.",
             oefeningen=[
                 ("rij", [("le potager", "de tuin / de legumetuin"),
                          ("le toit", "het dak"),
                          ("la récolte", "de oogst"),
                          ("cependant", "nochtans / toch"),
                          ("agrandir", "groter maken / uitbreiden"),
                          ("environ", "ongeveer")],
                  "Wat betekent dit woord in de tekst?", WW),
                 ("open", "„L'argent serait pour du nouveau matériel.” Naar welk geld verwijst "
                          "'l'argent' in deze zin?",
                  "Naar het geld van de legumes die ze op de zaterdagmarkt willen verkopen.", 3),
             ]),
        dict(kop="Texte 2", opdracht="Een ander soort tekst: gegevens zoeken.",
             oefeningen=[
                 ("tekst",
                  "<h3 style='margin:0 0 .4em'>Piscine communale — horaire et tarifs</h3>"
                  "<p><b>Lundi:</b> fermé (nettoyage)<br>"
                  "<b>Mardi et jeudi:</b> 7h–9h et 16h–21h<br>"
                  "<b>Mercredi:</b> 13h–19h<br>"
                  "<b>Vendredi:</b> 16h–22h<br>"
                  "<b>Samedi et dimanche:</b> 9h–18h</p>"
                  "<p><b>Tarifs:</b> adultes 5,50 €&nbsp;· enfants (&minus;12 ans) 3,20 €&nbsp;· "
                  "étudiants 4 €&nbsp;· abonnement 10 entrées 45 €</p>"
                  "<p>Le bonnet de bain est obligatoire. Les enfants de moins de huit ans "
                  "doivent être accompagnés d'un adulte. Pendant les vacances scolaires, la "
                  "piscine ouvre aussi le lundi de 13h à 18h.</p>"),
             ]),
        dict(kop="Gegevens uit de tekst halen",
             opdracht="Antwoord kort. Soms moet je twee gegevens samenleggen.",
             oefeningen=[
                 ("kort", "Op welke dag is het zwembad gesloten buiten de vakantie?",
                  "op maandag", W),
                 ("kort", "Hoeveel betaalt een kind van tien jaar?", "3,20 euro", W),
                 ("kort", "Vanaf hoe laat kan je er op woensdag zwemmen?", "vanaf 13 uur", W),
                 ("open", "Een gezin met twee ouders en twee kinderen van 9 en 14 jaar gaat "
                          "zwemmen. Reken uit wat ze samen betalen en schrijf je bewerking op.",
                  "Twee volwassenen: 2 x 5,50 = 11 euro. Het kind van 9: 3,20 euro. Het kind van "
                  "14 is geen kind meer volgens het tarief, dus 5,50 euro. Samen 11 + 3,20 + "
                  "5,50 = 19,70 euro.", 4),
                 ("open", "Wat moet je zeker meenemen, en wat geldt er voor een kind van zes "
                          "jaar?",
                  "Een badmuts is verplicht, en een kind van minder dan acht jaar moet door een "
                  "volwassene begeleid worden.", 3),
                 ("waar", "Tijdens de schoolvakantie blijft het zwembad op maandag gesloten.",
                  False),
             ]),
    ],
)

# ============================================================
zet("tekstsoorten-tekstverbanden-en-leesstrategieen",
    titel="Tekstsoorten, tekstverbanden en leesstrategieën",
    onder="Zes tekstjes en {aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE_LEZEN,
    reeksen=[
        dict(kop="Zes korte teksten",
             opdracht="Lees ze alle zes. De vragen erna verwijzen naar hun nummer.",
             oefeningen=[
                 ("tekst",
                  "<p><b>1.</b> « Mélangez la farine et les œufs. Ajoutez le lait petit à petit. "
                  "Laissez reposer la pâte pendant trente minutes. Ne mettez pas le beurre "
                  "avant. »</p>"
                  "<p><b>2.</b> « La Meuse traverse la Belgique sur une longueur de "
                  "cent-quatre-vingts kilomètres. Elle prend sa source en France et se termine "
                  "aux Pays-Bas. »</p>"
                  "<p><b>3.</b> « Achetez maintenant ! Nos vélos électriques sont à moitié prix "
                  "jusqu'au 30 avril. Ne manquez pas cette occasion unique ! »</p>"
                  "<p><b>4.</b> « À mon avis, les examens en juin sont mal placés. Les élèves "
                  "sont fatigués et il fait trop chaud dans les classes. Je trouve qu'il "
                  "faudrait les organiser en mai. »</p>"
                  "<p><b>5.</b> « Samedi dernier, nous sommes partis à six heures du matin. Il "
                  "pleuvait. Après deux heures de route, la voiture s'est arrêtée au milieu de "
                  "l'autoroute. »</p>"
                  "<p><b>6.</b> « La nuit tombait sur le village endormi. Seule une fenêtre "
                  "brillait encore, comme un œil ouvert dans le noir. »</p>"),
             ]),
        dict(kop="Welke tekstsoort?",
             opdracht="Schrijf bij elk nummer de tekstsoort, en één woord uit de tekst dat het "
                      "verraadt.",
             oefeningen=[
                 ("rij", [("tekst 1", "prescriptief: mélangez, ajoutez"),
                          ("tekst 2", "informatief: cijfers en feiten"),
                          ("tekst 3", "persuasief: achetez maintenant"),
                          ("tekst 4", "opiniërend: à mon avis, je trouve"),
                          ("tekst 5", "narratief: samedi dernier, een verhaal"),
                          ("tekst 6", "literair: beeldspraak, comme un œil")],
                  "Welke tekstsoort is dit, en waaraan zie je het?", WL),
                 ("open", "Teksten 3 en 4 lijken op elkaar: ze geven beide een standpunt. "
                          "Waarin verschillen ze?",
                  "Tekst 3 wil je iets doen kopen, dus die overtuigt met het oog op een "
                  "handeling: dat is persuasief. Tekst 4 geeft alleen een mening en wil je "
                  "laten nadenken, zonder je iets te doen kopen: dat is opiniërend.", 4),
                 ("open", "In welke twee teksten staan werkwoorden in de impératif? Geef bij "
                          "elke tekst één voorbeeld.",
                  "In tekst 1 (mélangez, ajoutez, laissez) en in tekst 3 (achetez, ne manquez "
                  "pas).", 3),
             ]),
        dict(kop="Mening of feit",
             opdracht="Schrijf 'feit' of 'mening', en waarom.",
             oefeningen=[
                 ("rij", [("La Meuse fait 180 kilomètres.", "feit: te controleren"),
                          ("Je trouve qu'il fait trop chaud.", "mening: je trouve"),
                          ("Selon une étude récente, …", "feit met een bron erbij"),
                          ("D'après l'auteur, c'est une erreur.", "mening van de auteur"),
                          ("Il faudrait les organiser en mai.", "mening: wat zou moeten")],
                  "Feit of mening, en waaraan je het ziet.", WL),
                 ("waar", "Een zin met een cijfer erin is altijd een feit.", False),
             ]),
        dict(kop="Signaalwoorden",
             opdracht="Schrijf bij elk signaalwoord wat het aankondigt.",
             oefeningen=[
                 ("rij", [("mais", "een tegenstelling"),
                          ("donc", "een gevolg"),
                          ("parce que", "een reden"),
                          ("cependant", "een tegenstelling"),
                          ("de plus", "een toevoeging"),
                          ("par exemple", "een voorbeeld"),
                          ("d'abord … ensuite … enfin", "een opsomming in de tijd"),
                          ("si", "een voorwaarde")],
                  "Wat kondigt dit woord aan?", WW),
                 ("kort", "« Il pleuvait, ____ nous sommes restés à la maison. » Welk "
                          "signaalwoord past hier?", "donc", W),
                 ("open", "« Le vélo est pratique. Cependant, il est cher. » Herschrijf deze "
                          "twee zinnen tot één zin met 'mais'.",
                  "Le vélo est pratique, mais il est cher.", 2),
             ]),
        dict(kop="Verwijswoorden",
             opdracht="Naar wie of wat verwijst het vetgedrukte woord?",
             oefeningen=[
                 ("open", "« Mes voisins ont un chien. Il aboie toute la nuit. » Naar wie of "
                          "wat verwijst <b>il</b>?",
                  "Naar de hond van de buren, niet naar de buren zelf.", 2),
                 ("open", "« Marie a parlé à ses parents. Elle leur a tout expliqué. » Naar wie "
                          "verwijzen <b>elle</b> en <b>leur</b>?",
                  "Elle verwijst naar Marie, leur naar haar ouders.", 2),
                 ("open", "« Les élèves ont écrit une lettre au directeur. Ils l'ont déposée "
                          "lundi. » Naar wat verwijst <b>l'</b>?",
                  "Naar de brief, niet naar de directeur: je ziet het aan de e van déposée, die "
                  "bij une lettre hoort.", 3),
                 ("kort", "« J'ai deux sœurs. La plus jeune habite à Liège. » Over hoeveel "
                          "zussen gaat de tweede zin?", "over één", W),
             ]),
        dict(kop="Strategie",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Boven een tekst staat 'Les jeunes et le sommeil', met een foto van "
                          "een wekker erbij. Wat doe je het best vóór je begint te lezen?",
                  "Je gebruikt de titel en de foto om te voorspellen waarover het gaat, en je "
                  "bedenkt welke woorden je waarschijnlijk zal tegenkomen. Dan lees je sneller "
                  "en herken je meer.", 4),
                 ("open", "Je moet in een lange tekst alleen het uur van de vergadering "
                          "vinden. Lees je de tekst helemaal? Leg uit.",
                  "Nee, dan zoek je gericht: je laat je ogen over de tekst gaan tot je een uur "
                  "of een cijfer ziet staan. De hele tekst lezen doe je als je de hoofdgedachte "
                  "moet vinden.", 4),
                 ("waar", "Je moet elk Frans woord kennen om de hoofdgedachte van een tekst te "
                          "begrijpen.", False),
             ]),
    ],
)

# ============================================================
zet("de-franstalige-wereld-omgangsvormen-en-gewoontes",
    titel="De Franstalige wereld: omgangsvormen en gewoontes",
    reeksen=[
        dict(kop="Begroeten en afscheid nemen",
             opdracht="Schrijf wat je in deze situatie zegt.",
             oefeningen=[
                 ("rij", [("je komt om 9 uur een winkel binnen", "Bonjour madame / monsieur"),
                          ("je komt om 19 uur bij iemand thuis", "Bonsoir"),
                          ("je gaat weg bij iemand die je morgen terugziet", "À demain"),
                          ("je gaat weg uit een winkel", "Merci, au revoir"),
                          ("je begroet een vriend van je leeftijd", "Salut"),
                          ("iemand zegt merci tegen jou", "Je vous en prie / de rien")],
                  "Wat zeg je?", WW),
                 ("open", "Waarom zeg je in een Franse winkel bijna altijd 'bonjour madame' of "
                          "'bonjour monsieur' en niet gewoon 'bonjour'?",
                  "Het Frans vindt dat aanspreken hoffelijk: alleen bonjour klinkt kort en wat "
                  "onvriendelijk. Madame of monsieur erbij hoort bij de omgangsvorm.", 4),
                 ("waar", "Salut zeg je even goed tegen de directeur van de school als tegen "
                          "een vriend.", False),
             ]),
        dict(kop="Tu of vous",
             opdracht="Schrijf 'tu' of 'vous' en waarom.",
             oefeningen=[
                 ("rij", [("je praat met een leerling van je klas", "tu"),
                          ("je praat met de dokter", "vous"),
                          ("je schrijft een sollicitatiemail", "vous"),
                          ("je praat met je kleine neefje", "tu"),
                          ("je spreekt twee vrienden samen aan", "vous (meervoud van tu)"),
                          ("een onbekende op straat vraagt je de weg", "vous")],
                  "Tu of vous?", W),
                 ("open", "Vous heeft twee betekenissen. Leg ze uit met een voorbeeld.",
                  "Vous is het hoffelijke enkelvoud voor één onbekende of iemand boven je: "
                  "« Pourriez-vous m'aider, madame ? » En vous is ook het gewone meervoud van "
                  "tu, zelfs voor vrienden: « Vous venez, les gars ? »", 4),
                 ("kort", "Hoe heet het werkwoord voor 'tu zeggen tegen iemand'?",
                  "tutoyer", W),
                 ("open", "Een Franstalige collega zegt: « On peut se tutoyer ? » Wat vraagt "
                          "hij, en wat antwoord je als je dat goed vindt?",
                  "Hij vraagt of jullie elkaar met tu mogen aanspreken. Je antwoordt "
                  "bijvoorbeeld « Oui, bien sûr ! » en spreekt hem vanaf dan met tu aan.", 4),
             ]),
        dict(kop="Gewoontes en gebruiken",
             opdracht="Antwoord in het Nederlands.",
             oefeningen=[
                 ("open", "Wat is 'la bise', en wanneer doe je het wel en wanneer niet?",
                  "Een kus op de wang bij het begroeten. Je doet het bij familie en vrienden; "
                  "bij een onbekende of in een formele situatie geef je een hand.", 3),
                 ("kort", "Hoe zeggen ze in België 'septante' en 'nonante' in Frankrijk?",
                  "soixante-dix en quatre-vingt-dix", WL),
                 ("open", "Welke nationale feestdag valt op 21 juli, en welke op 14 juli?",
                  "21 juli is de nationale feestdag van België, 14 juli die van Frankrijk.", 2),
                 ("rij", [("la boulangerie", "de bakker, voor brood en croissants"),
                          ("la terrasse", "het terras van een café"),
                          ("le marché", "de markt, vaak op een vaste dag"),
                          ("l'apéritif", "een drankje met iets erbij, vóór de maaltijd")],
                  "Wat is dit?", WL),
                 ("waar", "In heel de Franstalige wereld wordt hetzelfde woord voor zeventig "
                          "gebruikt.", False),
             ]),
        dict(kop="Waar wordt Frans gesproken",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Noem drie landen buiten Frankrijk waar Frans een officiële taal is.",
                  "Bijvoorbeeld België, Zwitserland, Canada, Luxemburg, Senegal of Marokko.", 2),
                 ("kort", "Hoe heet het Franstalige deel van België in het Frans?",
                  "la Wallonie", W),
                 ("open", "Waarom hoort cultuur en omgangsvormen bij een taalexamen?",
                  "Omdat een taal spreken meer is dan woorden kennen: je moet weten hoe je "
                  "iemand aanspreekt, wanneer je tu of vous gebruikt en wat in dat land gewoon "
                  "is. Wie dat niet weet, klinkt onbeleefd zonder het te willen.", 5),
             ]),
    ],
)

# ============================================================
zet("schrijven-schriftelijke-interactie-en-leesbeleving",
    titel="Schrijven, schriftelijke interactie en leesbeleving",
    onder="Schrijfopdrachten en {aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Schrijf eerst in het klad wat je wil zeggen, dan pas in het net.",
        "Lees je tekst achteraan nog eens na op de uitgangen: de persoonsvorm en de adjectieven.",
        "Een korte juiste zin is beter dan een lange zin met vier fouten.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint. Je eigen tekst kan "
        "natuurlijk anders klinken dan het voorbeeld.",
    ],
    reeksen=[
        dict(kop="Een mail die past bij de situatie",
             opdracht="Schrijf de gevraagde zinnen. Let op tu of vous.",
             oefeningen=[
                 ("open", "Je schrijft naar een hotel om te vragen of er nog een kamer vrij is "
                          "van 2 tot 5 augustus, voor twee personen. Schrijf de aanspreking en "
                          "twee zinnen.",
                  "Madame, Monsieur, j'aimerais réserver une chambre pour deux personnes du 2 "
                  "au 5 août. Pourriez-vous me dire s'il y a encore une chambre libre ? "
                  "Merci d'avance.", 6),
                 ("open", "Je mailt een vriend om af te spreken aan het station om half zes. "
                          "Schrijf twee zinnen.",
                  "Salut Thomas ! On se retrouve à la gare à cinq heures et demie ? Réponds-moi "
                  "vite.", 4),
                 ("open", "Waarin verschillen die twee mails? Noem twee dingen.",
                  "De eerste is formeel: vous, een aanspreking met Madame, Monsieur, en de "
                  "hoffelijke vorm pourriez-vous. De tweede is informeel: tu, salut en een "
                  "kortere toon.", 4),
             ]),
        dict(kop="Een verslag over iets dat voorbij is",
             opdracht="Gebruik de verleden tijd.",
             oefeningen=[
                 ("open", "Schrijf vier zinnen over je weekend: waar je was, wat je gedaan hebt, "
                          "hoe het weer was en of het leuk was.",
                  "Samedi, je suis allé chez ma grand-mère à Namur. Nous avons fait une "
                  "promenade dans le parc. Il faisait froid mais le soleil brillait. "
                  "C'était un bon week-end.", 6),
                 ("open", "In die vier zinnen staan twee verleden tijden door elkaar. Leg uit "
                          "welke je waar gebruikt.",
                  "De passé composé voor wat één keer gebeurde en afgelopen is (je suis allé, "
                  "nous avons fait), en de imparfait voor de achtergrond: het weer en hoe het "
                  "was (il faisait froid, c'était).", 5),
             ]),
        dict(kop="Een formulier en een bericht",
             opdracht="Schrijf wat gevraagd wordt.",
             oefeningen=[
                 ("rij", [("Nom", "je familienaam"),
                          ("Prénom", "je voornaam"),
                          ("Date de naissance", "je geboortedatum"),
                          ("Lieu de naissance", "je geboorteplaats"),
                          ("Adresse", "je straat, nummer, postcode en gemeente"),
                          ("Numéro de téléphone", "je telefoonnummer")],
                  "Wat vul je hier in?", WL),
                 ("open", "Je kan vrijdag niet naar de sportclub. Schrijf een bericht van twee "
                          "zinnen aan de trainer, die u is.",
                  "Bonjour Monsieur, je ne peux pas venir à l'entraînement vendredi parce que "
                  "j'ai un rendez-vous chez le médecin. Je serai là mardi prochain.", 5),
                 ("open", "Je antwoordt op een berichtje van een vriendin die vraagt of je "
                          "meegaat naar de film. Schrijf een antwoord van twee zinnen waarin je "
                          "ja zegt en een uur voorstelt.",
                  "Oui, avec plaisir ! On se voit devant le cinéma à sept heures et demie ?", 4),
             ]),
        dict(kop="Leesbeleving",
             opdracht="Antwoord in volle zinnen. Hier is er geen juist of fout, maar je moet "
                      "je mening wel onderbouwen.",
             oefeningen=[
                 ("tekst",
                  "<p><i>La fenêtre</i></p>"
                  "<p>« Chaque matin, j'ouvre la fenêtre.<br>"
                  "Le bruit de la ville entre comme un ami<br>"
                  "qui arrive trop tôt et qui parle trop fort.<br>"
                  "Je le laisse entrer quand même. »</p>"),
                 ("open", "Waarmee vergelijkt de dichter het lawaai van de stad?",
                  "Met een vriend die te vroeg komt en te luid praat.", 2),
                 ("open", "Vind je die vergelijking geslaagd? Geef twee redenen voor je mening.",
                  "Een eigen antwoord. Bijvoorbeeld: ja, want een vriend is iets dat je graag "
                  "ziet en dat tegelijk stoort, en dat is precies hoe stadslawaai voelt. "
                  "Of: nee, want een vriend kies je zelf en het lawaai van een stad niet.", 5),
                 ("open", "Wat betekent de laatste regel « Je le laisse entrer quand même » "
                          "volgens jou?",
                  "Een eigen antwoord. Bijvoorbeeld: dat hij het lawaai aanvaardt omdat het bij "
                  "de stad hoort die hij graag ziet, ook al stoort het hem.", 4),
                 ("waar", "Bij een vraag naar je leesbeleving is elk antwoord goed, ook zonder "
                          "uitleg.", False),
             ]),
        dict(kop="Nakijken",
             opdracht="In elke zin staat één fout. Schrijf de zin juist op.",
             oefeningen=[
                 ("kort", "Les enfants joue dans le jardin.", "Les enfants jouent dans le jardin.",
                  WL),
                 ("kort", "J'ai allé au cinéma hier.", "Je suis allé au cinéma hier.", WL),
                 ("kort", "Elle est parti à six heures.", "Elle est partie à six heures.", WL),
                 ("kort", "Je voudrais un grande café.", "Je voudrais un grand café.", WL),
                 ("kort", "Nous avons mangés une pizza.", "Nous avons mangé une pizza.", WL),
                 ("open", "Welke drie dingen kijk je altijd na in je eigen Franse tekst?",
                  "De persoonsvorm bij zijn onderwerp, het adjectief bij zijn naamwoord, en bij "
                  "een passé composé of avoir of être het hulpwerkwoord is en of het deelwoord "
                  "moet meeveranderen.", 4),
             ]),
    ],
)

# ============================================================
zet("spreken-gesprekken-klank-en-spelling",
    titel="Spreken, gesprekken, klank en spelling",
    reeksen=[
        dict(kop="Een gesprek in gang houden",
             opdracht="Schrijf wat je zegt.",
             oefeningen=[
                 ("rij", [("je begrijpt iets niet", "Pardon ? / Je n'ai pas compris."),
                          ("je wil dat iemand trager spreekt",
                           "Pouvez-vous parler plus lentement ?"),
                          ("je wil tijd om na te denken", "Attendez, je réfléchis…"),
                          ("je weet het woord niet", "Comment dit-on … en français ?"),
                          ("je wil het gesprek beëindigen",
                           "Merci beaucoup, au revoir madame."),
                          ("je wil iets laten herhalen", "Pouvez-vous répéter, s'il vous plaît ?")],
                  "Wat zeg je?", WL),
                 ("open", "Je kent het woord 'paraplu' niet in het Frans. Hoe raak je er toch "
                          "mee rond in een gesprek? Geef één manier met een voorbeeldzin.",
                  "Je omschrijft het: « C'est la chose qu'on utilise quand il pleut. » Je kan "
                  "ook vragen « Comment dit-on 'paraplu' en français ? »", 4),
                 ("waar", "Als je een woord niet kent, is het beter te zwijgen dan het te "
                          "omschrijven.", False),
             ]),
        dict(kop="Hoffelijk vragen",
             opdracht="Herschrijf de zin hoffelijker.",
             oefeningen=[
                 ("kort", "Je veux un café.", "Je voudrais un café, s'il vous plaît.", WL),
                 ("kort", "Donnez-moi l'addition.",
                  "Pourriez-vous m'apporter l'addition, s'il vous plaît ?", WL),
                 ("kort", "Aidez-moi.", "Pourriez-vous m'aider, s'il vous plaît ?", WL),
                 ("kort", "Je veux travailler ici.", "J'aimerais travailler ici.", WL),
                 ("open", "Waarom klinkt 'je voudrais' hoffelijker dan 'je veux'?",
                  "Je veux is een eis: ik wil. Je voudrais is de hoffelijke vorm: ik zou willen. "
                  "Je laat de ander daarmee de ruimte om nee te zeggen.", 4),
             ]),
        dict(kop="Klank en spelling",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("ç in français", "een s-klank voor a, o of u"),
                          ("é in café", "een scherpe e"),
                          ("è in père", "een open e"),
                          ("ê in fenêtre", "een open e, met een accent circonflexe"),
                          ("ou in vous", "oe"),
                          ("u in tu", "uu"),
                          ("ai in maison", "è"),
                          ("eau in beau", "oo")],
                  "Welke klank is dit?", WW),
                 ("kort", "Schrijf het woord voor 'Frans' met het juiste teken onder de c.",
                  "français", W),
                 ("open", "Waarom schrijf je 'nous commençons' met een cedille en 'nous "
                          "commencerons' zonder?",
                  "De cedille houdt de c zacht voor een a, o of u. Voor een e of een i is de c "
                  "al zacht, dus dan heb je ze niet nodig.", 4),
                 ("kort", "Hoeveel klanken hoor je in 'ils parlent'?",
                  "twee woorden, maar de ent hoor je niet: het klinkt als il parl", WL),
                 ("open", "« Il parlait » en « ils parlaient » klinken hetzelfde. Hoe weet een "
                          "lezer dan het verschil, en hoe weet een luisteraar het?",
                  "Een lezer ziet het aan de s en de uitgang. Een luisteraar moet het uit de "
                  "rest van de zin halen, bijvoorbeeld uit een naam of een ander woord in het "
                  "meervoud.", 4),
                 ("waar", "De h aan het begin van 'hôtel' en 'homme' wordt in het Frans "
                          "uitgesproken.", False),
             ]),
        dict(kop="Vraag en antwoord",
             opdracht="Schrijf de vraag op drie manieren.",
             oefeningen=[
                 ("open", "Je wil vragen of iemand uit Brussel komt. Schrijf de vraag met "
                          "intonatie, met est-ce que, en met de omkering.",
                  "Tu viens de Bruxelles ? / Est-ce que tu viens de Bruxelles ? / Viens-tu de "
                  "Bruxelles ?", 4),
                 ("kort", "Vul aan met de juiste vorm: « ____-t-il à Liège ? » (habiter)",
                  "Habite", W),
                 ("open", "Welke van die drie vraagvormen gebruik je in een schriftelijke, "
                          "formele mail? Waarom?",
                  "De omkering of est-ce que: die zijn neutraal of formeel. De vorm met alleen "
                  "intonatie hoort bij spreektaal.", 4),
             ]),
    ],
)

# ============================================================
zet("woordvelden-mens-familie-gevoelens-en-gezondheid",
    titel="Woordvelden: mens, familie, gevoelens en gezondheid",
    reeksen=[
        dict(kop="De familie",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("de vader", "le père"), ("de moeder", "la mère"),
                          ("de broer", "le frère"), ("de zus", "la sœur"),
                          ("de grootvader", "le grand-père"), ("de grootmoeder", "la grand-mère"),
                          ("de zoon", "le fils"), ("de dochter", "la fille"),
                          ("de oom", "l'oncle"), ("de tante", "la tante"),
                          ("de neef", "le cousin"), ("de nicht", "la cousine")],
                  "Hoe zeg je dit in het Frans?", WW),
                 ("open", "« Le fils de ma tante » — hoe heet die persoon ten opzichte van jou, "
                          "en hoe zeg je dat in het Frans?",
                  "Dat is je neef: mon cousin.", 2),
                 ("kort", "Hoe zeg je 'mijn ouders'?", "mes parents", W),
             ]),
        dict(kop="Jezelf voorstellen",
             opdracht="Schrijf het antwoord in volle zinnen in het Frans.",
             oefeningen=[
                 ("open", "Stel jezelf voor in vier zinnen: je naam, je leeftijd, waar je woont "
                          "en wat je studeert.",
                  "Je m'appelle Lotte. J'ai seize ans. J'habite à Hasselt, en Belgique. "
                  "Je suis élève en troisième année.", 5),
                 ("kort", "Vul aan: « ____ quinze ans. »", "J'ai", W),
                 ("open", "Waarom staat daar 'j'ai' en niet 'je suis'?",
                  "Voor een leeftijd gebruikt het Frans avoir: j'ai quinze ans, letterlijk 'ik "
                  "heb vijftien jaar'. Je suis quinze ans bestaat niet.", 4),
                 ("rij", [("Quel âge as-tu ?", "J'ai seize ans."),
                          ("Où habites-tu ?", "J'habite à Genk."),
                          ("Comment t'appelles-tu ?", "Je m'appelle …"),
                          ("Tu as des frères et sœurs ?", "Oui, j'ai un frère.")],
                  "Antwoord op deze vraag.", WL),
             ]),
        dict(kop="Gevoelens",
             opdracht="Schrijf het Frans.",
             oefeningen=[
                 ("rij", [("blij", "content / heureux"), ("verdrietig", "triste"),
                          ("bang zijn", "avoir peur"), ("moe", "fatigué"),
                          ("boos", "fâché / en colère"), ("verrast", "surpris"),
                          ("honger hebben", "avoir faim"), ("dorst hebben", "avoir soif")],
                  "Hoe zeg je dit in het Frans?", WW),
                 ("kort", "Vul aan: « Elle est ____. » (blij, over een meisje)", "contente", W),
                 ("open", "Drie van die uitdrukkingen gaan met avoir in plaats van être. "
                          "Welke, en waarom is dat lastig voor een Nederlandstalige?",
                  "Avoir peur, avoir faim en avoir soif. Wij zeggen 'ik ben bang' en 'ik heb "
                  "honger' door elkaar; het Frans zegt bij alle drie avoir.", 4),
                 ("waar", "« J'ai froid » betekent dat het koud weer is.", False),
             ]),
        dict(kop="Het lichaam en bij de dokter",
             opdracht="Vul aan of antwoord kort.",
             oefeningen=[
                 ("rij", [("het hoofd", "la tête"), ("de arm", "le bras"),
                          ("het been", "la jambe"), ("de hand", "la main"),
                          ("de voet", "le pied"), ("de rug", "le dos"),
                          ("de buik", "le ventre"), ("het oog", "l'œil (meervoud: les yeux)")],
                  "Hoe zeg je dit in het Frans?", WW),
                 ("kort", "Vul aan: « J'ai mal ____ tête. »", "à la", W),
                 ("kort", "Vul aan: « J'ai mal ____ ventre. »", "au", W),
                 ("open", "Leg uit waarom er in de ene zin 'à la' en in de andere 'au' staat.",
                  "Au is à + le, voor een mannelijk woord: le ventre wordt au ventre. "
                  "À la blijft staan voor een vrouwelijk woord: la tête wordt à la tête.", 4),
                 ("open", "Je bent verkouden en gaat naar de dokter. Schrijf drie zinnen: wat je "
                          "hebt, sinds wanneer, en een vraag.",
                  "Bonjour docteur, je suis malade depuis trois jours. J'ai de la fièvre et mal "
                  "à la gorge. Pourriez-vous me donner quelque chose ?", 5),
                 ("rij", [("l'ordonnance", "het voorschrift"),
                          ("la pharmacie", "de apotheek"),
                          ("le médicament", "het geneesmiddel"),
                          ("prendre rendez-vous", "een afspraak maken"),
                          ("deux fois par jour", "twee keer per dag")],
                  "Wat betekent dit?", WL),
             ]),
        dict(kop="Instructietaal",
             opdracht="Wat moet je doen als dit op je examen staat?",
             oefeningen=[
                 ("rij", [("Complétez", "vul aan"), ("Cochez", "kruis aan"),
                          ("Soulignez", "onderstreep"), ("Reliez", "verbind"),
                          ("Choisissez", "kies"), ("Entourez", "omcirkel"),
                          ("Justifiez votre réponse", "verantwoord je antwoord"),
                          ("Répondez en néerlandais", "antwoord in het Nederlands")],
                  "Wat moet je doen?", WL),
                 ("open", "Boven een opgave staat « Vrai ou faux ? Justifiez avec un élément du "
                          "texte. » Wat verwacht men precies van jou?",
                  "Je schrijft of de stelling waar of fout is, én je haalt er een stuk uit de "
                  "tekst bij dat je antwoord bewijst. Alleen waar of fout is niet genoeg.", 4),
             ]),
    ],
)

# ============================================================
zet("woordvelden-eten-kleding-wonen-en-winkelen",
    titel="Woordvelden: eten, kleding, wonen en winkelen",
    reeksen=[
        dict(kop="Eten en drinken",
             opdracht="Schrijf het Franse woord met zijn lidwoord.",
             oefeningen=[
                 ("rij", [("het brood", "le pain"), ("het water", "l'eau"),
                          ("de melk", "le lait"), ("de kaas", "le fromage"),
                          ("het vlees", "la viande"), ("de vis", "le poisson"),
                          ("het ei", "l'œuf"), ("de appel", "la pomme"),
                          ("de aardappel", "la pomme de terre"), ("de soep", "la soupe")],
                  "Hoe zeg je dit in het Frans?", WW),
                 ("kort", "Vul aan: « Je voudrais ____ pain, s'il vous plaît. » (een beetje)",
                  "du", W),
                 ("kort", "Vul aan: « Je ne mange pas ____ viande. »", "de", W),
                 ("open", "Leg uit waarom er in de ene zin 'du' staat en in de andere 'de'.",
                  "Du is het partitieve lidwoord: een onbepaalde hoeveelheid brood. Na een "
                  "ontkenning wordt du, de la of des altijd de: je ne mange pas de viande.", 5),
             ]),
        dict(kop="Hoeveelheden",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("un kilo ____ pommes", "de"), ("une bouteille ____ eau", "d'"),
                          ("beaucoup ____ sucre", "de"), ("un peu ____ sel", "de"),
                          ("trois tranches ____ jambon", "de"), ("assez ____ lait", "de")],
                  "Vul het ontbrekende woord in.", W),
                 ("open", "Welke regel zit achter al die antwoorden?",
                  "Na een woord dat een hoeveelheid aangeeft, komt altijd de of d', zonder "
                  "lidwoord erachter.", 3),
                 ("waar", "Na 'beaucoup' zeg je in het Frans « beaucoup du sucre ».", False),
             ]),
        dict(kop="Winkelen en betalen",
             opdracht="Schrijf de zinnen in het Frans.",
             oefeningen=[
                 ("rij", [("Hoeveel kost het?", "Combien ça coûte ? / C'est combien ?"),
                          ("Ik zoek een cadeau.", "Je cherche un cadeau."),
                          ("Mag ik betalen met de kaart?", "Je peux payer par carte ?"),
                          ("Het is te duur.", "C'est trop cher."),
                          ("Hebt u dit in het zwart?", "Vous l'avez en noir ?"),
                          ("Ik neem het.", "Je le prends.")],
                  "Hoe zeg je dit?", WL),
                 ("rij", [("la boulangerie", "de bakker"), ("la boucherie", "de slager"),
                          ("la pharmacie", "de apotheek"),
                          ("le supermarché", "de supermarkt"),
                          ("la librairie", "de boekhandel"),
                          ("la caisse", "de kassa")],
                  "Waar ben je hier?", WW),
                 ("open", "Je wil brood en koeken kopen. Naar welke winkel ga je, en wat zeg je "
                          "als je binnenkomt?",
                  "Naar de boulangerie. Je zegt « Bonjour madame, je voudrais un pain et quatre "
                  "croissants, s'il vous plaît. »", 4),
                 ("kort", "Wat betekent 'la librairie'? Let op: het is geen bibliotheek.",
                  "de boekhandel", W),
             ]),
        dict(kop="Kleding en kleuren",
             opdracht="Vul aan of schrijf het Frans.",
             oefeningen=[
                 ("rij", [("de broek", "le pantalon"), ("het hemd", "la chemise"),
                          ("de schoenen", "les chaussures"), ("de jas", "le manteau"),
                          ("het kleed", "la robe"), ("de trui", "le pull")],
                  "Hoe zeg je dit in het Frans?", WW),
                 ("rij", [("rood", "rouge"), ("groen", "vert"), ("blauw", "bleu"),
                          ("zwart", "noir"), ("wit", "blanc"), ("geel", "jaune")],
                  "Welke kleur is dit?", W),
                 ("kort", "Vul aan: « une robe ____ » (wit)", "blanche", W),
                 ("kort", "Vul aan: « des chaussures ____ » (zwart)", "noires", W),
                 ("open", "Waarom verandert de kleur mee in die twee zinnen?",
                  "Een kleur is een bijvoeglijk naamwoord, en dat past zich aan het naamwoord "
                  "aan: la robe is vrouwelijk enkelvoud, les chaussures vrouwelijk meervoud.", 4),
             ]),
        dict(kop="Wonen en de dag",
             opdracht="Antwoord in het Frans.",
             oefeningen=[
                 ("rij", [("de keuken", "la cuisine"), ("de kamer", "la chambre"),
                          ("de badkamer", "la salle de bains"), ("de tuin", "le jardin"),
                          ("het appartement", "l'appartement"), ("de verdieping", "l'étage")],
                  "Hoe zeg je dit in het Frans?", WW),
                 ("open", "Beschrijf je woning in drie zinnen: wat voor woning, hoeveel kamers, "
                          "en wat je het liefst ziet.",
                  "J'habite dans une maison à Hasselt. Il y a trois chambres, une cuisine et un "
                  "petit jardin. J'aime surtout ma chambre, parce qu'elle est calme.", 5),
                 ("rij", [("se lever", "opstaan"), ("se laver", "zich wassen"),
                          ("prendre le petit déjeuner", "ontbijten"),
                          ("faire ses devoirs", "zijn huiswerk maken"),
                          ("se coucher", "gaan slapen"),
                          ("ranger sa chambre", "zijn kamer opruimen")],
                  "Wat betekent dit?", WL),
                 ("open", "Schrijf drie zinnen over je ochtend, met de uren erbij.",
                  "Je me lève à sept heures. Je prends le petit déjeuner à sept heures et "
                  "quart. Je pars à l'école à huit heures moins le quart.", 5),
             ]),
    ],
)

# ============================================================
zet("woordvelden-school-werk-en-de-professionele-wereld",
    titel="Woordvelden: school, werk en de professionele wereld",
    reeksen=[
        dict(kop="School",
             opdracht="Schrijf het Franse woord.",
             oefeningen=[
                 ("rij", [("de school", "l'école"), ("de leerling", "l'élève"),
                          ("de leraar", "le professeur"), ("het lokaal", "la classe"),
                          ("het vak", "la matière"), ("het uurrooster", "l'horaire"),
                          ("het rapport", "le bulletin"), ("het examen", "l'examen"),
                          ("het huiswerk", "les devoirs"), ("de vakantie", "les vacances")],
                  "Hoe zeg je dit in het Frans?", WW),
                 ("kort", "Hoe zeg je 'ik zit in het derde jaar'?",
                  "Je suis en troisième année.", WL),
                 ("open", "Een Franse leerling zegt: « Je suis en seconde. » Waarom kan je dat "
                          "niet gewoon als 'tweede jaar' lezen?",
                  "Het Franse systeem telt anders: la seconde is daar het eerste jaar van het "
                  "lycée. Je moet dus naar de leeftijd of de uitleg vragen, niet naar het "
                  "getal.", 4),
             ]),
        dict(kop="Beroepen",
             opdracht="Schrijf het beroep in het Frans, in de mannelijke en de vrouwelijke vorm "
                      "als die verschillen.",
             oefeningen=[
                 ("rij", [("verpleegkundige", "l'infirmier / l'infirmière"),
                          ("verkoper", "le vendeur / la vendeuse"),
                          ("bakker", "le boulanger / la boulangère"),
                          ("leraar", "le professeur / la professeure"),
                          ("kok", "le cuisinier / la cuisinière"),
                          ("kinesist", "le kinésithérapeute"),
                          ("boekhouder", "le comptable"),
                          ("elektricien", "l'électricien / l'électricienne")],
                  "Hoe heet dit beroep in het Frans?", WL),
                 ("kort", "Vul aan: « Ma mère est ____. » (verpleegkundige)", "infirmière", W),
                 ("open", "Waarom staat er in die zin geen lidwoord vóór het beroep?",
                  "Na être laat het Frans het lidwoord weg bij een beroep: elle est infirmière, "
                  "niet elle est une infirmière.", 4),
             ]),
        dict(kop="Stage en solliciteren",
             opdracht="Schrijf de zinnen in het Frans.",
             oefeningen=[
                 ("open", "Je schrijft een mail om naar een stageplaats te vragen. Schrijf de "
                          "eerste twee zinnen: wie je bent en wat je vraagt.",
                  "Madame, Monsieur, je m'appelle Lotte Peeters et je suis élève en troisième "
                  "année. J'aimerais faire un stage de deux semaines dans votre entreprise en "
                  "février.", 6),
                 ("rij", [("le stage", "de stage"), ("l'entreprise", "het bedrijf"),
                          ("le patron", "de baas"), ("le collègue", "de collega"),
                          ("le salaire", "het loon"), ("l'horaire de travail", "de werkuren"),
                          ("la candidature", "de sollicitatie"),
                          ("l'entretien", "het gesprek")],
                  "Wat betekent dit?", WW),
                 ("open", "Noem twee dingen die in een sollicitatiemail anders zijn dan in een "
                          "bericht aan een vriend.",
                  "Je gebruikt vous en een aanspreking met Madame, Monsieur, en je schrijft "
                  "hoffelijk met j'aimerais of pourriez-vous. Afkortingen en salut horen er "
                  "niet in.", 4),
                 ("kort", "Hoe sluit je een formele mail af?",
                  "Cordialement / Veuillez agréer mes salutations distinguées", WL),
             ]),
        dict(kop="Sport en vrije tijd",
             opdracht="Vul het juiste woord in.",
             oefeningen=[
                 ("rij", [("jouer ____ football", "au"), ("jouer ____ piano", "du"),
                          ("faire ____ natation", "de la"), ("faire ____ vélo", "du"),
                          ("jouer ____ guitare", "de la"), ("faire ____ athlétisme", "de l'")],
                  "Vul aan.", W),
                 ("open", "Leg de regel uit: wanneer jouer à, wanneer jouer de, en wanneer "
                          "faire de?",
                  "Jouer à bij een sport of een spel, jouer de bij een muziekinstrument, en "
                  "faire de bij een sport die je beoefent zonder tegenstander.", 5),
                 ("rij", [("le temps libre", "de vrije tijd"),
                          ("une série", "een reeks"),
                          ("un réseau social", "een sociaal netwerk"),
                          ("un ordinateur", "een computer"),
                          ("un mot de passe", "een wachtwoord"),
                          ("télécharger", "downloaden")],
                  "Wat betekent dit?", WW),
                 ("waar", "« Je joue du basket » is juist Frans.", False),
             ]),
    ],
)

# ============================================================
zet("woordvelden-tijd-weer-reizen-en-vervoer",
    titel="Woordvelden: tijd, weer, reizen en vervoer",
    reeksen=[
        dict(kop="Dagen, maanden en seizoenen",
             opdracht="Schrijf het Frans. Let op: dagen en maanden krijgen in het Frans geen "
                      "hoofdletter.",
             oefeningen=[
                 ("rij", [("maandag", "lundi"), ("woensdag", "mercredi"),
                          ("zaterdag", "samedi"), ("zondag", "dimanche"),
                          ("januari", "janvier"), ("juni", "juin"),
                          ("juli", "juillet"), ("september", "septembre")],
                  "Hoe zeg je dit in het Frans?", WW),
                 ("rij", [("de lente", "le printemps"), ("de zomer", "l'été"),
                          ("de herfst", "l'automne"), ("de winter", "l'hiver")],
                  "Welk seizoen is dit?", WW),
                 ("kort", "Vul aan: « Je suis né ____ mars. »", "en", W),
                 ("kort", "Vul aan: « Les cours commencent ____ 1er septembre. »", "le", W),
                 ("waar", "In het Frans schrijf je 'Lundi' en 'Mars' met een hoofdletter.",
                  False),
             ]),
        dict(kop="Het uur",
             opdracht="Schrijf het uur in woorden in het Frans.",
             oefeningen=[
                 ("rij", [("8.00", "huit heures"), ("8.15", "huit heures et quart"),
                          ("8.30", "huit heures et demie"),
                          ("8.45", "neuf heures moins le quart"),
                          ("12.00", "midi"), ("00.00", "minuit"),
                          ("14.20", "quatorze heures vingt / deux heures vingt"),
                          ("17.50", "six heures moins dix")],
                  "Hoe zeg je dit uur?", WL),
                 ("kort", "Hoe vraag je hoe laat het is?", "Quelle heure est-il ?", WL),
                 ("open", "Op een treinticket staat « départ 18h40 ». Hoe zeg je dat uur in een "
                          "gesprek, en hoe lees je het op een officieel bord?",
                  "In een gesprek: sept heures moins vingt. Op een bord of een ticket wordt het "
                  "voluit gelezen: dix-huit heures quarante.", 4),
             ]),
        dict(kop="Plaatsbepalingen",
             opdracht="Vul het juiste voorzetsel in.",
             oefeningen=[
                 ("rij", [("Le chat est ____ la table.", "sur"),
                          ("Le ballon est ____ la table.", "sous"),
                          ("La boulangerie est ____ de l'école.", "à côté"),
                          ("Le parc est ____ la gare et l'école.", "entre"),
                          ("Il attend ____ la gare.", "devant"),
                          ("Le jardin est ____ la maison.", "derrière"),
                          ("Les clés sont ____ le sac.", "dans")],
                  "Vul aan.", W),
                 ("open", "Beschrijf de weg van de school naar de bakker in drie zinnen, met "
                          "'tout droit', 'à gauche' en 'à droite'.",
                  "Vous allez tout droit jusqu'au feu. Puis vous tournez à gauche. La "
                  "boulangerie est à droite, à côté de la pharmacie.", 5),
             ]),
        dict(kop="Het weer",
             opdracht="Schrijf het Frans.",
             oefeningen=[
                 ("rij", [("het is mooi weer", "il fait beau"),
                          ("het is koud", "il fait froid"),
                          ("het regent", "il pleut"),
                          ("het sneeuwt", "il neige"),
                          ("het waait", "il y a du vent"),
                          ("het is 20 graden", "il fait vingt degrés"),
                          ("de zon schijnt", "le soleil brille")],
                  "Hoe zeg je dit?", WL),
                 ("open", "Drie van die uitdrukkingen beginnen met 'il fait' en twee met 'il'. "
                          "Wat is er bijzonder aan die 'il'?",
                  "Die il verwijst naar niemand: het is een onpersoonlijk werkwoord. Daarom "
                  "bestaat het alleen in die ene vorm, en zeg je nooit nous pleuvons.", 4),
                 ("kort", "Vul aan: « Demain, ____ va pleuvoir. »", "il", W),
             ]),
        dict(kop="Reizen en vervoer",
             opdracht="Vul aan of antwoord kort.",
             oefeningen=[
                 ("rij", [("de trein", "le train"), ("de bus", "le bus"),
                          ("de fiets", "le vélo"), ("de auto", "la voiture"),
                          ("het vliegtuig", "l'avion"), ("het station", "la gare"),
                          ("het perron", "le quai"), ("het ticket", "le billet")],
                  "Hoe zeg je dit in het Frans?", WW),
                 ("rij", [("Ik ga met de trein.", "Je vais en train."),
                          ("Ik ga te voet.", "Je vais à pied."),
                          ("Ik ga met de fiets.", "Je vais à vélo."),
                          ("Ik ga met de auto.", "Je vais en voiture.")],
                  "Hoe zeg je dit?", WL),
                 ("open", "Je staat aan het loket in Namen en wil een heen-en-terugticket naar "
                          "Brussel voor vandaag. Schrijf wat je zegt.",
                  "Bonjour madame, je voudrais un aller-retour pour Bruxelles, "
                  "s'il vous plaît. C'est pour aujourd'hui.", 4),
                 ("kort", "Wat betekent 'un aller simple'?", "een enkel ticket", W),
             ]),
        dict(kop="Landen en nationaliteiten",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("Ik woon in België.", "J'habite en Belgique."),
                          ("Ik ga naar Frankrijk.", "Je vais en France."),
                          ("Ik kom uit Portugal.", "Je viens du Portugal."),
                          ("Ik ga naar Canada.", "Je vais au Canada."),
                          ("Ik woon in Nederland.", "J'habite aux Pays-Bas.")],
                  "Hoe zeg je dit?", WL),
                 ("open", "Leg de regel uit: wanneer 'en', wanneer 'au' en wanneer 'aux' bij een "
                          "land?",
                  "En bij een vrouwelijk land (en Belgique, en France), au bij een mannelijk "
                  "land (au Canada, au Portugal) en aux bij een land in het meervoud "
                  "(aux Pays-Bas, aux États-Unis).", 5),
                 ("rij", [("belge", "Belgisch"), ("français", "Frans"),
                          ("néerlandais", "Nederlands"), ("allemand", "Duits"),
                          ("anglais", "Engels"), ("espagnol", "Spaans")],
                  "Wat betekent dit?", WW),
                 ("waar", "Een nationaliteit krijgt in het Frans altijd een hoofdletter.",
                  False),
             ]),
    ],
)

# ============================================================
zet("zelfstandige-naamwoorden-lidwoorden-en-determinanten",
    titel="Zelfstandige naamwoorden, lidwoorden en determinanten",
    reeksen=[
        dict(kop="Mannelijk of vrouwelijk",
             opdracht="Zet het juiste lidwoord (le, la of l') voor het woord.",
             oefeningen=[
                 ("rij", [("maison", "la"), ("livre", "le"), ("école", "l'"),
                          ("table", "la"), ("problème", "le"), ("liberté", "la"),
                          ("fromage", "le"), ("nation", "la")],
                  "Zet het juiste lidwoord ervoor.", W),
                 ("open", "Twee uitgangen in die lijst verraden het geslacht. Welke, en wat "
                          "verraden ze?",
                  "Woorden op -té (la liberté) en op -tion (la nation) zijn vrouwelijk. "
                  "Woorden op -age en -ème (le fromage, le problème) zijn mannelijk.", 4),
                 ("waar", "Een woord dat in het Nederlands 'de' heeft, is in het Frans altijd "
                          "vrouwelijk.", False),
             ]),
        dict(kop="Het meervoud",
             opdracht="Schrijf het meervoud.",
             oefeningen=[
                 ("rij", [("un livre", "des livres"), ("le cheval", "les chevaux"),
                          ("le journal", "les journaux"), ("un animal", "des animaux"),
                          ("le gâteau", "les gâteaux"), ("un bureau", "des bureaux"),
                          ("le bus", "les bus"), ("le prix", "les prix"),
                          ("l'œil", "les yeux")],
                  "Schrijf het meervoud.", WW),
                 ("open", "Drie van die woorden veranderen niet of helemaal. Welke, en waarom?",
                  "Le bus en le prix eindigen al op s of x, dus daar verandert niets. L'œil "
                  "wordt les yeux: dat is een helemaal ander woord, dat moet je kennen.", 4),
                 ("kort", "Hoor je het verschil tussen « le livre » en « les livres » in een "
                          "gesprek?", "ja, aan het lidwoord, niet aan het woord zelf", WL),
             ]),
        dict(kop="De vier soorten lidwoorden",
             opdracht="Vul aan en zeg welk soort lidwoord het is.",
             oefeningen=[
                 ("rij", [("Je vois ____ chien de mon voisin.", "le: bepaald"),
                          ("J'ai ____ chien.", "un: onbepaald"),
                          ("Je vais ____ cinéma.", "au: samengetrokken (à + le)"),
                          ("Je voudrais ____ eau.", "de l': partitief"),
                          ("Il parle ____ professeurs.", "des: samengetrokken (de + les)"),
                          ("Je mange ____ pain.", "du: partitief")],
                  "Vul aan en noem het soort.", WL),
                 ("open", "« du » kan twee dingen zijn. Geef van elk een voorbeeld.",
                  "Een partitief lidwoord: je mange du pain (een onbepaalde hoeveelheid brood). "
                  "Of de samentrekking van de + le: je parle du professeur.", 4),
                 ("kort", "Wat wordt « à + les »?", "aux", W),
                 ("kort", "Wat wordt « de + le »?", "du", W),
             ]),
        dict(kop="De na een hoeveelheid en na een ontkenning",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("un litre ____ lait", "de"), ("beaucoup ____ amis", "d'"),
                          ("Je n'ai pas ____ voiture.", "de"),
                          ("Il ne boit jamais ____ café.", "de"),
                          ("trop ____ sucre", "de"), ("Je n'ai plus ____ argent.", "d'")],
                  "Vul aan.", W),
                 ("open", "Schrijf « J'ai un vélo » in de ontkenning, en leg uit wat er met het "
                          "lidwoord gebeurt.",
                  "Je n'ai pas de vélo. Na een ontkenning wordt un, une, du, de la of des "
                  "vervangen door de.", 4),
                 ("waar", "Na « il n'y a pas » blijft « des » gewoon staan.", False),
             ]),
        dict(kop="Determinanten",
             opdracht="Vul de juiste vorm in.",
             oefeningen=[
                 ("rij", [("____ livre (dit)", "ce"), ("____ homme (deze)", "cet"),
                          ("____ maison (deze)", "cette"), ("____ enfants (deze)", "ces"),
                          ("____ frère (mijn)", "mon"), ("____ sœur (mijn)", "ma"),
                          ("____ parents (mijn)", "mes"), ("____ amie (mijn)", "mon")],
                  "Vul aan.", W),
                 ("open", "Waarom staat er « mon amie » en niet « ma amie », terwijl amie "
                          "vrouwelijk is?",
                  "Omdat amie met een klinker begint: ma amie zou lelijk klinken, dus gebruikt "
                  "het Frans mon. Hetzelfde gebeurt bij cet homme in plaats van ce homme.", 5),
                 ("rij", [("____ heure est-il ?", "Quelle"), ("____ livre préfères-tu ?", "Quel"),
                          ("____ matières aimes-tu ?", "Quelles"),
                          ("____ sont tes projets ?", "Quels")],
                  "Vul de juiste vorm van quel in.", W),
                 ("kort", "Vul aan: « ____ belle journée ! »", "Quelle", W),
             ]),
        dict(kop="Telwoorden",
             opdracht="Schrijf in woorden.",
             oefeningen=[
                 ("rij", [("15", "quinze"), ("21", "vingt et un"), ("70", "septante / soixante-dix"),
                          ("80", "quatre-vingts"), ("90", "nonante / quatre-vingt-dix"),
                          ("100", "cent"), ("1000", "mille"),
                          ("de derde", "le troisième"), ("de laatste", "le dernier")],
                  "Schrijf dit in woorden.", WW),
                 ("open", "Hoe zeg je 'de eerste' en 'de tweede' in het Frans, en wat valt er "
                          "op aan het eerste?",
                  "Le premier en le deuxième (of le second). Le premier is onregelmatig: het is "
                  "niet unième maar premier.", 4),
             ]),
    ],
)

# ============================================================
zet("voornaamwoorden-sujet-cod-coi-en-de-wederkerende",
    titel="Voornaamwoorden: sujet, COD, COI en de wederkerende",
    reeksen=[
        dict(kop="Het onderwerp",
             opdracht="Vul het juiste voornaamwoord in.",
             oefeningen=[
                 ("rij", [("____ suis belge.", "Je"), ("____ es fatigué ?", "Tu"),
                          ("____ pleut.", "Il"), ("____ allons au cinéma.", "Nous"),
                          ("____ êtes prêts ?", "Vous"), ("Marie et Léa ? ____ sont là.", "Elles")],
                  "Vul aan.", W),
                 ("open", "Wat betekent 'on' in « On va au cinéma » en in « En Belgique, on "
                          "parle trois langues »?",
                  "In de eerste zin betekent on 'wij', in spreektaal. In de tweede betekent het "
                  "'men'. In beide gevallen staat het werkwoord in de derde persoon "
                  "enkelvoud.", 5),
             ]),
        dict(kop="Het lijdend voorwerp (COD)",
             opdracht="Herschrijf de zin met een voornaamwoord in de plaats van het onderstreepte "
                      "deel.",
             oefeningen=[
                 ("rij", [("Je vois <u>le film</u>.", "Je le vois."),
                          ("Je vois <u>la maison</u>.", "Je la vois."),
                          ("Je vois <u>les enfants</u>.", "Je les vois."),
                          ("J'aime <u>Marie</u>.", "Je l'aime."),
                          ("Il achète <u>les billets</u>.", "Il les achète.")],
                  "Herschrijf met een voornaamwoord.", WL),
                 ("open", "Waar staat dat voornaamwoord in de Franse zin, en waar zou het in het "
                          "Nederlands staan?",
                  "In het Frans staat het vóór het werkwoord: je le vois. In het Nederlands "
                  "staat het erna: ik zie hem. Dat is het grootste verschil.", 4),
                 ("kort", "Vul aan: « Tu as le livre ? Oui, je ____ ai. »", "l'", W),
             ]),
        dict(kop="Het meewerkend voorwerp (COI)",
             opdracht="Vul aan met lui of leur.",
             oefeningen=[
                 ("rij", [("Je parle à Marie. → Je ____ parle.", "lui"),
                          ("Je parle à mes parents. → Je ____ parle.", "leur"),
                          ("Il téléphone à son frère. → Il ____ téléphone.", "lui"),
                          ("Elle écrit à ses amies. → Elle ____ écrit.", "leur"),
                          ("Je donne le livre à Paul. → Je ____ donne le livre.", "lui")],
                  "Vul aan.", W),
                 ("open", "Hoe weet je of je le, la, les moet nemen of lui, leur?",
                  "Je kijkt of er à voor het voorwerp staat. Zonder à is het een COD: le, la of "
                  "les. Met à is het een COI: lui of leur.", 5),
                 ("kort", "« Je lui parle. » Is 'lui' hier een man of een vrouw?",
                  "dat kan je niet zien: lui is voor beide", WL),
             ]),
        dict(kop="Wederkerende werkwoorden",
             opdracht="Vervoeg of vul aan.",
             oefeningen=[
                 ("rij", [("je ____ lève (se lever)", "me"), ("tu ____ laves", "te"),
                          ("il ____ appelle", "s'"), ("nous ____ levons", "nous"),
                          ("vous ____ couchez", "vous"), ("ils ____ amusent", "s'")],
                  "Vul het wederkerend voornaamwoord in.", W),
                 ("kort", "Schrijf « Hij staat op om zeven uur » in het Frans.",
                  "Il se lève à sept heures.", WL),
                 ("kort", "Schrijf diezelfde zin in de ontkenning.",
                  "Il ne se lève pas à sept heures.", WL),
                 ("open", "Waar staat het wederkerend voornaamwoord in een bevel, en wat "
                          "verandert er dan?",
                  "Achter het werkwoord, met een koppelteken, en te wordt toi: lève-toi ! "
                  "assieds-toi !", 4),
                 ("open", "Welk hulpwerkwoord nemen wederkerende werkwoorden in de passé "
                          "composé? Geef een voorbeeld.",
                  "Altijd être: je me suis levé, elle s'est lavée, nous nous sommes amusés.", 3),
             ]),
        dict(kop="Y en en",
             opdracht="Herschrijf of antwoord kort.",
             oefeningen=[
                 ("rij", [("Je vais à Paris. → J'____ vais.", "y"),
                          ("Il habite en Belgique. → Il ____ habite.", "y"),
                          ("Je mange des pommes. → J'____ mange.", "en"),
                          ("Elle a trois frères. → Elle ____ a trois.", "en")],
                  "Vul aan.", W),
                 ("open", "Waarvoor staat 'y' en waarvoor staat 'en'?",
                  "Y vervangt een plaats of iets met à: j'y vais. En vervangt iets met de of een "
                  "hoeveelheid: j'en mange, elle en a trois.", 4),
                 ("waar", "In « Il y a trois chaises » is 'y' een voornaamwoord dat naar een "
                          "plaats verwijst die eerder genoemd is.", False),
             ]),
    ],
)

# ============================================================
zet("bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen",
    titel="Bijvoeglijke naamwoorden, bijwoorden en de trappen",
    reeksen=[
        dict(kop="De vorm van het adjectief",
             opdracht="Zet het adjectief in de juiste vorm.",
             oefeningen=[
                 ("rij", [("une maison (petit)", "petite"), ("des livres (vert)", "verts"),
                          ("une fille (heureux)", "heureuse"), ("un homme (beau)", "beau"),
                          ("une robe (blanc)", "blanche"), ("des filles (sportif)", "sportives"),
                          ("une voiture (cher)", "chère"), ("des murs (blanc)", "blancs")],
                  "Schrijf de juiste vorm.", WW),
                 ("open", "Welke twee dingen bepalen de vorm van een Frans adjectief?",
                  "Het geslacht en het getal van het naamwoord waar het bij hoort: mannelijk of "
                  "vrouwelijk, enkelvoud of meervoud.", 3),
                 ("kort", "Schrijf het vrouwelijk meervoud van 'heureux'.", "heureuses", W),
             ]),
        dict(kop="De plaats van het adjectief",
             opdracht="Schrijf de hele groep op, met het adjectief op zijn juiste plaats.",
             oefeningen=[
                 ("rij", [("une maison + grand", "une grande maison"),
                          ("une voiture + rouge", "une voiture rouge"),
                          ("un garçon + jeune", "un jeune garçon"),
                          ("un livre + intéressant", "un livre intéressant"),
                          ("un homme + bon", "un bon homme"),
                          ("une table + ronde", "une table ronde")],
                  "Schrijf de groep juist op.", WL),
                 ("open", "Welke adjectieven staan vóór het naamwoord? Noem er vier.",
                  "Een kleine groep korte, veelgebruikte: grand, petit, bon, mauvais, jeune, "
                  "vieux, beau, joli. De meeste andere, zoals kleuren en nationaliteiten, staan "
                  "erachter.", 4),
                 ("waar", "In het Frans staat een adjectief altijd achter het naamwoord.",
                  False),
             ]),
        dict(kop="De trappen van vergelijking",
             opdracht="Schrijf de zin af.",
             oefeningen=[
                 ("rij", [("Paul est ____ grand ____ Marie. (groter dan)", "plus … que"),
                          ("Ce livre est ____ cher ____ l'autre. (minder duur dan)",
                           "moins … que"),
                          ("Elle est ____ grande ____ moi. (even groot als)", "aussi … que"),
                          ("C'est ____ film ____ intéressant. (de interessantste)",
                           "le … plus"),
                          ("C'est ____ maison ____ chère du quartier. (de duurste)",
                           "la … plus")],
                  "Vul aan.", WW),
                 ("kort", "Wat is de vergrotende trap van 'bon'?", "meilleur", W),
                 ("kort", "Wat is de overtreffende trap van 'bon'?", "le meilleur", W),
                 ("open", "Waarom kan je niet « plus bon » zeggen?",
                  "Bon heeft een eigen onregelmatige trap: meilleur. Net zoals wij 'goeder' niet "
                  "zeggen maar 'beter'.", 4),
                 ("kort", "Schrijf « Zij is de beste van de klas » in het Frans.",
                  "Elle est la meilleure de la classe.", WL),
             ]),
        dict(kop="Bijwoorden",
             opdracht="Maak het bijwoord of vul aan.",
             oefeningen=[
                 ("rij", [("lent", "lentement"), ("heureux", "heureusement"),
                          ("rapide", "rapidement"), ("vrai", "vraiment"),
                          ("doux", "doucement"), ("facile", "facilement")],
                  "Maak hier een bijwoord van.", WW),
                 ("open", "Leg uit hoe je van een adjectief een bijwoord maakt in het Frans.",
                  "Je neemt de vrouwelijke vorm van het adjectief en plakt er -ment aan: lent "
                  "wordt lente en dan lentement. Heureux wordt heureuse en dan "
                  "heureusement.", 5),
                 ("rij", [("toujours", "altijd"), ("souvent", "dikwijls"),
                          ("parfois", "soms"), ("rarement", "zelden"),
                          ("jamais", "nooit"), ("déjà", "al"),
                          ("encore", "nog"), ("bientôt", "binnenkort")],
                  "Wat betekent dit?", WW),
                 ("open", "Zet deze vier woorden van vaak naar zelden: parfois, toujours, "
                          "rarement, souvent.",
                  "toujours, souvent, parfois, rarement", 3),
                 ("kort", "Vul aan: « Il ne vient ____. » (nooit)", "jamais", W),
             ]),
        dict(kop="Voorzetsels",
             opdracht="Vul het juiste voorzetsel in.",
             oefeningen=[
                 ("rij", [("Je pense ____ toi.", "à"), ("Il a besoin ____ aide.", "d'"),
                          ("Elle habite ____ Namur.", "à"), ("C'est un cadeau ____ ma mère.",
                                                             "pour"),
                          ("Je travaille ____ lundi ____ vendredi.", "du … au"),
                          ("Il part ____ trois jours.", "dans")],
                  "Vul aan.", WW),
                 ("open", "Welk verschil is er tussen « dans trois jours » en « pendant trois "
                          "jours »?",
                  "Dans trois jours betekent 'binnen drie dagen', dus het begint pas over drie "
                  "dagen. Pendant trois jours betekent 'gedurende drie dagen', dus het duurt "
                  "drie dagen.", 4),
             ]),
    ],
)

# ============================================================
zet("present-imperatif-en-de-wederkerende-werkwoorden",
    titel="Présent, impératif en de wederkerende werkwoorden",
    reeksen=[
        dict(kop="Infinitief, persoonsvorm of deelwoord",
             opdracht="Schrijf bij elke vorm wat ze is, en waaraan je het ziet.",
             oefeningen=[
                 ("rij", [("parler", "infinitief"), ("vous parlez", "persoonsvorm"),
                          ("parlé", "voltooid deelwoord"), ("aller", "infinitief"),
                          ("il va", "persoonsvorm"), ("allé", "voltooid deelwoord")],
                  "Welke vorm is dit?", WW),
                 ("kort", "Vul aan: « Je vais ____ au cinéma. » (aller)", "aller", W),
                 ("kort", "Vul aan: « Je suis ____ au cinéma. » (aller, verleden)", "allé", W),
                 ("open", "Waarom staat er in de ene zin 'aller' en in de andere 'allé'?",
                  "Na je vais komt een infinitief, want je vais is zelf al de persoonsvorm. Na "
                  "je suis komt een voltooid deelwoord, want je suis is daar het "
                  "hulpwerkwoord.", 5),
             ]),
        dict(kop="De regelmatige présent",
             opdracht="Vervoeg.",
             oefeningen=[
                 ("rij", [("je (parler)", "parle"), ("nous (parler)", "parlons"),
                          ("ils (parler)", "parlent"), ("tu (finir)", "finis"),
                          ("nous (finir)", "finissons"), ("ils (finir)", "finissent"),
                          ("je (vendre)", "vends"), ("vous (vendre)", "vendez")],
                  "Vervoeg in de présent.", WW),
                 ("open", "Bij parler klinken vier vormen hetzelfde. Welke, en waarom is dat "
                          "lastig bij een schrijfopdracht?",
                  "Je parle, tu parles, il parle en ils parlent klinken gelijk. Bij schrijven "
                  "moet je dus nadenken welke uitgang erbij hoort; je hoort het niet.", 5),
             ]),
        dict(kop="De onregelmatige werkwoorden",
             opdracht="Vervoeg.",
             oefeningen=[
                 ("rij", [("je (être)", "suis"), ("vous (être)", "êtes"),
                          ("ils (avoir)", "ont"), ("nous (avoir)", "avons"),
                          ("je (aller)", "vais"), ("ils (aller)", "vont"),
                          ("vous (faire)", "faites"), ("ils (faire)", "font"),
                          ("je (pouvoir)", "peux"), ("nous (prendre)", "prenons"),
                          ("ils (venir)", "viennent"), ("je (devoir)", "dois")],
                  "Vervoeg in de présent.", WW),
                 ("open", "« Ils ont » en « ils sont » worden vaak verward. Schrijf van elk een "
                          "zin en zeg welk werkwoord het is.",
                  "Ils ont deux chiens: dat is avoir. Ils sont belges: dat is être.", 4),
                 ("kort", "Vul aan: « ____ quinze ans. » (ik ben vijftien)", "J'ai", W),
             ]),
        dict(kop="De impératif",
             opdracht="Schrijf het bevel.",
             oefeningen=[
                 ("rij", [("tegen tu: parler", "Parle !"), ("tegen vous: parler", "Parlez !"),
                          ("laten we gaan: aller", "Allons !"),
                          ("tegen tu: finir", "Finis !"),
                          ("tegen vous: être calme", "Soyez calme !"),
                          ("tegen tu: se lever", "Lève-toi !")],
                  "Schrijf het bevel.", WW),
                 ("open", "Waarom staat er « Parle ! » zonder s, terwijl je « tu parles » wel "
                          "met een s schrijft?",
                  "In de impératif verliest een werkwoord op -er zijn s in de tu-vorm. Bij finir "
                  "blijft die s wel staan: finis !", 4),
                 ("open", "Een recept zegt « Ajoutez le riz et laissez cuire dix minutes. » "
                          "Waarom staat daar geen 'vous'?",
                  "In de impératif valt het onderwerp weg: dat is het kenmerk van die vorm. "
                  "Daarom staat er ajoutez en niet vous ajoutez.", 4),
                 ("kort", "Schrijf « Bel me! » in het Frans.", "Appelle-moi !", W),
             ]),
        dict(kop="De infinitief na een ander werkwoord",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("J'aime ____ au foot. (jouer)", "jouer"),
                          ("Je dois ____ mes devoirs. (faire)", "faire"),
                          ("Tu peux ____ ? (venir)", "venir"),
                          ("Il faut ____ maintenant. (partir)", "partir"),
                          ("Nous allons ____ une pizza. (manger)", "manger")],
                  "Vul de juiste vorm in.", WW),
                 ("open", "Waarom is « Je veux je mange » fout, en hoe schrijf je het juist?",
                  "Na vouloir komt een infinitief, geen tweede persoonsvorm. Het is "
                  "je veux manger.", 4),
                 ("kort", "Vul aan: « Tu peux ____ aider ? » (mij)", "m'", W),
             ]),
        dict(kop="Onpersoonlijke werkwoorden",
             opdracht="Vul aan of antwoord kort.",
             oefeningen=[
                 ("rij", [("het regent", "il pleut"), ("het sneeuwt", "il neige"),
                          ("men moet", "il faut"), ("er is / er zijn", "il y a"),
                          ("het is mooi weer", "il fait beau")],
                  "Hoe zeg je dit?", WW),
                 ("kort", "Vul aan: « ____ trois chaises dans la classe. »", "Il y a", W),
                 ("open", "Waarom bestaat er geen vorm « nous pleuvons »?",
                  "Pleuvoir is onpersoonlijk: er is niemand die regent. Zulke werkwoorden "
                  "bestaan alleen in de derde persoon enkelvoud, met een il die naar niets "
                  "verwijst.", 4),
                 ("waar", "« Il y a » verandert in het meervoud in « ils y ont ».", False),
             ]),
    ],
)

# ============================================================
zet("passe-compose-imparfait-en-passe-recent",
    titel="Passé composé, imparfait en passé récent",
    reeksen=[
        dict(kop="Het voltooid deelwoord",
             opdracht="Schrijf het deelwoord.",
             oefeningen=[
                 ("rij", [("regarder", "regardé"), ("finir", "fini"),
                          ("vendre", "vendu"), ("faire", "fait"),
                          ("prendre", "pris"), ("voir", "vu"),
                          ("avoir", "eu"), ("être", "été"),
                          ("venir", "venu"), ("mettre", "mis")],
                  "Schrijf het voltooid deelwoord.", WW),
                 ("kort", "Welke uitgang krijgt een werkwoord op -er?", "-é", W),
             ]),
        dict(kop="Avoir of être",
             opdracht="Vul het juiste hulpwerkwoord in de juiste vorm in.",
             oefeningen=[
                 ("rij", [("Je ____ mangé une pomme.", "ai"),
                          ("Il ____ parti à six heures.", "est"),
                          ("Nous ____ fait nos devoirs.", "avons"),
                          ("Elles ____ arrivées hier.", "sont"),
                          ("Vous ____ pris le train ?", "avez"),
                          ("Je ____ levé à sept heures. (se lever)", "me suis"),
                          ("Ils ____ restés à la maison.", "sont"),
                          ("Tu ____ vu le film ?", "as")],
                  "Vul aan.", WW),
                 ("open", "Welke werkwoorden nemen être? Noem er vijf, en noem ook de groep die "
                          "er altijd bij hoort.",
                  "Werkwoorden van komen, gaan en blijven: aller, venir, partir, sortir, "
                  "arriver, rester, tomber, naître, mourir. En altijd alle wederkerende "
                  "werkwoorden.", 5),
             ]),
        dict(kop="De overeenkomst van het deelwoord",
             opdracht="Vul het deelwoord in de juiste vorm in.",
             oefeningen=[
                 ("rij", [("Elle est ____ . (partir)", "partie"),
                          ("Ils sont ____ . (arriver)", "arrivés"),
                          ("Elles sont ____ . (sortir)", "sorties"),
                          ("Elle a ____ une pomme. (manger)", "mangé"),
                          ("Ils ont ____ le train. (prendre)", "pris"),
                          ("Nous sommes ____ à la maison. (rester)", "restés")],
                  "Vul aan.", WW),
                 ("open", "Leg de regel uit die achter die zes antwoorden zit.",
                  "Met être past het deelwoord zich aan het onderwerp aan in geslacht en getal. "
                  "Met avoir blijft het deelwoord onveranderd.", 5),
                 ("waar", "« Nous avons mangés une pizza » is juist geschreven.", False),
             ]),
        dict(kop="De imparfait",
             opdracht="Vervoeg in de imparfait.",
             oefeningen=[
                 ("rij", [("je (parler)", "parlais"), ("nous (faire)", "faisions"),
                          ("il (être)", "était"), ("ils (avoir)", "avaient"),
                          ("tu (prendre)", "prenais"), ("vous (habiter)", "habitiez"),
                          ("elle (aller)", "allait"), ("nous (finir)", "finissions")],
                  "Vervoeg in de imparfait.", WW),
                 ("open", "Hoe maak je de imparfait? Leg het uit met 'faire' als voorbeeld.",
                  "Je neemt de stam van de nous-vorm van de présent en zet er de uitgangen -ais, "
                  "-ais, -ait, -ions, -iez, -aient achter. Nous faisons geeft fais-, dus je "
                  "faisais.", 5),
                 ("kort", "Welk werkwoord heeft een eigen stam in de imparfait?",
                  "être: j'étais", W),
             ]),
        dict(kop="Welke verleden tijd?",
             opdracht="Vul in de passé composé of in de imparfait, en schrijf erbij waarom.",
             oefeningen=[
                 ("rij", [("Hier, je ____ au cinéma. (aller)",
                           "suis allé: één keer, afgelopen"),
                          ("Quand j'étais petit, j'____ souvent chez ma grand-mère. (aller)",
                           "allais: een gewoonte"),
                          ("Il ____ froid et le ciel ____ gris. (faire, être)",
                           "faisait, était: de achtergrond"),
                          ("Soudain, le téléphone ____ . (sonner)",
                           "a sonné: één gebeurtenis"),
                          ("Je ____ quand il ____ . (dormir, arriver)",
                           "dormais, est arrivé: bezig, en dan de gebeurtenis")],
                  "Vul aan en zeg waarom.", WL),
                 ("open", "Je schrijft een verslag over je stage. Wat zet je in de imparfait en "
                          "wat in de passé composé?",
                  "Wat elke dag hetzelfde was, komt in de imparfait: je commençais à huit "
                  "heures. Wat op één bepaalde dag gebeurde, komt in de passé composé: le "
                  "premier jour, le patron m'a montré l'atelier.", 5),
             ]),
        dict(kop="De passé récent",
             opdracht="Schrijf of vul aan.",
             oefeningen=[
                 ("rij", [("Ik heb net gegeten.", "Je viens de manger."),
                          ("Ze is net aangekomen.", "Elle vient d'arriver."),
                          ("We zijn net vertrokken.", "Nous venons de partir."),
                          ("Hij heeft net gebeld.", "Il vient de téléphoner.")],
                  "Schrijf dit in het Frans.", WL),
                 ("open", "Wat is het verschil tussen « je viens de manger » en « je vais "
                          "manger »?",
                  "Je viens de manger betekent dat je net gegeten hebt, dus het is voorbij. "
                  "Je vais manger betekent dat je gaat eten, dus het komt nog.", 4),
                 ("kort", "Vul aan: « Elle ____ de partir. »", "vient", W),
                 ("waar", "In « je viens de manger » wordt ook 'manger' vervoegd.", False),
             ]),
    ],
)

# ============================================================
zet("futur-proche-futur-simple-en-de-conditionnel-de-politesse",
    titel="Futur proche, futur simple en de conditionnel de politesse",
    reeksen=[
        dict(kop="De futur proche",
             opdracht="Schrijf de zin in de futur proche.",
             oefeningen=[
                 ("rij", [("Je mange.", "Je vais manger."),
                          ("Tu pars.", "Tu vas partir."),
                          ("Il pleut.", "Il va pleuvoir."),
                          ("Nous voyons le film.", "Nous allons voir le film."),
                          ("Ils arrivent.", "Ils vont arriver."),
                          ("Elle se lève tôt.", "Elle va se lever tôt.")],
                  "Zet dit in de futur proche.", WL),
                 ("open", "Welk van de twee werkwoorden vervoeg je in een futur proche, en welk "
                          "niet?",
                  "Alleen aller wordt vervoegd; het tweede werkwoord blijft in de infinitief "
                  "staan.", 3),
                 ("kort", "Schrijf « Je ga niet eten » in het Frans.",
                  "Je ne vais pas manger.", WL),
             ]),
        dict(kop="De futur simple",
             opdracht="Vervoeg in de futur simple.",
             oefeningen=[
                 ("rij", [("je (parler)", "parlerai"), ("tu (finir)", "finiras"),
                          ("il (prendre)", "prendra"), ("nous (habiter)", "habiterons"),
                          ("vous (choisir)", "choisirez"), ("ils (travailler)", "travailleront")],
                  "Vervoeg in de futur simple.", WW),
                 ("open", "Hoe maak je de futur simple van een werkwoord op -re? Geef een "
                          "voorbeeld.",
                  "Je neemt de infinitief, laat de laatste e vallen en plakt de uitgangen erop: "
                  "prendre wordt prendr- en dan je prendrai.", 4),
                 ("kort", "Welke letter staat altijd vóór de uitgang van een futur simple?",
                  "een r", W),
             ]),
        dict(kop="De onregelmatige stammen",
             opdracht="Vervoeg in de futur simple.",
             oefeningen=[
                 ("rij", [("je (être)", "serai"), ("j' (avoir)", "aurai"),
                          ("j' (aller)", "irai"), ("je (faire)", "ferai"),
                          ("je (pouvoir)", "pourrai"), ("je (vouloir)", "voudrai"),
                          ("je (venir)", "viendrai"), ("je (voir)", "verrai"),
                          ("je (devoir)", "devrai")],
                  "Vervoeg in de futur simple.", WW),
                 ("kort", "Vul aan: « Demain, nous ____ à Bruxelles. » (aller)", "irons", W),
                 ("open", "Welke twee vormen van 'aller' kijken vooruit, en hoe verschillen ze?",
                  "J'irai is de futur simple, één woord, eerder schrijftaal. Je vais aller is de "
                  "futur proche, twee woorden, eerder spreektaal. Beide betekenen dat je zal "
                  "gaan.", 5),
             ]),
        dict(kop="Welke tijd?",
             opdracht="Vul de juiste tijd in. Het woord van tijd zegt je wat er moet staan.",
             oefeningen=[
                 ("rij", [("Hier, je ____ au cinéma. (aller)", "suis allé"),
                          ("Demain, je ____ au cinéma. (aller)", "vais aller / irai"),
                          ("Maintenant, je ____ mes devoirs. (faire)", "fais"),
                          ("La semaine prochaine, nous ____ un test. (avoir)",
                           "aurons / allons avoir"),
                          ("Quand j'étais petit, je ____ au foot. (jouer)", "jouais"),
                          ("Je ____ de rentrer. (venir, net)", "viens")],
                  "Vul de juiste tijd in.", WL),
                 ("open", "Welke twee woorden in die rij kijken vooruit, en welke twee kijken "
                          "terug?",
                  "Demain en la semaine prochaine kijken vooruit. Hier en quand j'étais petit "
                  "kijken terug. Maintenant blijft in het nu.", 4),
             ]),
        dict(kop="De conditionnel de politesse",
             opdracht="Herschrijf hoffelijk, of vul aan.",
             oefeningen=[
                 ("rij", [("Je veux un café.", "Je voudrais un café."),
                          ("Aidez-moi.", "Pourriez-vous m'aider ?"),
                          ("Je veux travailler ici.", "J'aimerais travailler ici."),
                          ("Viens à six heures.", "Pourrais-tu venir à six heures ?"),
                          ("Donnez-moi l'addition.",
                           "Pourriez-vous m'apporter l'addition ?")],
                  "Schrijf dit hoffelijker.", WL),
                 ("rij", [("j'aurai", "ik zal hebben"), ("j'aurais", "ik zou hebben"),
                          ("je serai", "ik zal zijn"), ("je serais", "ik zou zijn"),
                          ("je pourrai", "ik zal kunnen"), ("je pourrais", "ik zou kunnen")],
                  "Wat betekent dit?", WW),
                 ("open", "Eén letter maakt het verschil tussen die paren. Welke, en waarom is "
                          "dat op een schrijfopdracht belangrijk?",
                  "De s aan het eind. Zonder s is het de toekomst, met s de hoffelijke of "
                  "voorwaardelijke vorm. Je hoort het niet, dus bij schrijven moet je weten wat "
                  "je bedoelt.", 5),
                 ("open", "Schrijf twee zinnen van een mail aan een hotel: je zou een kamer "
                          "willen, en je vraagt hoffelijk of ze je de prijs kunnen doorgeven.",
                  "Madame, Monsieur, j'aimerais réserver une chambre pour deux nuits. "
                  "Pourriez-vous me donner le prix ?", 5),
             ]),
    ],
)

# ============================================================
zet("zinsbouw-zinsdelen-voegwoorden-en-de-overeenkomst",
    titel="Zinsbouw, zinsdelen, voegwoorden en de overeenkomst",
    reeksen=[
        dict(kop="De zinssoort",
             opdracht="Schrijf welke zinssoort dit is.",
             oefeningen=[
                 ("rij", [("Il travaille à Bruxelles.", "mededelend"),
                          ("Où habites-tu ?", "vragend"),
                          ("Ferme la porte !", "bevelend"),
                          ("Quel beau jardin !", "uitroepend"),
                          ("Il ne vient pas.", "ontkennend"),
                          ("J'aimerais partir plus tôt.", "wensend")],
                  "Welke zinssoort is dit?", WW),
                 ("kort", "Schrijf « Demain ik ga naar Brussel » juist in het Frans.",
                  "Demain je vais à Bruxelles.", WL),
                 ("open", "Een Nederlandstalige schrijft « Demain vais je à Bruxelles. » "
                          "Waarom is dat fout?",
                  "In het Nederlands komt er na een woord vooraan een omkering, in het Frans "
                  "niet: de volgorde blijft onderwerp, persoonsvorm, rest.", 4),
             ]),
        dict(kop="Een vraag stellen",
             opdracht="Schrijf de vraag op de gevraagde manier.",
             oefeningen=[
                 ("rij", [("Tu viens ? → met est-ce que", "Est-ce que tu viens ?"),
                          ("Tu viens ? → met omkering", "Viens-tu ?"),
                          ("Il travaille ici. → vraag met omkering",
                           "Travaille-t-il ici ?"),
                          ("Elle a un vélo. → vraag met omkering", "A-t-elle un vélo ?")],
                  "Schrijf de vraag.", WL),
                 ("open", "Waarom staat er « travaille-t-il » en niet « travaille-il »?",
                  "Er komt een -t- tussen om twee klinkers te scheiden. Dat gebeurt bij il, elle "
                  "en on na een werkwoord dat op een klinker eindigt.", 4),
                 ("rij", [("wie", "qui"), ("wat", "que / qu'est-ce que"),
                          ("waar", "où"), ("wanneer", "quand"),
                          ("hoe", "comment"), ("waarom", "pourquoi"),
                          ("hoeveel", "combien")],
                  "Hoe zeg je dit vraagwoord in het Frans?", WW),
             ]),
        dict(kop="De ontkenning",
             opdracht="Schrijf de zin ontkennend.",
             oefeningen=[
                 ("rij", [("Je comprends.", "Je ne comprends pas."),
                          ("Il vient. (nooit)", "Il ne vient jamais."),
                          ("Elle fume. (niet meer)", "Elle ne fume plus."),
                          ("Je vois quelque chose. (niets)", "Je ne vois rien."),
                          ("J'ai mangé.", "Je n'ai pas mangé."),
                          ("Je vais partir.", "Je ne vais pas partir."),
                          ("J'ai une voiture.", "Je n'ai pas de voiture.")],
                  "Schrijf dit ontkennend.", WL),
                 ("open", "Waar staat de ontkenning in een passé composé, en waarom daar?",
                  "Rond het hulpwerkwoord: je n'ai pas mangé. Het hulpwerkwoord is de "
                  "persoonsvorm, en de ontkenning gaat altijd rond de persoonsvorm.", 4),
                 ("open", "Wat gebeurt er met het lidwoord na een ontkenning? Geef een "
                          "voorbeeld.",
                  "Un, une, du, de la en des worden de: j'ai un vélo wordt je n'ai pas de "
                  "vélo.", 4),
             ]),
        dict(kop="Enkelvoudig of samengesteld",
             opdracht="Tel de persoonsvormen en schrijf 'enkelvoudig' of 'samengesteld'.",
             oefeningen=[
                 ("rij", [("Il travaille à Bruxelles.", "enkelvoudig: 1 persoonsvorm"),
                          ("Il travaille à Bruxelles parce qu'il aime la ville.",
                           "samengesteld: 2 persoonsvormen"),
                          ("Je veux partir.", "enkelvoudig: 1 persoonsvorm + infinitief"),
                          ("Quand il pleut, je prends le bus.", "samengesteld"),
                          ("Je vais manger et puis je vais dormir.", "samengesteld")],
                  "Enkelvoudig of samengesteld?", WL),
                 ("open", "Waarom is « Je veux partir » maar één zin, terwijl er twee "
                          "werkwoorden in staan?",
                  "Je telt de persoonsvormen, niet de werkwoorden. Veux is de enige "
                  "persoonsvorm; partir is een infinitief.", 4),
             ]),
        dict(kop="Voegwoorden",
             opdracht="Vul aan of antwoord kort.",
             oefeningen=[
                 ("rij", [("et", "en"), ("mais", "maar"), ("ou", "of"),
                          ("donc", "dus"), ("car", "want"),
                          ("parce que", "omdat"), ("quand", "wanneer"),
                          ("si", "als"), ("pendant que", "terwijl")],
                  "Wat betekent dit?", WW),
                 ("kort", "Vul aan: « Je reste à la maison ____ il pleut. » (omdat)",
                  "parce qu'", W),
                 ("open", "Verbind deze twee zinnen met een voegwoord dat een tegenstelling "
                          "aangeeft: « Le vélo est pratique. Il est cher. »",
                  "Le vélo est pratique, mais il est cher.", 2),
                 ("open", "Car en parce que betekenen bijna hetzelfde. Wat is het verschil in "
                          "soort?",
                  "Car is nevenschikkend: het verbindt twee gelijkwaardige zinnen. Parce que is "
                  "onderschikkend: het maakt van de tweede zin een bijzin.", 4),
             ]),
        dict(kop="De zinsdelen",
             opdracht="Benoem de onderstreepte delen.",
             oefeningen=[
                 ("rij", [("<u>Marie</u> donne un livre à Paul.", "sujet"),
                          ("Marie <u>donne</u> un livre à Paul.", "verbe conjugué"),
                          ("Marie donne <u>un livre</u> à Paul.", "COD"),
                          ("Marie donne un livre <u>à Paul</u>.", "COI"),
                          ("<u>Les élèves de ma classe</u> travaillent bien.", "sujet")],
                  "Welk zinsdeel is dit?", WW),
                 ("open", "Met welke vraag vind je het COD, en met welke het COI?",
                  "Het COD vind je met qui ? of quoi ? na het werkwoord, zonder voorzetsel. Het "
                  "COI vind je met à qui ?", 4),
                 ("open", "Waarom heb je dat onderscheid nodig als je een voornaamwoord wil "
                          "gebruiken?",
                  "Omdat een COD le, la of les wordt en een COI lui of leur. Zonder het "
                  "onderscheid kies je het verkeerde voornaamwoord.", 4),
             ]),
        dict(kop="De overeenkomst",
             opdracht="In elke zin staat één fout. Schrijf de zin juist op.",
             oefeningen=[
                 ("kort", "Les enfants joue dans le jardin.",
                  "Les enfants jouent dans le jardin.", WL),
                 ("kort", "Les élèves de ma classe travaille bien.",
                  "Les élèves de ma classe travaillent bien.", WL),
                 ("kort", "Marie et Paul est parti.", "Marie et Paul sont partis.", WL),
                 ("kort", "Elle est parti à six heures.", "Elle est partie à six heures.", WL),
                 ("kort", "Des maisons vert.", "Des maisons vertes.", WL),
                 ("kort", "Nous avons mangés une pizza.", "Nous avons mangé une pizza.", WL),
                 ("open", "Noem de drie soorten overeenkomst die je in het Frans moet nakijken.",
                  "De persoonsvorm met het onderwerp, het bijvoeglijk naamwoord met zijn "
                  "naamwoord, en bij être het voltooid deelwoord met het onderwerp.", 4),
                 ("open", "Waarom is die overeenkomst vooral bij schrijven belangrijk?",
                  "Omdat je ze meestal niet hoort: il joue en ils jouent klinken gelijk, net als "
                  "une maison verte en des maisons vertes. Alleen in het schrift zie je het.", 5),
             ]),
    ],
)


if __name__ == "__main__":
    for naam, b in OEFENBUNDELS.items():
        oefenbundel.schrijf(b, naam)
        print("  ", naam)

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-een-franse-tekst-begrijpen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Lees de tekst eerst één keer helemaal door zonder te stoppen bij woorden die je niet kent. Je zoekt in die eerste ronde alleen waarover het gaat. Pas daarna ga je op zoek naar de antwoorden.",
            waarom=[],
        ),
        dict(
            aanpak="Het onderwerp is waarover de tekst gaat, in een paar woorden. De hoofdgedachte is wat de tekst daarover zegt, in één volle zin. De getallen vind je door de tekst af te scannen op cijfers en getalwoorden.",
            waarom=[
                "Het onderwerp is geen zin maar een groepje woorden: een schooltuin op een dak. Zet er geen werkwoord bij, dan maak je er de hoofdgedachte van.",
                "De hoofdgedachte moet twee dingen bevatten: wat er gebeurd is (het lege dak werd een tuin die de keuken bevoorraadt) en waar het naartoe gaat (volgend jaar uitbreiden). Eén van de twee is niet genoeg.",
                "Quatre-vingts is tachtig: vier keer twintig. Mètres carrés zijn vierkante meter.",
                "Le mardi après-midi. Let op het lidwoord le voor een dag: dat betekent elke dinsdag, niet die ene dinsdag.",
                "Quinze is vijftien. Het staat in de zin « quinze élèves y travaillent chaque semaine ».",
            ],
        ),
        dict(
            aanpak="Bij deze vragen staat het antwoord letterlijk in de tekst, maar niet altijd in één zin. Zoek eerst het stukje tekst waar het over gaat en lees dan de twee zinnen eromheen mee.",
            waarom=[
                "Tomates en courgettes lijken genoeg op het Nederlands. Herbes zijn kruiden, geen gras.",
                "Er staan twee dingen in dezelfde zin: de soep van de kokkin en de tomaten in de sandwiches. De vraag naar twee dingen is een teken dat je in de tekst twee keer moet kijken.",
                "Het voorbehoud zit achter cependant, dat nochtans betekent. Zo'n signaalwoord is bijna altijd de plaats waar een tekst zijn eigen goed nieuws bijstelt. Un repas sur dix is één maaltijd op tien.",
                "Beide plannen staan in de laatste alinea: des fraises ajouter (aardbeien erbij) en vendre au marché du samedi (verkopen op de zaterdagmarkt).",
                "In de tekst staat het omgekeerde: « Au début, personne ne croyait au projet » betekent dat in het begin niemand erin geloofde.",
            ],
        ),
        dict(
            aanpak="Een woord raden uit zijn omgeving werkt beter dan je denkt. Kijk wat er vóór en na staat, en wat er in die zin logisch kan staan. Een verwijswoord zoek je altijd in de zin ervóór.",
            waarom=[
                "Le potager herken je aan les légumes in dezelfde alinea. Le toit staat in de titel en dus in heel de tekst. Cependant en environ zijn twee woorden die je in élke tekst terugziet: nochtans en ongeveer. Leer die twee echt vanbuiten.",
                "L'argent is het geld dat ze nog niet hebben: de opbrengst van de legumes op de markt. Het lidwoord l' betekent hier het geld dat we net genoemd hebben, niet geld in het algemeen.",
            ],
        ),
        dict(
            aanpak="Een uurrooster of een tarievenlijst lees je niet van begin tot eind. Je zoekt gericht: eerst de rij of de regel die over jouw vraag gaat, dan pas het getal.",
            waarom=[],
        ),
        dict(
            aanpak="Let bij dit soort tekst op de kleine lettertjes onderaan: daar staan de uitzonderingen, en net daarop gaan de vragen. En let op leeftijdsgrenzen: min twaalf jaar betekent tot en met elf.",
            waarom=[
                "Fermé betekent gesloten. Nettoyage is de poetsbeurt, en dat is de reden, geen tweede dag.",
                "Het tarief enfants geldt voor −12 ans, dus een kind van tien valt daaronder.",
                "Woensdag staat er 13h–19h: één blok, geen ochtenduur. Op dinsdag en donderdag zijn er wel twee blokken.",
                "De val zit in het kind van veertien. De tarievenlijst zegt enfants (−12 ans), dus veertien jaar betaalt het volle tarief van 5,50 euro. Er bestaat wel een tarief étudiants van 4 euro, maar in de tekst staat niet dat een scholier van veertien daaronder valt, dus reken met 5,50.",
                "Allebei staan onderaan in de kleine lettertjes: le bonnet de bain est obligatoire, en les enfants de moins de huit ans doivent être accompagnés. Zes jaar is minder dan acht, dus die moet begeleid worden.",
                "De laatste zin zegt juist het omgekeerde: pendant les vacances scolaires, la piscine ouvre aussi le lundi de 13h à 18h.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-tekstsoorten-tekstverbanden-en-leesstrategieen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Lees de zes teksten eerst gewoon door. Je hoeft niet elk woord te kennen om te zien wat voor soort tekst het is: de vorm en de werkwoorden verraden het al.",
            waarom=[],
        ),
        dict(
            aanpak="Vraag je bij elke tekst af wat hij met jou wil doen. Je iets laten doen is prescriptief. Je iets laten weten is informatief. Je iets laten kopen is persuasief. Je iets laten vinden is opiniërend. Je iets laten meemaken is narratief. Je iets laten voelen met beeldspraak is literair.",
            waarom=[
                "De werkwoordsvorm is je beste aanwijzing. Een impératif (mélangez, ajoutez) betekent prescriptief of persuasief. Cijfers zonder mening betekenen informatief. À mon avis en je trouve betekenen opiniërend. Een tijdsbepaling in het verleden (samedi dernier) betekent narratief. Een vergelijking met comme betekent literair.",
                "Het verschil zit in wat ze van je willen. Persuasief wil een handeling van jou: kopen, inschrijven, bellen. Opiniërend wil alleen dat je het met de schrijver eens wordt.",
                "De impératif staat in tekst 1 en tekst 3. Zie je het verschil met tekst 4? Daar staat il faudrait, een conditionnel: dat is geen bevel maar een mening over wat zou moeten.",
            ],
        ),
        dict(
            aanpak="Een feit kan je nakijken: iemand kan het meten, tellen of opzoeken. Een mening is wat iemand erover vindt. Zoek naar de kleine woordjes die een mening aankondigen: à mon avis, je trouve, d'après, il faudrait.",
            waarom=[
                "Let op de derde: selon une étude récente verwijst naar een bron, en dat maakt het een feit dat je kan nakijken. Maar d'après l'auteur verwijst naar een persoon en zijn mening. Hetzelfde soort bouw, een ander soort inhoud.",
                "Een cijfer kan ook in een mening staan: « Ce film de deux heures est beaucoup trop long » bevat een cijfer en blijft een mening. Het cijfer alleen zegt niets.",
            ],
        ),
        dict(
            aanpak="Signaalwoorden zijn de wegwijzers van een tekst: ze zeggen wat er na de komma komt. Leer ze in paren: mais en cependant doen hetzelfde, parce que geeft de reden en donc het gevolg.",
            waarom=[
                "Parce que en donc worden vaak verwisseld. Parce que staat vóór de oorzaak, donc vóór het gevolg. « Je reste à la maison parce qu'il pleut » tegenover « Il pleut, donc je reste à la maison »: dezelfde inhoud, omgekeerde volgorde.",
                "De regen is de oorzaak en thuisblijven het gevolg, dus je hebt een gevolgwoord nodig: donc. Parce que zou het omdraaien en dan klopt de zin niet meer.",
                "Cependant staat altijd aan het begin van een nieuwe zin, mais verbindt twee zinnen tot één. Daarom verdwijnt het punt en komt er een komma voor mais.",
            ],
        ),
        dict(
            aanpak="Een verwijswoord zoek je altijd in wat ervoor staat. Let op het geslacht en het getal: il of elle, le of la, lui of leur. Die vorm zegt je naar welk woord je terug moet.",
            waarom=[
                "Un chien is enkelvoud en mannelijk, dus il kan niet naar mes voisins verwijzen: dat zou ils zijn met een s.",
                "Elle is enkelvoud vrouwelijk, dus Marie. Leur is meervoud en betekent aan hen, dus de ouders.",
                "De e van déposée is de aanwijzing: het deelwoord komt overeen met une lettre, dat vrouwelijk is. Was het de directeur, dan stond er déposé zonder e.",
                "De tweede zin gaat over la plus jeune, de jongste van de twee, dus over één zus.",
            ],
        ),
        dict(
            aanpak="Een leesstrategie is een keuze die je maakt vóór je begint. Vraag je telkens af: wat moet ik precies weten? Daarna kies je hoe je leest.",
            waarom=[
                "Dit heet voorspellen, en het werkt omdat je hersenen woorden sneller herkennen als ze ze verwachten. Twintig seconden naar de titel en de foto kijken, levert bij een Franse tekst meer op dan twintig seconden woordjes opzoeken.",
                "Gericht zoeken naar één gegeven heet scannen. De hele tekst doorlezen (skimmen) doe je als je de hoofdgedachte moet vinden. Op het examen kies je bij elke vraag opnieuw welk van de twee je nodig hebt.",
                "Je begrijpt een tekst vaak al met zeventig of tachtig procent van de woorden. Onbekende woorden overslaan en verder lezen is een vaardigheid, geen zwakte.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-de-franstalige-wereld-omgangsvormen-en-gewoontes-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elke situatie twee dingen af: hoe laat is het, en wie staat er voor je? Het uur beslist tussen bonjour en bonsoir, de persoon beslist tussen salut en bonjour madame.",
            waarom=[
                "Bonsoir begint ongeveer bij het donker worden, zowat vanaf zes uur. Bonne nuit zeg je niet bij aankomst maar alleen als iemand gaat slapen.",
                "Dit is een echt verschil met het Nederlands, waar een los dag of hallo volstaat. In het Frans hoort de aanspreking erbij.",
                "Salut is voor vrienden en leeftijdsgenoten. Tegen de directeur zeg je bonjour monsieur. Dit is geen regel van de grammatica maar van het register, en net daarop let een examinator.",
            ],
        ),
        dict(
            aanpak="Tu gebruik je bij iemand die je kent en die naast je staat: een vriend, een klasgenoot, een kind, familie. Vous gebruik je bij iemand die je niet kent of die boven je staat, en altijd bij meer dan één persoon.",
            waarom=[
                "Let op de vijfde: twee vrienden samen worden ook vous. Dat is dan geen hoffelijkheid maar gewoon het meervoud. Vandaar dat vous twee heel verschillende dingen kan betekenen.",
                "Het is handig om bij vous even stil te staan bij welk van de twee je bedoelt, want je werkwoord verandert er niet van, maar je toon wel.",
                "Tutoyer komt van tu. Het andere werkwoord bestaat ook: vouvoyer, iemand met vous aanspreken.",
                "Dit is een vaste wending. Wie zelf wil overschakelen, vraagt het dus eerst: zomaar beginnen met tu kan te vrijpostig overkomen.",
            ],
        ),
        dict(
            aanpak="Deze vragen gaan niet over grammatica maar over wat je moet weten om niet onbeleefd te zijn. Let erop dat niet alles in heel de Franstalige wereld hetzelfde is: België en Frankrijk verschillen op kleine punten.",
            waarom=[
                "Het aantal kussen verschilt per streek, van twee tot vier. Bij twijfel wacht je af wat de ander doet.",
                "Septante en nonante zijn Belgisch (en Zwitsers) en volkomen correct Frans. In Frankrijk zeggen ze soixante-dix (zestig-tien) en quatre-vingt-dix (vier keer twintig plus tien). Tachtig is in beide landen quatre-vingts.",
                "Een handig steuntje: 21 juli is de eed van Leopold I in 1831, 14 juli de bestorming van de Bastille in 1789.",
                "L'apéritif is meer dan een drankje: het is het halfuur voor de maaltijd, met iets erbij om te knabbelen. Je wordt uitgenodigd pour l'apéritif en dan eet je niet noodzakelijk mee.",
                "Zie vraag 9: in België en Zwitserland is het septante, in Frankrijk soixante-dix.",
            ],
        ),
        dict(
            aanpak="Frans is een wereldtaal: ongeveer driehonderd miljoen mensen spreken het, op vijf werelddelen. Dat is precies waarom cultuur bij een taalexamen hoort.",
            waarom=[
                "Let op: in Marokko en Algerije is het Frans niet officieel (daar zijn dat het Arabisch en het Berbers), maar het wordt er wel heel veel gebruikt in onderwijs, bestuur en zaken. Officieel is het Frans onder meer in België, Zwitserland, Canada, Luxemburg, Monaco, Senegal, Ivoorkust en Congo.",
                "La Wallonie, met een hoofdletter en vrouwelijk. Het Nederlandstalige deel is la Flandre.",
                "Een voorbeeld maakt het concreet: wie een Franse winkel binnenstapt en alleen bonjour zegt zonder madame, of die een onbekende met tu aanspreekt, maakt geen taalfout maar wel een blunder. Dat weegt in een gesprek zwaarder dan een verkeerd werkwoord.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-schrijven-schriftelijke-interactie-en-leesbeleving-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Bedenk eerst aan wie je schrijft, want daar hangt alles van af: de aanspreking, tu of vous, en hoe je je vraag formuleert. Schrijf daarna korte zinnen die je zeker juist kan maken, in plaats van lange zinnen met een gok erin.",
            waarom=[
                "Drie dingen maken deze mail formeel: Madame, Monsieur zonder naam (je weet niet wie leest), pourriez-vous in plaats van pouvez-vous, en merci d'avance op het einde. Du 2 au 5 août betekent van de 2de tot de 5de: du … au … is het vaste paar voor een periode.",
                "Hier mag alles korter: salut, tu, en geen hoffelijke vorm. Cinq heures et demie is half zes, letterlijk vijf uur en een half. Een Nederlandstalige zegt hier vaak verkeerd demi six.",
                "Wat je hier opschrijft, is precies het criterium register van het examen. Een perfect geschreven mail die te familiair klinkt, verliest punten; een eenvoudige mail in de juiste toon niet.",
            ],
        ),
        dict(
            aanpak="In een verslag over het verleden heb je twee tijden tegelijk nodig. Zet eerst neer wat je deed (passé composé), en zet daarna de achtergrond erbij: het weer, de sfeer, hoe het was (imparfait).",
            waarom=[
                "Let op je hulpwerkwoord. Aller gaat met être (je suis allé) en krijgt dus een e als je een meisje bent: je suis allée. Faire gaat met avoir (nous avons fait) en verandert niet.",
                "De kortste manier om het te onthouden: wat je kan filmen van begin tot eind is passé composé, wat de hele tijd doorliep is imparfait. Il faisait froid duurde de hele dag, je suis allé gebeurde één keer.",
            ],
        ),
        dict(
            aanpak="Een formulier en een kort bericht zijn de twee schrijfopdrachten die je in het echt het meest nodig hebt. Let bij een formulier op nom en prénom: die staan in het Frans in de andere orde dan je gewoon bent.",
            waarom=[
                "Nom is je familienaam, prénom je voornaam. Veel mensen vullen dat precies verkeerd in. Lieu de naissance is je geboorteplaats, niet je woonplaats.",
                "De trainer is vous, dus: bonjour Monsieur, je ne peux pas venir, en een reden met parce que. Kondig ook aan wanneer je er wel bent: dat is wat een trainer wil weten.",
                "Aan een vriendin mag het kort en enthousiast: avec plaisir. Een uur voorstel je met een vraag, en in het Frans schuift er een spatie voor het vraagteken.",
            ],
        ),
        dict(
            aanpak="Bij leesbeleving vraagt men niet of je het gedicht juist begrepen hebt, maar of je kan zeggen wát er staat en wat jij ervan vindt. Zoek dus eerst de beeldspraak, en geef daarna je mening met een reden erbij.",
            waarom=[
                "Het woordje comme (zoals) wijst de vergelijking aan. Het lawaai is comme un ami qui arrive trop tôt et qui parle trop fort: een vriend die te vroeg komt en te luid praat.",
                "Twee redenen zijn er echt twee. En je mag perfect nee zeggen: een onderbouwd nee krijgt even veel punten als een onderbouwd ja.",
                "Quand même betekent toch, ondanks dat. Dat ene woord draait het hele gedicht om: hij weet dat het stoort en laat het binnen.",
                "Dit is de kern van zo'n vraag. Je mening kan niet fout zijn, maar een mening zonder uitleg levert geen punten op. Begin dus altijd met parce que of met een voorbeeld uit de tekst.",
            ],
        ),
        dict(
            aanpak="Vijf keer dezelfde drie fouten: de persoonsvorm bij zijn onderwerp, het adjectief bij zijn naamwoord, en het deelwoord van de passé composé. Lees je eigen tekst drie keer na, één keer voor elk van die drie.",
            waarom=[
                "Les enfants is meervoud, dus jouent met ent. Je hoort het verschil met joue niet, en net daarom wordt deze fout zo vaak gemaakt: je moet ze zien, niet horen.",
                "Aller is een van de werkwoorden met être. Vandaar je suis allé en nooit j'ai allé. Een goed steuntje: de werkwoorden van beweging en verandering (aller, venir, partir, arriver, entrer, sortir, naître, mourir, rester, devenir) gaan met être.",
                "Bij être verandert het deelwoord mee met het onderwerp. Elle is vrouwelijk, dus partie met een e.",
                "Grand staat bij café, en café is mannelijk, dus zonder e. De e van grande hoort bij een vrouwelijk woord: une grande maison.",
                "Bij avoir verandert het deelwoord niet mee met het onderwerp. Nous avons mangé blijft dus zonder s. Dit is het spiegelbeeld van oefening 15, en die twee door elkaar halen is de meest gemaakte fout van allemaal.",
                "Deze drie zijn letterlijk de helft van de punten op taalcorrectheid. Wie bij elke zin van zijn eigen tekst die drie dingen nakijkt, haalt bijna altijd meer dan wie nog een moeilijke zin bijschrijft.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-spreken-gesprekken-klank-en-spelling-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een gesprek in een vreemde taal houd je niet in gang door alles te weten, maar door te zeggen dat je iets niet weet. Leer deze zinnetjes vanbuiten: ze geven je tijd en ze houden het gesprek open.",
            waarom=[
                "Deze zes zinnen zijn samen de belangrijkste woordenschat van een spreekexamen. Pouvez-vous of pourriez-vous met de infinitief erachter is het vaste patroon: répéter, parler plus lentement, m'aider.",
                "Dit heet omschrijven, en een examinator geeft daar punten voor: je lost een probleem op in het Frans in plaats van stil te vallen. C'est la chose qu'on utilise quand… is een vaste opener die bij bijna elk voorwerp past.",
                "Zwijgen is het enige dat je zeker geen punten oplevert. Ook een omschrijving die niet helemaal klopt, houdt het gesprek aan de gang, en dat is precies wat gemeten wordt.",
            ],
        ),
        dict(
            aanpak="Hoffelijkheid in het Frans zit in de werkwoordsvorm, niet alleen in s'il vous plaît. Zet je wil om in een conditionnel (je voudrais, j'aimerais, pourriez-vous) en je zin klinkt meteen anders.",
            waarom=[
                "Je voudrais is de conditionnel van vouloir. Zet er s'il vous plaît bij en je zin is af.",
                "Een impératif alleen klinkt als een bevel. Pourriez-vous met de infinitief erachter maakt er een vraag van.",
                "Hetzelfde patroon als in oefening 5: pourriez-vous plus de infinitief. Let op het kleine woordje m' vóór het werkwoord, want in het Frans staat het voorwerp vóór de infinitief.",
                "J'aimerais is de conditionnel van aimer en betekent ik zou graag. In een sollicitatie zeg je nooit je veux.",
                "Een conditionnel laat de ander ruimte. Dat is geen taalversiering maar het verschil tussen hoffelijk en bot, en in een Franstalige winkel of op een gesprek valt dat echt op.",
            ],
        ),
        dict(
            aanpak="Frans spelt anders dan het klinkt, en de accenten helpen je daarbij. Leer de combinaties in groepjes: ou is oe, u is uu, ai is è, eau is oo. En onthoud dat de uitgang ent van een werkwoord niet te horen is.",
            waarom=[
                "De accenten op de e doen iets met de klank: é is scherp (café), è en ê zijn open (père, fenêtre). De cedille van ç doet iets met de c: ze houdt hem zacht. En let op het paar ou en u: vous met oe, tu met uu. Die twee verwisselen is de meest gehoorde fout bij Nederlandstaligen.",
                "Zonder cedille zou français als frankais klinken, want een c voor een a is hard.",
                "De regel in één zin: cedille voor a, o en u, geen cedille voor e en i. Commençons heeft een o erachter, commencerons een e.",
                "Dit is de grote verrassing van het Frans: de uitgangen e, es en ent van een werkwoord hoor je niet. Je parle, tu parles en ils parlent klinken alle drie hetzelfde.",
                "En net daarom moet je bij een dictee of een invulvraag nadenken in plaats van af te gaan op wat je hoort. De grammatica beslist hier, niet je oor.",
                "De h aan het begin is in het Frans stom: un hôtel klinkt als un otel, un homme als un omme. Daarom hoor je ook de liaison: les hommes klinkt als lezomme.",
            ],
        ),
        dict(
            aanpak="Een vraag stellen kan in het Frans op drie manieren, en ze zijn niet uitwisselbaar van toon. Intonatie is spreektaal, est-ce que is neutraal, de omkering is het meest formeel.",
            waarom=[
                "Let op de streepjes: bij de omkering komt er een koppelteken tussen werkwoord en voornaamwoord (viens-tu). Est-ce que verandert de woordorde niet, en net daarom is die vorm het veiligst als je twijfelt.",
                "Habite eindigt op een klinker, en il begint met een klinker. Daarom schuift er een t tussen: habite-t-il. Zonder die t zou je twee klinkers tegen elkaar krijgen, en dat doet het Frans niet.",
                "In een mail zie je geen intonatie, dus die vorm valt weg. Est-ce que is altijd veilig; de omkering klinkt nog een trapje formeler.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-woordvelden-mens-familie-gevoelens-en-gezondheid-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Leer familiewoorden altijd met hun lidwoord erbij: le of la hoort bij het woord. In het Frans is er geen keuze zoals bij ons de of het, en een verkeerd lidwoord sleept een verkeerd adjectief achter zich aan.",
            waarom=[
                "Twee paren worden vaak verwisseld. Le fils is de zoon en la fille is zowel het meisje als de dochter. En le cousin tegenover la cousine: dezelfde klank, maar de e maakt er een nicht van.",
                "Een stap tussenin: le fils de ma tante is de zoon van je tante, en dat is je neef, mon cousin. Let op dat mon mannelijk is omdat cousin mannelijk is, ook als het je tante is die ervoor staat.",
                "Mes is het meervoud van mon en ma. Je kiest dus niet tussen mon en ma als er een meervoud volgt: er is maar één vorm.",
            ],
        ),
        dict(
            aanpak="Jezelf voorstellen is het eerste wat je op een spreekexamen moet kunnen, en het bestaat uit vier vaste zinnen. Leer ze als blokken, dan kan je ze zonder nadenken opzeggen.",
            waarom=[
                "Habiter gaat met à voor een stad en en voor een land: j'habite à Hasselt, en Belgique. Voor een mannelijk land is het au: au Canada.",
                "J'ai, nooit je suis. Dit is de klassieke fout en ze valt onmiddellijk op.",
                "Het Frans ziet leeftijd als iets dat je hebt, zoals honger of dorst. Letterlijk zeg je ik heb vijftien jaren. Wij zeggen ik ben vijftien, en die vertaling maakt een zin die in het Frans niet bestaat.",
                "Let op de vraagvorm met tu: quel âge as-tu, comment t'appelles-tu. Het antwoord begint altijd met je, niet met tu.",
            ],
        ),
        dict(
            aanpak="Gevoelens splitsen zich in twee groepen: die met être (je suis triste) en die met avoir (j'ai peur). Leer ze meteen in die twee groepjes, dan vermijd je de fout voor altijd.",
            waarom=[
                "Content en fatigué veranderen mee met wie het is (contente, fatiguée voor een meisje). Avoir peur, avoir faim en avoir soif veranderen nooit: het is altijd peur, faim en soif.",
                "Elle is vrouwelijk, dus contente met een e. Je hoort het verschil hier wel: de t van contente wordt uitgesproken, die van content niet.",
                "Wij zeggen ik ben bang maar ik heb honger. Het Frans is hier makkelijker dan het Nederlands: alle drie met avoir, zonder uitzondering. Doe hetzelfde met avoir chaud, avoir froid en avoir raison.",
                "J'ai froid betekent ik heb het koud, over jezelf. Over het weer zeg je il fait froid. Dat verschil tussen avoir en faire bij weer en gevoel is het waard om vanbuiten te leren.",
            ],
        ),
        dict(
            aanpak="Bij de dokter heb je twee dingen nodig: de lichaamsdelen, en het vaste patroon j'ai mal à. Let daarbij op het samentrekken van à met het lidwoord, want dat is waar het vaak fout gaat.",
            waarom=[
                "Twee bijzondere vormen. Le dos is de rug (niet de rugzak), en l'œil wordt in het meervoud les yeux: een van de weinige woorden in het Frans die in het meervoud helemaal veranderen.",
                "La tête is vrouwelijk, dus à la tête. À la trekt niet samen.",
                "Le ventre is mannelijk, en à + le wordt au. Daarom au ventre en niet à le ventre, want die vorm bestaat niet.",
                "Zet de vier vormen even samen: au (à + le), à la, à l' (voor een klinker) en aux (à + les). Alleen à la en à l' blijven los staan.",
                "Depuis betekent sinds en gaat in het Frans met de tegenwoordige tijd: je suis malade depuis trois jours, letterlijk ik ben ziek sinds drie dagen. Wij zouden de verleden tijd gebruiken, en dat is hier fout.",
                "Deux fois par jour staat ook op echte doosjes: par jour is per dag. Prendre rendez-vous gaat zonder lidwoord, dus niet prendre un rendez-vous als je het in het algemeen bedoelt.",
            ],
        ),
        dict(
            aanpak="Dit is de woordenschat van de opgaven zelf. Ken je ze niet, dan kan je een vraag perfect begrijpen en toch het verkeerde doen. Lees ze één keer per week door tot ze er allemaal in zitten.",
            waarom=[
                "Cochez en entourez worden het meest verwisseld: aankruisen tegenover omcirkelen. En reliez (verbinden) is niet choisissez (kiezen).",
                "Justifiez is het woord waar de meeste punten op verloren gaan. Zodra het er staat, is je antwoord pas af als er een stuk tekst bij staat dat het bewijst. Eén korte verwijzing of een geciteerd zinsdeel volstaat.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-woordvelden-eten-kleding-wonen-en-winkelen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Bij eten en drinken komt er bijna altijd een hoeveelheid bij kijken, en daar heeft het Frans aparte woordjes voor: du, de la, de l' en des. Die heten partitieve lidwoorden en betekenen een onbepaalde hoeveelheid.",
            waarom=[
                "Twee woorden om apart te zetten. L'eau is vrouwelijk (de l'eau), ook al zie je dat niet aan het lidwoord. En la pomme de terre is letterlijk de aardappel: appel van de aarde.",
                "Du is de + le, voor een mannelijk woord: du pain. Bij een vrouwelijk woord wordt het de la soupe, en voor een klinker de l'eau.",
                "Dit is de regel die iedereen vergeet: na een ontkenning worden du, de la en des alle drie gewoon de. Je mange de la viande, maar je ne mange pas de viande.",
                "Zet de twee zinnen onder elkaar en je ziet het patroon. Positief kiest tussen du, de la en des; ontkennend is het altijd de, zonder uitzondering.",
            ],
        ),
        dict(
            aanpak="Zodra er een hoeveelheid vóór het woord staat, verdwijnt het lidwoord en blijft er alleen de of d' over. Dat geldt voor een maat (un kilo), voor een verpakking (une bouteille) en voor woorden als beaucoup, un peu en assez.",
            waarom=[
                "Alleen de tweede is d', en dat komt enkel door de klinker van eau. De regel verandert daar niet, alleen de spelling.",
                "Eén regel voor alle zes: hoeveelheid plus de plus het woord, zonder lidwoord. Un kilo de pommes, nooit un kilo des pommes.",
                "Dit is dé fout die een Nederlandstalige maakt, omdat wij veel van de suiker zeggen. In het Frans is het beaucoup de sucre: de en niets meer.",
            ],
        ),
        dict(
            aanpak="In een winkel heb je maar een handvol zinnen nodig, en je kan ze vanbuiten leren. Begin altijd met bonjour madame of bonjour monsieur: dat is in Frankrijk en Wallonië geen hoffelijkheid maar een gewoonte.",
            waarom=[
                "Vous l'avez en noir heeft een l' die naar het voorwerp verwijst: hebt u het in het zwart. Dat kleine woordje staat in het Frans vóór het werkwoord, niet erachter.",
                "Twee winkelnamen om te onthouden: la boucherie is de slager (van boeuf, rund) en la librairie is de boekhandel. De bibliotheek is la bibliothèque.",
                "Let op het ontbrekende lidwoord bij het brood: un pain is één brood. Wil je een hoeveelheid, dan zeg je du pain.",
                "La librairie is een valse vriend: het lijkt op library maar het is de boekhandel, een winkel. Wie boeken gaat lenen, gaat naar la bibliothèque.",
            ],
        ),
        dict(
            aanpak="Een kleur is in het Frans een bijvoeglijk naamwoord, en die past zich aan: een e erbij als het woord vrouwelijk is, een s erbij als het meervoud is. Leer de kleur dus nooit als los woordje maar met een naamwoord erbij.",
            waarom=[
                "Les chaussures staat altijd in het meervoud, net als bij ons de schoenen. En le pull is gewoon de trui: een van de weinige Franse woorden die uit het Engels komen.",
                "Drie van die zes veranderen in de vrouwelijke vorm (vert wordt verte, noir wordt noire, blanc wordt blanche). Rouge, bleu en jaune eindigen al op een e of blijven gelijk.",
                "Blanc is onregelmatig: de vrouwelijke vorm is blanche, niet blance. Zo ook sec en sèche.",
                "Les chaussures is vrouwelijk én meervoud, dus komen er twee letters bij: noir wordt noire en dan noires.",
                "Dit is het patroon van heel het Frans: een bijvoeglijk naamwoord kijkt naar het woord waar het bij staat, niet naar wie het zegt. Zoek dus eerst het naamwoord en zijn geslacht, dan pas de vorm van de kleur.",
            ],
        ),
        dict(
            aanpak="Je woning beschrijven en je ochtend beschrijven zijn twee vaste spreekopdrachten. Voor de ochtend heb je de wederkerende werkwoorden nodig: se lever, se laver, se coucher.",
            waarom=[
                "La salle de bains staat met een s op het einde, ook in het enkelvoud. En l'étage is de verdieping, niet de etage in de betekenis van appartement.",
                "Il y a is de onmisbare uitdrukking hier: er is of er zijn, en de vorm verandert nooit, ook niet bij een meervoud. Il y a trois chambres, nooit il y ont.",
                "Vier van de zes zijn wederkerend: se lever, se laver, se coucher, en ook ranger sa chambre heeft een bezittelijk woord dat meeverandert. Ik sta op is je me lève, met me erbij.",
                "Twee dingen om na te kijken. Een wederkerend werkwoord krijgt het juiste voornaamwoord (je me lève, tu te lèves), en een uur gaat met à: à sept heures.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-woordvelden-school-werk-en-de-professionele-wereld-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Schoolwoorden lijken vaak op het Nederlands, maar een paar zitten net anders. En het Franse schoolsysteem telt de jaren niet zoals bij ons, dus let op bij een getal.",
            waarom=[
                "Twee valkuilen. La classe is in het Frans zowel het lokaal als de groep leerlingen, en la matière is het vak (wiskunde, Frans), niet het materiaal. Les devoirs en les vacances staan altijd in het meervoud.",
                "Je suis en troisième année, met en en zonder lidwoord. Het rangtelwoord troisième schrijf je voluit of als 3e.",
                "In Frankrijk loopt de nummering omgekeerd: na la sixième (ons eerste middelbaar) daalt het tot la troisième, en dan komen la seconde, la première en la terminale. Een Franse leerling in la seconde zit dus in zijn vierde jaar middelbaar, niet in zijn tweede.",
            ],
        ),
        dict(
            aanpak="Beroepen bestaan in het Frans vaak in twee vormen, en de vrouwelijke vorm volgt een vast patroon: ier wordt ière, eur wordt euse, en soms komt er alleen een e bij. Een paar beroepen hebben maar één vorm.",
            waarom=[
                "Drie patronen naast elkaar: infirmier wordt infirmière (ier naar ière), vendeur wordt vendeuse (eur naar euse), électricien wordt électricienne (dubbele n plus e). Le kinésithérapeute en le comptable eindigen al op een e en blijven gelijk; alleen het lidwoord verandert: la comptable.",
                "Ma mère is vrouwelijk, dus de vrouwelijke vorm infirmière. Zonder lidwoord, zie de volgende oefening.",
                "Dit is een echt verschil met het Nederlands, waar we wel een lidwoord zetten. Elle est une infirmière klinkt voor een Franstalige fout. Het lidwoord komt er pas bij als je iets toevoegt: c'est une infirmière très douce.",
            ],
        ),
        dict(
            aanpak="Een stagemail of een sollicitatie is de meest formele tekst die je in het Frans zal schrijven. Hij heeft drie vaste delen: wie je bent, wat je vraagt, en een hoffelijke afsluiting.",
            waarom=[
                "Begin met wie je bent en in welk jaar je zit, want dat is het eerste wat een werkgever wil weten. J'aimerais faire un stage is hoffelijker dan je veux faire un stage, en zet er meteen bij hoe lang en wanneer.",
                "Twee woorden die vaak verwisseld worden: la candidature is de sollicitatie (de brief, het dossier) en l'entretien is het gesprek. En le patron is de baas, niet het patroon.",
                "Dit is het criterium register weer. Een sollicitatie met salut of met afkortingen leest een werkgever als onverzorgd, hoe goed je Frans ook is.",
                "Cordialement is kort en altijd veilig. Veuillez agréer mes salutations distinguées is de volledige, zeer formele formule: leer er één van de twee goed in plaats van beide half.",
            ],
        ),
        dict(
            aanpak="Jouer en faire hebben elk hun eigen voorzetsel, en dat is geen gevoel maar een regel. Jouer à bij een sport of spel met tegenstander, jouer de bij een instrument, faire de bij een sport die je beoefent.",
            waarom=[
                "Let op hoe à en de samentrekken met het lidwoord: à + le wordt au (au football), de + le wordt du (du piano, du vélo), de + la blijft de la (de la natation) en voor een klinker de l' (de l'athlétisme).",
                "Een handig steuntje: wat je bespeelt gaat met de, wat je speelt gaat met à. Daarom jouer du piano maar jouer au tennis.",
                "Twee woorden voor de digitale wereld die je echt nodig hebt: un mot de passe is een wachtwoord (letterlijk een doorgangswoord) en télécharger is downloaden.",
                "Basket is een sport met een tegenstander, dus jouer au basket. Du hoort bij een instrument, en zo wordt die zin: ik bespeel de basket.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-woordvelden-tijd-weer-reizen-en-vervoer-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Dagen, maanden en seizoenen krijgen in het Frans geen hoofdletter: dat is de eerste regel om te onthouden. Daarna let je op de kleine voorzetsels, want die verschillen per soort tijdsaanduiding.",
            waarom=[
                "Juin en juillet lijken sterk op elkaar: juni en juli. Spreek juillet uit als zjwie-jee, met de ll als een j.",
                "Alle vier mannelijk, maar drie beginnen met een klinker en krijgen dus l'. Het voorzetsel verschilt ook: au printemps, maar en été, en automne, en hiver.",
                "Bij een maand alleen gebruik je en: en mars, en septembre. Je kan ook au mois de mars zeggen.",
                "Bij een datum komt er le voor: le 1er septembre, le 15 mars. Dus en voor een maand alleen, le voor een dag in die maand.",
                "Dit is een echte spellingfout die veel punten kost. Lundi, mars, janvier: allemaal met een kleine letter, tenzij ze aan het begin van een zin staan. Alleen landen en talen volgen andere regels.",
            ],
        ),
        dict(
            aanpak="Het uur zeggen gaat in het Frans tot het halfuur vooruit (et quart, et demie) en daarna achteruit vanaf het volgende uur (moins le quart, moins dix). Op borden en tickets wordt het uur altijd voluit van 0 tot 24 gelezen.",
            waarom=[
                "Vergelijk 8.45 en 17.50: beide rekenen terug vanaf het volgende uur, dus neuf heures moins le quart en six heures moins dix. Let op het lidwoord le bij moins le quart, dat er bij et quart niet staat. En midi en minuit staan zonder heures: nooit douze heures voor de middag.",
                "Quelle heure est-il, met de omkering. In spreektaal hoor je ook il est quelle heure.",
                "Dit is handig in het echt: 18h40 lees je op een bord als dix-huit heures quarante, maar in een gesprek zeg je sept heures moins vingt. Wie zich aan de bordversie houdt, wordt wel begrepen; wie 18.40 vertaalt als huit heures quarante staat op het verkeerde perron.",
            ],
        ),
        dict(
            aanpak="Plaatsbepalingen leer je in paren: sur en sous, devant en derrière, dans en hors de. Let op à côté, want dat heeft altijd de erbij: à côté de l'école.",
            waarom=[
                "À côté de is het enige dat een de nodig heeft, en die de trekt samen met het lidwoord: à côté du parc, à côté de la gare, à côté de l'école. De andere staan los voor het lidwoord.",
                "De drie woorden die je bij een routebeschrijving echt nodig hebt: tout droit (rechtdoor), à gauche (links) en à droite (rechts). Let op het verschil tussen tout droit en à droite, want die twee lijken te veel op elkaar om te gokken.",
            ],
        ),
        dict(
            aanpak="Het weer gaat in het Frans met il: il fait, il pleut, il neige, il y a. Die il verwijst naar niemand en de vorm verandert nooit.",
            waarom=[
                "Drie patronen naast elkaar. Il fait plus een woord (beau, froid, vingt degrés), il plus een werkwoord dat alleen zo bestaat (il pleut, il neige), en il y a du plus een naamwoord (du vent, du soleil, du brouillard).",
                "Dit heet een onpersoonlijk werkwoord. Pleuvoir en neiger bestaan alleen in de derde persoon enkelvoud, net als bij ons het regent. Je kan dus niet zeggen nous pleuvons, en dat is precies waarom je die vormen niet moet leren.",
                "Ook in de toekomende tijd blijft het il: il va pleuvoir, il va neiger, il va faire froid.",
            ],
        ),
        dict(
            aanpak="Bij vervoer gaat het om twee dingen: de woorden zelf, en het voorzetsel waarmee je zegt hoe je gaat. En in een treinstation heb je maar twee zinnen nodig: een ticket vragen en zeggen voor wanneer.",
            waarom=[
                "Le quai is het perron (en ook de kade) en le billet is het ticket. Un ticket bestaat ook, maar dan voor de bus of de metro.",
                "Let op het verschil tussen en en à. En bij een vervoermiddel waar je in zit (en train, en voiture, en avion) en à bij een waar je op of aan zit: à vélo, à pied, à cheval.",
                "Un aller-retour is een heen-en-terugticket, als één woord met een streepje. Zeg er altijd bij voor wanneer en of je een korting hebt: dat verwacht de persoon aan het loket.",
                "Un aller simple is enkel heen. Aller is gaan, dus letterlijk een gewone heenreis.",
            ],
        ),
        dict(
            aanpak="Bij een land kiest het Frans zijn voorzetsel op het geslacht van dat land. Dat is dus eerst geslacht opzoeken, dan voorzetsel kiezen: en bij vrouwelijk, au bij mannelijk, aux bij meervoud.",
            waarom=[
                "Zet de vijf naast elkaar en je ziet het systeem. La Belgique en la France zijn vrouwelijk, dus en. Le Canada en le Portugal zijn mannelijk, dus au, en bij een herkomst du Portugal. Les Pays-Bas is meervoud, dus aux.",
                "Een nuttige vuistregel: een land dat op een e eindigt is bijna altijd vrouwelijk (la France, la Belgique, la Suisse). De uitzondering om te kennen is le Mexique.",
                "Belge, français, néerlandais: alle drie ook de naam van de taal, met een kleine letter. Let op néerlandais, want het Vlaams als taal bestaat in het Frans niet als officiële naam.",
                "Hier zit een echt verschil. Als bijvoeglijk naamwoord of als taal schrijf je klein: il est belge, je parle français. Als naam van een inwoner schrijf je groot: un Belge, les Français. Het Nederlands doet beide met een hoofdletter, dus dit moet je echt leren.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-zelfstandige-naamwoorden-lidwoorden-en-determinanten-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het geslacht van een Frans woord moet je leren, maar een aantal uitgangen verraden het. Leer die uitgangen en je hoeft maar de helft van de woorden te onthouden.",
            waarom=[
                "Let op l'école: de apostrof zegt niets over het geslacht. École is vrouwelijk, maar voor een klinker worden le en la allebei l'. Wil je het geslacht weten, zet er dan een adjectief bij: une grande école.",
                "Vier uitgangen zijn het waard om vanbuiten te kennen. Vrouwelijk: té (la liberté, la beauté) en tion (la nation, la question). Mannelijk: age (le fromage, le village) en ème (le problème, le système).",
                "Het Nederlandse lidwoord helpt je niet: la maison is vrouwelijk maar le livre is mannelijk, en bij ons zijn het beide de. Leer het Franse lidwoord dus samen met het woord, als één geheel.",
            ],
        ),
        dict(
            aanpak="Het meervoud is in het Frans meestal een s erbij, maar vier groepjes doen het anders: al wordt aux, eau wordt eaux, en woorden die al op s of x eindigen veranderen niet.",
            waarom=[
                "Zet de patronen even apart. Cheval en journal eindigen op al en worden chevaux en journaux. Gâteau en bureau krijgen gewoon een x erbij. Animal wordt animaux, dus ook die hoort bij de eerste groep.",
                "Bus en prix eindigen al op een sisklank, dus er komt niets bij. Œil wordt yeux, een volledig ander woord: dat is er één om echt te leren.",
                "Dit is het lastige aan het Franse meervoud: je hoort het niet aan het woord, want die s blijft stom. Je hoort het alleen aan le tegenover les. En bij un tegenover des.",
            ],
        ),
        dict(
            aanpak="Het Frans heeft vier soorten lidwoorden, en die door elkaar halen is de meest gemaakte fout. Bepaald (le, la, les) voor iets dat je kent, onbepaald (un, une, des) voor iets nieuws, partitief (du, de la, de l') voor een hoeveelheid, en samengetrokken (au, aux, du, des) na à of de.",
            waarom=[
                "Vergelijk de laatste twee. Je mange du pain is een hoeveelheid brood, dus partitief. Il parle des professeurs is de + les, dus samengetrokken. Dezelfde vorm, een andere reden.",
                "Dit is precies waarom du twee keer in de lijst staat. Je ziet het verschil aan het werkwoord: manger of boire vraagt een hoeveelheid, parler de of avoir besoin de vraagt een samentrekking.",
                "Aux, want à + les trekt altijd samen. Alleen à la en à l' blijven los.",
                "Du, want ook de + le trekt samen. De la en de l' blijven los staan.",
            ],
        ),
        dict(
            aanpak="Twee gevallen waar het lidwoord gewoon de wordt: na een hoeveelheid, en na een ontkenning. Onthoud ze als één regel, want ze zien er in een oefening hetzelfde uit.",
            waarom=[
                "Alleen vóór een klinker wordt het d': d'amis, d'argent. De regel verandert daar niet.",
                "Un, une, du, de la en des worden alle vijf de. Alleen na être blijft het lidwoord staan: ce n'est pas un problème.",
                "Il n'y a pas de chaises, met de. Dit is dezelfde regel als in oefening 12, en net hier wordt des het vaakst laten staan.",
            ],
        ),
        dict(
            aanpak="Een determinant is het woordje vóór het naamwoord dat zegt welk of wiens: ce, mon, quel. Ze passen zich alle drie aan het naamwoord aan, en ze hebben alle drie een aparte vorm voor een woord dat met een klinker begint.",
            waarom=[
                "Drie rijtjes naast elkaar. Aanwijzend: ce, cet (voor een klinker), cette, ces. Bezittelijk: mon, ma, mes. En let op mon amie, zie de volgende vraag.",
                "Het Frans vermijdt twee klinkers na elkaar. Daarom mon amie, mon école, cet homme en cet arbre. Het geslacht van het woord verandert daar niet door: je zegt nog altijd mon amie est belle, met een e.",
                "Quel verandert mee met het naamwoord, net als een adjectief: quel livre, quelle heure, quels projets, quelles matières. Dat is de hele regel.",
                "Une journée is vrouwelijk, dus quelle. Quel belle journée is een van de meest gemaakte fouten, omdat we het verschil niet horen.",
            ],
        ),
        dict(
            aanpak="Tot twintig moet je de telwoorden gewoon kennen. Daarboven let je op de koppeltekens en op het verschil tussen België en Frankrijk bij zeventig en negentig.",
            waarom=[
                "Twee dingen om op te letten. Vingt et un is de enige groep met et erin (zoals trente et un, quarante et un); de rest gaat met een streepje: vingt-deux, vingt-trois. En quatre-vingts krijgt een s, maar quatre-vingt-un en quatre-vingt-dix niet.",
                "Le premier is onregelmatig, zoals bij ons eerste en niet eenste. Vanaf drie is het altijd het getal plus ième: troisième, quatrième, dixième. Le second bestaat ook naast le deuxième, maar dan vooral als er maar twee zijn.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-voornaamwoorden-sujet-cod-coi-en-de-wederkerende-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het onderwerp zoek je door te vragen: wie doet het? Let bij de derde persoon op het getal en het geslacht, en op on, dat een vorm apart is.",
            waarom=[
                "Twee bijzondere gevallen. Il pleut heeft een il die naar niemand verwijst. En Marie et Léa zijn twee vrouwen, dus elles met een s; was er één man bij, dan werd het ils.",
                "On is spreektaal voor nous en tegelijk het Franse men. Het belangrijkste om te onthouden: het werkwoord staat altijd in de hij-vorm. On va, on parle, on est. Nooit on allons.",
            ],
        ),
        dict(
            aanpak="Een COD is het lijdend voorwerp: je vindt het met de vraag wie of wat. Het voornaamwoord ervoor is le, la of les, en in het Frans schuift dat vóór het werkwoord.",
            waarom=[
                "Le voor mannelijk, la voor vrouwelijk, les voor meervoud, en l' voor een klinker (je l'aime). Let op: les blijft les, ook voor een klinker.",
                "Dit is het grootste verschil tussen de twee talen, en de fout die een Nederlandstalige blijft maken. Wij zeggen ik zie hem, het Frans zegt je le vois: ik hem zie. Oefen dat tot het automatisch gaat.",
                "L', want ai begint met een klinker. Het volledige antwoord is oui, je l'ai.",
            ],
        ),
        dict(
            aanpak="Een COI is het meewerkend voorwerp, en je herkent het aan het voorzetsel à: parler à, téléphoner à, écrire à, donner à. Het voornaamwoord is lui voor één persoon en leur voor meerdere.",
            waarom=[
                "Let op leur zonder s, ook al is het meervoud. Leurs met een s bestaat ook, maar dat is het bezittelijke: leurs parents.",
                "Dit is de hele truc, en ze werkt altijd: staat er à voor, dan lui of leur. Let op de werkwoorden die in het Frans een à nemen en in het Nederlands niet, zoals téléphoner à en obéir à.",
                "Lui is hier onzijdig wat geslacht betreft: het kan aan hem of aan haar zijn. Wil je het verduidelijken, dan zeg je je parle à elle. Dat is het spiegelbeeld van le en la, waar je het geslacht juist wel ziet.",
            ],
        ),
        dict(
            aanpak="Een wederkerend werkwoord heeft een voornaamwoord dat meeverandert met het onderwerp: me, te, se, nous, vous, se. Dat woordje hoort bij het werkwoord en gaat overal mee: in de ontkenning, in de passé composé en in een bevel.",
            waarom=[
                "Me, te en se worden m', t' en s' voor een klinker: il s'appelle, je m'amuse. Nous en vous blijven gelijk, en daardoor staat het er twee keer: nous nous levons.",
                "Het voornaamwoord se wordt hier il se lève. Let ook op het accent: lever krijgt in de ik-, jij-, hij- en zij-vorm een accent grave (je me lève), maar niet in nous levons.",
                "In de ontkenning staan ne en pas rond het geheel van se lève: il ne se lève pas. Het se blijft dus binnen de tang zitten.",
                "In een bevel verhuist het naar achter, met een streepje: lève-toi, couche-toi, amusez-vous. En te wordt toi. In de ontkennende vorm gaat het weer naar voren: ne te lève pas.",
                "Altijd être, zonder uitzondering, en dan verandert het deelwoord mee: elle s'est levée met een e, ils se sont levés met een s. Dit is de meest gemaakte fout bij een verslag in het verleden.",
            ],
        ),
        dict(
            aanpak="Y en en zijn twee kleine woordjes die een heel stuk zin vervangen. Y staat voor een plaats of iets met à, en voor iets met de of een hoeveelheid.",
            waarom=[
                "Let op de laatste: elle en a trois. Het getal blijft staan en en vervangt alleen het naamwoord. Dat voelt vreemd maar het is verplicht: elle a trois kan niet.",
                "Een steuntje: y hoort bij à en en hoort bij de. Daarom j'y vais (aller à) en j'en parle (parler de).",
                "Dit is de val. Il y a is een vaste uitdrukking die er is of er zijn betekent, en die y verwijst naar niets. Je kan hem niet weglaten en niet vervangen.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een adjectief kijkt altijd naar het naamwoord waar het bij staat. Zoek dus eerst dat naamwoord, bepaal of het vrouwelijk is en of het meervoud is, en pas dan de vorm aan.",
            waarom=[
                "Vier patronen in één rij. Gewoon een e of een s erbij (petite, verts). Eux wordt euse (heureux, heureuse). If wordt ive (sportif, sportive). En blanc wordt blanche, een eigen vorm. Beau blijft beau bij een mannelijk woord; bij een vrouwelijk wordt het belle.",
                "Twee dingen, en in die orde: eerst het geslacht, dan het getal. De e komt vóór de s: une petite maison, des petites maisons.",
                "Heureux eindigt al op een x, dus in het mannelijk meervoud verandert er niets (des hommes heureux). Vrouwelijk wordt het heureuse, en in het meervoud heureuses.",
            ],
        ),
        dict(
            aanpak="De meeste Franse adjectieven staan achter het naamwoord, en dat is het omgekeerde van het Nederlands. Alleen een kleine groep korte, veelgebruikte woorden staat ervoor.",
            waarom=[
                "Vergelijk une grande maison en une voiture rouge. Grand hoort bij de groep die vooraan staat, een kleur hoort er altijd achter. Dat is geen gevoel maar een lijstje dat je moet kennen.",
                "Een geheugensteuntje dat in het Frans zelf gebruikt wordt: beauté, âge, bonté, nombre, grandeur. Dus beau en joli, jeune en vieux, bon en mauvais, premier en deuxième, grand en petit. Al de rest staat achter het naamwoord.",
                "De meeste staan erachter, maar niet allemaal. En bij een paar verandert de betekenis zelfs met de plaats: un homme grand is een lange man, un grand homme een groot man.",
            ],
        ),
        dict(
            aanpak="De trappen van vergelijking werken met een vast paar woorden rond het adjectief: plus … que, moins … que, aussi … que. Voor de overtreffende trap zet je het lidwoord ervoor: le plus, la plus, les plus.",
            waarom=[
                "Let erop dat het lidwoord van de overtreffende trap meeverandert met het naamwoord: le film le plus intéressant, la maison la plus chère. En que is het vergelijkingswoord, niet comme.",
                "Meilleur, net zoals bon in het Nederlands beter wordt en niet goeder.",
                "Le meilleur, la meilleure, les meilleurs. Het lidwoord verandert mee met het naamwoord.",
                "Elke taal heeft een paar woorden die hun eigen trap hebben. In het Frans zijn dat bon (meilleur), mauvais (pire) en bien (mieux).",
                "Twee dingen in één zin: la meilleure met een e omdat elle vrouwelijk is, en de la classe met de voor het geheel waar ze de beste van is.",
            ],
        ),
        dict(
            aanpak="Een bijwoord zegt hoe iets gebeurt, en in het Frans maak je het bijna altijd met ment. De truc: begin bij de vrouwelijke vorm van het adjectief, en plak er dan ment aan.",
            waarom=[
                "Zie je waarom je via de vrouwelijke vorm moet? Lent wordt lente en dan lentement; heureux wordt heureuse en dan heureusement. Eindigt het adjectief al op een klinker, dan komt ment er gewoon bij: rapide wordt rapidement, vrai wordt vraiment.",
                "Deze ene regel dekt bijna alle Franse bijwoorden. De uitzonderingen die je apart moet kennen zijn bien (van bon) en mal (van mauvais).",
                "Jamais betekent nooit, maar alleen met ne erbij: il ne vient jamais. Los gebruikt in een antwoord betekent jamais ook nooit: « Tu fumes ? Jamais ! »",
                "Toujours, souvent, parfois, rarement. Zet ze in die orde in je hoofd, dan heb je meteen vier woorden die je in elk gesprek nodig hebt.",
                "Jamais, en ne staat vooraan: il ne vient jamais. Pas verdwijnt daarbij, want twee ontkenningen zet het Frans niet naast elkaar.",
            ],
        ),
        dict(
            aanpak="Voorzetsels vertaal je niet: ze horen bij het werkwoord. Penser à, avoir besoin de, parler de: leer het werkwoord met zijn voorzetsel als één stuk.",
            waarom=[
                "Twee vaste paren om apart te leren. Penser à iemand (denken aan) en avoir besoin de iets (nodig hebben). En du … au voor een periode: du lundi au vendredi, du 2 au 5 août.",
                "Dit verschil kost in het echt afspraken. Dans trois jours is over drie dagen, pendant trois jours is drie dagen lang, en il y a trois jours is drie dagen geleden. Die drie staan het best samen in je hoofd.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-present-imperatif-en-de-wederkerende-werkwoorden-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Drie vormen die er in het Frans bijna gelijk uitzien: de infinitief (parler), de persoonsvorm (il parle) en het deelwoord (parlé). Ze klinken bij een werkwoord op er zelfs precies hetzelfde. Je herkent ze aan wat ervoor staat.",
            waarom=[
                "De vuistregel: staat er een persoonsvorm voor (je vais, je dois, j'aime), dan volgt een infinitief. Staat er een hulpwerkwoord voor (j'ai, je suis), dan volgt een deelwoord.",
                "Je vais is al vervoegd, dus wat erachter komt blijft in de infinitief: aller. Je vais aller betekent ik ga gaan, en dat is gewoon de toekomende tijd.",
                "Je suis is hier het hulpwerkwoord van de passé composé, dus komt er een deelwoord: allé.",
                "Dit is de fout die een luisterend oor nooit vindt, want aller en allé klinken hetzelfde. Je moet dus kijken naar het woord ervóór, niet luisteren.",
            ],
        ),
        dict(
            aanpak="De regelmatige werkwoorden vallen in drie groepen: op er (parler), op ir (finir) en op re (vendre). Leer één werkwoord per groep echt goed vanbuiten, dan heb je er honderden.",
            waarom=[
                "Let op de ir-groep: die schuift er iss tussen in het meervoud (nous finissons, ils finissent). De re-groep doet dat niet (nous vendons, ils vendent).",
                "Dit is de reden waarom een dictee in het Frans zo lastig is. Je parle, tu parles, il parle en ils parlent klinken alle vier als parl. Alleen de nous- en de vous-vorm hoor je. Bij een schrijfopdracht moet je dus eerst het onderwerp zoeken en daarna de uitgang kiezen.",
            ],
        ),
        dict(
            aanpak="De onregelmatige werkwoorden zijn precies de werkwoorden die je het vaakst nodig hebt: être, avoir, aller, faire, pouvoir, devoir, prendre, venir. Leer ze als rijtjes, want een regel is er niet.",
            waarom=[
                "Twee rijtjes die je echt moet kennen, want ze zijn ook de hulpwerkwoorden: être (suis, es, est, sommes, êtes, sont) en avoir (ai, as, a, avons, avez, ont). Let op vous faites en vous dites, de twee vous-vormen die niet op ez eindigen.",
                "Ils ont is avoir (zij hebben), ils sont is être (zij zijn). Je hoort het verschil wel: bij ils ont klinkt er een z (ilzon), bij ils sont een s (ilson).",
                "Leeftijd gaat in het Frans met avoir, nooit met être. Zie ook het hoofdstuk over jezelf voorstellen.",
            ],
        ),
        dict(
            aanpak="De impératif is de vorm van de présent zonder het onderwerp ervoor. Er zijn maar drie personen: tu, nous en vous. Let op de s die bij de er-werkwoorden wegvalt.",
            waarom=[
                "Vergelijk parle en finis. Een werkwoord op er verliest zijn s in de tu-vorm, de andere houden ze. En être is onregelmatig: sois, soyons, soyez.",
                "Dit is zuiver spelling, want je hoort het verschil niet. Alleen bij de er-groep (en bij aller: va !) valt die s weg.",
                "Precies daaraan herken je een voorschrift: er staat geen onderwerp. Dat is het kenmerk van recepten, handleidingen en bijsluiters, en net daarom zie je het terug bij de vraag naar de tekstsoort.",
                "Appelle-moi, met een streepje en met moi in plaats van me. In een bevel verhuist het voornaamwoord naar achter, en me wordt moi, te wordt toi.",
            ],
        ),
        dict(
            aanpak="Zodra er twee werkwoorden na elkaar komen, is het tweede een infinitief. Dat is een van de weinige Franse regels zonder uitzondering, en ze lost heel veel zinnen op.",
            waarom=[
                "Vijf verschillende werkwoorden ervoor (aimer, devoir, pouvoir, il faut, aller), en vijf keer dezelfde infinitief erachter. Dat is het patroon.",
                "Twee persoonsvormen na elkaar bestaat niet in het Frans. Wij zeggen ik wil dat ik eet of ik wil eten; het Frans heeft daar alleen die tweede vorm voor.",
                "M', want aider begint met een klinker (me wordt m'). En let op de plaats: het staat vóór de infinitief, niet erachter. Tu peux m'aider, letterlijk jij kan mij helpen.",
            ],
        ),
        dict(
            aanpak="Een onpersoonlijk werkwoord heeft een il die naar niemand verwijst. Je kan die werkwoorden dus niet vervoegen in de andere personen: ze bestaan maar in één vorm.",
            waarom=[
                "Il faut is er een om goed te kennen: het betekent men moet of het is nodig, en er komt een infinitief achter (il faut partir).",
                "Il y a, wat er is of er zijn betekent. De vorm verandert nooit, ook niet bij een meervoud.",
                "Er is geen wij die regent. Daarom staan pleuvoir, neiger en falloir alleen in de hij-vorm. Dat scheelt je drie rijtjes leren.",
                "Il y a blijft altijd il y a, bij één stoel en bij honderd stoelen. In het verleden wordt het il y avait, en in de toekomst il y aura, maar nooit in het meervoud.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-passe-compose-imparfait-en-passe-recent-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een passé composé bestaat uit twee stukken: een hulpwerkwoord (avoir of être) en een voltooid deelwoord. Begin met de deelwoorden, want die moet je sowieso kennen.",
            waarom=[
                "De regelmatige zijn makkelijk: er wordt é, ir wordt i, re wordt u. De tien onregelmatige hieronder zijn de tien die je het vaakst nodig hebt: fait, pris, vu, eu, été, venu, mis. Die moet je echt vanbuiten leren.",
                "Een é met een accent aigu. Let op dat je daar geen er van maakt: parler en parlé klinken hetzelfde maar zijn niet hetzelfde.",
            ],
        ),
        dict(
            aanpak="De grote vraag bij elke passé composé: avoir of être? De meeste werkwoorden nemen avoir. Alleen een korte lijst van werkwoorden van komen, gaan en blijven neemt être, plus alle wederkerende werkwoorden.",
            waarom=[
                "Let op de wederkerende: je me suis levé, met me tussen je en suis. Het hulpwerkwoord is daar altijd être.",
                "Een geheugensteuntje dat in heel Vlaanderen gebruikt wordt: het huis van être. Je gaat naar binnen (entrer) en naar buiten (sortir), je komt aan (arriver) en vertrekt (partir), je gaat omhoog (monter) en omlaag (descendre), je wordt geboren (naître) en je sterft (mourir), je valt (tomber) en je blijft (rester). Al de rest gaat met avoir.",
            ],
        ),
        dict(
            aanpak="Dit is de regel waarop de meeste punten verloren gaan, en ze is kort: met être verandert het deelwoord mee met het onderwerp, met avoir niet.",
            waarom=[
                "Zet de twee helften naast elkaar. Met être: partie, arrivés, sorties, restés, allemaal met een e of een s. Met avoir: mangé en pris, allebei onveranderd, hoe het onderwerp er ook uitziet.",
                "Denk aan être als een spiegel: het deelwoord weerspiegelt het onderwerp. Avoir doet dat niet. (Er bestaat één uitzondering bij avoir, als het lijdend voorwerp vóór het werkwoord staat, maar die hoef je voor dit niveau niet te kennen.)",
                "Nous avons mangé une pizza, zonder s. Avoir laat het deelwoord met rust, hoe meervoudig het onderwerp ook is.",
            ],
        ),
        dict(
            aanpak="De imparfait is de regelmatigste tijd van het Frans: één recept voor zowat alle werkwoorden. Neem de nous-vorm van de présent, haal de uitgang ons eraf, en plak er ais, ais, ait, ions, iez, aient aan.",
            waarom=[
                "Zie hoe het recept werkt. Nous faisons wordt fais- en dan faisais. Nous prenons wordt pren- en dan prenais. Nous allons wordt all- en dan allait. Alleen être volgt het recept niet.",
                "Dit recept is goud waard, want het werkt ook bij de onregelmatige werkwoorden. Wie de nous-vorm van de présent kent, kent de hele imparfait.",
                "Être, met de stam ét-: j'étais, tu étais, il était, nous étions, vous étiez, ils étaient. Dat is de enige uitzondering die je moet onthouden.",
            ],
        ),
        dict(
            aanpak="Kiezen tussen de twee verleden tijden gaat met één vraag: is het een gebeurtenis of een achtergrond? Een gebeurtenis die begon en eindigde gaat in de passé composé. Een toestand, een gewoonte of iets dat bezig was gaat in de imparfait.",
            waarom=[
                "Let op de signaalwoorden, want die verraden de tijd. Hier, soudain, tout à coup en un jour kondigen een passé composé aan. Souvent, toujours, chaque jour, quand j'étais petit en het weer kondigen een imparfait aan. En de laatste zin toont het klassieke paar: iets was bezig (dormais) toen er iets gebeurde (est arrivé).",
                "Een verslag is net daarom een goede oefening: het heeft beide tijden nodig. Wat elke dag zo was, staat in de imparfait; wat op één dag gebeurde, in de passé composé.",
            ],
        ),
        dict(
            aanpak="De passé récent zegt dat iets nét gebeurd is, en hij bestaat uit drie vaste stukken: venir vervoegd, dan de, dan de infinitief. Meer is het niet.",
            waarom=[
                "Alleen venir verandert mee (je viens, elle vient, nous venons). De en de infinitief blijven gelijk, en de wordt d' voor een klinker: elle vient d'arriver.",
                "Zet de twee tegenover elkaar, want ze zijn elkaars spiegel. Venir de kijkt net achteruit, aller kijkt net vooruit. Je viens de manger en je vais manger verschillen maar in één woord.",
                "Elle vient de partir. Het hele patroon blijft staan: alleen venir volgt het onderwerp.",
                "Dat is net het gemakkelijke eraan: het tweede werkwoord blijft altijd in de infinitief. Zoals bij je vais manger en je veux manger.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-futur-proche-futur-simple-en-de-conditionnel-de-politesse-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De futur proche is de makkelijkste toekomende tijd die er is: aller vervoegen en er een infinitief achter zetten. Precies zoals wij ik ga eten zeggen.",
            waarom=[
                "Let op de laatste: bij een wederkerend werkwoord verhuist het voornaamwoord mee naar de infinitief, en het volgt het onderwerp: elle va se lever, je vais me lever.",
                "Alleen aller. Het tweede werkwoord blijft onveranderd staan, in welke persoon de zin ook staat.",
                "Ne en pas gaan rond vais, want dat is de persoonsvorm: je ne vais pas manger. Niet rond manger.",
            ],
        ),
        dict(
            aanpak="De futur simple is één woord in plaats van twee. Je vertrekt van de infinitief zelf en plakt er de uitgangen ai, as, a, ons, ez, ont aan. Dat zijn, niet toevallig, zowat de vormen van avoir.",
            waarom=[
                "Zie hoe de infinitief gewoon blijft staan: parler wordt parlerai, finir wordt finiras, habiter wordt habiterons. Er komt niets weg behalve de laatste e bij de re-groep.",
                "Prendre verliest alleen zijn laatste e: prendr- plus de uitgang. Zo ook vendre (je vendrai) en attendre (j'attendrai).",
                "Dat ene teken is de beste controle die je hebt. Staat er geen r vóór de uitgang, dan is het geen futur. Het is ook wat de futur van de imparfait onderscheidt: je parlerai tegenover je parlais.",
            ],
        ),
        dict(
            aanpak="Een handvol werkwoorden heeft een eigen stam in de futur. Het goede nieuws: diezelfde stam gebruik je ook voor de conditionnel, dus wie ze één keer leert, heeft er twee tijden mee.",
            waarom=[
                "Negen stammen om vanbuiten te kennen: ser- (être), aur- (avoir), ir- (aller), fer- (faire), pourr- (pouvoir), voudr- (vouloir), viendr- (venir), verr- (voir), devr- (devoir). Ze eindigen allemaal op een r, net als bij de regelmatige.",
                "Irons: de stam ir- plus de uitgang ons. Het lijkt kort, maar dat is de hele vorm.",
                "Beide zijn juist, en je mag kiezen. In spreektaal hoor je vaker je vais aller, in een geschreven tekst staat er vaker j'irai.",
            ],
        ),
        dict(
            aanpak="Hier beslist het woord van tijd, niet je gevoel. Hier en quand j'étais petit vragen een verleden tijd, demain en la semaine prochaine een toekomende, maintenant de présent.",
            waarom=[
                "Let op het verschil tussen de twee verleden zinnen. Hier is één keer, dus passé composé. Quand j'étais petit is een gewoonte, dus imparfait. En je viens de rentrer is de passé récent: net gebeurd.",
                "Zoek bij een invulvraag altijd eerst het woord van tijd. Dat is sneller en betrouwbaarder dan de zin aanvoelen, en op een examen staat het er bijna altijd bij.",
            ],
        ),
        dict(
            aanpak="De conditionnel de politesse is de futur-stam met de uitgangen van de imparfait: ais, ais, ait, ions, iez, aient. Daarmee wordt je vraag hoffelijk in plaats van eisend.",
            waarom=[
                "Drie vormen die je in elk gesprek nodig hebt: je voudrais, j'aimerais en pourriez-vous. Let op de vierde: tegen tu wordt het pourrais-tu, met dezelfde stam maar de tu-vorm.",
                "Kijk naar de uitgangen: aurai tegenover aurais, serai tegenover serais, pourrai tegenover pourrais. Dezelfde stam, een andere uitgang.",
                "De s, en je hoort hem niet. Je pourrai venir betekent ik zal kunnen komen; je pourrais venir betekent ik zou kunnen komen. Op een schrijfopdracht is dat het verschil tussen een belofte en een voorstel.",
                "Een formele mail bestaat bijna helemaal uit conditionnels: j'aimerais voor wat je wil, pourriez-vous voor wat je vraagt. Zet er een aanspreking voor en een afsluiting achter en je mail is af.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-zinsbouw-zinsdelen-voegwoorden-en-de-overeenkomst-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De Franse woordvolgorde is vaster dan de Nederlandse: onderwerp, persoonsvorm, rest. Zet je iets vooraan, dan verandert er aan die volgorde niets, en dat is precies waar een Nederlandstalige struikelt.",
            waarom=[
                "Je herkent de zinssoort aan één teken of één woord: een vraagteken, een uitroepteken, ne … pas, of een conditionnel bij een wens.",
                "Demain staat vooraan en daarna gaat het gewoon verder: je vais. Geen omkering.",
                "Dit is de meest gemaakte fout van Nederlandstaligen in het Frans. Wij draaien om (morgen ga ik), het Frans niet (demain je vais). Lees je eigen zinnen daar één keer apart op na.",
            ],
        ),
        dict(
            aanpak="Een vraag stellen kan op drie manieren, en de omkering is de enige die de woordvolgorde verandert. Let daarbij op het streepje en op de t die er soms tussen schuift.",
            waarom=[
                "De omkering plakt werkwoord en voornaamwoord aan elkaar met een streepje: viens-tu, a-t-elle. Est-ce que laat de zin met rust en is daarom het veiligst.",
                "Travaille eindigt op een klinker en il begint met een klinker, dus komt er een t tussen. Hetzelfde bij a-t-elle en chante-t-on. Staat er al een t of een d op het einde (vient-il, prend-il), dan is die er niet nodig.",
                "Deze zeven vraagwoorden dekken bijna alles. Let op combien, dat de in zich meekrijgt als er een naamwoord op volgt: combien de frères ?",
            ],
        ),
        dict(
            aanpak="Een Franse ontkenning bestaat uit twee stukken die rond de persoonsvorm gaan staan: ne … pas, ne … jamais, ne … plus, ne … rien, ne … personne. Zoek dus eerst de persoonsvorm, en zet die twee stukken eromheen.",
            waarom=[
                "Vier dingen in één rij. Pas wordt vervangen door jamais, plus of rien (nooit twee negatieve woorden samen). Bij een passé composé staan ne en pas rond het hulpwerkwoord. Bij twee werkwoorden rond de persoonsvorm, dus rond vais en niet rond partir. En het lidwoord wordt de.",
                "Alles draait om de persoonsvorm. In j'ai mangé is ai de persoonsvorm en mangé het deelwoord, dus: je n'ai pas mangé. Je n'ai mangé pas bestaat niet.",
                "Een regel die je ook in het hoofdstuk over de lidwoorden tegenkomt: un, une, du, de la en des worden alle vijf de na een ontkenning. Alleen na être blijft het lidwoord staan.",
            ],
        ),
        dict(
            aanpak="Een zin is samengesteld als er twee persoonsvormen in staan. Tel dus persoonsvormen, niet werkwoorden: een infinitief telt niet mee.",
            waarom=[
                "Let op de derde en de vijfde. Je veux partir heeft één persoonsvorm (veux) en dus één zin. Je vais manger et puis je vais dormir heeft er twee (vais en vais), dus is die samengesteld.",
                "Dit is dezelfde manier van tellen als in het Nederlands. Een infinitief hangt aan de persoonsvorm vast en maakt geen eigen zin.",
            ],
        ),
        dict(
            aanpak="Voegwoorden verbinden zinnen, en ze vertellen de lezer wat er komt. Leer ze per betekenis: verbinden (et), tegenstellen (mais), kiezen (ou), gevolg (donc), reden (car, parce que), tijd (quand, pendant que), voorwaarde (si).",
            waarom=[
                "Vier woorden lijken op elkaar en worden verwisseld: ou is of (zonder accent), où is waar (met accent). En car en parce que betekenen allebei want of omdat, zie oefening 15.",
                "Parce qu', want il begint met een klinker. Parce que wordt dan parce qu', net als que in andere zinnen.",
                "Mais verbindt de twee zinnen tot één zin met een komma ervoor. Cependant zou ook kunnen, maar dan blijven het twee zinnen.",
                "Het verschil in de praktijk: car staat altijd tussen twee zinnen in en kan nooit vooraan. Parce que kan wel een zin openen als antwoord op pourquoi: « Pourquoi ? Parce qu'il pleut. »",
            ],
        ),
        dict(
            aanpak="Zinsdelen benoemen lijkt schoolwerk, maar je hebt het nodig zodra je een voornaamwoord wil gebruiken. Zoek eerst de persoonsvorm, dan het onderwerp (wie doet het), dan het COD (wie of wat) en het COI (aan wie).",
            waarom=[
                "Let op het laatste: het onderwerp is les élèves de ma classe, met de hele groep woorden erbij. Daarom staat er travaillent in het meervoud, en niet travaille bij classe.",
                "COD zonder voorzetsel, COI met à. Donner is het schoolvoorbeeld, want het heeft er allebei een: donner quelque chose (COD) à quelqu'un (COI).",
                "Dit is de hele reden waarom je het moet kunnen. Je vois le livre wordt je le vois, maar je parle à Paul wordt je lui parle. Zie je het verschil niet, dan kies je het verkeerde woordje.",
            ],
        ),
        dict(
            aanpak="Zes zinnen, drie soorten overeenkomst. Lees je eigen tekst drie keer na, één keer per soort: eerst alle persoonsvormen bij hun onderwerp, dan alle adjectieven bij hun naamwoord, dan alle deelwoorden met être.",
            waarom=[
                "Les enfants is meervoud, dus jouent. Je hoort het verschil niet, je moet het zien.",
                "De val zit in de woorden tussen het onderwerp en het werkwoord. Het onderwerp is les élèves, niet ma classe. Streep bij twijfel het stuk tussenin weg: les élèves … travaillent.",
                "Twee dingen tegelijk fout. Marie et Paul zijn samen meervoud, dus sont, en omdat partir met être gaat, verandert het deelwoord mee: partis.",
                "Elle is vrouwelijk en partir gaat met être, dus partie met een e.",
                "Vert past zich aan maisons aan: vrouwelijk meervoud, dus eerst een e en dan een s: vertes.",
                "Hier gaat het net niet, want manger gaat met avoir. Vergelijk dit met oefening 22: être verandert mee, avoir niet.",
                "De persoonsvorm met het onderwerp, het adjectief met zijn naamwoord, en het deelwoord met het onderwerp bij être. Die drie staan voor de meeste punten op taalcorrectheid.",
                "En net daarom staat deze reeks op het einde. Je oor helpt je hier niet: il joue en ils jouent klinken gelijk, une maison verte en des maisons vertes ook. Nakijken is kijken, letterlijk.",
            ],
        ),
    ]
)
