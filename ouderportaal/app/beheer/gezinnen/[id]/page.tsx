import { notFound } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { FicheRegels } from "@/components/FicheRegels";
import { type Kind, KINDVELDEN, watOntbreekt } from "@/lib/kind";
import { FicheStand } from "@/components/FicheStand";
import {
  upsertToegang,
  verwijderGezin,
  wijzigWachtwoord,
  wijzigKindAlsBeheerder,
  voegKindToeAlsBeheerder,
} from "../actions";
import { KindVelden } from "@/components/KindVelden";
import { zetDeelnames } from "../../activiteiten/actions";
import { mailadresVan } from "@/lib/mailadressen";
import { Kopieer } from "../../aanvragen/Kopieer";
import {
  dagTekst,
  datumTekst,
  sorteer,
  type Activiteit,
} from "@/lib/activiteiten";
import { startMeekijken } from "@/app/portaal/meekijken-actions";

export default async function GezinDetailPage({
  params,
  searchParams,
}: {
  params: Promise<{ id: string }>;
  searchParams: Promise<{ succes?: string; fout?: string }>;
}) {
  const { id } = await params;
  const { succes, fout } = await searchParams;
  const session = await requireBeheerder();
  const naam = session.profile?.full_name ?? session.email ?? "";

  const supabase = await createClient();
  const [
    { data: gezin },
    { data: klasjes },
    { data: toegangData },
    { data: kinderen },
  ] = await Promise.all([
    supabase
      .from("profiles")
      .select("id, full_name, telefoon, adres")
      .eq("id", id)
      .single(),
    supabase.from("klasjes").select("id, naam").order("naam"),
    supabase
      .from("toegang")
      .select("klasje_id, materiaal, fotos")
      .eq("profile_id", id),
    supabase
      .from("kinderen")
      .select(KINDVELDEN)
      .eq("profile_id", id)
      .order("naam"),
  ]);

  if (!gezin) notFound();

  /* Het mailadres staat niet in profiles maar in auth.users; zie
     lib/mailadressen.ts. */
  const mailadres = await mailadresVan(id);

  /*
    Bij welke kampen en lessen hoort elk kind van dit gezin? Kim vroeg dat op
    11 oktober 2026: aanduiden bij de fiche zelf, en een kind mag bij
    verschillende dingen staan. Het archief laten we weg; dat zijn de kampen
    die voorbij zijn.
  */
  const kindIds = ((kinderen as Kind[] | null) ?? []).map((k) => k.id);
  const [{ data: activiteitenData }, { data: deelnamesData }] =
    await Promise.all([
      supabase
        .from("activiteiten")
        .select("id, naam, soort, datum, plaats, archief")
        .eq("archief", false),
      kindIds.length
        ? supabase
            .from("deelnames")
            .select("kind_id, activiteit_id")
            .in("kind_id", kindIds)
        : Promise.resolve({ data: [] as { kind_id: string; activiteit_id: string }[] }),
    ]);

  /*
    Enkel wat nu loopt, anders staat er na een maand wekelijkse lessen een
    muur van vinkjes bij elk kind. Een dag van langer dan een week geleden
    blijft bereikbaar: op het blad van die activiteit zelf staat een keuzelijst
    om er een kind bij te zetten.
  */
  const grens = dagTekst(7);
  const activiteiten = sorteer(
    ((activiteitenData ?? []) as Activiteit[]).filter(
      (a) => !a.datum || a.datum >= grens,
    ),
  );
  const deelnamesPerKind = new Map<string, Set<string>>();
  for (const rij of (deelnamesData ?? []) as {
    kind_id: string;
    activiteit_id: string;
  }[]) {
    const huidig = deelnamesPerKind.get(rij.kind_id) ?? new Set<string>();
    huidig.add(rij.activiteit_id);
    deelnamesPerKind.set(rij.kind_id, huidig);
  }

  const toegangPerKlasje = new Map(
    (toegangData ?? []).map((t) => [
      t.klasje_id,
      { materiaal: t.materiaal, fotos: t.fotos },
    ]),
  );

  return (
    <>
      <Header
        naam={naam}
        rol="beheerder"
        terugHref="/beheer/gezinnen"
        terugLabel="Gezinnen"
      />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <h1 className="font-display text-2xl font-semibold text-ink">
            {gezin.full_name}
          </h1>
          {/* Het portaal bekijken zoals dit gezin het ziet, zonder uit te loggen. */}
          <form action={startMeekijken}>
            <input type="hidden" name="gezinId" value={gezin.id} />
            <button
              type="submit"
              className="rounded-md border border-forest px-3 py-2 text-sm font-medium text-forest-dark transition hover:bg-forest/5"
            >
              Bekijk het portaal zoals dit gezin het ziet
            </button>
          </form>
        </div>
        <p className="mt-1 text-sm text-ink-dim">
          Lesmateriaal en foto&apos;s staan hieronder los van elkaar — je kan
          het ene toestaan zonder het andere.
        </p>

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

        <section className="mt-6 rounded-xl border border-border bg-surface p-5">
          <h2 className="font-display text-base font-semibold text-ink">
            Contactgegevens
          </h2>
          <dl className="mt-2 space-y-1 text-sm text-ink-dim">
            <div>
              <dt className="inline font-medium text-ink">E-mail: </dt>
              <dd className="inline">
                {mailadres ?? "niet gevonden"}
              </dd>
              {mailadres && (
                <span className="ml-2 inline-block align-middle">
                  <Kopieer waarde={mailadres} wat="het mailadres" />
                </span>
              )}
            </div>
          </dl>
          {gezin.telefoon || gezin.adres ? (
            <dl className="mt-1 space-y-1 text-sm text-ink-dim">
              {gezin.telefoon && (
                <div>
                  <dt className="inline font-medium text-ink">Telefoon: </dt>
                  <dd className="inline">{gezin.telefoon}</dd>
                </div>
              )}
              {gezin.adres && (
                <div>
                  <dt className="inline font-medium text-ink">Adres: </dt>
                  <dd className="inline">{gezin.adres}</dd>
                </div>
              )}
            </dl>
          ) : (
            <p className="mt-1 text-sm text-ink-dim">
              Telefoon en adres zijn nog niet ingevuld door dit gezin.
            </p>
          )}
        </section>

        <section className="mt-4 rounded-xl border border-border bg-surface p-5">
          <h2 className="font-display text-base font-semibold text-ink">
            Inlichtingenfiche(s)
          </h2>
          {(kinderen ?? []).length === 0 && (
            <p className="mt-2 text-sm text-ink-dim">
              Nog geen kind toegevoegd door dit gezin.
            </p>
          )}
          <div className="mt-3 space-y-4">
            {((kinderen as Kind[] | null) ?? []).map((kind) => (
              <div
                key={kind.id}
                className="rounded-lg border border-border bg-paper p-4 text-sm"
              >
                <p className="font-display font-semibold text-ink">
                  {kind.naam}
                  {kind.geboortedatum && (
                    <span className="ml-2 font-sans text-xs font-normal text-ink-dim">
                      geboren{" "}
                      {new Date(kind.geboortedatum).toLocaleDateString("nl-BE")}
                    </span>
                  )}
                </p>
                {/* Groen of rood, net als op de lijst van de gezinnen: zo
                    zie je ook hier meteen of er nog iets moet gebeuren. */}
                <p className="mt-1.5">
                  <FicheStand ontbreekt={watOntbreekt(kind)} klein />
                </p>
                <div className="mt-2">
                  <FicheRegels kind={kind} />
                </div>
                <div className="mt-2 flex flex-wrap gap-2">
                  <span
                    className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${kind.toestemming_fotos ? "bg-forest/10 text-forest-dark" : "bg-danger/10 text-danger"}`}
                  >
                    {kind.toestemming_fotos
                      ? "Toestemming foto's"
                      : "Geen toestemming foto's"}
                  </span>
                  <span
                    className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${kind.toestemming_social_media ? "bg-forest/10 text-forest-dark" : "bg-danger/10 text-danger"}`}
                  >
                    {kind.toestemming_social_media
                      ? "Toestemming social media"
                      : "Geen toestemming social media"}
                  </span>
                </div>

                {/* De fiche hier meteen kunnen aanpassen. Vroeger kon dat enkel
                    door eerst met dit gezin mee te kijken, en dat is precies
                    hoe een fiche op het verkeerde profiel belandt. Dichtgeklapt,
                    want bij vijf kinderen wordt deze bladzijde anders eindeloos. */}
                <details className="mt-3 border-t border-border pt-3">
                  <summary className="cursor-pointer text-sm font-medium text-forest-dark">
                    Fiche aanpassen
                  </summary>
                  <KindVelden
                    action={wijzigKindAlsBeheerder}
                    kind={kind}
                    gezinId={gezin.id}
                    submitLabel="Bewaren"
                  />
                </details>

                {/* Waar hoort dit kind bij? Vink aan en bewaar; het kind komt
                    dan op de lijst van elk aangevinkt kamp of elke les. */}
                {activiteiten.length > 0 && (
                  <form action={zetDeelnames} className="mt-3 border-t border-border pt-3">
                    <input type="hidden" name="kind_id" value={kind.id} />
                    <input type="hidden" name="profile_id" value={gezin.id} />
                    <p className="text-xs font-medium text-ink">
                      Hoort bij
                    </p>
                    <div className="mt-1.5 grid gap-1 sm:grid-cols-2">
                      {activiteiten.map((activiteit) => (
                        <label
                          key={activiteit.id}
                          className="flex items-start gap-1.5 text-sm text-ink-dim"
                        >
                          <input type="hidden" name="alle" value={activiteit.id} />
                          <input
                            type="checkbox"
                            name="activiteit"
                            value={activiteit.id}
                            defaultChecked={deelnamesPerKind
                              .get(kind.id)
                              ?.has(activiteit.id)}
                            className="mt-1 h-4 w-4 shrink-0 accent-forest"
                          />
                          <span>
                            {activiteit.naam}
                            {datumTekst(activiteit.datum) && (
                              <span className="block text-xs text-ink-dim">
                                {datumTekst(activiteit.datum)}
                              </span>
                            )}
                          </span>
                        </label>
                      ))}
                    </div>
                    <button
                      type="submit"
                      className="mt-2 rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
                    >
                      Bewaren
                    </button>
                  </form>
                )}
              </div>
            ))}
          </div>

          {/* Een gezin dat zijn fiche niet zelf invult, kan Kim er hier zelf
              bij zetten in plaats van eerst mee te moeten kijken. */}
          <details className="mt-4 rounded-lg border border-dashed border-border-strong bg-surface p-4">
            <summary className="cursor-pointer text-sm font-medium text-forest-dark">
              Kind toevoegen
            </summary>
            <KindVelden
              action={voegKindToeAlsBeheerder}
              gezinId={gezin.id}
              submitLabel="Toevoegen"
            />
          </details>
        </section>

        <div className="mt-6 space-y-3">
          {(klasjes ?? []).map((k) => {
            const huidig = toegangPerKlasje.get(k.id) ?? {
              materiaal: false,
              fotos: false,
            };
            return (
              <form
                key={k.id}
                action={upsertToegang}
                className="flex flex-wrap items-center justify-between gap-3 rounded-lg border border-border bg-surface p-4"
              >
                <input type="hidden" name="profile_id" value={gezin.id} />
                <input type="hidden" name="klasje_id" value={k.id} />
                <p className="font-medium text-ink">{k.naam}</p>
                <div className="flex items-center gap-4 text-sm">
                  <label className="flex items-center gap-1.5">
                    <input
                      type="checkbox"
                      name="materiaal"
                      defaultChecked={huidig.materiaal}
                    />
                    Lesmateriaal
                  </label>
                  <label className="flex items-center gap-1.5">
                    <input
                      type="checkbox"
                      name="fotos"
                      defaultChecked={huidig.fotos}
                    />
                    Foto&apos;s
                  </label>
                  <button
                    type="submit"
                    className="rounded-md bg-forest px-3 py-1.5 font-medium text-white hover:bg-forest-dark"
                  >
                    Bewaren
                  </button>
                </div>
              </form>
            );
          })}
          {(klasjes ?? []).length === 0 && (
            <p className="text-sm text-ink-dim">
              Maak eerst een klasje aan onder Beheer.
            </p>
          )}
        </div>

        <form
          action={wijzigWachtwoord}
          className="mt-10 border-t border-border pt-6"
        >
          <input type="hidden" name="profile_id" value={gezin.id} />
          <h2 className="font-display text-lg font-semibold text-ink">
            Wachtwoord wijzigen
          </h2>
          <p className="mt-1 text-sm text-ink-dim">
            Stel een nieuw wachtwoord in voor dit gezin en geef dat opnieuw
            veilig aan hen door.
          </p>
          <div className="mt-3 flex gap-2">
            <input
              name="wachtwoord"
              type="text"
              minLength={8}
              required
              placeholder="Nieuw wachtwoord (min. 8 tekens)"
              className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
            <button
              type="submit"
              className="shrink-0 rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Bijwerken
            </button>
          </div>
        </form>

        <form
          action={verwijderGezin}
          className="mt-10 border-t border-border pt-6"
        >
          <input type="hidden" name="profile_id" value={gezin.id} />
          <p className="text-sm text-ink-dim">
            Verwijder dit account volledig, bijvoorbeeld als het kind stopt. Dit
            kan niet ongedaan gemaakt worden.
          </p>
          <button
            type="submit"
            className="mt-2 rounded-md border border-danger px-3 py-1.5 text-sm font-medium text-danger hover:bg-danger/10"
          >
            Gezin verwijderen
          </button>
        </form>
      </main>
    </>
  );
}
