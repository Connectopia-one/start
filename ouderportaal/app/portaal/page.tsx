import Link from "next/link";
import { requirePortaalSessie } from "@/lib/auth";
import { MeekijkBalk } from "@/components/MeekijkBalk";
import { startMeekijken } from "./meekijken-actions";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";

type ToegangRij = {
  materiaal: boolean;
  fotos: boolean;
  klasjes:
    | { id: string; naam: string; slug: string }
    | { id: string; naam: string; slug: string }[]
    | null;
};

function klasjeVan(rij: ToegangRij) {
  return Array.isArray(rij.klasjes) ? rij.klasjes[0] : rij.klasjes;
}

export default async function PortaalPage() {
  const session = await requirePortaalSessie();
  const naam = session.profile?.full_name ?? session.email ?? "";
  const rol = session.profile?.role ?? "ouder";
  const isBeheerder = rol === "beheerder";
  const isLeerkracht = rol === "leerkracht";

  const supabase = await createClient();
  const { data } = await supabase
    .from("toegang")
    .select("materiaal, fotos, klasjes(id, naam, slug)")
    .eq("profile_id", session.userId);

  const rijen = ((data as ToegangRij[] | null) ?? []).filter(
    (r) => r.materiaal || r.fotos,
  );

  /*
    Ben je beheerder en kijk je nog niet mee, dan hoort de keuze om het
    portaal als een gezin te bekijken hier te staan — dit is het scherm waar
    je je afvraagt hoe een gezin het ziet.
  */
  const toonKiezer =
    session.echtProfiel?.role === "beheerder" && !session.meekijken;
  const { data: gezinnen } = toonKiezer
    ? await supabase
        .from("profiles")
        .select("id, full_name")
        .eq("role", "ouder")
        .order("full_name")
    : { data: null };

  return (
    <>
      {session.meekijken && (
        <MeekijkBalk naam={session.meekijken.naam} terug="/beheer/gezinnen" />
      )}
      <Header naam={naam} rol={rol} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">
          Welkom, {naam}
        </h1>

        {isBeheerder && (
          <div className="mt-4 rounded-lg border border-forest/30 bg-forest/5 px-4 py-3 text-sm text-forest-dark">
            Je bent aangemeld als beheerder.{" "}
            <Link href="/beheer" className="font-medium underline">
              Ga naar het beheerscherm
            </Link>{" "}
            om klasjes, gezinnen en content te beheren.
          </div>
        )}

        {toonKiezer && (
          <div className="mt-4 rounded-lg border border-border bg-surface px-4 py-4">
            <p className="text-sm font-medium text-ink">
              Bekijk het portaal zoals een gezin het ziet
            </p>
            <p className="mt-1 text-sm text-ink-dim">
              Je blijft gewoon als jezelf ingelogd. Handig om na te kijken of
              het materiaal er staat en of de links werken.
            </p>
            {gezinnen?.length ? (
              <form
                action={startMeekijken}
                className="mt-3 flex flex-wrap items-center gap-2"
              >
                <label htmlFor="gezinId" className="sr-only">
                  Kies een gezin
                </label>
                <select
                  id="gezinId"
                  name="gezinId"
                  className="rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                >
                  {gezinnen.map((g) => (
                    <option key={g.id} value={g.id}>
                      {g.full_name}
                    </option>
                  ))}
                </select>
                <button
                  type="submit"
                  className="rounded-md bg-forest px-3 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
                >
                  Bekijken
                </button>
              </form>
            ) : (
              <p className="mt-3 text-sm text-ink-dim">
                Er zijn nog geen gezinnen om mee te bekijken.
              </p>
            )}
          </div>
        )}

        {isLeerkracht && (
          <div className="mt-4 rounded-lg border border-forest/30 bg-forest/5 px-4 py-3 text-sm text-forest-dark">
            Je bent aangemeld als teamlid.{" "}
            <Link href="/team" className="font-medium underline">
              Ga naar het teamscherm
            </Link>{" "}
            om foto&apos;s toe te voegen en fiches te bekijken.
          </div>
        )}

        {rijen.length === 0 && !isBeheerder && !isLeerkracht && (
          <p className="mt-6 text-sm text-ink-dim">
            Er is nog geen klasje aan je account gekoppeld. Neem contact op met
            Connectopia als je denkt dat dit niet klopt.
          </p>
        )}

        <div className="mt-8 grid gap-4 sm:grid-cols-2">
          {rijen.map((rij) => {
            const klasje = klasjeVan(rij);
            if (!klasje) return null;
            return (
              <div
                key={klasje.id}
                className="rounded-xl border border-border bg-surface p-5"
              >
                <h2 className="font-display text-lg font-semibold text-ink">
                  {klasje.naam}
                </h2>
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
                    <span className="text-ink-dim">
                      Foto&apos;s — niet ingeschakeld voor jouw account
                    </span>
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
