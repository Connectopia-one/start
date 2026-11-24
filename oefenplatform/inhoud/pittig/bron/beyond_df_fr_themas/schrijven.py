"""Schrijven en spreken in het Frans — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis le mail de Noah.\n\nMadame Dupont,\n\nJ'ai vu votre annonce pour un baby-sitter sur le site de l'école. J'ai dix-sept ans et je m'occupe souvent de mes petits frères. "
        "Je suis libre le mercredi après-midi et le week-end. Pourriez-vous me dire combien vous payez par heure ?\n\n"
        "Merci d'avance pour votre réponse.\n\nCordialement,\nNoah Peeters",
        [
            keuze("Het register van deze mail is [[*formeel|informeel]].", "Madame Dupont, vous en Cordialement."),
            keuze("Noah gebruikt de [[*vous-vorm|tu-vorm]] omdat hij Madame Dupont niet goed kent.", "Vous bij een onbekende volwassene."),
            mk("Wat vraagt Noah aan Madame Dupont?",
               ["hoeveel ze per uur betaalt", "of hij op woensdag mag beginnen", "hoe oud haar kinderen zijn", "waar ze precies woont"], 0,
               "Combien vous payez par heure."),
            keuze("« Pourriez-vous me dire » staat in de [[*conditionnel de politesse|futur simple]].", "Hoffelijk vragen."),
            mk("Welke zin hoort bij het slot van de mail?",
               ["Merci d'avance pour votre réponse.", "J'ai vu votre annonce sur le site.", "J'ai dix-sept ans et je garde mes frères.", "Je suis libre le mercredi après-midi."], 0,
               "Een slotzin kijkt uit naar een antwoord."),
        ],
    ),
    tabel("Is dit een goede strategie bij een Franse schrijfopdracht?", [
        ("eerst een lijstje kernwoorden maken", J), ("de opgegeven lengte negeren", F),
        ("je tekst nalezen voor je hem inlevert", J), ("in een formele mail tu schrijven", F),
    ], "Plannen, de lengte respecteren, nalezen en vous in een formele mail."),
    volgorde("Zet de stappen van een schrijfopdracht in de juiste volgorde.", [
        "nadenken waarom en voor wie je schrijft", "een lijstje kernwoorden maken", "de tekst schrijven", "de tekst nalezen",
    ], "Eerst het communicatiemodel, dan plannen, schrijven en nalezen."),
    sorteer("Hoort het bij een formele of een informele Franse mail?", ["formeel", "informeel"], [
        ["Madame, Monsieur,", "formeel"], ["Salut Tom,", "informeel"], ["Cordialement,", "formeel"],
        ["Bisous,", "informeel"], ["Merci d'avance.", "formeel"], ["À plus !", "informeel"],
    ], "Formeel tegenover een onbekende, informeel tegenover een vriend."),
    koppel("Koppel elke Franse zin aan wat je ermee doet.", [
        ["Pourriez-vous m'indiquer la gare ?", "informatie vragen"], ["Tu devrais essayer, c'est moins cher.", "overtuigen"],
        ["Je trouve que c'est injuste.", "een mening geven"], ["J'ai vu un accident hier soir.", "iets vertellen"],
    ], ["iemand bedanken"], "Elke zin heeft een eigen doel."),
    koppel("Koppel elke uitdrukking aan haar gebruik.", [
        ["Je suis désolé.", "je verontschuldigen"], ["Ce n'est pas grave.", "reageren op een verontschuldiging"],
        ["Beau travail !", "iemand feliciteren"], ["Tu viens samedi ?", "iemand uitnodigen"],
    ], ["afscheid nemen"], "Sociale contacten in het Frans."),
    mk("Je verstaat je gesprekspartner niet goed. Wat zeg je?",
       ["Pouvez-vous répéter, s'il vous plaît ?", "Je ne comprends rien, au revoir et merci !", "Arrête de parler, s'il te plaît, merci.", "Tu parles très mal le français, je trouve."], 0,
       "Vraag beleefd om herhaling."),
    mk("Je kent het Franse woord voor « ladder » niet. Wat doe je in je tekst?",
       ["het omschrijven met woorden die je wel kent", "het Nederlandse woord gewoon in de zin laten staan", "de hele zin dan maar uit de tekst weglaten", "stoppen met schrijven en iets anders doen"], 0,
       "Bereik je doel met wat je al kent."),
    mk("Je vriend vraagt of hij met de trein moet gaan. Welke zin overtuigt?",
       ["Tu devrais prendre le train, c'est plus rapide.", "Le train part à huit heures et quart du matin.", "Le billet de train coûte vingt euros en tout, aller.", "Est-ce qu'il y a un train demain matin ou pas ?"], 0,
       "Een aanbeveling met een argument."),
    mk("Welke van deze zinnen legt iets uit?",
       ["Prenez le premier chemin à droite.", "J'adore marcher dans la forêt le dimanche.", "Hier, nous avons vu un cerf dans la forêt.", "Tu viens marcher avec nous demain ?"], 0,
       "Een uitleg gebruikt vaak de imperatief."),
    mk("Je schrijft een formele mail. Hoe begin je als je de naam niet kent?",
       ["Madame, Monsieur,", "Salut tout le monde,", "Coucou à vous deux,", "Cher ami de l'hôtel,"], 0,
       "Madame, Monsieur zonder naam."),
    inv("Vul de hoffelijke vorm in: « ___ -vous m'aider, s'il vous plaît ? » (pouvoir) Eén woord.", ["pourriez", "Pourriez"],
        "Pourriez-vous."),
    inv("Vul in: « Je vous ___ de votre aide. » Formeel bedanken, van remercier. Eén woord.", ["remercie"], "Je vous remercie."),
    inv("Vul in: « Je ___ que c'est une bonne idée. » Een mening, van trouver. Eén woord.", ["trouve"], "Je trouve que."),
    inv("Hoe zeg je een mail in het Frans van Québec? Eén woord.", ["courriel", "un courriel"], "Un courriel."),
    inv("Vul in: « Pouvez-vous parler plus ___ ? » (trager) Eén woord.", ["lentement"], "Lentement: traag."),
    inv("Hoe zeg je in het Frans « alstublieft » bij de vous-vorm? Vier woorden.", ["s'il vous plaît", "s'il vous plait"],
        "S'il vous plaît; bij tu: s'il te plaît."),
    keuze("In een mail aan een vriend schrijf je [[*Salut|Madame, Monsieur]].", "Informeel."),
    keuze("Spelfouten mogen bij het examen [[*het tekstbegrip niet in de weg staan|nooit voorkomen]].", "Foutloos hoeft niet, duidelijk wel."),
    keuze("Bij een spreekopdracht tellen [[*je uitspraak en je lichaamstaal|alleen je woorden]] mee.", "Ook spreektempo en intonatie."),
    keuze("In een gesprek [[*toon je interesse|zeg je enkel wat jij wil]] in wat de ander zegt.", "Speel in op de ander."),
    keuze("« Je [[*souhaiterais|souhaiterai]] réserver une table. » Je vraagt hoffelijk.", "Conditionnel: -ais."),
    tabel("Is dit een goede zin om een vriend te overtuigen om mee te gaan wandelen?", [
        ("C'est gratuit et il fait beau.", J), ("Quelle est ton adresse ?", F),
        ("Tu devrais venir, ce sera chouette !", J), ("La forêt a un site internet.", F),
    ], "Overtuigen: een argument of een aanbeveling geven."),
    sleep("Salut Emma,\n\nMerci [[pour]] ton message ! [[D'abord]], je vais à Paris. [[Ensuite]], je vais à Lyon.\n\nBisous, Mia",
          ["de la", "Cependant"], "Merci pour; d'abord en ensuite zetten de stappen op een rij."),
    open_("Je schreef een mail aan een hotel. Leg in het Nederlands uit waarom je « je voudrais » schrijft en niet « je veux ».",
          "Je voudrais is de conditionnel de politesse en klinkt hoffelijk; je veux klinkt bot.",
          "Je past je taal aan de ontvanger aan."),
    tabel("Hoort dit bij een goede tekststructuur?", [
        ("een inleiding, een midden en een slot", J), ("signaalwoorden zoals d'abord en enfin", J), ("geen titel en geen alinea's", F),
    ], "Inleiding, midden en slot met duidelijke tekstverbanden."),
]
