"""Tekstsoorten en de bedoeling van een tekst — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis les trois petits textes.\n\nTexte A : « Ne ratez pas la Fête d'été ! Musique, jeux et les meilleures frites de la ville. Venez avec vos amis ! »\n"
        "Texte B : « Prenez un comprimé deux fois par jour après le repas. Ne pas utiliser plus de cinq jours. »\n"
        "Texte C : « Je suis allé à la Fête d'été l'année dernière. À mon avis, la musique était trop forte, mais les frites étaient délicieuses. »",
        [
            keuze("Texte A is [[*persuasief|prescriptief|narratief]].", "Een oproep met wervende woorden."),
            keuze("Texte B is [[*prescriptief|informatief|literair]].", "Une notice zegt wat je moet doen."),
            keuze("Texte C is [[*opiniërend|persuasief|prescriptief]].", "À mon avis verraadt een mening."),
            mk("Welke zin uit de teksten is een feit?",
               ["Je suis allé à la Fête d'été l'année dernière.", "À mon avis, la musique était trop forte.",
                "Les frites étaient délicieuses, vraiment très bonnes.", "Les meilleures frites de toute la ville."], 0,
               "Dat iemand ging, kan je nakijken; de rest is een oordeel."),
            mk("Voor wie is Texte B bedoeld?",
               ["iemand die het geneesmiddel neemt", "de organisatoren van de Fête d'été", "de vrienden van de schrijver", "iemand die frieten wil bakken"], 0,
               "Une notice is voor de gebruiker van het middel."),
        ],
    ),
    tabel("Welke tekstsoort is het?", [
        ("la météo à la radio", "informatief"), ("une affiche : Inscris-toi à notre club de foot !", "persuasief"),
        ("les règles d'un jeu de société", "prescriptief"), ("une nouvelle sur un chien perdu", "literair"),
    ], "Weerbericht informeert, affiche overtuigt, spelregels schrijven voor, een kortverhaal is literair.",
        kolommen=["informatief", "persuasief", "prescriptief", "literair"]),
    sorteer("Feit of mening?", ["feit", "mening"], [
        ["Paris est la capitale de la France.", "feit"], ["Paris est la ville la plus agréable.", "mening"],
        ["Le film dure deux heures.", "feit"], ["Le film est beaucoup trop long.", "mening"],
        ["L'eau bout à 100 °C.", "feit"], ["L'eau froide est meilleure.", "mening"],
    ], "Een feit kan je nakijken; een mening is een oordeel."),
    sorteer("Formeel of informeel?", ["formeel", "informeel"], [
        ["Madame, Monsieur,", "formeel"], ["Salut Lucas !", "informeel"], ["Cordialement,", "formeel"],
        ["Bisous !", "informeel"], ["Je voudrais vous demander", "formeel"], ["Ça te dit ?", "informeel"],
    ], "Formele woorden en vous voor een onbekende, tu en informele woorden voor vrienden."),
    koppel("Koppel elke Franse tekst aan zijn bedoeling.", [
        ["une recette", "uitleggen hoe iets moet"], ["une publicité", "overtuigen"], ["un journal télévisé", "informeren"], ["un avis sur un hôtel", "een mening geven"],
    ], ["een vriend uitnodigen"], "Elke tekstsoort heeft zijn eigen bedoeling."),
    mk("Lees: « Tournez à gauche après l'église et continuez tout droit sur 200 mètres. » Welke tekstsoort is dit?",
       ["prescriptief", "opiniërend", "narratief", "persuasief en literair"], 0, "Een wegbeschrijving zegt wat je moet doen."),
    mk("Lees: « Quand j'ai ouvert la porte, un chat inconnu dormait sur mon lit. » Welke tekstsoort is dit?",
       ["narratief", "prescriptief", "informatief", "persuasief en literair"], 0, "Een verhaal over wat er gebeurde."),
    mk("Lees: « Franchement, c'est la pire pizza que j'ai mangée. » Welk woord verraadt vooral een mening?",
       ["pire", "la pizza", "j'ai mangée", "c'est"], 0, "La pire is een oordeel."),
    mk("Lees: « Les élèves doivent porter leur badge en permanence. » Waar vind je deze zin?",
       ["in een schoolreglement", "in een kortverhaal over een school", "in een recensie van een school", "in een gedicht over een badge"], 0,
       "Doivent: een regel."),
    mk("Lees: « En forme en 30 jours avec notre nouvelle appli ! Téléchargez-la gratuitement. » Wat is de bedoeling van de schrijver?",
       ["je overhalen om de app te downloaden", "je vertellen hoe een app gebouwd wordt", "een verhaal vertellen over sporten", "je mening vragen over de app"], 0,
       "Reclame wil je overtuigen."),
    mk("Lees: « Coucou mamie, merci pour le joli pull ! Il est très chaud. Bisous, Lucie » Welk register is dit?",
       ["informeel", "formeel", "zeer formeel", "zakelijk en neutraal"], 0, "Coucou, merci en bisous horen bij familie."),
    mk("Je schrijft een mail aan de directeur van een hotel. Welke slotformule past het best?",
       ["Cordialement, Tom Janssens", "Bisous et à plus tard, mon ami !", "Salut, à la prochaine fois au café !", "Réponds-moi vite, d'accord, merci !"], 0,
       "Formeel en hoffelijk."),
    mk("Lees: « La lune était une pièce d'argent dans le ciel noir. » Waarom is dit literair?",
       ["het gebruikt een beeld", "het geeft een feit over de maan", "het geeft je een opdracht", "het wil je iets verkopen"], 0,
       "Une pièce d'argent is een beeld."),
    mk("Lees: « Des milliers de touristes visitent Bruges chaque été. La ville a beaucoup de vieux canaux. » Welke tekstsoort is dit?",
       ["informatief", "opiniërend, want het noemt een stad", "prescriptief, want het zegt wat je moet bezoeken", "literair, want het gaat over een mooie stad"], 0,
       "Twee feiten, geen oordeel en geen opdracht."),
    inv("Hoe noem je een tekst die je wil doen kopen of stemmen? Eén woord.", ["persuasief", "persuasieve"], "Persuasief: overtuigend."),
    inv("Vul in: « Je ___ que c'est une bonne idée. » Een woord dat een mening aankondigt, van penser. Eén woord.", ["pense"], "Je pense que."),
    keuze("Een krantenartikel over een treinstaking is meestal [[*informatief|literair]].", "Het geeft informatie."),
    keuze("Een chanson over liefdesverdriet is [[*literair|prescriptief]].", "Liederen zijn literaire teksten."),
    keuze("Een getuigenis over je eerste werkdag is [[*narratief|prescriptief]].", "Je vertelt wat er gebeurde."),
    keuze("« Je trouve que » kondigt [[*een mening|een feit]] aan.", "Net als à mon avis."),
    keuze("In een mail aan een onbekende volwassene gebruik je de [[*vous-vorm|tu-vorm]].", "Vous is beleefd."),
    tabel("Lees: « La nouvelle bibliothèque a ouvert en mai. Elle a 20 000 livres et une salle d'étude. Je pense que c'est le meilleur endroit pour étudier. » Feit of mening?", [
        ("La bibliothèque a ouvert en mai.", "feit"), ("Elle a 20 000 livres.", "feit"), ("C'est le meilleur endroit pour étudier.", "mening"),
    ], "Je pense que kondigt de mening aan.", kolommen=["feit", "mening"]),
    tabel("Hoort dit in een formele Franse mail?", [
        ("Je vous remercie de votre aide.", J), ("Salut, ça va ?", F), ("Pourriez-vous m'envoyer", J), ("À plus !", F),
    ], "Hoffelijke vous-vormen horen in een formele mail."),
    volgorde("Zet de delen van een formele Franse mail in de juiste volgorde.", [
        "Madame, Monsieur,", "Je vous écris au sujet du job d'été.", "Merci d'avance pour votre réponse.", "Cordialement,", "Sara Peeters",
    ], "Aanspreking, inleiding, slotzin, groet, naam."),
    mk("Lees: « Comment fabriquer un avion en papier : 1. Pliez la feuille en deux. 2. Pliez les coins. » Wat vertelt de titel je al?",
       ["dat het om instructies gaat", "dat het een verhaal over vliegen is", "dat de schrijver een mening geeft", "dat het een reclame voor papier is"], 0,
       "Comment + infinitief kondigt een handleiding aan."),
    open_("Lees: « Notre ville a besoin d'un nouveau skatepark. Les jeunes n'ont nulle part où aller et l'ancien parc est dangereux. Signez notre pétition ! » Leg in het Nederlands uit welke tekstsoort dit is en hoe je dat weet.",
          "Het is persuasief: de schrijver geeft argumenten en roept je op om de petitie te tekenen.",
          "Argumenten plus een oproep: overtuigen."),
]
