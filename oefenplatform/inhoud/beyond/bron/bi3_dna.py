# -*- coding: utf-8 -*-
"""DNA, RNA en de replicatie — 🌍 Beyond, biologie.

Deel 1 gaat over de bouwstenen: de nucleotide, de dubbele helix, het verschil
tussen DNA en RNA, en de weg van DNA over chromatine naar een chromosoom, met
het karyogram erbij. Deel 2 gaat over de replicatie en over wat elk enzym daarin
doet.

De fiche somt de enzymen van de replicatie één voor één op (topoisomerase,
helicase, primase, polymerase, ligase, ssbp) en vraagt uitdrukkelijk hun
functie. Daarom krijgt elk van die zes in deel 2 een eigen vraag, en niet één
vraag die ze samen opsomt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Uit welke drie delen bestaat een nucleotide?",
        opties=[
            "een suiker, een fosfaatgroep en een stikstofbase",
            "een suiker, een vetzuur en een aminozuur",
            "een fosfaatgroep, een aminozuur en een base",
            "twee suikers en een stikstofbase",
        ],
        antwoord=0,
        uitleg="Een nucleotide is een suiker met een fosfaatgroep en een stikstofbase. "
        "Zonder de fosfaatgroep heet het geheel een nucleoside.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een suiker met een stikstofbase, maar zonder fosfaatgroep?",
        antwoord=["nucleoside", "een nucleoside"],
        uitleg="Komt er een fosfaatgroep bij het nucleoside, dan is het een nucleotide. "
        "Nucleotiden aan elkaar vormen een nucleïnezuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stikstofbasen staan in DNA tegenover elkaar?",
        opties=[
            "A tegenover T en C tegenover G",
            "A tegenover C en T tegenover G",
            "A tegenover G en C tegenover T",
            "A tegenover U en C tegenover G",
        ],
        antwoord=0,
        uitleg="Adenine past bij thymine, cytosine bij guanine. Die vaste koppels heten "
        "de complementariteit en houden de helix bij elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat houdt de twee strengen van de dubbele helix samen?",
        opties=[
            "waterstofbruggen tussen de basen",
            "peptidebindingen tussen de basen",
            "fosfaatbruggen tussen de suikers",
            "waterstofbruggen tussen de fosfaatgroepen",
        ],
        antwoord=0,
        uitleg="Tussen A en T liggen twee waterstofbruggen, tussen C en G drie. Elk brugje "
        "is zwak, maar samen houden ze de helix stevig dicht.",
    ),
    dict(
        type="waarofniet",
        vraag="De twee strengen van een DNA-molecule lopen in tegengestelde richting.",
        antwoord=True,
        uitleg="Dat heet de antiparallelle oriëntatie: waar de ene streng van 5' naar 3' "
        "loopt, loopt de andere van 3' naar 5'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verschillen zijn er tussen DNA en RNA? Kruis alles aan wat juist is.",
        opties=[
            "RNA heeft ribose, DNA desoxyribose",
            "RNA heeft uracil waar DNA thymine heeft",
            "RNA bestaat altijd uit twee strengen",
            "RNA bevat geen fosfaatgroepen",
        ],
        antwoord=[0, 1],
        uitleg="Ribose heeft één OH-groep meer dan desoxyribose, en uracil neemt de plaats "
        "in van thymine. RNA is bovendien meestal enkelstrengig.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stikstofbase staat in RNA op de plaats van thymine?",
        antwoord=["uracil", "U", "uraciel"],
        uitleg="Uracil past net als thymine bij adenine. Daarom kan RNA gewoon van een "
        "DNA-streng gekopieerd worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke streng van een gen wordt bij het kopiëren als voorbeeld gelezen?",
        opties=[
            "de antisense-streng of matrijs",
            "de sense-streng of coderende streng",
            "altijd beide strengen samen",
            "geen van de twee strengen",
        ],
        antwoord=0,
        uitleg="De antisense-streng dient als template of matrijs. Het RNA dat daarvan "
        "gemaakt wordt, is identiek aan de sense-streng, met U in plaats van T.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de streng die als voorbeeld gelezen wordt, met een woord dat een gietvorm betekent?",
        antwoord=["matrijs", "template", "de matrijs"],
        uitleg="De matrijs of template is de streng waarlangs de nieuwe streng gebouwd "
        "wordt. Daardoor wordt de informatie altijd exact doorgegeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een nucleosoom?",
        opties=[
            "DNA dat rond acht histonen gewonden is",
            "een chromosoom met twee chromatiden",
            "de kern van een eukaryote cel",
            "een stuk RNA rond een ribosoom",
        ],
        antwoord=0,
        uitleg="Acht histonen vormen een octameer, en het DNA wikkelt er bijna twee keer "
        "rond. Die kralenketting rolt daarna op tot een chromatinevezel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor histonen? Kruis alles aan wat juist is.",
        opties=[
            "ze zijn positief geladen eiwitten",
            "het DNA windt zich rond een groepje van acht",
            "ze knippen het DNA in losse stukken",
            "ze komen alleen bij prokaryoten voor",
        ],
        antwoord=[0, 1],
        uitleg="Histonen zijn kleine, positief geladen eiwitten, en het negatief geladen "
        "DNA hecht daar vlot aan. Acht van die eiwitten vormen de octameer van een "
        "nucleosoom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen eu- en heterochromatine?",
        opties=[
            "euchromatine is losser en wordt gelezen",
            "euchromatine zit altijd in het cytoplasma",
            "heterochromatine bevat geen DNA",
            "heterochromatine zit alleen in prokaryoten",
        ],
        antwoord=0,
        uitleg="Euchromatine ligt los, zodat de enzymen erbij kunnen. Heterochromatine is "
        "sterk gecondenseerd en wordt niet of weinig tot expressie gebracht.",
    ),
    dict(
        type="waarofniet",
        vraag="Een chromosoom is het best zichtbaar wanneer het chromatine helemaal losgerold is.",
        antwoord=False,
        uitleg="Net omgekeerd: pas als het chromatine sterk condenseert, wordt een "
        "chromosoom onder de microscoop zichtbaar. Dat gebeurt bij een celdeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zit er op de plaats van het centromeer?",
        opties=[
            "het kinetochoor waar de trekdraden aangrijpen",
            "de kernporiën van het kernmembraan",
            "het beginpunt van de transcriptie",
            "de plaats waar het DNA vrij ligt",
        ],
        antwoord=0,
        uitleg="Het centromeer is de insnoering waar de twee zusterchromatiden samenhangen. "
        "Op het kinetochoor hechten de microtubuli van de spoelfiguur.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een geordende foto van alle chromosomen van een cel?",
        antwoord=["karyogram", "een karyogram", "karyotype"],
        uitleg="Op een karyogram staan de chromosomen per paar en op grootte geordend. "
        "Daarmee worden afwijkingen in aantal of bouw opgespoord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een autosoom en een heterosoom?",
        opties=[
            "een heterosoom bepaalt het geslacht",
            "een autosoom zit alleen in gameten",
            "een heterosoom bevat geen genen",
            "een autosoom komt maar één keer voor",
        ],
        antwoord=0,
        uitleg="De mens heeft 22 paar autosomen en één paar heterosomen of "
        "geslachtschromosomen. Dat zijn XX bij een vrouw en XY bij een man.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor homologe chromosomen? Kruis alles aan wat juist is.",
        opties=[
            "ze dragen dezelfde genen op dezelfde plaats",
            "de ene komt van de moeder, de andere van de vader",
            "ze hebben altijd exact dezelfde allelen",
            "ze zitten enkel in haploïde cellen",
        ],
        antwoord=[0, 1],
        uitleg="Homologe chromosomen hebben dezelfde genloci, maar niet noodzakelijk "
        "dezelfde allelen. Een haploïde cel heeft juist geen paren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een menselijke eicel is diploïd en heeft 46 chromosomen.",
        antwoord=False,
        uitleg="Een eicel is een gameet en dus haploïd: 23 chromosomen. Een lichaamscel is "
        "diploïd en heeft er 46, 23 paren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat noemt men de plaats van een gen op een chromosoom?",
        opties=[
            "de locus",
            "het centromeer",
            "het kinetochoor",
            "de matrijs",
        ],
        antwoord=0,
        uitleg="Elk gen heeft een vaste locus op zijn chromosoom. Daardoor liggen dezelfde "
        "genen op twee homologe chromosomen op dezelfde plaats.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee zusterchromatiden van één chromosoom dragen na de replicatie dezelfde informatie.",
        antwoord=True,
        uitleg="Ze zijn kopieën van elkaar, gemaakt tijdens de S-fase. Bij de mitose wordt "
        "er één naar elke dochtercel getrokken.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer in de celcyclus gebeurt de DNA-replicatie?",
        opties=[
            "in de S-fase van de interfase",
            "in de metafase van de mitose",
            "in de G0-fase",
            "tijdens de cytokinese",
        ],
        antwoord=0,
        uitleg="S staat voor synthese. Na de S-fase heeft elk chromosoom twee "
        "zusterchromatiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet helicase bij de replicatie?",
        opties=[
            "de waterstofbruggen verbreken en de strengen scheiden",
            "de nieuwe nucleotiden aan elkaar hangen",
            "de losse stukjes aan elkaar plakken",
            "een kort stukje RNA als beginpunt leggen",
        ],
        antwoord=0,
        uitleg="Helicase opent de dubbele helix en maakt zo de replicatievork. De "
        "losgekomen strengen worden door ssbp's open gehouden.",
    ),
    dict(
        type="invultekst",
        vraag="Welk enzym haalt de spanning uit het DNA dat voor de replicatievork opgewonden raakt?",
        antwoord=["topoisomerase", "het topoisomerase"],
        uitleg="Omdat de helix opengetrokken wordt, draait het DNA ervoor te strak op. "
        "Topoisomerase knipt, laat draaien en hecht weer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient primase?",
        opties=[
            "een kort stukje RNA als beginpunt leggen",
            "de strengen van elkaar trekken",
            "de dochterstrengen aan elkaar hechten",
            "de fouten in het nieuwe DNA herstellen",
        ],
        antwoord=0,
        uitleg="DNA-polymerase kan niet uit het niets beginnen; het heeft een primer "
        "nodig. Primase legt die primer, een kort stukje RNA.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet DNA-polymerase?",
        opties=[
            "nucleotiden aanhangen van 5' naar 3'",
            "nucleotiden aanhangen van 3' naar 5'",
            "de waterstofbruggen van de helix verbreken",
            "de histonen rond het DNA plaatsen",
        ],
        antwoord=0,
        uitleg="Polymerase bouwt de nieuwe streng maar in één richting, van 5' naar 3'. "
        "Daardoor verloopt de replicatie op de twee strengen verschillend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt de lagging strand in stukjes gebouwd?",
        opties=[
            "omdat polymerase maar in één richting werkt",
            "omdat die streng korter is dan de andere",
            "omdat er op die streng geen primer past",
            "omdat helicase die streng dichtlaat",
        ],
        antwoord=0,
        uitleg="De lagging strand loopt tegen de beweging van de vork in. Daarom wordt hij "
        "telkens een stukje achteruit gebouwd: de Okazaki-fragmenten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de korte stukjes nieuw DNA op de lagging strand?",
        antwoord=["okazakifragmenten", "okazaki-fragmenten", "okazaki fragmenten"],
        uitleg="Die fragmenten worden daarna aan elkaar gehecht door ligase. Zo ontstaat "
        "ook daar één doorlopende streng.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk enzym plakt de losse stukjes van de lagging strand aan elkaar?",
        opties=[
            "ligase",
            "helicase",
            "primase",
            "topoisomerase",
        ],
        antwoord=0,
        uitleg="Ligase sluit het laatste gaatje tussen twee fragmenten. Zonder ligase "
        "blijft de nieuwe streng onderbroken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heten, met hun afkorting van vier letters, de eiwitten die de losgekomen strengen open houden?",
        antwoord=["ssbp", "ssbp's", "ssbp s"],
        uitleg="Single strand binding proteins hechten op de losgekomen strengen. Zo "
        "kunnen die niet opnieuw tegen elkaar klappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een replicatievork?",
        opties=[
            "de plaats waar de twee strengen uiteenwijken",
            "de plaats waar twee chromatiden samenkomen",
            "het punt waar de transcriptie start",
            "de holte waarin het nieuwe DNA opgeslagen wordt",
        ],
        antwoord=0,
        uitleg="Aan de vork splijt de helix open en wordt er aan twee nieuwe strengen "
        "gebouwd. In één replicatielus werken er twee vorken, elk in hun richting.",
    ),
    dict(
        type="waarofniet",
        vraag="Na de replicatie bestaat elke nieuwe DNA-molecule uit één oude en één nieuwe streng.",
        antwoord=True,
        uitleg="Elke ouderlijke streng dient als matrijs voor een dochterstreng. Daarom "
        "heet de replicatie semiconservatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het resultaat van één replicatie?",
        opties=[
            "twee identieke DNA-moleculen",
            "twee verschillende DNA-moleculen",
            "één molecule met vier strengen",
            "vier haploïde cellen",
        ],
        antwoord=0,
        uitleg="Omdat de basenparen vastliggen, zijn de twee kopieën identiek aan het "
        "origineel. Alleen een fout die niet hersteld wordt, geeft verschil.",
    ),
    dict(
        type="waarofniet",
        vraag="De replicatie van het menselijke DNA start op één enkele plaats per chromosoom.",
        antwoord=False,
        uitleg="Er zijn honderden startpunten per chromosoom. Anders zou het kopiëren van "
        "een chromosoom dagen duren in plaats van uren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de replicatie zo nauwkeurig? Kruis alles aan wat juist is.",
        opties=[
            "de basenparen passen maar op één manier",
            "polymerase kijkt zijn eigen werk na",
            "er wordt maar één streng gekopieerd",
            "de histonen controleren elke base",
        ],
        antwoord=[0, 1],
        uitleg="De complementariteit laat weinig keuze, en polymerase haalt een verkeerd "
        "geplaatste nucleotide er meestal weer uit. Toch blijft er af en toe een fout "
        "staan, en dat is een mutatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor de leading strand? Kruis alles aan wat juist is.",
        opties=[
            "hij wordt in één stuk doorgebouwd",
            "hij loopt mee met de replicatievork",
            "hij wordt in losse Okazaki-fragmenten gebouwd",
            "hij heeft geen enkele primer nodig",
        ],
        antwoord=[0, 1],
        uitleg="De leading strand loopt mee met de vork, dus kan polymerase blijven "
        "doorbouwen. Eén primer vooraan volstaat, maar helemaal zonder primer gaat het "
        "niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de oorspronkelijke streng die als voorbeeld dient bij de replicatie?",
        antwoord=[
            "ouderlijke streng",
            "de ouderlijke streng",
            "moederstreng",
        ],
        uitleg="Tegenover de ouderlijke streng staat de dochterstreng, die nieuw gebouwd "
        "wordt. In elke kopie zit er één van elk.",
    ),
    dict(
        type="waarofniet",
        vraag="De RNA-primers worden na de replicatie door DNA vervangen.",
        antwoord=True,
        uitleg="De primers worden weggehaald en het gat wordt met DNA-nucleotiden "
        "opgevuld. Daarna sluit ligase de streng.",
    ),
    dict(
        type="waarofniet",
        vraag="Een prokaryote cel repliceert haar DNA in de kern.",
        antwoord=False,
        uitleg="Een prokaryoot heeft geen kern. Haar ringvormige DNA ligt vrij in het "
        "cytoplasma en wordt daar gekopieerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom moet het DNA gekopieerd worden voor een cel deelt?",
        opties=[
            "elke dochtercel heeft een volledige set nodig",
            "het DNA wordt bij het delen afgebroken",
            "anders kan de cel geen eiwitten maken",
            "anders blijven de chromosomen onzichtbaar",
        ],
        antwoord=0,
        uitleg="Zonder replicatie zou elke dochtercel maar de helft van de informatie "
        "krijgen. Daarom komt de S-fase altijd voor de M-fase.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn nucleïnezuren? Kruis alles aan wat juist is.",
        opties=[
            "DNA",
            "RNA",
            "glucose",
            "hemoglobine",
        ],
        antwoord=[0, 1],
        uitleg="Een nucleïnezuur is een keten van nucleotiden, en dat zijn DNA en RNA. "
        "Glucose is een sacharide en hemoglobine een proteïne.",
    ),
]
