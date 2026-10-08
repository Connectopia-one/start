# De twee brieven met de uitslag van het meetesten

Zesentwintig mensen vulden het formulier op connectopia.one/meetesten in. Tien
daarvan zijn gekozen als tester, de zestien anderen krijgen drie dagen.

- `gekozen.html` → `../meetesten-gekozen.png` en `.pdf`
  Code **TOPTESTER2026**, dezelfde regels als de testgezinnen van de winactie:
  een maand alles open (tot en met zondag 8 november 2026), daarna de evaluatie
  invullen en je krijgt een gratis jaarlicentie.
- `niet-gekozen.html` → `../meetesten-drie-dagen.png` en `.pdf`
  Code **3DAGEN**, open tot zondag 11 oktober 2026 om 18 uur. Daarna zet Kim de
  toegang van die gezinnen uit bij Beheer → Gezinnen; ze vallen dan terug op de
  gratis hoofdstukken en zien bij een hoofdstuk op slot de knop naar de
  betaalpagina.

Allebei opnieuw renderen met

    node bron/render.js

Het script zegt per blad of de tekst nog boven de voettekst eindigt
(`tijdOnder` moet onder `voetBoven` blijven, dus onder 1050). Het blad van de
gekozenen zit vol: daar staan onderaan de stijl een paar krappere
tussenruimtes.

De lettertypes en het logo staan hier wel in de repo, net als bij
`drukwerk/nieuwsbrief/bron`.
