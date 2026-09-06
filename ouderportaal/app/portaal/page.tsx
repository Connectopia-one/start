import Link from "next/link";
import { requireIngelogd } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";

type ToegangRij = {
  materiaal: boolean;
  fotos: boolean;
  klasjes: { id: string; naam: string; slug: string } | { id: string; naam: string; slug: string }[] | null;
};

function klasjeVan(rij: ToegangRij) {
  return Array.isArray(rij.klasjes) ? rij.klasjes[0] : rij.klasjes;
}

export default async function PortaalPage() {
  const session = await requireIngelogd();
  const naam = session.profile?.full_name ?? session.email ?? "";
  const isBeheerder = session.profile?.role === "beheerder";

  const supabase = await createClient();
  const { data } = await supabase
    .from("toegang")
    .select("materiaal, fotos, klasjes(id, naam, slug)")
    .eq("profile_id", session.userId);

  const rijen = ((data as ToegangRij[] | null) ?? []).filter((r) => r.materiaal || r.fotos);

  return (
    <>
      <Header naam={naam} isBeheerder={isBeheerder} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">Welkom, {naam}</h1>

        {isBeheerder && (
          <div className="mt-4 rounded-lg border border-forest/30 bg-forest/5 px-4 py-3 text-sm text-forest-dark">
            Je bent aangemeld als beheerder.{" "}
            <Link href="/beheer" className="font-medium underline">
              Ga naar het beheerscherm
            </Link>{" "}
            om klasjes, gezinnen en content te beheren.
          </div>
        )}

        {rijen.length === 0 && !isBeheerder && (
          <p className="mt-6 text-sm text-ink-dim">
            Er is nog geen klasje aan je account gekoppeld. Neem contact op met Connectopia als je
            denkt dat dit niet klopt.
          </p>
        )}

        <div className="mt-8 grid gap-4 sm:grid-cols-2">
          {rijen.map((rij) => {
            const klasje = klasjeVan(rij);
            if (!klasje) return null;
            return (
              <div key={klasje.id} className="rounded-xl border border-border bg-surface p-5">
                <h2 className="font-display text-lg font-semibold text-ink">{klasje.naam}</h2>
                <div className="mt-3 flex flex-col gap-2 text-sm">
                  {rij.materiaal ? (
                    <Link
                      href={`/portaal/klasje/${klasje.slug}/materiaal`}
                      className="font-medium text-forest-dark hover:underline"
                    >
                      Lesmateriaal bekijken &rarr;
                    </Link>
                  ) : null}
                  {rij.fotos ? (
                    <Link
                      href={`/portaal/klasje/${klasje.slug}/fotos`}
                      className="font-medium text-forest-dark hover:underline"
                    >
                      Foto&apos;s bekijken &rarr;
                    </Link>
                  ) : (
                    <span className="text-ink-dim">Foto&apos;s — niet ingeschakeld voor jouw account</span>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </main>
    </>
  );
}
