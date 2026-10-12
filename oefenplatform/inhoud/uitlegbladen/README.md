# Uitlegbladen (pdf) bij de oefenbundels

Een uitlegblad is **een apart blad naast een oefenbundel**, met bij elke
oefening het antwoord en waarom dat antwoord juist is. Het is bedoeld om samen
na te lezen nadat het kind de bundel gemaakt heeft, niet om er zelf in te
schrijven.

Febe, een tester die zich op de Examencommissie voorbereidt, schreef op
12 oktober 2026 dat ze bij de oefeningen graag zou weten waarom iets juist is.
Kim wou daarvoor geen enkele bestaande bundel opnieuw maken: "ik zou ook de
uitleg van de oefenbundel apart doen, die kan ik gewoon extra opladen". Vandaar
een los blad, met dezelfde nummers als de bundel.

## Hoe het blad eruitziet

Per reeks staat er bovenaan een **aanpak**: hoe je aan zo'n oefening begint, in
gewone taal, zonder vakjargon. Daaronder staat elke oefening met haar nummer,
een echo van de vraag, het antwoord, en waar dat nodig is een **waarom**.

Bij veel oefeningen zegt het antwoord zelf al genoeg ("16, want een derde van
24 is 8"). Daar staat bewust niets bij. Een uitleg die niets toevoegt, maakt
het blad enkel langer en de rest minder zichtbaar.

De nummers komen **uit de oefenbundel zelf**, niet uit een tweede lijst. Anders
verschuift het blad zodra er een oefening bijkomt en wijst een kind in zijn
bundel naar nummer 14 terwijl het blad er 13 bedoelt. Klopt het aantal niet,
dan stopt `uitlegblad.py` met een melding in plaats van een blad te schrijven
dat ernaast zit.

## Wat er klaar is

**Wiskunde 🌱 Start: 7 bladen, bij alle zeven de oefenbundels van dat vak.**

| vak | categorie | bladen |
| --- | --- | --- |
| Wiskunde | 🌱 Start | 7 |

De andere vakken volgen. Er staat per vak en per categorie een zip
(`wiskunde-start.zip`) en één met alles erin (`alle-uitlegbladen.zip`), net als
bij de leerbundels en de oefenbundels.

## Een uitlegblad maken

De beschrijving staat náást de oefenbundel, in hetzelfde
`../leerbundels/bron/maak_oefeningen_*.py`, in een dict `UITLEGBLADEN`:

```python
UITLEGBLADEN["oefenbundel-rekenen-en-breuken"] = dict(
    reeksen=[
        dict(aanpak="Hoe je aan deze reeks begint.",
             waarom=[None, "Waarom bij oefening 2.", ...]),
        ...
    ],
)
```

Eén `dict` per reeks, in dezelfde volgorde als de oefenbundel, en de lijst
`waarom` is precies even lang als het aantal genummerde oefeningen in die
reeks. `None` laat een oefening over zonder uitleg.

Bouwen, vanuit `../leerbundels/bron`:

```
python3 maak_oefeningen_wiskunde.py     # schrijft de html
python3 maak_alles.py wiskunde          # html, pdf, en op zijn plaats zetten
```

## Hoe een blad bij een hoofdstuk raakt

Net als een oefenbundel: op `/beheer/leerstof` kies je het vak en sleep je de
pdf erin. De bestandsnaam begint met `uitlegblad-` en daarna de naam van het
hoofdstuk, zodat het platform zelf het juiste hoofdstuk vindt. Het komt naast
de oefenbundel te staan en wist die niet, want de titel verschilt.
