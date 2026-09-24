"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { volgendVolgnummer, vrijeVolgnummers } from "@/lib/volgnummer";

type NieuweVraag = {
  type: "meerkeuze" | "invultekst" | "waarofniet";
  vraag: string;
  opties?: string[] | null;
  antwoord: number | string | boolean | number[];
  uitleg?: string | null;
  /** Optioneel: een volledige externe URL naar een afbeelding (bv. na bulk-import). */
  afbeelding_url?: string | null;
};

function terugPad(vakSlug: string, volgnummer: string) {
  return `/beheer/vakken/${vakSlug}/${volgnummer}`;
}

/**
 * Wordt rechtstreeks aangeroepen vanuit NieuwVraagForm (een client component),
 * niet als een `<form action>` — gooit daarom een gewone Error in plaats van
 * te redirecten, zodat het formulier zelf de foutmelding kan tonen (dezelfde
 * aanpak als registreerLeerstof hieronder).
 */
export async function maakVraag(formData: FormData) {
  await requireBeheerder();
  const hoofdstukId = String(formData.get("hoofdstuk_id") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");
  const type = String(formData.get("type") || "meerkeuze") as NieuweVraag["type"];
  const vraag = String(formData.get("vraag") || "").trim();
  const optiesRaw = String(formData.get("opties") || "").trim();
  const antwoordRaw = String(formData.get("antwoord") || "").trim();
  const uitleg = String(formData.get("uitleg") || "").trim() || null;
  const afbeeldingPad = String(formData.get("afbeelding_pad") || "").trim() || null;

  if (!vraag || !antwoordRaw) {
    throw new Error("Vul minstens de vraag en het antwoord in.");
  }

  const opties = type === "meerkeuze" ? optiesRaw.split("\n").map((r) => r.trim()).filter(Boolean) : null;
  let antwoord: number | string | boolean | number[];
  // Bij meerkeuze mag je meer dan één nummer invullen, gescheiden door een
  // komma: "0, 2" betekent dat het eerste én het derde antwoord juist zijn en
  // dat een kind ze allebei moet aanduiden. Zie lib/antwoord.ts.
  if (type === "meerkeuze") {
    const nummers = antwoordRaw
      .split(",")
      .map((deel) => Number(deel.trim()))
      .filter((n) => Number.isInteger(n));
    if (!nummers.length) throw new Error("Vul bij meerkeuze een nummer in, of meerdere met een komma ertussen.");
    antwoord = nummers.length === 1 ? nummers[0] : nummers.sort((a, b) => a - b);
  }
  else if (type === "waarofniet") antwoord = antwoordRaw.toLowerCase() === "waar" || antwoordRaw.toLowerCase() === "true";
  else antwoord = antwoordRaw;

  const admin = createAdminClient();

  const { error } = await admin.from("vragen").insert({
    hoofdstuk_id: hoofdstukId,
    volgnummer: await volgendVolgnummer(admin, "vragen", "hoofdstuk_id", hoofdstukId),
    type,
    vraag,
    opties,
    antwoord,
    uitleg,
    afbeelding_pad: afbeeldingPad,
  });

  if (error) throw new Error("Vraag toevoegen is niet gelukt: " + error.message);

  revalidatePath(terugPad(vakSlug, volgnummer));
}

/**
 * Haalt de vragen uit wat er geplakt is.
 *
 * Dit veld verwacht een kale lijst van vragen, want je zit al in één hoofdstuk.
 * Maar de bestanden in `inhoud/start` zijn gemaakt voor het andere invoerveld,
 * dat op de vakkenpagina staat: daar zit de lijst in `{"hoofdstukken": [...]}`.
 * Die twee door elkaar halen is zo gebeurd, dus we nemen zo'n bestand hier ook
 * gewoon aan. Staat er meer dan één hoofdstuk in, dan is het echt voor het
 * andere veld bedoeld en zeggen we dat.
 */
function haalVragenEruit(gelezen: unknown): NieuweVraag[] {
  if (Array.isArray(gelezen)) return gelezen as NieuweVraag[];

  const hoofdstukken = (gelezen as { hoofdstukken?: unknown })?.hoofdstukken;
  if (Array.isArray(hoofdstukken)) {
    if (hoofdstukken.length === 1) {
      const vragen = (hoofdstukken[0] as { vragen?: unknown })?.vragen;
      if (Array.isArray(vragen)) return vragen as NieuweVraag[];
    }
    throw new Error(
      "dit bestand bevat meerdere hoofdstukken. Gebruik het invoerveld op de vakkenpagina," +
        " onder \"Bulk-import: meerdere hoofdstukken tegelijk\"."
    );
  }

  throw new Error("Verwacht een JSON-array van vragen.");
}

export async function bulkImportVragen(formData: FormData) {
  await requireBeheerder();
  const hoofdstukId = String(formData.get("hoofdstuk_id") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");
  const json = String(formData.get("json") || "").trim();

  let vragen: NieuweVraag[];
  try {
    const gelezen = JSON.parse(json);
    vragen = haalVragenEruit(gelezen);
  } catch (e) {
    redirect(
      terugPad(vakSlug, volgnummer) +
        "?fout=" +
        encodeURIComponent("Ongeldige JSON: " + (e instanceof Error ? e.message : "onbekende fout"))
    );
  }

  const admin = createAdminClient();
  const neemVolgnummer = await vrijeVolgnummers(admin, "vragen", "hoofdstuk_id", hoofdstukId);

  const rijen = vragen!.map((v) => ({
    hoofdstuk_id: hoofdstukId,
    volgnummer: neemVolgnummer(),
    type: v.type,
    vraag: v.vraag,
    opties: v.opties ?? null,
    antwoord: v.antwoord,
    uitleg: v.uitleg ?? null,
    afbeelding_pad: v.afbeelding_url ?? null,
  }));

  const { error } = await admin.from("vragen").insert(rijen);
  if (error) {
    redirect(terugPad(vakSlug, volgnummer) + "?fout=" + encodeURIComponent("Bulk-import mislukt: " + error.message));
  }

  revalidatePath(terugPad(vakSlug, volgnummer));
  redirect(terugPad(vakSlug, volgnummer));
}

export async function verwijderVraag(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");

  const admin = createAdminClient();
  const { data: vraag } = await admin.from("vragen").select("afbeelding_pad").eq("id", id).maybeSingle();
  // Enkel opruimen in onze eigen bucket — een externe URL (bulk-import) is niet
  // iets dat wij bewaren en dus niet iets dat wij kunnen/mogen verwijderen.
  if (vraag?.afbeelding_pad && !vraag.afbeelding_pad.startsWith("http")) {
    await admin.storage.from("vraagafbeeldingen").remove([vraag.afbeelding_pad]);
  }
  await admin.from("vragen").delete().eq("id", id);

  revalidatePath(terugPad(vakSlug, volgnummer));
  redirect(terugPad(vakSlug, volgnummer));
}

/**
 * Geeft een tijdelijke, rechtstreekse upload-link naar Supabase Storage terug
 * voor een afbeelding bij een vraag (zelfde patroon als leerstof-uploads).
 */
export async function maakVraagAfbeeldingUploadUrl(hoofdstukId: string, bestandsnaam: string) {
  await requireBeheerder();
  const admin = createAdminClient();
  const path = `${hoofdstukId}/${Date.now()}-${bestandsnaam}`;

  const { data, error } = await admin.storage.from("vraagafbeeldingen").createSignedUploadUrl(path);
  if (error || !data) {
    throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  }
  return { path: data.path, token: data.token };
}

/**
 * Geeft een tijdelijke, rechtstreekse upload-link naar Supabase Storage terug.
 * Het bestand zelf gaat zo NIET door de server action heen — dat omzeilt de
 * limiet van ~4,5MB die Vercel op reguliere server-verzoeken zet.
 */
export async function maakLeerstofUploadUrl(hoofdstukId: string, bestandsnaam: string) {
  await requireBeheerder();
  const admin = createAdminClient();
  const path = `${hoofdstukId}/${Date.now()}-${bestandsnaam}`;

  const { data, error } = await admin.storage.from("leerstof").createSignedUploadUrl(path);
  if (error || !data) {
    throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  }
  return { path: data.path, token: data.token };
}

export async function registreerLeerstof(input: {
  hoofdstukId: string;
  vakSlug: string;
  volgnummer: string;
  titel: string;
  bestandspad: string;
}) {
  await requireBeheerder();
  const admin = createAdminClient();

  const { error } = await admin.from("leerstof").insert({
    hoofdstuk_id: input.hoofdstukId,
    titel: input.titel,
    bestandspad: input.bestandspad,
  });

  if (error) throw new Error(error.message);
  revalidatePath(terugPad(input.vakSlug, input.volgnummer));
}

export async function verwijderLeerstof(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const bestandspad = String(formData.get("bestandspad") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");

  const admin = createAdminClient();
  if (bestandspad) await admin.storage.from("leerstof").remove([bestandspad]);
  await admin.from("leerstof").delete().eq("id", id);

  revalidatePath(terugPad(vakSlug, volgnummer));
  redirect(terugPad(vakSlug, volgnummer));
}

/* ------------------------------------------------------------------ leerbundel
   Een leerbundel is de theorie in het platform zelf, opgebouwd uit blokjes:
   een tussentitel, een stuk tekst, een weetje in een kadertje, of een
   afbeelding met een onderschrift. Zo kan je uitleg afwisselen met beeld.
   De blokjes staan in de volgorde van hun volgnummer; met verplaatsLeerbundelBlok
   wissel je een blokje van plaats met zijn buur. */

export type LeerbundelSoort = "titel" | "tekst" | "weetje" | "afbeelding";

/** Zie maakLeerstofUploadUrl: het bestand gaat rechtstreeks naar Supabase. */
export async function maakLeerbundelUploadUrl(hoofdstukId: string, bestandsnaam: string) {
  await requireBeheerder();
  const admin = createAdminClient();
  const path = `${hoofdstukId}/${Date.now()}-${bestandsnaam}`;

  const { data, error } = await admin.storage.from("leerbundel").createSignedUploadUrl(path);
  if (error || !data) {
    throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  }
  return { path: data.path, token: data.token };
}

export async function voegLeerbundelBlokToe(input: {
  hoofdstukId: string;
  vakSlug: string;
  volgnummer: string;
  soort: LeerbundelSoort;
  tekst: string | null;
  afbeeldingPad: string | null;
}) {
  await requireBeheerder();

  const tekst = input.tekst?.trim() || null;
  if (input.soort === "afbeelding") {
    if (!input.afbeeldingPad) throw new Error("Kies eerst een afbeelding.");
  } else if (!tekst) {
    throw new Error("Vul de tekst in.");
  }

  const admin = createAdminClient();
  const { data: laatste } = await admin
    .from("leerbundel")
    .select("volgnummer")
    .eq("hoofdstuk_id", input.hoofdstukId)
    .order("volgnummer", { ascending: false })
    .limit(1);

  const { error } = await admin.from("leerbundel").insert({
    hoofdstuk_id: input.hoofdstukId,
    volgnummer: (laatste?.[0]?.volgnummer ?? 0) + 1,
    soort: input.soort,
    tekst,
    afbeelding_pad: input.afbeeldingPad,
  });
  if (error) throw new Error("Toevoegen is niet gelukt: " + error.message);

  revalidatePath(terugPad(input.vakSlug, input.volgnummer));
}

export async function verwijderLeerbundelBlok(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");

  const admin = createAdminClient();
  const { data: blok } = await admin
    .from("leerbundel")
    .select("afbeelding_pad")
    .eq("id", id)
    .maybeSingle();
  if (blok?.afbeelding_pad) {
    await admin.storage.from("leerbundel").remove([blok.afbeelding_pad]);
  }
  await admin.from("leerbundel").delete().eq("id", id);

  revalidatePath(terugPad(vakSlug, volgnummer));
  redirect(terugPad(vakSlug, volgnummer));
}

/** Wisselt het blokje van plaats met het blokje erboven of eronder. */
export async function verplaatsLeerbundelBlok(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const richting = String(formData.get("richting") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");
  const terug = terugPad(vakSlug, volgnummer);

  const admin = createAdminClient();
  const { data: blok } = await admin
    .from("leerbundel")
    .select("id, hoofdstuk_id, volgnummer")
    .eq("id", id)
    .maybeSingle();
  if (!blok) redirect(terug);

  const omhoog = richting === "omhoog";
  const { data: buur } = await admin
    .from("leerbundel")
    .select("id, volgnummer")
    .eq("hoofdstuk_id", blok!.hoofdstuk_id)
    [omhoog ? "lt" : "gt"]("volgnummer", blok!.volgnummer)
    .order("volgnummer", { ascending: !omhoog })
    .limit(1);

  const ander = buur?.[0];
  if (ander) {
    // Even naar een vrij nummer parkeren, anders botsen de twee nummers.
    await admin.from("leerbundel").update({ volgnummer: -1 }).eq("id", blok!.id);
    await admin.from("leerbundel").update({ volgnummer: blok!.volgnummer }).eq("id", ander.id);
    await admin.from("leerbundel").update({ volgnummer: ander.volgnummer }).eq("id", blok!.id);
  }

  revalidatePath(terug);
  redirect(terug);
}
