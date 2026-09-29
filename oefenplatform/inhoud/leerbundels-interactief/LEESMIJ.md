# De interactieve leerbundel

Hier staan de leerbundels van 🌱 Start nog eens, maar als gegevens in plaats van
als pdf. Het oefenplatform maakt daar een eigen bladzijde mee: **de tocht door
het hoofdstuk**, met de haltes één voor één.

**Dit is een apart ding, het vervangt niets.** Kim op 29 september 2026: *"ik
wil niets veranderen aan wat er al was maar echt een extra knop per hoofdstuk
met aparte interactieve lesbundels"* en *"dit gaat echt een heel apart nieuw
ding zijn. wel met de leerstof van de lesbundels maar dan leuker gegeven voor
hun."* Het hoofdstuk zelf, de tabbladen en de pdf's om af te drukken zijn dus
niet aangeraakt. Er staat enkel een knop bij, boven de tabbladen, naar
`/vakken/<vak>/<nummer>/leerbundel`.

**Er zit geen slot op.** De oefeningen staan gewoon open, of het kind de tocht
nu doet of niet.

**Niet met de hand aanpassen.** De bron blijft
`inhoud/leerbundels/bron/maak_*.py`, dezelfde bestanden waar de pdf uit komt.
Verander je daar iets, draai dan:

    python3 inhoud/leerbundels/bron/maak_interactief.py

Zo kan de tekst op het scherm nooit achterlopen op de pdf.

## Hoe een hoofdstuk zijn bundel vindt

Aan de titel. Het hoofdstuk "Getallenkennis" in het vak wiskunde zoekt de
sleutel `wiskunde/getallenkennis`. Er is dus geen kolom in de databank en geen
SQL voor nodig.

Een pittig hoofdstuk deelt de bundel van het gewone hoofdstuk: " — pittig" wordt
van de titel afgehaald voor er gezocht wordt. Dezelfde leerstof, moeilijkere
vragen.

Heet de bundel net anders dan het hoofdstuk, zet dan de naam van het hoofdstuk
in de bundel zelf, bij `hoofdstukken=[...]`. Dat staat nu bij twee bundels:
"België: landschap en streken" (het hoofdstuk heet gewoon "België") en
"Spelling" (het hoofdstuk draagt nog zijn naam van bij het opzetten).

## Wat er géén bundel heeft

De zes uitdagingshoofdstukken, want die halen alle hoofdstukken door elkaar, en
de twee hoofdstukken begrijpend lezen, want daar staat de leestekst al boven de
vragen. Bij die hoofdstukken verschijnt de knop gewoon niet.

## Hoe de tocht werkt

Zie `components/InteractieveLeerbundel.tsx`.

- Elke sectie van de bundel is een **halte**. Er staat er één tegelijk op het
  scherm, met bovenaan een rij bolletjes om te zien waar je zit en om vrij heen
  en weer te springen.
- "Gehad, volgende halte" zet een **stempel** op die halte. De stempels blijven
  in de browser van het kind staan (`connectopia-tocht-<hoofdstuk>`), dus je
  kunt de tocht over meerdere keren doen.
- Op de **eindhalte** staat "onthoud dit" als afvinklijst
  (`connectopia-onthoud-<hoofdstuk>`), daarna een spelletje en een knop naar de
  oefeningen.
- Het spelletje is bij voorkeur de **schuifpuzzel**
  (`components/Schuifpuzzel.tsx`): een tekening uit dít hoofdstuk, in stukken,
  met één leeg vakje. Welke tekening dat wordt en in hoeveel stukken, kiezen
  `puzzelBeeld` en `puzzelRooster` in `lib/leerbundel.ts`: de tekening die het
  dichtst bij een gewone liggende verhouding komt, in 8 tot 9 stukken. Heel
  brede stroken vallen af, want daar staat op een stukje niets herkenbaars.
- Zeven bundels hebben zo'n tekening niet. Daar blijft het **volgordespel**
  (`components/Volgordespel.tsx`) staan: de haltes weer op een rij zetten.
- Een weetje wordt een geel kaartje, een figuur staat groot met zijn
  onderschrift eronder.
