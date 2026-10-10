import Link from "next/link";

/*
  Eén zin die zegt wat dit platform is, onderaan een hoofdstuk en onder de
  hoofdstukkenlijst van een vak.

  Waarom die zin er staat: Enya Vermeyen, leerkracht wiskunde, keek op
  10 oktober 2026 naar een gratis hoofdstuk en schreef dat het niet duidelijk
  is wat het doel van het platform is. Ze had gelijk. Wie via een losse link
  op één hoofdstuk binnenvalt, ziet alleen vragen en moet zelf raden waar die
  vandaan komen. Op /onderwijsdoelen staat het hele verhaal met de fiches
  erbij, maar daar kom je alleen als je ernaar zoekt.

  De zin zelf is van Kim, dezelfde dag: "ik bezie het als een leidraad door de
  te kennen leerstof". Pas die gerust aan; het is gewone tekst.
*/
export function Leidraad() {
  return (
    <p className="mt-8 border-t border-border pt-5 text-sm text-ink-dim">
      Een leidraad door de te kennen leerstof, opgebouwd rond de vakfiches van
      de Examencommissie. Een extra bron naast een handboek of een cursus, geen
      vervanging ervan.{" "}
      <Link
        href="/onderwijsdoelen"
        className="text-forest-dark underline-offset-2 hover:underline"
      >
        Waarop is dit gebaseerd?
      </Link>
    </p>
  );
}
