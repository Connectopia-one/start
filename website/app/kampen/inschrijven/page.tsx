import type { Metadata } from "next";
import { KampInschrijving } from "@/components/KampInschrijving";
import { PaginaKop, Sectie } from "@/components/ui";
import { kampRegels, kampen } from "@/content/kampen";
import { site } from "@/content/site";

export const metadata: Metadata = {
  title: "Inschrijven voor een vakantiekamp",
  description:
    "Kies je kamp in Hasselt of Genk, schrijf één of meer kinderen in en zie meteen wat het kost.",
};

/* Elk uur opnieuw opbouwen, zodat een kamp waarvan alle dagen voorbij zijn
   vanzelf verdwijnt, zonder dat iemand de site opnieuw moet uitrollen. */
export const revalidate = 3600;

export default function KampenInschrijven() {
  const vandaag = new Date().toISOString().slice(0, 10);
  const open = kampen
    .map((k) => ({ ...k, dagen: k.dagen.filter((d) => d.datum >= vandaag) }))
    .filter((k) => k.dagen.length > 0);

  return (
    <>
      <PaginaKop
        label="Vakantiekampen"
        titel="Inschrijven voor een kamp"
        handgeschreven="Hasselt en Genk"
        tekst={`Kies een kamp, klik op "Kies dit" en vul onderaan één formulier in. ${kampRegels.uren}, voor kinderen van ${kampRegels.leeftijd}. De groepen zijn klein, dus de plaatsen zijn beperkt.`}
      />
      <Sectie className="py-8">
        {open.length ? (
          <KampInschrijving kampen={open} />
        ) : (
          <p className="text-ink-dim">
            Er staat op dit moment geen kamp open. Mail ons op {site.email} als
            je op de hoogte wil blijven.
          </p>
        )}
      </Sectie>
    </>
  );
}
