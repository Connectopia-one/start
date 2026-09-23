import "server-only";
import { cookies } from "next/headers";
import { createClient } from "@/lib/supabase/server";

/*
  MEEKIJKEN — het portaal bekijken zoals een gezin het ziet

  Als beheerder wil je kunnen nakijken hoe een gezin het portaal te zien krijgt
  (staat het materiaal er, werken de links) zonder uit te loggen en met een
  ander account weer in te loggen.

  Hoe het werkt: een koekje met het id van het gezin waar je mee meekijkt. Je
  blijft gewoon als jezelf ingelogd — er wordt dus NIET van account gewisseld
  en er is geen wachtwoord van iemand anders bij betrokken. De schermen van
  het portaal halen enkel hun gegevens op alsof jij dat gezin bent, en de
  toegangsregels van dat gezin worden daarbij wél toegepast: zie je iets niet,
  dan ziet dat gezin het ook niet.

  Alleen een beheerder kan dit. Staat het koekje er bij iemand anders, dan
  wordt het gewoon genegeerd.
*/

const KOEKJE = "meekijken";
/* Vier uur. Lang genoeg voor een werksessie, kort genoeg om niet te blijven hangen. */
const DUUR = 60 * 60 * 4;

export type Meekijken = { id: string; naam: string };

/**
 * Met welk gezin kijk je nu mee? Geeft null terug als je niet meekijkt, als je
 * geen beheerder bent, of als dat gezin intussen niet meer bestaat.
 */
export async function huidigMeekijken(): Promise<Meekijken | null> {
  const jar = await cookies();
  const id = jar.get(KOEKJE)?.value;
  if (!id) return null;

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return null;

  const { data: ik } = await supabase
    .from("profiles")
    .select("role")
    .eq("id", user.id)
    .single();
  if (ik?.role !== "beheerder") return null;

  const { data: gezin } = await supabase
    .from("profiles")
    .select("id, full_name")
    .eq("id", id)
    .single();
  if (!gezin) return null;

  return { id: gezin.id, naam: gezin.full_name };
}

/** Zet het koekje. Enkel een beheerder mag dit, en enkel op een bestaand gezin. */
export async function zetMeekijken(gezinId: string) {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return false;

  const { data: ik } = await supabase
    .from("profiles")
    .select("role")
    .eq("id", user.id)
    .single();
  if (ik?.role !== "beheerder") return false;

  const { data: gezin } = await supabase
    .from("profiles")
    .select("id")
    .eq("id", gezinId)
    .single();
  if (!gezin) return false;

  const jar = await cookies();
  jar.set(KOEKJE, gezin.id, {
    httpOnly: true,
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
    path: "/",
    maxAge: DUUR,
  });
  return true;
}

export async function wisMeekijken() {
  const jar = await cookies();
  jar.delete(KOEKJE);
}
