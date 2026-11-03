import type { SupabaseClient } from "@supabase/supabase-js";

/*
  Maakt tijdelijke links voor een hele reeks foto's.

  Vroeger vroeg elke foto apart een link aan, allemaal tegelijk. Bij een
  klasje met meer dan honderd foto's antwoordde de opslag dan voor een deel
  met "Too many requests", en die foto's verdwenen stil uit de lijst terwijl
  de teller ze wel meetelde. Nu gaan de links per pakje van 50 in één
  verzoek, en wat niet lukt wordt tot drie keer opnieuw gevraagd met een
  korte pauze ertussen.
*/
const PAKJE = 50;
const POGINGEN = 4;

function wacht(ms: number) {
  return new Promise((r) => setTimeout(r, ms));
}

export async function maakFotoLinks(
  supabase: { storage: SupabaseClient["storage"] },
  paden: string[],
  geldigSeconden = 60 * 10,
): Promise<Map<string, string>> {
  const links = new Map<string, string>();
  let open = Array.from(new Set(paden));

  for (let poging = 0; poging < POGINGEN && open.length > 0; poging++) {
    if (poging > 0) await wacht(400 * 2 ** (poging - 1));

    for (let i = 0; i < open.length; i += PAKJE) {
      const pakje = open.slice(i, i + PAKJE);
      const { data } = await supabase.storage.from("fotos").createSignedUrls(pakje, geldigSeconden);
      for (const item of data ?? []) {
        if (item.path && item.signedUrl && !item.error) links.set(item.path, item.signedUrl);
      }
    }

    open = open.filter((p) => !links.has(p));
  }

  return links;
}
