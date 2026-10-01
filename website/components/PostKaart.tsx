import { NaarLink } from "@/components/ui";
import { datumInWoorden } from "@/lib/datum";
import { inkijker, kanalen } from "@/content/inkijker";
import type { Kanaal, Post } from "@/content/inkijker";

/*
  Eén bericht van sociale media, als kaartje in onze eigen stijl.

  Het is bewust géén echt Facebook- of Instagramvenster: zo'n venster
  plaatst cookies bij elke bezoeker en dan moet er een cookiebanner op de
  site. Zie de uitleg bovenaan content/inkijker.ts.

  Een bericht van onszelf krijgt een groene rand, een bericht van iemand
  anders een paarse, zodat een lezer meteen ziet wie aan het woord is.
*/

type Beeld = { adres: string; beschrijving: string };

export function PostKaart({
  post,
  beeld,
}: {
  post: Post;
  /* Waar het beeld staat. Zonder beeld blijft dit leeg. */
  beeld?: Beeld | null;
}) {
  const naam = kanalen[post.kanaal as Kanaal] ?? kanalen.anders;
  const eigen = post.eigen === true;
  const rand = eigen ? "border-green/35" : "border-purple/35";
  const pil = eigen ? "bg-sage-soft text-green" : "bg-purple-soft text-purple";

  return (
    <article
      className={`flex break-inside-avoid flex-col overflow-hidden rounded-[18px] border bg-surface shadow-[0_2px_10px_rgba(47,74,34,0.07)] ${rand}`}
    >
      {beeld ? (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={beeld.adres}
          alt={beeld.beschrijving}
          className="aspect-[4/3] w-full max-w-full object-cover"
        />
      ) : null}

      <div className="flex flex-1 flex-col gap-2 p-5">
        <div className="flex flex-wrap items-center gap-2">
          <span
            className={`rounded-full px-3 py-1 text-[13px] font-extrabold ${pil}`}
          >
            {naam}
          </span>
          <span className="text-[14.5px] font-bold text-ink-dim">
            {post.van}
          </span>
        </div>

        {post.titel ? (
          <h3 className="text-[19px] leading-snug text-ink">{post.titel}</h3>
        ) : null}

        <p className="text-[16px] leading-relaxed text-ink">{post.tekst}</p>

        <div className="mt-auto flex flex-wrap items-baseline justify-between gap-2 pt-3">
          <NaarLink
            href={post.link}
            className="text-[15px] font-extrabold text-green underline-offset-4 hover:underline"
          >
            {inkijker.bekijkKnop} →
          </NaarLink>
          {post.datum ? (
            <span className="text-[14px] text-ink-dim">
              {datumInWoorden(post.datum)}
            </span>
          ) : null}
        </div>
      </div>
    </article>
  );
}
