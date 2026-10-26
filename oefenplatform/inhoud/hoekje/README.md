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
| De ruimte | Sterren, planeten en afstanden · Zwaartekracht, licht en het heelal · Verder dan de planeten · Tijd, licht en reizen door de ruimte · Zonnestormen, kometen en verre manen | 100 |
| Coderen en computers | Hoe een computer denkt · Algoritmes, netwerken en geheimschrift · Poorten, netwerken en veiligheid · Beelden, netwerken en slimme machines · Geheimschrift, kleurcodes en slimme trucs | 100 |
| Geschiedenis van België | Van 1830 tot de Eerste Wereldoorlog · Van de Koningskwestie tot vandaag · Legendes, uitvinders en oude tijden · Van de Romeinen tot de jaren tachtig · Graven, geleerden en wereldtentoonstellingen | 100 |
| Paradoxen en weetjes | Paradoxen die je hoofd kraken · Wonderlijke weetjes · Getallen, natuur en toeval · Levende wonderen en hardnekkige mythes · Raadsels, raven en rare proefjes | 100 |

Het derde, vierde en vijfde hoofdstuk van elk vak komen grotendeels van Kim
zelf (26 september, 8 oktober en 26 oktober 2026, de laatste uit haar
Gemini-reeksen). Wat inhoudelijk al in een vorig deel stond, is telkens
vervangen door iets nieuws over hetzelfde thema, zodat er niets dubbel staat.
Kijk bij het aanvullen dus altijd naar het onderwerp, niet naar de letterlijke
vraagtekst.

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
voortgang verloren. En omdat elk bestand alleen de hoofdstukken van zijn eigen vak
aanraakt, is een tweede import met dat vinkje aan onschadelijk.

## De vragen aanpassen

De bron staat in `bron/<vak>_<deel>.py`. Bouwen doe je met:

    python3 inhoud/hoekje/bron/bouw_hoekje.py

Het script weigert te schrijven bij een vraag zonder uitleg, een antwoord dat
buiten de opties valt, twee keer dezelfde vraag, of een patroon waarmee je zou
kunnen gokken: het juiste antwoord dat te vaak de langste optie is, of
waar-of-niet-vragen die te vaak op waar staan. Zie `inhoud/controleer_patronen.py`
voor die twee grenzen.
