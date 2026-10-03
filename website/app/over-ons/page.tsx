import type { Metadata } from "next";
import Link from "next/link";
import { Foto, Icoon, Kaart, PaginaKop, Sectie } from "@/components/ui";
import { kijkje } from "@/content/kijkje";
import { overOns } from "@/content/over-ons";
import { site } from "@/content/site";

export const metadata: Metadata = {
  title: "Wie is Connectopia",
  description: overOns.verhaal[0].slice(0, 155),
};

export default function OverOnsPagina() {
  return (
    <>
      <PaginaKop
        label={overOns.label}
        titel={overOns.titel}
        handgeschreven={overOns.handgeschreven}
      />

      <Sectie>
        <div className="grid gap-8 lg:grid-cols-[1.15fr_0.85fr] lg:items-start">
          <div className="grid max-w-[68ch] gap-4 text-[18px] text-ink-dim">
            {overOns.verhaal.map((alinea) => (
              <p key={alinea.slice(0, 24)}>{alinea}</p>
            ))}
          </div>
          {overOns.verhaalFoto ? (
            <figure className="lg:sticky lg:top-24">
              <Foto
                bestand={overOns.verhaalFoto.bestand}
                beschrijving={overOns.verhaalFoto.beschrijving}
                verhouding="vrij"
              />
              {overOns.verhaalFoto.bijschrift ? (
                <figcaption className="font-hand mt-2 text-center text-2xl text-orange">
                  {overOns.verhaalFoto.bijschrift}
                </figcaption>
              ) : null}
            </figure>
          ) : null}
        </div>
      </Sectie>

      <Sectie>
        <h2 className="text-2xl text-green">{overOns.rol.titel}</h2>
        <div className="mt-3 grid max-w-[68ch] gap-4 text-ink-dim">
          {overOns.rol.tekst.map((alinea) => (
            <p key={alinea.slice(0, 24)}>{alinea}</p>
          ))}
        </div>

        <p className="font-hand mt-8 rounded-[20px] bg-sage-soft px-6 py-5 text-center text-2xl text-green">
          {overOns.citaat}
        </p>
      </Sectie>

      <Sectie>
        <h2 className="text-2xl text-green">Onze kernwaarden</h2>
        <div className="mt-5 grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
          {overOns.kernwaarden.map((waarde) => (
            <div key={waarde.titel} className="flex flex-col items-start gap-2">
              <Icoon kleur={waarde.kleur}>{waarde.icoon}</Icoon>
              <h3 className="text-[18px] text-green">{waarde.titel}</h3>
              <p className="text-[15px] text-ink-dim">{waarde.tekst}</p>
            </div>
          ))}
        </div>
      </Sectie>

      {/*
        Een strookje van drie foto's met een link naar de fotopagina. Het staat
        hier omdat iemand die het verhaal gelezen heeft, vanzelf benieuwd is
        hoe een dag er dan uitziet.
      */}
      <Sectie>
        <div className="flex flex-wrap items-end justify-between gap-3">
          <div>
            <h2 className="text-2xl text-green">{kijkje.strook.titel}</h2>
            <p className="mt-2 max-w-[60ch] text-ink-dim">
              {kijkje.strook.tekst}
            </p>
          </div>
          <Link
            href="/kijkje"
            className="rounded-full bg-orange px-5 py-2.5 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5"
          >
            {kijkje.strook.knop} →
          </Link>
        </div>
        <ul className="mt-5 grid gap-4 sm:grid-cols-3">
          {kijkje.strook.bestanden.map((bestand) => {
            const foto = kijkje.fotos.find((f) => f.bestand === bestand);
            if (!foto) return null;
            return (
              <li key={bestand}>
                <Link href="/kijkje">
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img
                    src={`/kijkje/${foto.bestand}`}
                    alt={foto.alt}
                    loading="lazy"
                    className="aspect-[4/3] w-full rounded-[20px] border border-border object-cover"
                  />
                </Link>
              </li>
            );
          })}
        </ul>
      </Sectie>

      <Sectie>
        <h2 className="text-2xl text-green">Ons team</h2>
        {overOns.teamFoto ? (
          <Foto
            bestand={overOns.teamFoto.bestand}
            beschrijving={overOns.teamFoto.beschrijving}
            verhouding="vrij"
            className="mt-5 max-w-xl"
          />
        ) : null}
        <div className="mt-5 grid gap-4 sm:grid-cols-3">
          {overOns.team.map((lid) => (
            <Kaart key={lid.naam}>
              <h3 className="text-xl text-green">{lid.naam}</h3>
              <p className="mt-2 text-[16px] text-ink-dim">{lid.rol}</p>
            </Kaart>
          ))}
        </div>
      </Sectie>

      <Sectie className="pb-16">
        <div
          id="contact"
          className="scroll-mt-24 rounded-[20px] bg-green px-7 py-9 text-cream"
        >
          <h2 className="text-2xl text-cream">{overOns.contact.titel}</h2>
          <p className="mt-3 max-w-[58ch] text-cream/85">
            {overOns.contact.tekst}
          </p>
          <a
            href={`mailto:${site.email}`}
            className="mt-6 inline-block rounded-full bg-cream px-6 py-3 text-[16px] font-extrabold text-green transition hover:-translate-y-0.5"
          >
            Mail ons op {site.email}
          </a>
        </div>
      </Sectie>
    </>
  );
}
