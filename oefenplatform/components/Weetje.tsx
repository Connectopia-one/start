import { Blaadje } from "@/components/Blaadje";

/*
  Eén weetje op het prikbord. De vorm van het blaadje zelf staat in
  Blaadje.tsx, want de tipspagina gebruikt diezelfde look.
*/

export type WeetjeRij = {
  id: string;
  tekst: string;
  voornaam: string | null;
  leeftijd: number | null;
};

export function Weetje({ weetje, nummer }: { weetje: WeetjeRij; nummer: number }) {
  const van = [weetje.voornaam, weetje.leeftijd ? `${weetje.leeftijd} jaar` : null]
    .filter(Boolean)
    .join(", ");

  return (
    <Blaadje nummer={nummer}>
      <p className="text-[17px] leading-relaxed text-ink">{weetje.tekst}</p>
      {van && <p className="mt-3 text-[14px] text-ink-dim">— {van}</p>}
    </Blaadje>
  );
}
