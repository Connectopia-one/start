import { requireIngelogd } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { wijzigContactgegevens, voegKindToe, wijzigKind, verwijderKind } from "./actions";

type Kind = {
  id: string;
  naam: string;
  geboortedatum: string | null;
  allergieen: string | null;
  diagnoses: string | null;
  noodcontact_naam: string | null;
  noodcontact_telefoon: string | null;
  toestemming_fotos: boolean;
  toestemming_social_media: boolean;
};

export default async function GezinProfielPage() {
  const session = await requireIngelogd();
  const naam = session.profile?.full_name ?? session.email ?? "";
  const isBeheerder = session.profile?.role === "beheerder";

  const supabase = await createClient();
  const [{ data: profiel }, { data: kinderenData }] = await Promise.all([
    supabase.from("profiles").select("telefoon, adres").eq("id", session.userId).single(),
    supabase
      .from("kinderen")
      .select(
        "id, naam, geboortedatum, allergieen, diagnoses, noodcontact_naam, noodcontact_telefoon, toestemming_fotos, toestemming_social_media"
      )
      .eq("profile_id", session.userId)
      .order("naam"),
  ]);

  const kinderen = (kinderenData as Kind[] | null) ?? [];

  return (
    <>
      <Header naam={naam} isBeheerder={isBeheerder} terugHref="/portaal" terugLabel="Overzicht" />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">Mijn gezin</h1>
        <p className="mt-1 text-sm text-ink-dim">
          Contactgegevens en de inlichtingenfiche van je kind(eren) — enkel zichtbaar voor jou en
          Connectopia.
        </p>

        <section className="mt-8 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">Contactgegevens</h2>
          <form action={wijzigContactgegevens} className="mt-4 space-y-4">
            <div className="space-y-1.5">
              <label htmlFor="telefoon" className="text-sm font-medium text-ink">
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
          <h2 className="font-display text-lg font-semibold text-ink">Inlichtingenfiche(s)</h2>
          <div className="mt-4 space-y-4">
            {kinderen.map((kind) => (
              <KindForm key={kind.id} kind={kind} />
            ))}
          </div>

          <div className="mt-6 rounded-xl border border-dashed border-border-strong bg-surface p-6">
            <h3 className="font-display text-base font-semibold text-ink">Kind toevoegen</h3>
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
        <h3 className="font-display text-base font-semibold text-ink">{kind.naam}</h3>
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

function KindVelden({
  action,
  kind,
  submitLabel,
}: {
  action: (formData: FormData) => void | Promise<void>;
  kind?: Kind;
  submitLabel: string;
}) {
  return (
    <form action={action} className="mt-4 space-y-4">
      {kind && <input type="hidden" name="kind_id" value={kind.id} />}

      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">Naam kind</label>
          <input
            name="naam"
            required
            defaultValue={kind?.naam ?? ""}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">Geboortedatum</label>
          <input
            name="geboortedatum"
            type="date"
            defaultValue={kind?.geboortedatum ?? ""}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">Allergieën</label>
        <textarea
          name="allergieen"
          rows={2}
          defaultValue={kind?.allergieen ?? ""}
          placeholder="Bv. noten, penicilline — of laat leeg indien niet van toepassing"
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">Diagnoses / aandachtspunten</label>
        <textarea
          name="diagnoses"
          rows={2}
          defaultValue={kind?.diagnoses ?? ""}
          placeholder="Bv. ADHD, ASS, HB — wat wij als begeleiders goed zouden moeten weten"
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">Noodcontact — naam</label>
          <input
            name="noodcontact_naam"
            defaultValue={kind?.noodcontact_naam ?? ""}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">Noodcontact — telefoon</label>
          <input
            name="noodcontact_telefoon"
            type="tel"
            defaultValue={kind?.noodcontact_telefoon ?? ""}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
      </div>

      <div className="space-y-2 rounded-md bg-paper p-3">
        <label className="flex items-start gap-2 text-sm">
          <input
            type="checkbox"
            name="toestemming_fotos"
            defaultChecked={kind?.toestemming_fotos ?? false}
            className="mt-0.5"
          />
          <span>
            Ik geef toestemming om foto&apos;s van mijn kind te maken en te delen binnen het
            ouderportaal (klasje, kamp).
          </span>
        </label>
        <label className="flex items-start gap-2 text-sm">
          <input
            type="checkbox"
            name="toestemming_social_media"
            defaultChecked={kind?.toestemming_social_media ?? false}
            className="mt-0.5"
          />
          <span>
            Ik geef toestemming om foto&apos;s van mijn kind te gebruiken op de publieke website
            of social media van Connectopia.
          </span>
        </label>
      </div>

      <button
        type="submit"
        className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
      >
        {submitLabel}
      </button>
    </form>
  );
}
