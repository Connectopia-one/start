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
