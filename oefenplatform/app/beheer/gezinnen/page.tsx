import Link from "next/link";
import { Header } from "@/components/Header";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { huidigSchooljaar } from "@/lib/schooljaar";
import { Mailadressen, type MailRij } from "./Mailadressen";
import { Gezinslijst, type CodeRij, type GezinRij } from "./Gezinslijst";

type Rij = {
  id: string;
  full_name: string;
  role: string;
  is_plusklas: boolean;
  toegang_schooljaar: string | null;
  plusklas_code: string | null;
  created_at: string;
  kinderen: { id: string; naam: string }[] | null;
};

export const metadata = { title: "Gezinnen — Oefenplatform Connectopia" };

function datum(waarde: string) {
  return new Date(waarde).toLocaleDateString("nl-BE", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
}

export default async function GezinnenPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; melding?: string; toon?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout, melding, toon } = await searchParams;

  /* Met de service-sleutel, want we willen ook accounts zonder kind zien. */
  const admin = createAdminClient();
  const [{ data }, { data: codesData }] = await Promise.all([
    admin
      .from("profiles")
      .select(
        "id, full_name, role, is_plusklas, toegang_schooljaar, plusklas_code, created_at, kinderen(id, naam)",
      )
      .order("created_at", { ascending: false }),
    admin
      .from("plusklas_codes")
      .select("code, label, actief")
      .order("created_at", { ascending: false }),
  ]);

  const rijen = (data ?? []) as Rij[];
  const gezinnen = rijen.filter((r) => r.role !== "beheerder");
  const codes = (codesData ?? []) as CodeRij[];
  const schooljaar = huidigSchooljaar();
  const heeftToegang = (r: Rij) =>
    r.is_plusklas || r.toegang_schooljaar === schooljaar;

  /* Het mailadres staat niet in "profiles" maar in auth.users, en dat is enkel
     met de service-sleutel te lezen. Eén oproep, en daarna zoeken we per id. */
  const mailPerId = new Map<string, string>();
  for (let bladzijde = 1; bladzijde <= 10; bladzijde++) {
    const { data: lijst, error } = await admin.auth.admin.listUsers({
      page: bladzijde,
      perPage: 200,
    });
    const gebruikers = lijst?.users ?? [];
    for (const u of gebruikers) if (u.email) mailPerId.set(u.id, u.email);
    if (error || gebruikers.length < 200) break;
  }

  const mailrijen: MailRij[] = gezinnen
    .map((r) => ({
      naam: r.full_name,
      email: mailPerId.get(r.id) ?? "",
      toegang: heeftToegang(r),
    }))
    .filter((r) => r.email);

  const lijstrijen: GezinRij[] = gezinnen.map((r) => ({
    id: r.id,
    naam: r.full_name,
    email: mailPerId.get(r.id) ?? "",
    rol: r.role,
    isPlusklas: r.is_plusklas,
    betaald: r.toegang_schooljaar === schooljaar,
    toegangSchooljaar: r.toegang_schooljaar,
    code: r.plusklas_code,
    sinds: datum(r.created_at),
    kinderen: (r.kinderen ?? []).map((k) => k.naam),
  }));

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          Gezinnen
        </h1>
        <p className="mt-2 text-sm text-ink-dim">
          Wie heeft volledige toegang, en waar komt die vandaan? Toegang
          uitzetten raakt niets van wat een gezin opgebouwd heeft: de kinderen,
          hun voortgang en hun stickers blijven staan, ze zien daarna enkel nog
          de gratis hoofdstukken. Zet je de toegang later weer aan, dan pikken
          ze op waar ze gestopt waren.
        </p>
        <p className="mt-2 text-sm text-ink-dim">
          Een gezin dat betaald heeft voor dit schooljaar ({schooljaar}) houdt
          zijn toegang, ook als de knop hier op uit staat. Die knop gaat enkel
          over de gratis toegang die je zelf geeft, bijvoorbeeld met een code.
        </p>
        <p className="mt-2 text-sm text-ink-dim">
          Onderaan elk gezin staat met welke code het binnenkwam. Die code
          bepaalt in welke lijst het gezin staat bij Opvolging, en zegt niets
          over de toegang.
        </p>

        {fout && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            {fout}
          </p>
        )}
        {melding && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">
            {melding}
          </p>
        )}

        <Mailadressen rijen={mailrijen} />

        {/* ?toon=open komt van de teller bovenaan Beheer: dan staat de lijst
            meteen op de accounts die enkel de gratis hoofdstukken zien. */}
        <Gezinslijst rijen={lijstrijen} codes={codes} start={toon} />
      </main>
    </>
  );
}
