/*
  Een briefje op een prikbord: een gekleurd blaadje met een punaise, dat een
  beetje scheef hangt.

  De vorm komt van het prikbord van de website. Kim vroeg die look eerst voor
  de weetjes en daarna ook voor de tips, dus staat hij hier één keer en gebruiken
  beide pagina's hem. De kleur en de scheefstand volgen uit de plaats in de rij,
  zodat een bord levendig is zonder dat er per briefje iets te kiezen valt.

  De kleuren staan hier als vaste waarden en niet als thema-kleuren: het
  oefenplatform heeft zelf een sobere kaft, en deze hoekjes mogen eruitzien
  als papier.

  Twee manieren om de blaadjes te schikken. Op het prikbord van de weetjes
  staan ze in kolommen: de volgorde doet er niet toe en de blaadjes schuiven
  mooi in elkaar. Bij de tips telt de volgorde wel, en kolommen lezen dan van
  boven naar beneden: 1, 2, 3 onder elkaar en pas daarna 4 ernaast. Daarom
  zetten de tips ze in een raster, dat rij per rij van links naar rechts
  leest. Zet daar `inRaster` aan, zodat het blaadje zijn eigen ondermarge
  loslaat en de tussenruimte van het raster volgt.
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

/* De kurken achtergrond waar de blaadjes op hangen. */
export const bordKlassen =
  "rounded-[20px] border border-border bg-[#f1e8d7] p-5 pb-0 shadow-[inset_0_2px_8px_rgba(35,41,31,0.08)]";

export function Blaadje({
  nummer,
  inRaster = false,
  children,
}: {
  nummer: number;
  inRaster?: boolean;
  children: React.ReactNode;
}) {
  const blaadje = blaadjes[nummer % blaadjes.length];
  const hoek = scheef[nummer % scheef.length];
  const plaatsing = inRaster ? "" : "mb-5 break-inside-avoid";

  return (
    <article
      className={`${plaatsing} rounded-[14px] border p-5 pt-6 shadow-[0_4px_14px_rgba(35,41,31,0.12)] ${blaadje} ${hoek} transition hover:rotate-0`}
    >
      {/* De punaise */}
      <span
        aria-hidden
        className="mx-auto mb-3 block h-3 w-3 rounded-full bg-amber shadow-[0_1px_3px_rgba(0,0,0,0.3)]"
      />
      {children}
    </article>
  );
}
