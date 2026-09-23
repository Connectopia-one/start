"use server";

import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Een account de rol "begeleider" geven of weer afnemen. Enkel jij als
  beheerder kan dit. Je kan met dit scherm géén beheerder maken of afzetten —
  dat blijft iets voor de SQL Editor, zodat niemand zichzelf per ongeluk
  buitensluit of alle rechten geeft.
*/
export async function zetRol(formData: FormData) {
  const session = await requireBeheerder();

  const id = String(formData.get("id") || "");
  const nieuweRol = String(formData.get("rol") || "");
  if (!id || (nieuweRol !== "ouder" && nieuweRol !== "begeleider")) return;
  if (id === session.userId) return;

  const admin = createAdminClient();

  /* Nooit een beheerder overschrijven. */
  const { data: huidig } = await admin
    .from("profiles")
    .select("role")
    .eq("id", id)
    .single();
  if (!huidig || huidig.role === "beheerder") return;

  const { error } = await admin
    .from("profiles")
    .update({ role: nieuweRol })
    .eq("id", id);
  if (error) throw new Error(error.message);

  revalidatePath("/beheer/begeleiders");
}
