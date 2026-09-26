/**
 * Bij een taalvak wordt een ingetypt antwoord streng vergeleken.
 *
 * Bij de zaakvakken mag "kieuw" doorgaan voor "kieuwen": het kind kent het
 * orgaan, en dat is wat de vraag wil weten. Bij Frans, Engels en Nederlands is
 * net dát verschil de leerstof — "parle" tegenover "parles", "kind" tegenover
 * "kinderen" — dus daar telt alleen de juiste vorm. Zie woordkern in
 * lib/antwoord.ts.
 */
const TAALVAKKEN = ["nederlands", "frans", "engels", "duits"];

export function isTaalvak(slug: string | null | undefined): boolean {
  if (!slug) return false;
  const kaal = slug.toLowerCase();
  return TAALVAKKEN.some((taal) => kaal === taal || kaal.startsWith(taal + "-"));
}
