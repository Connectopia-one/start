# Van woorden naar wiskundige notatie

Het gereedschap waarmee de vragen en de bundels van woorden ("de wortel van
vijftig") naar echte notatie (`\(\sqrt{50}\)`) gaan. Zie
`oefenplatform/lib/wiskunde.ts` voor hoe een formule geschreven wordt en
waarom `$` géén scheidingsteken is.

## De weg

1. **Omzetten.** `python3 -I inhoud/omzetten/naar_notatie.py <bestand.py> …`
   - zonder vlag: enkel wat achter `vraag=`, `uitleg=` en `opties=` staat;
   - `--bundels`: alle tekst behalve wat in een aanroep of tussen blokhaken
     staat (de getallen van een tekening, de sleutel van een bundel);
   - `--sets`: ook `{1, 2, 3}` en een losse hoofdletter, voor een hoofdstuk
     over verzamelingen.
   Een hoofdstuk dat enkel in een json staat: `json_omzet.py <json> "<titel>"`.
   Dit script zet enkel de getallen in notatie. Wat daarna nog in woorden
   staat, doen deze drie, in deze volgorde:
   - `woordmacht.py` — "tot de macht", "wortel uit", "in het kwadraat",
     "maal" en "gedeeld door" tussen twee stukjes notatie;
   - `woordgetal.py` — machten waarvan het grondtal of de exponent nog een
     woord is ("zeven tot de macht nul", "tot de macht een half");
   - `funcnot.py` — functienotatie: `f(x) is \(3 \cdot 2^{x}\)` wordt
     `\(f(x) = 3 \cdot 2^{x}\)`, en `x is \(0\)` wordt `\(x = 0\)`.
   Voor de wetenschappen komen daar nog drie bij:
   - `chemnot.py` — **voor** `naar_notatie.py` met `--vooraf` (zet de formules
     van de stoffen in subscript: `H2O` wordt `H₂O`) en **erna** zonder vlag
     (herstelt wat naar_notatie van een ion of een configuratie gemaakt had).
     Scheikunde blijft met unicode geschreven, niet met KaTeX: `\text{}` kan
     geen `₂` tekenen ("No character metrics"). Enkel een macht van tien
     (`6,02 · 10²³`) wordt een formule.
   - `fysnot.py` — een hele natuurkundige vergelijking (`Q = c . m . ΔT`,
     `p.V = n.R.T`) wordt een formule, met `\cdot` tussen twee symbolen en
     `\times` tussen twee getallen. Met `--los` wordt ook een symbool dat
     helemaal alleen in een zin staat omgezet (`Ek`, `Δx`, `Fn`, `ρ`).
   - `plak_formules.py` — twee formules met enkel een rekenteken ertussen
     worden één formule: `\(14\) x \(4 = 56\)` wordt
     `\(14 \times 4 = 56\)`. Kijk de uitvoer van `--toon` altijd na.
   Alle drie kennen `--velden` (enkel `vraag`, `uitleg`, `opties`, `stelling`
   en `tekst`) en `--strings` (elke string, voor de bundelbestanden).
   Daarna altijd **`rauw.py`**: dat zet een `r` voor elke gewone string die
   een backslash gekregen heeft. Het gebruikt de tokenizer van python zelf,
   want een regex telt de aanhalingstekens van een bestaande r-string fout.
2. **Narekenen.** Het bouwscript van het niveau opnieuw draaien, zodat elke
   vraag weer wordt nagerekend en de json opnieuw wordt geschreven.
3. **Nakijken.**
   - `node inhoud/omzetten/katex_na.js <json> …` — leest KaTeX elke formule?
   - `python3 -I inhoud/omzetten/lek_json.py <json> …` — notatie buiten `\( \)`?
   - `python3 -I inhoud/omzetten/kaal_getal.py <json> …` — nog getallen in
     woorden? (kaartjes van een sleepvraag en een uur mógen gewone tekst zijn)
   - `python3 -I inhoud/omzetten/stuk_teken.py <bestand.py> …` — is er een × of
     een − een `-` geworden?
   - `python3 -I inhoud/controleer_patronen.py` — niets te raden?
4. **Bundels.** `python3 -I inhoud/omzetten/bouw_module.py maak_<module> …`
   maakt de pdf's van één bronbestand opnieuw en zet ze bij hun vak.
   `lek_bundel.py maak_<module>` zoekt notatie buiten de formules,
   `bladspiegel.py <pdf>` geeft per bladzijde de laagste inkt (onder 790
   blijven) en daarna lees je de bundel gerenderd na.
5. Tochten (`maak_interactief.py`), zips (`maak_zips.py`) en `npx tsc --noEmit`.

## Wat we onderweg geleerd hebben

- **Een teken dat buiten een formule blijft staan, moet zijn eigen teken
  blijven.** × mag geen · worden en − geen `-`. Daarom gaan die tekens als
  sentinel door het script: binnen een formule worden ze latex, erbuiten weer
  het teken uit de tekst.
- **Een titel blijft gewone tekst.** De leerbundel hangt met haar titel aan het
  hoofdstuk vast; een formule in `titel=`, `kop=` of `breed=` breekt dat. Zie
  `SLA_VELD_OVER`.
- **Het antwoord van een invulvraag blijft gewone tekst**, en de kaartjes van
  een sleepvraag ook: die worden zonder `<Formule>` getekend. Zie
  `ANTWOORD_ARG`.
- **Wie een optie naleest, moet de notatie kunnen weglezen.** `reken.plat()`
  (🧱 Basis) en `zonder_notatie()` (`inhoud/notatie.py`) doen dat; `zichtbaar()`
  telt een optie op schermbreedte voor de gokcontroles.
- **Een f-string slaat het script over**, want het kan ze niet veilig
  herschrijven. Zoek ze zelf: `grep -n 'f"' <bestand>`.
- Woorden die enkel een zin aan elkaar praten ("Bij × 1000") horen nooit in een
  formule; zie `STOPWOORDEN`.
- Lees een bundel altijd gerenderd na, niet in de html.
- **Twee getallen naast elkaar worden één getal.** `\(2025\) \(46000\)`
  wordt bij het samenvoegen `\(2025\,46000\)`, en dat leest als één getal.
  Zoek erop: `grep -o '\\([0-9]\{1,4\}\\,[0-9]\{4,\}'`.
- **Een getal van vijf cijfers of meer krijgt zijn groepjes**: `20\,000`,
  niet `20000`. Een jaartal van vier cijfers blijft zoals het is.
- **Een nummer in een opsomming is geen formule.** "1. Begrijp het probleem"
  blijft gewone tekst.
- **De docstring van een bestand blijft gewone tekst**, anders breekt de
  module: een gewone docstring met `\(` erin is een foute escape.
- **Een formule mag nooit midden in een woord eindigen.** `\(5 = s\)torten`
  hoort `\(5\) = storten` te zijn: het script las de eerste letter van het
  volgende woord als een symbool. `stuk_teken.py` meldt dit nu, en de span van
  `fysnot.py` eindigt niet meer vlak voor een letter.
- **`reken=` en `antwoord=` blijven gewone tekst.** `reken` wordt uitgerekend
  en `antwoord` letterlijk vergeleken, dus draai op een bestand met dicts
  altijd `--velden`, nooit zonder vlag.
- **Een sleutel van een dict is een bestandsnaam.** Komt er notatie in een
  sleutel van `BUNDELS` of `OEFENBUNDELS`, dan krijgt de pdf een naam met
  `\(` erin en struikelt pdf.js.
- **Een middelste punt (·) en een schuine streep scheiden ook een opsomming.**
  `\(0{,}2\) · \(0{,}7\)` is een rijtje, geen maalbewerking; daarom staat `·`
  niet in `plak_formules.py`.
- **Fe is ijzer, geen F maal e.** De scheikundige symbolen staan in `CHEM` van
  `fysnot.py`, zodat een reactievergelijking geen formule wordt. Draai
  `fysnot.py` niet op de scheikundebestanden: daar is `C=C` een dubbele
  binding en geen vergelijking.
- **Een wortel staat rond de hele breuk of rond niets.**
  `\(\sqrt{p}\) \((1-p)\)/\(n\)` was fout: het hoort
  `\(\sqrt{\dfrac{p \cdot (1-p)}{n}}\)` te zijn.
