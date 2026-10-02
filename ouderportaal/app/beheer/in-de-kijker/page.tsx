import { requireBeheerder } from "@/lib/auth";
import { createAdminClient, tabelOntbreekt } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import { BeeldForm, NieuwePostForm } from "./PostFormulieren";
import { markeerGezien, verwijderPost, zetZichtbaar } from "./actions";

/* De ingestuurde berichten komen binnen terwijl je kijkt, dus niets bewaren. */
export const dynamic = "force-dynamic";

type Post = {
  id: string;
  titel: string | null;
  tekst: string;
  van: string;
  kanaal: string;
  link: string;
  beeld: string | null;
  eigen: boolean;
  zichtbaar: boolean;
  gezien: boolean;
  volledige_naam: string | null;
  contact: string | null;
  created_at: string;
};

const KANAALNAAM: Record<string, string> = {
  facebook: "Facebook",
  instagram: "Instagram",
  linkedin: "LinkedIn",
  tiktok: "TikTok",
  youtube: "YouTube",
  anders: "Elders online",
};

function tijdstip(waarde: string) {
  return new Date(waarde).toLocaleString("nl-BE", {
    day: "numeric",
    month: "long",
    hour: "2-digit",
    minute: "2-digit",
  });
}

export default async function InDeKijkerBeheer({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; succes?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout, succes } = await searchParams;
  const naam = session.profile?.full_name ?? session.email ?? "";

  const db = createAdminClient();
  const { data, error } = await db
    .from("kijker_posts")
    .select(
      "id, titel, tekst, van, kanaal, link, beeld, eigen, zichtbaar, gezien, volledige_naam, contact, created_at",
    )
    .order("created_at", { ascending: false })
    .limit(200);

  /*
    Een leesfout mag niet stil blijven. Zonder dit stond er "0 berichten" op
    het scherm, ook als de tabel helemaal niet bestond, en dan valt er niets
    aan te zien wat er misloopt.
  */
  const leesfout = error
    ? tabelOntbreekt(error, "voor In de kijker", "website/supabase/social.sql") ??
      `De berichten konden niet gelezen worden: ${error.message}`
    : null;

  const posts = (data ?? []) as Post[];
  const nieuw = posts.filter((p) => !p.gezien).length;
  const wachtend = posts.filter((p) => !p.zichtbaar).length;

  /* Het webadres van een beeld in de open bak "social". */
  const beeldAdres = (pad: string) =>
    pad.startsWith("https://")
      ? pad
      : db.storage.from("social").getPublicUrl(pad).data.publicUrl;

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
          In de kijker
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {posts.length} bericht{posts.length === 1 ? "" : "en"}
          {nieuw > 0 ? ` · ${nieuw} nieuw` : ""}
          {wachtend > 0 ? ` · ${wachtend} wacht op jou` : ""}
        </p>
        <p className="mt-2 max-w-2xl text-sm text-ink-dim">
          Dit zijn de berichten op www.connectopia.one/in-de-kijker. Wat jij
          hieronder zelf toevoegt, staat er meteen op. Een bericht dat iemand
          anders instuurde, staat er pas op nadat jij het op de website zet.
        </p>

        {leesfout && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
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

        <section className="mt-6 rounded-lg border border-border bg-surface p-4">
          <h2 className="font-display text-lg font-semibold text-ink">
            Een bericht erbij zetten
          </h2>
          <NieuwePostForm />
        </section>

        {nieuw > 0 && (
          <form action={markeerGezien} className="mt-6">
            <button
              type="submit"
              className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
            >
              Alles als gezien markeren
            </button>
          </form>
        )}

        <ul className="mt-6 space-y-3">
          {posts.map((post) => (
            <li
              key={post.id}
              className={`rounded-lg border bg-surface p-4 ${
                post.gezien ? "border-border" : "border-forest"
              }`}
            >
              <div className="flex flex-wrap items-center gap-2 text-xs text-ink-dim">
                <span className="rounded-full bg-paper px-2 py-0.5 font-medium">
                  {KANAALNAAM[post.kanaal] ?? post.kanaal}
                </span>
                <span>{tijdstip(post.created_at)}</span>
                {!post.gezien && (
                  <span className="font-semibold text-forest-dark">nieuw</span>
                )}
                {post.zichtbaar ? (
                  <span className="font-semibold text-forest-dark">
                    staat op de website
                  </span>
                ) : (
                  <span className="font-semibold text-danger">
                    nog niet op de website
                  </span>
                )}
                {post.eigen && <span>van onszelf</span>}
              </div>

              {post.beeld && (
                /* eslint-disable-next-line @next/next/no-img-element */
                <img
                  src={beeldAdres(post.beeld)}
                  alt=""
                  className="mt-3 max-h-48 w-auto rounded-md border border-border"
                />
              )}

              {post.titel && (
                <p className="mt-2 font-semibold text-ink">{post.titel}</p>
              )}
              <p className="mt-1 whitespace-pre-line text-ink">{post.tekst}</p>

              <p className="mt-2 text-sm text-ink-dim">
                Op het kaartje als <strong>{post.van}</strong>
                {post.volledige_naam
                  ? ` · ingestuurd door ${post.volledige_naam}`
                  : ""}
                {post.contact ? ` · ${post.contact}` : ""}
              </p>

              <a
                href={post.link}
                target="_blank"
                rel="noopener noreferrer"
                className="mt-1 inline-block break-all text-sm text-forest-dark underline"
              >
                {post.link}
              </a>

              <BeeldForm id={post.id} heeftBeeld={Boolean(post.beeld)} />

              <div className="mt-3 flex flex-wrap gap-2">
                <form action={zetZichtbaar}>
                  <input type="hidden" name="id" value={post.id} />
                  <input
                    type="hidden"
                    name="zichtbaar"
                    value={post.zichtbaar ? "nee" : "ja"}
                  />
                  <button
                    type="submit"
                    className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
                  >
                    {post.zichtbaar
                      ? "Van de website halen"
                      : "Op de website zetten"}
                  </button>
                </form>

                {!post.gezien && (
                  <form action={markeerGezien}>
                    <input type="hidden" name="id" value={post.id} />
                    <button
                      type="submit"
                      className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
                    >
                      Gezien
                    </button>
                  </form>
                )}

                <form action={verwijderPost}>
                  <input type="hidden" name="id" value={post.id} />
                  <input type="hidden" name="beeld" value={post.beeld ?? ""} />
                  <button
                    type="submit"
                    className="rounded-md border border-danger/40 px-3 py-1.5 text-sm text-danger hover:bg-danger/10"
                  >
                    Verwijderen
                  </button>
                </form>
              </div>
            </li>
          ))}

          {posts.length === 0 && (
            <li className="text-sm text-ink-dim">
              Er staat nog geen enkel bericht in de kijker. Zet er hierboven een
              bij, dan staat het meteen op de website.
            </li>
          )}
        </ul>
      </main>
    </>
  );
}
