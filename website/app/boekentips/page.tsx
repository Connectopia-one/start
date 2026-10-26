import type { Metadata } from "next";
import { Boekenrek } from "@/components/Boekenrek";
import { PaginaKop, Sectie } from "@/components/ui";
import { boekentipsTekst } from "@/content/boekentips";

export const metadata: Metadata = {
  title: "Boekentips",
  description: boekentipsTekst.tekst,
};

export default function BoekentipsPagina() {
  return (
    <>
      <PaginaKop
        label={boekentipsTekst.label}
        titel={boekentipsTekst.titel}
        handgeschreven={boekentipsTekst.handgeschreven}
        tekst={boekentipsTekst.tekst}
      />
      <Sectie>
        <Boekenrek />
      </Sectie>
    </>
  );
}
