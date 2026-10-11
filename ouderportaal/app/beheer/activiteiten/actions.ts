"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder, requireStaff } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Activiteiten aanmaken, archiveren en verwijderen, en kinderen eraan koppelen.
  Het schema staat in supabase/activiteiten.sql.
*/

async function admin() {
  await requireBeheerder();
  return createAdminClient();
}

function terug(pad: string, bericht: string, fout = false): never {
  revalidatePath(pad);
  redirect(`${pad}?${fout ? "fout" : "succes"}=${encodeURIComponent(bericht)}`);
}

export async function maakActiviteit(formData: FormData) {
  const db = await admin();
  const naam = String(formData.get("naam") || "").trim();
  const soort = String(formData.get("soort") || "kamp").trim() || "kamp";
  const datum = String(formData.get("datum") || "").trim();
  const plaats = String(formData.get("plaats") || "").trim();
  const factuurregel = String(formData.get("factuurregel") || "").trim();
  const prijs = String(formData.get("prijs") || "").trim().replace(",", ".");

  if (!naam) terug("/beheer/activiteiten", "Geef de activiteit een naam.", true);
  if (prijs && !Number.isFinite(Number(prijs)))
    terug("/beheer/activiteiten", "De prijs is geen bedrag.", true);

  const { error } = await db.from("activiteiten").insert({
    naam,
    soort,
    datum: datum || null,
    plaats: plaats || null,
    factuurregel: factuurregel || null,
    prijs: prijs ? Number(prijs) : null,
  });

  if (error) terug("/beheer/activiteiten", error.message, true);
  terug("/beheer/activiteiten", `${naam} staat erbij.`);
}

export async function zetArchief(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const archief = String(formData.get("archief") || "") === "ja";

  const { error } = await db
    .from("activiteiten")
    .update({ archief })
    .eq("id", id);

  if (error) terug("/beheer/activiteiten", error.message, true);
  terug(
    "/beheer/activiteiten",
    archief ? "Naar het archief gezet." : "Terug uit het archief.",
  );
}

export async function verwijderActiviteit(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");

  /* De deelnames gaan mee weg: de koppeling staat met on delete cascade in
     supabase/activiteiten.sql. De kinderen zelf blijven uiteraard staan. */
  const { error } = await db.from("activiteiten").delete().eq("id", id);
  if (error) terug("/beheer/activiteiten", error.message, true);
  terug("/beheer/activiteiten", "Activiteit verwijderd.");
}

export async function voegKindToe(formData: FormData) {
  const db = await admin();
  const activiteitId = String(formData.get("activiteit_id") || "");
  const kindId = String(formData.get("kind_id") || "");
  const pad = `/beheer/activiteiten/${activiteitId}`;

  if (!kindId) terug(pad, "Kies eerst een kind.", true);

  /* Twee keer hetzelfde kind toevoegen mag gewoon niets doen; de sleutel van
     de tabel is (activiteit, kind). */
  const { error } = await db
    .from("deelnames")
    .upsert(
      { activiteit_id: activiteitId, kind_id: kindId },
      { onConflict: "activiteit_id,kind_id" },
    );

  if (error) terug(pad, error.message, true);
  terug(pad, "Kind toegevoegd.");
}

export async function haalKindWeg(formData: FormData) {
  const db = await admin();
  const activiteitId = String(formData.get("activiteit_id") || "");
  const kindId = String(formData.get("kind_id") || "");
  const pad = `/beheer/activiteiten/${activiteitId}`;

  const { error } = await db
    .from("deelnames")
    .delete()
    .eq("activiteit_id", activiteitId)
    .eq("kind_id", kindId);

  if (error) terug(pad, error.message, true);
  terug(pad, "Kind van de lijst gehaald.");
}

export async function bewaarNotitie(formData: FormData) {
  const db = await admin();
  const activiteitId = String(formData.get("activiteit_id") || "");
  const kindId = String(formData.get("kind_id") || "");
  const notitie = String(formData.get("notitie") || "").trim();
  const pad = `/beheer/activiteiten/${activiteitId}`;

  const { error } = await db
    .from("deelnames")
    .update({ notitie: notitie || null })
    .eq("activiteit_id", activiteitId)
    .eq("kind_id", kindId);

  if (error) terug(pad, error.message, true);
  terug(pad, "Notitie bewaard.");
}

/*
  De vinkjes op de gezinspagina: bij welke activiteiten hoort dit kind?

  Het formulier stuurt alle activiteiten mee als `alle`, en enkel de
  aangevinkte als `activiteit`. Zonder die eerste lijst zouden we niet weten
  welke vinkjes net uitgezet zijn, want een leeg vakje stuurt niets mee.
*/
export async function zetDeelnames(formData: FormData) {
  const db = await admin();
  const kindId = String(formData.get("kind_id") || "");
  const profileId = String(formData.get("profile_id") || "");
  const pad = `/beheer/gezinnen/${profileId}`;

  const alle = formData.getAll("alle").map(String);
  const gekozen = new Set(formData.getAll("activiteit").map(String));
  const weg = alle.filter((id) => !gekozen.has(id));

  if (weg.length) {
    const { error } = await db
      .from("deelnames")
      .delete()
      .eq("kind_id", kindId)
      .in("activiteit_id", weg);
    if (error) terug(pad, error.message, true);
  }

  if (gekozen.size) {
    const { error } = await db.from("deelnames").upsert(
      [...gekozen].map((activiteit_id) => ({ activiteit_id, kind_id: kindId })),
      { onConflict: "activiteit_id,kind_id" },
    );
    if (error) terug(pad, error.message, true);
  }

  terug(pad, "Aangepast.");
}

export async function pasActiviteitAan(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const naam = String(formData.get("naam") || "").trim();
  const soort = String(formData.get("soort") || "kamp").trim() || "kamp";
  const datum = String(formData.get("datum") || "").trim();
  const plaats = String(formData.get("plaats") || "").trim();
  const factuurregel = String(formData.get("factuurregel") || "").trim();
  const prijs = String(formData.get("prijs") || "").trim().replace(",", ".");
  const pad = `/beheer/activiteiten/${id}`;

  if (!naam) terug(pad, "Geef de activiteit een naam.", true);
  if (prijs && !Number.isFinite(Number(prijs)))
    terug(pad, "De prijs is geen bedrag.", true);

  const { error } = await db
    .from("activiteiten")
    .update({
      naam,
      soort,
      datum: datum || null,
      plaats: plaats || null,
      factuurregel: factuurregel || null,
      prijs: prijs ? Number(prijs) : null,
    })
    .eq("id", id);

  if (error) terug(pad, error.message, true);
  terug(pad, "Aangepast.");
}

/*
  Een wekelijkse les is elke week dezelfde activiteit op een andere datum.

  Zonder dit zou Kim vijf keer hetzelfde formulier invullen, en dan nog eens
  bij elk van die vijf dagen de kinderen aanduiden. Daarom: één keer invullen
  en zeggen hoeveel weken het doorgaat. De factuurregel en de prijs gaan mee,
  anders staan de dagen van dezelfde reeks straks onder verschillende regels
  op de factuur.
*/
export async function herhaalActiviteit(formData: FormData) {
  const db = await admin();
  const id = String(formData.get("id") || "");
  const keren = Number(formData.get("keren") || 0);
  const metKinderen = String(formData.get("kinderen") || "") === "ja";
  const pad = `/beheer/activiteiten/${id}`;

  if (!Number.isInteger(keren) || keren < 1 || keren > 20)
    terug(pad, "Kies tussen 1 en 20 keer.", true);

  const { data: bron, error: leesfout } = await db
    .from("activiteiten")
    .select("naam, soort, datum, plaats, factuurregel, prijs")
    .eq("id", id)
    .maybeSingle();

  if (leesfout) terug(pad, leesfout.message, true);
  if (!bron) terug(pad, "Deze activiteit bestaat niet meer.", true);
  if (!bron.datum)
    terug(
      pad,
      "Zet eerst een datum op deze activiteit, anders weet ik niet vanaf wanneer.",
      true,
    );

  /* De datums tellen we in UTC op, zodat een zomeruur geen dag opschuift. */
  const start = new Date(`${bron.datum}T00:00:00Z`);
  const nieuwe = Array.from({ length: keren }, (_, i) => {
    const dag = new Date(start.getTime());
    dag.setUTCDate(dag.getUTCDate() + 7 * (i + 1));
    return {
      naam: bron.naam,
      soort: bron.soort,
      datum: dag.toISOString().slice(0, 10),
      plaats: bron.plaats,
      factuurregel: bron.factuurregel,
      prijs: bron.prijs,
    };
  });

  const { data: gemaakt, error } = await db
    .from("activiteiten")
    .insert(nieuwe)
    .select("id");

  if (error) terug(pad, error.message, true);

  if (metKinderen && gemaakt?.length) {
    const { data: deelnames } = await db
      .from("deelnames")
      .select("kind_id")
      .eq("activiteit_id", id);
    const kinderen = (deelnames ?? []) as { kind_id: string }[];
    if (kinderen.length) {
      const rijen = gemaakt.flatMap((activiteit: { id: string }) =>
        kinderen.map((kind) => ({
          activiteit_id: activiteit.id,
          kind_id: kind.kind_id,
        })),
      );
      const { error: koppelfout } = await db
        .from("deelnames")
        .upsert(rijen, { onConflict: "activiteit_id,kind_id" });
      if (koppelfout) terug(pad, koppelfout.message, true);
    }
  }

  terug(
    "/beheer/activiteiten",
    `${keren} ${keren === 1 ? "dag" : "dagen"} erbij gezet.`,
  );
}

/*
  De aanwezigheid van één kind op één dag.

  Dit mag ook een begeleider doen, niet enkel Kim: "kan ik dan ergens de
  aanwezigheden aanduiden of de begeleiders". Daarom requireStaff en niet
  requireBeheerder. Het scherm van het team staat op /team/aanwezigheden, dat
  van Kim bij de activiteit zelf; `terug` zegt waar de knop stond, en we
  controleren die waarde zodat er niemand een ander adres in kan schuiven.
*/
export async function zetAanwezig(formData: FormData) {
  await requireStaff();
  const db = createAdminClient();
  const activiteitId = String(formData.get("activiteit_id") || "");
  const kindId = String(formData.get("kind_id") || "");
  const waarde = String(formData.get("waarde") || "");
  const gevraagd = String(formData.get("terug") || "");

  const pad = gevraagd.startsWith("/team/aanwezigheden/")
    ? gevraagd
    : `/beheer/activiteiten/${activiteitId}`;

  const aanwezig =
    waarde === "ja" ? true : waarde === "nee" ? false : null;

  const { error } = await db
    .from("deelnames")
    .update({ aanwezig })
    .eq("activiteit_id", activiteitId)
    .eq("kind_id", kindId);

  if (error) terug(pad, error.message, true);
  revalidatePath(pad);
  redirect(pad);
}

/* Alles in één keer op aanwezig zetten: op een gewone les is dat de regel, en
   dan hoeft er enkel nog afgevinkt te worden wie er niet was. */
export async function alleAanwezig(formData: FormData) {
  await requireStaff();
  const db = createAdminClient();
  const activiteitId = String(formData.get("activiteit_id") || "");
  const gevraagd = String(formData.get("terug") || "");
  const pad = gevraagd.startsWith("/team/aanwezigheden/")
    ? gevraagd
    : `/beheer/activiteiten/${activiteitId}`;

  const { error } = await db
    .from("deelnames")
    .update({ aanwezig: true })
    .eq("activiteit_id", activiteitId)
    .is("aanwezig", null);

  if (error) terug(pad, error.message, true);
  revalidatePath(pad);
  redirect(pad);
}
