import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import { Kopieer } from "../Kopieer";
import {
  KOLOMMEN,
  MET_DE_HAND,
  adressenVan,
  alsTabel,
  maakGroepen,
  vindWaarde,
  waardeVan,
  type Aanvraag,
} from "@/lib/aanvraaglijsten";
import { verwijderKind, voegKindToe } from "./actions";

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
  searchParams: Promise<{ onderwerp?: string; fout?: string; succes?: string }>;
}) {
  const session = await requireBeheerder();
  const { onderwerp: gekozen = "", fout, succes } = await searchParams;
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
  /* Voor de vakjes van het formulier: elke dag die ooit aangekruist werd,
     ook als er nu op een andere soort gefilterd is. */
  const alleDagen = maakGroepen(alles);

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
          Lijsten uit de inschrijvingen
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          Wie welke dag aankruiste op het inschrijfformulier, plus de kinderen
          die je hieronder zelf toevoegt. Een kind dat twee dagen koos, staat op
          allebei de lijsten, en broers en zussen uit één inschrijving tellen
          elk apart. Dit is dus wat ouders
          vroegen; de lijst die je meeneemt, met de gegevens van de fiche,
          staat bij{" "}
          <Link
            href="/beheer/activiteiten"
            className="underline underline-offset-2"
          >
            Kampen en lessen
          </Link>
          .
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
            Lijsten uit de inschrijvingen
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

        {!error && (
          <details className="mt-6 rounded-lg border border-border bg-surface p-5 print:hidden">
            <summary className="cursor-pointer font-medium text-ink">
              Een kind met de hand toevoegen
            </summary>
            <p className="mt-2 text-sm text-ink-dim">
              Voor een kind dat niet via het formulier kwam, of dat er een dag
              bij wil. Het telt mee op elke dag die je aanvinkt. Enkel de naam
              en minstens één dag zijn nodig.
            </p>
            <form action={voegKindToe} className="mt-4 space-y-4">
              <div className="grid gap-3 sm:grid-cols-2">
                {[
                  ["kind", "Naam van het kind", true],
                  ["leeftijd", "Leeftijd", false],
                  ["ouder", "Ouder", false],
                  ["gsm", "Gsm", false],
                  ["mail", "E-mail", false],
                  ["gemeente", "Gemeente", false],
                ].map(([veld, label, nodig]) => (
                  <label key={veld as string} className="block text-sm">
                    <span className="text-ink-dim">{label}</span>
                    <input
                      name={veld as string}
                      required={nodig as boolean}
                      className="mt-1 w-full rounded-md border border-border bg-white px-3 py-1.5 text-ink"
                    />
                  </label>
                ))}
              </div>
              <label className="block text-sm">
                <span className="text-ink-dim">Opmerking (mag leeg)</span>
                <input
                  name="boodschap"
                  placeholder="bijvoorbeeld: zit in de plusklas"
                  className="mt-1 w-full rounded-md border border-border bg-white px-3 py-1.5 text-ink"
                />
              </label>
              <fieldset>
                <legend className="text-sm text-ink-dim">Welke dagen?</legend>
                <div className="mt-1 grid gap-1 sm:grid-cols-2">
                  {alleDagen.map((dag) => (
                    <label key={dag.naam} className="flex items-center gap-2 text-sm text-ink">
                      <input type="checkbox" name="dag" value={dag.naam} />
                      {dag.naam}
                      <input
                        type="hidden"
                        name={`onderwerp:${dag.naam}`}
                        value={dag.onderwerpen[0] ?? ""}
                      />
                    </label>
                  ))}
                </div>
                <label className="mt-2 block text-sm">
                  <span className="text-ink-dim">
                    Of een dag die hier nog niet staat
                  </span>
                  <input
                    name="nieuwe_dag"
                    placeholder="bijvoorbeeld: Hasselt maandag 21 december"
                    className="mt-1 w-full rounded-md border border-border bg-white px-3 py-1.5 text-ink"
                  />
                </label>
              </fieldset>
              <button
                type="submit"
                className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
              >
                Zet op de lijst
              </button>
            </form>
          </details>
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
            const open = groep.rijen.filter((r) => !r.aanvraag.afgehandeld).length;
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
                    {groep.rijen.length}{" "}
                    {groep.rijen.length === 1 ? "kind" : "kinderen"}
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
                      {groep.rijen.map((rij) => {
                        const aanvraag = rij.aanvraag;
                        const zelf = aanvraag.soort === MET_DE_HAND;
                        const boodschap = vindWaarde(
                          aanvraag.gegevens,
                          "vraag of boodschap",
                        );
                        return (
                          <tr
                            key={rij.sleutel}
                            className="border-b border-border/60 align-top last:border-0"
                          >
                            {KOLOMMEN.map((kolom, i) => (
                              <td
                                key={kolom.kop}
                                className={`py-1.5 pr-4 ${
                                  i === 0 ? "font-medium text-ink" : "text-ink-dim"
                                }`}
                              >
                                {waardeVan(rij, kolom.woord) ?? "—"}
                                {i === 0 && (zelf || aanvraag.afgehandeld) && (
                                  <span className="ml-1.5 text-xs font-normal text-ink-dim">
                                    {zelf ? "met de hand" : "afgehandeld"}
                                  </span>
                                )}
                                {i === 0 && boodschap && (
                                  <p className="mt-0.5 text-xs font-normal text-ink-dim">
                                    {boodschap}
                                  </p>
                                )}
                                {i === 0 && zelf && (
                                  <form action={verwijderKind} className="print:hidden">
                                    <input type="hidden" name="id" value={aanvraag.id} />
                                    <button
                                      type="submit"
                                      className="mt-0.5 text-xs font-normal text-danger underline underline-offset-2"
                                    >
                                      van alle lijsten halen
                                    </button>
                                  </form>
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
