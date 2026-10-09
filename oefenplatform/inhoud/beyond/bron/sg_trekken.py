# -*- coding: utf-8 -*-
"""Persoonlijkheid: trekken, de big five en HEXACO.

Het laatste van drie thema's over persoonlijkheidspsychologie, en het meest
telbare: de trektheoretische benadering probeert een persoonlijkheid in een
beperkt aantal eigenschappen te beschrijven.

De lijstjes staan letterlijk in de fiche:

    Gordon Allport, grondlegger: cardinale, centrale en secundaire trekken
    Hans Eysenck, PEN-model: psychoticisme, extraversie, neuroticisme
    Costa en McCrae, Big Five: openheid voor ervaringen, zorgvuldigheid,
        extraversie, vriendelijkheid, emotionele stabiliteit versus
        neuroticisme
    Lee en Ashton, HEXACO-model: integriteit, emotionaliteit, extraversie,
        vriendelijkheid, zorgvuldigheid, openheid voor ervaringen

HEXACO is de Big Five met één factor erbij: de integriteit, in het Engels
honesty-humility. Dat is het verschil tussen de twee modellen, en het is hier
meermaals gevraagd.

Hans Eysenck staat in deze fiche twee keer: bij de biologische benadering met
de arousal, en hier met zijn PEN-model.

Deel 1 is Allport en het PEN-model van Eysenck.
Deel 2 is de Big Five en HEXACO.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat wil de trektheoretische benadering van persoonlijkheid doen?",
        opties=[
            "een persoonlijkheid in vaste eigenschappen beschrijven",
            "een persoonlijkheid uit het brein verklaren",
            "een persoonlijkheid uit de jeugd verklaren",
            "een persoonlijkheid uit de cultuur van een land verklaren",
        ],
        antwoord=0,
        uitleg="Een trektheorie beschrijft eerst: welke eigenschappen heeft iemand en hoe sterk. Het verklaren komt pas daarna.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie noemt de fiche de grondlegger van de trektheoretische benadering?",
        opties=[
            "Gordon Allport",
            "Hans Eysenck",
            "Paul Costa",
            "Michael Ashton",
        ],
        antwoord=0,
        uitleg="Allport. Hij onderscheidde cardinale, centrale en secundaire trekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie soorten trekken onderscheidt Allport?",
        opties=[
            "cardinale trekken",
            "centrale trekken",
            "secundaire trekken",
            "primaire trekken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Cardinaal, centraal en secundair. Primaire trekken staan niet in de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een cardinale trek bij Allport?",
        opties=[
            "een trek die het hele leven van iemand kleurt",
            "een trek die je in veel situaties ziet terugkomen",
            "een trek die alleen in bijzondere situaties opduikt",
            "een trek die iemand van zijn ouders erft",
        ],
        antwoord=0,
        uitleg="Een cardinale trek is zo sterk dat ze alles overheerst. Allport vond dat zeldzaam: de meeste mensen hebben er geen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een centrale trek bij Allport?",
        opties=[
            "een trek die je in veel situaties ziet terugkomen",
            "een trek die het hele leven van iemand kleurt",
            "een trek die zelden naar buiten komt",
            "een trek die iemand alleen thuis laat zien",
        ],
        antwoord=0,
        uitleg="Centrale trekken zijn de vijf tot tien eigenschappen die iemand typeren. Die noem je als je iemand beschrijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een secundaire trek bij Allport?",
        opties=[
            "een trek die maar in bepaalde situaties opduikt",
            "een trek die iemands hele leven lang alles bepaalt",
            "een trek die bij iedereen even sterk is",
            "een trek die iemand nooit laat zien",
        ],
        antwoord=0,
        uitleg="Een secundaire trek komt enkel in bepaalde omstandigheden boven: nerveus bij spreken voor een groep, bijvoorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand is bij alles wat hij doet, thuis en op het werk, in de eerste plaats bezig met rechtvaardigheid. Welke soort trek is dit?",
        opties=[
            "een cardinale trek",
            "een centrale trek",
            "een secundaire trek",
            "een tijdelijke stemming",
        ],
        antwoord=0,
        uitleg="Als één eigenschap alles overheerst en in elke situatie te zien is, is ze cardinaal.",
    ),
    dict(
        type="invultekst",
        vraag="De soort trek bij Allport die slechts in bepaalde situaties naar buiten komt, heet een ... trek.",
        antwoord=["secundaire", "secundair"],
        uitleg="Een secundaire trek. De drie soorten zijn cardinaal, centraal en secundair.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Allport heeft bijna iedereen wel een cardinale trek.",
        antwoord=False,
        uitleg="Niet waar. Allport beschouwde een cardinale trek als zeldzaam. De meeste mensen beschrijf je met centrale trekken.",
    ),
    dict(
        type="waarofniet",
        vraag="Centrale trekken zijn de eigenschappen die je zou noemen als iemand je vraagt hoe een vriend is.",
        antwoord=True,
        uitleg="Waar. De vijf tot tien eigenschappen die iemand typeren, zijn de centrale trekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de drie letters van het PEN-model van Eysenck?",
        opties=[
            "psychoticisme, extraversie en neuroticisme",
            "persoonlijkheid, ervaring en nurture samen",
            "psychodynamiek, empathie en nature",
            "primair, essentieel en normatief",
        ],
        antwoord=0,
        uitleg="P van psychoticisme, E van extraversie, N van neuroticisme. Dat zijn de drie assen van Eysenck.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat meet de as extraversie bij Eysenck?",
        opties=[
            "hoe sterk iemand gezelschap en prikkels zoekt",
            "hoe gevoelig iemand voor stress en zorgen is",
            "hoe weinig iemand zich aan regels houdt",
            "hoe zorgvuldig iemand te werk gaat",
        ],
        antwoord=0,
        uitleg="Extraversie staat tegenover introversie. Eysenck verklaarde dat verschil met de arousal uit het eerdere thema.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat meet de as neuroticisme bij Eysenck?",
        opties=[
            "hoe gevoelig iemand voor stress en zorgen is",
            "hoe sterk iemand gezelschap zoekt",
            "hoe open iemand voor nieuwe dingen staat",
            "hoe vriendelijk iemand in contact is",
        ],
        antwoord=0,
        uitleg="Een hoog neuroticisme betekent sneller en langer gespannen, bezorgd of prikkelbaar zijn.",
    ),
    dict(
        type="invultekst",
        vraag="De drie assen van het PEN-model zijn psychoticisme, neuroticisme en ...",
        antwoord=["extraversie"],
        uitleg="Extraversie. De P, de E en de N van het PEN-model.",
    ),
    dict(
        type="waarofniet",
        vraag="Het PEN-model van Eysenck werkt met minder assen dan de Big Five.",
        antwoord=True,
        uitleg="Waar. Eysenck heeft drie assen, de Big Five vijf en HEXACO zes.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hoge score op een as van het PEN-model betekent dat iemand ziek is.",
        antwoord=False,
        uitleg="Niet waar. De assen beschrijven gewone verschillen tussen mensen. Een hoge score is geen diagnose.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt een trektheorie liever een as dan een hokje?",
        opties=[
            "omdat mensen tussen de twee uitersten in liggen",
            "omdat een hokje te veel mensen bevat",
            "omdat een as makkelijker te onthouden valt dan een hokje",
            "omdat een hokje per cultuur verschilt",
        ],
        antwoord=0,
        uitleg="Niemand is volledig introvert of volledig extravert. Een as laat alle tussenposities toe, een hokje niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat heeft het werk van Allport met de Big Five te maken?",
        opties=[
            "Allport begon het denken in trekken, de Big Five verfijnde dat",
            "Allport heeft de Big Five zelf opgesteld",
            "de Big Five verwerpt het idee van trekken van Allport volledig",
            "de Big Five gaat over trekken bij dieren",
        ],
        antwoord=0,
        uitleg="Allport is de grondlegger van het denken in trekken. Latere onderzoekers brachten die trekken samen tot een beperkt aantal factoren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling is doorgaans zorgvuldig, spontaan en behulpzaam. Welke soort trekken worden hier genoemd?",
        opties=[
            "centrale trekken",
            "cardinale trekken",
            "secundaire trekken",
            "bewustzijnsniveaus",
        ],
        antwoord=0,
        uitleg="Drie eigenschappen die iemand typeren, zonder dat één alles overheerst: dat zijn centrale trekken.",
    ),
    dict(
        type="invultekst",
        vraag="De soort trek bij Allport die zo sterk is dat ze iemands hele leven kleurt, heet een ... trek.",
        antwoord=["cardinale", "cardinaal"],
        uitleg="Een cardinale trek. Allport vond die zeldzaam.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wie staan in de fiche bij de Big Five?",
        opties=[
            "Costa en McCrae",
            "Lee en Ashton",
            "Allport en Eysenck",
            "Darley en Latané",
        ],
        antwoord=0,
        uitleg="Costa en McCrae. Lee en Ashton staan bij HEXACO.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factoren horen bij de Big Five?",
        opties=[
            "openheid voor ervaringen",
            "zorgvuldigheid",
            "vriendelijkheid",
            "integriteit",
            "emotionaliteit",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vijf zijn openheid voor ervaringen, zorgvuldigheid, extraversie, vriendelijkheid en neuroticisme. Integriteit en emotionaliteit komen uit HEXACO.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat meet de factor zorgvuldigheid in de Big Five?",
        opties=[
            "hoe ordelijk en plichtsbewust iemand werkt",
            "hoe graag iemand onder mensen is",
            "hoe open iemand voor nieuwe ideeën staat",
            "hoe snel iemand zich zorgen maakt",
        ],
        antwoord=0,
        uitleg="Zorgvuldigheid of conscientiousness gaat over orde, planning, doorzetten en afspraken nakomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat meet de factor openheid voor ervaringen in de Big Five?",
        opties=[
            "hoe graag iemand nieuwe dingen en ideeën opzoekt",
            "hoe graag iemand onder mensen is",
            "hoe eerlijk iemand tegen anderen is",
            "hoe rustig iemand onder zware stress blijft",
        ],
        antwoord=0,
        uitleg="Openheid gaat over nieuwsgierigheid, fantasie en belangstelling voor kunst, ideeën en het onbekende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat meet de factor vriendelijkheid in de Big Five?",
        opties=[
            "hoe meegaand en hulpvaardig iemand in contact is",
            "hoe graag iemand het middelpunt van een groep is",
            "hoe zorgvuldig iemand zijn werk afmaakt",
            "hoe gevoelig iemand voor stress is",
        ],
        antwoord=0,
        uitleg="Vriendelijkheid of agreeableness gaat over samenwerken, vertrouwen geven en rekening houden met anderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt de fiche de vijfde factor van de Big Five?",
        opties=[
            "emotionele stabiliteit versus neuroticisme",
            "integriteit versus volstrekte oneerlijkheid",
            "introversie versus extraversie",
            "openheid versus geslotenheid",
        ],
        antwoord=0,
        uitleg="De fiche zet die factor met twee polen: emotionele stabiliteit aan de ene kant, neuroticisme aan de andere.",
    ),
    dict(
        type="invultekst",
        vraag="De factor van de Big Five die over orde, planning en doorzetten gaat, heet ...",
        antwoord=["zorgvuldigheid"],
        uitleg="Zorgvuldigheid, in het Engels conscientiousness.",
    ),
    dict(
        type="waarofniet",
        vraag="De Big Five bestaat uit vijf factoren waarop iedereen een score heeft, hoog of laag.",
        antwoord=True,
        uitleg="Waar. Het zijn geen types maar assen: iedereen zit ergens op elk van de vijf.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lage score op een factor van de Big Five betekent dat die factor bij iemand niet bestaat.",
        antwoord=False,
        uitleg="Niet waar. Een lage score is ook een score. Weinig extravert betekent introvert, niet zonder die eigenschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie staan in de fiche bij het HEXACO-model?",
        opties=[
            "Kibeom Lee en Michael Ashton",
            "Costa en McCrae",
            "Gordon Allport en Hans Eysenck",
            "Jeffrey Gray en Julian Rotter",
        ],
        antwoord=0,
        uitleg="Lee en Ashton. Hun model heeft zes factoren in plaats van vijf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel factoren heeft het HEXACO-model?",
        opties=[
            "zes",
            "vijf",
            "drie",
            "zeven",
        ],
        antwoord=0,
        uitleg="Zes. De naam HEXACO verwijst naar de zes beginletters van de factoren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factor heeft HEXACO bovenop de Big Five?",
        opties=[
            "de integriteit",
            "de zorgvuldigheid",
            "de extraversie",
            "de vriendelijkheid",
        ],
        antwoord=0,
        uitleg="De integriteit, in het Engels honesty-humility. Dat is precies het verschil tussen de twee modellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat meet de factor integriteit in HEXACO?",
        opties=[
            "hoe oprecht en bescheiden iemand is",
            "hoe meegaand iemand in een groep is",
            "hoe ordelijk iemand werkt",
            "hoe open iemand voor ideeën is",
        ],
        antwoord=0,
        uitleg="Integriteit gaat over eerlijkheid, bescheidenheid en anderen niet gebruiken voor eigen gewin.",
    ),
    dict(
        type="invultekst",
        vraag="De factor die HEXACO extra heeft tegenover de Big Five, heet in de fiche de ...",
        antwoord=["integriteit"],
        uitleg="De integriteit. In het Engels staat er honesty-humility.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factoren komen in zowel de Big Five als HEXACO voor?",
        opties=[
            "extraversie",
            "vriendelijkheid",
            "zorgvuldigheid",
            "integriteit",
        ],
        antwoord=[0, 1, 2],
        uitleg="Extraversie, vriendelijkheid, zorgvuldigheid en openheid staan in beide. De integriteit staat enkel in HEXACO.",
    ),
    dict(
        type="waarofniet",
        vraag="HEXACO gebruikt het woord emotionaliteit waar de Big Five over neuroticisme spreekt.",
        antwoord=True,
        uitleg="Waar. De fiche noemt de HEXACO-factor Emotionality en vertaalt ze als emotionaliteit.",
    ),
    dict(
        type="waarofniet",
        vraag="HEXACO verwerpt de Big Five volledig en begint helemaal opnieuw.",
        antwoord=False,
        uitleg="Niet waar. HEXACO bouwt erop verder: vier factoren zijn gelijk, een krijgt een andere naam en een komt erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een werkgever wil weten of een kandidaat met geld van de zaak eerlijk omgaat. Welk model biedt daar een eigen factor voor?",
        opties=[
            "HEXACO, met de integriteit",
            "de Big Five, met de vriendelijkheid",
            "het PEN-model, met het psychoticisme",
            "Allport, met de cardinale trek",
        ],
        antwoord=0,
        uitleg="Juist voor dat soort vragen voegden Lee en Ashton de integriteit toe. De Big Five heeft er geen aparte factor voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is cross-cultureel onderzoek belangrijk voor een model als de Big Five?",
        opties=[
            "om na te gaan of de vijf factoren overal terugkomen",
            "om na te gaan hoeveel mensen er hoog op scoren",
            "om de vragenlijst korter te maken",
            "om een zesde factor te kunnen verwerpen",
        ],
        antwoord=0,
        uitleg="Als dezelfde factoren in heel verschillende talen en landen opduiken, zegt het model iets over mensen en niet over één cultuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een bezwaar tegen de trektheoretische benadering?",
        opties=[
            "ze beschrijft goed, maar verklaart weinig",
            "ze verklaart goed, maar beschrijft weinig",
            "ze kan geen verschillen tussen mensen meten",
            "ze werkt niet met vragenlijsten of scores",
        ],
        antwoord=0,
        uitleg="Een score op vijf of zes assen zegt hoe iemand is, maar niet waar die eigenschappen vandaan komen. Daarvoor heb je de andere benaderingen nodig.",
    ),
]
