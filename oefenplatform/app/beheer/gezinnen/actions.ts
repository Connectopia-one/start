"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/**
 * Zet de gratis volledige toegang van één gezin aan of uit (het veld
 * is_plusklas op het profiel).
 *
 * Nodig omdat een plusklas-code niets meer met een account te maken heeft
 * zodra hij gebruikt is: de code uitzetten houdt alleen nieuwe mensen tegen.
 * Zonder dit scherm bleef een testgezin dus voor altijd alles zien.
 *
 * Toegang uitzetten raakt niets van wat het gezin opgebouwd heeft: de
 * kinderen, hun voortgang en hun stickers hangen aan het kind, niet aan de
 * toegang. Ze zien daarna enkel nog de gratis hoofdstukken, en wie later weer
 * toegang krijgt, pikt op waar hij gestopt was.
 */
export async function zetVolledigeToegang(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const aan = formData.get("aan") === "ja";
  if (!id) redirect("/beheer/gezinnen");

  const admin = createAdminClient();
  const { error } = await admin
    .from("profiles")
    .update({ is_plusklas: aan })
    .eq("id", id);
  if (error) {
    redirect(
      "/beheer/gezinnen?fout=" +
        encodeURIComponent(`De toegang aanpassen lukte niet: ${error.message}`)
    );
  }

  revalidatePath("/beheer/gezinnen");
  redirect(
    "/beheer/gezinnen?melding=" +
      encodeURIComponent(
        aan ? "De volledige toegang staat aan." : "De volledige toegang staat uit."
      )
  );
}
