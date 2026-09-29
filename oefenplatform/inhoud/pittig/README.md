# Pittig: bij elk hoofdstuk een moeilijker broertje

Naast "Getallenkennis" staat "Getallenkennis — pittig": dezelfde leerstof,
twintig moeilijkere vragen. Bedoeld voor de kinderen die de gewone reeks vlot
afwerken en daarna niets meer te doen hebben.

Dit kwam er op 28 september 2026 na een melding van een kind uit de testgroep
dat een leerjaar gesprongen was:

> ik zit in het 5de leerjaar én ik heb een leerjaar gesprongen. En nog vind ik
> deze oefeningen te makkelijk. Er zitten oefeningen in die al een keer eerder
> in rekenen zijn voorgekomen. En als een beetje goed geheugen hebt onthoud je
> de antwoorden.

Klaar: **heel 🌱 Start**, alle zes de vakken, 31 hoofdstukken en 620 vragen.

| Vak | Hoofdstukken | Vragen |
|-----|--------------|--------|
| Wiskunde | 7 | 140 |
| Wetenschap en techniek | 7 | 140 |
| Engels | 6 | 120 |
| Nederlands | 5 | 100 |
| Geschiedenis | 3 | 60 |
| Aardrijkskunde | 3 | 60 |

Nederlands laat twee hoofdstukken bewust liggen: spelling, dat al een eigen
bestand heeft, en begrijpend lezen, waar een pittige versie eerst een eigen
leestekst nodig heeft.

## Wat maakt een vraag hier moeilijker?

Geen nieuwe leerstof, net zoals bij [de uitdagingshoofdstukken](../uitdaging/README.md).
Alles staat op wat in het gewone hoofdstuk al aan bod komt, zodat de leerbundel
blijft dekken. De verdieping zit in de vraag zelf:

- **twee stappen** in plaats van één (een trui van 40 euro, eerst 20 % af en
  daarna nog 5 euro met een bon);
- **omgekeerd denken** (je rondt af op 3 600 — wat is het grootste getal waarvan
  je kon vertrekken?);
- **een veelgemaakte fout** die juist lijkt (een fles met dop kost 11 euro en de
  fles kost 10 euro meer dan de dop, dus de dop kost geen 1 euro);
- **een besluit trekken** (het middelste getal is 7 en het gemiddelde 8: hoe kan
  dat?).

Het verschil met een uitdagingshoofdstuk: dat is er één per vak en haalt alle
hoofdstukken door elkaar. Een pittig hoofdstuk blijft bij zijn eigen onderwerp,
zodat een kind gericht verder kan met waar het net mee bezig was.

## Geen enkele vraag mag al bestaan

De tweede helft van de melding ging over herhaling. `bron/bouw_pittig.py` legt
daarom elke nieuwe vraag naast álle vragen die al ergens in `inhoud/` staan, en
weigert te schrijven bij een herhaling binnen hetzelfde niveau. Datzelfde script
bewaakt ook de gokpatronen (het juiste antwoord dat de langste optie is, en de
verhouding waar tegenover niet waar) en rekent elk `reken`-veld na.

Bouwen:

    python3 inhoud/pittig/bron/bouw_pittig.py                 # alles
    python3 inhoud/pittig/bron/bouw_pittig.py start_wiskunde  # één vak

## Waar het kind ze ziet

`components/HoofdstukTegels.tsx` herkent een titel die op "— pittig" eindigt,
zet dat vakje meteen achter zijn gewone hoofdstuk en geeft het een oranje randje
met het label **Moeilijker**. Geen kolom in de databank, dus **geen SQL**.

## Importeren

| Bestand | Vak | Niveau | Vervangen |
|---------|-----|--------|-----------|
| `start-wiskunde-pittig.json` | Wiskunde | 🌱 Start | **aan** |
| `start-nederlands-pittig.json` | Nederlands | 🌱 Start | **aan** |
| `start-geschiedenis-pittig.json` | Geschiedenis | 🌱 Start | **aan** |
| `start-aardrijkskunde-pittig.json` | Aardrijkskunde | 🌱 Start | **aan** |
| `start-engels-pittig.json` | Engels | 🌱 Start | **aan** |
| `start-wetenschap-en-techniek-pittig.json` | Wetenschap en techniek | 🌱 Start | **aan** |

Telkens via **Beheer → Vakken → het vak → vragen importeren**, met het vinkje
**"Bestaande vragen vervangen" aan**. Een bestand raakt alleen zijn eigen nieuwe
hoofdstukken aan; de gewone hoofdstukken en de voortgang erop blijven zoals ze
zijn. Importeer je per ongeluk een tweede keer, dan staan er nog altijd twintig
vragen per hoofdstuk in plaats van veertig.
