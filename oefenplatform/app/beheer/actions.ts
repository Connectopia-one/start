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
 * Twee titels vergelijken zonder te struikelen over een streepje of een spatie
 * te veel. Een titel die je uit een bestand kopieert, heeft soms een lang
 * streepje (—) waar in de databank een kort streepje (-) staat, of een dubbele
 * spatie. Zonder deze opkuis ziet de import zo'n titel als nieuw en maakt ze
 * het hoofdstuk een tweede keer aan.
 */
function titelSleutel(titel: string) {
  return titel
    .replace(/[\u2010-\u2015]/g, "-")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}

/**
 * Importeert in één keer meerdere hoofdstukken (met hun vragen) voor een vak.
 * Een hoofdstuk met een titel die al bestaat binnen dit vak krijgt de nieuwe
 * vragen erbij toegevoegd; een onbekende titel wordt als nieuw hoofdstuk
 * aangemaakt, op het eerste volgnummer dat nog vrij is. Verwijderde je net een
 * hoofdstuk, dan komt het nieuwe dus op die vrijgekomen plek te staan; anders
 * achteraan de lijst.
 *
 * Staat "vervang" aan, dan gaan de vragen die al bij zo'n hoofdstuk stonden
 * eerst weg en blijven alleen die uit dit bestand over. Zo kan je een
 * verouderd hoofdstuk bijwerken zonder het eerst te verwijderen — het houdt
 * dan ook zijn plek, zijn webadres en zijn leerbundel.
 */
export async function bulkImportVakInhoud(formData: FormData) {
  await requireBeheerder();
  const vakId = String(formData.get("vak_id") || "");
  const json = String(formData.get("json") || "").trim();
  const vervang = formData.get("vervang") === "on";
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
  (bestaande ?? []).forEach((h) => titelNaarId.set(titelSleutel(h.titel), h.id));
  // Het eerste hoofdstuk van elke categorie (niveau) binnen dit vak is altijd
  // gratis om uit te proberen — zowel al bestaande als in deze import zelf.
  const niveausMetHoofdstuk = new Set<string>((bestaande ?? []).map((h) => h.niveau));

  for (const hfst of payload!.hoofdstukken) {
    const titel = String(hfst.titel || "").trim();
    if (!titel) continue;
    const niveau = NIVEAUS.some((n) => n.slug === hfst.niveau) ? hfst.niveau! : "start";

    let hoofdstukId = titelNaarId.get(titelSleutel(titel));
    if (!hoofdstukId) {
      const eersteVanNiveau = !niveausMetHoofdstuk.has(niveau);
      niveausMetHoofdstuk.add(niveau);
      const rij = { vak_id: vakId, titel, gratis: !!hfst.gratis || eersteVanNiveau, niveau };
      let { data: nieuw, error: hoofdstukFout } = await admin
        .from("hoofdstukken")
        .insert({ ...rij, volgnummer: neemVolgnummer() })
        .select("id")
        .single();
      // Botst het nummer toch nog (bijvoorbeeld omdat iemand anders tegelijk
      // iets toevoegde), kijk dan opnieuw welke nummers vrij zijn en probeer
      // het nog één keer.
      if (hoofdstukFout?.code === "23505") {
        const opnieuw = await vrijeVolgnummers(admin, "hoofdstukken", "vak_id", vakId);
        ({ data: nieuw, error: hoofdstukFout } = await admin
          .from("hoofdstukken")
          .insert({ ...rij, volgnummer: opnieuw() })
          .select("id")
          .single());
      }
      if (hoofdstukFout || !nieuw) {
        redirect(
          "/beheer/vakken?fout=" +
            encodeURIComponent(`Hoofdstuk "${titel}" aanmaken mislukt: ${hoofdstukFout?.message ?? "onbekende fout"}`)
        );
      }
      hoofdstukId = nieuw!.id as string;
      titelNaarId.set(titelSleutel(titel), hoofdstukId);
    }

    const vragen = Array.isArray(hfst.vragen) ? hfst.vragen : [];
    if (!vragen.length) continue;

    // Bij "vervangen" gaan de oude vragen van dit hoofdstuk eerst weg, zodat je
    // een bijgewerkt bestand kan importeren zonder alles dubbel te krijgen.
    if (vervang) {
      const { error: wisFout } = await admin.from("vragen").delete().eq("hoofdstuk_id", hoofdstukId);
      if (wisFout) {
        redirect(
          "/beheer/vakken?fout=" +
            encodeURIComponent(`Oude vragen van "${titel}" verwijderen mislukt: ${wisFout.message}`)
        );
      }
    }

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
