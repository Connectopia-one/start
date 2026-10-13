# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Frans 🚀 Boost doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde stof
met andere vragen, dus gaat dezelfde pdf bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die op het scherm: andere
teksten om te lezen, andere zinnen om aan te vullen, en opdrachten die je enkel
op papier kan maken — een tabel invullen, een zin herschrijven, een mail
uitschrijven. Wie hier iets bijschrijft, legt het eerst naast
`../../boost-doorstroom/frans.json` en naast `maak_frans_boost.py`.

Het niveau is B1, zoals de twee vakfiches van de examencommissie vragen.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-doorstroom". Zonder dat achtervoegsel wint een bundel van Boost
dubbele finaliteit, want die heeft bijna dezelfde titels.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

VAK = "Frans"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
NIVEAU = "-boost-doorstroom"
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
    "Onderstreep wat je niet kent en raad het eerst uit de zin eromheen.",
    "Kom bij elke vraag terug naar de tekst.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

HOE_SCHRIJVEN = [
    "Schrijf eerst in het klad wat je wil zeggen, dan pas op de lijnen.",
    "Tel je woorden: een opdracht met een aantal erbij wordt daarop beoordeeld.",
    "Lees je tekst luidop na. Wat je niet kan voorlezen, loopt niet.",
    "Het antwoordblad zit achteraan. Daar staat een voorbeeldantwoord, niet het enige juiste.",
]

OEFENBUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BOOST)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS[VOOR + slug + NIVEAU] = b


# ============================================================
zet("een-franse-tekst-analyseren",
    titel="Een Franse tekst analyseren",
    onder="Twee teksten en {aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE_LEZEN,
    reeksen=[
        dict(kop="Texte 1", opdracht="Lees deze tekst. De vragen erna gaan alleen hierover.",
             oefeningen=[
                 ("tekst",
                  "<h3 style='margin:0 0 .4em'>La bibliothèque qui prête des outils</h3>"
                  "<p>À Namur, la bibliothèque de la rue Saint-Nicolas ne prête pas seulement "
                  "des livres. Depuis deux ans, on y emprunte aussi une perceuse, une machine à "
                  "coudre ou une tente. „Nous avons commencé avec quarante objets”, explique "
                  "Sophie Lenoir, la responsable. „Aujourd'hui, le catalogue en compte plus de "
                  "six cents.”</p>"
                  "<p>Le principe est simple. On s'inscrit une fois, pour vingt euros par an, et "
                  "on emprunte ensuite trois objets à la fois, pendant deux semaines. Les "
                  "réparations sont payées par la bibliothèque, sauf si l'objet a été clairement "
                  "mal utilisé.</p>"
                  "<p>Le succès s'explique surtout par le prix. Une perceuse coûte environ "
                  "quatre-vingts euros à l'achat, et la plupart des gens s'en servent moins "
                  "d'une heure par an. Toutefois, tout ne s'emprunte pas aussi bien: les "
                  "appareils de cuisine reviennent souvent sales, et certains objets, comme les "
                  "échelles, prennent beaucoup de place pour peu de demandes.</p>"
                  "<p>D'autres villes wallonnes suivent le mouvement. „On nous appelle de "
                  "partout”, dit madame Lenoir. „Mon conseil est toujours le même: commencez "
                  "petit, et écoutez ce que les gens demandent vraiment.”</p>"),
             ]),
        dict(kop="Het onderwerp en de hoofdgedachte",
             opdracht="Antwoord in het Nederlands, tenzij er iets anders staat.",
             oefeningen=[
                 ("kort", "Schrijf het onderwerp van de tekst in enkele woorden.",
                  "een bibliotheek die ook gereedschap uitleent", WL),
                 ("open", "Wat is de hoofdgedachte van de tekst? Eén zin.",
                  "Een bibliotheek in Namen leent naast boeken ook voorwerpen uit, wat vooral "
                  "lukt omdat mensen die dingen te weinig gebruiken om ze zelf te kopen.", 3),
                 ("kort", "Hoeveel voorwerpen staan er nu in de catalogus?",
                  "meer dan zeshonderd", W),
                 ("kort", "Hoeveel kost het lidmaatschap per jaar?", "twintig euro", W),
                 ("kort", "Hoeveel voorwerpen mag je tegelijk lenen?", "drie", W),
             ]),
        dict(kop="De hoofdpunten uit de tekst halen",
             opdracht="Zoek het antwoord in de tekst terug.",
             oefeningen=[
                 ("open", "Waarom lukt het uitlenen van een boormachine zo goed? "
                          "Geef de twee redenen uit de tekst.",
                  "Een boormachine kost ongeveer tachtig euro, en de meeste mensen gebruiken "
                  "er minder dan een uur per jaar.", 3),
                 ("open", "Welke twee moeilijkheden noemt de tekst?",
                  "Keukentoestellen komen vaak vuil terug, en voorwerpen zoals ladders nemen "
                  "veel plaats in terwijl er weinig vraag naar is.", 3),
                 ("kort", "Wie betaalt een herstelling?", "de bibliotheek", W),
                 ("open", "In welk geval betaalt de bibliotheek de herstelling níét?",
                  "Als het voorwerp duidelijk verkeerd gebruikt is.", 2),
                 ("open", "Welke raad geeft mevrouw Lenoir aan andere steden?",
                  "Klein beginnen, en luisteren naar wat de mensen echt vragen.", 2),
                 ("waar", "Volgens de tekst leent de bibliotheek geen boeken meer uit.", False),
             ]),
        dict(kop="Woorden raden uit de tekst",
             opdracht="Gebruik de zin eromheen. Sla je woordenboek pas daarna open.",
             oefeningen=[
                 ("rij", [("emprunter", "lenen / ontlenen"),
                          ("une perceuse", "een boormachine"),
                          ("la responsable", "de verantwoordelijke"),
                          ("toutefois", "nochtans / toch"),
                          ("une échelle", "een ladder"),
                          ("un conseil", "een raad / een tip")],
                  "Wat betekent dit woord in de tekst?", WW),
                 ("open", "„On nous appelle de partout.” Wie is 'on' in deze zin?",
                  "De mensen uit andere steden die ook zo'n uitleendienst willen beginnen.", 2),
                 ("kies", "„Le succès s'explique surtout par le prix.” Wat betekent "
                          "<em>surtout</em> hier?",
                  ["vooral", "overal", "zeker niet", "ongeveer"], 0),
             ]),
        dict(kop="Texte 2",
             opdracht="Een korte tekst van een ander soort. Lees eerst, antwoord daarna.",
             oefeningen=[
                 ("tekst",
                  "<div style='border:1px solid #999;padding:.6em .8em'>"
                  "<p style='margin:0 0 .3em'><strong>AVIS AUX HABITANTS</strong></p>"
                  "<p style='margin:0 0 .3em'>En raison de travaux à la conduite d'eau, la rue "
                  "des Tilleuls sera fermée à la circulation du lundi 6 au vendredi 17 avril, "
                  "de 7h à 18h.</p>"
                  "<p style='margin:0 0 .3em'>Les riverains peuvent sortir à pied. Le ramassage "
                  "des déchets se fera le mercredi au coin de la place du Marché, et non devant "
                  "les maisons.</p>"
                  "<p style='margin:0'>Merci de votre compréhension. — Le collège communal</p>"
                  "</div>"),
                 ("kort", "Wat voor soort tekst is dit?", "een bericht / een bekendmaking", WL),
                 ("kort", "Waarom is de straat dicht?",
                  "door werken aan de waterleiding", WL),
                 ("kort", "Op welke dag moet het afval buiten?", "op woensdag", W),
                 ("open", "Waar moeten de bewoners hun afval zetten, en waar níét?",
                  "Op de hoek van het Marktplein, en niet meer voor hun huis.", 2),
                 ("waar", "De bewoners mogen tussen 7 en 18 uur met de auto door de straat.",
                  False),
                 ("kort", "Wie heeft dit bericht geschreven?",
                  "het gemeentebestuur / het schepencollege", WL),
             ]),
        dict(kop="Hoe je een onbekende tekst aanpakt",
             opdracht="Deze vragen gaan over je werkwijze, niet over één tekst.",
             oefeningen=[
                 ("open", "Je krijgt op het examen een tekst waarvan je de helft van de woorden "
                          "niet kent. Wat doe je als eerste?",
                  "Eerst de hele tekst doorlezen zonder te stoppen, en kijken waarover hij "
                  "ongeveer gaat. Pas daarna de vragen lezen en gericht terugzoeken.", 3),
                 ("open", "Waaraan zie je, nog voor je leest, of een tekst informeert, "
                          "overtuigt of iets uitlegt?",
                  "Aan de vorm: titel en tussentitels, een kader, een afzender, de lengte van "
                  "de zinnen, en of er cijfers of meningen in staan.", 3),
                 ("kies", "Je moet de hoofdgedachte van een tekst geven. Wat is dat?",
                  ["de boodschap van de hele tekst in één zin",
                   "de eerste zin van de tekst",
                   "het woord dat het vaakst terugkomt",
                   "de mening van de schrijver over zichzelf"], 0),
             ]),
    ])


# ============================================================
zet("tekstsoorten-tekstverbanden-en-verwijswoorden",
    titel="Tekstsoorten, tekstverbanden en verwijswoorden",
    hoe=HOE_LEZEN,
    reeksen=[
        dict(kop="Welke tekstsoort is dit?",
             opdracht="Schrijf de soort erbij: een bericht, een verhaal, een briefwisseling, "
                      "een artikel, een reclame of een gebruiksaanwijzing.",
             oefeningen=[
                 ("kort", "„Mélangez la farine et le beurre. Ajoutez ensuite deux œufs et "
                          "laissez reposer la pâte pendant trente minutes.”",
                  "een gebruiksaanwijzing / een recept", WL),
                 ("kort", "„Chère Madame, je vous écris au sujet de la facture du 3 mars, qui "
                          "ne correspond pas à ma commande.”",
                  "een briefwisseling / een brief", WL),
                 ("kort", "„Ce soir-là, Julien ne savait pas encore que la lettre allait tout "
                          "changer. Il la posa sur la table et sortit.”",
                  "een verhaal", WL),
                 ("kort", "„–40 % sur tout le rayon jardin, ce week-end seulement!”",
                  "een reclame", WL),
                 ("kort", "„Le conseil communal informe les habitants que la piscine sera "
                          "fermée du 2 au 9 mai.”",
                  "een bericht / een bekendmaking", WL),
                 ("kort", "„Selon une étude de l'université de Liège, un jeune sur trois dort "
                          "moins de sept heures par nuit.”",
                  "een artikel", WL),
             ]),
        dict(kop="Waaraan herken je het?",
             opdracht="Antwoord in het Nederlands.",
             oefeningen=[
                 ("open", "Noem twee dingen waaraan je een gebruiksaanwijzing herkent, "
                          "nog voor je de inhoud leest.",
                  "Aan de genummerde of opgesomde stappen en aan de werkwoorden in de gebiedende "
                  "wijs (mélangez, ajoutez).", 3),
                 ("open", "Waaraan zie je het verschil tussen een artikel en een reclame "
                          "over hetzelfde product?",
                  "Een artikel geeft cijfers en bronnen en laat beide kanten zien; een reclame "
                  "noemt alleen voordelen, spreekt je rechtstreeks aan en wil dat je koopt.", 3),
                 ("waar", "Een brief en een mail zijn allebei briefwisseling.", True),
             ]),
        dict(kop="Het juiste signaalwoord",
             opdracht="Vul het signaalwoord in dat het verband legt dat tussen haakjes staat.",
             oefeningen=[
                 ("rij", [("Il pleut, ___ je prends mon parapluie. (gevolg)", "donc"),
                          ("Je suis fatigué ___ j'ai mal dormi. (oorzaak)", "parce que"),
                          ("___ le froid, le match a eu lieu. (toegeving)", "Malgré"),
                          ("Elle aime le thé, ___ son frère préfère le café. (tegenstelling)",
                           "tandis que / alors que"),
                          ("___, nous allons voir les chiffres. (volgorde)", "D'abord"),
                          ("___ nous avons visité le musée. (volgorde)", "Ensuite")],
                  "Welk woord hoort in de leegte?", WW),
                 ("kies", "„Le train avait du retard. <u>Pourtant</u>, elle est arrivée à "
                          "l'heure.” Welk verband legt <em>pourtant</em>?",
                  ["een tegenstelling", "een gevolg", "een oorzaak", "een opsomming"], 0),
                 ("kies", "„Il n'a pas étudié, <u>c'est pourquoi</u> il a raté.” Welk verband "
                          "legt <em>c'est pourquoi</em>?",
                  ["een gevolg", "een tegenstelling", "een voorwaarde", "een vergelijking"], 0),
                 ("open", "Schrijf twee zinnen over je eigen week: één met <em>d'abord</em> en "
                          "één met <em>enfin</em>.",
                  "Bijvoorbeeld: D'abord, j'ai fait mes devoirs. Enfin, j'ai regardé un film.", 3),
             ]),
        dict(kop="Waarnaar verwijst dat woordje?",
             opdracht="Schrijf op naar welk woord of welke woordgroep uit de zin verwezen wordt.",
             oefeningen=[
                 ("rij", [("Marie a acheté un vélo. <u>Il</u> est rouge.", "le vélo"),
                          ("Les voisins sont partis. <u>Ils</u> reviennent lundi.",
                           "les voisins"),
                          ("J'ai lu ton message. Je <u>le</u> trouve clair.", "ton message"),
                          ("Nous allons à Gand. J'<u>y</u> vais chaque mois.", "à Gand"),
                          ("Tu as du pain? Oui, j'<u>en</u> ai.", "du pain"),
                          ("Le prof a parlé aux élèves et <u>leur</u> a donné un délai.",
                           "aux élèves")],
                  "Waarnaar verwijst het onderstreepte woord?", WW),
                 ("open", "„Les deux sœurs travaillent à l'hôpital. <u>Celle-ci</u> est "
                          "infirmière, <u>celle-là</u> est médecin.” Leg uit welk verschil er "
                          "zit tussen <em>celle-ci</em> en <em>celle-là</em>.",
                  "Celle-ci wijst naar de laatstgenoemde en celle-là naar de eerstgenoemde.", 3),
                 ("waar", "<em>Y</em> vervangt meestal een persoon.", False),
             ]),
        dict(kop="De draad van een alinea",
             opdracht="Lees en antwoord in het Nederlands.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Beaucoup de jeunes travaillent le samedi. D'abord, cela donne un peu "
                  "d'argent de poche. Ensuite, on apprend à être à l'heure et à parler aux "
                  "clients. Cependant, un job qui dure trop longtemps pèse sur les études: "
                  "selon une enquête récente, un élève sur cinq travaille plus de dix heures "
                  "par semaine. C'est pourquoi plusieurs écoles conseillent de rester sous "
                  "cette limite.</em></p>"),
                 ("open", "Welke twee voordelen noemt de tekst?",
                  "Je verdient wat zakgeld, en je leert op tijd komen en met klanten praten.", 2),
                 ("kort", "Welk signaalwoord kondigt het nadeel aan?", "cependant", W),
                 ("kort", "Welk signaalwoord kondigt het gevolg aan?", "c'est pourquoi", W),
                 ("open", "„...de rester sous <u>cette limite</u>.” Welke grens is dat?",
                  "Tien uur werken per week.", 2),
             ]),
    ])


# ============================================================
zet("de-franstalige-wereld-omgangsvormen-en-gewoontes",
    titel="De Franstalige wereld: omgangsvormen en gewoontes",
    reeksen=[
        dict(kop="Tutoyer of vouvoyer?",
             opdracht="Schrijf <em>tu</em> of <em>vous</em> op, en daarachter in één woord waarom.",
             oefeningen=[
                 ("rij", [("tegen een klasgenoot", "tu — leeftijdgenoot"),
                          ("tegen de directeur van je stageplaats", "vous — formeel"),
                          ("tegen een onbekende in de winkel", "vous — onbekend"),
                          ("tegen je neef van tien", "tu — familie"),
                          ("tegen twee vrienden samen", "vous — meervoud"),
                          ("tegen een leeftijdgenoot op een forum", "tu — leeftijdgenoot")],
                  "Welke aanspreekvorm gebruik je?", WW),
                 ("open", "Waarom is <em>vous</em> in het Frans soms meervoud en soms beleefd? "
                          "Hoe weet je welk van de twee bedoeld is?",
                  "De vorm is dezelfde; je leidt het af uit de situatie en soms uit het "
                  "bijvoeglijk naamwoord: vous êtes prêt richt zich tot één persoon, "
                  "vous êtes prêts tot meerdere.", 3),
                 ("waar", "Als iemand jou met <em>tu</em> aanspreekt, mag je altijd meteen "
                          "terug tutoyeren.", True),
             ]),
        dict(kop="Wat zeg je in deze situatie?",
             opdracht="Schrijf de Franse uitdrukking op.",
             oefeningen=[
                 ("rij", [("Je komt een winkel binnen.", "Bonjour"),
                          ("Je wil langs iemand in de bus.", "Pardon / Excusez-moi"),
                          ("Iemand bedankt je.", "De rien / Je vous en prie"),
                          ("Je neemt afscheid 's avonds.", "Bonne soirée / Bonne nuit"),
                          ("Je vraagt beleefd om een brood.", "Je voudrais un pain, s'il vous plaît"),
                          ("Je biedt je excuses aan voor een fout.", "Je suis désolé(e)")],
                  "Wat zeg je?", WW),
                 ("open", "In Frankrijk zegt bijna iedereen <em>bonjour</em> bij het "
                          "binnenkomen van een kleine winkel. Wat gebeurt er als je dat niet doet?",
                  "Dat wordt als onbeleefd gezien; de verkoper helpt je vaak pas nadat je "
                  "gegroet hebt.", 2),
             ]),
        dict(kop="Waar spreekt men Frans?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["land of gebied", "werelddeel"],
                  [["la Belgique", None], ["le Québec", None], ["le Sénégal", None],
                   ["la Suisse", None], ["la Martinique", None], ["le Maroc", None]],
                  "België: Europa · Québec: Noord-Amerika · Senegal: Afrika · "
                  "Zwitserland: Europa · Martinique: Midden-Amerika (de Antillen) · "
                  "Marokko: Afrika", "150px"),
                 ("kort", "Hoeveel landen hebben het Frans als officiële taal, ongeveer?",
                  "ongeveer dertig", W),
                 ("open", "Noem twee verschillen tussen het Frans van België en dat van "
                          "Frankrijk.",
                  "België zegt septante en nonante waar Frankrijk soixante-dix en "
                  "quatre-vingt-dix zegt, en gebruikt woorden als une farde en un GSM.", 3),
                 ("rij", [("septante", "70"), ("nonante", "90"),
                          ("quatre-vingts", "80"), ("soixante-dix", "70"),
                          ("quatre-vingt-dix", "90"), ("huitante (Zwitserland)", "80")],
                  "Welk getal is dit?", "90px"),
             ]),
        dict(kop="Gewoontes en feesten",
             opdracht="Antwoord in het Nederlands.",
             oefeningen=[
                 ("kort", "Wanneer is de nationale feestdag van Frankrijk?", "14 juli", W),
                 ("kort", "Wanneer is de nationale feestdag van België?", "21 juli", W),
                 ("kort", "Hoe heet het Franse eindexamen van het secundair?",
                  "le baccalauréat / le bac", WL),
                 ("open", "Een Franse familie nodigt je uit om 20 uur te eten. Wat neem je mee "
                          "en hoe laat kom je aan?",
                  "Een kleinigheid zoals bloemen, chocolade of een fles; en je komt niet te "
                  "vroeg, eerder een kwartiertje later dan het uur.", 3),
                 ("waar", "In Frankrijk krijg je bij de maaltijd meestal eerst de kaas en "
                          "daarna het dessert.", True),
             ]),
        dict(kop="Beleefd of te direct?",
             opdracht="Herschrijf de zin beleefder in het Frans.",
             oefeningen=[
                 ("open", "<em>Donnez-moi l'adresse.</em>",
                  "Pourriez-vous me donner l'adresse, s'il vous plaît?", 2),
                 ("open", "<em>Je veux parler au responsable.</em>",
                  "Je voudrais parler au responsable, s'il vous plaît.", 2),
                 ("open", "<em>C'est faux.</em> (je spreekt een leerkracht tegen)",
                  "Excusez-moi, mais je ne suis pas tout à fait d'accord.", 2),
                 ("open", "<em>Répétez.</em>",
                  "Pourriez-vous répéter, s'il vous plaît?", 2),
             ]),
    ])


# ============================================================
zet("schrijven-schriftelijke-interactie-en-leesbeleving",
    titel="Schrijven, schriftelijke interactie en leesbeleving",
    hoe=HOE_SCHRIJVEN,
    reeksen=[
        dict(kop="De juiste aanhef en slotformule",
             opdracht="Schrijf op wat je gebruikt.",
             oefeningen=[
                 ("rij", [("een mail aan een onbekend bedrijf", "Madame, Monsieur,"),
                          ("een mail aan mevrouw Dubois, die je kent",
                           "Chère Madame Dubois, / Bonjour Madame Dubois,"),
                          ("een bericht aan een vriend", "Salut Lucas,"),
                          ("het slot van een formele mail",
                           "Cordialement / Veuillez agréer mes salutations distinguées"),
                          ("het slot van een bericht aan een vriend", "À bientôt / Bises"),
                          ("een klacht aan een winkel", "Madame, Monsieur,")],
                  "Wat schrijf je?", WW),
                 ("waar", "Je begint een formele Franse mail met <em>Cher Monsieur Dupont</em> "
                          "als je de persoon niet kent.", False),
             ]),
        dict(kop="Een mail van zestig woorden",
             opdracht="Schrijf in het Frans. Tel je woorden en zet het aantal erbij.",
             oefeningen=[
                 ("open", "Je hebt online een trui besteld. Je kreeg de verkeerde maat. "
                          "Schrijf een mail aan de winkel: zeg wat je bestelde, wat er fout is, "
                          "en wat je wil. Ongeveer zestig woorden.",
                  "Madame, Monsieur, J'ai commandé un pull bleu en taille M le 3 octobre "
                  "(commande 4471). J'ai reçu un pull en taille S, que je ne peux pas porter. "
                  "Je vous renvoie l'article aujourd'hui et je voudrais recevoir la bonne "
                  "taille, ou être remboursé si elle n'est plus disponible. Pourriez-vous me "
                  "confirmer par mail? Je vous remercie d'avance. Cordialement, ...", 9),
                 ("open", "Je kan niet naar de verjaardag van je Franse vriendin komen. "
                          "Schrijf haar een bericht van ongeveer veertig woorden: bedanken, "
                          "uitleggen waarom, en iets voorstellen.",
                  "Salut Léa, merci beaucoup pour ton invitation! Malheureusement, je ne peux "
                  "pas venir samedi: je travaille tout le week-end au magasin. Je suis vraiment "
                  "déçue. Est-ce qu'on pourrait se voir le mercredi d'après? Je t'offre un "
                  "verre. Bises, ...", 7),
             ]),
        dict(kop="Van spreektaal naar schrijftaal",
             opdracht="Herschrijf de zin zoals ze in een formele mail hoort.",
             oefeningen=[
                 ("open", "<em>J'ai pas reçu le colis.</em>",
                  "Je n'ai pas reçu le colis.", 2),
                 ("open", "<em>Vous pouvez me dire quand ça arrive?</em>",
                  "Pourriez-vous me dire quand le colis arrivera?", 2),
                 ("open", "<em>C'est nul, votre service.</em>",
                  "Je suis déçu du service et je souhaite une solution.", 2),
                 ("open", "<em>Faut que je parte avant 16h.</em>",
                  "Il faut que je parte avant 16 heures.", 2),
             ]),
        dict(kop="Een tekst verbeteren",
             opdracht="In elke zin staat één fout. Schrijf de zin juist over.",
             oefeningen=[
                 ("open", "<em>Je suis allé à la gare et j'ai prendre le train.</em>",
                  "Je suis allé à la gare et j'ai pris le train.", 2),
                 ("open", "<em>Nous avons visité une grande musée.</em>",
                  "Nous avons visité un grand musée.", 2),
                 ("open", "<em>Elle est arrivé en retard.</em>",
                  "Elle est arrivée en retard.", 2),
                 ("open", "<em>Je ne mange pas de la viande.</em>",
                  "Je ne mange pas de viande.", 2),
                 ("open", "<em>Il m'a dit que il viendra demain.</em>",
                  "Il m'a dit qu'il viendrait demain.", 2),
             ]),
        dict(kop="Leesbeleving",
             opdracht="Lees het fragment en antwoord in het Nederlands.",
             oefeningen=[
                 ("tekst",
                  "<p><em>„Le dernier jour, Hugo a laissé la clé sous le pot de fleurs, comme "
                  "toujours. Il a regardé la maison une dernière fois. Les volets étaient "
                  "fermés, le jardin déjà plus haut que lui. Il n'a pas pleuré. Il a seulement "
                  "pensé qu'il faudrait revenir couper l'herbe.”</em></p>"),
                 ("open", "Welk gevoel roept dit fragment op? Noem het en zeg waaraan je dat "
                          "merkt.",
                  "Afscheid en verdriet dat niet uitgesproken wordt: hij huilt niet, maar denkt "
                  "aan het gras — een klein, dagelijks ding in plaats van het grote gevoel.", 3),
                 ("open", "Waarom staat er dat het gras al hoger was dan hij?",
                  "Het laat zien dat het huis al een tijd leegstaat en dat niemand er nog voor "
                  "zorgt.", 2),
                 ("kies", "Welke zin past het best bij de toon van het fragment?",
                  ["ingehouden en droevig", "vrolijk en snel",
                   "spannend en dreigend", "zakelijk en koel"], 0),
                 ("open", "Zou je dit boek verder lezen? Geef in het Frans één zin met je "
                          "mening en een reden.",
                  "Bijvoorbeeld: Oui, j'aimerais lire la suite, parce que je veux savoir "
                  "pourquoi il part.", 2),
             ]),
    ])


# ============================================================
zet("woordvelden-mens-gezondheid-en-het-dagelijkse-leven",
    titel="Woordvelden: mens, gezondheid en het dagelijkse leven",
    reeksen=[
        dict(kop="Het lichaam",
             opdracht="Vertaal naar het Frans, met het lidwoord erbij.",
             oefeningen=[
                 ("rij", [("het hoofd", "la tête"), ("de keel", "la gorge"),
                          ("de rug", "le dos"), ("de knie", "le genou"),
                          ("de schouder", "l'épaule (v)"), ("de buik", "le ventre")],
                  "Hoe zeg je dat in het Frans?", WW),
                 ("rij", [("l'estomac", "de maag"), ("la cheville", "de enkel"),
                          ("le poignet", "de pols"), ("la peau", "de huid"),
                          ("le cœur", "het hart"), ("les poumons", "de longen")],
                  "Wat betekent dit in het Nederlands?", WW),
             ]),
        dict(kop="Bij de dokter",
             opdracht="Vul de zin aan of antwoord in het Frans.",
             oefeningen=[
                 ("kort", "Hoe zeg je „ik heb keelpijn”?", "J'ai mal à la gorge", WL),
                 ("kort", "Hoe zeg je „ik ben verkouden”?", "Je suis enrhumé(e)", WL),
                 ("kort", "Hoe zeg je „ik heb koorts”?", "J'ai de la fièvre", WL),
                 ("open", "De dokter vraagt <em>Depuis quand?</em> Antwoord dat het sinds "
                          "eergisteren is.",
                  "Depuis avant-hier.", 2),
                 ("open", "Schrijf twee zinnen waarmee je een afspraak maakt bij de dokter, "
                          "per telefoon.",
                  "Bonjour, je voudrais prendre rendez-vous, s'il vous plaît. Est-ce que vous "
                  "avez quelque chose cette semaine, de préférence l'après-midi?", 3),
                 ("waar", "<em>Une ordonnance</em> is het briefje waarmee je medicijnen "
                          "gaat halen.", True),
             ]),
        dict(kop="Eten en de winkel",
             opdracht="Zet elk woord in de juiste kolom.",
             oefeningen=[
                 ("tabel", ["woord", "winkel of soort"],
                  [["le pain", None], ["la viande", None], ["les fraises", None],
                   ["le fromage", None], ["le cabillaud", None], ["les haricots", None]],
                  "pain: boulangerie (brood) · viande: boucherie (vlees) · "
                  "fraises: fruit · fromage: zuivel · cabillaud: poissonnerie (vis) · "
                  "haricots: groenten", "160px"),
                 ("rij", [("un kilo de pommes", "een kilo appels"),
                          ("une tranche de jambon", "een sneetje ham"),
                          ("une bouteille d'eau", "een fles water"),
                          ("un morceau de fromage", "een stuk kaas"),
                          ("une douzaine d'œufs", "een dozijn eieren"),
                          ("un paquet de riz", "een pak rijst")],
                  "Wat betekent dit?", WW),
                 ("open", "Waarom staat er <em>de</em> zonder lidwoord in "
                          "<em>un kilo de pommes</em>?",
                  "Na een maat of hoeveelheid komt altijd de zonder lidwoord: un kilo de, "
                  "beaucoup de, une tranche de.", 2),
             ]),
        dict(kop="Kleren en kleuren",
             opdracht="Vul in. Let op de uitgang van het bijvoeglijk naamwoord.",
             oefeningen=[
                 ("rij", [("une robe (vert)", "verte"), ("des chaussures (noir)", "noires"),
                          ("un manteau (gris)", "gris"), ("des gants (marron)", "marron"),
                          ("une veste (orange)", "orange"), ("des pulls (bleu)", "bleus")],
                  "Welke vorm hoort hier?", "120px"),
                 ("open", "Waarom blijft <em>marron</em> onveranderd en <em>vert</em> niet?",
                  "Marron is eigenlijk de naam van een ding, een kastanje, en zulke kleuren "
                  "veranderen nooit van vorm. Vert is een gewoon bijvoeglijk naamwoord.", 3),
                 ("kort", "Hoe zeg je „ik draag een jas”?", "Je porte un manteau", WL),
             ]),
        dict(kop="De dag van Camille",
             opdracht="Vul het ontbrekende woord in.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Camille se ___(1) à sept heures. Elle prend une ___(2) et "
                  "s'habille. À huit heures, elle ___(3) son petit-déjeuner: du pain et du "
                  "café. Elle ___(4) le bus de huit heures vingt. Le soir, elle ___(5) à la "
                  "maison vers six heures et ___(6) le repas avec sa sœur.</em></p>"),
                 ("rij", [("1", "lève"), ("2", "douche"), ("3", "prend"),
                          ("4", "prend / attend"), ("5", "rentre"), ("6", "prépare")],
                  "Welk woord hoort op die plaats?", "130px"),
                 ("open", "Schrijf drie zinnen over je eigen ochtend, in het Frans, met "
                          "<em>d'abord</em>, <em>ensuite</em> en <em>enfin</em>.",
                  "Bijvoorbeeld: D'abord, je me lève à six heures et demie. Ensuite, je prends "
                  "une douche et je déjeune. Enfin, je pars à l'école à sept heures et quart.", 4),
             ]),
    ])


# ============================================================
zet("woordvelden-school-werk-reizen-en-de-samenleving",
    titel="Woordvelden: school, werk, reizen en de samenleving",
    reeksen=[
        dict(kop="Op school",
             opdracht="Vertaal, met lidwoord waar het kan.",
             oefeningen=[
                 ("rij", [("het rapport", "le bulletin"), ("het lesuur", "l'heure de cours"),
                          ("de leerkracht", "le professeur / la professeure"),
                          ("een toets", "un contrôle / une interrogation"),
                          ("het huiswerk", "les devoirs"), ("de speeltijd", "la récréation")],
                  "Hoe zeg je dat in het Frans?", WW),
                 ("rij", [("réussir", "slagen"), ("rater / échouer", "buizen"),
                          ("une note", "een punt / een cijfer"),
                          ("la cantine", "de refter"), ("le stage", "de stage"),
                          ("un horaire", "een uurrooster")],
                  "Wat betekent dit?", WW),
             ]),
        dict(kop="Werk en solliciteren",
             opdracht="Antwoord in het Frans.",
             oefeningen=[
                 ("kort", "Hoe heet een vakantiejob?", "un job d'été / un job de vacances", WL),
                 ("kort", "Hoe heet een sollicitatiebrief?", "une lettre de motivation", WL),
                 ("kort", "Hoe heet een sollicitatiegesprek?", "un entretien d'embauche", WL),
                 ("open", "Schrijf twee zinnen waarin je in het Frans zegt waarom jij geschikt "
                          "bent voor een job in een winkel.",
                  "Je suis ponctuel et j'aime le contact avec les clients. J'ai déjà travaillé "
                  "deux étés dans une boulangerie, donc je connais la caisse.", 3),
                 ("rij", [("un salaire", "een loon"), ("un contrat", "een contract"),
                          ("un employeur", "een werkgever"),
                          ("une candidature", "een sollicitatie"),
                          ("à temps partiel", "deeltijds"), ("licencier", "ontslaan")],
                  "Wat betekent dit?", WW),
             ]),
        dict(kop="Reizen en onderweg",
             opdracht="Vul in of vertaal.",
             oefeningen=[
                 ("rij", [("een enkele reis", "un aller simple"),
                          ("een heen-en-terugticket", "un aller-retour"),
                          ("het perron", "le quai"), ("de vertraging", "le retard"),
                          ("overstappen", "changer"), ("de bagage", "les bagages")],
                  "Hoe zeg je dat in het Frans?", WW),
                 ("open", "Vraag aan het loket beleefd een heen-en-terugticket naar Rijsel "
                          "voor zaterdag.",
                  "Bonjour, je voudrais un aller-retour pour Lille pour samedi, s'il vous "
                  "plaît.", 2),
                 ("open", "Je trein heeft een uur vertraging. Vraag in het Frans wat je moet "
                          "doen en of je geld terugkrijgt.",
                  "Excusez-moi, mon train a une heure de retard. Qu'est-ce que je dois faire? "
                  "Est-ce que je peux être remboursé?", 3),
                 ("waar", "<em>Le quai</em> betekent het loket.", False),
             ]),
        dict(kop="De samenleving",
             opdracht="Zet het woord bij de juiste omschrijving.",
             oefeningen=[
                 ("rij", [("le chômage", "de werkloosheid"),
                          ("une élection", "een verkiezing"),
                          ("le réchauffement climatique", "de opwarming van het klimaat"),
                          ("le recyclage", "de recyclage"),
                          ("les transports en commun", "het openbaar vervoer"),
                          ("une association", "een vereniging")],
                  "Wat betekent dit?", WW),
                 ("open", "Geef in het Frans je mening over het openbaar vervoer in je buurt, "
                          "in twee zinnen, met een reden.",
                  "À mon avis, les bus ne passent pas assez souvent le soir. C'est dommage, "
                  "parce que beaucoup de jeunes n'ont pas encore de voiture.", 3),
                 ("kort", "Hoe begin je een mening in het Frans, met drie woorden?",
                  "À mon avis / Je pense que", WL),
             ]),
        dict(kop="Een advertentie lezen",
             opdracht="Lees en antwoord in het Nederlands.",
             oefeningen=[
                 ("tekst",
                  "<div style='border:1px solid #999;padding:.6em .8em'>"
                  "<p style='margin:0 0 .3em'><strong>Magasin Le Panier — étudiant(e) "
                  "le samedi</strong></p>"
                  "<p style='margin:0 0 .3em'>Nous cherchons un(e) étudiant(e) pour la mise en "
                  "rayon et la caisse, le samedi de 9h à 17h30, avec une pause d'une heure. "
                  "Expérience non exigée, formation assurée le premier jour.</p>"
                  "<p style='margin:0'>Envoyez votre candidature avant le 20 mai à "
                  "emploi@lepanier.be. Entretiens la dernière semaine de mai.</p></div>"),
                 ("kort", "Hoeveel uren werk je per zaterdag, pauze niet meegerekend?",
                  "zeven en een half uur", W),
                 ("kort", "Is ervaring nodig?", "nee", W),
                 ("kort", "Tegen wanneer moet je solliciteren?", "voor 20 mei", W),
                 ("open", "Welke twee taken staan in de advertentie?",
                  "De rekken vullen en aan de kassa staan.", 2),
                 ("open", "Schrijf de eerste twee zinnen van je sollicitatiemail in het Frans.",
                  "Madame, Monsieur, J'ai lu votre annonce pour un job d'étudiant le samedi et "
                  "je souhaite poser ma candidature. Je suis élève en cinquième année et je "
                  "suis libre tous les samedis.", 4),
             ]),
    ])


# ============================================================
zet("zelfstandige-naamwoorden-lidwoorden-en-determinanten",
    titel="Zelfstandige naamwoorden, lidwoorden en determinanten",
    reeksen=[
        dict(kop="Welk lidwoord?",
             opdracht="Vul <em>le</em>, <em>la</em>, <em>l'</em> of <em>les</em> in.",
             oefeningen=[
                 ("rij", [("___ maison", "la"), ("___ garçon", "le"),
                          ("___ école", "l'"), ("___ enfants", "les"),
                          ("___ problème", "le"), ("___ liberté", "la")],
                  "Welk bepaald lidwoord hoort erbij?", "80px"),
                 ("open", "Waarom staat er <em>l'</em> voor <em>école</em> en niet "
                          "<em>la</em>?",
                  "Omdat het woord met een klinker begint; la en le worden dan l'. Het woord "
                  "blijft wel vrouwelijk.", 2),
             ]),
        dict(kop="Bepaald, onbepaald of delend",
             opdracht="Vul in en schrijf erbij welke soort het is.",
             oefeningen=[
                 ("rij", [("Je mange ___ pain. (een deel)", "du — delend"),
                          ("J'achète ___ voiture. (één, onbepaald)", "une — onbepaald"),
                          ("___ soleil brille. (bekend)", "Le — bepaald"),
                          ("Elle boit ___ eau. (een deel)", "de l' — delend"),
                          ("Nous avons ___ amis en France.", "des — onbepaald"),
                          ("Je n'ai pas ___ argent.", "d' — na een ontkenning")],
                  "Wat hoort in de leegte?", WW),
                 ("open", "Leg uit waarom <em>du pain</em> na een ontkenning <em>de pain</em> "
                          "wordt.",
                  "Na een ontkenning verdwijnt het delend lidwoord en blijft alleen de of d' "
                  "over: je mange du pain wordt je ne mange pas de pain.", 3),
                 ("waar", "Na <em>beaucoup</em> komt altijd <em>de</em> zonder lidwoord.", True),
             ]),
        dict(kop="Mannelijk of vrouwelijk, enkelvoud of meervoud",
             opdracht="Zet het woord in het meervoud.",
             oefeningen=[
                 ("rij", [("un journal", "des journaux"), ("un cheval", "des chevaux"),
                          ("un œil", "des yeux"), ("un gâteau", "des gâteaux"),
                          ("un prix", "des prix"), ("un travail", "des travaux")],
                  "Wat is het meervoud?", WW),
                 ("open", "Waarom verandert <em>un prix</em> niet in het meervoud?",
                  "Een woord dat al op s, x of z eindigt, krijgt er in het meervoud niets bij.", 2),
                 ("rij", [("un acteur", "une actrice"), ("un boulanger", "une boulangère"),
                          ("un infirmier", "une infirmière"), ("un professeur", "une professeure"),
                          ("un chanteur", "une chanteuse"), ("un élève", "une élève")],
                  "Wat is de vrouwelijke vorm?", WW),
             ]),
        dict(kop="Bezit en aanwijzen",
             opdracht="Vul het juiste woordje in.",
             oefeningen=[
                 ("rij", [("___ sœur (van mij)", "ma"), ("___ amie (van mij)", "mon"),
                          ("___ parents (van jou)", "tes"), ("___ voiture (van hem)", "sa"),
                          ("___ livre (dit, hier)", "ce"), ("___ maison (deze)", "cette")],
                  "Welk woordje hoort erbij?", "90px"),
                 ("open", "Waarom staat er <em>mon amie</em> en niet <em>ma amie</em>, "
                          "terwijl <em>amie</em> vrouwelijk is?",
                  "Voor een vrouwelijk woord dat met een klinker begint, gebruik je mon, ton of "
                  "son, omdat ma amie moeilijk uit te spreken is.", 3),
                 ("open", "<em>Sa voiture</em> kan twee dingen betekenen. Welke?",
                  "Zijn auto of haar auto: het Frans richt zich naar het bezit, niet naar de "
                  "bezitter.", 2),
             ]),
        dict(kop="Tout, chaque en de rangtelwoorden",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("___ le monde (iedereen)", "tout"), ("___ la journée", "toute"),
                          ("___ les jours", "tous"), ("___ les semaines", "toutes"),
                          ("___ élève (elke)", "chaque"), ("le ___ étage (1ste)", "premier")],
                  "Wat hoort in de leegte?", "100px"),
                 ("kort", "Hoe zeg je „de tweede keer”?", "la deuxième fois", WL),
                 ("kort", "Hoe zeg je „de negende”?", "le neuvième / la neuvième", WL),
                 ("waar", "Na <em>chaque</em> staat het naamwoord altijd in het enkelvoud.",
                  True),
             ]),
    ])


# ============================================================
zet("voornaamwoorden-cod-coi-y-en-en",
    titel="Voornaamwoorden: COD, COI, y en en",
    reeksen=[
        dict(kop="COD of COI?",
             opdracht="Het voorwerp staat onderstreept. Schrijf COD of COI op.",
             oefeningen=[
                 ("rij", [("Je vois <u>Marie</u>.", "COD"),
                          ("Je parle <u>à Marie</u>.", "COI"),
                          ("Il écrit <u>une lettre</u>.", "COD"),
                          ("Il téléphone <u>à ses parents</u>.", "COI"),
                          ("Nous aidons <u>les voisins</u>.", "COD"),
                          ("Elle répond <u>au professeur</u>.", "COI")],
                  "Welk soort voorwerp is dit?", "90px"),
                 ("open", "Hoe vind je zeker of iets COD of COI is?",
                  "Vraag qui of quoi na het werkwoord: dan is het COD. Moet je à qui of à quoi "
                  "vragen, dan is het COI.", 3),
                 ("waar", "<em>Téléphoner</em> heeft in het Frans een COD.", False),
             ]),
        dict(kop="Vervang door een voornaamwoord",
             opdracht="Schrijf de hele zin opnieuw, met het voornaamwoord op zijn plaats.",
             oefeningen=[
                 ("open", "Je regarde <u>le film</u>.", "Je le regarde.", 2),
                 ("open", "Elle écrit <u>à sa grand-mère</u>.", "Elle lui écrit.", 2),
                 ("open", "Nous invitons <u>les voisins</u>.", "Nous les invitons.", 2),
                 ("open", "Il donne un cadeau <u>à ses amis</u>.",
                  "Il leur donne un cadeau.", 2),
                 ("open", "Tu vas <u>à Paris</u>.", "Tu y vas.", 2),
                 ("open", "J'ai <u>trois frères</u>.", "J'en ai trois.", 2),
                 ("open", "Je ne mange pas <u>de viande</u>.", "Je n'en mange pas.", 2),
             ]),
        dict(kop="Waar staat het voornaamwoord?",
             opdracht="Zet de zin juist in elkaar.",
             oefeningen=[
                 ("open", "(le / je / vois / ne / pas) → een ontkennende zin",
                  "Je ne le vois pas.", 2),
                 ("open", "(l' / j' / vu / ai) → in de passé composé",
                  "Je l'ai vu.", 2),
                 ("open", "(moi / donne / le) → een bevel: geef het me",
                  "Donne-le-moi.", 2),
                 ("open", "(me / donne / le / ne / pas) → een verbod",
                  "Ne me le donne pas.", 2),
                 ("open", "(y / nous / aller / allons) → wij gaan erheen",
                  "Nous allons y aller.", 2),
                 ("open", "Waarom staat het voornaamwoord in <em>Donne-le-moi</em> achteraan, "
                          "en in <em>Ne me le donne pas</em> vooraan?",
                  "Alleen in een bevestigend bevel komt het voornaamwoord achter het werkwoord; "
                  "in alle andere zinnen, ook in een verbod, staat het ervoor.", 3),
             ]),
        dict(kop="Het deelwoord dat meegaat",
             opdracht="Vul de juiste vorm van het voltooid deelwoord in.",
             oefeningen=[
                 ("rij", [("Les lettres? Je les ai (écrire).", "écrites"),
                          ("La porte? Il l'a (fermer).", "fermée"),
                          ("Elle est (partir) à midi.", "partie"),
                          ("Nous avons (voir) le film.", "vu"),
                          ("Les filles sont (arriver).", "arrivées"),
                          ("Elle s'est (laver).", "lavée")],
                  "Welke vorm hoort hier?", "120px"),
                 ("open", "Leg de regel uit die je bij de eerste twee zinnen gebruikt hebt.",
                  "Met avoir gaat het deelwoord mee in geslacht en getal met het lijdend "
                  "voorwerp, maar alleen als dat vóór het werkwoord staat.", 3),
             ]),
        dict(kop="Alleen staan of niet",
             opdracht="Vul het juiste voornaamwoord in.",
             oefeningen=[
                 ("rij", [("Qui vient? ___! (ik)", "Moi"),
                          ("Je pars avec ___. (hem)", "lui"),
                          ("C'est ___ qui a gagné. (zij, enkelvoud)", "elle"),
                          ("Ce livre est ___. (van mij)", "à moi / le mien"),
                          ("Chez ___, on mange à sept heures. (ons)", "nous"),
                          ("___ aussi, nous sommes fatigués.", "Nous")],
                  "Welk voornaamwoord hoort hier?", "110px"),
                 ("open", "Wanneer gebruik je <em>moi</em> in plaats van <em>je</em>?",
                  "Als het voornaamwoord alleen staat, na een voorzetsel, of in een zin met "
                  "c'est — dus overal waar het niet rechtstreeks onderwerp bij het werkwoord "
                  "is.", 3),
             ]),
    ])


# ============================================================
zet("bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen",
    titel="Bijvoeglijke naamwoorden, bijwoorden en de trappen",
    reeksen=[
        dict(kop="De juiste uitgang",
             opdracht="Vul de vorm in die bij het naamwoord past.",
             oefeningen=[
                 ("rij", [("une fille (heureux)", "heureuse"), ("des murs (blanc)", "blancs"),
                          ("une voiture (neuf)", "neuve"), ("des idées (nouveau)", "nouvelles"),
                          ("un homme (vieux)", "vieux"), ("une femme (actif)", "active")],
                  "Welke vorm hoort hier?", "130px"),
                 ("rij", [("un (beau) arbre", "bel"), ("un (vieux) ami", "vieil"),
                          ("un (nouveau) élève", "nouvel"), ("une (beau) maison", "belle"),
                          ("des (beau) jours", "beaux"), ("une (long) histoire", "longue")],
                  "Welke vorm hoort hier?", "130px"),
                 ("open", "Waarom staat er <em>un bel arbre</em> en niet <em>un beau "
                          "arbre</em>?",
                  "Voor een mannelijk woord dat met een klinker of stomme h begint, worden "
                  "beau, nouveau en vieux tot bel, nouvel en vieil.", 3),
             ]),
        dict(kop="Voor of achter het naamwoord",
             opdracht="Zet het bijvoeglijk naamwoord op zijn plaats en schrijf de groep over.",
             oefeningen=[
                 ("rij", [("une maison (grand)", "une grande maison"),
                          ("une voiture (rouge)", "une voiture rouge"),
                          ("un garçon (jeune)", "un jeune garçon"),
                          ("un film (intéressant)", "un film intéressant"),
                          ("une (bon) idée", "une bonne idée"),
                          ("un repas (italien)", "un repas italien")],
                  "Schrijf de groep juist op.", WW),
                 ("open", "Welke soorten bijvoeglijke naamwoorden staan in het Frans vóór het "
                          "naamwoord?",
                  "Een kleine groep korte, veel gebruikte woorden over schoonheid, leeftijd, "
                  "goedheid en grootte: beau, joli, jeune, vieux, bon, mauvais, grand, petit, "
                  "gros, nouveau.", 3),
                 ("open", "<em>Un homme grand</em> en <em>un grand homme</em> betekenen niet "
                          "hetzelfde. Leg uit.",
                  "Un homme grand is een lange man; un grand homme is een groot man in de zin "
                  "van belangrijk.", 3),
             ]),
        dict(kop="Van bijvoeglijk naamwoord naar bijwoord",
             opdracht="Maak het bijwoord.",
             oefeningen=[
                 ("rij", [("lent", "lentement"), ("heureux", "heureusement"),
                          ("vrai", "vraiment"), ("patient", "patiemment"),
                          ("évident", "évidemment"), ("bon", "bien")],
                  "Welk bijwoord hoort hierbij?", WW),
                 ("open", "Leg de gewone regel uit om een bijwoord te maken.",
                  "Je neemt de vrouwelijke vorm van het bijvoeglijk naamwoord en zet er -ment "
                  "achter: lent wordt lente wordt lentement.", 3),
                 ("waar", "Het bijwoord bij <em>bon</em> is <em>bonnement</em>.", False),
             ]),
        dict(kop="Vergelijken",
             opdracht="Schrijf de zin af.",
             oefeningen=[
                 ("open", "Paul (1m80) / Luc (1m70): Paul est ___ Luc.",
                  "Paul est plus grand que Luc.", 2),
                 ("open", "Een fiets / een auto, qua prijs: Un vélo est ___ une voiture.",
                  "Un vélo est moins cher qu'une voiture.", 2),
                 ("open", "Twee broers even oud: Il est ___ son frère.",
                  "Il est aussi âgé que son frère.", 2),
                 ("open", "Dit restaurant is het beste van de stad.",
                  "C'est le meilleur restaurant de la ville.", 2),
                 ("open", "Zij werkt het best van de klas.",
                  "Elle travaille le mieux de la classe.", 2),
                 ("open", "Waarom schrijf je niet <em>plus bon</em> en niet <em>plus "
                          "bien</em>?",
                  "Bon en bien hebben een eigen vergrotende trap: meilleur voor bon en mieux "
                  "voor bien. Plus bon en plus bien bestaan niet.", 3),
             ]),
        dict(kop="Vind de fout",
             opdracht="In elke zin zit één fout. Schrijf de zin juist over.",
             oefeningen=[
                 ("open", "<em>C'est une film intéressante.</em>",
                  "C'est un film intéressant.", 2),
                 ("open", "<em>Elle court plus vite comme moi.</em>",
                  "Elle court plus vite que moi.", 2),
                 ("open", "<em>Ce sont des grands maisons.</em>",
                  "Ce sont de grandes maisons.", 2),
                 ("open", "<em>Il parle français bon.</em>",
                  "Il parle bien français.", 2),
             ]),
    ])


# ============================================================
zet("present-imperatif-en-de-wederkerende-werkwoorden",
    titel="Présent, impératif en de wederkerende werkwoorden",
    reeksen=[
        dict(kop="De drie groepen",
             opdracht="Vervoeg in de présent.",
             oefeningen=[
                 ("rij", [("je (parler)", "parle"), ("nous (finir)", "finissons"),
                          ("ils (vendre)", "vendent"), ("tu (choisir)", "choisis"),
                          ("vous (attendre)", "attendez"), ("elle (regarder)", "regarde")],
                  "Welke vorm hoort hier?", "120px"),
                 ("open", "Waaraan herken je een werkwoord van de tweede groep, en wat is er "
                          "bijzonder aan het meervoud?",
                  "Het eindigt op -ir en krijgt in het meervoud -iss- erbij: nous finissons, "
                  "vous finissez, ils finissent.", 3),
             ]),
        dict(kop="De onregelmatige werkwoorden",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["werkwoord", "je", "nous", "ils"],
                  [["être", None, None, None], ["avoir", None, None, None],
                   ["aller", None, None, None], ["faire", None, None, None],
                   ["pouvoir", None, None, None], ["vouloir", None, None, None]],
                  "être: suis / sommes / sont · avoir: ai / avons / ont · "
                  "aller: vais / allons / vont · faire: fais / faisons / font · "
                  "pouvoir: peux / pouvons / peuvent · vouloir: veux / voulons / veulent",
                  "90px"),
                 ("rij", [("je (devoir)", "dois"), ("nous (prendre)", "prenons"),
                          ("ils (venir)", "viennent"), ("tu (savoir)", "sais"),
                          ("vous (dire)", "dites"), ("elle (mettre)", "met")],
                  "Welke vorm hoort hier?", "120px"),
             ]),
        dict(kop="De gebiedende wijs",
             opdracht="Schrijf het bevel op.",
             oefeningen=[
                 ("rij", [("(tu) parler", "Parle!"), ("(vous) finir", "Finissez!"),
                          ("(nous) partir", "Partons!"), ("(tu) aller", "Va!"),
                          ("(vous) être", "Soyez!"), ("(tu) avoir", "Aie!")],
                  "Hoe luidt het bevel?", "120px"),
                 ("open", "Waarom valt bij <em>tu parles</em> de s weg in het bevel?",
                  "Bij werkwoorden op -er en bij aller verdwijnt de slot-s in de tu-vorm van de "
                  "gebiedende wijs: tu parles wordt parle.", 3),
                 ("open", "Schrijf een verbod: zeg tegen iemand dat hij niet te laat mag komen.",
                  "N'arrive pas en retard. / Ne sois pas en retard.", 2),
             ]),
        dict(kop="Wederkerende werkwoorden",
             opdracht="Vervoeg en let op het voornaamwoord.",
             oefeningen=[
                 ("rij", [("je (se lever)", "me lève"), ("tu (se laver)", "te laves"),
                          ("il (s'habiller)", "s'habille"), ("nous (se dépêcher)",
                          "nous dépêchons"), ("vous (se reposer)", "vous reposez"),
                          ("elles (se coucher)", "se couchent")],
                  "Welke vorm hoort hier?", "140px"),
                 ("open", "Schrijf in het Frans: ik sta op om zeven uur en ik was me.",
                  "Je me lève à sept heures et je me lave.", 2),
                 ("open", "Zet in de ontkenning: <em>Elle se dépêche.</em>",
                  "Elle ne se dépêche pas.", 2),
                 ("open", "Zet in een bevel: <em>tu te lèves</em>.",
                  "Lève-toi!", 2),
             ]),
        dict(kop="Een stukje tekst invullen",
             opdracht="Vul de werkwoorden in de présent in.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Le samedi, nous ___(1, aller) au marché. Ma mère ___(2, choisir) "
                  "les légumes et moi, je ___(3, prendre) le pain. Après, nous ___(4, boire) "
                  "un café sur la place. Mon père ne ___(5, venir) jamais: il ___(6, préférer) "
                  "rester à la maison.</em></p>"),
                 ("rij", [("1", "allons"), ("2", "choisit"), ("3", "prends"),
                          ("4", "buvons"), ("5", "vient"), ("6", "préfère")],
                  "Welke vorm hoort op die plaats?", "120px"),
             ]),
    ])


# ============================================================
zet("passe-compose-imparfait-en-plus-que-parfait",
    titel="Passé composé, imparfait en plus-que-parfait",
    reeksen=[
        dict(kop="Avoir of être?",
             opdracht="Schrijf het hulpwerkwoord op en daarna de hele vorm.",
             oefeningen=[
                 ("rij", [("je (manger)", "avoir — j'ai mangé"),
                          ("elle (aller)", "être — elle est allée"),
                          ("nous (prendre)", "avoir — nous avons pris"),
                          ("ils (venir)", "être — ils sont venus"),
                          ("tu (se laver)", "être — tu t'es lavé(e)"),
                          ("vous (finir)", "avoir — vous avez fini")],
                  "Welk hulpwerkwoord en welke vorm?", WW),
                 ("open", "Welke werkwoorden nemen <em>être</em> in de passé composé?",
                  "De werkwoorden van beweging en verandering van toestand (aller, venir, "
                  "partir, arriver, entrer, sortir, monter, descendre, naître, mourir, rester, "
                  "tomber, devenir) en alle wederkerende werkwoorden.", 4),
             ]),
        dict(kop="Onregelmatige deelwoorden",
             opdracht="Schrijf het voltooid deelwoord op.",
             oefeningen=[
                 ("rij", [("prendre", "pris"), ("voir", "vu"), ("faire", "fait"),
                          ("être", "été"), ("avoir", "eu"), ("écrire", "écrit")],
                  "Wat is het deelwoord?", "110px"),
                 ("rij", [("mettre", "mis"), ("ouvrir", "ouvert"), ("boire", "bu"),
                          ("vivre", "vécu"), ("naître", "né"), ("venir", "venu")],
                  "Wat is het deelwoord?", "110px"),
             ]),
        dict(kop="Passé composé of imparfait?",
             opdracht="Vul in en schrijf achter de zin waarom je die tijd koos.",
             oefeningen=[
                 ("open", "Hier, il ___ (pleuvoir) toute la journée.",
                  "il a plu — één afgebakende gebeurtenis met een duur die af is", 2),
                 ("open", "Quand j'___ (être) petit, nous ___ (habiter) à Gand.",
                  "j'étais, nous habitions — een toestand in het verleden", 2),
                 ("open", "Elle lisait quand le téléphone ___ (sonner).",
                  "a sonné — een plotse gebeurtenis in een lopende achtergrond", 2),
                 ("open", "Chaque été, nous ___ (aller) à la mer.",
                  "allions — een gewoonte", 2),
                 ("open", "Soudain, la lumière ___ (s'éteindre).",
                  "s'est éteinte — soudain wijst op één plots moment", 2),
                 ("open", "Geef in je eigen woorden het verschil tussen de twee tijden.",
                  "De imparfait schildert het decor: hoe het was, wat gewoonlijk gebeurde, wat "
                  "bezig was. De passé composé vertelt wat er dan gebeurde: één feit dat af is "
                  "en de verhaallijn vooruitduwt.", 4),
             ]),
        dict(kop="Een verhaal in de verleden tijd",
             opdracht="Vul de juiste verleden tijd in.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Il ___(1, être) huit heures et il ___(2, faire) encore noir. Léa "
                  "___(3, attendre) le bus depuis dix minutes quand elle ___(4, voir) son "
                  "voisin. Il lui ___(5, proposer) de la conduire. Elle ___(6, accepter) et "
                  "elle ___(7, arriver) à l'heure pour la première fois de la semaine.</em></p>"),
                 ("rij", [("1", "était"), ("2", "faisait"), ("3", "attendait"),
                          ("4", "a vu"), ("5", "a proposé"), ("6", "a accepté"),
                          ("7", "est arrivée")],
                  "Welke vorm hoort op die plaats?", "130px"),
             ]),
        dict(kop="Plus-que-parfait",
             opdracht="Zet de zin in de plus-que-parfait of leg uit.",
             oefeningen=[
                 ("open", "Quand je suis arrivé, le train (partir) déjà.",
                  "le train était déjà parti", 2),
                 ("open", "Elle m'a dit qu'elle (oublier) son code.",
                  "qu'elle avait oublié son code", 2),
                 ("open", "Nous (ne pas réserver), donc il n'y avait plus de place.",
                  "Nous n'avions pas réservé", 2),
                 ("open", "Wanneer gebruik je de plus-que-parfait?",
                  "Voor iets dat nog vroeger gebeurde dan een ander verleden feit: het verleden "
                  "achter het verleden.", 3),
             ]),
    ])


# ============================================================
zet("futur-conditionnel-en-subjonctif",
    titel="Futur, conditionnel en subjonctif",
    reeksen=[
        dict(kop="Futur proche of futur simple",
             opdracht="Schrijf de gevraagde vorm op.",
             oefeningen=[
                 ("rij", [("je (partir) — futur proche", "je vais partir"),
                          ("nous (manger) — futur simple", "nous mangerons"),
                          ("tu (être) — futur simple", "tu seras"),
                          ("ils (avoir) — futur simple", "ils auront"),
                          ("elle (aller) — futur simple", "elle ira"),
                          ("vous (faire) — futur simple", "vous ferez")],
                  "Welke vorm hoort hier?", WW),
                 ("open", "Wanneer kies je voor de futur proche?",
                  "Voor iets dat vlak voor de deur staat of al vastligt, en in gesproken taal; "
                  "de futur simple past bij een verdere toekomst en bij geschreven taal.", 3),
             ]),
        dict(kop="Onregelmatige stammen",
             opdracht="Geef de stam van de futur.",
             oefeningen=[
                 ("rij", [("venir", "viendr-"), ("voir", "verr-"), ("pouvoir", "pourr-"),
                          ("vouloir", "voudr-"), ("devoir", "devr-"), ("savoir", "saur-")],
                  "Welke stam gebruikt de futur?", "110px"),
                 ("open", "Waarom heeft de conditionnel dezelfde stammen als de futur?",
                  "De conditionnel is die stam plus de uitgangen van de imparfait: je viendrais, "
                  "tu viendrais, nous viendrions.", 3),
             ]),
        dict(kop="Conditionnel: beleefdheid, wens en voorwaarde",
             opdracht="Schrijf de zin in het Frans.",
             oefeningen=[
                 ("open", "Ik zou graag een koffie willen.", "Je voudrais un café.", 2),
                 ("open", "Zou u mij kunnen helpen?", "Pourriez-vous m'aider?", 2),
                 ("open", "Als ik geld had, zou ik reizen.",
                  "Si j'avais de l'argent, je voyagerais.", 2),
                 ("open", "Volgens de krant zou de brug in mei dichtgaan.",
                  "Selon le journal, le pont fermerait en mai.", 2),
                 ("open", "Welke vier dingen kan de conditionnel uitdrukken?",
                  "Beleefdheid, een wens, het gevolg van een voorwaarde, en een bericht waarvan "
                  "je niet zeker bent.", 3),
             ]),
        dict(kop="Subjonctif: wanneer wel?",
             opdracht="Schrijf <em>wel</em> of <em>niet</em> en de juiste vorm erbij.",
             oefeningen=[
                 ("rij", [("Il faut que tu (venir).", "wel — viennes"),
                          ("Je pense qu'il (être) malade.", "niet — est"),
                          ("Je veux que vous (faire) attention.", "wel — fassiez"),
                          ("Je sais qu'elle (avoir) raison.", "niet — a"),
                          ("Bien qu'il (pleuvoir), nous sortons.", "wel — pleuve"),
                          ("J'espère qu'il (venir).", "niet — viendra")],
                  "Subjonctif of niet, en welke vorm?", WW),
                 ("open", "Geef de vuistregel voor de subjonctif.",
                  "Na uitdrukkingen die geen feit geven maar een wil, een gevoel, een twijfel of "
                  "een noodzaak: il faut que, je veux que, je suis content que, bien que, "
                  "avant que. Na een zeker weten (je sais que, j'espère que) komt hij niet.", 4),
                 ("rij", [("être (que je)", "sois"), ("avoir (que tu)", "aies"),
                          ("aller (qu'il)", "aille"), ("faire (que nous)", "fassions"),
                          ("pouvoir (que vous)", "puissiez"), ("savoir (qu'ils)", "sachent")],
                  "Welke subjonctif hoort hier?", "110px"),
             ]),
        dict(kop="Een plan voor volgend jaar",
             opdracht="Schrijf in het Frans, ongeveer zestig woorden.",
             oefeningen=[
                 ("open", "Vertel wat je volgend jaar gaat doen: gebruik minstens twee keer de "
                          "futur simple, één keer de conditionnel en één keer "
                          "<em>il faut que</em> met een subjonctif.",
                  "L'année prochaine, je commencerai une formation de mécanicien. Je "
                  "travaillerai aussi le samedi pour payer mon permis. Si j'avais le choix, je "
                  "partirais un mois en France pour mieux parler la langue. Mais il faut que je "
                  "réussisse d'abord mes examens de juin.", 9),
             ]),
    ])


# ============================================================
zet("soorten-zinnen-bijzinnen-en-si-zinnen",
    titel="Soorten zinnen, bijzinnen en si-zinnen",
    reeksen=[
        dict(kop="Drie manieren om een vraag te stellen",
             opdracht="Schrijf dezelfde vraag drie keer: met de stem, met <em>est-ce que</em> "
                      "en met omkering.",
             oefeningen=[
                 ("open", "Je komt mee. (tu / venir)",
                  "Tu viens? · Est-ce que tu viens? · Viens-tu?", 2),
                 ("open", "Zij woont in Luik. (elle / habiter à Liège)",
                  "Elle habite à Liège? · Est-ce qu'elle habite à Liège? · "
                  "Habite-t-elle à Liège?", 2),
                 ("open", "Waarom staat er een t tussen de streepjes in "
                          "<em>Habite-t-elle</em>?",
                  "Om twee klinkers uit elkaar te houden; die t is alleen om uit te spreken en "
                  "betekent niets.", 2),
             ]),
        dict(kop="Ontkennen",
             opdracht="Zet de zin in de ontkenning met het gevraagde woord.",
             oefeningen=[
                 ("rij", [("Il parle. (pas)", "Il ne parle pas."),
                          ("Je mange de la viande. (plus)", "Je ne mange plus de viande."),
                          ("Elle voit quelqu'un. (personne)", "Elle ne voit personne."),
                          ("Nous faisons quelque chose. (rien)", "Nous ne faisons rien."),
                          ("Tu es déjà allé à Paris. (jamais)", "Tu n'es jamais allé à Paris."),
                          ("Il a un vélo. (que / alleen een auto)",
                           "Il n'a qu'une voiture.")],
                  "Schrijf de ontkennende zin.", WL),
                 ("open", "Waar staan <em>ne</em> en het tweede woordje in de passé composé?",
                  "Rond het hulpwerkwoord: il n'a pas mangé. Alleen personne komt achter het "
                  "deelwoord: il n'a vu personne.", 3),
             ]),
        dict(kop="Bijzinnen koppelen",
             opdracht="Maak van de twee zinnen één zin met het gevraagde woord.",
             oefeningen=[
                 ("open", "Je connais un garçon. Ce garçon joue du piano. (qui)",
                  "Je connais un garçon qui joue du piano.", 2),
                 ("open", "Voici le livre. J'ai acheté ce livre. (que)",
                  "Voici le livre que j'ai acheté.", 2),
                 ("open", "C'est la ville. Je suis né dans cette ville. (où)",
                  "C'est la ville où je suis né.", 2),
                 ("open", "Voilà le film. Tout le monde parle de ce film. (dont)",
                  "Voilà le film dont tout le monde parle.", 2),
                 ("open", "Wanneer gebruik je <em>dont</em>?",
                  "Als het werkwoord of het naamwoord in de bijzin met de gaat: parler de, "
                  "avoir besoin de, le titre de.", 3),
             ]),
        dict(kop="De si-zin",
             opdracht="Vul de twee werkwoorden in en schrijf erbij welk patroon het is.",
             oefeningen=[
                 ("open", "Si tu (avoir) le temps, tu (pouvoir) m'aider. (het is mogelijk)",
                  "Si tu as le temps, tu pourras m'aider — présent + futur", 2),
                 ("open", "Si j'(être) riche, j'(acheter) une maison. (niet echt zo)",
                  "Si j'étais riche, j'achèterais une maison — imparfait + conditionnel", 2),
                 ("open", "Si nous (partir) plus tôt, nous (ne pas rater) le train. "
                          "(het is te laat)",
                  "Si nous étions partis plus tôt, nous n'aurions pas raté le train — "
                  "plus-que-parfait + conditionnel passé", 2),
                 ("waar", "Na <em>si</em> mag in het Frans een futur staan.", False),
             ]),
        dict(kop="Vind de fout",
             opdracht="In elke zin zit één fout. Schrijf de zin juist over.",
             oefeningen=[
                 ("open", "<em>Est-ce que tu viens-tu?</em>",
                  "Est-ce que tu viens? of Viens-tu?", 2),
                 ("open", "<em>Je ne vois pas personne.</em>",
                  "Je ne vois personne.", 2),
                 ("open", "<em>Si j'aurai le temps, je viendrai.</em>",
                  "Si j'ai le temps, je viendrai.", 2),
                 ("open", "<em>Voici le livre qui j'ai lu.</em>",
                  "Voici le livre que j'ai lu.", 2),
                 ("open", "<em>Il n'a pas vu rien.</em>",
                  "Il n'a rien vu.", 2),
             ]),
    ])


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-een-franse-tekst-analyseren-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Lees de tekst eerst helemaal door zonder te stoppen bij een woord dat je niet kent. "
                    "Pas daarna de vragen, en dan gericht terugzoeken.",
             waarom=[]),
        dict(aanpak="Het onderwerp is waarover de tekst gaat, in enkele woorden. De hoofdgedachte is wat "
                    "de tekst erover zegt, in één volle zin.",
             waarom=[
                 None,
                 "Een hoofdgedachte is geen opsomming van alles wat er staat; ze vat samen waar de tekst "
                 "naartoe werkt. Hier dus niet alleen wat ze uitlenen, maar ook waarom het lukt.",
                 None, None, None,
             ]),
        dict(aanpak="Een vraag met twee of drie punten erin wil ook twee of drie antwoorden. Tel dus hoeveel "
                    "er gevraagd worden voor je schrijft.",
             waarom=[
                 "De tekst zet de prijs en het gebruik naast elkaar: tachtig euro voor minder dan een uur "
                 "per jaar. Dat is één reden in twee cijfers.",
                 None, None,
                 "Let op het verschil tussen verkeerd gebruik en gewone slijtage: alleen bij het eerste "
                 "betaal je zelf.",
                 None,
                 "De tekst zegt dat ze náást boeken ook voorwerpen uitleent, niet in de plaats ervan.",
             ]),
        dict(aanpak="Raad een woord uit de zin eromheen: het soort woord, wat ervoor en erachter staat, en "
                    "wat in die zin logisch past. Een woordenboek sla je pas daarna open.",
             waarom=[
                 "Une perceuse en une échelle zijn te raden uit de zin zelf: je leent ze, en je gebruikt "
                 "ze zelden. Un conseil lijkt op het Nederlandse consult maar betekent een raad.",
                 "On is in het Frans vaak een vage men, en wat dat men is, staat in de zin ervoor.",
                 None,
             ]),
        dict(aanpak="Een tekst van een ander soort lees je anders: bij een bericht zoek je wie het stuurt, "
                    "aan wie, en wat er van je gevraagd wordt.",
             waarom=[
                 "Een kader, een afzender en een datum zonder verhaal erbij: dat is een bekendmaking.",
                 None, None, None,
                 "De straat is net dicht tussen die uren; daarbuiten mag het wel.",
                 None,
             ]),
        dict(aanpak="Deze vragen gaan over hoe je werkt, niet over één tekst. Het antwoord dat je hier "
                    "opschrijft, is wat je op het examen zelf doet.",
             waarom=[
                 "De fout die het meest punten kost, is woord per woord beginnen vertalen. Dan ben je door "
                 "je tijd voor je weet waarover de tekst gaat.",
                 None, None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-tekstsoorten-tekstverbanden-en-verwijswoorden-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Je herkent de soort aan de vorm, nog voor je de inhoud snapt: gebiedende wijs en "
                    "stappen, een aanspreking, een verleden tijd met een verhaal, een prijs, een afzender.",
             waarom=[
                 "Mélangez en ajoutez staan in de gebiedende wijs: iemand zegt je wat je moet doen.",
                 "Chère Madame en je vous écris au sujet de: de twee vaste kenmerken van een brief.",
                 "Een verleden tijd plus een vooruitwijzing (ne savait pas encore) hoort bij een verhaal.",
                 None, None,
                 "Selon une étude verwijst naar een bron. Dat doet een artikel, geen reclame.",
             ]),
        dict(aanpak="Zeg niet wat de tekst betekent maar waaraan je het ziet: aan de vorm, de werkwoorden, "
                    "de aanspreking, de cijfers.",
             waarom=[None, None, None]),
        dict(aanpak="Zet eerst in het Nederlands welk verband er ligt (oorzaak, gevolg, tegenstelling, "
                    "volgorde) en kies dan het Franse woord dat daarbij hoort.",
             waarom=[
                 "Let op het verschil tussen parce que (oorzaak, achteraan) en donc (gevolg). Malgré krijgt "
                 "een naamwoord achter zich, geen zin.",
                 None, None, None,
             ]),
        dict(aanpak="Zoek het woord waar het verwijswoord voor staat, meestal in de zin ervoor. Let bij y "
                    "en en op wat ze vervangen: y een plaats, en een hoeveelheid.",
             waarom=[
                 "Le vervangt een lijdend voorwerp, leur een meewerkend voorwerp in het meervoud. Dat "
                 "verschil bepaalt de vorm.",
                 "Ci betekent hier, là betekent daar: ci staat dus bij wat het dichtst bij staat in de "
                 "tekst, en dat is het laatstgenoemde.",
                 "Y vervangt een plaats of een zaak met à. Voor een persoon gebruik je lui of leur.",
             ]),
        dict(aanpak="De signaalwoorden zijn de wegwijzers van een alinea: ze zeggen of er een voordeel, "
                    "een nadeel of een gevolg komt.",
             waarom=[
                 None,
                 "Cependant betekent nochtans: het kondigt altijd een tegenstelling aan, dus hier het nadeel.",
                 None,
                 "Cette limite verwijst terug naar het cijfer dat er net voor staat. Een verwijswoord "
                 "opzoeken doe je altijd in de zin ervoor.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-de-franstalige-wereld-omgangsvormen-en-gewoontes-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vraag je twee dingen af: ken ik deze persoon, en sta ik in een formele situatie. Bij "
                    "twijfel is vous altijd de veilige keuze.",
             waarom=[
                 "Let op de laatste twee: vous kan ook gewoon meervoud zijn tegen twee vrienden, en op een "
                 "forum tutoyeert bijna iedereen.",
                 None,
                 "Dat is de vaste omgangsvorm: wie begint met tu, geeft daarmee toestemming. Zelf beginnen "
                 "tegen iemand ouder doe je niet.",
             ]),
        dict(aanpak="Deze uitdrukkingen leer je als geheel, niet woord per woord. Ze komen op elk "
                    "spreekexamen terug.",
             waarom=[
                 "Je voudrais is de beleefde vorm van je veux. Met je veux klink je in het Frans eisend.",
                 None,
             ]),
        dict(aanpak="Het Frans is een wereldtaal, niet enkel de taal van Frankrijk. Onthoud van elk "
                    "werelddeel minstens één voorbeeld.",
             waarom=[
                 None, None, None,
                 "Septante en nonante zijn Belgisch en Zwitsers, soixante-dix en quatre-vingt-dix Frans. "
                 "Huitante hoort enkel in Zwitserland.",
             ]),
        dict(aanpak="Gewoontes zijn examenstof zoals de grammatica: ze komen terug in de spreek- en "
                    "schrijftaken over een bezoek of een uitwisseling.",
             waarom=[
                 None, None, None,
                 "Te vroeg komen is in Frankrijk onhandig, want de gastheer is dan nog niet klaar. Een "
                 "kwartiertje later is de gewoonte.",
                 "De kaas komt in Frankrijk vóór het dessert, anders dan bij ons.",
             ]),
        dict(aanpak="Beleefder maken doe je in het Frans met drie middelen: de voorwaardelijke wijs "
                    "(pourriez-vous, je voudrais), een s'il vous plaît, en een excuses vooraf.",
             waarom=[
                 None, None,
                 "Iemand rechtstreeks tegenspreken doe je in het Frans met een verzachting: je ne suis pas "
                 "tout à fait d'accord in plaats van c'est faux.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-schrijven-schriftelijke-interactie-en-leesbeleving-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De aanhef hangt af van twee dingen: ken je de naam, en is het formeel. Ken je de naam "
                    "niet, dan is het Madame, Monsieur, zonder meer.",
             waarom=[
                 "Let op het slot: cordialement is het gewone formele slot, veuillez agréer is het zeer "
                 "formele. Bises schrijf je enkel aan vrienden.",
                 "Cher of chère gebruik je alleen bij iemand die je kent. Bij een onbekende is dat te "
                 "familiair.",
             ]),
        dict(aanpak="Een mail van zestig woorden heeft drie delen: wat er gebeurd is, wat het probleem is, "
                    "en wat je vraagt. Zet een aanhef en een slotformule rond dat geheel.",
             waarom=[
                 "Het verschil tussen punten en geen punten zit in de derde stap: zeg uitdrukkelijk wat je "
                 "wil, en vraag een antwoord. Een klacht zonder vraag is geen klacht.",
                 "Een bericht aan een vriend heeft dezelfde drie delen, maar in spreektaal: bedanken, "
                 "uitleggen, iets anders voorstellen.",
             ]),
        dict(aanpak="Schrijftaal is in het Frans iets heel anders dan spreektaal. Drie vaste ingrepen: de "
                    "ne terug, je veux wordt je voudrais, en een vraag met pourriez-vous.",
             waarom=[
                 "In gesproken Frans valt de ne weg. Op papier zet je ze er altijd terug.",
                 None,
                 "C'est nul is een gevoel, geen klacht. Zeg wat je vindt en wat je wil, in plaats van een "
                 "oordeel.",
                 "Faut que is spreektaal; schrijf il faut que. Zet ook het uur voluit.",
             ]),
        dict(aanpak="Loop je eigen tekst na op vier dingen in deze volgorde: de werkwoordsvorm, het "
                    "geslacht van het naamwoord, de overeenkomst van het deelwoord, en de ontkenning.",
             waarom=[
                 "Na avoir komt het voltooid deelwoord: pris, niet prendre.",
                 "Musée is mannelijk, al eindigt het op -e. Daar struikelt bijna iedereen over.",
                 "Bij être komt het deelwoord overeen met het onderwerp: elle est arrivée.",
                 "In een ontkenning wordt du, de la en des altijd de: pas de viande.",
                 "Que plus il wordt qu'il. En na een verleden tijd in de hoofdzin komt de conditionnel: "
                 "viendrait in plaats van viendra.",
             ]),
        dict(aanpak="Bij leesbeleving vraagt men niet wat er staat maar wat het met je doet, én waaraan je "
                    "dat merkt. Dat tweede deel is waar de punten zitten.",
             waarom=[
                 "Een gevoel noemen is de helft; het andere halve punt zit in het detail uit de tekst dat "
                 "het laat zien.",
                 None, None,
                 "Een mening in het Frans mag kort zijn, maar de reden met parce que moet erbij staan.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-mens-gezondheid-en-het-dagelijkse-leven-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Leer een Frans naamwoord altijd met zijn lidwoord erbij. Zonder dat lidwoord weet je "
                    "later het geslacht niet meer, en dan loopt het bijvoeglijk naamwoord mis.",
             waarom=[
                 "Épaule is vrouwelijk, al staat er l' voor. Dat kan je niet horen, dus moet je het leren.",
                 "Le cœur is enkelvoud, les poumons meervoud. Longen zijn er twee, dus altijd meervoud.",
             ]),
        dict(aanpak="Pijn zeg je in het Frans met avoir mal à, en dan smelt à samen met het lidwoord: à la "
                    "gorge, au dos, aux dents.",
             waarom=[
                 None,
                 "Enrhumé is een bijvoeglijk naamwoord, dus je gebruikt être. Bij een meisje komt er een "
                 "tweede e bij.",
                 "Koorts is in het Frans een hoeveelheid: de la fièvre, niet la fièvre.",
                 "Depuis betekent sinds en antwoordt op depuis quand. Pendant zou de duur zijn.",
                 None, None,
             ]),
        dict(aanpak="Na een maat of een hoeveelheid komt in het Frans de, zonder lidwoord. Dat is één regel "
                    "die je in deze hele reeks kan toepassen.",
             waarom=[None, None, None]),
        dict(aanpak="Een bijvoeglijk naamwoord past zich aan in geslacht en getal. Op drie kleuren na: "
                    "marron, orange en kleuren met twee woorden blijven gelijk.",
             waarom=[
                 "Let op gris: dat eindigt al op -s, dus in het mannelijk enkelvoud verandert er niets.",
                 None, None,
             ]),
        dict(aanpak="Bij een gatentekst lees je eerst de hele tekst door. Pas als je weet waarover hij "
                    "gaat, vul je de gaten in.",
             waarom=[
                 "Se lever is wederkerend: elle se lève. Prendre une douche is vast, net als prendre le bus.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-school-werk-reizen-en-de-samenleving-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Deze woorden heb je nodig zodra je over je eigen school praat, en dat is in bijna elke "
                    "spreektaak het eerste onderwerp.",
             waarom=[
                 None,
                 "Rater betekent zowel buizen als missen, bijvoorbeeld een trein. De zin eromheen zegt "
                 "welke van de twee.",
             ]),
        dict(aanpak="Een sollicitatie draait om drie dingen: wat je al deed, wat je kan, en wanneer je vrij "
                    "bent. Zeg die drie altijd met een concreet voorbeeld erbij.",
             waarom=[
                 None, None, None,
                 "Een eigenschap zonder voorbeeld zegt niets. Noem dus wat je al deed, niet enkel dat je "
                 "vriendelijk bent.",
                 None,
             ]),
        dict(aanpak="Aan een loket of een balie gebruik je altijd je voudrais plus s'il vous plaît. Dat is "
                    "de vaste vorm, ook voor een vraag die eigenlijk een bevel is.",
             waarom=[
                 None, None, None,
                 "Le quai is het perron. Het loket is le guichet.",
             ]),
        dict(aanpak="Voor een mening in het Frans heb je twee bouwstenen nodig: een inleiding (à mon avis, "
                    "je pense que) en een reden (parce que).",
             waarom=[None, None, None]),
        dict(aanpak="Bij een advertentie lees je gericht: wat moet je doen, wanneer, voor wie, en tegen "
                    "wanneer melden. Reken de uren zelf na.",
             waarom=[
                 "De pauze moet eraf. Een advertentie geeft het begin- en het einduur, de pauze staat er "
                 "los bij.",
                 None, None, None,
                 "Begin een sollicitatiemail met waar je de vacature zag. Dan weet de werkgever meteen "
                 "waarover het gaat.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-zelfstandige-naamwoorden-lidwoorden-en-determinanten-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Het lidwoord verraadt het geslacht. Begint het woord met een klinker, dan zie je dat "
                    "niet meer, en dan moet je het geleerd hebben.",
             waarom=[
                 "Problème is mannelijk ondanks de -e, liberté vrouwelijk. Woorden op -té zijn bijna altijd "
                 "vrouwelijk.",
                 None,
             ]),
        dict(aanpak="Drie soorten: bepaald als het bekend is, onbepaald als het er één van vele is, delend "
                    "als het een onbepaalde hoeveelheid is (du, de la, de l', des).",
             waarom=[
                 "Na een ontkenning verdwijnt het delend lidwoord: pas d'argent, niet pas de l'argent.",
                 None, None,
             ]),
        dict(aanpak="De meeste woorden krijgen -s. De uitzonderingen zijn -al dat -aux wordt, -eau dat "
                    "-eaux wordt, en wat al op s, x of z eindigt.",
             waarom=[
                 "Œil is volledig onregelmatig: des yeux. Travail wordt travaux, net als journal.",
                 None,
                 "Professeur krijgt in het Frans van vandaag een -e in het vrouwelijk. Élève is voor "
                 "allebei hetzelfde woord, alleen het lidwoord verandert.",
             ]),
        dict(aanpak="Het bezittelijk voornaamwoord volgt het dìng, niet de bezitter: sa voiture gaat over "
                    "de auto, die vrouwelijk is, niet over wie hem bezit.",
             waarom=[None, None, None]),
        dict(aanpak="Tout past zich aan aan wat erachter komt, chaque nooit. En een rangtelwoord maak je "
                    "met -ième, behalve de eerste.",
             waarom=[
                 "Tout le monde blijft tout, want monde is mannelijk enkelvoud. Premier is het enige "
                 "rangtelwoord dat geen -ième krijgt.",
                 None,
                 "Bij neuf valt de f weg: neuvième, niet neufième.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-voornaamwoorden-cod-coi-y-en-en-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vraag qui of quoi na het werkwoord: past dat, dan is het een COD. Moet je à qui of à "
                    "quoi vragen, dan is het een COI.",
             waarom=[
                 "Téléphoner, parler en répondre krijgen in het Frans altijd à. In het Nederlands hoor je "
                 "dat niet, dus daar gaat het mis.",
                 None,
                 "Je téléphone à quelqu'un: dus een COI, en daarom lui of leur, nooit le of la.",
             ]),
        dict(aanpak="COD wordt le, la of les. COI wordt lui of leur. Een plaats wordt y, een hoeveelheid of "
                    "iets met de wordt en.",
             waarom=[
                 None, None, None, None, None,
                 "Bij en blijft het getal staan: j'en ai trois. Het voornaamwoord vervangt alleen frères.",
                 "Ook na een ontkenning komt en op zijn plaats vóór het werkwoord: je n'en mange pas.",
             ]),
        dict(aanpak="Het voornaamwoord staat vóór het werkwoord, op één geval na: een bevestigend bevel. "
                    "Daar komt het erachter met een streepje.",
             waarom=[
                 None,
                 "In de passé composé staat het voornaamwoord vóór avoir, niet vóór het deelwoord.",
                 "In een bevestigend bevel wordt me ook moi: donne-le-moi.",
                 None,
                 "Bij twee werkwoorden hoort het voornaamwoord bij het werkwoord waar het bij past, dus "
                 "vóór de infinitief: allons y aller.",
                 None,
             ]),
        dict(aanpak="Met être gaat het deelwoord mee met het onderwerp. Met avoir gaat het alleen mee als "
                    "het lijdend voorwerp vóór het werkwoord staat.",
             waarom=[
                 "Les lettres en la porte staan als voornaamwoord vóór avoir, dus gaat het deelwoord mee. "
                 "In nous avons vu le film staat het erachter, dus niet.",
                 None,
             ]),
        dict(aanpak="Moi, toi, lui, elle, nous, vous, eux en elles zijn de vormen die alleen kunnen staan: "
                    "na een voorzetsel, in een c'est-zin of als antwoord.",
             waarom=[
                 "Ce livre est à moi gaat over bezit met à; le mien is het bezittelijk voornaamwoord dat "
                 "alleen staat. Beide zijn juist.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zoek eerst het naamwoord: geslacht en getal daarvan bepalen de uitgang. Let op de "
                    "groepen -eux dat -euse wordt, -f dat -ve wordt, en -eau dat -elle wordt.",
             waarom=[
                 "Neuf wordt neuve: de f wordt een v. Vieux blijft in het mannelijk gelijk, want het "
                 "eindigt al op x.",
                 "Beau, nouveau en vieux hebben een extra vorm voor een mannelijk woord met een klinker: "
                 "bel, nouvel, vieil.",
                 None,
             ]),
        dict(aanpak="De meeste bijvoeglijke naamwoorden staan in het Frans achter het naamwoord. Een kleine "
                    "groep korte, veel gebruikte staat ervoor.",
             waarom=[
                 "Kleuren, nationaliteiten en lange woorden staan altijd achteraan. Grand, jeune en bon "
                 "horen bij de kleine groep die vooraan staat.",
                 None,
                 "Bij een paar woorden verandert de plaats de betekenis. Vooraan is het figuurlijk, "
                 "achteraan letterlijk.",
             ]),
        dict(aanpak="De gewone regel: neem de vrouwelijke vorm en zet -ment erachter. Woorden op -ant en "
                    "-ent worden -amment en -emment.",
             waarom=[
                 "Vrai wordt vraiment zonder e, want de vrouwelijke vorm klinkt hetzelfde. Bon is "
                 "onregelmatig: bien.",
                 None,
                 "Het bijwoord bij bon is bien. Bonnement bestaat alleen in de vaste uitdrukking tout "
                 "bonnement.",
             ]),
        dict(aanpak="Vergelijken doe je met plus, moins of aussi, en altijd que erachter. Bon en bien "
                    "hebben hun eigen vorm: meilleur en mieux.",
             waarom=[
                 None,
                 "Que wordt qu' voor een klinker: qu'une voiture.",
                 None,
                 "Meilleur is het bijvoeglijk naamwoord bij bon, dus het hoort bij restaurant.",
                 "Mieux is het bijwoord bij bien, dus het hoort bij travaille. Dat is het verschil met "
                 "meilleur.",
                 None,
             ]),
        dict(aanpak="Loop de zin na op drie dingen: klopt het geslacht, klopt que in een vergelijking, en "
                    "staat het bijwoord op zijn plaats.",
             waarom=[
                 "Film is mannelijk, dus un film intéressant. De uitgang van het bijvoeglijk naamwoord "
                 "volgt dat.",
                 "Vergelijken gaat met que, niet met comme. Comme betekent zoals of als in een gelijkenis.",
                 "Staat een bijvoeglijk naamwoord vóór een meervoudig naamwoord, dan wordt des tot de: de "
                 "grandes maisons.",
                 "Bij een werkwoord hoort een bijwoord: il parle bien. En het bijwoord komt vóór het "
                 "lijdend voorwerp.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-present-imperatif-en-de-wederkerende-werkwoorden-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Kijk eerst naar de uitgang van de infinitief: -er is de eerste groep, -ir de tweede, "
                    "-re de derde. Elke groep heeft zijn eigen rij uitgangen.",
             waarom=[
                 "Let op choisir en finir: in het enkelvoud -is, -is, -it, maar in het meervoud komt er "
                 "-iss- tussen.",
                 None,
             ]),
        dict(aanpak="De onregelmatige werkwoorden zijn precies de werkwoorden die je het vaakst nodig hebt. "
                    "Leer ze in de volle rij, niet per vorm.",
             waarom=[
                 None,
                 "Dites is onregelmatig: vous dites, niet vous disez. Faites en êtes horen in dezelfde "
                 "kleine groep.",
             ]),
        dict(aanpak="De gebiedende wijs is de vervoegde vorm zonder het voornaamwoord. Bij -er valt de "
                    "slot-s weg in de tu-vorm.",
             waarom=[
                 "Être en avoir hebben een eigen vorm: sois, soyons, soyez en aie, ayons, ayez.",
                 None,
                 "Een verbod is ne … pas rond het bevel: n'arrive pas.",
             ]),
        dict(aanpak="Bij een wederkerend werkwoord verandert niet alleen het werkwoord maar ook het "
                    "voornaamwoord ervoor: me, te, se, nous, vous, se.",
             waarom=[
                 "Se lever krijgt een accent in het enkelvoud: je me lève, maar nous nous levons.",
                 None,
                 "In de ontkenning staat ne vóór het voornaamwoord: elle ne se dépêche pas.",
                 "In een bevestigend bevel komt het voornaamwoord erachter en wordt te tot toi: lève-toi.",
             ]),
        dict(aanpak="Zoek bij elke leegte eerst het onderwerp, en vervoeg daarna. De infinitief staat er bij "
                    "deze oefening al, dus de vraag is alleen de vorm.",
             waarom=[
                 "Boire en venir zijn onregelmatig: nous buvons, il vient. Préférer krijgt een accent grave "
                 "in het enkelvoud: elle préfère.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-passe-compose-imparfait-en-plus-que-parfait-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vraag je eerst af welk hulpwerkwoord erbij hoort. Met être gaat het deelwoord mee met "
                    "het onderwerp, met avoir meestal niet.",
             waarom=[
                 "Elle est allée krijgt een e, ils sont venus een s: bij être gaat het deelwoord mee. Bij "
                 "avoir blijft het gelijk.",
                 None,
             ]),
        dict(aanpak="De onregelmatige deelwoorden moet je uit het hoofd kennen; er zit geen regel in. Leer ze "
                    "per groepje met dezelfde uitgang.",
             waarom=[None, None]),
        dict(aanpak="De imparfait is het decor: hoe het was, wat gewoonlijk gebeurde, wat bezig was. De passé "
                    "composé is wat er dan gebeurde: één feit dat af is.",
             waarom=[
                 "Toute la journée lijkt op een duur, maar de dag is af: het is één afgeronde gebeurtenis.",
                 None,
                 "Lisait is de achtergrond, a sonné is wat erin gebeurde. Dat is het klassieke paar.",
                 "Chaque été wijst op een gewoonte, en een gewoonte staat altijd in de imparfait.",
                 "Soudain is het signaalwoord van de passé composé. Let op het deelwoord: s'éteindre is "
                 "wederkerend, dus être en een e erbij.",
                 None,
             ]),
        dict(aanpak="Lees het hele verhaal eerst door. Zet daarna het decor in de imparfait en de "
                    "gebeurtenissen in de passé composé.",
             waarom=[
                 "De eerste drie zijn decor, de laatste vier zijn wat er gebeurde. Est arrivée krijgt être "
                 "en een e, want het gaat over een zij.",
             ]),
        dict(aanpak="De plus-que-parfait is het hulpwerkwoord in de imparfait plus het deelwoord: j'avais fait, "
                    "j'étais parti.",
             waarom=[
                 "Partir neemt être, dus était parti. Déjà staat tussen het hulpwerkwoord en het deelwoord.",
                 None,
                 "In een ontkenning staat ne … pas rond het hulpwerkwoord: nous n'avions pas réservé.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-futur-conditionnel-en-subjonctif-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De futur proche is aller plus de infinitief. De futur simple is de infinitief plus -ai, "
                    "-as, -a, -ons, -ez, -ont.",
             waarom=[
                 "Être, avoir, aller en faire hebben een eigen stam: ser-, aur-, ir-, fer-. De uitgangen "
                 "blijven wel dezelfde.",
                 None,
             ]),
        dict(aanpak="Ken je de stam van de futur, dan ken je ook de conditionnel. Dat zijn twee tijden voor "
                    "de prijs van één rij.",
             waarom=[None, None]),
        dict(aanpak="De conditionnel doet vier dingen: beleefd vragen, een wens uiten, het gevolg van een "
                    "voorwaarde geven, en een onzeker bericht melden.",
             waarom=[
                 "Je voudrais is de beleefde vorm van je veux. Dat is de meest gebruikte conditionnel van "
                 "het Frans.",
                 None,
                 "Na si komt de imparfait en in de hoofdzin de conditionnel. Nooit twee keer de conditionnel.",
                 "Een bericht uit tweede hand zet het Frans in de conditionnel: le pont fermerait betekent "
                 "dat het zo gezegd wordt, niet dat het zeker is.",
                 None,
             ]),
        dict(aanpak="De subjonctif komt na een wil, een gevoel, een twijfel of een noodzaak. Na een zeker "
                    "weten komt hij niet.",
             waarom=[
                 "Je pense que en j'espère que geven iets dat je voor waar houdt, dus geen subjonctif. Bien "
                 "que geeft een toegeving, en die vraagt hem wel.",
                 None,
                 "Aller, faire, pouvoir en savoir hebben een eigen subjonctifstam: aille, fasse, puisse, "
                 "sache.",
             ]),
        dict(aanpak="Deze taak toetst of je de drie tijden door elkaar kan gebruiken. Schrijf eerst wat je "
                    "wil zeggen, en zet er dan de gevraagde vormen in.",
             waarom=[
                 "Il faut que vraagt een subjonctif: que je réussisse. Dat is precies waar deze taak naar "
                 "kijkt.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-soorten-zinnen-bijzinnen-en-si-zinnen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Drie manieren, van spreektaal naar schrijftaal: alleen de stem omhoog, est-ce que ervoor, "
                    "of het onderwerp achter het werkwoord.",
             waarom=[
                 None,
                 "Bij omkering met il, elle of on komt er na een klinker een -t- bij: habite-t-elle.",
                 None,
             ]),
        dict(aanpak="De ontkenning bestaat in het Frans uit twee delen: ne vóór het werkwoord en pas, plus, "
                    "jamais, rien, personne of que erachter.",
             waarom=[
                 "Let op plus de viande: na een ontkenning wordt de la gewoon de. En ne … que betekent niet "
                 "ontkennen maar beperken: alleen.",
                 None,
             ]),
        dict(aanpak="Kijk welke rol het herhaalde woord in de tweede zin speelt: onderwerp wordt qui, lijdend "
                    "voorwerp wordt que, een plaats of tijd wordt où, iets met de wordt dont.",
             waarom=[
                 None,
                 "Que is hier lijdend voorwerp van ai acheté, dus que en niet qui. Het werkwoord dat erachter "
                 "komt, verraadt het.",
                 None,
                 "Parler de wordt dont. Daarom moet je bij elk werkwoord weten of het de bij zich heeft.",
                 None,
             ]),
        dict(aanpak="De si-zin heeft drie vaste patronen. Welk je neemt, hangt af van hoe waarschijnlijk het "
                    "is: mogelijk, niet echt zo, of te laat.",
             waarom=[
                 None, None,
                 "Bij het derde patroon staat er twee keer een voltooide vorm: étions partis en aurions raté. "
                 "Dat gaat over iets dat niet meer kan.",
                 "Na si komt een tegenwoordige of een verleden tijd, nooit een futur. De futur hoort in de "
                 "hoofdzin.",
             ]),
        dict(aanpak="Loop de zin na op drie dingen: één vraagvorm per zin, één ontkennend woordje naast ne, "
                    "en de juiste tijd na si.",
             waarom=[
                 "Est-ce que en de omkering zijn twee manieren voor dezelfde vraag; je gebruikt er één.",
                 "Personne is zelf al het tweede deel van de ontkenning, dus pas valt weg.",
                 None,
                 "Qui of que hangt af van de rol: hier is le livre het lijdend voorwerp van ai lu, dus que.",
                 "In de passé composé komt rien tussen het hulpwerkwoord en het deelwoord: il n'a rien vu.",
             ]),
    ],
)
