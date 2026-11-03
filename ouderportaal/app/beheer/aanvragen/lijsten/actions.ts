"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import {
  AFGEZEGD,
  MET_DE_HAND,
  afgezegdVoor,
  gaatOverEenKind,
  maakGroepen,
  vindWaarde,
  type Aanvraag,
} from "@/lib/aanvraaglijsten";
import { datumUitNaam, plaatsUitNaam, zoekKind } from "@/lib/kindzoeken";
import { portaalKinderen } from "@/lib/portaalkinderen";
import { zetStapVoorGezin } from "@/lib/aanvraagstap-bewaren";
import { KINDVELDEN, lijstZin, watOntbreekt, type Kind } from "@/lib/kind";

/*
  Een kind met de hand op een kamplijst zetten.

  Kim op 28 oktober 2026: "er zijn kinderen die van de plusklas willen
  inschrijven en kinderen die extra willen komen dus daan is ingeschreven in
  hasselt maar gaat ook naar herfstkamp genk komen. Ellena komt ook alle
  dagen" en "ik moet hier ook dus handmatig kinderen kunnen extra erin
  zetten".

  Zo'n kind komt in dezelfde tabel als de inschrijvingen van de website, met
  dezelfde vragen als sleutel en "ja" bij elke aangekruiste dag. Zo telt de
  lijst het mee zonder dat er een tabel of een SQL-bestand bij moet. De soort
  "met de hand" houdt het uit elkaar met wat een ouder zelf invulde.
*/

function terug(bericht: string, fout = false, pad = "/beheer/aanvragen/lijsten"): never {
  revalidatePath("/beheer/aanvragen/lijsten");
  if (pad !== "/beheer/aanvragen/lijsten") revalidatePath(pad);
  redirect(`${pad}?${fout ? "fout" : "succes"}=${encodeURIComponent(bericht)}`);
}

const VELDEN = [
  ["kind", "Naam van het kind"],
  ["leeftijd", "Leeftijd van het kind"],
  ["ouder", "Naam van de ouders"],
  ["gemeente", "Gemeente"],
  ["gsm", "Gsm-nummer"],
  ["mail", "E-mailadres"],
  ["boodschap", "Vraag of boodschap"],
] as const;

export async function voegKindToe(formData: FormData) {
  await requireBeheerder();
  const tekst = (naam: string) => String(formData.get(naam) ?? "").trim();

  const kind = tekst("kind");
  if (!kind) terug("Vul de naam van het kind in.", true);

  const dagen = formData
    .getAll("dag")
    .map((d) => String(d).trim())
    .filter(Boolean);
  const nieuw = tekst("nieuwe_dag");
  if (nieuw) dagen.push(nieuw);
  if (dagen.length === 0) terug("Vink minstens één dag aan.", true);

  const gegevens: Record<string, string> = {};
  for (const [veld, vraag] of VELDEN) {
    const waarde = tekst(veld);
    if (waarde) gegevens[vraag] = waarde;
  }
  for (const dag of dagen) gegevens[dag] = "ja";

  /* Hetzelfde onderwerp als de inschrijvingen van die dag, zodat het kind
     ook blijft staan als je bovenaan op één soort filtert. */
  const onderwerp =
    tekst(`onderwerp:${dagen[0]}`) || "Met de hand op een lijst gezet";

  const db = createAdminClient();
  const { error } = await db.from("aanvragen").insert({
    onderwerp,
    soort: MET_DE_HAND,
    gegevens,
    gezien: true,
    afgehandeld: true,
  });
  if (error) terug(error.message, true);

  let bericht = `${kind} staat erbij, op ${dagen.length === 1 ? "1 lijst" : `${dagen.length} lijsten`}.`;

  /* Gekozen uit de kinderen van het ouderportaal: zeg erbij als de fiche
     nog niet in orde is. */
  const kindId = tekst("kind_id");
  if (kindId) {
    const { data: rij } = await db
      .from("kinderen")
      .select(KINDVELDEN)
      .eq("id", kindId)
      .maybeSingle();
    const ontbreekt = rij ? watOntbreekt(rij as unknown as Kind) : [];
    if (ontbreekt.length) {
      bericht += ` Let op: de fiche is nog niet in orde, nog nodig is ${lijstZin(ontbreekt)}.`;
    }
  }

  terug(bericht);
}

/* Enkel wat met de hand toegevoegd is, kan hier weg. Een echte inschrijving
   verwijder je bij Alle aanvragen, waar je ziet wat je weggooit. */
export async function verwijderKind(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") ?? "");
  const db = createAdminClient();
  const { error } = await db
    .from("aanvragen")
    .delete()
    .eq("id", id)
    .eq("soort", MET_DE_HAND);
  if (error) terug(error.message, true);
  terug("Het kind staat niet meer op de lijsten.");
}

/*
  Een kind dat niet komt, van één kampdag halen, of het terugzetten.

  Kim op 3 november 2026: "ik kan geen kinderen van een lijst doen van een
  kamp, ik kan nu olivia en juliette niet verwijderen die afgezegd hebben".
  De inschrijving blijft staan; er komt enkel "Afgezegd voor <dag>" bij met
  de naam (zie lib/aanvraaglijsten.ts). Stond het kind voor die dag al bij
  Kampen en lessen, dan gaat het daar ook af, anders zet "Fiches van deze
  dag afdrukken" het er niet terug op, maar zit het wel nog op het blad.
*/
export async function zegAf(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") ?? "");
  const dag = String(formData.get("dag") ?? "").trim();
  const kind = String(formData.get("kind") ?? "").trim();
  const terugzetten = String(formData.get("terug") ?? "") === "ja";
  /* Van waar er geklikt werd: de lijsten, of een kamp bij Kampen en lessen. */
  const gevraagdPad = String(formData.get("pad") ?? "");
  const pad = /^\/beheer\/activiteiten\/[\w-]+$/.test(gevraagdPad)
    ? gevraagdPad
    : "/beheer/aanvragen/lijsten";
  if (!id || !dag || !kind) terug("Er ontbreekt iets om af te zeggen.", true, pad);

  const db = createAdminClient();
  const { data, error } = await db
    .from("aanvragen")
    .select("id, onderwerp, soort, gegevens, gezien, afgehandeld, created_at")
    .eq("id", id)
    .maybeSingle();
  if (error || !data) terug(error?.message ?? "Die inschrijving is niet gevonden.", true, pad);
  const aanvraag = data as Aanvraag;

  const zelfde = (n: string) => n.toLowerCase() === kind.toLowerCase();
  const namen = afgezegdVoor(aanvraag, dag).filter((n) => !zelfde(n));
  if (!terugzetten) namen.push(kind);

  const gegevens = { ...aanvraag.gegevens };
  if (namen.length) gegevens[AFGEZEGD + dag] = namen.join(", ");
  else delete gegevens[AFGEZEGD + dag];

  const { error: bewaarFout } = await db
    .from("aanvragen")
    .update({ gegevens })
    .eq("id", id);
  if (bewaarFout) terug(bewaarFout.message, true, pad);

  if (terugzetten) {
    terug(`${kind} staat terug op ${dag}.`, false, pad);
  }

  /* Ook van de lijst bij Kampen en lessen, als die dag daar al staat. */
  let ookBijKampen = false;
  const { data: activiteit } = await db
    .from("activiteiten")
    .select("id")
    .eq("naam", dag)
    .eq("archief", false)
    .maybeSingle();
  if (activiteit) {
    const gevonden = zoekKind(
      kind,
      {
        gsm: vindWaarde(aanvraag.gegevens, "gsm"),
        mail: vindWaarde(aanvraag.gegevens, "mail"),
      },
      await portaalKinderen(),
    );
    if (gevonden) {
      const { error: weg } = await db
        .from("deelnames")
        .delete()
        .eq("activiteit_id", (activiteit as { id: string }).id)
        .eq("kind_id", gevonden.id);
      if (!weg) {
        ookBijKampen = true;
        revalidatePath(`/beheer/activiteiten/${(activiteit as { id: string }).id}`);
      }
    }
  }

  terug(
    `${kind} staat niet meer op ${dag}${ookBijKampen ? ", ook niet bij Kampen en lessen" : ""}. De inschrijving zelf blijft bewaard.`,
    false,
    pad,
  );
}

/*
  Een kampdag van deze lijsten naar Kampen en lessen zetten, met elk kind dat
  in het ouderportaal staat er al op. Kim op 2 november 2026: "kunnen de
  lijsten van de kampen niet automatisch hier bij kampen komen te staan".

  Twee keer klikken mag: de activiteit wordt op naam teruggevonden en een kind
  dat er al op staat, blijft er gewoon één keer op. Een kind dat niet in het
  ouderportaal staat, heeft geen fiche; dat toont de kamppagina zelf, onder
  de lijst, met de gegevens van de inschrijving.
*/
export async function naarKampen(formData: FormData) {
  await requireBeheerder();
  const gevraagd = String(formData.get("groep") ?? "");
  const db = createAdminClient();

  const [{ data: aanvraagData, error: fout }, portaal] = await Promise.all([
    db
      .from("aanvragen")
      .select("id, onderwerp, soort, gegevens, gezien, afgehandeld, created_at")
      .limit(1000),
    portaalKinderen(),
  ]);
  if (fout) terug(fout.message, true);

  const groepen = maakGroepen(
    ((aanvraagData ?? []) as Aanvraag[]).filter(gaatOverEenKind),
  ).filter((g) =>
    gevraagd ? g.naam === gevraagd : datumUitNaam(g.naam) !== null,
  );
  if (groepen.length === 0) terug("Er is geen kampdag gevonden.", true);

  const { data: bestaandData } = await db
    .from("activiteiten")
    .select("id, naam")
    .eq("archief", false);
  const bestaand = new Map(
    ((bestaandData ?? []) as { id: string; naam: string }[]).map((a) => [
      a.naam,
      a.id,
    ]),
  );

  let gekoppeld = 0;
  let zonder = 0;
  let laatste = "";
  for (const groep of groepen) {
    let id = bestaand.get(groep.naam);
    if (!id) {
      const { data: nieuw, error } = await db
        .from("activiteiten")
        .insert({
          naam: groep.naam,
          soort: "kamp",
          datum: datumUitNaam(groep.naam),
          plaats: plaatsUitNaam(groep.naam),
        })
        .select("id")
        .single();
      if (error || !nieuw) terug(error?.message ?? "Aanmaken lukte niet.", true);
      id = (nieuw as { id: string }).id;
    }
    laatste = id;

    const ids = new Set<string>();
    for (const rij of groep.rijen) {
      const kind = zoekKind(
        rij.kind,
        {
          gsm: vindWaarde(rij.aanvraag.gegevens, "gsm"),
          mail: vindWaarde(rij.aanvraag.gegevens, "mail"),
        },
        portaal,
      );
      if (kind) ids.add(kind.id);
      else zonder++;
    }
    if (ids.size) {
      const { error } = await db.from("deelnames").upsert(
        [...ids].map((kind_id) => ({ activiteit_id: id, kind_id })),
        { onConflict: "activiteit_id,kind_id" },
      );
      if (error) terug(error.message, true);
    }
    gekoppeld += ids.size;
  }

  const bericht =
    `${groepen.length === 1 ? groepen[0].naam + " staat" : groepen.length + " kampdagen staan"} bij Kampen en lessen, met ${gekoppeld} ${gekoppeld === 1 ? "kind" : "kinderen"} uit het ouderportaal.` +
    (zonder
      ? ` ${zonder} ${zonder === 1 ? "kind staat" : "kinderen staan"} niet in het ouderportaal en ${zonder === 1 ? "heeft" : "hebben"} dus geen fiche; die staan onderaan de kamplijst.`
      : "");

  const pad =
    groepen.length === 1 ? `/beheer/activiteiten/${laatste}` : "/beheer/activiteiten";
  revalidatePath(pad);
  redirect(`${pad}?succes=${encodeURIComponent(bericht)}`);
}

/*
  Betaald of nog te betalen, aangeklikt op de kamplijst. Kim op 2 november
  2026: "bij de kampen aanklikken wie betaald heeft en wie nog moet
  betalen". Het hele gezin (zelfde mededeling) gaat mee; zie
  lib/aanvraagstap-bewaren.ts.
*/
export async function zetBetaald(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") ?? "");
  const aan = String(formData.get("aan") ?? "") === "ja";
  const onderwerp = String(formData.get("onderwerp") ?? "");
  const { fout, aantal } = await zetStapVoorGezin(id, "betaald", aan);

  revalidatePath("/beheer/aanvragen/lijsten");
  revalidatePath("/beheer/aanvragen");
  const vraag = new URLSearchParams();
  if (onderwerp) vraag.set("onderwerp", onderwerp);
  if (fout) {
    vraag.set(
      "fout",
      /stappen/.test(fout)
        ? "Draai eerst website/supabase/aanvragen-status.sql in Supabase; daarna werkt betaald aanklikken."
        : fout,
    );
  } else {
    vraag.set(
      "succes",
      `${aan ? "Betaald" : "Terug op nog te betalen"}${
        aantal > 1 ? `, voor de ${aantal} kinderen met dezelfde mededeling` : ""
      }.`,
    );
  }
  redirect(`/beheer/aanvragen/lijsten?${vraag.toString()}`);
}
