import Link from "next/link";
import { Header } from "@/components/Header";
import { BadgeKast } from "@/components/BadgeKast";
import { getSessionProfile } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";

export const metadata = {
  title: "Mijn verzameling — Oefenplatform Connectopia",
  description: "De badges die een kind bij elkaar oefende in het oefenplatform van Connectopia vzw.",
};

export default async function BadgesPage() {
  const session = await getSessionProfile();
  const supabase = await createClient();

  const { data: kinderen } = session
    ? await supabase
        .from("kinderen")
        .select("id, naam")
        .eq("profile_id", session.userId)
        .order("naam")
    : { data: [] };

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">⭐ Mijn verzameling</h1>
        <p className="mt-2 max-w-2xl text-sm text-ink-dim">
          Alles wat je al bij elkaar geoefend hebt. Er is geen ranglijst en niets om te winnen van
          iemand anders — elke badge gaat over wat jij zelf deed.
        </p>

        {(kinderen ?? []).length === 0 ? (
          <p className="mt-6 max-w-2xl rounded-md bg-info/10 px-4 py-3 text-sm text-ink">
            Badges worden per kind bijgehouden.{" "}
            <Link href="/account" className="underline underline-offset-2">
              Voeg een kind toe aan je account
            </Link>{" "}
            om ze te zien verschijnen.
          </p>
        ) : (
          <BadgeKast kinderen={kinderen ?? []} />
        )}
      </main>
    </>
  );
}
