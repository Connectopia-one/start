"""De Franstalige wereld: omgangsvormen en gewoontes — pittig (🌍 Beyond doorstroom, Frans)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lisez le dialogue.\n\n"
    "— Bonjour madame. Excusez-moi de vous déranger, pourriez-vous m'indiquer la gare, s'il vous plaît ?\n"
    "— Bien sûr. Vous continuez tout droit, puis vous tournez à gauche au deuxième feu.\n"
    "— Pardon, pourriez-vous répéter plus lentement ?\n"
    "— Tout droit, puis à gauche au deuxième feu.\n"
    "— Merci beaucoup, madame. Bonne journée !\n"
    "— Je vous en prie. Bonne journée à vous aussi."
)

TEKST2 = (
    "Lisez le texte.\n\n"
    "En France, la rentrée a lieu début septembre. Les élèves de terminale préparent le bac, qu'ils passent en juin. "
    "À midi, beaucoup d'élèves mangent à la cantine : une entrée, un plat principal et un dessert. "
    "Le 14 juillet, jour de la fête nationale, il n'y a pas d'école : c'est déjà les grandes vacances."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            tabel(
                "Is dit een hoffelijke formule uit het gesprek?",
                [
                    ("Excusez-moi de vous déranger", J),
                    ("Pourriez-vous répéter ?", J),
                    ("Tout droit", F),
                    ("Je vous en prie", J),
                ],
                "Tout droit is gewoon een wegbeschrijving.",
            ),
            mk(
                "Waarom gebruikt de vrager « pourriez-vous » en niet « pouvez-vous »?",
                ["Om beleefder te klinken", "Omdat het verleden tijd is", "Omdat het om een kind gaat", "Omdat het een bevel is"],
                0,
                "Conditionnel de politesse.",
            ),
            keuze(
                "De vrager gebruikt [[*vous|tu]] omdat hij de vrouw niet kent.",
                "Tegen een onbekende volwassene: vouvoyer.",
            ),
            mk(
                "Wat doet de vrager als hij de uitleg niet begrijpt?",
                ["Vragen om te herhalen", "Hij stopt het gesprek", "Hij vraagt het aan iemand anders", "Hij knikt toch maar"],
                0,
                "Pardon, pourriez-vous répéter plus lentement ?",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            tabel(
                "Staat dit in de tekst over de Franse school?",
                [
                    ("Het schooljaar begint begin september.", J),
                    ("Leerlingen in terminale leggen het bac af in juni.", J),
                    ("Op 14 juli is er gewoon school.", F),
                ],
                "Le 14 juillet valt in de grote vakantie.",
            ),
            inv(
                "Hoe heet het hoofdgerecht in de tekst? Antwoord in het Frans.",
                ["le plat principal", "plat principal", "un plat principal"],
                "Entrée, plat principal, dessert.",
            ),
            keuze(
                "« La rentrée » is het [[*begin|einde]] van het schooljaar.",
                "Rentrer: terugkeren.",
            ),
        ],
    ),
    tabel(
        "Tu of vous?",
        [
            ("Je praat met de bakker die je niet kent.", "vous"),
            ("Je praat met je beste vriendin.", "tu"),
            ("Je schrijft aan de directeur van een bedrijf.", "vous"),
            ("Je praat met je kleine neefje.", "tu"),
        ],
        "Vous tegen onbekende volwassenen en in formele situaties.",
        kolommen=["tu", "vous"],
    ),
    sorteer(
        "Formele of informele begroeting?",
        ["Formeel", "Informeel"],
        [
            ("Monsieur le Directeur,", "Formeel"),
            ("Coucou !", "Informeel"),
            ("Madame, Monsieur,", "Formeel"),
            ("Salut Léo !", "Informeel"),
            ("Cordialement", "Formeel"),
        ],
        "Cordialement is een vriendelijke zakelijke afsluiting.",
    ),
    mk(
        "Hoe bestel je het beleefdst in een Frans café?",
        ["Je voudrais un café, s'il vous plaît.", "Je veux un café tout de suite, monsieur.", "Donne-moi un café, s'il te plaît.", "Un café pour moi, et vite !"],
        0,
        "Je voudrais: conditionnel de politesse.",
    ),
    mk(
        "Je belt een bedrijf. Wat zeg je eerst?",
        ["Bonjour, pourrais-je parler à M. Dubois ?", "Allô, passe-moi Dubois tout de suite.", "Salut, est-ce que Dubois est là, là ?", "Dubois, vite, c'est super urgent, hein !"],
        0,
        "Eerst bonjour, dan een beleefde vraag.",
    ),
    mk(
        "« On se tutoie ? » Wat stelt de spreker voor?",
        ["Tu te gebruiken", "Samen naar buiten te gaan", "Vous te blijven gebruiken", "Elkaar een kus te geven"],
        0,
        "Tutoyer: tu zeggen.",
    ),
    mk(
        "Hoe vraag je beleefd naar iemands mening?",
        ["Qu'en pensez-vous ?", "Tais-toi et écoute.", "Tu as tort, non ?", "Pourquoi tu parles ?"],
        0,
        "Qu'en pensez-vous: wat denkt u ervan?",
    ),
    koppel(
        "Koppel het land of gebied aan wat er klopt.",
        [
            ("Québec", "Franstalig gewest in Canada"),
            ("Sénégal", "Afrikaans land met Frans als officiële taal"),
            ("la Suisse", "land met onder meer Frans en Duits"),
            ("la Wallonie", "Franstalig gewest in België"),
        ],
        ["Franstalige stad in Spanje"],
        "Het Frans is officieel op meerdere continenten.",
    ),
    tabel(
        "Zeg je dit in België of in Frankrijk?",
        [
            ("septante", "België"),
            ("soixante-dix", "Frankrijk"),
            ("nonante", "België"),
            ("quatre-vingt-dix", "Frankrijk"),
        ],
        "Belgische Franstaligen zeggen septante en nonante.",
        kolommen=["België", "Frankrijk"],
    ),
    keuze(
        "Onder vrienden geven Fransen elkaar vaak [[*la bise|een stevige handdruk]].",
        "La bise: een kus op de wang.",
    ),
    keuze(
        "In Frankrijk duurt de middagpauze traditioneel [[*vrij lang|heel kort]].",
        "Le déjeuner is er een echte maaltijd.",
    ),
    keuze(
        "« Le smic » is het [[*minimumloon|maximumloon]].",
        "Salaire minimum interprofessionnel de croissance.",
    ),
    inv(
        "Wat is de Franse nationale feestdag? Schrijf de datum, bv. 1/1.",
        ["14/7", "14 juli", "14 juillet", "14/07", "14-7"],
        "De bestorming van de Bastille in 1789.",
    ),
    inv(
        "Vul aan met twee Franse woorden: « Merci ! — De ___. »",
        ["rien"],
        "De rien: graag gedaan.",
    ),
    mk(
        "Hoeveel weken betaalde vakantie krijgt een Franse werknemer wettelijk?",
        ["Vijf", "Twee", "Geen", "Tien"],
        0,
        "Cinq semaines de congés payés.",
    ),
    mk(
        "Waarvoor staat de organisatie « la Francophonie »?",
        ["Samenwerking Franstalige landen", "Een bekende Franse radiozender", "Het officiële Franse taalexamen", "Een nationale feestdag in Québec"],
        0,
        "De Organisation internationale de la Francophonie.",
    ),
    mk(
        "Je zit vast in een Frans gesprek. Wat doe je best?",
        ["Het anders proberen te zeggen", "Stoppen met praten", "Overschakelen op het Nederlands", "Doen alsof je alles begrijpt"],
        0,
        "Omschrijven of een synoniem zoeken helpt.",
    ),
    mk(
        "Je hebt iemand op de voet getrapt. Wat zeg je?",
        ["Pardon, excusez-moi !", "De rien, madame.", "Bon appétit !", "À tout à l'heure !"],
        0,
        "Pardon en excusez-moi zijn verontschuldigingen.",
    ),
    keuze(
        "Op een mail aan je leraar zet je als afsluiting best [[*Cordialement|Bisous]].",
        "Cordialement is vriendelijk en zakelijk.",
    ),
    inv(
        "Hoe zeggen Franstalige Belgen « negentig »? Eén Frans woord.",
        ["nonante"],
        "In Frankrijk: quatre-vingt-dix.",
    ),
    volgorde(
        "Zet de delen van een formele Franse brief in de juiste volgorde.",
        ["Madame, Monsieur,", "Je me permets de vous écrire au sujet de…", "Dans l'attente de votre réponse,", "Veuillez agréer mes salutations distinguées."],
        "Aanhef, inleiding, afronding, slotformule.",
    ),
    tabel(
        "Is dit beleefd in een Frans gesprek?",
        [
            ("de ander laten uitspreken", J),
            ("je gesprekspartner aankijken", J),
            ("iemand die je niet kent meteen tutoyeren", F),
        ],
        "Wacht tot de ander voorstelt om tu te zeggen.",
    ),
    sleep(
        "In Frankrijk begint het schooljaar met [[la rentrée]]. Het laatste jaar heet [[la terminale]], en het eindexamen is [[le bac]].",
        ["le brevet", "la sixième"],
        "Het Franse secundair telt de jaren omgekeerd.",
    ),
    open_(
        "Schrijf in het Frans een beleefde vraag aan een onbekende voorbijganger: je zoekt het station.",
        "Bonjour madame, excusez-moi de vous déranger. Pourriez-vous m'indiquer où se trouve la gare, s'il vous plaît ?",
    ),
]
