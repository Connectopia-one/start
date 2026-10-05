# -*- coding: utf-8 -*-
"""Woordvelden: mens, familie, gevoelens, gezondheid en lichaamsdelen.

Uit de vakfiche Frans van de 2de graad dubbele finaliteit. De woordvelden die
hier aan bod komen: familie, gevoelens, gezondheid en lichaamsdelen,
persoonlijke gegevens, en de instructietaal die je op een examen nodig hebt.

Woordenschat leren is nooit een doel op zich, staat er bij: je hebt de woorden
nodig om teksten te begrijpen en om zelf te schrijven of te spreken. Daarom
staan de woorden hier niet in een lijst maar in een zin, en vaak in een kort
tekstje waarin ze echt iets doen.

Je mag op het examen een online woordenboek gebruiken, maar je hebt niet de
tijd om elk woord op te zoeken. Hoe rijker je woordenschat, hoe vlotter het
gaat.

Deel 1 gaat over jezelf en je gezin: persoonlijke gegevens, familie en
gevoelens. Deel 2 gaat over het lichaam en de gezondheid: bij de dokter, in de
apotheek, en wat je zegt als je je niet goed voelt.
"""

FAMILLE = (
    "Nous sommes cinq à la maison : mes parents, mon frère, ma sœur et moi. Mon frère est "
    "l'aîné, il a vingt ans. Ma sœur a huit ans, donc je suis au milieu. Mes grands-parents "
    "habitent dans la même rue, et ma tante vient manger tous les dimanches."
)
FICHE = (
    "Nom : Dubois. Prénom : Camille. Date de naissance : 14 mars 2010. Lieu de naissance : "
    "Namur. Nationalité : belge. Adresse : rue des Écoles 12, 5000 Namur. Numéro de téléphone : "
    "0470 12 34 56. Adresse mail : camille.dubois@exemple.be"
)
SENTIMENTS = (
    "Hier, j'étais vraiment fatiguée, et un peu triste aussi. Ce matin, ça va beaucoup mieux : "
    "j'ai reçu une bonne nouvelle et je suis contente. Mon frère, lui, est en colère parce que "
    "son équipe a perdu."
)

DEEL1 = [
    # --- La famille --------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {FAMILLE} » Hoeveel kinderen zijn er in dit gezin?",
         opties=["drie", "twee", "vier", "vijf"],
         antwoord=0,
         uitleg="Mes parents, mon frère, ma sœur et moi: vijf personen, waarvan twee ouders. Blijven er drie kinderen over."),
    dict(type="meerkeuze",
         vraag="Hetzelfde tekstje over het gezin. Wat betekent l'aîné?",
         opties=["de oudste", "de jongste", "de middelste", "de enige zoon"],
         antwoord=0,
         uitleg="Mon frère est l'aîné, il a vingt ans. L'aîné is de oudste van de kinderen; le cadet is de jongste."),
    dict(type="invultekst",
         vraag="Nog dat tekstje. Welk Frans woord betekent 'zus'? Schrijf het woord.",
         antwoord=["sœur", "soeur"],
         uitleg="Ma sœur. Je mag het ook soeur schrijven als je het lijfje van de œ niet vindt op je toetsenbord."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden horen bij de familie?",
         opties=["la tante",
                 "les grands-parents",
                 "le cousin",
                 "le voisin"],
         antwoord=[0, 1, 2],
         uitleg="Tante, grootouders, neef. Le voisin is de buur, en die hoort bij een ander woordveld."),
    dict(type="waarofniet",
         vraag="Mon oncle betekent mijn oom.",
         antwoord=True,
         uitleg="Un oncle is een oom, une tante een tante. Let op de stille letters: je hoort de slot-e van tante niet."),
    dict(type="meerkeuze",
         vraag="Je wil zeggen dat je een jongere broer hebt. Welke zin is juist?",
         opties=["J'ai un frère plus jeune que moi.",
                 "J'ai un frère plus vieux que moi.",
                 "Je suis un frère plus jeune.",
                 "Mon frère a un frère plus jeune."],
         antwoord=0,
         uitleg="Plus jeune que moi: jonger dan ik. De vergrotende trap maak je met plus ... que."),
    # --- Les données personnelles ------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit formulier: « {FICHE} » Wat is de familienaam van deze persoon?",
         opties=["Dubois", "Camille", "Namur", "Écoles"],
         antwoord=0,
         uitleg="Nom is de familienaam, prénom de voornaam. In het Frans staat de familienaam dus eerst."),
    dict(type="invultekst",
         vraag="Hetzelfde formulier. In welke maand is Camille geboren? Schrijf de maand in het Nederlands.",
         antwoord=["maart"],
         uitleg="Date de naissance : 14 mars 2010. Mars is maart."),
    dict(type="waarofniet",
         vraag="Op dat formulier staat bij lieu de naissance de geboorteplaats.",
         antwoord=True,
         uitleg="Un lieu is een plaats, la naissance de geboorte. Lieu de naissance : Namur."),
    dict(type="meerkeuze",
         vraag="Welke gegevens vraagt een Frans formulier als het naar je persoonlijke gegevens vraagt?",
         opties=["nom en prénom",
                 "date de naissance",
                 "adresse",
                 "matière préférée"],
         antwoord=[0, 1, 2],
         uitleg="Naam, geboortedatum en adres. Je lievelingsvak vraagt een formulier niet."),
    dict(type="meerkeuze",
         vraag="Iemand vraagt: « Quelle est votre nationalité ? » Wat antwoord je als Belg?",
         opties=["Je suis belge.", "Je suis la Belgique.", "J'habite belge.", "Je viens belge."],
         antwoord=0,
         uitleg="Een nationaliteit is in het Frans een bijvoeglijk naamwoord met een kleine letter: je suis belge, je suis française."),
    # --- Les sentiments ----------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {SENTIMENTS} » Hoe voelt de schrijfster zich vandaag?",
         opties=["blij", "moe", "verdrietig", "boos"],
         antwoord=0,
         uitleg="Je suis contente. Moe en verdrietig was ze gisteren, boos is haar broer."),
    dict(type="meerkeuze",
         vraag="Hetzelfde tekstje. Waarom is haar broer boos?",
         opties=["zijn ploeg heeft verloren",
                 "hij heeft slecht nieuws gekregen",
                 "hij is te moe",
                 "hij moet naar school"],
         antwoord=0,
         uitleg="Il est en colère parce que son équipe a perdu. Perdre is verliezen, une équipe is een ploeg."),
    dict(type="invultekst",
         vraag="Nog dat tekstje. Welke Franse uitdrukking betekent 'boos'? Vul in: « être en ... ». Schrijf één woord.",
         antwoord=["colère"],
         uitleg="Être en colère: boos zijn. Let op het accent grave op de eerste e."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden drukken een gevoel uit?",
         opties=["triste",
                 "content",
                 "fâché",
                 "lundi"],
         antwoord=[0, 1, 2],
         uitleg="Verdrietig, tevreden, kwaad. Lundi is maandag en hoort bij de dagen van de week."),
    dict(type="waarofniet",
         vraag="Avoir peur betekent 'bang worden gemaakt'.",
         antwoord=False,
         uitleg="Het betekent bang zijn, letterlijk 'angst hebben'. Het Frans gebruikt avoir waar wij 'zijn' zeggen: avoir peur, avoir faim, avoir soif."),
    dict(type="meerkeuze",
         vraag="Je wil in het Frans zeggen dat je honger hebt. Welke zin is juist?",
         opties=["J'ai faim.", "Je suis faim.", "J'ai la faim.", "Je fais faim."],
         antwoord=0,
         uitleg="Avoir faim, zonder lidwoord. Zo ook j'ai soif, j'ai froid, j'ai chaud."),
    dict(type="waarofniet",
         vraag="Je suis fatigué en je suis fatiguée klinken verschillend.",
         antwoord=False,
         uitleg="Allebei klinken ze gelijk; de extra e schrijf je omdat een vrouw het zegt. Dat is de overeenkomst van het bijvoeglijk naamwoord met het onderwerp."),
    # --- La langue des instructions -----------------------------------------
    dict(type="meerkeuze",
         vraag="Op je examen staat « Complétez le texte avec les mots suivants. » Wat moet je doen?",
         opties=["de tekst vervolledigen met de woorden die erbij staan",
                 "de tekst in het Nederlands vertalen",
                 "de woorden in de goede orde zetten",
                 "de tekst samenvatten in enkele zinnen"],
         antwoord=0,
         uitleg="Compléter is vervolledigen, suivant betekent volgend. Instructietaal is een eigen woordveld: wie de opdracht niet begrijpt, verliest punten zonder fout te maken."),
    dict(type="invultekst",
         vraag="Op een examenopdracht staat « Cochez la bonne réponse. » Welk woord betekent hier 'antwoord'? Schrijf het woord.",
         antwoord=["réponse"],
         uitleg="Cocher is aankruisen, la réponse het antwoord. Une question is de vraag."),
]

CORPS = (
    "Je me suis réveillé avec mal à la gorge et un peu de fièvre. J'ai aussi mal à la tête, "
    "surtout quand je bouge. Mes jambes vont bien, mais je n'ai pas faim du tout."
)
MEDECIN = (
    "— Bonjour, qu'est-ce qui ne va pas ? — J'ai mal au ventre depuis deux jours, docteur. — "
    "Vous avez de la fièvre ? — Non, mais je dors mal. — Je vous donne une ordonnance. Prenez "
    "un comprimé matin et soir, pendant cinq jours."
)
PHARMACIE = (
    "À la pharmacie, vous pouvez acheter du paracétamol sans ordonnance. Pour un antibiotique, "
    "il faut une ordonnance du médecin. Demandez conseil au pharmacien : il vous dira aussi "
    "combien de temps vous pouvez prendre un médicament."
)

DEEL2 = [
    # --- Le corps ----------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {CORPS} » Waar heeft deze persoon pijn?",
         opties=["aan zijn hals en zijn hoofd",
                 "aan zijn benen en zijn hoofd",
                 "aan zijn buik en zijn hals",
                 "aan zijn rug en zijn benen"],
         antwoord=0,
         uitleg="Mal à la gorge en mal à la tête. La gorge is de hals of de keel, la tête het hoofd. Mes jambes vont bien: met zijn benen is niets."),
    dict(type="invultekst",
         vraag="Hetzelfde tekstje. Welk Frans woord betekent 'koorts'? Schrijf het woord.",
         antwoord=["fièvre"],
         uitleg="Un peu de fièvre: een beetje koorts. Avoir de la fièvre is koorts hebben."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden zijn lichaamsdelen?",
         opties=["la main",
                 "le dos",
                 "le pied",
                 "le lit"],
         antwoord=[0, 1, 2],
         uitleg="Hand, rug, voet. Un lit is een bed en hoort bij het woordveld van de woning."),
    dict(type="meerkeuze",
         vraag="Hoe zeg je in het Frans « ik heb buikpijn »?",
         opties=["J'ai mal au ventre.",
                 "J'ai mal le ventre.",
                 "Je suis mal au ventre.",
                 "J'ai un ventre mal."],
         antwoord=0,
         uitleg="Avoir mal à + lidwoord. À + le wordt au: au ventre, au dos, au pied. Bij een vrouwelijk woord blijft het à la: à la tête."),
    dict(type="waarofniet",
         vraag="Avoir mal aux dents betekent oorpijn hebben.",
         antwoord=False,
         uitleg="Une dent is een tand, dus het is tandpijn. Oorpijn is avoir mal aux oreilles. À + les wordt in allebei de gevallen aux."),
    dict(type="meerkeuze",
         vraag="Welk lichaamsdeel is l'épaule?",
         opties=["de schouder", "de elleboog", "de knie", "de enkel"],
         antwoord=0,
         uitleg="Une épaule is een schouder. Le coude is de elleboog, le genou de knie, la cheville de enkel."),
    dict(type="invultekst",
         vraag="Welk Frans woord betekent 'oog'? Schrijf het woord in het enkelvoud.",
         antwoord=["œil", "oeil"],
         uitleg="Un œil, in het meervoud les yeux. Dat meervoud is onregelmatig, dus dat moet je kennen."),
    # --- Chez le médecin ----------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit gesprekje: « {MEDECIN} » Wat heeft de patiënt?",
         opties=["buikpijn sinds twee dagen",
                 "koorts sinds twee dagen",
                 "hoofdpijn sinds vijf dagen",
                 "keelpijn en koorts"],
         antwoord=0,
         uitleg="J'ai mal au ventre depuis deux jours. Depuis betekent sinds. Koorts heeft hij juist niet."),
    dict(type="meerkeuze",
         vraag="Hetzelfde gesprekje. Wat moet de patiënt doen?",
         opties=["vijf dagen lang 's morgens en 's avonds een tablet nemen",
                 "vijf dagen lang in bed blijven",
                 "twee tabletten per dag nemen tot de pijn weg is",
                 "morgen terugkomen bij de dokter"],
         antwoord=0,
         uitleg="Prenez un comprimé matin et soir, pendant cinq jours. Un comprimé is een tablet."),
    dict(type="invultekst",
         vraag="Nog dat gesprekje. Welk Frans woord betekent 'voorschrift'? Schrijf het woord.",
         antwoord=["ordonnance"],
         uitleg="Une ordonnance geeft de dokter mee naar de apotheek."),
    dict(type="waarofniet",
         vraag="In dat gesprekje vraagt de dokter « Qu'est-ce qui ne va pas ? », en dat betekent 'wat is er aan de hand?'.",
         antwoord=True,
         uitleg="Letterlijk: wat gaat er niet? Het is de gewone openingsvraag van een dokter."),
    dict(type="meerkeuze",
         vraag="Je belt in het Frans naar een dokter voor een afspraak. Welke zin past?",
         opties=["Je voudrais prendre un rendez-vous, s'il vous plaît.",
                 "Je prends un rendez-vous maintenant.",
                 "Donnez-moi un rendez-vous demain.",
                 "Tu as un rendez-vous pour moi ?"],
         antwoord=0,
         uitleg="Prendre rendez-vous is een afspraak maken. Je voudrais is hoffelijk, en tegen een onbekende blijf je bij vous."),
    # --- À la pharmacie -----------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {PHARMACIE} » Waarvoor heb je een voorschrift nodig?",
         opties=["voor een antibioticum",
                 "voor paracetamol",
                 "voor elk geneesmiddel",
                 "voor advies van de apotheker"],
         antwoord=0,
         uitleg="Pour un antibiotique, il faut une ordonnance. Paracetamol krijg je sans ordonnance, zonder voorschrift."),
    dict(type="meerkeuze",
         vraag="Hetzelfde tekstje. Welke twee dingen kan de apotheker voor je doen?",
         opties=["advies geven",
                 "zeggen hoelang je een geneesmiddel mag nemen",
                 "een voorschrift schrijven",
                 "je ziektebriefje maken"],
         antwoord=[0, 1],
         uitleg="Demandez conseil au pharmacien: il vous dira aussi combien de temps. Een voorschrift komt van de dokter."),
    dict(type="invultekst",
         vraag="Welk Frans woord betekent 'geneesmiddel'? Schrijf het woord in het enkelvoud.",
         antwoord=["médicament"],
         uitleg="Un médicament. De apotheek zelf is une pharmacie, de apotheker un pharmacien."),
    dict(type="waarofniet",
         vraag="Volgens dat tekstje kan je paracetamol alleen met een voorschrift kopen.",
         antwoord=False,
         uitleg="Sans ordonnance betekent zonder voorschrift. Net dat staat er van paracetamol."),
    dict(type="meerkeuze",
         vraag="Welke Franse zinnen zeg je als je je niet goed voelt?",
         opties=["Je ne me sens pas bien.",
                 "J'ai de la fièvre.",
                 "Je suis malade.",
                 "Je suis en vacances."],
         antwoord=[0, 1, 2],
         uitleg="Zich niet goed voelen, koorts hebben, ziek zijn. In vakantie zijn is iets heel anders."),
    dict(type="waarofniet",
         vraag="Se sentir is een wederkerend werkwoord: je me sens, tu te sens, il se sent.",
         antwoord=True,
         uitleg="Het wederkerend voornaamwoord verandert mee met de persoon. Zonder dat woordje zegt de zin niets."),
    dict(type="meerkeuze",
         vraag="Je bent op reis in Frankrijk en je hebt een dokter nodig. Welke vraag stel je aan iemand op straat?",
         opties=["Excusez-moi, où est le médecin le plus proche ?",
                 "Excusez-moi, vous êtes médecin ?",
                 "Pardon, je cherche la pharmacie de garde ?",
                 "Bonjour, j'ai mal à la tête."],
         antwoord=0,
         uitleg="Le plus proche is de naastbijzijnde: dat is wat je wil weten. De derde zin is geen volledige vraag, en de vierde vertelt alleen wat je voelt."),
    dict(type="invultekst",
         vraag="Welk Frans woord betekent 'ziek'? Schrijf het woord.",
         antwoord=["malade"],
         uitleg="Je suis malade. Hetzelfde woord voor een man en een vrouw: het eindigt al op een e."),
]
