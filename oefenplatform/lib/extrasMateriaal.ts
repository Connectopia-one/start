import { createClient } from "@/lib/supabase/server";
import { schoolVan, soortVan, type School, type Soort } from "@/inhoud/extras";

export type MateriaalItem = {
  id: string;
  groep: string;
  type: "link" | "pdf";
  titel: string;
  omschrijving: string | null;
  href: string;
  soort: Soort;
  school: School;
};

/*
  Alle links, documenten en filmpjes uit Beheer > Materiaal.

  We vragen "*" op en niet de kolommen bij naam: zolang de kolommen soort en
  schoolniveau er nog niet zijn (supabase/materiaal-soort.sql), werkt de pagina
  dan gewoon verder. Een pdf is dan een document, de rest een link, en alles
  staat onder "Voor iedereen".
*/
export async function haalMateriaal(): Promise<MateriaalItem[]> {
  const supabase = await createClient();
  const { data } = await supabase
    .from("materiaal")
    .select("*")
    .order("created_at", { ascending: true });

  const items: MateriaalItem[] = [];
  for (const rij of (data ?? []) as Record<string, string | null>[]) {
    const type = rij.type === "pdf" ? "pdf" : "link";
    let href: string | null = null;
    if (type === "link") href = rij.link;
    else if (rij.bestandspad) {
      href = supabase.storage.from("materiaal").getPublicUrl(rij.bestandspad)
        .data.publicUrl;
    }
    if (!href || !rij.id || !rij.titel) continue;
    items.push({
      id: rij.id,
      groep: rij.groep ?? "",
      type,
      titel: rij.titel,
      omschrijving: rij.omschrijving,
      href,
      soort: soortVan({ soort: rij.soort, type }),
      school: schoolVan({ schoolniveau: rij.schoolniveau }),
    });
  }
  return items;
}
