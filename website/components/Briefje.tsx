import { NaarLink } from "@/components/ui";
import { datumInWoorden } from "@/lib/datum";
import type { Briefje as BriefjeType } from "@/content/prikbord";

/*
  Eén briefje op het prikbord, zoals een sticky note: een gekleurd blaadje
  met een punaise erboven en een lichte scheefstand.

  De kleur en de scheefstand hangen af van de plek in de rij, zodat een
  bord er levendig uitziet zonder dat je per briefje iets moet kiezen.
*/

const blaadjes = [
  "bg-[#fdf3c9] border-[#f0e29a]",
  "bg-orange-soft border-[#f2cfae]",
  "bg-purple-soft border-[#d6c4ec]",
  "bg-blue-soft border-[#c2daea]",
  "bg-sage-soft border-[#c8d5b3]",
  "bg-[#fbdde4] border-[#f0c2cd]",
];

const scheef = ["-rotate-1", "rotate-1", "-rotate-2", "rotate-2", "rotate-0"];

export function Briefje({
  briefje,
  nummer,
}: {
  briefje: BriefjeType;
  nummer: number;
}) {
  const blaadje = blaadjes[nummer % blaadjes.length];
  const hoek = scheef[nummer % scheef.length];

  return (
    <article
      className={`mb-5 break-inside-avoid rounded-[14px] border p-5 pt-6 shadow-[0_4px_14px_rgba(47,74,34,0.12)] ${blaadje} ${hoek} transition hover:rotate-0`}
    >
      {/* De punaise */}
      <span
        aria-hidden
        className="mx-auto mb-3 block h-3 w-3 rounded-full bg-orange shadow-[0_1px_3px_rgba(0,0,0,0.3)]"
      />

      {briefje.label ? (
        <p className="text-[11px] font-bold tracking-[0.09em] text-ink-dim uppercase">
          {briefje.label}
        </p>
      ) : null}

      {briefje.foto ? (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={`/prikbord/${briefje.foto.bestand}`}
          alt={briefje.foto.beschrijving}
          className="mb-3 w-full rounded-[10px] border border-white/70 object-cover"
        />
      ) : null}

      {briefje.wanneer ? (
        <p className="mb-1 text-[14px] font-extrabold text-green">
          {briefje.wanneer}
        </p>
      ) : null}

      <p className="font-hand text-[21px] leading-snug text-ink">
        {briefje.tekst}
      </p>

      {briefje.link ? (
        <NaarLink
          href={briefje.link.href}
          className="mt-3 inline-block text-[14px] font-extrabold text-green underline-offset-4 hover:underline"
        >
          {briefje.link.tekst} →
        </NaarLink>
      ) : null}

      {briefje.van || briefje.datum ? (
        <p className="mt-3 text-[13px] text-ink-dim">
          {briefje.van}
          {briefje.van && briefje.datum ? " · " : null}
          {briefje.datum ? datumInWoorden(briefje.datum) : null}
        </p>
      ) : null}
    </article>
  );
}
