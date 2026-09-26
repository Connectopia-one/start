# 🔭 De uitdagingshoek

Een hoekje dat **naast** de leerstof ligt in plaats van erin. Geen leerjaar,
geen vakfiche, geen examen: vragen die een kind meenemen naar de ruimte, naar
de binnenkant van een computer, door de geschiedenis van ons land en langs
paradoxen die je hoofd kraken.

Bedoeld voor de kinderen die de gewone hoofdstukken vlot afwerken en dan nog
honger hebben. Het zit mee in de volledige toegang, als extraatje: een account
is dus nodig. Anders dan bij de leerjaren staat hier **geen** eerste hoofdstuk
gratis open — zie `heeftProefhoofdstuk()` in `lib/niveaus.ts`, want dit is geen
leerweg om eerst uit te proberen.

**Niet te verwarren** met het hoofdstuk *"Uitdaging — alles door elkaar"* dat
bij elk gewoon vak staat. Dat blijft binnen de leerstof van dat vak en hoort bij
de leerbundels. Dit hoekje doet juist het tegenovergestelde: het stapt eruit.

## Wat erin zit

| Vak | Hoofdstukken | Vragen |
|-----|--------------|--------|
| De ruimte | Sterren, planeten en afstanden · Zwaartekracht, licht en het heelal · Verder dan de planeten | 60 |
| Coderen en computers | Hoe een computer denkt · Algoritmes, netwerken en geheimschrift · Poorten, netwerken en veiligheid | 60 |
| Geschiedenis van België | Van 1830 tot de Eerste Wereldoorlog · Van de Koningskwestie tot vandaag · Legendes, uitvinders en oude tijden | 60 |
| Paradoxen en weetjes | Paradoxen die je hoofd kraken · Wonderlijke weetjes · Getallen, natuur en toeval | 60 |

Het derde hoofdstuk van elk vak komt grotendeels van Kim zelf (26 september
2026). Twaalf van haar veertig vragen stonden inhoudelijk al in deel 1 of 2 en
zijn vervangen door nieuwe over hetzelfde thema, zodat er niets dubbel staat.

Elk hoofdstuk telt twintig vragen. Er hoort **geen leerbundel** bij: de uitleg
onder elke vraag doet hier het werk, en die is daarom bewust langer dan
gewoonlijk. Wie het antwoord fout had, leert het in die paar zinnen alsnog.

## Wat je één keer moet doen

1. Draai `supabase/uitdagingshoek.sql` in de SQL-editor van het oefenplatform.
   Dat laat de nieuwe categorie toe én maakt de vier vakken aan.
2. Importeer de vier bestanden hieronder via **Beheer → Vakken → het vak →
   vragen importeren**, met het vinkje **"Bestaande vragen vervangen" aan**.

| Bestand | Vak |
|---------|-----|
| `de-ruimte.json` | De ruimte |
| `coderen-en-computers.json` | Coderen en computers |
| `geschiedenis-van-belgie.json` | Geschiedenis van België |
| `paradoxen-en-weetjes.json` | Paradoxen en weetjes |

Er staat nog niets in die vakken, dus er gaat bij deze import geen enkele
voortgang verloren. En omdat elk bestand alleen zijn eigen twee hoofdstukken
aanraakt, is een tweede import met dat vinkje aan onschadelijk.

## De vragen aanpassen

De bron staat in `bron/<vak>_<deel>.py`. Bouwen doe je met:

    python3 inhoud/hoekje/bron/bouw_hoekje.py

Het script weigert te schrijven bij een vraag zonder uitleg, een antwoord dat
buiten de opties valt, twee keer dezelfde vraag, of een patroon waarmee je zou
kunnen gokken: het juiste antwoord dat te vaak de langste optie is, of
waar-of-niet-vragen die te vaak op waar staan. Zie `inhoud/controleer_patronen.py`
voor die twee grenzen.
