import Link from "next/link";
import { Header } from "@/components/Header";
import { HelpOnsStappen } from "@/components/HelpOnsStappen";
import { Verzendknop } from "@/components/Verzendknop";
import { requireIngelogd } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { ALLE_VRAGEN, ENQUETE, type EnqueteAntwoorden } from "@/inhoud/enquete";
import { stuurEnqueteIn } from "./acties";

/*
  De enquête (Kim, 5 november 2026).

  Privé: alleen Kim leest de antwoorden. Daarom staat ze los van het
  reviewbord, dat voor iedereen is. Ze vraagt geen toegang tot de betalende
  hoofdstukken, enkel een account: ook een tester wiens testmaand voorbij is,
  moet ze nog kunnen invullen.

  Wie al instuurde, ziet zijn antwoorden terug en mag ze aanpassen.
*/

export const dynamic = "force-dynamic";

export const metadata = {
  title: "Enquête — Oefenplatform Connectopia",
  robots: { index: false },
};

const veld =
  "w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest";

export default async function EnquetePage({
  searchParams,
}: {
  searchParams: Promise<{ melding?: string; fout?: string }>;
}) {
  const { melding, fout } = await searchParams;
  const session = await requireIngelogd();
  const supabase = await createClient();

  const { data: bestaand } = await supabase
    .from("enquetes")
    .select("antwoorden")
    .eq("profile_id", session.userId)
    .maybeSingle();
  const vorige = (bestaand?.antwoorden ?? {}) as EnqueteAntwoorden;

  // Doorlopende nummers over alle delen heen.
  const nummerVan = new Map(ALLE_VRAGEN.map((v, i) => [v.sleutel, i + 1]));

  return (
    <>
      <Header naam={session.profile?.full_name} rol={session.profile?.role} />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">📝 Help ons beter worden</h1>
        <p className="mt-2 max-w-2xl text-sm text-ink-dim">
          Een tiental minuten, over wat goed werkte en wat beter kan. Alleen wij lezen je
          antwoorden, ze komen nergens op het platform te staan. Wees gerust kritisch: net daar
          hebben we het meest aan.
        </p>

        <HelpOnsStappen userId={session.userId} />

        {melding === "bedankt" && (
          <div className="mt-5 max-w-2xl rounded-md bg-forest/10 px-4 py-3 text-sm text-forest-dark">
            <p className="font-semibold">Dank je wel! Je antwoorden zijn goed aangekomen.</p>
            <p className="mt-1">
              Schreef je al een review?{" "}
              <Link href="/reviews#schrijf" className="underline underline-offset-2">
                Dat kan op het reviewbord
              </Link>
              . Je antwoorden hieronder kan je nog altijd aanpassen.
            </p>
          </div>
        )}
        {fout && (
          <p className="mt-5 max-w-2xl rounded-md bg-danger/10 px-4 py-3 text-sm text-danger">
            {fout}
          </p>
        )}

        <form action={stuurEnqueteIn} className="mt-8 grid gap-8">
          {ENQUETE.map((deel) => (
            <fieldset
              key={deel.titel}
              className="rounded-xl border border-border bg-surface p-6"
            >
              <legend className="px-2 font-display text-lg font-semibold text-ink">
                {deel.titel}
              </legend>

              <div className="grid gap-6">
                {deel.vragen.map((v) => {
                  const nummer = nummerVan.get(v.sleutel);
                  const kop = (
                    <span className="text-sm font-medium text-ink">
                      {nummer}. {v.vraag}
                      {v.verplicht ? <span className="text-danger"> *</span> : null}
                    </span>
                  );
                  const eerder = vorige[v.sleutel];

                  if (v.soort === "keuze") {
                    return (
                      <div key={v.sleutel} className="grid gap-2">
                        {kop}
                        <div className="flex flex-wrap gap-x-5 gap-y-2">
                          {v.opties.map((o) => (
                            <label key={o} className="flex items-center gap-2 text-sm text-ink">
                              <input
                                type="radio"
                                name={v.sleutel}
                                value={o}
                                required={v.verplicht}
                                defaultChecked={eerder === o}
                                className="accent-forest"
                              />
                              {o}
                            </label>
                          ))}
                        </div>
                      </div>
                    );
                  }

                  if (v.soort === "meerdere") {
                    const gekozen = Array.isArray(eerder) ? eerder : [];
                    return (
                      <div key={v.sleutel} className="grid gap-2">
                        {kop}
                        <span className="text-xs text-ink-dim">Meerdere antwoorden mogen.</span>
                        <div className="grid gap-2 sm:grid-cols-3">
                          {v.opties.map((o) => (
                            <label key={o} className="flex items-center gap-2 text-sm text-ink">
                              <input
                                type="checkbox"
                                name={v.sleutel}
                                value={o}
                                defaultChecked={gekozen.includes(o)}
                                className="accent-forest"
                              />
                              {o}
                            </label>
                          ))}
                        </div>
                      </div>
                    );
                  }

                  if (v.soort === "score") {
                    const stappen = Array.from({ length: v.tot - v.van + 1 }, (_, i) => v.van + i);
                    return (
                      <div key={v.sleutel} className="grid gap-2">
                        {kop}
                        <div className="flex flex-wrap items-center gap-2 text-xs text-ink-dim">
                          <span>{v.laag}</span>
                          {stappen.map((n) => (
                            <label
                              key={n}
                              className="flex cursor-pointer flex-col items-center rounded-md border border-border bg-paper px-2.5 py-1.5 text-sm text-ink has-[:checked]:border-forest has-[:checked]:bg-forest/10"
                            >
                              <input
                                type="radio"
                                name={v.sleutel}
                                value={n}
                                required={v.verplicht}
                                defaultChecked={eerder === String(n)}
                                className="sr-only"
                              />
                              {n}
                            </label>
                          ))}
                          <span>{v.hoog}</span>
                        </div>
                      </div>
                    );
                  }

                  return (
                    <label key={v.sleutel} className="grid gap-1">
                      {kop}
                      {v.hulp && <span className="text-xs text-ink-dim">{v.hulp}</span>}
                      <textarea
                        name={v.sleutel}
                        rows={v.minimum ? 4 : 2}
                        required={v.verplicht}
                        minLength={v.minimum}
                        maxLength={3000}
                        defaultValue={typeof eerder === "string" ? eerder : ""}
                        className={veld}
                      />
                    </label>
                  );
                })}
              </div>
            </fieldset>
          ))}

          <p className="text-xs text-ink-dim">
            <span className="text-danger">*</span> verplicht. Bij de grote open vragen vragen we
            een paar zinnen.
          </p>

          <Verzendknop
            label={bestaand ? "Aanpassingen bewaren" : "Enquête insturen"}
            bezigLabel="Bezig met versturen…"
            className="justify-self-start rounded-md bg-forest px-5 py-2.5 text-sm font-medium text-white transition hover:bg-forest-dark"
          />
        </form>
      </main>
    </>
  );
}
