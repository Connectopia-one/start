/*
  Eén weetje op het prikbord, als een briefje met een punaise erboven.

  De vorm komt van het prikbord van de website: een gekleurd blaadje dat een
  beetje scheef hangt. Kim vroeg uitdrukkelijk om diezelfde look. De kleur en
  de scheefstand volgen uit de plaats in de rij, zodat een bord er levendig
  uitziet zonder dat er per briefje iets te kiezen valt.

  De kleuren staan hier als vaste waarden en niet als thema-kleuren: het
  oefenplatform heeft zelf een sobere kaft, en dit ene hoekje mag eruitzien
  als papier.
*/

const blaadjes = [
  "bg-[#fdf3c9] border-[#f0e29a]",
  "bg-[#fbeadb] border-[#f2cfae]",
  "bg-[#efe6f8] border-[#d6c4ec]",
  "bg-[#e4f0f7] border-[#c2daea]",
  "bg-[#eaf1de] border-[#c8d5b3]",
  "bg-[#fbdde4] border-[#f0c2cd]",
];

const scheef = ["-rotate-1", "rotate-1", "-rotate-2", "rotate-2", "rotate-0"];

export type WeetjeRij = {
  id: string;
  tekst: string;
  voornaam: string | null;
  leeftijd: number | null;
};

export function Weetje({ weetje, nummer }: { weetje: WeetjeRij; nummer: number }) {
  const blaadje = blaadjes[nummer % blaadjes.length];
  const hoek = scheef[nummer % scheef.length];

  const van = [weetje.voornaam, weetje.leeftijd ? `${weetje.leeftijd} jaar` : null]
    .filter(Boolean)
    .join(", ");

  return (
    <article
      className={`mb-5 break-inside-avoid rounded-[14px] border p-5 pt-6 shadow-[0_4px_14px_rgba(35,41,31,0.12)] ${blaadje} ${hoek} transition hover:rotate-0`}
    >
      {/* De punaise */}
      <span
        aria-hidden
        className="mx-auto mb-3 block h-3 w-3 rounded-full bg-amber shadow-[0_1px_3px_rgba(0,0,0,0.3)]"
      />

      <p className="text-[17px] leading-relaxed text-ink">{weetje.tekst}</p>

      {van && <p className="mt-3 text-[14px] text-ink-dim">— {van}</p>}
    </article>
  );
}
