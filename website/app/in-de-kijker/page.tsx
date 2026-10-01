import type { Metadata } from "next";
import { PaginaKop, Sectie } from "@/components/ui";
import { PostKaart } from "@/components/PostKaart";
import { Postformulier } from "@/components/Postformulier";
import type { Kanaal, Post } from "@/content/inkijker";
import { inkijker } from "@/content/inkijker";
import { beeldAdres, haalPosts, inkijkerKlaar } from "@/lib/inkijker-db";

/* De berichten komen erbij terwijl je kijkt, dus geen opgeslagen versie. */
export const dynamic = "force-dynamic";

export const metadata: Metadata = {
  title: "In de kijker",
  description: inkijker.tekst,
};

/*
  Welk bericht er bovenaan staat nadat iemand iets instuurde. De codes komen
  uit app/in-de-kijker/acties.ts.
*/
function melding(code: string | undefined) {
  const t = inkijker.formulier;
  const berichten: Record<string, string> = {
    gelukt: t.gelukt,
    mislukt: t.mislukt,
    link: t.foutLink,
    tekst: t.foutTekst,
    naam: t.foutNaam,
    mail: t.foutMail,
  };
  if (!code || !(code in berichten)) return null;
  return { tekst: berichten[code], goed: code === "gelukt" };
}

type MetBeeld = {
  post: Post;
  beeld?: { adres: string; beschrijving: string } | null;
};

export default async function InDeKijkerPagina({
  searchParams,
}: {
  searchParams: Promise<{ melding?: string }>;
}) {
  const { melding: code } = await searchParams;
  const bericht = melding(code);

  const klaar = inkijkerKlaar();
  const uitDatabank = klaar ? await haalPosts() : [];

  /* Eerst onze eigen vaste berichten, daarna wat uit de databank komt. */
  const posts: MetBeeld[] = [
    ...inkijker.vastePosts.map((post) => ({
      post,
      beeld: post.beeld
        ? {
            adres: `/in-de-kijker/${post.beeld.bestand}`,
            beschrijving: post.beeld.beschrijving,
          }
        : null,
    })),
    ...uitDatabank.map((rij) => {
      const adres = rij.beeld ? beeldAdres(rij.beeld) : null;
      return {
        post: {
          tekst: rij.tekst,
          van: rij.van,
          kanaal: rij.kanaal as Kanaal,
          link: rij.link,
          titel: rij.titel ?? undefined,
          datum: rij.created_at.slice(0, 10),
          eigen: rij.eigen,
        },
        beeld: adres
          ? { adres, beschrijving: `Beeld bij het bericht van ${rij.van}` }
          : null,
      };
    }),
  ];

  return (
    <>
      <PaginaKop
        label={inkijker.label}
        titel={inkijker.titel}
        handgeschreven={inkijker.handgeschreven}
        tekst={inkijker.tekst}
      />

      {bericht ? (
        <Sectie className="pt-4 pb-0">
          <p
            className={`rounded-[14px] px-5 py-4 text-[16px] ${
              bericht.goed
                ? "bg-sage-soft text-green"
                : "bg-orange-soft text-ink"
            }`}
          >
            {bericht.tekst}
          </p>
        </Sectie>
      ) : null}

      <Sectie className="pt-6 pb-8">
        {posts.length > 0 ? (
          <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {posts.map((rij, nummer) => (
              <PostKaart
                key={`${rij.post.link}-${nummer}`}
                post={rij.post}
                beeld={rij.beeld}
              />
            ))}
          </div>
        ) : (
          <p className="rounded-[18px] border border-border bg-surface px-6 py-8 text-center text-[17px] text-ink-dim">
            {inkijker.leegTekst}
          </p>
        )}
      </Sectie>

      <Sectie className="pt-0 pb-10" id="insturen">
        <div className="rounded-[20px] border border-border bg-surface p-7">
          <h2 className="text-2xl text-green">{inkijker.formulier.titel}</h2>
          <p className="mt-2 max-w-2xl text-[16px] text-ink-dim">
            {inkijker.formulier.tekst}
          </p>
          <div className="mt-5">
            {klaar ? (
              <Postformulier />
            ) : (
              <p className="text-[16px] text-ink-dim">
                {inkijker.formulier.nogNiet}
              </p>
            )}
          </div>
        </div>
      </Sectie>

      <Sectie className="pt-0 pb-16">
        <div className="rounded-[20px] bg-sage-soft px-7 py-7">
          <h2 className="text-2xl text-green">{inkijker.spelregels.titel}</h2>
          <ul className="mt-4 grid gap-2.5 sm:grid-cols-2">
            {inkijker.spelregels.punten.map((punt) => (
              <li key={punt} className="text-[16px] text-ink">
                {punt}
              </li>
            ))}
          </ul>
        </div>
      </Sectie>
    </>
  );
}
