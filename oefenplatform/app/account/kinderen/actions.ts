"use server";

import { revalidatePath } from "next/cache";
import { requireIngelogd } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Twee dingen die hier misliepen (gemeld op 29 september 2026):

  1. Laadde de pagina traag, dan klikten mensen nog eens op Toevoegen, en
     nog eens. Elke klik maakte een nieuw kind aan. Daarom kijkt maakKind nu
     eerst of er al een kind met diezelfde naam in dit gezin staat, en doet
     het dan niets meer. De knop zelf gaat intussen ook op slot, zie
     KinderenLijst.tsx, maar die slotknop alleen is niet genoeg: een tweede
     tabblad of een trage herlaadbeurt komt er langs.

  2. Er was helemaal geen manier om een kind weer weg te halen.
*/

function zelfdeNaam(a: string, b: string) {
  return a.trim().toLowerCase() === b.trim().toLowerCase();
}

export async function maakKind(formData: FormData): Promise<{ fout?: string }> {
  const session = await requireIngelogd();
  const naam = String(formData.get("naam") || "").trim();
  if (!naam) return { fout: "Geef een naam op voor je kind." };

  const admin = createAdminClient();

  const { data: bestaande, error: leesfout } = await admin
    .from("kinderen")
    .select("id, naam")
    .eq("profile_id", session.userId);
  if (leesfout)
    return { fout: "Kon je kinderen niet nakijken, probeer opnieuw." };

  if ((bestaande ?? []).some((k) => zelfdeNaam(k.naam, naam))) {
    revalidatePath("/account");
    return {};
  }

  const { error } = await admin
    .from("kinderen")
    .insert({ profile_id: session.userId, naam });
  if (error) return { fout: "Kon je kind niet toevoegen, probeer opnieuw." };

  revalidatePath("/account");
  return {};
}

export async function verwijderKind(
  formData: FormData,
): Promise<{ fout?: string }> {
  const session = await requireIngelogd();
  const kindId = String(formData.get("kind_id") || "");
  if (!kindId) return { fout: "Geen kind gekozen." };

  // profile_id staat er bewust bij: zo kan niemand het kind van een ander wissen.
  const admin = createAdminClient();
  const { error } = await admin
    .from("kinderen")
    .delete()
    .eq("id", kindId)
    .eq("profile_id", session.userId);
  if (error) return { fout: "Kon dit kind niet verwijderen, probeer opnieuw." };

  revalidatePath("/account");
  return {};
}
