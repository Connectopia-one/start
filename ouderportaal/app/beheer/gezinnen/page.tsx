import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { maakGezin } from "./actions";
import { startMeekijken } from "@/app/portaal/meekijken-actions";
import { alleMailadressen } from "@/lib/mailadressen";
import {
  KINDVELDEN,
  watOntbreekt,
  watOntbreektGezin,
  lijstZin,
  type Kind,
} from "@/lib/kind";

export default async function GezinnenPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; succes?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout, succes } = await searchParams;
  const naam = session.profile?.full_name ?? session.email ?? "";

  const supabase = await createClient();
  const [{ data: gezinnen }, { data: kinderen }, mailadressen] =
    await Promise.all([
      supabase
        .from("profiles")
        .select("id, full_name, telefoon, adres")
        .eq("role", "ouder")
        .order("full_name"),
      supabase.from("kinderen").select(`profile_id, ${KINDVELDEN}`),
      /* Het mailadres hoort bij het account, niet bij het profiel; zie
         lib/mailadressen.ts. */
      alleMailadressen(),
    ]);

  /*
    Per gezin: wat er aan de fiches ontbreekt. Kim moet voor een kamp weten wie
    ze nog moet achternabellen, en dat stond tot nu enkel achter een klik per
    kind. Een gezin zonder kinderen telt als onvolledig: er staat dan nog geen
    enkele fiche klaar.
  */
  const kinderenVan = new Map<string, Kind[]>();
  for (const rij of (kinderen ?? []) as unknown as (Kind & {
    profile_id: string;
  })[]) {
    const lijst = kinderenVan.get(rij.profile_id) ?? [];
    lijst.push(rij);
    kinderenVan.set(rij.profile_id, lijst);
  }

  const rijen = (gezinnen ?? []).map((g) => {
    const eigen = kinderenVan.get(g.id) ?? [];
    const onvolledig = eigen.filter((k) => watOntbreekt(k).length > 0);
    const gezinsgegevens = watOntbreektGezin(g);
    return {
      ...g,
      kinderen: eigen,
      onvolledig,
      gezinsgegevens,
      klaar:
        eigen.length > 0 &&
        onvolledig.length === 0 &&
        gezinsgegevens.length === 0,
    };
  });

  const nogTeDoen = rijen.filter((r) => !r.klaar).length;

  return (
    <>
      <Header
        naam={naam}
        rol="beheerder"
        terugHref="/beheer"
        terugLabel="Beheer"
      />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <h1 className="font-display text-2xl font-semibold text-ink">
            Gezinnen
          </h1>
          <Link
            href="/beheer/gezinnen/afdrukken"
            className="rounded-md border border-border px-3 py-1.5 text-sm font-medium text-forest-dark hover:border-forest"
          >
            Alle fiches afdrukken
          </Link>
        </div>

        {rijen.length > 0 && (
          <p className="mt-1 text-sm text-ink-dim">
            {nogTeDoen === 0
              ? `Alle ${rijen.length} fiches zijn in orde.`
              : `${nogTeDoen} van de ${rijen.length} gezinnen moeten hun fiche nog aanvullen.`}
          </p>
        )}

        {fout && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            {fout}
          </p>
        )}
        {succes && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">
            {succes}
          </p>
        )}

        <ul className="mt-6 space-y-2">
          {rijen.map((g) => (
            <li
              key={g.id}
              /* Het gekleurde randje links is wat Kim vroeg: groen als het in
                 orde is, rood als er nog iets moet gebeuren. */
              className={`flex items-center justify-between gap-3 rounded-lg border border-l-4 border-border bg-surface p-3 ${
                g.klaar ? "border-l-forest" : "border-l-danger"
              }`}
            >
              <div className="min-w-0">
                <Link
                  href={`/beheer/gezinnen/${g.id}`}
                  className="font-medium text-ink hover:underline"
                >
                  {g.full_name}
                </Link>
                {/* Het adres waarmee dit gezin inlogt. Zonder dit moest Kim
                    in Supabase gaan kijken wie welk account was. */}
                <p className="truncate text-xs text-ink-dim">
                  {mailadressen.get(g.id) ?? "geen mailadres gevonden"}
                </p>
                <p className="mt-1 text-xs">
                  {g.kinderen.length === 0 ? (
                    <span className="text-danger">
                      Nog geen kind toegevoegd
                    </span>
                  ) : g.klaar ? (
                    <span className="text-forest-dark">
                      Fiche in orde ({g.kinderen.length}{" "}
                      {g.kinderen.length === 1 ? "kind" : "kinderen"})
                    </span>
                  ) : (
                    <span className="text-danger">
                      {g.gezinsgegevens.length > 0 &&
                        `Van het gezin ontbreekt ${lijstZin(g.gezinsgegevens)}. `}
                      {g.onvolledig.length > 0 &&
                        `Onvolledig: ${g.onvolledig
                          .map((k) => `${k.naam} (${lijstZin(watOntbreekt(k))})`)
                          .join(", ")}`}
                    </span>
                  )}
                </p>
              </div>
              <form action={startMeekijken}>
                <input type="hidden" name="gezinId" value={g.id} />
                <button
                  type="submit"
                  className="shrink-0 text-sm font-medium text-forest-dark hover:underline"
                >
                  Bekijk het portaal zo &rarr;
                </button>
              </form>
            </li>
          ))}
          {rijen.length === 0 && (
            <li className="text-sm text-ink-dim">
              Nog geen gezinnen toegevoegd.
            </li>
          )}
        </ul>

        <section className="mt-10 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">
            Nieuw gezin toevoegen
          </h2>
          <p className="mt-1 text-sm text-ink-dim">
            Na het aanmaken kies je op de volgende pagina welke klasjes dit
            gezin mag zien, en of dat lesmateriaal, foto&apos;s, of beide zijn.
          </p>
          <form action={maakGezin} className="mt-4 space-y-4">
            <div className="space-y-1.5">
              <label htmlFor="naam" className="text-sm font-medium text-ink">
                Naam gezin
              </label>
              <input
                id="naam"
                name="naam"
                required
                placeholder="Bv. Familie Peeters"
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>
            <div className="space-y-1.5">
              <label htmlFor="email" className="text-sm font-medium text-ink">
                E-mailadres
              </label>
              <input
                id="email"
                name="email"
                type="email"
                required
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>
            <div className="space-y-1.5">
              <label
                htmlFor="wachtwoord"
                className="text-sm font-medium text-ink"
              >
                Tijdelijk wachtwoord (minstens 8 tekens)
              </label>
              <input
                id="wachtwoord"
                name="wachtwoord"
                type="text"
                minLength={8}
                required
                placeholder="Deel dit veilig met het gezin"
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>
            <button
              type="submit"
              className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Account aanmaken
            </button>
          </form>
        </section>
      </main>
    </>
  );
}
