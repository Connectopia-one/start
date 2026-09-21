import { prikbord } from "@/content/prikbord";
import { site } from "@/content/site";

/*
  Het blokje dat bovenaan het prikbord en boven elk bord staat:
  hier hangen we alleen positieve briefjes op. De tekst staat in
  content/prikbord.ts bij "toon".
*/
export function PositieveToon({ klein = false }: { klein?: boolean }) {
  return (
    <div className="rounded-[20px] border border-purple/20 bg-purple-soft px-6 py-5">
      <h2 className={`text-purple ${klein ? "text-lg" : "text-xl"}`}>
        {prikbord.toon.titel}
      </h2>
      <p className="mt-2 max-w-[68ch] text-[16px] text-ink">
        {prikbord.toon.tekst}
      </p>
      <a
        href={`mailto:${site.email}`}
        className="mt-3 inline-block text-[15px] font-extrabold text-purple underline-offset-4 hover:underline"
      >
        {prikbord.toon.knopTekst} op {site.email} →
      </a>
    </div>
  );
}
