import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import { Kopieer } from "../Kopieer";
import {
  KOLOMMEN,
  adressenVan,
  alsTabel,
  maakGroepen,
  vindWaarde,
  type Aanvraag,
} from "@/lib/aanvraaglijsten";

/* Er kan elk moment een inschrijving bijkomen, dus niets bewaren. */
export const dynamic = "force-dynamic";

/*
  Eén lijst per kampdag, met de kinderen die erop staan.

  De lijst hiernaast, /beheer/aanvragen, toont elke aanvraag apart: goed om
  iemand terug te mailen, maar je ziet er niet in één oogopslag wie er maandag
  voor je staat. Deze pagina draait het om: ze groepeert op wat een gezin
  aankruiste. Wie twee dagen aanvinkt, staat op allebei de lijsten.

  Alle rekenwerk staat in lib/aanvraaglijsten.ts, zodat deze pagina enkel nog
  over de opmaak gaat.
*/
export default async function LijstenBeheer({
  searchParams,
}: {
  searchParams: Promise<{ onderwerp?: string }>;
}) {
  const session = await requireBeheerder();
  const { onderwerp: gekozen = "" } = await searchParams;
  const naam = session.profile?.full_name ?? session.email ?? "";

  const db = createAdminClient();
  const { data, error } = await db
    .from("aanvragen")
    .select("id, onderwerp, soort, gegevens, gezien, afgehandeld, created_at")
    .order("created_at", { ascending: false })
    .limit(1000);

  const alles = (data ?? []) as Aanvraag[];
  const onderwerpen = [...new Set(alles.map((a) => a.onderwerp))].sort((a, b) =>
    a.localeCompare(b, "nl"),
  );
  const gefilterd = gekozen
    ? alles.filter((a) => a.onderwerp === gekozen)
    : alles;
  const groepen = maakGroepen(gefilterd);

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
          Lijsten per kamp
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          Wie welke dag aankruiste, met de gegevens die je die dag nodig hebt.
          Een kind dat twee dagen koos, staat op allebei de lijsten.
        </p>

        {/* De twee manieren om naar dezelfde aanvragen te kijken. */}
        <div className="mt-4 flex flex-wrap gap-2 print:hidden">
          <a
            href="/beheer/aanvragen"
            className="rounded-full border border-border px-3 py-1 text-sm text-ink-dim transition hover:border-forest hover:text-forest-dark"
          >
            Alle aanvragen
          </a>
          <span className="rounded-full bg-forest px-3 py-1 text-sm text-white">
            Lijsten per kamp
          </span>
        </div>

        {onderwerpen.length > 1 && (
          <div className="mt-3 flex flex-wrap gap-2 print:hidden">
            <a
              href="/beheer/aanvragen/lijsten"
              className={`rounded-full px-3 py-1 text-sm transition ${
                gekozen
                  ? "border border-border text-ink-dim hover:border-forest hover:text-forest-dark"
                  : "bg-forest text-white"
              }`}
            >
              Alle soorten
            </a>
            {onderwerpen.map((soort) => (
              <a
                key={soort}
                href={`/beheer/aanvragen/lijsten?onderwerp=${encodeURIComponent(soort)}`}
                className={`rounded-full px-3 py-1 text-sm transition ${
                  gekozen === soort
                    ? "bg-forest text-white"
                    : "border border-border text-ink-dim hover:border-forest hover:text-forest-dark"
                }`}
              >
                {soort.replace(/\s*via de website\s*/i, " ").trim()}
              </a>
            ))}
          </div>
        )}

        {error && (
          <div className="mt-6 rounded-lg border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            <p className="font-medium">Deze lijst kan nog niet gelezen worden.</p>
            <p className="mt-2 text-ink-dim">
              Waarschijnlijk staat de tabel er nog niet. Open Supabase, ga naar
              de SQL Editor en voer het bestand{" "}
              <code className="rounded bg-ink/5 px-1">
                website/supabase/aanvragen.sql
              </code>{" "}
              uit.
            </p>
            <p className="mt-2 text-xs text-ink-dim">{error.message}</p>
          </div>
        )}

        {!error && groepen.length === 0 && (
          <p className="mt-6 text-sm text-ink-dim">
            Er is nog niemand die een dag aankruiste. Zodra er iemand inschrijft
            voor een kampdag, staat die lijst hier.
          </p>
        )}

        <p className="mt-6 text-xs text-ink-dim print:hidden">
          Tip: wil je zo&apos;n lijst op papier, druk de pagina dan af met
          ctrl+p. De knopjes worden dan niet meegeprint.
        </p>

        <div className="mt-4 space-y-6">
          {groepen.map((groep) => {
            const adressen = adressenVan(groep.aanvragen);
            const open = groep.aanvragen.filter((a) => !a.afgehandeld).length;
            return (
              <section
                key={groep.naam}
                className="rounded-lg border border-border bg-surface p-5 print:break-inside-avoid"
              >
                <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
                  <h2 className="font-display text-lg font-semibold text-ink">
                    {groep.naam}
                  </h2>
                  <p className="text-sm text-ink-dim">
                    {groep.aanvragen.length}{" "}
                    {groep.aanvragen.length === 1 ? "kind" : "kinderen"}
                    {open > 0 && ` · ${open} nog niet afgehandeld`}
                  </p>
                </div>
                {groep.onderwerpen.length === 1 && (
                  <p className="mt-0.5 text-xs text-ink-dim">
                    {groep.onderwerpen[0]}
                  </p>
                )}

                <div className="mt-3 overflow-x-auto">
                  <table className="w-full min-w-[34rem] border-collapse text-sm">
                    <thead>
                      <tr className="border-b border-border text-left">
                        {KOLOMMEN.map((kolom) => (
                          <th
                            key={kolom.kop}
                            className="py-1.5 pr-4 font-medium text-ink-dim"
                          >
                            {kolom.kop}
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {groep.aanvragen.map((aanvraag) => {
                        const boodschap = vindWaarde(
                          aanvraag.gegevens,
                          "vraag of boodschap",
                        );
                        return (
                          <tr
                            key={aanvraag.id}
                            className="border-b border-border/60 align-top last:border-0"
                          >
                            {KOLOMMEN.map((kolom, i) => (
                              <td
                                key={kolom.kop}
                                className={`py-1.5 pr-4 ${
                                  i === 0 ? "font-medium text-ink" : "text-ink-dim"
                                }`}
                              >
                                {vindWaarde(aanvraag.gegevens, kolom.woord) ?? "—"}
                                {i === 0 && aanvraag.afgehandeld && (
                                  <span className="ml-1.5 text-xs font-normal text-ink-dim">
                                    afgehandeld
                                  </span>
                                )}
                                {i === 0 && boodschap && (
                                  <p className="mt-0.5 text-xs font-normal text-ink-dim">
                                    {boodschap}
                                  </p>
                                )}
                              </td>
                            ))}
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>

                <div className="mt-4 flex flex-wrap gap-2 print:hidden">
                  <Kopieer
                    waarde={alsTabel(groep)}
                    wat={`de lijst van ${groep.naam}`}
                    label="Kopieer de lijst"
                    stijl="vol"
                  />
                  {adressen.length > 0 && (
                    <Kopieer
                      waarde={adressen.join("; ")}
                      wat={`de ${adressen.length} mailadressen van ${groep.naam}`}
                      label={`Kopieer de ${adressen.length} mailadressen`}
                    />
                  )}
                </div>
                <p className="mt-1.5 text-xs text-ink-dim print:hidden">
                  De lijst plak je zo in een rekenblad: elke kolom komt apart te
                  staan. De adressen horen in het bcc-vak.
                </p>
              </section>
            );
          })}
        </div>
      </main>
    </>
  );
}
