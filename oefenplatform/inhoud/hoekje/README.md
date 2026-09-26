# 🔭 De uitdagingshoek

Een hoekje dat **naast** de leerstof ligt in plaats van erin. Geen leerjaar,
geen vakfiche, geen examen: vragen die een kind meenemen naar de ruimte, naar
de binnenkant van een computer, door de geschiedenis van ons land en langs
paradoxen die je hoofd kraken.

Bedoeld voor de kinderen die de gewone hoofdstukken vlot afwerken en dan nog
honger hebben. Het is ook het enige deel van het oefenplatform dat helemaal
open staat, ook zonder account: wie via de website binnenwandelt, kan meteen
beginnen.

**Niet te verwarren** met het hoofdstuk *"Uitdaging — alles door elkaar"* dat
bij elk gewoon vak staat. Dat blijft binnen de leerstof van dat vak en hoort bij
de leerbundels. Dit hoekje doet juist het tegenovergestelde: het stapt eruit.

## Wat erin zit

| Vak | Hoofdstukken | Vragen |
|-----|--------------|--------|
| De ruimte | Sterren, planeten en afstanden · Zwaartekracht, licht en het heelal | 40 |
| Coderen en computers | Hoe een computer denkt · Algoritmes, netwerken en geheimschrift | 40 |
| Geschiedenis van België | Van 1830 tot de Groote Oorlog · Van de Koningskwestie tot vandaag | 40 |
| Paradoxen en weetjes | Paradoxen die je hoofd kraken · Wonderlijke weetjes | 40 |

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
