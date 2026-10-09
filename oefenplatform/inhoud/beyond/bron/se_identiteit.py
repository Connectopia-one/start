# -*- coding: utf-8 -*-
"""Identiteit: de lagen, de factoren en het wereldbeeld.

Het blok "ik ben wie ik ben" weegt vijf procent, het lichtste van de negen.
Toch is het de sleutel van de hele fiche: de drie woorden waarmee het leerdoel
identiteit beschrijft — relationeel, gelaagd en dynamisch — komen later terug
bij diversiteit en bij samenleven.

De fiche is hier heel precies over de lijstjes, en die staan hieronder letterlijk:

    persoonlijke identiteit: biologische aspecten, persoonlijkheidstrekken,
        familiale achtergrond
    groepsidentiteit: regionale, nationale en supranationale aspecten; groepen
        waar je deel van uitmaakt (gendergerelateerde, sociaaleconomische en
        levensbeschouwelijke groepen); subculturen
    factoren die de identiteit vormen: verbondenheid, discriminatie,
        wij-zij-denken

De fiche zegt ook dat je op het examen altijd **fictieve situaties** krijgt,
"om neutraliteit te garanderen en persoonsgegevens te beschermen". De
situatievragen hieronder zijn daarom ook met verzonnen namen geschreven.

Deel 1 is wat identiteit is en uit welke lagen ze bestaat.
Deel 2 is hoe die lagen elkaar beïnvloeden en hoe een identiteit verandert.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt de vakfiche met identiteit?",
        opties=[
            "het geheel van wie iemand is, in verhouding tot anderen",
            "de gegevens die op iemands identiteitskaart staan afgedrukt",
            "het karakter waarmee iemand geboren wordt en dat vastligt",
            "de rol die iemand opneemt in zijn of haar eigen gezin",
        ],
        antwoord=0,
        uitleg="De fiche noemt identiteit relationeel: wie je bent, krijgt vorm in verhouding tot de mensen rond je.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee soorten identiteit onderscheidt de vakfiche?",
        opties=[
            "persoonlijke identiteit en groepsidentiteit",
            "wettelijke identiteit en gevoelsidentiteit",
            "aangeboren identiteit en gekozen identiteit",
            "binnenlandse identiteit en buitenlandse identiteit",
        ],
        antwoord=0,
        uitleg="Alleen die twee staan in de fiche. De andere namen bestaan daar niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke drie dingen zijn de lagen van je persoonlijke identiteit verbonden?",
        opties=[
            "biologische aspecten, persoonlijkheidstrekken en familiale achtergrond",
            "nationaliteit, subcultuur en sociaaleconomische groep",
            "opleiding, beroep en inkomen van je ouders of verzorgers",
            "taal, geloofsovertuiging en de streek waar je woont",
        ],
        antwoord=0,
        uitleg="De andere rijtjes horen bij de groepsidentiteit of staan helemaal niet in de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Thema is geboren met een hartafwijking. Bij welke laag van haar persoonlijke identiteit hoort dat?",
        opties=[
            "de biologische aspecten",
            "de persoonlijkheidstrekken",
            "de familiale achtergrond",
            "de subcultuur waar ze bij hoort",
        ],
        antwoord=0,
        uitleg="Alles wat met je lichaam zelf te maken heeft, hoort bij de biologische aspecten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Joris is van jongs af aan erg verlegen. Bij welke laag hoort dat?",
        opties=[
            "de persoonlijkheidstrekken",
            "de biologische aspecten",
            "de familiale achtergrond",
            "de levensbeschouwelijke groep",
        ],
        antwoord=0,
        uitleg="Verlegenheid is een trek van je persoonlijkheid, geen lichamelijk gegeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lagen horen volgens de fiche bij de groepsidentiteit?",
        opties=[
            "regionale, nationale en supranationale aspecten",
            "de groepen waar je deel van uitmaakt",
            "de subculturen waar je bij hoort",
            "de persoonlijkheidstrekken die je van jongs af hebt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt er drie. Persoonlijkheidstrekken horen bij de persoonlijke identiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke groepen noemt de fiche als onderdeel van de groepsidentiteit?",
        opties=[
            "gendergerelateerde groepen",
            "sociaaleconomische groepen",
            "levensbeschouwelijke groepen",
            "groepen op basis van je schoolresultaten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie staan er met zoveel woorden. Over schoolresultaten zegt de fiche niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand noemt zich in de eerste plaats Europeaan. Bij welke laag hoort dat?",
        opties=[
            "een supranationaal aspect van de groepsidentiteit",
            "een nationaal aspect van de groepsidentiteit",
            "een regionaal aspect van de groepsidentiteit",
            "een persoonlijkheidstrek binnen de eigen identiteit",
        ],
        antwoord=0,
        uitleg="Supranationaal betekent boven het niveau van één land, en Europa is daar het gewone voorbeeld van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een subcultuur?",
        opties=[
            "een kleinere groep met eigen gewoonten binnen een grotere cultuur",
            "een cultuur die minder waard is dan de cultuur van de meerderheid",
            "de cultuur van een land waar weinig mensen wonen",
            "een groep die zich volledig afsluit van de samenleving",
        ],
        antwoord=0,
        uitleg="Denk aan een muziekscene of een sportwereld: eigen taal en gewoonten, binnen de grotere cultuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Je persoonlijke identiteit en je groepsidentiteit staan volledig los van elkaar.",
        antwoord=False,
        uitleg="Ze beïnvloeden elkaar. De fiche vraagt juist dat je over die wederzijdse invloed kan nadenken.",
    ),
    dict(
        type="waarofniet",
        vraag="Je familiale achtergrond is volgens de fiche een laag van je persoonlijke identiteit.",
        antwoord=True,
        uitleg="Ze staat in het rijtje naast de biologische aspecten en de persoonlijkheidstrekken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een identiteit ligt vast vanaf je geboorte en verandert daarna niet meer.",
        antwoord=False,
        uitleg="De fiche noemt identiteit dynamisch: ze kan veranderen in de loop van je leven.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens de fiche bestaat je identiteit uit meerdere lagen samen.",
        antwoord=True,
        uitleg="Gelaagd is een van de drie woorden waarmee het leerdoel identiteit beschrijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat identiteit relationeel is?",
        opties=[
            "ze krijgt vorm in de omgang met andere mensen",
            "ze hangt af van je relatie met één vaste partner",
            "ze ligt vast zolang je in dezelfde groep blijft",
            "ze bestaat enkel binnen je eigen familie",
        ],
        antwoord=0,
        uitleg="Relationeel verwijst naar alle mensen rond je, niet alleen naar een liefdesrelatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat identiteit dynamisch is?",
        opties=[
            "ze kan in de loop van je leven veranderen",
            "ze beweegt mee met de mode van het moment",
            "ze is bij iedereen even sterk aanwezig",
            "ze wordt bepaald door je lichamelijke energie",
        ],
        antwoord=0,
        uitleg="Dynamisch staat tegenover vast: wie je bent, kan verschuiven.",
    ),
    dict(
        type="invultekst",
        vraag="Vul aan: de drie woorden waarmee de fiche identiteit beschrijft zijn relationeel, dynamisch en ...",
        antwoord=["gelaagd"],
        uitleg="Relationeel, gelaagd en dynamisch: die drie samen vormen het leerdoel van dit blok.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt de fiche een kleinere groep met eigen gewoonten binnen een grotere cultuur?",
        antwoord=["subcultuur", "een subcultuur"],
        uitleg="Subculturen horen bij de lagen van de groepsidentiteit.",
    ),
    dict(
        type="invultekst",
        vraag="Welk woord gebruikt de fiche voor identiteit die hoger reikt dan één land, zoals Europees?",
        antwoord=["supranationaal", "supranationale"],
        uitleg="Regionaal, nationaal en supranationaal: de drie niveaus in het rijtje van de groepsidentiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom krijg je op het examen fictieve situaties in plaats van echte?",
        opties=[
            "om neutraliteit te bewaren en persoonsgegevens te beschermen",
            "omdat echte situaties te moeilijk zijn om kort te beschrijven",
            "omdat de fiche elk jaar nieuwe voorbeelden moet verzinnen",
            "om te vermijden dat je de actualiteit moet opvolgen",
        ],
        antwoord=0,
        uitleg="Die twee redenen staan letterlijk in de fiche. De actualiteit moet je trouwens wél opvolgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vraagt de fiche je over de actualiteit?",
        opties=[
            "dat je ze opvolgt op lokaal, regionaal en nationaal vlak",
            "dat je er op het examen letterlijk uit kan citeren",
            "dat je enkel het nationale nieuws van dit jaar kent",
            "dat je er niets van hoeft te weten voor dit vak",
        ],
        antwoord=0,
        uitleg="Die drie niveaus staan bij Wat moet je leren, meteen vooraan in de fiche.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie factoren noemt de fiche als dingen die je identiteit vormen en beïnvloeden?",
        opties=[
            "verbondenheid, discriminatie en wij-zij-denken",
            "opvoeding, onderwijs en vriendenkring",
            "taal, geloof en nationaliteit",
            "inkomen, beroep en woonplaats",
        ],
        antwoord=0,
        uitleg="Precies die drie staan in de fiche, en over die drie moet je kunnen nadenken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is verbondenheid als factor in de vorming van een identiteit?",
        opties=[
            "het gevoel ergens bij te horen en erkend te worden",
            "het aantal mensen dat je in je omgeving kent",
            "de band die je wettelijk met je familie hebt",
            "de plicht om je aan te passen aan een groep",
        ],
        antwoord=0,
        uitleg="Wie zich verbonden voelt met een groep, neemt iets van die groep mee in de eigen identiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is wij-zij-denken?",
        opties=[
            "mensen indelen in een eigen groep en een andere groep",
            "een gesprek voeren waarin ieder zijn mening geeft",
            "het verschil tussen een persoonlijke en een groepsidentiteit",
            "de regels die binnen een subcultuur gelden",
        ],
        antwoord=0,
        uitleg="Wij-zij-denken zet de eigen groep tegenover de anderen, en dat kleurt hoe je naar jezelf kijkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Nora wordt op de sportclub nooit gekozen omdat ze een hoofddoek draagt. Welke factor is hier aan het werk?",
        opties=[
            "discriminatie",
            "verbondenheid",
            "een biologisch aspect",
            "een supranationaal aspect",
        ],
        antwoord=0,
        uitleg="Ze wordt anders behandeld om een kenmerk van haar identiteit. Dat is discriminatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan discriminatie doen met iemands identiteit?",
        opties=[
            "ze kan het gevoel van verbondenheid afbreken",
            "ze laat de identiteit volledig onaangeroerd",
            "ze maakt de persoonlijke identiteit sterker",
            "ze vervangt de groepsidentiteit door een nationale",
        ],
        antwoord=0,
        uitleg="Wie uitgesloten wordt, voelt zich minder deel van de groep, en dat raakt de identiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een mensbeeld?",
        opties=[
            "de manier waarop je naar de mens en zijn aard kijkt",
            "een foto of tekening waarop een mens te zien is",
            "het beeld dat anderen van jou hebben",
            "de wettelijke beschrijving van een persoon",
        ],
        antwoord=0,
        uitleg="Je mensbeeld gaat over wat je denkt dat de mens is: goed, vrij, verantwoordelijk, en zo verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe staan het wereldbeeld en de identiteit volgens de fiche tot elkaar?",
        opties=[
            "ze bepalen elkaar in twee richtingen",
            "het wereldbeeld bepaalt de identiteit, niet omgekeerd",
            "de identiteit bepaalt het wereldbeeld, niet omgekeerd",
            "ze hebben niets met elkaar te maken",
        ],
        antwoord=0,
        uitleg="De fiche zegt letterlijk: hoe het mens- en wereldbeeld de identiteit bepaalt en andersom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Kan iemands wereldbeeld veranderen?",
        opties=[
            "ja, de fiche vraagt juist dat je over die verandering nadenkt",
            "nee, een wereldbeeld staat vast na de kindertijd",
            "enkel wanneer iemand van land verhuist",
            "enkel wanneer iemand van geloof verandert",
        ],
        antwoord=0,
        uitleg="De fiche vraagt te reflecteren over hoe het wereldbeeld bij een persoon kan veranderen.",
    ),
    dict(
        type="waarofniet",
        vraag="Verbondenheid, discriminatie en wij-zij-denken zijn de drie factoren die de fiche noemt.",
        antwoord=True,
        uitleg="Precies die drie, en in die bewoordingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Wij-zij-denken komt altijd van buitenaf en nooit uit de eigen groep.",
        antwoord=False,
        uitleg="Een groep kan zelf een scherpe grens trekken tussen wij en zij.",
    ),
    dict(
        type="waarofniet",
        vraag="De lagen van je identiteit kunnen elkaar onderling beïnvloeden.",
        antwoord=True,
        uitleg="De fiche vraagt uit te leggen hoe de verschillende lagen elkaar beïnvloeden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een mensbeeld en een wereldbeeld zijn in de fiche twee namen voor hetzelfde.",
        antwoord=False,
        uitleg="Het mensbeeld gaat over de mens, het wereldbeeld over de wereld als geheel. Ze hangen samen maar zijn niet gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lagen zijn volgens de fiche het meest bepalend voor iemands identiteit?",
        opties=[
            "dat verschilt van persoon tot persoon en vraagt reflectie",
            "altijd de biologische aspecten, want die liggen vast",
            "altijd de groepsidentiteit, want de groep is sterker",
            "altijd de familiale achtergrond, want die komt eerst",
        ],
        antwoord=0,
        uitleg="De fiche vraagt te reflecteren over welke lagen het meest bepalend zijn, en geeft dus geen vast antwoord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Sam verhuist naar een andere stad, vindt daar nieuwe vrienden en gaat zich anders kleden. Wat laat dat zien?",
        opties=[
            "het dynamische karakter van identiteit",
            "het relationele karakter van een subcultuur",
            "de voorrang van biologische aspecten",
            "het verdwijnen van de persoonlijke identiteit",
        ],
        antwoord=0,
        uitleg="De identiteit verschuift mee met de nieuwe omgeving. Dat is wat dynamisch betekent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over discriminatie passen bij de fiche?",
        opties=[
            "ze behandelt mensen anders om een kenmerk van hun identiteit",
            "ze kan het wij-zij-denken versterken",
            "ze is een factor die de identiteit beïnvloedt",
            "ze komt enkel voor tussen mensen van verschillende nationaliteit",
        ],
        antwoord=[0, 1, 2],
        uitleg="De laatste is te eng: discriminatie kan ook om gender, geloof, lichaam of afkomst gaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij de lagen van de persoonlijke identiteit?",
        opties=[
            "biologische aspecten",
            "persoonlijkheidstrekken",
            "familiale achtergrond",
            "subculturen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Subculturen staan bij de groepsidentiteit, niet bij de persoonlijke identiteit.",
    ),
    dict(
        type="invultekst",
        vraag="Welke factor uit de fiche betekent dat je het gevoel hebt ergens bij te horen?",
        antwoord=["verbondenheid", "de verbondenheid"],
        uitleg="Verbondenheid staat naast discriminatie en wij-zij-denken in het rijtje van de drie factoren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het indelen van mensen in een eigen groep en een andere groep? Antwoord met één woord uit de fiche.",
        antwoord=["wij-zij-denken", "wij zij denken"],
        uitleg="De fiche schrijft het met streepjes: wij-zij-denken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt de fiche de manier waarop je naar de wereld als geheel kijkt?",
        antwoord=["wereldbeeld", "het wereldbeeld"],
        uitleg="Naast het mensbeeld, waarmee het in de fiche in één adem genoemd wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarover moet je volgens de fiche kunnen reflecteren bij dit blok?",
        opties=[
            "hoe persoonlijke identiteit en groepsidentiteit elkaar beïnvloeden",
            "hoe je een identiteitskaart aanvraagt bij de gemeente",
            "hoeveel subculturen er in België bestaan",
            "welke nationaliteit het meest voorkomt in je klas",
        ],
        antwoord=0,
        uitleg="Reflecteren over die wederzijdse invloed staat letterlijk bij de leerdoelen.",
    ),
]
