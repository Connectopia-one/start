# -*- coding: utf-8 -*-
"""Pedagogische modellen en opvoeden in bijzondere contexten.

Het tweede van twee thema's over pedagogiek. Hier staan de visies achter het
opvoeden, de factoren die meespelen, en de modellen waarmee je een
opvoedingssituatie uit elkaar haalt. Daarna volgt het opvoeden in bijzondere
contexten, met de orthopedagogische modellen.

De lijstjes staan letterlijk in de fiche:

    historische pedagogische visies: de leer van Confucius, de leer van Plato,
        Abu Hamid ibn Muhammad Al-Ghazali, Jean-Jacques Rousseau
    hedendaagse pedagogische visies: behoefteondersteunende opvoeding,
        nieuwe autoriteit
    beïnvloedende factoren: risicofactoren en beschermende factoren, op
        microniveau, mesoniveau en macroniveau
    pedagogische modellen: het bio-ecologisch model van Urie Bronfenbrenner
        (vijf systemen) en het balansmodel van Bakker et al. (draaglast en
        draagkracht)
    bijzondere contexten: handicap (fysiek, zintuiglijk, verstandelijk,
        meervoudig), ontwikkelingsstoornissen (ADHD, ASS), leerstoornissen
        (dyslexie, dyscalculie), verontrustende opvoedingssituaties (VOS),
        maatschappelijke kwetsbaarheid en kansarmoede
    orthopedagogische modellen: kwaliteit van bestaan van Schalock en Verdugo
        (onafhankelijkheid, sociale participatie, welbevinden) en het
        viervariabelenmodel van Jacobus E. Rink (K, O, Sc en St)

De fiche noemt bij de hedendaagse visies geen namen. Daarom vragen de vragen
hieronder wat de visies inhouden, en niet wie ze bedacht heeft.

Deel 1 zijn de visies, de factoren en de pedagogische modellen.
Deel 2 zijn de bijzondere contexten en de orthopedagogische modellen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een pedagogische visie?",
        opties=[
            "een samenhangend idee over hoe je hoort op te voeden",
            "een vaste reeks regels die elke ouder moet volgen",
            "een onderzoek naar het gedrag van één kind",
            "een lijst van toegestane opvoedingsmiddelen",
        ],
        antwoord=0,
        uitleg="Een visie is een onderliggend idee over wat opvoeden is en waar het naartoe moet. Uit die visie volgen dan de keuzes in de praktijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke namen noemt de fiche bij de historische pedagogische visies?",
        opties=[
            "Confucius",
            "Plato",
            "Jean-Jacques Rousseau",
            "Urie Bronfenbrenner",
            "Jacobus E. Rink",
        ],
        antwoord=[0, 1, 2],
        uitleg="Vier historische visies: Confucius, Plato, Al-Ghazali en Rousseau. Bronfenbrenner en Rink staan bij de modellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar legt de leer van Confucius de nadruk op in de opvoeding?",
        opties=[
            "op respect, deugd en het goede voorbeeld",
            "op de vrije natuur van het kind",
            "op de opvoeding door de staat",
            "op belonen en straffen",
        ],
        antwoord=0,
        uitleg="Bij Confucius staan respect voor ouderen, deugdzaamheid en het voorbeeld van de opvoeder centraal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor de visie van Plato op opvoeding?",
        opties=[
            "opvoeding is een opdracht van de samenleving zelf",
            "opvoeding hoort volledig in het gezin thuis",
            "opvoeding moet het kind met rust laten",
            "opvoeding hoort pas na de kindertijd te beginnen",
        ],
        antwoord=0,
        uitleg="Plato denkt opvoeding vanuit de ideale staat: de samenleving voedt mee op en elk mens krijgt een plaats naar zijn aard.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor de visie van Jean-Jacques Rousseau?",
        opties=[
            "opvoeden moet de natuur van het kind volgen",
            "opvoeden moet de natuur van het kind breken",
            "opvoeden is in de eerste plaats kennis overdragen",
            "opvoeden is de taak van de staat alleen",
        ],
        antwoord=0,
        uitleg="Rousseau gaat ervan uit dat een kind van nature goed is. Opvoeden moet daarom aansluiten bij wat het kind op dat moment aankan.",
    ),
    dict(
        type="invultekst",
        vraag="De vierde historische visie in de fiche, naast Confucius, Plato en Rousseau, is van Abu Hamid ibn Muhammad ...",
        antwoord=["Al-Ghazali", "Al Ghazali", "Ghazali"],
        uitleg="Al-Ghazali. Zijn werk legt de nadruk op de vorming van het karakter, met gewoonte en voorbeeld als weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat houdt de behoefteondersteunende opvoeding in?",
        opties=[
            "opvoeden dat ingaat op de basisbehoeften van een kind",
            "opvoeden dat een kind alles geeft wat het vraagt",
            "opvoeden dat met zo weinig regels mogelijk werkt",
            "opvoeden dat uitsluitend met belonen werkt",
        ],
        antwoord=0,
        uitleg="Deze hedendaagse visie vertrekt van de behoeften van een kind: ruimte om zelf te kiezen, zich verbonden voelen en iets kunnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat houdt de visie van de nieuwe autoriteit in?",
        opties=[
            "gezag door aanwezigheid en steun, niet door macht",
            "gezag door strenger te straffen dan vroeger",
            "gezag volledig aan het kind overlaten",
            "gezag enkel bij de school leggen",
        ],
        antwoord=0,
        uitleg="De nieuwe autoriteit zoekt gezag in nabijheid, volharding en een netwerk rond het kind, in plaats van in overwicht en straf.",
    ),
    dict(
        type="waarofniet",
        vraag="Historische pedagogische visies hebben volgens de fiche nog invloed op de pedagogiek van vandaag.",
        antwoord=True,
        uitleg="Waar. De fiche vraagt uitdrukkelijk uit te leggen waarom die oude visies vandaag nog doorwerken.",
    ),
    dict(
        type="waarofniet",
        vraag="De nieuwe autoriteit betekent dat een opvoeder geen grenzen meer stelt.",
        antwoord=False,
        uitleg="Niet waar. De grenzen blijven, maar ze worden niet met macht doorgedrukt. Een opvoeder houdt vol en zoekt steun bij anderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een risicofactor in de opvoeding?",
        opties=[
            "iets dat de kans op problemen groter maakt",
            "iets dat de kans op problemen kleiner maakt",
            "iets dat een kind altijd schade toebrengt",
            "iets dat alleen op macroniveau voorkomt",
        ],
        antwoord=0,
        uitleg="Een risicofactor verhoogt de kans, maar maakt niets zeker. Daarnaast staan de beschermende factoren, die de kans verkleinen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke drie niveaus kunnen beïnvloedende factoren volgens de fiche spelen?",
        opties=[
            "microniveau",
            "mesoniveau",
            "macroniveau",
            "chrononiveau",
        ],
        antwoord=[0, 1, 2],
        uitleg="Micro, meso en macro. Het chronosysteem is een begrip van Bronfenbrenner, geen niveau in deze lijst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een grootmoeder die elke week opvangt en bijstaat, is in de opvoeding vooral wat?",
        opties=[
            "een beschermende factor",
            "een risicofactor",
            "een opvoedingsmiddel",
            "een opvoedingsdimensie",
        ],
        antwoord=0,
        uitleg="Steun uit de omgeving verkleint de kans op problemen. Dat is een beschermende factor, hier op mesoniveau.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt de fiche opvoeding een multifactorieel proces?",
        opties=[
            "omdat er altijd meerdere factoren samen inwerken",
            "omdat er altijd precies drie factoren inwerken",
            "omdat elke factor even zwaar weegt",
            "omdat één factor volstaat om alles te verklaren",
        ],
        antwoord=0,
        uitleg="Multifactorieel betekent dat je nooit één oorzaak kan aanwijzen. Risicofactoren en beschermende factoren tellen samen op drie niveaus.",
    ),
    dict(
        type="invultekst",
        vraag="Een factor die de kans op problemen in de opvoeding verkleint, heet een ... factor.",
        antwoord=["beschermende", "beschermend"],
        uitleg="Een beschermende factor. Haar tegenhanger is de risicofactor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee pedagogische modellen noemt de fiche?",
        opties=[
            "het bio-ecologisch model van Bronfenbrenner",
            "het balansmodel van Bakker en anderen",
            "het viervariabelenmodel van Rink",
            "het PEN-model van Eysenck",
        ],
        antwoord=[0, 1],
        uitleg="Die twee. Het viervariabelenmodel van Rink is een orthopedagogisch model, en het PEN-model hoort bij persoonlijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke twee begrippen werkt het balansmodel van Bakker en anderen?",
        opties=[
            "draaglast en draagkracht",
            "risico en kans",
            "micro en macro",
            "autonomie en controle",
        ],
        antwoord=0,
        uitleg="De draaglast is wat een gezin te dragen heeft, de draagkracht is wat het kan dragen. Als de last zwaarder weegt, loopt het mis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gezin krijgt op korte tijd een ziekte, een ontslag en een verhuis te verwerken, maar heeft een sterk netwerk rond zich. Hoe lees je dat in het balansmodel?",
        opties=[
            "veel draaglast, maar ook veel draagkracht",
            "veel draagkracht, maar geen draaglast",
            "weinig draaglast en weinig draagkracht",
            "geen van beide, het model geldt hier niet",
        ],
        antwoord=0,
        uitleg="De drie gebeurtenissen zijn draaglast, het netwerk is draagkracht. Het balansmodel weegt die twee tegen elkaar af.",
    ),
    dict(
        type="waarofniet",
        vraag="In het balansmodel kan je een gezin ook helpen door de draagkracht te vergroten in plaats van de draaglast te verkleinen.",
        antwoord=True,
        uitleg="Waar. Soms kan je de last niet wegnemen. Dan helpt extra steun, zodat het gezin meer kan dragen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het bio-ecologisch model komt in deze vakfiche maar één keer voor.",
        antwoord=False,
        uitleg="Niet waar. Het staat bij de systemische benadering van ontwikkeling en hier opnieuw als pedagogisch model. Dezelfde vijf systemen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een opvoedingssituatie in een bijzondere context?",
        opties=[
            "een situatie waarin opvoeden extra vraagt van iedereen",
            "een situatie waarin niemand het kind kan opvoeden",
            "een situatie die alleen op school voorkomt",
            "een situatie waarin geen enkel model nog opgaat",
        ],
        antwoord=0,
        uitleg="Een bijzondere context vraagt meer van het kind, van de opvoeders en van de omgeving. Opvoeden gaat verder, maar met andere accenten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten handicap noemt de fiche?",
        opties=[
            "een fysieke handicap",
            "een zintuiglijke handicap",
            "een verstandelijke handicap",
            "een tijdelijke handicap",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt vier soorten: fysiek, zintuiglijk, verstandelijk en meervoudig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee ontwikkelingsstoornissen noemt de fiche bij naam?",
        opties=[
            "ADHD en ASS",
            "dyslexie en dyscalculie",
            "ADHD en dyslexie",
            "ASS en dyscalculie",
        ],
        antwoord=0,
        uitleg="ADHD en ASS staan bij de ontwikkelingsstoornissen. Dyslexie en dyscalculie staan apart, bij de leerstoornissen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee leerstoornissen noemt de fiche bij naam?",
        opties=[
            "dyslexie en dyscalculie",
            "ADHD en ASS",
            "dyslexie en ADHD",
            "dyscalculie en ASS",
        ],
        antwoord=0,
        uitleg="Dyslexie, moeite met lezen en spellen, en dyscalculie, moeite met rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staat de afkorting VOS in de fiche?",
        opties=[
            "verontrustende opvoedingssituatie",
            "veilige opvoedingssituatie",
            "vrijwillige ondersteuning in school",
            "verplichte ondersteuning in school",
        ],
        antwoord=0,
        uitleg="Een verontrustende opvoedingssituatie: een situatie waarin de ontwikkeling van een kind bedreigd is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt de fiche met maatschappelijke kwetsbaarheid?",
        opties=[
            "een gezin botst telkens op nadeel in de samenleving",
            "een gezin wil geen hulp van buitenaf aanvaarden",
            "een kind is lichamelijk kwetsbaar",
            "een kind heeft een leerstoornis",
        ],
        antwoord=0,
        uitleg="Bij maatschappelijke kwetsbaarheid, met kansarmoede als voorbeeld in de fiche, werken instellingen eerder tegen dan mee voor een gezin.",
    ),
    dict(
        type="invultekst",
        vraag="De leerstoornis waarbij rekenen heel moeilijk gaat, heet ...",
        antwoord=["dyscalculie"],
        uitleg="Dyscalculie. De leerstoornis voor lezen en spellen is dyslexie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bijzondere context raakt volgens de fiche niet alleen het kind, maar ook de opvoeders en de omgeving.",
        antwoord=True,
        uitleg="Waar. De fiche vraagt uitdrukkelijk naar de invloed op het kind, de opvoeders én de omgeving.",
    ),
    dict(
        type="waarofniet",
        vraag="Kansarmoede staat in de fiche bij de ontwikkelingsstoornissen.",
        antwoord=False,
        uitleg="Niet waar. Kansarmoede staat bij de maatschappelijke kwetsbaarheid. ADHD en ASS zijn de ontwikkelingsstoornissen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee orthopedagogische modellen noemt de fiche?",
        opties=[
            "de kwaliteit van bestaan van Schalock en Verdugo",
            "het viervariabelenmodel van Jacobus E. Rink",
            "het balansmodel van Bakker en anderen",
            "het bio-ecologisch model van Bronfenbrenner",
        ],
        antwoord=[0, 1],
        uitleg="Die twee zijn de orthopedagogische modellen. Het balansmodel en het bio-ecologisch model staan bij de pedagogische modellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie grote delen heeft het model kwaliteit van bestaan van Schalock en Verdugo?",
        opties=[
            "onafhankelijkheid",
            "sociale participatie",
            "welbevinden",
            "draagkracht",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie, elk met eigen onderdelen. Draagkracht hoort bij het balansmodel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort volgens Schalock en Verdugo bij onafhankelijkheid?",
        opties=[
            "persoonlijke ontwikkeling en zelfbepaling",
            "interpersoonlijke relaties en rechten",
            "emotioneel en fysiek welbevinden",
            "sociale inclusie en materieel welbevinden",
        ],
        antwoord=0,
        uitleg="Onafhankelijkheid bestaat uit persoonlijke ontwikkeling en zelfbepaling: zelf kunnen groeien en zelf kunnen beslissen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort volgens Schalock en Verdugo bij sociale participatie?",
        opties=[
            "relaties, sociale inclusie en rechten",
            "persoonlijke ontwikkeling en zelfbepaling",
            "emotioneel, fysiek en materieel welbevinden",
            "draaglast en draagkracht",
        ],
        antwoord=0,
        uitleg="Sociale participatie bestaat uit interpersoonlijke relaties, sociale inclusie en rechten: erbij horen en meetellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie soorten welbevinden noemt het model kwaliteit van bestaan?",
        opties=[
            "emotioneel welbevinden",
            "fysiek welbevinden",
            "materieel welbevinden",
            "sociaal welbevinden",
        ],
        antwoord=[0, 1, 2],
        uitleg="Emotioneel, fysiek en materieel welbevinden. Het sociale zit in het andere deel, de sociale participatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de vier variabelen in het model van Rink?",
        opties=[
            "kind, opvoeder, situationele context en situatietypes",
            "kind, ouder, school en samenleving",
            "kennis, oefening, steun en structuur",
            "kind, omgeving, school en tijd",
        ],
        antwoord=0,
        uitleg="De K-variabele is het kind, de O-variabele de opvoeder, de Sc-variabele de situationele context en de St-variabele de situatietypes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie zaken horen volgens Rink bij de situatietypes?",
        opties=[
            "de activiteiten",
            "de regels of sociale verwachtingen",
            "de sfeer",
            "de draagkracht",
        ],
        antwoord=[0, 1, 2],
        uitleg="Activiteiten, regels of sociale verwachtingen, en sfeer. Dat zijn de drie onderdelen van de St-variabele.",
    ),
    dict(
        type="invultekst",
        vraag="In het model van Rink staat de letter O voor de ...",
        antwoord=["opvoeder"],
        uitleg="De opvoeder. K staat voor het kind, Sc voor de situationele context en St voor de situatietypes.",
    ),
    dict(
        type="waarofniet",
        vraag="Het model van Rink helpt om te kijken of een situatie zelf aangepast kan worden in plaats van alleen het kind.",
        antwoord=True,
        uitleg="Waar. Door de context en het situatietype apart te zetten, zie je dat ook de activiteit, de regels of de sfeer veranderd kunnen worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Het model kwaliteit van bestaan kijkt alleen naar de gezondheid van iemand.",
        antwoord=False,
        uitleg="Niet waar. Het fysieke welbevinden is maar een van de onderdelen. Zelfbepaling, relaties, inclusie en rechten horen er ook bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraagt de fiche om een opvoedingssituatie in een bijzondere context met een model te bekijken?",
        opties=[
            "omdat een model je alle kanten laat nagaan in plaats van één",
            "omdat een model het probleem onmiddellijk oplost",
            "omdat een model zegt wie er schuld heeft",
            "omdat een model de hulp verplicht maakt",
        ],
        antwoord=0,
        uitleg="Een model dwingt je om naar het kind, de opvoeders, de context en de niveaus te kijken, met risicofactoren en beschermende factoren erbij.",
    ),
]
