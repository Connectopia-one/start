"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder, requireStaff } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { KINDVELDEN, lijstZin, watOntbreekt, type Kind } from "@/lib/kind";
import { ficheUitFormulier } from "@/lib/fiche";
import { noteerAfgezegd } from "@/lib/afzeggen";

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

/*
  Eén of meer kinderen die al in het ouderportaal staan op een lijst zetten.
  Het formulier op de lijst stuurt elk aangevinkt kind mee als kind_id. Een
  kind waarvan de fiche nog niet in orde is, mag er gewoon bij; we zeggen het
  er enkel bij, zodat Kim weet bij wie ze nog moet aandringen.
*/
export async function voegKindToe(formData: FormData) {
  const db = await admin();
  const activiteitId = String(formData.get("activiteit_id") || "");
  const kindIds = [
    ...new Set(formData.getAll("kind_id").map(String).filter(Boolean)),
  ];
  const pad = `/beheer/activiteiten/${activiteitId}`;

  if (kindIds.length === 0) terug(pad, "Vink eerst een kind aan.", true);

  /* Twee keer hetzelfde kind toevoegen mag gewoon niets doen; de sleutel van
     de tabel is (activiteit, kind). */
  const { error } = await db.from("deelnames").upsert(
    kindIds.map((kind_id) => ({ activiteit_id: activiteitId, kind_id })),
    { onConflict: "activiteit_id,kind_id" },
  );
  if (error) terug(pad, error.message, true);

  const { data } = await db
    .from("kinderen")
    .select(KINDVELDEN)
    .in("id", kindIds);
  const kinderen = (data ?? []) as unknown as Kind[];
  const zonderFiche = kinderen
    .filter((k) => watOntbreekt(k).length > 0)
    .map((k) => k.naam);

  let bericht =
    kindIds.length === 1
      ? `${kinderen[0]?.naam ?? "Het kind"} staat op de lijst.`
      : `${kindIds.length} kinderen staan op de lijst.`;
  if (zonderFiche.length) {
    bericht += ` Let op: de fiche van ${lijstZin(zonderFiche)} is nog niet in orde.`;
  }
  terug(pad, bericht);
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

  /* Ook bij de inschrijvingen van die dag als afgezegd noteren, anders
     stelt deze pagina meteen voor om het kind er terug bij te zetten. */
  const { data: activiteit } = await db
    .from("activiteiten")
    .select("naam")
    .eq("id", activiteitId)
    .maybeSingle();
  const naam = (activiteit as { naam: string } | null)?.naam;
  const afgezegd = naam ? await noteerAfgezegd(db, naam, kindId) : 0;

  terug(
    pad,
    afgezegd
      ? "Kind van de lijst gehaald, en bij de inschrijvingen van deze dag als afgezegd genoteerd."
      : "Kind van de lijst gehaald.",
  );
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

/*
  Een ingeschreven kind zonder fiche toch op de kamplijst zetten.

  Kim op 2 november 2026, de ochtend van het herfstkamp: "ik zou de kinderen
  wel willen kunnen aanvinken als ze zo staan dat we hun aanwezigheid wel
  kunnen registreren maar de ouders op die moment rechtstreeks ook het laten
  invullen als ze het nog niet gedaan hebben. dus een lege fiche erbij
  plaatsen".

  Heeft het gezin al een account (profile_id), dan komt het kind daarbij.
  Zo niet, dan maken we het account, met het mailadres van de inschrijving
  en het wachtwoord dat Kim zelf intypt. Het wachtwoord staat nergens in de
  code: deze code is openbaar.
*/
export async function zetZonderFicheErop(formData: FormData) {
  const db = await admin();
  const activiteitId = String(formData.get("activiteit_id") || "");
  const pad = `/beheer/activiteiten/${activiteitId}`;
  const naam = String(formData.get("naam") || "").trim();
  let profileId = String(formData.get("profile_id") || "");

  if (!naam) terug(pad, "De naam van het kind ontbreekt.", true);

  if (!profileId) {
    const ouder = String(formData.get("ouder") || "").trim();
    const email = String(formData.get("email") || "").trim();
    const wachtwoord = String(formData.get("wachtwoord") || "");
    const gsm = String(formData.get("gsm") || "").trim();
    if (!ouder || !email)
      terug(pad, `Vul de naam en het mailadres van de ouder van ${naam} in.`, true);
    if (wachtwoord.length < 8)
      terug(pad, "Het wachtwoord moet minstens 8 tekens hebben.", true);

    const { data: gemaakt, error } = await db.auth.admin.createUser({
      email,
      password: wachtwoord,
      email_confirm: true,
    });
    if (error || !gemaakt?.user)
      terug(
        pad,
        `Het account voor ${email} lukte niet: ${error?.message ?? "onbekende fout"}`,
        true,
      );
    profileId = gemaakt.user.id;
    const { error: profielFout } = await db
      .from("profiles")
      .insert({
        id: profileId,
        full_name: ouder,
        role: "ouder",
        telefoon: gsm || null,
      });
    if (profielFout) terug(pad, profielFout.message, true);
  }

  /* Staat er bij dat gezin al een kind met die naam, dan nemen we dat. */
  const { data: bestaand } = await db
    .from("kinderen")
    .select("id, naam")
    .eq("profile_id", profileId);
  let kindId = ((bestaand ?? []) as { id: string; naam: string }[]).find(
    (k) => k.naam.trim().toLowerCase() === naam.toLowerCase(),
  )?.id;
  if (!kindId) {
    const { data: nieuw, error } = await db
      .from("kinderen")
      .insert({ profile_id: profileId, naam })
      .select("id")
      .single();
    if (error || !nieuw) terug(pad, error?.message ?? "Het kind kon niet bewaard worden.", true);
    kindId = (nieuw as { id: string }).id;
  }

  const { error } = await db
    .from("deelnames")
    .upsert(
      { activiteit_id: activiteitId, kind_id: kindId },
      { onConflict: "activiteit_id,kind_id" },
    );
  if (error) terug(pad, error.message, true);
  terug(pad, `${naam} staat op de lijst, met een lege fiche om in te vullen.`);
}

/* De fiche invullen vanop de kamplijst, en daarna terug naar die lijst. */
export async function bewaarFicheOpLijst(formData: FormData) {
  const db = await admin();
  const activiteitId = String(formData.get("activiteit_id") || "");
  const kindId = String(formData.get("kind_id") || "");
  const pad = `/beheer/activiteiten/${activiteitId}`;
  const fiche = ficheUitFormulier(formData);
  if (!fiche.naam) terug(pad, "De naam mag niet leeg zijn.", true);

  const { data, error } = await db
    .from("kinderen")
    .update({ ...fiche, updated_at: new Date().toISOString() })
    .eq("id", kindId)
    .select("id");
  if (error) terug(pad, `De fiche van ${fiche.naam} is niet bewaard: ${error.message}`, true);
  if (!data || data.length === 0)
    terug(pad, `De fiche van ${fiche.naam} is niet bewaard. Laad de bladzijde opnieuw.`, true);
  terug(pad, `De fiche van ${fiche.naam} is bewaard.`);
}
