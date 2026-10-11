import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient, tabelOntbreekt } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import {
  ACTIVITEITVELDEN,
  SOORTEN,
  datumTekst,
  euro,
  factuurLabel,
  sorteer,
  type Activiteit,
} from "@/lib/activiteiten";
import { maakActiviteit, verwijderActiviteit, zetArchief } from "./actions";

export const dynamic = "force-dynamic";

/*
  De kampen, lessen en werkingen waar kinderen bij horen.

  Dit is Kims eigen indeling, niet die van het inschrijfformulier. Een ouder
  die een vakje aankruist doet een aanvraag; pas als Kim het kind hier bij een
  activiteit zet, staat het op de lijst die ze meeneemt. Een kind mag bij
  zoveel activiteiten staan als nodig: wie wekelijks naar Young Engineers komt
  en ook op het kamp staat, hoort op allebei de lijsten.
*/
export default async function ActiviteitenBeheer({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; succes?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout, succes } = await searchParams;
  const naam = session.profile?.full_name ?? session.email ?? "";

  const db = createAdminClient();
  const [{ data, error }, { data: deelnames }] = await Promise.all([
    db.from("activiteiten").select(ACTIVITEITVELDEN),
    db.from("deelnames").select("activiteit_id, aanwezig"),
  ]);

  const activiteiten = sorteer((data ?? []) as Activiteit[]);
  const aantallen = new Map<string, number>();
  const openVinkjes = new Map<string, number>();
  for (const rij of (deelnames ?? []) as {
    activiteit_id: string;
    aanwezig: boolean | null;
  }[]) {
    aantallen.set(
      rij.activiteit_id,
      (aantallen.get(rij.activiteit_id) ?? 0) + 1,
    );
    if (rij.aanwezig === null)
      openVinkjes.set(
        rij.activiteit_id,
        (openVinkjes.get(rij.activiteit_id) ?? 0) + 1,
      );
  }

  /* Een leesfout mag niet stil blijven: zonder dit stond er gewoon "er staat
     nog niets", ook als de tabel helemaal niet bestaat. */
  const leesfout = error
    ? (tabelOntbreekt(
        error,
        "voor de kampen en lessen",
        "ouderportaal/supabase/activiteiten.sql",
      ) ?? `Dit kon niet gelezen worden: ${error.message}`)
    : null;

  const lopend = activiteiten.filter((a) => !a.archief);
  const gearchiveerd = activiteiten.filter((a) => a.archief);

  return (
    <>
      <Header
        naam={naam}
        rol="beheerder"
        terugHref="/beheer"
        terugLabel="Beheer"
      />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">
          Kampen en lessen
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          Zet hier elke kampdag, les of werking die doorgaat. Daarna duid je bij
          een kind aan waar het bij hoort, en krijg je per activiteit een lijst
          met de gegevens van de fiche. Wie er was, vink je per dag aan; het{" "}
          <a href="/beheer/facturatie" className="underline underline-offset-2">
            maandoverzicht voor de facturen
          </a>{" "}
          telt die aanwezigheden samen.
        </p>

        {leesfout && (
          <p className="mt-6 rounded-lg border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            {leesfout}
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

        {!leesfout && (
          <section className="mt-6 rounded-xl border border-border bg-surface p-5">
            <h2 className="font-display text-base font-semibold text-ink">
              Een activiteit bijzetten
            </h2>
            <form action={maakActiviteit} className="mt-3 grid gap-3 sm:grid-cols-2">
              <label className="sm:col-span-2">
                <span className="text-sm font-medium text-ink">Naam</span>
                <input
                  name="naam"
                  required
                  placeholder="Herfstkamp Hasselt, dag 1"
                  className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                />
              </label>
              <label>
                <span className="text-sm font-medium text-ink">Soort</span>
                <select
                  name="soort"
                  defaultValue="kamp"
                  className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                >
                  {SOORTEN.map((soort) => (
                    <option key={soort} value={soort}>
                      {soort}
                    </option>
                  ))}
                </select>
              </label>
              <label>
                <span className="text-sm font-medium text-ink">
                  Datum <span className="text-ink-dim">(mag leeg)</span>
                </span>
                <input
                  type="date"
                  name="datum"
                  className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                />
              </label>
              <label className="sm:col-span-2">
                <span className="text-sm font-medium text-ink">
                  Plaats <span className="text-ink-dim">(mag leeg)</span>
                </span>
                <input
                  name="plaats"
                  placeholder="Level X 28, Vilderstraat 28, Hasselt"
                  className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                />
              </label>
              <label>
                <span className="text-sm font-medium text-ink">
                  Op de factuur <span className="text-ink-dim">(mag leeg)</span>
                </span>
                <input
                  name="factuurregel"
                  placeholder="Les Young Engineers"
                  className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                />
              </label>
              <label>
                <span className="text-sm font-medium text-ink">
                  Prijs per kind{" "}
                  <span className="text-ink-dim">(mag leeg)</span>
                </span>
                <input
                  name="prijs"
                  inputMode="decimal"
                  placeholder="20"
                  className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                />
              </label>
              <div className="sm:col-span-2">
                <button
                  type="submit"
                  className="rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
                >
                  Toevoegen
                </button>
                <p className="mt-1.5 text-xs text-ink-dim">
                  Een wekelijkse les laat je zonder datum. Die komt onder de
                  dagen te staan.
                </p>
              </div>
            </form>
          </section>
        )}

        {!leesfout && lopend.length === 0 && (
          <p className="mt-6 text-sm text-ink-dim">
            Er staat nog niets. Zet hierboven je eerste kampdag of les erbij.
          </p>
        )}

        <ul className="mt-6 space-y-3">
          {lopend.map((activiteit) => (
            <Rij
              key={activiteit.id}
              activiteit={activiteit}
              aantal={aantallen.get(activiteit.id) ?? 0}
              open={openVinkjes.get(activiteit.id) ?? 0}
            />
          ))}
        </ul>

        {gearchiveerd.length > 0 && (
          <>
            <h2 className="mt-10 font-display text-base font-semibold text-ink">
              Archief
            </h2>
            <ul className="mt-3 space-y-3">
              {gearchiveerd.map((activiteit) => (
                <Rij
                  key={activiteit.id}
                  activiteit={activiteit}
                  aantal={aantallen.get(activiteit.id) ?? 0}
                  open={openVinkjes.get(activiteit.id) ?? 0}
                />
              ))}
            </ul>
          </>
        )}
      </main>
    </>
  );
}

function Rij({
  activiteit,
  aantal,
  open,
}: {
  activiteit: Activiteit;
  aantal: number;
  open: number;
}) {
  const wanneer = datumTekst(activiteit.datum);
  return (
    <li
      className={`rounded-lg border border-border bg-surface p-4 ${
        activiteit.archief ? "opacity-70" : ""
      }`}
    >
      <div className="flex flex-wrap items-start justify-between gap-2">
        <div>
          <Link
            href={`/beheer/activiteiten/${activiteit.id}`}
            className="font-medium text-ink underline-offset-2 hover:underline"
          >
            {activiteit.naam}
          </Link>
          <p className="mt-0.5 text-xs text-ink-dim">
            {activiteit.soort}
            {wanneer && ` · ${wanneer}`}
            {activiteit.plaats && ` · ${activiteit.plaats}`}
          </p>
          <p className="mt-0.5 text-xs text-ink-dim">
            {factuurLabel(activiteit)}
            {activiteit.prijs !== null &&
              ` · ${euro(Number(activiteit.prijs))} per kind`}
            {!activiteit.datum && " · geen datum, valt in geen maand"}
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-2">
          <span className="rounded-full bg-forest/10 px-2.5 py-0.5 text-xs font-medium text-forest-dark">
            {aantal} {aantal === 1 ? "kind" : "kinderen"}
          </span>
          {open > 0 && (
            <span className="rounded-full bg-amber/15 px-2.5 py-0.5 text-xs font-medium text-ink">
              {open} nog aan te duiden
            </span>
          )}
          <Link
            href={`/beheer/activiteiten/${activiteit.id}`}
            className="rounded-md bg-forest px-3 py-1.5 text-sm font-medium text-white hover:bg-forest-dark"
          >
            Lijst
          </Link>
          <form action={zetArchief}>
            <input type="hidden" name="id" value={activiteit.id} />
            <input
              type="hidden"
              name="archief"
              value={activiteit.archief ? "nee" : "ja"}
            />
            <button
              type="submit"
              className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
            >
              {activiteit.archief ? "Terughalen" : "Archiveren"}
            </button>
          </form>
          {aantal === 0 && (
            <form action={verwijderActiviteit}>
              <input type="hidden" name="id" value={activiteit.id} />
              <button
                type="submit"
                className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-danger hover:text-danger"
              >
                Verwijderen
              </button>
            </form>
          )}
        </div>
      </div>
    </li>
  );
}
