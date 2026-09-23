import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import { huidigMeekijken, type Meekijken } from "@/lib/meekijken";

export type Profile = {
  id: string;
  full_name: string;
  role: "ouder" | "beheerder" | "leerkracht";
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
    .select("id, full_name, role")
    .eq("id", user.id)
    .single();

  return {
    userId: user.id,
    email: user.email ?? null,
    profile: (profile as Profile) ?? null,
  };
}

/** Stuurt niet-ingelogde bezoekers naar /login. Geeft de sessie terug. */
export async function requireIngelogd(): Promise<Session> {
  const session = await getSessionProfile();
  if (!session) redirect("/login");
  return session;
}

/** Zoals requireIngelogd, maar enkel voor beheerders — anderen gaan terug naar /portaal. */
export async function requireBeheerder(): Promise<Session> {
  const session = await requireIngelogd();
  if (session.profile?.role !== "beheerder") redirect("/portaal");
  return session;
}

/*
  De sessie voor de schermen van het portaal zelf (/portaal/...).

  Kijk je als beheerder mee met een gezin (zie lib/meekijken.ts), dan geeft
  deze functie dat gezin terug in plaats van jezelf: de schermen halen hun
  gegevens dan op alsof je dat gezin bent, en tonen zich ook zo. "meekijken"
  zegt met wie, zodat er een balk boven kan die eraan herinnert.

  alsOuder is waar zodra je het portaal als een gezin bekijkt. De schermen
  gebruiken dat om de toegangsregels van dat gezin echt toe te passen, ook al
  zou jij als beheerder alles mogen zien.
*/
export type PortaalSessie = Session & {
  meekijken: Meekijken | null;
  alsOuder: boolean;
  /* Wie je echt bent, ook terwijl je meekijkt met een gezin. */
  echtProfiel: Profile | null;
};

export async function requirePortaalSessie(): Promise<PortaalSessie> {
  const session = await requireIngelogd();
  const meekijken = await huidigMeekijken();

  if (!meekijken) {
    const rol = session.profile?.role ?? "ouder";
    return {
      ...session,
      meekijken: null,
      alsOuder: rol === "ouder",
      echtProfiel: session.profile,
    };
  }

  return {
    userId: meekijken.id,
    email: null,
    echtProfiel: session.profile,
    profile: { id: meekijken.id, full_name: meekijken.naam, role: "ouder" },
    meekijken,
    alsOuder: true,
  };
}

/** Zoals requireIngelogd, maar voor beheerders én leerkrachten (beperkte teamtoegang). */
export async function requireStaff(): Promise<Session> {
  const session = await requireIngelogd();
  const rol = session.profile?.role;
  if (rol !== "beheerder" && rol !== "leerkracht") redirect("/portaal");
  return session;
}
