# -*- coding: utf-8 -*-
"""Woordvelden: onderwijs, beroepen, werk, multimedia, sport en ontspanning.

Uit de vakfiche Frans van de 2de graad dubbele finaliteit. De woordvelden die
hier aan bod komen: onderwijs en vorming; de professionele wereld met de
beroepen; communicatie en multimedia; en sport en ontspanning.

Dit zijn de woorden waarmee je over jezelf en je toekomst spreekt. Ze komen op
het examen terug in een mail over een vakantiejob, in een verslag over je
stage, in een zoekertje, in een gesprek over wat je graag doet.

Deel 1 gaat over school en over de beroepen. Deel 2 gaat over werken en
solliciteren, over communicatie en multimedia, en over sport en vrije tijd.
"""

ECOLE = (
    "Je suis en quatrième année. Mes cours préférés sont le français et les sciences. Les maths, "
    "c'est plus difficile pour moi, mais j'ai un bon professeur. Nous avons cours de huit heures "
    "vingt à quatre heures, avec une heure de midi. Le mercredi, on finit à midi."
)
BULLETIN = (
    "Bulletin du premier trimestre — Français : 14/20. Mathématiques : 11/20. Sciences : 16/20. "
    "Éducation physique : 15/20. Remarque du titulaire : élève attentif, mais doit rendre ses "
    "devoirs à temps."
)
METIERS = (
    "Dans ma famille, tout le monde travaille avec les mains. Mon père est électricien, ma mère "
    "est infirmière et mon oncle est boulanger. Moi, je voudrais devenir éducateur. Ma sœur, "
    "elle, veut travailler dans un bureau."
)

DEEL1 = [
    # --- À l'école ----------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {ECOLE} » Welke vakken doet deze leerling het liefst?",
         opties=["Frans en wetenschappen",
                 "wiskunde en Frans",
                 "wetenschappen en wiskunde",
                 "Frans en lichamelijke opvoeding"],
         antwoord=0,
         uitleg="Mes cours préférés sont le français et les sciences. Préféré betekent favoriet."),
    dict(type="meerkeuze",
         vraag="Hetzelfde tekstje. Hoe laat is de school op woensdag gedaan?",
         opties=["om twaalf uur", "om vier uur", "om acht uur twintig", "om één uur"],
         antwoord=0,
         uitleg="Le mercredi, on finit à midi. Midi is twaalf uur 's middags; minuit is middernacht."),
    dict(type="invultekst",
         vraag="Nog dat tekstje. Welk Frans woord betekent 'leraar'? Schrijf het woord zonder lidwoord.",
         antwoord=["professeur"],
         uitleg="Un professeur, in het dagelijks Frans vaak un prof."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden horen bij onderwijs en vorming?",
         opties=["un cours",
                 "un devoir",
                 "un bulletin",
                 "un loyer"],
         antwoord=[0, 1, 2],
         uitleg="Een les, een taak, een rapport. Un loyer is de huurprijs van een woning."),
    dict(type="waarofniet",
         vraag="Une année scolaire is een schooljaar.",
         antwoord=True,
         uitleg="Scolaire komt van école. Een schooldag is une journée scolaire."),
    dict(type="meerkeuze",
         vraag=f"Lees dit rapport: « {BULLETIN} » Voor welk vak staat het hoogste cijfer?",
         opties=["wetenschappen", "Frans", "wiskunde", "lichamelijke opvoeding"],
         antwoord=0,
         uitleg="Sciences : 16/20, hoger dan de drie andere."),
    dict(type="meerkeuze",
         vraag="Hetzelfde rapport. Wat moet deze leerling volgens de titularis beter doen?",
         opties=["zijn taken op tijd afgeven",
                 "beter opletten in de les",
                 "meer vragen stellen",
                 "zijn cijfer voor wiskunde ophalen"],
         antwoord=0,
         uitleg="Doit rendre ses devoirs à temps: moet zijn taken op tijd inleveren. Attentief is hij juist wel: élève attentif."),
    dict(type="invultekst",
         vraag="Nog dat rapport. Welk Frans woord betekent 'trimester'? Schrijf het woord zonder lidwoord.",
         antwoord=["trimestre"],
         uitleg="Le premier trimestre is het eerste trimester. Un semestre is een halfjaar."),
    dict(type="waarofniet",
         vraag="Une remarque op een Frans rapport is een cijfer.",
         antwoord=False,
         uitleg="Une remarque is een opmerking, van remarquer, opmerken. Een cijfer is une note. De titulaire is de klastitularis."),
    dict(type="meerkeuze",
         vraag="Je wil in het Frans zeggen in welk jaar je zit. Welke zin is juist?",
         opties=["Je suis en quatrième année.",
                 "J'ai quatrième année.",
                 "Je fais la quatrième année.",
                 "Je suis quatre années."],
         antwoord=0,
         uitleg="Être en + rangtelwoord + année. Quatrième is het rangtelwoord van quatre."),
    dict(type="invultekst",
         vraag="Welk Frans woord betekent 'examen'? Schrijf het woord zonder lidwoord.",
         antwoord=["examen"],
         uitleg="Un examen, met een stille n op het einde. Une interrogation is een overhoring."),
    # --- Les métiers ----------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {METIERS} » Welk beroep heeft de moeder?",
         opties=["verpleegkundige", "elektricien", "bakker", "opvoeder"],
         antwoord=0,
         uitleg="Ma mère est infirmière. Un infirmier, une infirmière: verpleegkundige."),
    dict(type="meerkeuze",
         vraag="Hetzelfde tekstje. Wat wil de schrijver worden?",
         opties=["opvoeder", "bakker", "elektricien", "iets op een bureau"],
         antwoord=0,
         uitleg="Je voudrais devenir éducateur. Devenir is worden. Zijn zus wil op een bureau werken."),
    dict(type="invultekst",
         vraag="Nog dat tekstje. Welk Frans woord betekent 'bakker'? Schrijf het woord zonder lidwoord.",
         antwoord=["boulanger"],
         uitleg="Un boulanger werkt in une boulangerie."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden zijn beroepen?",
         opties=["un vendeur",
                 "un coiffeur",
                 "un cuisinier",
                 "un bureau"],
         antwoord=[0, 1, 2],
         uitleg="Verkoper, kapper, kok. Un bureau is een bureau of een kantoor, dus een plaats."),
    dict(type="waarofniet",
         vraag="Een beroepsnaam in het Frans verandert mee met het geslacht: un vendeur, une vendeuse.",
         antwoord=True,
         uitleg="Zo ook un coiffeur, une coiffeuse en un infirmier, une infirmière. Een paar namen blijven gelijk, zoals un médecin."),
    dict(type="meerkeuze",
         vraag="Hoe zeg je in het Frans « ik zou graag kok worden »?",
         opties=["Je voudrais devenir cuisinier.",
                 "Je voudrais un cuisinier.",
                 "Je deviens cuisinier déjà.",
                 "Je suis devenu cuisinier demain."],
         antwoord=0,
         uitleg="Na devenir komt de beroepsnaam zonder lidwoord: devenir cuisinier, être infirmière."),
    dict(type="waarofniet",
         vraag="Un ouvrier is een werkloze.",
         antwoord=False,
         uitleg="Un ouvrier is een arbeider. Werkloos is au chômage: être au chômage."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden horen bij de professionele wereld?",
         opties=["un salaire",
                 "un contrat",
                 "un horaire",
                 "un trimestre"],
         antwoord=[0, 1, 2],
         uitleg="Loon, contract, uurregeling. Un trimestre hoort bij de school."),
    dict(type="invultekst",
         vraag="Welk Frans woord betekent 'werk' of 'arbeid'? Schrijf het woord zonder lidwoord.",
         antwoord=["travail"],
         uitleg="Le travail, van het werkwoord travailler. In het meervoud wordt het les travaux."),
]

STAGE = (
    "Mon stage s'est bien passé. Le premier jour, j'avais peur de mal faire, mais l'équipe m'a "
    "aidé. J'ai appris à répondre au téléphone et à classer des documents. Ce que j'ai trouvé "
    "difficile, c'est de rester assis toute la journée. Je recommencerais quand même."
)
ANNONCE = (
    "Magasin de sport cherche étudiant pour les samedis. Tâches : accueillir les clients, "
    "ranger les rayons, aider à la caisse. Expérience non exigée. Envoyez votre CV par mail "
    "avant le 15 du mois."
)
NUMERIQUE = (
    "Pour vous inscrire, créez un compte avec votre adresse mail. Vous recevrez un message avec "
    "un lien. Si le message n'arrive pas, regardez dans les courriers indésirables. N'envoyez "
    "jamais votre mot de passe par mail."
)
SPORT = (
    "Je joue au basket depuis cinq ans, deux fois par semaine. Le samedi, il y a souvent un "
    "match. Quand je ne joue pas, je regarde des séries ou je lis. Ma sœur, elle, fait de la "
    "danse et joue du piano."
)

DEEL2 = [
    # --- Le stage et le travail ------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit verslagje: « {STAGE} » Wat vond deze leerling moeilijk?",
         opties=["de hele dag stilzitten",
                 "de telefoon opnemen",
                 "documenten klasseren",
                 "met de ploeg samenwerken"],
         antwoord=0,
         uitleg="Ce que j'ai trouvé difficile, c'est de rester assis toute la journée. Rester assis is blijven zitten."),
    dict(type="meerkeuze",
         vraag="Hetzelfde verslagje. Wat heeft de leerling geleerd?",
         opties=["de telefoon opnemen",
                 "documenten klasseren",
                 "de klanten begroeten",
                 "met een kassa werken"],
         antwoord=[0, 1],
         uitleg="J'ai appris à répondre au téléphone et à classer des documents. Apprendre à betekent leren om."),
    dict(type="waarofniet",
         vraag="Volgens dat verslagje zou de leerling de stage opnieuw doen.",
         antwoord=True,
         uitleg="Je recommencerais quand même: ik zou toch opnieuw beginnen. Quand même betekent toch, ondanks dat."),
    dict(type="meerkeuze",
         vraag=f"Lees dit zoekertje: « {ANNONCE} » Welke taken horen bij de job?",
         opties=["de klanten verwelkomen",
                 "de rekken opruimen",
                 "aan de kassa helpen",
                 "de etalage inrichten"],
         antwoord=[0, 1, 2],
         uitleg="Accueillir les clients, ranger les rayons, aider à la caisse. Over de etalage staat er niets."),
    dict(type="meerkeuze",
         vraag="Hetzelfde zoekertje. Wat betekent expérience non exigée?",
         opties=["ervaring is niet vereist",
                 "ervaring is noodzakelijk",
                 "ervaring wordt beter betaald",
                 "je krijgt ervaring in de job"],
         antwoord=0,
         uitleg="Exiger is eisen. Non exigée betekent dus: niet geëist, niet vereist."),
    dict(type="invultekst",
         vraag="Nog dat zoekertje. Op welke dag van de week zoekt de winkel iemand? Schrijf de dag in het Nederlands.",
         antwoord=["zaterdag"],
         uitleg="Cherche étudiant pour les samedis. Samedi is zaterdag."),
    dict(type="waarofniet",
         vraag="Envoyer betekent in dat zoekertje 'invullen'.",
         antwoord=False,
         uitleg="Envoyer is sturen, zenden: envoyez votre CV par mail, stuur je cv met een mail. Invullen is remplir."),
    dict(type="meerkeuze",
         vraag="Je solliciteert in het Frans voor een studentenjob. Welke dingen zet je zeker in je mail?",
         opties=["wie je bent en in welk jaar je zit",
                 "wanneer je kan werken",
                 "waarom je net die job wil",
                 "welk cijfer je had voor Frans"],
         antwoord=[0, 1, 2],
         uitleg="Taakvoltooiing betekent dat je boodschap volledig is. Je punten op school hoort de werkgever niet te vragen en jij niet te vertellen."),
    # --- La communication et les multimédias -------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees deze uitleg: « {NUMERIQUE} » Wat doe je als het bericht niet aankomt?",
         opties=["in de map met ongewenste berichten kijken",
                 "opnieuw een account aanmaken",
                 "je wachtwoord opsturen",
                 "een ander mailadres gebruiken"],
         antwoord=0,
         uitleg="Les courriers indésirables zijn de ongewenste berichten, de spam. Indésirable betekent ongewenst."),
    dict(type="waarofniet",
         vraag="Volgens die uitleg mag je je wachtwoord nooit met een mail opsturen.",
         antwoord=True,
         uitleg="N'envoyez jamais votre mot de passe par mail. Un mot de passe is een wachtwoord, letterlijk een doorgangswoord."),
    dict(type="invultekst",
         vraag="Welke twee Franse woorden betekenen samen 'wachtwoord'? Vul in: « mot de ... ». Schrijf één woord.",
         antwoord=["passe"],
         uitleg="Un mot de passe. Un mot is een woord."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden horen bij communicatie en multimedia?",
         opties=["un ordinateur",
                 "un écran",
                 "une application",
                 "un rayon"],
         antwoord=[0, 1, 2],
         uitleg="Computer, scherm, app. Un rayon is een rek in een winkel."),
    dict(type="meerkeuze",
         vraag="Wat betekent de Franse uitdrukking « se connecter »?",
         opties=["inloggen", "uitloggen", "doorverbinden", "opladen"],
         antwoord=0,
         uitleg="Se connecter is inloggen, se déconnecter uitloggen. Allebei wederkerend."),
    dict(type="waarofniet",
         vraag="Un courriel is in het Frans een telefoongesprek.",
         antwoord=False,
         uitleg="Un courriel is een mail, naast het kortere un mail. Een telefoongesprek is un appel."),
    # --- Le sport et les loisirs -------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {SPORT} » Hoe vaak speelt de schrijver basket?",
         opties=["twee keer per week", "een keer per week", "elke dag", "alleen op zaterdag"],
         antwoord=0,
         uitleg="Deux fois par semaine. Une fois is een keer, par semaine per week."),
    dict(type="meerkeuze",
         vraag="Hetzelfde tekstje. Wat doet de zus?",
         opties=["dansen en piano spelen",
                 "basket en piano spelen",
                 "dansen en series kijken",
                 "lezen en dansen"],
         antwoord=0,
         uitleg="Elle fait de la danse et joue du piano. Let op het verschil: jouer au basket voor een sport, jouer du piano voor een instrument."),
    dict(type="meerkeuze",
         vraag="Welke Franse uitdrukkingen zijn juist?",
         opties=["jouer au football",
                 "jouer de la guitare",
                 "faire du vélo",
                 "jouer du tennis"],
         antwoord=[0, 1, 2],
         uitleg="Bij een sport of een spel hoort jouer à, bij een instrument jouer de, en voor veel sporten gebruik je faire de. Jouer du tennis bestaat niet."),
    dict(type="invultekst",
         vraag="Hoe zeg je in het Frans 'ik zwem graag'? Vul in: « J'aime ... ». Schrijf één woord.",
         antwoord=["nager"],
         uitleg="Nager is zwemmen. Na aimer komt de infinitief: j'aime nager, j'aime lire."),
    dict(type="waarofniet",
         vraag="Un match en une équipe horen allebei bij sport.",
         antwoord=True,
         uitleg="Een wedstrijd en een ploeg. Un joueur is een speler, un entraîneur een trainer."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden horen bij ontspanning?",
         opties=["un film",
                 "une série",
                 "un livre",
                 "un contrat"],
         antwoord=[0, 1, 2],
         uitleg="Film, reeks, boek. Un contrat hoort bij werken."),
]
