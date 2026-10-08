# -*- coding: utf-8 -*-
"""De leerbundels en oefenbundels voor Frans op 🌍 Beyond-niveau.

Gebaseerd op de vakfiches Frans 1 en Frans 2 van de derde graad
doorstroomfinaliteit, geldig vanaf 1 januari 2027. Allebei gelden ze voor
humane wetenschappen, Latijn-wiskunde met extra wetenschappen,
wiskunde-wetenschappen en economie-wiskunde. Het ERK-niveau is B1+, een stap
hoger dan de B1 van 🚀 Boost.

Frans 1 is een digitaal examen van 120 minuten, half lezen en half luisteren.
Frans 2 bestaat uit een spreekopdracht die je thuis opneemt, twee
schrijfopdrachten op het digitale examen en een gesprek van tien minuten;
schrijven en schriftelijke interactie wegen daar elk 29 %, literatuurbeleving
4 %.

Deze bundels dragen wat een platform met tekstvragen kán dragen: lezen,
schrijven, schriftelijke interactie, literatuurbeleving, en de woordenschat en
de grammatica die daarachter liggen. Luisteren, spreken en het gesprek staan er
niet in, en daarom staat in elke bundel achteraan hetzelfde kader dat de
leerling daar zelf naartoe stuurt.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen, dus Kim laadt dezelfde bundel twee keer op.

De bundelsleutels eindigen op "-beyond", de naam van de categorie. Dat
achtervoegsel is nodig omdat de themanamen van Beyond botsen met die van
🚀 Boost.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Frans"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
NA = "-beyond"
tabel = bundel.tabel

BUNDELS = {}


def spreken(opdracht):
    """Het vaste slotkader over wat je niet achter een scherm leert."""
    return dict(kop="Oefen dit ook buiten het scherm", blokken=[
        ("p", "Op dit platform oefen je lezen, woordenschat en grammatica. Maar <strong>luisteren</strong> "
              "is de helft van het examen Frans 1, en Frans 2 bestaat uit <strong>een spreekopdracht die "
              "je thuis opneemt</strong>, twee schrijfopdrachten en <strong>een gesprek van tien "
              "minuten</strong>. Luisteren en spreken leer je niet achter een scherm. Je leert ze door te "
              "luisteren naar mensen die echt Frans spreken, en door zelf je mond open te doen, ook als "
              "het hakkelt."),
        ("kader", "<strong>Deze week:</strong> " + opdracht + " Doe het één keer, en let daarna op wat je "
                  "miste of niet gezegd kreeg. Dat is precies je volgende oefening."),
    ])


def zet(sleutel, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BEYOND)
    BUNDELS[sleutel + NA] = b


# ───────────────────────── 1. Een Franse tekst analyseren
zet("een-franse-tekst-analyseren",
    titel="Een Franse tekst analyseren",
    onder="Onderwerp, hoofdgedachte en hoofdpunten, gericht zoeken, de signaalwoorden en de verwijswoorden, en een onbekend woord uit de context halen.",
    secties=[
        dict(kop="Onderwerp, hoofdgedachte en hoofdpunten", blokken=[
            ("p", "Drie woorden die op elkaar lijken en die je uit elkaar moet houden. "
                  "<strong>De hoofdgedachte van een tekst is niet hetzelfde als het onderwerp.</strong>"),
            ("p", tabel(["", "hoe lang", "voorbeeld"],
                        [["het onderwerp", "enkele woorden", "uitleenfietsen in Lyon"],
                         ["de hoofdgedachte", "een hele zin", "Te weinig slaap is slecht voor het hart."],
                         ["de hoofdpunten", "de zinnen eronder", "wat de hoofdgedachte ondersteunt"]])),
            ("p", "Lees: <em>Depuis janvier, la ville de Lyon prête des vélos électriques aux habitants "
                  "qui n'ont pas de voiture. Mille personnes ont déjà fait la demande.</em> Het onderwerp "
                  "in enkele woorden: <strong>uitleenfietsen in Lyon</strong>."),
            ("p", "Lees: <em>Dormir moins de six heures par nuit augmente le risque de maladies du cœur. "
                  "Les chercheurs conseillent donc de se coucher plus tôt.</em> De hoofdgedachte is een "
                  "hele zin: <strong>te weinig slaap is slecht voor het hart</strong>."),
            ("p", "Lees: <em>Ce roman raconte l'histoire d'une famille belge pendant la guerre. L'auteur "
                  "s'est inspiré du journal de sa grand-mère.</em> De hoofdpunten: <strong>het boek gaat "
                  "over een Belgisch gezin</strong>, <strong>het verhaal speelt tijdens de oorlog</strong> "
                  "en <strong>de schrijver gebruikte een dagboek</strong>."),
            ("kader", "<strong>Bij een leesvraag mag je het antwoord niet halen uit wat je zelf al over "
                      "het onderwerp weet, zeker niet als het de tekst tegenspreekt.</strong> En "
                      "<strong>de titel, de tussentitels en de foto bij een tekst mag je niet "
                      "overslaan</strong>: ze horen er wel degelijk bij."),
            ("p", "Vooraf stel je met het communicatiemodel drie vragen: <strong>van wie is de "
                  "tekst?</strong>, <strong>waarom is hij gemaakt?</strong> en <strong>voor wie is hij "
                  "bedoeld?</strong>"),
        ]),
        dict(kop="Gericht zoeken", blokken=[
            ("p", tabel(["de zin", "de vraag", "het antwoord"],
                        [["Le musée est fermé le mardi.", "welke dag gesloten?", "mardi"],
                         ["Le colis arrivera entre 14 h et 16 h.", "ten vroegste?", "14 h"],
                         ["L'entrée est gratuite pour les moins de 12 ans.", "tot welke leeftijd?", "12"],
                         ["Il ne reste plus que deux places.", "hoeveel plaatsen vrij?", "nog maar twee"]])),
            ("p", "Lees: <em>Le train de 7 h 12 a été supprimé. Les voyageurs doivent prendre le bus de "
                  "remplacement devant la gare.</em> Drie dingen staan er: <strong>de trein rijdt "
                  "niet</strong>, <strong>er staat een vervangbus klaar</strong> en <strong>de bus "
                  "vertrekt voor het station</strong>."),
            ("p", "Lees: <em>Les élèves de terminale passent le bac en juin.</em> Dat gaat over "
                  "<strong>leerlingen van het laatste jaar</strong>: <em>la terminale</em> is in Frankrijk "
                  "het laatste jaar van het middelbaar."),
            ("p", "Lees: <em>Ce guide s'adresse aux parents d'enfants à haut potentiel.</em> De gids is "
                  "bedoeld <strong>voor ouders van hoogbegaafde kinderen</strong>. En <em>Attention : ce "
                  "produit contient des arachides</em> is vooral belangrijk <strong>voor wie allergisch is "
                  "aan noten</strong>."),
        ]),
        dict(kop="Tussen de regels lezen", blokken=[
            ("p", tabel(["de zin", "wat ze zegt"],
                        [["Il n'a pas été nécessaire d'annuler le concert.", "het concert ging door"],
                         ["La bibliothèque sera exceptionnellement ouverte dimanche.", "bij uitzondering"],
                         ["Faute de bénévoles, la fête n'aura pas lieu.",
                          "er zijn te weinig vrijwilligers"],
                         ["Le film, pourtant primé à Cannes, n'a attiré que peu de spectateurs.",
                          "een prijs, maar weinig volk"],
                         ["Les travaux dureront jusqu'à la fin du mois, sauf en cas de pluie.",
                          "bij regen kan het langer duren"]])),
            ("p", "Let op <em>faute de</em> (bij gebrek aan) en <em>sauf en cas de</em> (behalve bij). "
                  "Twee kleine uitdrukkingen die het hele antwoord dragen."),
            ("p", "Lees: <em>Selon l'auteur, les réseaux sociaux ne sont pas responsables de tout.</em> "
                  "Het standpunt: <strong>sociale media krijgen te veel de schuld</strong>."),
            ("p", "Lees: <em>Je vous écris afin de vous signaler une erreur dans ma facture et de demander "
                  "un remboursement.</em> Drie dingen kloppen: <strong>de schrijver meldt een "
                  "fout</strong>, <strong>de schrijver vraagt geld terug</strong> en <strong>de mail gaat "
                  "over een factuur</strong>."),
        ]),
        dict(kop="Signaalwoorden", blokken=[
            ("p", tabel(["signaalwoord", "verband"],
                        [["pourtant, en revanche, alors que", "een tegenstelling"],
                         ["donc, par conséquent, c'est pourquoi, du coup", "een gevolg"],
                         ["car, parce que", "een reden"],
                         ["bien que", "een toegeving"],
                         ["d'abord, ensuite, enfin", "een volgorde in de tijd"],
                         ["par exemple, notamment, ainsi", "een voorbeeld"],
                         ["en effet", "een onderbouwing van wat er net stond"]])),
            ("p", "Een gevolg kondigen <strong>donc</strong>, <strong>par conséquent</strong> en "
                  "<strong>c'est pourquoi</strong> aan. Het woord van twee letters dat dus betekent, is "
                  "<strong>donc</strong>."),
            ("p", "<strong>Het woord <em>car</em> kondigt geen gevolg aan maar een reden</strong>: het is "
                  "hetzelfde als <em>parce que</em>. Verwar het niet met <em>donc</em>, dat precies de "
                  "andere kant op wijst."),
            ("p", "<em>Pourtant</em> legt <strong>een tegenstelling</strong>, en <em>alors que</em> in "
                  "<em>Alors que le Nord connaît la sécheresse, le Sud est inondé</em> ook. <em>En "
                  "revanche</em> zegt <strong>daar staat iets tegenover</strong>, en <em>bien que</em> in "
                  "<em>Bien qu'il soit fatigué, il continue à travailler</em> legt <strong>een "
                  "toegeving</strong>. Let op: na <em>bien que</em> staat altijd de subjonctif."),
            ("p", "<em>D'abord, on prépare la pâte. Ensuite, on ajoute les œufs. Enfin, on met le plat au "
                  "four.</em> Die woorden leggen <strong>een volgorde in de tijd</strong>. <strong>De "
                  "woorden <em>par exemple</em>, <em>notamment</em> en <em>ainsi</em> kondigen een "
                  "voorbeeld aan.</strong>"),
            ("p", "Lees: <em>Les jeunes lisent moins qu'avant. En effet, une enquête montre que…</em> De "
                  "tweede zin <strong>onderbouwt de eerste</strong>. En <em>Il a raté son train. Du coup, "
                  "il est arrivé en retard</em>: <em>du coup</em> betekent hier <strong>daardoor</strong>."),
            ("p", "<strong>Een alinea in een argumentatieve tekst kan de functie hebben om een "
                  "tegenargument te weerleggen.</strong> Zo'n alinea begint vaak met <em>certes</em> of "
                  "<em>on pourrait objecter que</em>, en draait daarna met <em>mais</em>."),
        ]),
        dict(kop="Verwijswoorden", blokken=[
            ("p", tabel(["de zinnen", "het woordje", "waarnaar"],
                        [["Marie a appelé son frère. Il n'a pas répondu.", "il", "naar de broer van Marie"],
                         ["Je n'aime pas les épinards. Mon frère, lui, en mange tous les jours.", "en",
                          "naar de spinazie"],
                         ["Ce que je retiens surtout, c'est son courage.", "ce que",
                          "naar de moed verder in de zin"]])),
            ("p", "Het woordje <strong>en</strong> vervangt iets met <em>de</em> erbij: <em>il en mange</em> "
                  "is <em>il mange des épinards</em>. Het is klein en makkelijk over het hoofd te zien, en "
                  "juist daarom vaak de sleutel van een leesvraag."),
        ]),
        dict(kop="Een onbekend woord", blokken=[
            ("p", "De fiche geeft drie manieren om een onbekend woord aan te pakken: <strong>de betekenis "
                  "uit de context afleiden</strong>, <strong>letten op hoe het woord gevormd is</strong>, "
                  "en <strong>je voorkennis en andere talen gebruiken</strong>."),
            ("p", "Lees: <em>Ce livre est illisible.</em> Je leidt het af <strong>uit <em>lire</em> plus de "
                  "ontkenning <em>il-</em></strong>: niet te lezen. En <em>Le réchauffement climatique "
                  "s'accélère</em>: <em>réchauffement</em> betekent <strong>opwarming</strong>, van "
                  "<em>chaud</em>."),
            ("p", tabel(["deel", "wat het doet", "voorbeeld"],
                        [["in-, im-, il-, ir-", "maakt het tegendeel", "incorrect, impossible, illisible"],
                         ["re-, ré-", "opnieuw", "refaire, réchauffer"],
                         ["-able, -ible", "het kan gedaan worden", "faisable, lisible"],
                         ["-ment", "maakt er een bijwoord van", "lentement"],
                         ["-eur, -euse", "de persoon die het doet", "chanteur, chanteuse"]])),
        ]),
        spreken("luister vijftien minuten naar een Franstalige podcast of radiozender over iets wat je "
                "toch al interesseert, en vertel daarna in het Frans waar het over ging."),
    ])


# ───────────────────────── 2. Tekstsoorten en de bedoeling van een tekst
zet("tekstsoorten-en-de-bedoeling-van-een-tekst",
    titel="Tekstsoorten en de bedoeling van een tekst",
    onder="De zeven tekstsoorten van de fiche, feit tegenover mening, formeel tegenover informeel, en voor wie een tekst gemaakt is.",
    secties=[
        dict(kop="De zeven tekstsoorten", blokken=[
            ("p", tabel(["soort", "wat hij doet", "voorbeeld"],
                        [["informatief", "informatie geven", "een krantenartikel, een interview"],
                         ["prescriptief", "zeggen wat je moet doen", "een recept, een handleiding"],
                         ["persuasief", "je gedrag veranderen", "een reclamespot, een campagne"],
                         ["argumentatief", "een stelling met argumenten staven", "een opiniestuk"],
                         ["narratief", "feiten verhalend weergeven", "een reisverslag, een getuigenis"],
                         ["opiniërend", "zeggen wat de schrijver vindt", "een recensie"],
                         ["literair", "iets maken met taal", "een roman, een gedicht, een strip"]])),
            ("p", "De tekst die vooral informatie wil geven, is <strong>een informatieve tekst</strong>. "
                  "Een tekst die je van iets wil overtuigen of je gedrag wil veranderen, is "
                  "<strong>persuasief</strong>. Een tekst die feiten en gebeurtenissen verhalend weergeeft, "
                  "is <strong>narratief</strong>."),
            ("p", "<strong>Een argumentatieve tekst voert argumenten aan om een stelling te "
                  "ondersteunen.</strong> <strong>Eén tekst kan tot meer dan één van de zeven soorten "
                  "horen</strong>: een reisverslag is narratief en informatief tegelijk."),
            ("p", tabel(["de tekst", "de soort"],
                        [["Mélangez la farine et le beurre, puis laissez reposer la pâte.", "prescriptief"],
                         ["Ce restaurant est une véritable déception : service lent et plats froids.",
                          "opiniërend"],
                         ["Et soudain, le silence. La pluie avait cessé de tomber…", "literair"],
                         ["Avis aux habitants : la collecte des déchets est reportée à jeudi.",
                          "een informatieve mededeling"],
                         ["Interdire les voitures en ville ? Trois raisons de ne pas le faire.",
                          "argumentatief"]])),
            ("p", "Volgens de fiche zijn <strong>een reisverslag</strong>, <strong>een getuigenis</strong> "
                  "en <strong>een videoblog</strong> narratief, en zijn <strong>een krantenartikel</strong>, "
                  "<strong>een interview</strong> en <strong>een nieuwsitem</strong> informatief. "
                  "<strong>Een strip en een cartoon horen bij de literaire teksten.</strong>"),
            ("p", "<strong>Een reclamespot is geen informatieve tekst</strong>, al geeft hij informatie "
                  "over een product: zijn bedoeling is je iets te doen kopen, dus hij is persuasief."),
            ("p", "Een prescriptieve tekst herken je snel <strong>aan de imperatief</strong>, <strong>aan "
                  "de stappen in volgorde</strong> en <strong>soms aan een infinitief</strong> "
                  "(<em>mélanger, laisser reposer</em>, zoals in veel Franse recepten)."),
        ]),
        dict(kop="De bedoeling", blokken=[
            ("p", tabel(["de tekst", "de bedoeling"],
                        [["Roulez moins vite. Chaque année, la vitesse tue 300 personnes.",
                          "je gedrag veranderen"],
                         ["Ce documentaire montre comment vivent les derniers bergers des Pyrénées.",
                          "je iets laten zien en bijbrengen"],
                         ["À mon avis, l'école devrait commencer plus tard. Les adolescents dorment trop peu.",
                          "een mening met een reden geven"],
                         ["Comment réussir son entretien d'embauche en cinq étapes.", "een stappenplan"],
                         ["Vous êtes nombreux à nous avoir écrit. Voici nos réponses.",
                          "antwoorden op lezersvragen"]])),
            ("p", "Een <strong>avis</strong> is een aankondiging of mededeling, zoals in <em>avis aux "
                  "habitants</em>. En <em>Chers voyageurs, veuillez composter votre billet avant de "
                  "monter</em> betekent: <strong>je ticket afstempelen</strong> voor je opstapt."),
            ("p", "De elementen die je helpen de soort te bepalen: <strong>de titel en de "
                  "tussentitels</strong>, <strong>de plaats waar hij verscheen</strong> en <strong>de "
                  "werkwoordstijden erin</strong>. <strong>De passé simple kom je in het Frans vooral "
                  "tegen in verhalende en literaire teksten</strong>, bijna nooit in spreektaal."),
        ]),
        dict(kop="Feit of mening", blokken=[
            ("p", "<strong>Het verschil tussen een feit en een mening: een feit kan je nagaan.</strong>"),
            ("p", "Lees: <em>Le musée a accueilli 120 000 visiteurs. C'est un succès incroyable.</em> "
                  "<strong>De eerste zin is een feit</strong>, <strong>de tweede zin is een mening</strong>, "
                  "en <strong>het cijfer kan je nagaan</strong>. Twee zinnen naast elkaar, twee heel "
                  "verschillende soorten uitspraak."),
            ("p", tabel(["uitdrukking", "wat ze aankondigt"],
                        [["à mon avis, selon moi", "een persoonlijke mening"],
                         ["il est prouvé que", "een feit"],
                         ["le gouvernement aurait décidé", "nog niet bevestigd: de conditionnel"]])),
            ("p", "De uitdrukking van drie woorden die naar mijn mening betekent, is <strong>à mon "
                  "avis</strong>. De uitdrukking die een feit aankondigt, is <strong>il est prouvé "
                  "que</strong>."),
            ("p", "Lees: <em>Le gouvernement aurait décidé de reporter la réforme.</em> Die conditionnel "
                  "zegt <strong>het is nog niet bevestigd</strong>. Dat is in de Franse pers een vaste "
                  "manier om iets te melden waar nog geen bevestiging van is: <em>le conditionnel "
                  "journalistique</em>."),
            ("p", "<strong>In een krantenartikel kan naast feiten ook de mening van de journalist "
                  "staan.</strong> En <strong>een tekst met veel cijfers en bronvermeldingen is daarom "
                  "niet automatisch objectief</strong>: ook een selectie van ware cijfers kan sturen."),
            ("p", "Lees: <em>Ni l'un ni l'autre candidat ne convainc vraiment.</em> De schrijver vindt "
                  "<strong>dat geen van beide kandidaten overtuigt</strong>."),
        ]),
        dict(kop="Formeel of informeel", blokken=[
            ("p", "<strong>Tegen een onbekende volwassene gebruik je <em>vous</em>.</strong> Dat is in het "
                  "Frans geen beleefdheidsdetail maar de regel."),
            ("p", "Je merkt dat een tekst formeel is <strong>aan de vous-vorm</strong>, <strong>aan de "
                  "volledige zinnen</strong> en <strong>aan vaste beleefdheidsformules</strong>. <em>Monsieur "
                  "le Directeur, je me permets de vous écrire au sujet de…</em> zegt meteen: <strong>het "
                  "is een formele brief</strong>."),
            ("p", "Lees: <em>Salut ! T'as vu le match hier soir ? C'était dingue !</em> Daaraan valt op "
                  "dat <strong>het spreektaal is</strong>: <em>salut</em>, de weggelaten <em>ne</em>, "
                  "<em>t'as</em> in plaats van <em>tu as</em>, en <em>dingue</em>. <strong>Het woord "
                  "<em>dingue</em> past niet in een formele brief.</strong>"),
            ("p", "Het is nuttig te weten voor wie een tekst bedoeld is, <strong>omdat dat de toon en de "
                  "woordkeuze verklaart</strong>. De lezer of hoorder voor wie een tekst bedoeld is, heet "
                  "in het Frans de <strong>destinataire</strong>."),
            ("p", "Lees: <em>Ce téléphone ? Le meilleur de tous les temps, à un prix imbattable !</em> Wat "
                  "de bedoeling verraadt, zijn <strong>de overdreven superlatieven</strong>."),
        ]),
        spreken("lees één Franstalig opiniestuk en zeg daarna hardop in het Frans, in drie zinnen, wat de "
                "schrijver vindt en of je het ermee eens bent."),
    ])


# ───────────────────────── 3. De Franstalige wereld: omgangsvormen en gewoontes
zet("de-franstalige-wereld-omgangsvormen-en-gewoontes",
    titel="De Franstalige wereld: omgangsvormen en gewoontes",
    onder="Tutoyeren of vousvoyeren, hoffelijk vragen, de Franstalige wereld, en de gewoontes die je tekst of gesprek doen kloppen.",
    secties=[
        dict(kop="Tu of vous", blokken=[
            ("p", "<strong>Tegen een onbekende volwassene gebruik je <em>vous</em>.</strong> In een Franse "
                  "winkel spreek je een verkoopster die je niet kent dus aan met <em>vous</em>, en "
                  "<strong>in een mail aan een leraar met wie je geen nauwe band hebt gebruik je ook de "
                  "vous-vorm</strong>. Iemand met <em>vous</em> aanspreken heet <strong>vouvoyer</strong>."),
            ("p", "<strong>Zeg altijd eerst <em>bonjour</em></strong> als je een onbekende om een "
                  "inlichting vraagt. In Frankrijk is dat geen beleefd extraatje maar het minimum: wie "
                  "zonder bonjour begint, komt onbeschoft over, hoe correct zijn Frans verder ook is."),
            ("p", "Zegt een Fransman <em>on se tutoie ?</em>, dan <strong>stelt hij voor om <em>tu</em> te "
                  "gebruiken</strong>. Dat voorstel komt van de oudste of de hoogste in rang; jij wacht "
                  "het af."),
            ("p", "Onder vrienden hoort bij een Franse begroeting <strong>la bise, een kus op de "
                  "wang</strong>, <strong><em>salut</em> of <em>coucou</em> zeggen</strong> en <strong>van "
                  "bij de eerste keer tutoyeren</strong>. <strong>Mensen die elkaar goed kennen geven "
                  "elkaar bij het begroeten vaak een kus op de wang.</strong>"),
        ]),
        dict(kop="Hoffelijk vragen", blokken=[
            ("p", "De <strong>conditionnel de politesse</strong> is <strong>een hoffelijke vorm met "
                  "<em>voudrais</em> of <em>pourriez</em></strong>. Hij maakt van een eis een vraag."),
            ("p", tabel(["te direct", "hoffelijk"],
                        [["Je veux un café.", "Je voudrais un café, s'il vous plaît."],
                         ["Aidez-moi.", "Pourriez-vous m'aider ?"],
                         ["Vous avez un instant ?", "Est-ce que vous auriez un instant ?"],
                         ["Dites-moi si…", "Je voudrais savoir si…"]])),
            ("p", "<strong><em>Je veux un café</em> is in een Frans café niet de meest hoffelijke manier "
                  "om iets te vragen.</strong> <em>Je veux</em> klinkt als een bevel; <em>je voudrais</em> "
                  "is de gewone vorm."),
            ("p", "Bel je een Frans bedrijf, dan zeg je: <strong>Bonjour, pourrais-je parler à madame "
                  "Leroy ?</strong> Begrijp je iemand niet, dan zeg je <strong>Pardon, pourriez-vous "
                  "répéter ?</strong> Op <em>merci</em> antwoord je met <strong>de rien</strong> of "
                  "<em>pas de quoi</em>."),
            ("p", "Een gewone zakelijke mail sluit je af met <strong>cordialement</strong>; een formele "
                  "brief met <strong>Veuillez agréer mes salutations distinguées.</strong> De aanhef aan "
                  "een directeur die je niet kent, is <strong>Monsieur le Directeur,</strong>"),
        ]),
        dict(kop="In gesprek blijven", blokken=[
            ("p", "Bij hoffelijke lichaamstaal in een Frans gesprek hoort <strong>de ander aankijken "
                  "terwijl hij spreekt</strong>, <strong>een hand geven bij een eerste ontmoeting</strong> "
                  "en <strong>knikken om te laten zien dat je volgt</strong>."),
            ("p", "Naar iemands mening vraag je met <strong>Qu'en pensez-vous ?</strong>, en je toont "
                  "interesse met <strong>Et vous, qu'est-ce que vous en pensez ?</strong> Een gesprek is "
                  "geen beurtrol van twee monologen: de vraag terug is wat het gaande houdt."),
            ("kader", "<strong>Zit je vast in het Frans, dan is stoppen met spreken juist het slechtste "
                      "wat je kan doen.</strong> Zeg <em>comment dire…</em>, <em>c'est-à-dire…</em> of "
                      "<em>je cherche le mot</em>, omschrijf het woord dat je niet vindt, of vraag "
                      "<em>comment on dit… ?</em> Doorpraten met een omweg levert op een examen punten op; "
                      "zwijgen niet."),
        ]),
        dict(kop="Waar wordt Frans gesproken", blokken=[
            ("p", "In België is het Frans de taal van <strong>Wallonië en Brussel</strong>. Daarnaast is "
                  "het een officiële taal in onder meer <strong>Canada</strong>, <strong>Zwitserland</strong> "
                  "en <strong>Senegal</strong>. <strong>Het Frans wordt op meerdere continenten als "
                  "officiële taal gebruikt.</strong>"),
            ("p", "Het Franstalige gewest van Canada is <strong>Québec</strong>. <strong>La "
                  "Francophonie</strong> is <strong>de samenwerking van Franstalige landen</strong>."),
            ("p", "<strong>Het verschil tussen <em>la Wallonie</em> en <em>la Flandre</em> is in een "
                  "Franse tekst een geografisch én een talig verschil.</strong>"),
            ("p", tabel(["België", "Frankrijk"],
                        [["septante, nonante", "soixante-dix, quatre-vingt-dix"],
                         ["déjeuner = het ontbijt", "petit déjeuner = het ontbijt"],
                         ["dîner = het middagmaal", "déjeuner = het middagmaal"],
                         ["souper = het avondmaal", "dîner = het avondmaal"],
                         ["bourgmestre", "maire"]])),
            ("p", "Belgische Franstaligen zeggen <strong>septante</strong> voor zeventig, en de drie "
                  "verschillen die de fiche noemt zijn: <strong>België zegt septante en nonante</strong>, "
                  "<strong>België zegt déjeuner voor het ontbijt</strong> en <strong>België gebruikt "
                  "bourgmestre voor burgemeester</strong>. Let dus op bij de maaltijden: hetzelfde woord "
                  "betekent aan weerszijden van de grens een ander uur van de dag."),
        ]),
        dict(kop="School en werk in Frankrijk", blokken=[
            ("p", "<strong>Le bac</strong> is <strong>het eindexamen van het secundair</strong>; het "
                  "laatste jaar heet <strong>la terminale</strong>. <strong>La rentrée</strong> is "
                  "<strong>het begin van het schooljaar</strong>, en dat woord gebruikt men in Frankrijk "
                  "voor veel meer dan school: het hele land begint in september opnieuw."),
            ("p", "Het Franse schooljaar verschilt van het onze doordat <strong>de jaren omgekeerd geteld "
                  "worden</strong>: na la sixième komt la cinquième, en zo verder tot la première en "
                  "daarna la terminale."),
            ("p", "<strong>Le smic</strong> is <strong>het wettelijk minimumloon</strong>, en <strong>een "
                  "Franse werknemer heeft wel degelijk recht op betaalde vakantie</strong>: vijf weken, "
                  "wettelijk vastgelegd."),
        ]),
        dict(kop="Aan tafel", blokken=[
            ("p", "Bij een Franse maaltijd horen <strong>l'entrée</strong>, <strong>le plat "
                  "principal</strong> en <strong>le dessert</strong>. Een <strong>entrée</strong> is "
                  "<strong>het voorgerecht</strong>, niet het hoofdgerecht; in het Amerikaans Engels "
                  "betekent <em>entrée</em> juist wél het hoofdgerecht, en daar gaat het vaak mis."),
            ("p", "Het ontbijt heet in Frankrijk <strong>le petit déjeuner</strong>."),
            ("p", "<strong>De middagpauze is in Frankrijk traditioneel niet kort.</strong> Een echte "
                  "maaltijd aan tafel, vaak een uur of meer, hoort er nog altijd bij, ook al eet men in de "
                  "grote steden vaker snel."),
            ("p", "De nationale feestdag van Frankrijk is <strong>14 juli</strong>."),
            ("p", "De fiche vraagt dat je culturele verschillen kan benoemen <strong>om beter te begrijpen "
                  "wat je leest</strong>. Wie niet weet wat <em>la rentrée</em> of <em>le bac</em> is, "
                  "leest een krantenartikel maar half."),
        ]),
        spreken("spreek een Franstalige aan met een vraag om inlichting, met bonjour vooraan en de "
                "conditionnel de politesse erin, en let op het verschil tussen tu en vous."),
    ])


# ───────────────────────── 4. Literaire teksten en literatuurbeleving
zet("literaire-teksten-en-literatuurbeleving",
    titel="Literaire teksten en literatuurbeleving",
    onder="De bouw van een verhaal, de woorden om erover te spreken, en hoe je zegt wat een tekst met je deed.",
    secties=[
        dict(kop="Wat is een literaire tekst", blokken=[
            ("p", "De fiche noemt literair: <strong>een gedicht en een lied</strong>, <strong>een strip en "
                  "een cartoon</strong>, en <strong>een kortverhaal of romanfragment</strong>."),
            ("p", tabel(["Frans", "Nederlands"],
                        [["un roman", "een roman"],
                         ["un poème", "een gedicht"],
                         ["une nouvelle", "een kortverhaal"],
                         ["une bande dessinée", "een strip"],
                         ["un chapitre", "een hoofdstuk"],
                         ["la couverture", "de kaft"],
                         ["un résumé", "een korte samenvatting"]])),
            ("p", "<strong><em>Une nouvelle</em> kan in het Frans zowel een kortverhaal als een nieuwtje "
                  "betekenen.</strong> De context beslist, en in een literatuurvraag is het bijna altijd "
                  "het kortverhaal."),
            ("p", "<strong>Een cartoon kan je wel degelijk als een literaire tekst lezen</strong>, ook al "
                  "staan er weinig woorden in: het beeld, de verhouding tussen tekst en tekening en de "
                  "ironie dragen er de betekenis."),
        ]),
        dict(kop="De bouw van een verhaal", blokken=[
            ("p", "Om over de bouw van een verhaal te spreken gebruik je <strong>le personnage</strong>, "
                  "<strong>l'intrigue</strong> en <strong>le dénouement</strong>."),
            ("p", tabel(["Frans", "Nederlands"],
                        [["un personnage", "een personage"],
                         ["l'auteur, l'écrivain", "de schrijver"],
                         ["l'intrigue", "de verhaallijn"],
                         ["le dénouement", "de ontknoping"],
                         ["une strophe", "een strofe, een groepje regels"],
                         ["un vers", "een versregel"]])),
            ("p", "<strong>In een Franse roman staat het verhaal vaak in de passé simple en de "
                  "imparfait.</strong> Lees: <em>Il entra dans la pièce. Le feu brûlait encore.</em> De "
                  "tweede zin staat in <strong>de imparfait</strong>: die geeft de achtergrond, terwijl de "
                  "passé simple de handeling draagt."),
        ]),
        dict(kop="Beeldspraak", blokken=[
            ("p", "Een literaire tekst gebruikt vaker dan een krantenartikel <strong>beeldspraak</strong>, "
                  "<strong>vergelijkingen</strong> en <strong>klank en ritme</strong>."),
            ("p", "Lees: <em>Le temps passe et moi, je reste.</em> Die regel gebruikt het beeld van "
                  "<strong>de tijd als iets dat wandelt</strong>. En <em>Elle avait les yeux de la mer "
                  "après la tempête</em> doet maar één ding: <strong>een beeld oproepen</strong>. Je kan "
                  "zo'n zin niet nagaan en niet uitleggen in cijfers; je moet hem zien."),
            ("kader", "<strong>Bij een literaire tekst moet je niet elk woord kennen om de tekst te kunnen "
                      "beleven.</strong> Dat is het verschil met een leesvraag over een treinbericht. Een "
                      "gedicht waarvan je drie woorden mist, kan je nog altijd raken, en dat mag je ook "
                      "zo zeggen."),
        ]),
        dict(kop="Literatuurbeleving", blokken=[
            ("p", "<strong>Literatuurbeleving</strong> is <strong>zeggen wat een tekst met je doet</strong>. "
                  "Het is geen samenvatting en geen analyse: het is jouw reactie, met de tekst erbij."),
            ("p", "<strong>Je onderbouwt je mening het best met een stukje uit de tekst.</strong> Zonder "
                  "zo'n stukje is het een smaakoordeel; mét is het literatuurbeleving."),
            ("p", tabel(["uitdrukking", "wat ze zegt"],
                        [["j'ai aimé ce passage", "ik vond dit stuk goed"],
                         ["ce personnage m'a surpris", "dit personage verraste me"],
                         ["la fin m'a déçu", "het einde stelde me teleur"],
                         ["ce qui m'a frappé, c'est…", "wat me opviel, is…"],
                         ["je n'ai pas pu le lâcher", "ik kon het niet wegleggen"]])),
            ("p", "Het werkwoord dat raken of ontroeren betekent, is <strong>toucher</strong>: <em>ce livre "
                  "m'a touché</em>. <em>Ce qui m'a frappé, c'est le silence du père</em>: daarmee "
                  "<strong>zegt de schrijver wat hem opviel</strong>."),
            ("p", "Woorden om een boek positief te beoordelen: <strong>émouvant</strong>, "
                  "<strong>captivant</strong> en <strong>bien écrit</strong>. <strong>Passionnant</strong> "
                  "betekent boeiend of meeslepend, van <em>passionner</em>. En <strong>décevant</strong> "
                  "betekent <strong>ontgoochelend</strong>."),
            ("p", "<strong>Je mag bij literatuurbeleving zeggen dat je een boek niet goed vond.</strong> "
                  "Een eerlijk en onderbouwd mishagen is evenveel waard als lof; wat telt is dat je zegt "
                  "waarom, met een passage erbij."),
            ("p", "<strong>Over een boek spreek je in het Frans niet altijd in een verleden tijd.</strong> "
                  "De inhoud beschrijf je gewoon in de présent: <em>Le roman raconte l'histoire d'une "
                  "famille…</em> Je eigen leeservaring staat wel in de passé composé: <em>j'ai aimé</em>."),
        ]),
        dict(kop="Je beoordeling voorbereiden", blokken=[
            ("p", "Het is nuttig om bij het lezen notities te maken, <strong>want dan vind je je passages "
                  "snel terug</strong>. Op het moment dat je je mening moet staven, heb je geen tijd meer "
                  "om een boek door te bladeren."),
            ("p", "Drie vragen helpen je om over een gelezen tekst te spreken: <strong>wat raakte mij, en "
                  "waarom?</strong>, <strong>wat begreep ik niet meteen?</strong> en <strong>aan wie zou "
                  "ik dit aanraden?</strong>"),
            ("p", "<strong>Een citaat uit een Franse tekst moet je bij een beoordeling niet naar het "
                  "Nederlands vertalen.</strong> Je spreekt of schrijft in het Frans, dus het citaat "
                  "blijft in het Frans staan."),
            ("p", "<em>Recommander un livre</em> betekent <strong>een boek aanraden</strong>, en een "
                  "passende slotzin onder je eigen beoordeling is <strong>Je le recommande "
                  "vivement.</strong>"),
            ("p", "<strong>Een strip of een lied kan even goed dienen om je literatuurbeleving te laten "
                  "zien als een roman.</strong> De fiche vraagt niet om dikke boeken, maar om wat een "
                  "tekst met je doet."),
        ]),
        spreken("vertel in het Frans over een boek, een lied of een strip die je echt raakte, met één "
                "passage erbij en de reden waarom hij bleef hangen."),
    ])
