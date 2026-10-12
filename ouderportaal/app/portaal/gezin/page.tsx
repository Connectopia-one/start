import { requirePortaalSessie } from "@/lib/auth";
import { MeekijkBalk } from "@/components/MeekijkBalk";
import { createClient } from "@/lib/supabase/server";
import { kolomOntbreekt } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import {
  wijzigContactgegevens,
  voegKindToe,
  wijzigKind,
  verwijderKind,
} from "./actions";

import { type Kind, KINDVELDEN } from "@/lib/kind";
import { KindVelden } from "@/components/KindVelden";

export default async function GezinProfielPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; succes?: string }>;
}) {
  const { fout, succes } = await searchParams;
  const session = await requirePortaalSessie();
  const naam = session.profile?.full_name ?? session.email ?? "";
  const rol = session.profile?.role ?? "ouder";

  const supabase = await createClient();
  const [{ data: profiel }, { data: kinderenData, error: kinderenFout }] =
    await Promise.all([
      supabase
        .from("profiles")
        .select("telefoon, adres")
        .eq("id", session.userId)
        .single(),
      supabase
        .from("kinderen")
        .select(KINDVELDEN)
        .eq("profile_id", session.userId)
        .order("naam"),
    ]);

  const kinderen = (kinderenData as Kind[] | null) ?? [];

  /*
    Mislukt deze select, dan staat er geen enkel kind op het scherm en ziet dat
    eruit alsof er nooit iets bewaard is. Dat mag niet stil gebeuren: zeg wat
    er aan de hand is en welk bestand er nog moet draaien.
  */
  const leesFout = kinderenFout
    ? kolomOntbreekt(kinderenFout, "supabase/inlichtingenfiche.sql") ||
      `De fiches konden niet opgehaald worden: ${kinderenFout.message}`
    : null;

  return (
    <>
      {session.meekijken && (
        <MeekijkBalk naam={session.meekijken.naam} terug="/beheer/gezinnen" />
      )}
      <Header
        naam={naam}
        rol={rol}
        terugHref="/portaal"
        terugLabel="Overzicht"
      />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">
          {session.meekijken ? `Gezin ${session.meekijken.naam}` : "Mijn gezin"}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          Contactgegevens en de inlichtingenfiche van je kind(eren) — enkel
          zichtbaar voor jou en Connectopia.
        </p>

        {/* Na elke bewaring staat hier wat er gebeurd is. Zonder deze regel
            ziet een geslaagde bewaring er net zo uit als een mislukte. */}
        {succes && (
          <p className="mt-4 rounded-md bg-forest/10 px-4 py-3 text-sm text-forest-dark">
            {succes}
          </p>
        )}
        {fout && (
          <p className="mt-4 rounded-md bg-danger/10 px-4 py-3 text-sm text-danger">
            {fout}
          </p>
        )}
        {leesFout && (
          <p className="mt-4 rounded-md bg-danger/10 px-4 py-3 text-sm text-danger">
            {leesFout}
          </p>
        )}

        {/* Je kijkt mee, dus wat je invult hoort bij dat gezin. Dat hoort op
            het scherm te staan voor je begint te typen, niet achteraf. */}
        {session.meekijken && (
          <p className="mt-3 rounded-md bg-amber/15 px-4 py-3 text-sm text-ink">
            Je kijkt mee met {session.meekijken.naam}. Wat je hier invult of
            aanpast, bewaren we bij dit gezin en niet bij jezelf. Zo kan je de
            fiche invullen voor een gezin dat dat zelf niet doet.
          </p>
        )}

        <section className="mt-8 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">
            Contactgegevens
          </h2>
          <form action={wijzigContactgegevens} className="mt-4 space-y-4">
            <div className="space-y-1.5">
              <label
                htmlFor="telefoon"
                className="text-sm font-medium text-ink"
              >
                Telefoonnummer
              </label>
              <input
                id="telefoon"
                name="telefoon"
                type="tel"
                defaultValue={profiel?.telefoon ?? ""}
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>
            <div className="space-y-1.5">
              <label htmlFor="adres" className="text-sm font-medium text-ink">
                Adres
              </label>
              <input
                id="adres"
                name="adres"
                defaultValue={profiel?.adres ?? ""}
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>
            <button
              type="submit"
              className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Bewaren
            </button>
          </form>
        </section>

        <section className="mt-8">
          <h2 className="font-display text-lg font-semibold text-ink">
            Inlichtingenfiche(s)
          </h2>
          <div className="mt-4 space-y-4">
            {kinderen.map((kind) => (
              <KindForm key={kind.id} kind={kind} />
            ))}
          </div>

          <div className="mt-6 rounded-xl border border-dashed border-border-strong bg-surface p-6">
            <h3 className="font-display text-base font-semibold text-ink">
              Kind toevoegen
            </h3>
            <KindVelden action={voegKindToe} submitLabel="Toevoegen" />
          </div>
        </section>
      </main>
    </>
  );
}

function KindForm({ kind }: { kind: Kind }) {
  return (
    <div className="rounded-xl border border-border bg-surface p-6">
      <div className="flex items-center justify-between">
        <h3 className="font-display text-base font-semibold text-ink">
          {kind.naam}
        </h3>
        <form action={verwijderKind}>
          <input type="hidden" name="kind_id" value={kind.id} />
          <button type="submit" className="text-sm text-danger hover:underline">
            Verwijderen
          </button>
        </form>
      </div>
      <KindVelden action={wijzigKind} kind={kind} submitLabel="Bewaren" />
    </div>
  );
}
