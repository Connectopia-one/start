import { schrijfInvul, schrijfKeuzes } from "@/lib/antwoord";
import { schrijfVorm, type VraagType } from "@/lib/vraagvorm";

/** Genoeg van een vraag om een antwoord leesbaar te tonen. */
export type WeergaveVraag = {
  type: VraagType;
  vraag: string;
  opties: string[] | null;
  antwoord: unknown;
};

/** Een gegeven of juist antwoord zoals een ouder het wil lezen. */
export function formatAntwoord(
  vraag: WeergaveVraag,
  waarde: number | string | boolean | number[] | string[] | null,
): string {
  if (waarde === null || waarde === undefined || waarde === "") return "—";
  // Een tabel of een keuzelijst, zie lib/vraagvorm.ts.
  const vorm = schrijfVorm(vraag, waarde);
  if (vorm !== null) return vorm;
  if (vraag.type === "meerkeuze") return schrijfKeuzes(vraag.opties, waarde);
  if (vraag.type === "waarofniet") {
    return waarde === true ? "Waar" : "Niet waar";
  }
  // Een invulvraag kan meer dan één juist antwoord hebben; we tonen het eerste.
  if (Array.isArray(waarde)) return schrijfInvul(waarde);
  return String(waarde);
}
