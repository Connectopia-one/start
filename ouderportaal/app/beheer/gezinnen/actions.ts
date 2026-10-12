"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient, kolomOntbreekt } from "@/lib/supabase/admin";
import { ficheUitFormulier } from "@/lib/fiche";

export async function maakGezin(formData: FormData) {
  await requireBeheerder();

  const fullName = String(formData.get("naam") || "").trim();
  const email = String(formData.get("email") || "").trim();
  const password = String(formData.get("wachtwoord") || "");

  if (!fullName || !email || password.length < 8) {
    redirect(
      "/beheer/gezinnen?fout=" +
        encodeURIComponent("Vul naam en e-mailadres in; wachtwoord moet minstens 8 tekens hebben.")
    );
  }

  const admin = createAdminClient();
  const { data: created, error } = await admin.auth.admin.createUser({
    email,
    password,
    email_confirm: true,
  });

  if (error || !created?.user) {
    redirect("/beheer/gezinnen?fout=" + encodeURIComponent(error?.message || "Aanmaken account mislukt."));
  }

  const { error: profileError } = await admin
    .from("profiles")
    .insert({ id: created.user.id, full_name: fullName, role: "ouder" });

  if (profileError) {
    redirect("/beheer/gezinnen?fout=" + encodeURIComponent(profileError.message));
  }

  revalidatePath("/beheer/gezinnen");
  redirect(`/beheer/gezinnen/${created.user.id}?succes=` + encodeURIComponent("Account aangemaakt."));
}

export async function upsertToegang(formData: FormData) {
  await requireBeheerder();

  const profileId = String(formData.get("profile_id") || "");
  const klasjeId = String(formData.get("klasje_id") || "");
  const materiaal = formData.get("materiaal") === "on";
  const fotos = formData.get("fotos") === "on";

  const admin = createAdminClient();

  if (!materiaal && !fotos) {
    await admin.from("toegang").delete().eq("profile_id", profileId).eq("klasje_id", klasjeId);
  } else {
    await admin
      .from("toegang")
      .upsert({ profile_id: profileId, klasje_id: klasjeId, materiaal, fotos }, { onConflict: "profile_id,klasje_id" });
  }

  revalidatePath(`/beheer/gezinnen/${profileId}`);
}

export async function wijzigWachtwoord(formData: FormData) {
  await requireBeheerder();

  const profileId = String(formData.get("profile_id") || "");
  const wachtwoord = String(formData.get("wachtwoord") || "");

  if (wachtwoord.length < 8) {
    redirect(
      `/beheer/gezinnen/${profileId}?fout=` + encodeURIComponent("Wachtwoord moet minstens 8 tekens hebben.")
    );
  }

  const admin = createAdminClient();
  const { error } = await admin.auth.admin.updateUserById(profileId, { password: wachtwoord });
  if (error) {
    redirect(`/beheer/gezinnen/${profileId}?fout=` + encodeURIComponent(error.message));
  }

  redirect(`/beheer/gezinnen/${profileId}?succes=` + encodeURIComponent("Nieuw wachtwoord ingesteld."));
}

export async function verwijderGezin(formData: FormData) {
  await requireBeheerder();
  const profileId = String(formData.get("profile_id") || "");

  const admin = createAdminClient();
  await admin.auth.admin.deleteUser(profileId);

  revalidatePath("/beheer/gezinnen");
  redirect("/beheer/gezinnen?succes=" + encodeURIComponent("Account verwijderd."));
}

/*
  De inlichtingenfiche aanpassen vanuit Beheer.

  Tot 12 oktober 2026 kon dat enkel via "Bekijk het portaal zoals dit gezin het
  ziet": het beheerscherm toonde de fiche, maar om er iets in te veranderen
  moest je eerst meekijken met dat gezin. Kim liep daar op vast, en erger: ze
  vulde de fiche van haar zoon in op haar eigen beheerdersaccount, want dat is
  wat "Mijn gezin" toont als je als beheerder inlogt. Zie
  connectopia-kim-twee-accounts in het geheugen.

  Daarom staan deze twee acties hier. Ze bewaren bij het gezin dat in het
  formulier staat, niet bij wie ingelogd is, en enkel een beheerder mag ze
  aanroepen.
*/
function terugNaarGezin(gezinId: string, bericht: string, fout = false): never {
  revalidatePath(`/beheer/gezinnen/${gezinId}`);
  redirect(
    `/beheer/gezinnen/${gezinId}?${fout ? "fout" : "succes"}=` +
      encodeURIComponent(bericht),
  );
}

export async function wijzigKindAlsBeheerder(formData: FormData) {
  await requireBeheerder();
  const gezinId = String(formData.get("gezin_id") || "");
  const kindId = String(formData.get("kind_id") || "");
  const fiche = ficheUitFormulier(formData);

  if (!gezinId || !kindId) {
    redirect(
      "/beheer/gezinnen?fout=" +
        encodeURIComponent("We weten niet bij welk gezin deze fiche hoort."),
    );
  }
  if (!fiche.naam) {
    terugNaarGezin(gezinId, "De naam mag niet leeg zijn.", true);
  }

  const admin = createAdminClient();
  /* .select() erachter, zodat een update die geen enkele rij raakte niet op
     een geslaagde lijkt. */
  const { data: aangepast, error } = await admin
    .from("kinderen")
    .update({ ...fiche, updated_at: new Date().toISOString() })
    .eq("id", kindId)
    .eq("profile_id", gezinId)
    .select("id");

  if (error) {
    terugNaarGezin(
      gezinId,
      `De fiche van ${fiche.naam} is niet bewaard: ${kolomOntbreekt(error, "supabase/inlichtingenfiche.sql") || error.message}`,
      true,
    );
  }
  if (!aangepast || aangepast.length === 0) {
    terugNaarGezin(
      gezinId,
      `De fiche van ${fiche.naam} is niet bewaard: dit kind hoort niet bij dit gezin. Laad de bladzijde opnieuw.`,
      true,
    );
  }
  terugNaarGezin(gezinId, `De fiche van ${fiche.naam} is bewaard.`);
}

export async function voegKindToeAlsBeheerder(formData: FormData) {
  await requireBeheerder();
  const gezinId = String(formData.get("gezin_id") || "");
  const fiche = ficheUitFormulier(formData);

  if (!gezinId) {
    redirect(
      "/beheer/gezinnen?fout=" +
        encodeURIComponent("We weten niet bij welk gezin dit kind hoort."),
    );
  }
  if (!fiche.naam) {
    terugNaarGezin(gezinId, "Vul de naam van het kind in.", true);
  }

  const admin = createAdminClient();

  /* Twee keer klikken mag geen twee kinderen opleveren. */
  const { data: bestaande } = await admin
    .from("kinderen")
    .select("naam")
    .eq("profile_id", gezinId);
  const alGekend = (bestaande ?? []).some(
    (k: { naam: string }) =>
      k.naam.trim().toLowerCase() === fiche.naam.toLowerCase(),
  );
  if (alGekend) {
    terugNaarGezin(gezinId, `${fiche.naam} stond er al bij dit gezin.`);
  }

  const { error } = await admin
    .from("kinderen")
    .insert({ profile_id: gezinId, ...fiche });

  if (error) {
    terugNaarGezin(
      gezinId,
      `${fiche.naam} is niet toegevoegd: ${kolomOntbreekt(error, "supabase/inlichtingenfiche.sql") || error.message}`,
      true,
    );
  }
  terugNaarGezin(gezinId, `${fiche.naam} is toegevoegd.`);
}
