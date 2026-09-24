/*
  Een ingevuld formulier omzetten in een mail.

  Waarom dit bestaat: vroeger stond er `action="mailto:..."` met
  `method="post"` op het formulier zelf. Dat werkt, maar de browser ziet een
  formulier dat naar iets anders dan https verstuurt, en toont dan een scherm
  met "De gegevens die je wilt sturen, zijn niet beveiligd". Een ouder die op
  het punt staat de naam van zijn kind door te geven, haakt daar af — terecht.

  Er is niets onveilig aan: de mail vertrekt vanuit het eigen mailprogramma van
  de ouder, en er gaat geen enkel gegeven over het internet langs ons of langs
  iemand anders. Maar dat weet de browser niet.

  Daarom bouwen we de mail nu zelf op en openen we ze als een gewone maillink.
  De browser ziet dan geen formulier dat iets verstuurt, en zegt niets.
*/
export function mailtoUitFormulier(
  formulier: HTMLFormElement,
  naar: string,
  onderwerp: string
): string {
  const regels: string[] = [];
  for (const [naam, waarde] of new FormData(formulier).entries()) {
    if (typeof waarde !== "string") continue;
    const schoon = waarde.trim();
    // Een leeg vakje laten we weg, anders staat de mail vol lege regels.
    // Een aankruisvakje dat niet aangevinkt is, komt hier sowieso niet langs.
    if (schoon) regels.push(`${naam}: ${schoon}`);
  }
  return (
    `mailto:${naar}` +
    `?subject=${encodeURIComponent(onderwerp)}` +
    `&body=${encodeURIComponent(regels.join("\n"))}`
  );
}
