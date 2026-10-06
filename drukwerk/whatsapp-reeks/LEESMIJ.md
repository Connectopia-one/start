# Reeks beelden voor whatsapp en voor een verhaal

Zes staande beelden die samen het hele verhaal vertellen. Bedoeld om na
elkaar door te sturen aan mensen die via whatsapp reageerden, en om als
verhaal te posten op instagram of facebook. Een reeks leest vlotter dan één
volgepropt beeld, en wie er één doorstuurt heeft er nog altijd alles op
staan: wie we zijn en waar hij moet zijn.

## Twee maten

- `gsm/` — **1080 x 1350** (staand 4:5), voor whatsapp. Dat is het grootste
  formaat dat whatsapp in het gesprek toont zonder de boven- en onderkant af
  te snijden.
- `verhaal/` — **1080 x 1920** (9:16), voor een verhaal op instagram of
  facebook. Daar staat de tekst verder van de randen, want die apps leggen er
  hun eigen knoppen overheen.
- `connectopia-beelden.zip` — alles samen.

## De zes beelden

1. Wie we zijn, met vier foto's uit de werking
2. Waarom we dit doen: Kims verhaal, en waar we voor staan
3. Het aanbod in de week: plusklas en pluswerking woensdag
4. Het aanbod in het weekend: pluswerking zaterdag en Young Engineers
5. De vakantiekampen, met de datums van de herfst en de kerst
6. Zo begin je: gratis proefles, website, telefoon en mail

## Een berichtje om erbij te zetten

> Dag! Je had ons ooit een berichtje gestuurd, dus ik dacht: ik laat even
> weten wat er dit schooljaar allemaal is. Ik stuur je een paar beeldjes
> achter elkaar, dan lees je het rustig na. Alles staat ook op
> www.connectopia.one/aanbod. Vragen mag altijd, gewoon hier antwoorden.

## Opnieuw maken

```
cd bron
node render.js
```

Het script maakt beide maten in één keer en zegt per beeld `ok` of
`PAST NIET`. De tekst staat in `bron/reeks.html`; elk beeld is één
`<section class="beeld">`.

## Wat je nakijkt als je ze later hergebruikt

- De **datums** op beeld 5; die verouderen het snelst.
- De **prijzen** op beeld 3 en 4.
- Beeld 2 komt uit Kims eigen tekst op de website
  (`website/content/over-ons.ts`). Verandert die, verander dan ook dit beeld.
