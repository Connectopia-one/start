"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { MET_DE_HAND } from "@/lib/aanvraaglijsten";

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

function terug(bericht: string, fout = false): never {
  revalidatePath("/beheer/aanvragen/lijsten");
  redirect(
    `/beheer/aanvragen/lijsten?${fout ? "fout" : "succes"}=${encodeURIComponent(bericht)}`,
  );
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

  terug(
    `${kind} staat erbij, op ${dagen.length === 1 ? "1 lijst" : `${dagen.length} lijsten`}.`,
  );
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
