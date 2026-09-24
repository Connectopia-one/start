import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import { markeerAllesGezien, verwijderAanvraag, zetAfgehandeld } from "./actions";

/* Aanvragen komen binnen terwijl je kijkt, dus niets bewaren. */
export const dynamic = "force-dynamic";

type Aanvraag = {
  id: string;
  onderwerp: string;
  soort: string;
  gegevens: Record<string, string>;
  gezien: boolean;
  afgehandeld: boolean;
  created_at: string;
};

function tijdstip(waarde: string) {
  return new Date(waarde).toLocaleString("nl-BE", {
    day: "numeric",
    month: "long",
    hour: "2-digit",
    minute: "2-digit",
  });
}

/*
  Uit de antwoorden halen we het mailadres en het telefoonnummer naar boven,
  want dat is wat je nodig hebt om iemand terug te contacteren. De namen van
  de vakjes staan in website/content/formulier.ts; herkennen op een woord in
  de vraag werkt ook als die vraag ooit anders geformuleerd wordt.
*/
function vindWaarde(gegevens: Record<string, string>, woord: string) {
  const sleutel = Object.keys(gegevens).find((k) =>
    k.toLowerCase().includes(woord)
  );
  return sleutel ? gegevens[sleutel] : null;
}

export default async function AanvragenBeheer({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; succes?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout, succes } = await searchParams;
  const naam = session.profile?.full_name ?? session.email ?? "";

  const db = createAdminClient();
  const { data, error } = await db
    .from("aanvragen")
    .select("id, onderwerp, soort, gegevens, gezien, afgehandeld, created_at")
    .order("created_at", { ascending: false })
    .limit(300);

  const aanvragen = (data ?? []) as Aanvraag[];
  const nieuw = aanvragen.filter((a) => !a.gezien).length;
  const open = aanvragen.filter((a) => !a.afgehandeld).length;

  return (
    <>
      <Header
        naam={naam}
        rol="beheerder"
        terugHref="/beheer"
        terugLabel="Beheer"
      />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">
          Aanvragen van de website
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {aanvragen.length} aanvra{aanvragen.length === 1 ? "ag" : "gen"}
          {nieuw > 0 ? ` · ${nieuw} nieuw` : ""}
          {open > 0 ? ` · ${open} nog open` : ""}
        </p>

        {/* Staat de tabel er nog niet, dan zeggen we wat er moet gebeuren in
            plaats van een leeg scherm te tonen. */}
        {error && (
          <div className="mt-6 rounded-lg border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            <p className="font-medium">Deze lijst kan nog niet gelezen worden.</p>
            <p className="mt-2 text-ink-dim">
              Waarschijnlijk staat de tabel er nog niet. Open Supabase, ga naar
              de SQL Editor en voer het bestand{" "}
              <code className="rounded bg-ink/5 px-1">
                website/supabase/aanvragen.sql
              </code>{" "}
              uit. Daarna verschijnen de aanvragen hier vanzelf.
            </p>
            <p className="mt-2 text-xs text-ink-dim">{error.message}</p>
          </div>
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

        {nieuw > 0 && (
          <form action={markeerAllesGezien} className="mt-4">
            <button
              type="submit"
              className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
            >
              Alles als gelezen markeren
            </button>
          </form>
        )}

        {!error && !aanvragen.length && (
          <p className="mt-6 text-sm text-ink-dim">
            Er is nog niets binnengekomen.
          </p>
        )}

        <ul className="mt-6 space-y-3">
          {aanvragen.map((aanvraag) => {
            const mail = vindWaarde(aanvraag.gegevens, "mail");
            const gsm = vindWaarde(aanvraag.gegevens, "gsm");
            return (
              <li
                key={aanvraag.id}
                className={`rounded-lg border bg-surface p-4 ${
                  aanvraag.afgehandeld
                    ? "border-border opacity-70"
                    : aanvraag.gezien
                      ? "border-border"
                      : "border-forest/50"
                }`}
              >
                <div className="flex flex-wrap items-start justify-between gap-2">
                  <div>
                    <p className="font-medium text-ink">{aanvraag.onderwerp}</p>
                    <p className="mt-0.5 text-xs text-ink-dim">
                      {tijdstip(aanvraag.created_at)}
                      {!aanvraag.gezien && " · nieuw"}
                      {aanvraag.afgehandeld && " · afgehandeld"}
                    </p>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {mail && (
                      <a
                        href={`mailto:${mail}`}
                        className="rounded-md bg-forest px-3 py-1.5 text-sm font-medium text-white transition hover:bg-forest-dark"
                      >
                        Mailen
                      </a>
                    )}
                    {gsm && (
                      <a
                        href={`tel:${gsm.replace(/\s/g, "")}`}
                        className="rounded-md border border-border px-3 py-1.5 text-sm text-ink hover:border-forest"
                      >
                        Bellen
                      </a>
                    )}
                  </div>
                </div>

                <dl className="mt-3 grid gap-x-6 gap-y-1.5 sm:grid-cols-2">
                  {Object.entries(aanvraag.gegevens).map(([vraag, antwoord]) => (
                    <div key={vraag}>
                      <dt className="text-xs text-ink-dim">{vraag}</dt>
                      <dd className="text-sm text-ink">{antwoord}</dd>
                    </div>
                  ))}
                </dl>

                <div className="mt-4 flex flex-wrap gap-2">
                  <form action={zetAfgehandeld}>
                    <input type="hidden" name="id" value={aanvraag.id} />
                    <input
                      type="hidden"
                      name="afgehandeld"
                      value={aanvraag.afgehandeld ? "nee" : "ja"}
                    />
                    <button
                      type="submit"
                      className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
                    >
                      {aanvraag.afgehandeld
                        ? "Terug openzetten"
                        : "Afgehandeld"}
                    </button>
                  </form>
                  <form action={verwijderAanvraag}>
                    <input type="hidden" name="id" value={aanvraag.id} />
                    <button
                      type="submit"
                      className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-danger hover:text-danger"
                    >
                      Verwijderen
                    </button>
                  </form>
                </div>
              </li>
            );
          })}
        </ul>
      </main>
    </>
  );
}
