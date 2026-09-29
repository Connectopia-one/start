# -*- coding: utf-8 -*-
"""Beschrijven wat je ziet, in het Frans — twee prenten van Kim.

Kim op 29 september 2026: "op het examencommissie moeten ze ook beelden
beschrijven in de taalvakken, hier krijg je dan een foto of prent en moet je
beschrijven wat je ziet ... zoals de teksten begrijpend lezen zijn maar dan met
een prent."

Een geschreven beschrijving kan het platform niet nakijken, maar de
woordenschat eronder wel: il y a, links en rechts, kleuren, aantallen, en wie
wat aan het doen is. Kim vroeg uitdrukkelijk om de antwoorden hard op elkaar te
laten lijken, zodat een kind écht moet kijken.

DE PRENT IS DE BRON. Elke vraag hieronder is nageteld op de prent zelf, met de
prent stuk voor stuk uitvergroot. Maakt iemand later een nieuwe prent, dan
kloppen deze vragen niet meer: dan moeten ze opnieuw geschreven worden.

Wat er op "Wat zie je op de prent?" staat (nageteld op 29-09-2026):
een jongen op een blauwe fiets, blauwe helm, rode jas, spijkerbroek, rugzak;
één bruin-witte koe achter een houten hek; een eekhoorn in de boom linksboven;
drie vogels in de lucht; een mees op een paaltje linksonder; besneeuwde bergen;
de zon rechtsboven; een dorp met een kerk; een stenen huis rechts op de heuvel;
een stenen brug met één boog; een rivier; een waterval; één eend met een groene
kop; een konijn dat rechtsonder wegloopt; een oranje vlinder; een slak op een
steen; een lieveheersbeestje; madeliefjes en paardenbloemen. Géén hond.

Wat er op "Wat zie je aan zee?" staat (nageteld op 29-09-2026):
drie kinderen — een jongen in een rode trui die een hond aait, een jongen met
een blauwe pet die vist op de steiger, een meisje met een strohoed dat schelpen
raapt; een golden retriever met een blauwe halsband; een groene tent, een
rugzak, een picknickmand, een rode appel, een blauwe drinkfles, een groen
doosje, een rood-wit geruit kleed; een boomhut met een rode kat; een mees op
een tak; een schommel van een autoband; een wit huis met een rood dak en blauwe
luiken; een vuurtoren rechts op de rotsen; meeuwen; een houten steiger; een
witte roeiboot; een zeilboot; de ondergaande zon; een rode emmer; een
zandkasteel met een rood vlaggetje; een zeester; schelpen; een groene hagedis;
een lieveheersbeestje; een oranje vlinder; drie eenden in het water.
"""

# --------------------------------------------------------------- prent 1
BERG = [
    dict(type="meerkeuze",
         vraag="Wat doet de jongen op de prent?",
         opties=["Il fait du vélo",
                 "Il joue au football",
                 "Il marche à l'école",
                 "Il nage dans la rivière"],
         antwoord=0,
         uitleg="Il fait du vélo: hij fietst. Faire du vélo is fietsen, net zoals faire du sport sporten is."),
    dict(type="meerkeuze",
         vraag="Welke kleur heeft de fiets van de jongen?",
         opties=["bleu", "rouge", "vert", "gris"],
         antwoord=0,
         uitleg="Le vélo est bleu. Rouge is rood, vert is groen en gris is grijs."),
    dict(type="meerkeuze",
         vraag="Je wil vertellen wat er op een prent staat. Met welke woorden begin je?",
         opties=["Sur l'image, il y a",
                 "Sur l'image, je suis",
                 "Sur l'image, il est",
                 "Sur l'image, j'ai"],
         antwoord=0,
         uitleg="Sur l'image, il y a ... betekent op de prent is er of zijn er ... Daarmee begin je bijna elke beschrijving."),
    dict(type="invultekst",
         vraag="Hoe zeg je in het Frans \"er is\" of \"er zijn\"? (drie woordjes)",
         antwoord="il y a",
         uitleg="Il y a verandert nooit: il y a un lapin (er is een konijn), il y a trois oiseaux (er zijn drie vogels)."),
    dict(type="meerkeuze",
         vraag="De eekhoorn zit in de boom. Waar staat die boom op de prent?",
         opties=["à gauche", "à droite", "au milieu", "en bas"],
         antwoord=0,
         uitleg="De boom met de eekhoorn staat links: à gauche. À droite is rechts, au milieu is in het midden en en bas is onderaan."),
    dict(type="meerkeuze",
         vraag="De jongen rijdt niet links en niet rechts van de prent. Welk Frans woordje past bij waar hij rijdt?",
         opties=["au milieu", "à gauche", "à droite", "en haut"],
         antwoord=0,
         uitleg="Au milieu is in het midden. En haut is bovenaan, en dat gebruik je voor de zon en de bergen."),
    dict(type="waarofniet",
         vraag="\"Sur l'image, il y a une vache.\"",
         antwoord=True,
         uitleg="Klopt. Une vache is een koe, en die staat links in de wei achter het hek."),
    dict(type="meerkeuze",
         vraag="Hoeveel koeien staan er op de prent?",
         opties=["une", "deux", "trois", "quatre"],
         antwoord=0,
         uitleg="Er staat er maar één: une vache. Une is een bij een vrouwelijk woord, un bij een mannelijk."),
    dict(type="meerkeuze",
         vraag="Welke kleuren heeft de koe?",
         opties=["brun et blanc", "noir et blanc", "tout brun", "tout blanc"],
         antwoord=0,
         uitleg="De koe is bruin met wit: brun et blanc. Een zwart-witte koe zou noir et blanc zijn."),
    dict(type="invultekst",
         vraag="Hoeveel vogels vliegen er in de lucht? Schrijf het getal in het Frans.",
         antwoord="trois",
         uitleg="Er vliegen er drie: trois oiseaux. Tel mee: un, deux, trois."),
    dict(type="waarofniet",
         vraag="\"Il y a un chien sur l'image.\"",
         antwoord=False,
         uitleg="Niet waar. Un chien is een hond, en die staat er niet op. Wel een koe, een eekhoorn, een konijn en een eend."),
    dict(type="meerkeuze",
         vraag="Wat is \"un lapin\"?",
         opties=["een konijn", "een eekhoorn", "een eend", "een vogel"],
         antwoord=0,
         uitleg="Un lapin is een konijn. Een eekhoorn is un écureuil, een eend un canard en een vogel un oiseau."),
    dict(type="meerkeuze",
         vraag="Wat gebeurt er rechtsonder op de prent?",
         opties=["un lapin qui court",
                 "un chat qui dort",
                 "un chien qui joue",
                 "un cheval qui mange"],
         antwoord=0,
         uitleg="Un lapin qui court: een konijn dat loopt. Courir is lopen."),
    dict(type="meerkeuze",
         vraag="Er zwemt een dier in de rivier. Welk?",
         opties=["un canard", "un poisson", "une grenouille", "une tortue"],
         antwoord=0,
         uitleg="Un canard is een eend, en die zwemt rechts in het water. Un poisson is een vis, une grenouille een kikker en une tortue een schildpad."),
    dict(type="waarofniet",
         vraag="\"Le soleil est en haut à droite.\"",
         antwoord=True,
         uitleg="Klopt. De zon staat rechtsboven: en haut à droite."),
    dict(type="invultekst",
         vraag="Hoe zeg je \"de zon\" in het Frans? (twee woordjes)",
         antwoord="le soleil",
         uitleg="Le soleil is de zon. Il fait du soleil betekent het is zonnig."),
    dict(type="meerkeuze",
         vraag="Wat betekent \"un pont\"?",
         opties=["een brug", "een berg", "een pad", "een poort"],
         antwoord=0,
         uitleg="Un pont is een brug, en die van steen ligt rechts over de rivier. Een berg is une montagne."),
    dict(type="waarofniet",
         vraag="\"Il n'y a pas de montagnes sur l'image.\"",
         antwoord=False,
         uitleg="Niet waar: er staan wél bergen op, met sneeuw erop. Il n'y a pas de ... betekent er is of er zijn geen ..."),
    dict(type="meerkeuze",
         vraag="Welke kleur heeft de jas van de jongen?",
         opties=["rouge", "bleu", "vert", "jaune"],
         antwoord=0,
         uitleg="Sa veste est rouge: zijn jas is rood. Zijn helm en zijn fiets zijn wel blauw."),
    dict(type="waarofniet",
         vraag="\"Le garçon porte un casque.\"",
         antwoord=True,
         uitleg="Klopt. Un casque is een helm, en die heeft hij op. Porter betekent dragen."),
]

# --------------------------------------------------------------- prent 2
ZEE = [
    dict(type="meerkeuze",
         vraag="Waar speelt deze prent zich af?",
         opties=["à la mer", "dans la ville", "dans la forêt", "à la montagne"],
         antwoord=0,
         uitleg="À la mer: aan zee. Je ziet het water, de boten, het zand en de schelpen."),
    dict(type="meerkeuze",
         vraag="Hoeveel kinderen zie je op de prent?",
         opties=["trois", "un", "deux", "quatre"],
         antwoord=0,
         uitleg="Drie: de jongen bij de hond, de jongen die vist en het meisje op het strand."),
    dict(type="waarofniet",
         vraag="\"Il y a un chat dans la cabane.\"",
         antwoord=True,
         uitleg="Klopt. Un chat is een kat, en die kijkt uit de boomhut. Une cabane is een hut."),
    dict(type="meerkeuze",
         vraag="Welke kleur heeft de tent?",
         opties=["verte", "rouge", "bleue", "jaune"],
         antwoord=0,
         uitleg="La tente est verte: de tent is groen. Tente is vrouwelijk, dus vert krijgt er een e bij."),
    dict(type="invultekst",
         vraag="Hoe zeg je \"de zee\" in het Frans? (twee woordjes)",
         antwoord="la mer",
         uitleg="La mer is de zee. Aan zee zeg je à la mer."),
    dict(type="meerkeuze",
         vraag="Wat doet de jongen met de blauwe pet?",
         opties=["Il pêche", "Il nage", "Il dort", "Il chante"],
         antwoord=0,
         uitleg="Il pêche: hij vist. Nager is zwemmen, dormir is slapen en chanter is zingen."),
    dict(type="meerkeuze",
         vraag="Wat is \"un bateau\"?",
         opties=["een boot", "een bad", "een bal", "een bed"],
         antwoord=0,
         uitleg="Un bateau is een boot. Er liggen er twee: een roeiboot bij de steiger en een zeilboot verderop."),
    dict(type="meerkeuze",
         vraag="Wat draagt het meisje op haar hoofd?",
         opties=["un chapeau", "un casque", "un manteau", "un parapluie"],
         antwoord=0,
         uitleg="Un chapeau is een hoed, de hare is van stro. Un casque is een helm en un manteau een jas."),
    dict(type="waarofniet",
         vraag="\"Le garçon caresse un chat.\"",
         antwoord=False,
         uitleg="Niet waar: hij aait een hond, un chien. De kat zit in de boomhut. Caresser betekent aaien."),
    dict(type="invultekst",
         vraag="Welk Frans woord betekent het strand?",
         antwoord="plage",
         uitleg="La plage is het strand. Het meisje raapt er schelpen: des coquillages."),
    dict(type="meerkeuze",
         vraag="Welke kleur heeft de emmer van het meisje?",
         opties=["rouge", "bleu", "vert", "jaune"],
         antwoord=0,
         uitleg="Le seau est rouge: de emmer is rood, met een geel handvat."),
    dict(type="waarofniet",
         vraag="\"Le soleil se couche.\" (De zon gaat onder.)",
         antwoord=True,
         uitleg="Klopt. De zon hangt laag boven het water en de lucht is oranje: het is avond."),
    dict(type="meerkeuze",
         vraag="Wat betekent \"un château de sable\"?",
         opties=["een zandkasteel", "een zandbak", "een zandpad", "een zandstrand"],
         antwoord=0,
         uitleg="Un château is een kasteel en le sable is zand, dus samen een zandkasteel. Dat staat rechtsonder, met een rood vlaggetje."),
    dict(type="meerkeuze",
         vraag="Wat zwemt er in het water, vlak bij de kant?",
         opties=["des canards", "des poissons", "des tortues", "des grenouilles"],
         antwoord=0,
         uitleg="Des canards: eenden. Er zwemmen er drie, een grote en twee kleintjes."),
    dict(type="waarofniet",
         vraag="\"Il n'y a pas d'arbres sur l'image.\"",
         antwoord=False,
         uitleg="Niet waar: er staan wél bomen, en in een ervan hangt de boomhut. Un arbre is een boom."),
    dict(type="meerkeuze",
         vraag="Wat is \"une tente\"?",
         opties=["een tent", "een tafel", "een toren", "een trap"],
         antwoord=0,
         uitleg="Une tente is een tent. De groene tent staat links, naast de picknick."),
    dict(type="invultekst",
         vraag="Hoe zeg je \"de vuurtoren\" in het Frans? (twee woordjes)",
         antwoord="le phare",
         uitleg="Le phare is de vuurtoren. Die staat rechts op de rotsen, wit met een rode top."),
    dict(type="waarofniet",
         vraag="\"La fille porte une robe.\"",
         antwoord=True,
         uitleg="Klopt. Une robe is een jurk, en zij draagt er een met bloemetjes op."),
    dict(type="meerkeuze",
         vraag="Waar staat de vuurtoren op de prent?",
         opties=["à droite", "à gauche", "au milieu", "en bas"],
         antwoord=0,
         uitleg="À droite: rechts, boven op de rotsen. De tent staat à gauche."),
    dict(type="waarofniet",
         vraag="\"Le garçon sur le ponton porte un chapeau.\"",
         antwoord=False,
         uitleg="Niet waar: hij draagt een pet, une casquette. Un chapeau met een rand heeft alleen het meisje op het strand."),
]

HOOFDSTUKKEN = [
    ("Wat zie je op de prent?", BERG),
    ("Wat zie je aan zee?", ZEE),
]
