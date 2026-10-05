# -*- coding: utf-8 -*-
"""De Engelse vragen die bij dubbele finaliteit anders moeten dan bij doorstroom.

De sleutel is de vráág van de doorstroomversie, woord voor woord.
`bouw_engels.py` zoekt ze op en zet er deze vraag voor in de plaats; staat een
sleutel niet (meer) in de doorstroombestanden, dan stopt het script.

Het verschil tussen de twee fiches is hier vooral een verschil in niveau. Bij
doorstroom is het ERK-niveau B1, bij dubbele finaliteit A2, en de
grammaticalijst van A2 is korter. Deze vijf dingen staan wél op de
doorstroomfiche en **niet** op die van dubbele finaliteit:

  * de modale hulpwerkwoorden (can, must, should …) — daarom valt het hele
    thema `en_modalen` hier weg
  * de past perfect simple
  * de toekomst met 'going to', de future continuous en 'shall'
  * de betrekkelijke voornaamwoorden en de betrekkelijke bijzinnen
  * de voorwaardelijke bijzinnen (conditionals zero en first) als apart begrip
  * de onpersoonlijke werkwoorden en de nadrukkelijke 'do'

Wat de A2-fiche er juist bij heeft, staat niet in losse vervangingen maar in
twee nieuwe thema's: `endf_klank` (klank, klemtoon, intonatie en spelling) en
`endf_spreken` (spreken en gesprekken, samen bijna een kwart van het examen).

Elke vervanging houdt hetzelfde type en, bij waar of niet waar, ook hetzelfde
antwoord, zodat de verhoudingen per hoofdstuk blijven kloppen. Bij meerdere
juiste antwoorden blijft het er ook meerdere.
"""

VERVANGINGEN = {
    # ─────────────────────────────────────────────────────────
    # Pronouns — deel 2. De betrekkelijke voornaamwoorden gaan eruit; wat
    # ervoor in de plaats komt, zijn de vragende voornaamwoorden en de
    # woorden die een hoeveelheid aanduiden. Allebei staan ze wél op de fiche.
    "Welk betrekkelijk voornaamwoord hoort bij een persoon?": dict(
        type="meerkeuze",
        vraag="Welke vraag naar het beroep van iemands vader is juist?",
        opties=["What does your father do?",
                "What do your father do?",
                "What does do your father?",
                "What your father does do?"],
        antwoord=0,
        uitleg="Na 'does' blijft het werkwoord in de basisvorm. De woordvolgorde is: vraagwoord, "
               "hulpwerkwoord, onderwerp, werkwoord.",
    ),
    "Welke betrekkelijke voornaamwoorden kan je bij een ding gebruiken?": dict(
        type="meerkeuze",
        vraag="Welke vragen zijn juist gevormd?",
        opties=["Who lives next door?",
                "What do you want?",
                "Which bus goes to town?",
                "Who does live next door?"],
        antwoord=[0, 1, 2],
        uitleg="Vraag je met 'who' naar het onderwerp, dan heb je geen 'do' nodig. 'Who does live "
               "next door' is daarom fout.",
    ),
    "Vul het betrekkelijk voornaamwoord in: the shop … sells old records is closed. Gebruik het "
    "woord voor dingen dat met wh begint.": dict(
        type="invultekst",
        vraag="Vul één vraagwoord in: … of these two jackets do you prefer? Je laat kiezen uit twee.",
        antwoord=["which"],
        uitleg="'Which' gebruik je als de keuze beperkt is, 'what' als ze open ligt. 'What jacket "
               "do you want?' kan over elke jas ter wereld gaan.",
    ),
    "In de zin 'the book that I read' mag je 'that' weglaten.": dict(
        type="waarofniet",
        vraag="Vraag je met 'who' naar het onderwerp van de zin, dan gebruik je geen 'do': Who "
              "wants tea?",
        antwoord=True,
        uitleg="'Who' neemt dan zelf de plaats van het onderwerp in. Vergelijk met 'Who do you "
               "want?', waar 'who' het lijdend voorwerp is en 'do' wel nodig is.",
    ),
    "Welk woord hoort in de plaats van de puntjes? This is the town … I was born.": dict(
        type="meerkeuze",
        vraag="Welk vraagwoord past bij iets dat je kan tellen?",
        opties=["how many", "how much", "how long", "how often"],
        antwoord=0,
        uitleg="How many apples, maar how much milk. Kan je het tellen, dan is het 'many'.",
    ),
    "Welke zin over de dag van een ontmoeting is juist?": dict(
        type="meerkeuze",
        vraag="Welke zin vraagt correct naar de prijs?",
        opties=["How much is this jacket?",
                "How many is this jacket?",
                "How much are this jacket?",
                "How many costs this jacket?"],
        antwoord=0,
        uitleg="Een prijs tel je niet, dus is het 'how much'. Het onderwerp is enkelvoud, dus 'is'.",
    ),
    "In het Engels mag je 'what' gebruiken als betrekkelijk voornaamwoord: the film what I saw.":
    dict(
        type="waarofniet",
        vraag="In een vraag met een vraagwoord staat het onderwerp altijd vóór de persoonsvorm: "
              "What you want?",
        antwoord=False,
        uitleg="Het is 'What do you want?'. Het hulpwerkwoord komt vóór het onderwerp; alleen als "
               "het vraagwoord zelf het onderwerp is, blijft die volgorde achterwege.",
    ),

    # ─────────────────────────────────────────────────────────
    # De verleden en de toekomende tijden. De past perfect, 'going to', de
    # future continuous en 'shall' staan niet op de A2-fiche. Deel 2 gaat hier
    # dus volledig over de toekomst met 'will'.
    "'Used to' zegt dat iets vroeger gewoonte was en nu niet meer: I used to play the piano.": dict(
        type="waarofniet",
        vraag="In de past continuous gebruik je 'was' bij I, he, she en it, en 'were' bij you, we "
              "en they.",
        antwoord=True,
        uitleg="I was reading, maar they were reading. Dat is dezelfde verdeling als bij de "
               "tegenwoordige tijd van to be.",
    ),
    "Waaruit bestaat de past perfect simple?": dict(
        type="meerkeuze",
        vraag="Waaruit bestaat de toekomende tijd met will?",
        opties=["will plus de basisvorm van het werkwoord",
                "will plus het werkwoord met -ing erachter",
                "will plus het voltooid deelwoord erachter",
                "will plus de verleden tijd van het werkwoord"],
        antwoord=0,
        uitleg="I will go, she will come. Er komt nooit een s achter het werkwoord, ook niet bij "
               "he, she of it.",
    ),
    "Welke zin over een trein die al weg was is juist?": dict(
        type="meerkeuze",
        vraag="Welke zin over het vertrek van een trein morgen is juist?",
        opties=["The train will leave at six tomorrow.",
                "The train will leaves at six tomorrow.",
                "The train will to leave at six tomorrow.",
                "The train will leaving at six tomorrow."],
        antwoord=0,
        uitleg="Na 'will' staat de kale basisvorm: geen s, geen to, geen -ing.",
    ),
    "Vul het ontbrekende woord in: by the time she called, I … already gone to bed.": dict(
        type="invultekst",
        vraag="Vul het ontbrekende woord in: I … call you tomorrow morning. Het gaat over de "
              "toekomst.",
        antwoord=["will", "'ll"],
        uitleg="'I will call you' of de korte vorm 'I'll call you'. Allebei kijken ze vooruit.",
    ),
    "De past perfect gebruik je om te tonen welk van twee dingen in het verleden het eerst gebeurde.":
    dict(
        type="waarofniet",
        vraag="Je gebruikt 'will' ook voor een beslissing die je op het moment zelf neemt.",
        antwoord=True,
        uitleg="De telefoon gaat en je zegt 'I'll get it'. Je had dat niet gepland; je beslist het "
               "terwijl je het zegt.",
    ),
    "Welke zin klopt qua volgorde in de tijd? 'When I got home, my brother had cooked dinner.'":
    dict(
        type="meerkeuze",
        vraag="Welke zin is een voorspelling over het weer van morgen?",
        opties=["I think it will rain tomorrow.",
                "I think it rains tomorrow a lot.",
                "I think it rained tomorrow again.",
                "I think it is raining tomorrow now."],
        antwoord=0,
        uitleg="Een voorspelling kijkt vooruit, dus gebruik je 'will'. De drie andere zinnen zetten "
               "'tomorrow' bij een tijd die niet vooruitkijkt.",
    ),
    "Welke zinnen hebben terecht een past perfect?": dict(
        type="meerkeuze",
        vraag="Welke zinnen met will zijn juist gevormd?",
        opties=["She will be here at nine.",
                "They will not come tonight.",
                "Will you help me with this?",
                "He will goes to the shop."],
        antwoord=[0, 1, 2],
        uitleg="'He will goes' is fout: na will blijft het werkwoord kaal, dus 'he will go'.",
    ),
    "Na 'after' en 'before' is de past perfect vaak overbodig, want die woorden zeggen zelf al wat "
    "eerst kwam.": dict(
        type="waarofniet",
        vraag="Na 'will' blijft het werkwoord in de basisvorm, ook bij he, she en it.",
        antwoord=True,
        uitleg="He will come, she will stay, it will work. De s van de tegenwoordige tijd valt weg "
               "zodra er 'will' voor staat.",
    ),
    "Wanneer gebruik je 'going to'?": dict(
        type="meerkeuze",
        vraag="Wat is de korte vorm van 'I will'?",
        opties=["I'll", "I'ill", "Il'l", "I'wl"],
        antwoord=0,
        uitleg="De apostrof vervangt wi. Zo ook she'll, we'll en they'll.",
    ),
    "Vul aan met twee woorden: look at those clouds, it … to rain. Gebruik de vorm die bij een "
    "voorspelling met bewijs hoort.": dict(
        type="invultekst",
        vraag="Vul aan met één woord: she … not be at home tonight. Het gaat over vanavond, dus "
              "over de toekomst.",
        antwoord=["will"],
        uitleg="'She will not be at home tonight', of korter 'she won't be at home tonight'.",
    ),
    "Welke zinnen kijken naar de toekomst?": dict(
        type="meerkeuze",
        vraag="Welke zinnen kijken vooruit naar de toekomst?",
        opties=["We will see tomorrow.",
                "She will move next month.",
                "The train will be late.",
                "The train was late again."],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie hebben 'will'. De vierde staat in de verleden tijd en kijkt dus "
               "achteruit.",
    ),
    "Welke vorm gebruik je voor iets dat morgen bezig zal zijn?": dict(
        type="meerkeuze",
        vraag="Welk woord verraadt meteen dat je de toekomende tijd nodig hebt?",
        opties=["tomorrow", "yesterday", "last week", "an hour ago"],
        antwoord=0,
        uitleg="Tomorrow, next week en in a few days wijzen vooruit. De drie andere wijzen naar het "
               "verleden en vragen de past simple.",
    ),
    "'Shall' komt in het moderne Engels vooral voor in vragen zoals 'Shall I open the window?'":
    dict(
        type="waarofniet",
        vraag="'Won't' is de korte vorm van 'will not'.",
        antwoord=True,
        uitleg="Won't is de enige korte vorm die de klank helemaal verandert. Vergelijk met don't "
               "en can't, waar je het hele woord nog hoort.",
    ),
    "Welke zin hoort bij 'Ik had het boek al gelezen voor de film uitkwam.'?": dict(
        type="meerkeuze",
        vraag="Welke zin hoort bij 'Ik zal je morgen het boek meebrengen.'?",
        opties=["I will bring you the book tomorrow.",
                "I bring you the book tomorrow sure.",
                "I brought you the book tomorrow then.",
                "I am bringing you the book now here."],
        antwoord=0,
        uitleg="'Ik zal' wordt 'I will'. Het meewerkend voorwerp 'you' staat voor het lijdend "
               "voorwerp 'the book', zonder 'to'.",
    ),

    # ─────────────────────────────────────────────────────────
    # Zinsdelen en soorten zinnen — deel 2. De betrekkelijke bijzinnen en de
    # conditionals als apart begrip gaan eruit. Wat de fiche wél vraagt,
    # nevenschikking en onderschikking, komt er dieper voor in de plaats.
    "In welke zin staat een betrekkelijke bijzin?": dict(
        type="meerkeuze",
        vraag="In welke zin staat een bijzin?",
        opties=["I stayed at home because it was raining.",
                "I stayed at home and watched a film.",
                "I stayed at home, it was raining hard.",
                "I stayed at home for the whole evening."],
        antwoord=0,
        uitleg="'Because it was raining' kan niet op zichzelf staan: dat maakt er een bijzin van. "
               "'And watched a film' is nevenschikking, geen bijzin.",
    ),
    "Vul aan met één woord: this is the house … we lived for ten years. Het gaat over een plaats.":
    dict(
        type="invultekst",
        vraag="Vul één voegwoord in: … it was raining, we went for a walk. Je geeft een "
              "tegenstelling aan.",
        antwoord=["although", "though"],
        uitleg="Although en though leiden allebei een bijzin met een tegenstelling in. 'But' kan "
               "hier niet, want dat verbindt twee hoofdzinnen.",
    ),
    "Een bijzin die alleen extra informatie geeft, zet je tussen komma's: my sister, who lives in "
    "Ghent, is a vet.": dict(
        type="waarofniet",
        vraag="In een samengestelde zin met 'and' kunnen allebei de delen ook op zichzelf staan.",
        antwoord=True,
        uitleg="'I called her and she answered' bestaat uit twee volwaardige zinnen. Dat is precies "
               "wat nevenschikking betekent.",
    ),
    "Wat is het verschil tussen 'the students who worked hard passed' en 'the students, who worked "
    "hard, passed'?": dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen nevenschikking en onderschikking?",
        opties=["bij nevenschikking zijn de delen gelijkwaardig",
                "bij nevenschikking staat er altijd een komma",
                "bij nevenschikking is de zin altijd korter",
                "bij nevenschikking staat het werkwoord achteraan"],
        antwoord=0,
        uitleg="And, but en or knopen gelijke delen aan elkaar. Because, although en when maken van "
               "het tweede deel een bijzin die van het eerste afhangt.",
    ),
    "Hoe ziet een conditional zero eruit?": dict(
        type="meerkeuze",
        vraag="Welk voegwoord geeft een reden aan?",
        opties=["because", "although", "unless", "while"],
        antwoord=0,
        uitleg="Because geeft de reden. Although geeft een tegenstelling, unless een voorwaarde en "
               "while een gelijktijdigheid.",
    ),
    "Welke zinnen zijn conditionals zero?": dict(
        type="meerkeuze",
        vraag="Welke zinnen zijn samengesteld?",
        opties=["She was tired, but she kept working.",
                "I waited until the bus arrived.",
                "We left early because it was late.",
                "The children played in the garden."],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie hebben twee persoonsvormen en dus twee zinnen in één. De vierde "
               "heeft er maar één en is een enkelvoudige zin.",
    ),
    "Vul aan met één woord: if you study hard, you … pass. Het gaat over één keer, in de toekomst.":
    dict(
        type="invultekst",
        vraag="Vul één voegwoord in: I will wait … you come back. Je bedoelt: tot je terugkomt.",
        antwoord=["until", "till"],
        uitleg="Until en till betekenen allebei 'tot'. Ze leiden een bijzin in die zegt hoelang het "
               "wachten duurt.",
    ),
    "Na 'if' zet je in een conditional first geen will: if it will rain is fout.": dict(
        type="waarofniet",
        vraag="Een bevelende zin heeft meestal geen onderwerp: Close the door, please.",
        antwoord=True,
        uitleg="Het onderwerp 'you' blijft weg, want het is duidelijk wie je aanspreekt. Ontkennend "
               "wordt het 'Don't close the door'.",
    ),
    "Welke zin is een conditional first?": dict(
        type="meerkeuze",
        vraag="Welke zin gebruikt 'so' als nevenschikkend voegwoord?",
        opties=["It was late, so we went home.",
                "It was so late in the evening.",
                "We were so tired after the trip.",
                "So, what did you do yesterday?"],
        antwoord=0,
        uitleg="In de eerste zin verbindt 'so' twee hoofdzinnen en betekent het 'dus'. In de andere "
               "drie is het een bijwoord of een stopwoordje.",
    ),
    "In een conditional mag de hoofdzin ook vooraan staan: we will stay at home if it rains.": dict(
        type="waarofniet",
        vraag="Een zin met twee persoonsvormen is een samengestelde zin.",
        antwoord=True,
        uitleg="Elke persoonsvorm hoort bij een eigen zin. Tel je er twee, dan zijn er twee zinnen "
               "aan elkaar geknoopt, met of zonder voegwoord.",
    ),

    # ─────────────────────────────────────────────────────────
    # Schrijven. Bij dubbele finaliteit bestaat er geen Engels 1 en Engels 2.
    "Literatuurbeleving weegt bij Engels 2 evenveel als schrijven.": dict(
        type="waarofniet",
        vraag="Lezen en luisteren wegen samen even zwaar als alle andere onderdelen van het examen "
              "samen.",
        antwoord=False,
        uitleg="Lezen en luisteren zijn elk 30 %, samen 60 %. De rest, schrijven en spreken samen, "
               "is 40 %. Lezen en luisteren wegen dus zwaarder.",
    ),
}
