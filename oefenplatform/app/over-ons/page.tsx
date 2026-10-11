import Link from "next/link";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { NIVEAUS } from "@/lib/niveaus";
import { overOns } from "@/inhoud/overons";
import { PRIJS_NU_EUR, TIJDELIJKE_PRIJS, TIJDELIJKE_PRIJS_UITLEG } from "@/lib/prijs";

/*
  Alle tekst van deze pagina staat in `inhoud/overons.ts`, zodat Kim ze kan
  aanpassen zonder code. Eén stuk staat daar met opzet niet in: het overzicht
  van wat we aanbieden. Dat stond hier met de hand getypt (vijf vakken) en was
  al lang achterhaald — er staan er intussen bijna zeventig. Daarom telt de
  pagina de vakken nu zelf uit de databank, per categorie. Een nieuw vak in
  Beheer verschijnt hier dus vanzelf, en deze lijst kan niet meer verouderen.
*/

type Rij = { naam: string; hoofdstukken: { niveau: string }[] | null };

export default async function OverOnsPage() {
  const session = await getSessionProfile();
  const supabase = await createClient();

  const { data: vakken } = await supabase
    .from("vakken")
    .select("naam, hoofdstukken(niveau)")
    .order("volgorde", { ascending: true });

  /* Per categorie de vakken die er minstens één hoofdstuk in hebben. Een vak
     zoals wiskunde staat in de databank één keer, met hoofdstukken in
     meerdere categorieën; het hoort dus in meerdere rijen thuis. */
  const perNiveau = NIVEAUS.map((niveau) => {
    const namen = ((vakken ?? []) as Rij[])
      .filter((vak) =>
        (vak.hoofdstukken ?? []).some((h) => h.niveau === niveau.slug),
      )
      .map((vak) => vak.naam)
      .sort((a, b) => a.localeCompare(b, "nl"));
    const hoofdstukken = ((vakken ?? []) as Rij[]).reduce(
      (som, vak) =>
        som + (vak.hoofdstukken ?? []).filter((h) => h.niveau === niveau.slug).length,
      0,
    );
    return { niveau, namen, hoofdstukken };
  }).filter((rij) => rij.namen.length > 0);

  const aantalVakken = perNiveau.reduce((som, rij) => som + rij.namen.length, 0);
  const aantalHoofdstukken = perNiveau.reduce((som, rij) => som + rij.hoofdstukken, 0);
  const getal = (n: number) => n.toLocaleString("nl-BE");

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          {overOns.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">{overOns.titel}</h1>
        <p className="mt-4 text-sm text-ink-dim">{overOns.aanhef}</p>
        <p className="mt-3 text-sm text-ink-dim">{overOns.welkom}</p>

        <div className="mt-8 space-y-8">
          <section className="rounded-lg border border-border bg-surface px-5 py-4">
            <h2 className="font-display text-lg font-semibold text-ink">
              {overOns.leidraad.kop}
            </h2>
            {overOns.leidraad.alinea.map((alinea) => (
              <p key={alinea} className="mt-2 text-sm text-ink-dim">
                {alinea}
              </p>
            ))}
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">
              {overOns.bijzonder.kop}
            </h2>
            <p className="mt-2 text-sm text-ink-dim">{overOns.bijzonder.alinea1}</p>
            <p className="mt-2 text-sm text-ink-dim">{overOns.bijzonder.alinea2}</p>
            <ul className="mt-2 list-disc space-y-1 pl-5 text-sm text-ink-dim">
              {overOns.bijzonder.punten.map((punt) => (
                <li key={punt}>{punt}</li>
              ))}
            </ul>
            <p className="mt-2 text-sm text-ink-dim">{overOns.bijzonder.slot}</p>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">
              {overOns.leerstof.kop}
            </h2>
            <p className="mt-2 text-sm text-ink-dim">{overOns.leerstof.intro}</p>
            <ul className="mt-2 list-disc space-y-1 pl-5 text-sm text-ink-dim">
              {overOns.leerstof.punten.map((punt) => (
                <li key={punt}>{punt}</li>
              ))}
            </ul>
            <p className="mt-2 text-sm text-ink-dim">{overOns.leerstof.slot}</p>
            <p className="mt-2 text-sm">
              <Link
                href="/onderwijsdoelen"
                className="text-forest-dark underline-offset-2 hover:underline"
              >
                {overOns.leerstof.link}
              </Link>
            </p>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">
              {overOns.aanbod.kop}
            </h2>
            <p className="mt-2 text-sm text-ink-dim">{overOns.aanbod.intro}</p>

            {perNiveau.length === 0 ? (
              <p className="mt-2 text-sm text-ink-dim">{overOns.aanbod.leeg}</p>
            ) : (
              <>
                <p className="mt-3 text-sm text-ink">
                  {getal(aantalVakken)} vakken in {perNiveau.length} categorieën, samen{" "}
                  {getal(aantalHoofdstukken)} hoofdstukken.
                </p>
                <dl className="mt-3 space-y-3">
                  {perNiveau.map(({ niveau, namen }) => (
                    <div key={niveau.slug}>
                      <dt className="text-sm font-medium text-ink">
                        <Link
                          href={`/niveaus/${niveau.slug}`}
                          className="underline-offset-2 hover:underline"
                        >
                          {niveau.emoji} {niveau.naam}
                        </Link>
                      </dt>
                      <dd className="mt-0.5 text-sm text-ink-dim">{namen.join(", ")}</dd>
                    </div>
                  ))}
                </dl>
              </>
            )}

            <p className="mt-3 text-sm text-ink-dim">{overOns.aanbod.slot}</p>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">
              {overOns.voorWie.kop}
            </h2>
            <p className="mt-2 text-sm text-ink-dim">{overOns.voorWie.intro}</p>
            <ul className="mt-2 list-disc space-y-1 pl-5 text-sm text-ink-dim">
              {overOns.voorWie.punten.map((punt) => (
                <li key={punt}>{punt}</li>
              ))}
            </ul>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">{overOns.prijs.kop}</h2>
            {TIJDELIJKE_PRIJS && (
              <p className="mt-2 rounded-md bg-amber/10 px-4 py-3 text-sm text-ink">
                {TIJDELIJKE_PRIJS_UITLEG}
              </p>
            )}
            <p className="mt-2 text-sm text-ink-dim">
              We vragen €{PRIJS_NU_EUR} {overOns.prijs.uitleg}
            </p>
            <p className="mt-3 rounded-md bg-amber/10 px-4 py-3 text-sm text-ink">
              ⚠️ <strong>Belangrijk:</strong> {overOns.prijs.waarschuwing}
            </p>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">{overOns.gratis.kop}</h2>
            <p className="mt-2 text-sm text-ink-dim">{overOns.gratis.tekst}</p>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">{overOns.fouten.kop}</h2>
            <p className="mt-2 text-sm text-ink-dim">{overOns.fouten.tekst}</p>
            <p className="mt-2 text-sm">
              📧{" "}
              <a
                href={`mailto:${overOns.fouten.mail}`}
                className="text-forest-dark underline-offset-2 hover:underline"
              >
                {overOns.fouten.mail}
              </a>
            </p>
            <p className="mt-2 text-sm text-ink-dim">{overOns.fouten.slot}</p>
          </section>

          <section className="border-t border-border pt-6">
            <p className="text-sm text-ink-dim">{overOns.afsluiter.dank}</p>
            <p className="mt-2 text-sm text-ink-dim">{overOns.afsluiter.tekst}</p>
            <p className="mt-4 text-sm text-ink">
              {overOns.afsluiter.groet}
              <br />
              {overOns.afsluiter.naam}
            </p>
          </section>
        </div>
      </main>
    </>
  );
}
