import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";

export type Profile = {
  id: string;
  full_name: string;
  role: "ouder" | "beheerder" | "begeleider";
  is_plusklas: boolean;
  toegang_schooljaar: string | null;
  /** Gratis volledige toegang tot en met deze dag ("2027-08-31"), los van code of betaling. */
  gratis_tot?: string | null;
};

export type Session = {
  userId: string;
  email: string | null;
  profile: Profile | null;
};

export async function getSessionProfile(): Promise<Session | null> {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return null;

  const { data: profile } = await supabase
    .from("profiles")
    // Een sterretje en geen vaste kolomlijst: gratis_tot komt pas met
    // supabase/enquete-en-reviews.sql. Zolang dat niet gedraaid is, mag het
    // inloggen daar niet op stuklopen.
    .select("*")
    .eq("id", user.id)
    .single();

  return {
    userId: user.id,
    email: user.email ?? null,
    profile: (profile as Profile) ?? null,
  };
}

/**
 * Stuurt niet-ingelogde bezoekers naar /login. Geeft de sessie terug.
 * Met `volgende` komt de ouder na het inloggen meteen terug op die pagina,
 * in plaats van op /account (Kim, 6 november 2026: wie op de enquêtelink
 * uit de mail klikte, moest daarna zelf de knop zoeken).
 */
export async function requireIngelogd(volgende?: string): Promise<Session> {
  const session = await getSessionProfile();
  if (!session) {
    redirect(volgende ? `/login?volgende=${encodeURIComponent(volgende)}` : "/login");
  }
  return session;
}

/** Enkel een pad binnen het platform zelf, nooit een ander adres. */
export function veiligVolgende(waarde: unknown): string | null {
  const pad = typeof waarde === "string" ? waarde.trim() : "";
  if (!pad.startsWith("/") || pad.startsWith("//") || pad.startsWith("/\\")) return null;
  return pad;
}

/** Zoals requireIngelogd, maar enkel voor beheerders. */
export async function requireBeheerder(): Promise<Session> {
  const session = await requireIngelogd();
  if (session.profile?.role !== "beheerder") redirect("/account");
  return session;
}

/**
 * Voor de opvolgfiches van de plusklas: beheerder of begeleider.
 * Een begeleider komt hiermee NIET in /beheer — die blijft enkel voor jou.
 */
export async function requireBegeleider(): Promise<Session> {
  const session = await requireIngelogd();
  const rol = session.profile?.role;
  if (rol !== "beheerder" && rol !== "begeleider") redirect("/account");
  return session;
}
