"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requirePortaalSessie } from "@/lib/auth";
import { createAdminClient, kolomOntbreekt } from "@/lib/supabase/admin";
import { ficheUitFormulier } from "@/lib/fiche";

const PAD = "/portaal/gezin";

/*
  Elk scherm hier eindigt met een zin: "Bewaard" of wat er misging.

  Kim op 11 én op 12 oktober 2026: "ik heb al 3 x proberen de inlichtingsfiche
  in te vullen en dit wordt niet bewaard" en "zelfs mijn eigen fiche onthoudt
  die niet". Beide keren viel er niets te zien, want deze acties lazen de fout
  van Supabase niet uit en gaven ook bij een geslaagde bewaring niets terug.
  Een scherm dat er na het klikken exact hetzelfde uitziet, is niet te
  onderscheiden van een scherm dat niets gedaan heeft.

  Zie connectopia-fout-441 in het geheugen: een server action die stil mislukt,
  kost altijd meer tijd dan een lelijke foutmelding.
*/
/*
  Zet een fout van Supabase om in een zin die zegt wat Kim moet doen. Gaat het
  om een kolom die nog niet bestaat, dan is het sql-bestand niet gedraaid en
  helpt de naam van dat bestand meer dan de ruwe melding.
*/
function uitleg(fout: { message?: string; code?: string }): string {
  return (
    kolomOntbreekt(fout, "supabase/inlichtingenfiche.sql") ||
    fout.message ||
    "onbekende fout"
  );
}

function terug(bericht: string, fout = false): never {
  revalidatePath(PAD);
  redirect(`${PAD}?${fout ? "fout" : "succes"}=${encodeURIComponent(bericht)}`);
}

/*
  Bij welk gezin horen de gegevens van dit scherm?

  Normaal bij jezelf. Kijk je als beheerder mee met een gezin, dan toont het
  scherm de gegevens van dat gezin, en dan horen ze daar ook bewaard te worden.

  Hier stond eerst een slot: tijdens het meekijken wierp elke actie een fout.
  Dat was precies verkeerd om. Kim op 11 oktober 2026: "ik heb al 3 x proberen
  de inlichtingsfiche in te vullen en dit wordt niet bewaard." Een fout uit een
  server action komt niet als een zin op het scherm maar verdwijnt, dus het
  scherm deed gewoon niets, drie keer na elkaar. En er was geen andere weg:
  een kind toevoegen voor een gezin dat zijn fiche niet zelf invult kon
  nergens. Nu bewaart dit scherm bij het gezin waar je naar kijkt, en staat er
  bovenaan dat scherm dat dat zo is.

  De les: een actie die mag mislukken geeft een zin terug; een actie die niets
  hoort te doen hoort niet te bestaan. Zie ook lib/meekijken.ts.
*/
async function gezinVanDitScherm() {
  const sessie = await requirePortaalSessie();
  return sessie.userId;
}

export async function wijzigContactgegevens(formData: FormData) {
  const gezinId = await gezinVanDitScherm();
  const telefoon = String(formData.get("telefoon") || "").trim() || null;
  const adres = String(formData.get("adres") || "").trim() || null;

  const admin = createAdminClient();
  const { error } = await admin
    .from("profiles")
    .update({ telefoon, adres })
    .eq("id", gezinId);

  if (error) terug(`Je contactgegevens zijn niet bewaard: ${uitleg(error)}`, true);
  terug("Je contactgegevens zijn bewaard.");
}

export async function voegKindToe(formData: FormData) {
  const gezinId = await gezinVanDitScherm();
  const fiche = ficheUitFormulier(formData);
  if (!fiche.naam) {
    terug("Vul de naam van je kind in, de rest mag leeg blijven.", true);
  }

  const admin = createAdminClient();

  // Klikt iemand twee keer op Toevoegen omdat de pagina traag laadt, dan zou
  // hetzelfde kind er twee keer in komen. Staat die naam er al, dan doen we niets.
  const { data: bestaande } = await admin
    .from("kinderen")
    .select("naam")
    .eq("profile_id", gezinId);
  const alGekend = (bestaande ?? []).some(
    (k: { naam: string }) =>
      k.naam.trim().toLowerCase() === fiche.naam.toLowerCase(),
  );
  if (alGekend) {
    terug(`${fiche.naam} stond er al. We hebben niets dubbel toegevoegd.`);
  }

  const { error } = await admin
    .from("kinderen")
    .insert({ profile_id: gezinId, ...fiche });

  if (error) terug(`${fiche.naam} is niet toegevoegd: ${uitleg(error)}`, true);
  terug(`${fiche.naam} is toegevoegd.`);
}

export async function wijzigKind(formData: FormData) {
  const gezinId = await gezinVanDitScherm();
  const kindId = String(formData.get("kind_id") || "");
  const fiche = ficheUitFormulier(formData);
  if (!fiche.naam) {
    terug("De naam mag niet leeg zijn, de rest van de fiche wel.", true);
  }

  const admin = createAdminClient();
  /*
    Met .select() erachter krijgen we de rijen terug die écht aangepast zijn.
    Zonder dat kan je een update die niets raakte — omdat dit kind bij een
    ander gezin hoort, of intussen verwijderd is — niet onderscheiden van een
    geslaagde. Dat is precies hoe "hij bewaart niet" eruitziet.
  */
  const { data: aangepast, error } = await admin
    .from("kinderen")
    .update({ ...fiche, updated_at: new Date().toISOString() })
    .eq("id", kindId)
    .eq("profile_id", gezinId)
    .select("id");

  if (error) {
    terug(`De fiche van ${fiche.naam} is niet bewaard: ${uitleg(error)}`, true);
  }
  if (!aangepast || aangepast.length === 0) {
    terug(
      `De fiche van ${fiche.naam} is niet bewaard: we vonden dit kind niet terug bij dit gezin. ` +
        `Laad de bladzijde opnieuw en probeer nog eens.`,
      true,
    );
  }
  terug(`De fiche van ${fiche.naam} is bewaard.`);
}

export async function verwijderKind(formData: FormData) {
  const gezinId = await gezinVanDitScherm();
  const kindId = String(formData.get("kind_id") || "");

  const admin = createAdminClient();
  const { error } = await admin
    .from("kinderen")
    .delete()
    .eq("id", kindId)
    .eq("profile_id", gezinId);

  if (error) terug(`Verwijderen is niet gelukt: ${uitleg(error)}`, true);
  terug("Het kind is verwijderd.");
}
