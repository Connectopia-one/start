"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { slugify } from "@/lib/slug";
import { NIVEAUS } from "@/lib/niveaus";
import { volgendVolgnummer, vrijeVolgnummers } from "@/lib/volgnummer";

export async function maakVak(formData: FormData) {
  await requireBeheerder();
  const naam = String(formData.get("naam") || "").trim();
  const rekenmachine = formData.get("rekenmachine") === "on";
  if (!naam) redirect("/beheer?fout=" + encodeURIComponent("Geef een naam op voor het vak."));

  const admin = createAdminClient();
  const { count } = await admin.from("vakken").select("id", { count: "exact", head: true });
  const { error } = await admin
    .from("vakken")
    .insert({ naam, slug: slugify(naam), volgorde: count ?? 0, rekenmachine });
  if (error) redirect("/beheer?fout=" + encodeURIComponent("Kon vak niet aanmaken (bestaat de naam al?)."));

  revalidatePath("/beheer/vakken");
  redirect("/beheer/vakken");
}

/**
 * De naam van een vak aanpassen, bijvoorbeeld na een typfout.
 *
 * De slug staat in het webadres van het vak. Die passen we mee aan zolang ze
 * nog de automatische vorm van de oude naam is — dan is het adres immers ook
 * fout getypt. Koos je de slug ooit zelf anders, dan blijft het adres staan,
 * zodat bestaande links blijven werken.
 */
export async function hernoemVak(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const naam = String(formData.get("naam") || "").trim();
  if (!id) redirect("/beheer/vakken");
  if (!naam) redirect("/beheer/vakken?fout=" + encodeURIComponent("Geef een naam op voor het vak."));

  const admin = createAdminClient();
  const { data: vak } = await admin.from("vakken").select("naam, slug").eq("id", id).maybeSingle();
  if (!vak) redirect("/beheer/vakken?fout=" + encodeURIComponent("Dit vak bestaat niet meer."));

  const nieuweSlug = slugify(naam);
  const slugVolgdeDeNaam = vak.slug === slugify(vak.naam);
  const wijziging: { naam: string; slug?: string } = { naam };
  if (slugVolgdeDeNaam && nieuweSlug && nieuweSlug !== vak.slug) {
    wijziging.slug = nieuweSlug;
  }

  const { error } = await admin.from("vakken").update(wijziging).eq("id", id);
  if (error) {
    redirect(
      "/beheer/vakken?fout=" +
        encodeURIComponent("Kon de naam niet aanpassen. Bestaat er al een vak met die naam?"),
    );
  }

  revalidatePath("/beheer/vakken");
  revalidatePath("/");
  redirect("/beheer/vakken");
}

/**
 * De titel van een hoofdstuk aanpassen, bijvoorbeeld na een typfout.
 *
 * Anders dan bij een vak zit hier geen slug aan vast: een hoofdstuk staat in
 * het webadres als zijn volgnummer. Een nieuwe titel breekt dus geen links.
 *
 * Let wel: de bulk-import zoekt een hoofdstuk op zijn titel. Hernoem je er een,
 * dan moet een JSON-bestand dat je daarna importeert de nieuwe titel gebruiken,
 * anders wordt het oude hoofdstuk opnieuw aangemaakt.
 */
export async function hernoemHoofdstuk(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const titel = String(formData.get("titel") || "").trim();
  if (!id) redirect("/beheer/vakken");
  if (!titel) {
    redirect("/beheer/vakken?fout=" + encodeURIComponent("Geef een titel op voor het hoofdstuk."));
  }

  const admin = createAdminClient();
  const { error } = await admin.from("hoofdstukken").update({ titel }).eq("id", id);
  if (error) {
    redirect("/beheer/vakken?fout=" + encodeURIComponent("Kon de titel van het hoofdstuk niet aanpassen."));
  }

  revalidatePath("/beheer/vakken");
  revalidatePath("/");
  redirect("/beheer/vakken");
}

export async function wisselRekenmachine(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const rekenmachine = formData.get("rekenmachine") === "true";
  const admin = createAdminClient();
  await admin.from("vakken").update({ rekenmachine: !rekenmachine }).eq("id", id);
  revalidatePath("/beheer/vakken");
  redirect("/beheer/vakken");
}

export async function verwijderVak(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const admin = createAdminClient();
  await admin.from("vakken").delete().eq("id", id);
  revalidatePath("/beheer/vakken");
  redirect("/beheer/vakken");
}

export async function maakHoofdstuk(formData: FormData) {
  await requireBeheerder();
  const vakId = String(formData.get("vak_id") || "");
  const titel = String(formData.get("titel") || "").trim();
  const gratis = formData.get("gratis") === "on";
  const niveau = String(formData.get("niveau") || "start");
  if (!vakId || !titel) redirect("/beheer/vakken?fout=" + encodeURIComponent("Geef een titel op voor het hoofdstuk."));
  if (!NIVEAUS.some((n) => n.slug === niveau)) redirect("/beheer/vakken?fout=" + encodeURIComponent("Ongeldige categorie."));

  const admin = createAdminClient();

  const { error } = await admin.from("hoofdstukken").insert({
    vak_id: vakId,
    titel,
    volgnummer: await volgendVolgnummer(admin, "hoofdstukken", "vak_id", vakId),
    gratis: gratis || (await isEersteVanNiveau(admin, vakId, niveau)),
    niveau,
  });
  if (error) {
    redirect("/beheer/vakken?fout=" + encodeURIComponent(`Hoofdstuk "${titel}" aanmaken mislukt: ${error.message}`));
  }

  revalidatePath("/beheer/vakken");
  redirect("/beheer/vakken");
}

/** Het eerste hoofdstuk van elke categorie (niveau) binnen een vak is altijd
 * gratis om uit te proberen — zo geeft elk vak een gratis staaltje op elk
 * niveau, niet enkel op het allereerste (start-)niveau. */
async function isEersteVanNiveau(
  admin: ReturnType<typeof createAdminClient>,
  vakId: string,
  niveau: string
): Promise<boolean> {
  const { count } = await admin
    .from("hoofdstukken")
    .select("id", { count: "exact", head: true })
    .eq("vak_id", vakId)
    .eq("niveau", niveau);
  return (count ?? 0) === 0;
}

export async function wisselGratis(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const gratis = formData.get("gratis") === "true";
  const admin = createAdminClient();
  await admin.from("hoofdstukken").update({ gratis: !gratis }).eq("id", id);
  revalidatePath("/beheer/vakken");
  redirect("/beheer/vakken");
}

export async function verwijderHoofdstuk(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const admin = createAdminClient();
  await admin.from("hoofdstukken").delete().eq("id", id);
  revalidatePath("/beheer/vakken");
  redirect("/beheer/vakken");
}

type BulkVraag = {
  type: "meerkeuze" | "invultekst" | "waarofniet";
  vraag: string;
  opties?: string[] | null;
  antwoord: number | string | boolean;
  uitleg?: string | null;
};

type BulkHoofdstuk = {
  titel: string;
  niveau?: string;
  gratis?: boolean;
  vragen: BulkVraag[];
};

/**
 * Importeert in één keer meerdere hoofdstukken (met hun vragen) voor een vak.
 * Een hoofdstuk met een titel die al bestaat binnen dit vak krijgt de nieuwe
 * vragen erbij toegevoegd; een onbekende titel wordt als nieuw hoofdstuk
 * aangemaakt, op het eerste volgnummer dat nog vrij is. Verwijderde je net een
 * hoofdstuk, dan komt het nieuwe dus op die vrijgekomen plek te staan; anders
 * achteraan de lijst.
 */
export async function bulkImportVakInhoud(formData: FormData) {
  await requireBeheerder();
  const vakId = String(formData.get("vak_id") || "");
  const json = String(formData.get("json") || "").trim();
  if (!vakId) redirect("/beheer/vakken?fout=" + encodeURIComponent("Onbekend vak."));

  let payload: { hoofdstukken: BulkHoofdstuk[] };
  try {
    payload = JSON.parse(json);
    if (!payload || !Array.isArray(payload.hoofdstukken)) {
      throw new Error('Verwacht een object met een "hoofdstukken"-lijst.');
    }
  } catch (e) {
    redirect(
      "/beheer/vakken?fout=" +
        encodeURIComponent("Ongeldige JSON: " + (e instanceof Error ? e.message : "onbekende fout"))
    );
  }

  const admin = createAdminClient();

  const { data: bestaande } = await admin
    .from("hoofdstukken")
    .select("id, titel, niveau")
    .eq("vak_id", vakId);

  const neemVolgnummer = await vrijeVolgnummers(admin, "hoofdstukken", "vak_id", vakId);
  const titelNaarId = new Map<string, string>();
  (bestaande ?? []).forEach((h) => titelNaarId.set(h.titel.trim().toLowerCase(), h.id));
  // Het eerste hoofdstuk van elke categorie (niveau) binnen dit vak is altijd
  // gratis om uit te proberen — zowel al bestaande als in deze import zelf.
  const niveausMetHoofdstuk = new Set<string>((bestaande ?? []).map((h) => h.niveau));

  for (const hfst of payload!.hoofdstukken) {
    const titel = String(hfst.titel || "").trim();
    if (!titel) continue;
    const niveau = NIVEAUS.some((n) => n.slug === hfst.niveau) ? hfst.niveau! : "start";

    let hoofdstukId = titelNaarId.get(titel.toLowerCase());
    if (!hoofdstukId) {
      const eersteVanNiveau = !niveausMetHoofdstuk.has(niveau);
      niveausMetHoofdstuk.add(niveau);
      const { data: nieuw, error: hoofdstukFout } = await admin
        .from("hoofdstukken")
        .insert({ vak_id: vakId, titel, volgnummer: neemVolgnummer(), gratis: !!hfst.gratis || eersteVanNiveau, niveau })
        .select("id")
        .single();
      if (hoofdstukFout || !nieuw) {
        redirect(
          "/beheer/vakken?fout=" +
            encodeURIComponent(`Hoofdstuk "${titel}" aanmaken mislukt: ${hoofdstukFout?.message ?? "onbekende fout"}`)
        );
      }
      hoofdstukId = nieuw!.id as string;
      titelNaarId.set(titel.toLowerCase(), hoofdstukId);
    }

    const vragen = Array.isArray(hfst.vragen) ? hfst.vragen : [];
    if (!vragen.length) continue;

    const neemVraagnummer = await vrijeVolgnummers(admin, "vragen", "hoofdstuk_id", hoofdstukId);

    const rijen = vragen.map((v) => ({
      hoofdstuk_id: hoofdstukId,
      volgnummer: neemVraagnummer(),
      type: v.type,
      vraag: v.vraag,
      opties: v.opties ?? null,
      antwoord: v.antwoord,
      uitleg: v.uitleg ?? null,
    }));

    const { error: vragenFout } = await admin.from("vragen").insert(rijen);
    if (vragenFout) {
      redirect(
        "/beheer/vakken?fout=" +
          encodeURIComponent(`Vragen voor "${titel}" importeren mislukt: ${vragenFout.message}`)
      );
    }
  }

  revalidatePath("/beheer/vakken");
  redirect("/beheer/vakken");
}
