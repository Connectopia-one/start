"use server";

import { revalidatePath } from "next/cache";
import { requireIngelogd } from "@/lib/auth";
import { zoekPlusklasCode } from "@/lib/plusklas";
import { createAdminClient } from "@/lib/supabase/admin";
import { heeftVolledigeToegang } from "@/lib/toegang";

/*
  Twee dingen die hier misliepen (gemeld op 29 september 2026):

  1. Laadde de pagina traag, dan klikten mensen nog eens op Toevoegen, en
     nog eens. Elke klik maakte een nieuw kind aan. Daarom kijkt maakKind nu
     eerst of er al een kind met diezelfde naam in dit gezin staat, en doet
     het dan niets meer. De knop zelf gaat intussen ook op slot, zie
     KinderenLijst.tsx, maar die slotknop alleen is niet genoeg: een tweede
     tabblad of een trage herlaadbeurt komt er langs.

  2. Er was helemaal geen manier om een kind weer weg te halen.

  3. (9 oktober 2026) Een gezin had zijn toegangscode ingetikt als de naam
     van zijn kind. Het stond er dus als "1 kind: TOPTESTER2026", zonder
     toegang, want de code was nooit als code gebruikt. Daarom kijkt maakKind
     nu eerst of de naam toevallig een geldige code is. Is dat zo, dan maken
     we geen kind aan maar gebruiken we de code waarvoor ze bedoeld was, en
     zeggen we dat ook. Een knop die op slot gaat is nooit genoeg: zet er ook
     een controle op de server naast.
*/

function zelfdeNaam(a: string, b: string) {
  return a.trim().toLowerCase() === b.trim().toLowerCase();
}

export async function maakKind(
  formData: FormData,
): Promise<{ fout?: string; melding?: string }> {
  const session = await requireIngelogd();
  const naam = String(formData.get("naam") || "").trim();
  if (!naam) return { fout: "Geef een naam op voor je kind." };

  const admin = createAdminClient();

  // Is deze "naam" in werkelijkheid een toegangscode? Dan is dat wat de
  // ouder bedoelde, en niet een kind dat zo heet.
  const code = await zoekPlusklasCode(naam);
  if (code) {
    if (heeftVolledigeToegang(session.profile)) {
      return {
        melding:
          `${code} is je toegangscode en geen naam. Je toegang stond al open, ` +
          `dus je hoeft er niets mee te doen. Vul hier de naam van je kind in.`,
      };
    }
    const { error: codefout } = await admin
      .from("profiles")
      .update({ is_plusklas: true, plusklas_code: code })
      .eq("id", session.userId);
    if (codefout)
      return {
        fout: `${code} is je toegangscode, geen naam. We konden ze niet bewaren, probeer het nog eens.`,
      };
    revalidatePath("/account");
    return {
      melding:
        `${code} is je toegangscode en geen naam van een kind. We hebben ze nu ` +
        `voor je gebruikt, dus al je hoofdstukken staan open. Vul hier de naam ` +
        `van je kind in.`,
    };
  }

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

/*
  De voortgangsbalk bij de oefeningen, aan of uit per kind.

  Gemeld door een ouder op 29 september 2026: hetzelfde scherm gaf bij haar
  ene kind rust (geen balk, geen aantal in zicht) en bij het andere frustratie
  (het wou net weten hoe ver het al was). Daarom kiest de ouder het per kind.

  profile_id staat er bewust bij: zo kan niemand aan het kind van een ander.
*/
export async function zetVoortgangsbalk(
  formData: FormData,
): Promise<{ fout?: string }> {
  const session = await requireIngelogd();
  const kindId = String(formData.get("kind_id") || "");
  const aan = String(formData.get("aan") || "") === "ja";
  if (!kindId) return { fout: "Geen kind gekozen." };

  const admin = createAdminClient();
  const { error } = await admin
    .from("kinderen")
    .update({ toon_voortgang: aan })
    .eq("id", kindId)
    .eq("profile_id", session.userId);
  if (error) return { fout: "Kon dit niet bewaren, probeer opnieuw." };

  revalidatePath("/account");
  return {};
}
