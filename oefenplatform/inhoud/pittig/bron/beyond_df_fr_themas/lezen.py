"""Een Franse tekst lezen — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis le texte.\n\n« De plus en plus de jeunes Belges ont un petit job le week-end. La plupart travaillent dans un magasin ou dans un café. "
        "Ils gagnent leur propre argent et ils apprennent à parler avec les clients. Par contre, les professeurs sont inquiets : "
        "les élèves qui travaillent plus de dix heures par semaine sont souvent fatigués en classe. Donc, un petit job, oui, mais l'école d'abord ! »",
        [
            mk("Wat is het onderwerp van de tekst?",
               ["bijbaantjes van jongeren", "de klanten van Belgische cafés", "de punten van Belgische leerlingen", "het weekend van leraren"], 0,
               "De hele tekst gaat over jongeren met een bijbaantje."),
            mk("Wat is de hoofdgedachte?",
               ["Een klein bijbaantje mag, maar school gaat voor.", "Jongeren moeten in het weekend in een winkel werken.",
                "Leraren willen dat leerlingen meer geld verdienen.", "Wie werkt, is nooit moe in de klas."], 0,
               "Het slot vat de boodschap samen."),
            keuze("« Par contre » kondigt een [[*tegenstelling|opsomming|reden]] aan.", "Na de voordelen komt de zorg."),
            keuze("« Donc » geeft [[*een gevolg|een voorbeeld]].", "Donc: dus."),
            inv("Vanaf hoeveel uur per week zijn leerlingen volgens de tekst vaak moe? Geef het getal.", ["10", "tien"],
                "Plus de dix heures par semaine."),
        ],
    ),
    casus(
        "Lis le message sur le site de la piscine.\n\n« À partir du lundi 4 mars, la piscine sera fermée pour travaux. "
        "La salle de sport et les terrains de tennis restent ouverts. Nos membres peuvent nager gratuitement à la piscine de Jambes pendant cette période. "
        "Montrez votre carte à l'accueil. Nous espérons rouvrir le 1er avril. Merci de votre compréhension ! »",
        [
            mk("Wat is gesloten vanaf 4 maart?",
               ["het zwembad", "de sportzaal en het zwembad", "de tennisvelden achter de zaal", "het hele sportcentrum"], 0,
               "Enkel la piscine sluit."),
            keuze("« gratuitement » betekent [[*gratis|tegen betaling]].", "Gratuit: gratis."),
            mk("Wat moeten leden in Jambes doen?",
               ["hun kaart tonen aan het onthaal", "vooraf een plaats reserveren", "een extra bijdrage betalen", "hun eigen handdoek en badmuts meebrengen"], 0,
               "Montrez votre carte à l'accueil."),
            keuze("Het zwembad gaat normaal weer open op [[*1 april|4 maart|1 maart]].", "Rouvrir le 1er avril."),
            keuze("« pour travaux » : het zwembad wordt [[*hersteld|verkocht|gesloopt]].", "Travaux: werken."),
        ],
    ),
    mk("Lees: « Jules a acheté une guitare d'occasion. Elle n'était pas chère, mais elle sonne très bien. » Naar wat verwijst elle?",
       ["de gitaar", "het geld dat Jules betaalde", "de winkel waar Jules was", "het lied dat Jules speelt"], 0,
       "Elle zoekt een vrouwelijk woord in de zin ervoor: une guitare."),
    mk("Lees: « Emma et son cousin sont allés au zoo. Leurs animaux préférés étaient les pingouins. » Naar wie verwijst leurs?",
       ["Emma en haar neef", "alleen Emma", "de pinguïns in de zoo", "de mensen van de zoo"], 0,
       "Leurs is meervoud en verwijst naar de twee personen."),
    mk("Lees: « La route était bloquée, donc nous avons pris un autre chemin. » Wat betekent bloquée?",
       ["versperd", "pas aangelegd", "heel erg druk", "goed verlicht"], 0, "Het gevolg verraadt de betekenis."),
    mk("Lees: « Entrée : 12 euros pour les adultes. Gratuit pour les enfants de moins de cinq ans. » Hoeveel betaalt een kind van drie?",
       ["niets", "12 euro", "de helft van 12 euro", "5 euro"], 0, "Moins de cinq ans: gratis."),
    mk("Lees: « Je voulais aller à la plage. Mais finalement, je suis resté à la maison pour ranger ma chambre. » Wat deed de schrijver?",
       ["thuisblijven en opruimen", "naar het strand gaan", "eerst opruimen en dan naar het strand", "naar het strand met een vriend"], 0,
       "Mais finalement: maar uiteindelijk."),
    mk("Lees: « Les sacs en plastique sont dangereux pour la mer. Par exemple, les tortues les mangent souvent. » Wat doet de tweede zin?",
       ["een voorbeeld geven", "een tegenstelling geven", "het besluit van de tekst geven", "een nieuw onderwerp beginnen"], 0,
       "Par exemple kondigt een voorbeeld aan."),
    tabel("Lees: « Notre café est ouvert tous les jours de 8 h à 18 h, sauf le mercredi. Nous vendons du café, du thé et des gâteaux maison. » Klopt dit?", [
        ("Het café is op woensdag gesloten.", J), ("Je kan er om 19 uur nog binnen.", F),
        ("Ze verkopen zelfgemaakte taart.", J), ("Het café is ook op zondag open.", J),
    ], "Sauf le mercredi; open tot 18 uur."),
    tabel("Lees: « Léo a quinze ans. Il habite à Liège avec sa mère et ses deux sœurs. Son père habite en Espagne. » Klopt dit?", [
        ("Léo heeft twee zussen.", J), ("Léo woont bij zijn papa.", F), ("Léo's papa woont in Spanje.", J),
    ], "Son père habite en Espagne; Léo woont bij zijn mama."),
    tabel("Lees: « Le festival a récolté 5 000 euros pour l'hôpital. Il faisait beau et beaucoup de gens portaient un chapeau. » Hoofdzaak of bijzaak?", [
        ("Het festival bracht geld op voor het ziekenhuis.", "hoofdzaak"),
        ("Het was mooi weer.", "bijzaak"),
        ("Veel mensen droegen een hoed.", "bijzaak"),
    ], "Het geld voor het ziekenhuis is de boodschap.", kolommen=["hoofdzaak", "bijzaak"]),
    koppel("Koppel elk Frans signaalwoord aan wat het aankondigt.", [
        ["mais", "een tegenstelling"], ["donc", "een gevolg"], ["parce que", "een reden"], ["enfin", "de laatste stap"],
    ], ["een vraag"], "Signaalwoorden tonen hoe zinnen samenhangen."),
    volgorde("Lees: « Après le déjeuner, nous avons visité le château. Le matin, nous avons pris le train pour Dinant. Le soir, nous avons mangé au bord de la Meuse. » Zet de activiteiten in de juiste volgorde.", [
        "de trein naar Dinant nemen", "het kasteel bezoeken", "eten aan de Maas",
    ], "Le matin, après le déjeuner, le soir."),
    inv("Lees: « Le bus part à 7 h 45 et le trajet dure vingt minutes. » Hoe laat komt de bus aan? Schrijf als 8.05.", ["8.05", "8:05", "8u05", "8 h 05"],
        "7.45 + 20 minuten = 8.05."),
    inv("Lees: « Ma grand-mère a quatre-vingts ans, mais elle va encore nager deux fois par semaine. » Hoeveel keer per week gaat ze zwemmen? Geef het getal.", ["2", "twee"],
        "Deux fois: twee keer."),
    keuze("Lees: « Sam était nerveux avant l'examen. Ses mains tremblaient. » Nerveux betekent [[*zenuwachtig|blij|moe]].",
          "Trillende handen verraden de betekenis."),
    keuze("Lees: « D'abord, rince les bouteilles. Puis, mets-les dans le sac bleu. » Wat doe je eerst? [[*de flessen uitspoelen|de flessen in de blauwe zak steken]].",
          "D'abord: eerst."),
    keuze("Lees: « Le match a été annulé à cause de la neige. » À cause de geeft een [[*oorzaak|gevolg]].", "À cause de: wegens."),
    keuze("Lees: « Malgré la pluie, nous sommes sortis. » Malgré betekent [[*ondanks|dankzij|tijdens]].", "Een tegenstelling."),
    mk("Lees: « Mia est infirmière. Chaque nuit, elle soigne des patients à l'hôpital de la ville. » Welke informatie is een hoofdpunt?",
       ["Mia werkt als verpleegster", "het ziekenhuis ligt in de stad", "Mia werkt zowel 's nachts als overdag", "Mia lag zelf ooit in het ziekenhuis"], 0,
       "Het beroep is de kern; waar het ziekenhuis ligt is een detail."),
    inv("Lees: « Elle était malheureuse, mais aujourd'hui elle est contente. » Welk Frans woord in de zin betekent het omgekeerde van malheureuse? Eén woord.", ["contente"],
        "Contente: blij, tevreden."),
    open_("Lees: « L'année dernière, Tom a oublié son passeport, donc il a raté son avion pour Rome. Cette année, il l'a préparé une semaine avant. » Leg in het Nederlands uit waarom Tom dit jaar zo vroeg was.",
          "Omdat hij vorig jaar zijn paspoort vergat en daardoor zijn vlucht miste.",
          "Donc geeft het gevolg; de tweede zin toont wat hij eruit leerde."),
]
