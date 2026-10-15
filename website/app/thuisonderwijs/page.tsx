import type { Metadata } from "next";
import { Foto, Kaart, PaginaKop, Sectie } from "@/components/ui";
import {
  blokken,
  bronnen,
  thuisonderwijsTekst,
  verhaal,
  waarden,
  waardenFoto,
  watWijDoen,
} from "@/content/thuisonderwijs";

export const metadata: Metadata = {
  title: "Thuisonderwijs en de Examencommissie",
  description: thuisonderwijsTekst.tekst,
};

function Punten({ punten }: { punten: { dik: string; tekst: string }[] }) {
  return (
    <ul className="mt-3 grid gap-2.5">
      {punten.map((punt) => (
        <li key={punt.dik} className="flex gap-2.5 text-ink-dim">
          <span
            aria-hidden
            className="mt-2 h-2 w-2 shrink-0 rounded-full bg-sage"
          />
          <span>
            <strong className="font-extrabold text-ink">{punt.dik}</strong>{" "}
            {punt.tekst}
          </span>
        </li>
      ))}
    </ul>
  );
}

export default function ThuisonderwijsPagina() {
  return (
    <>
      <PaginaKop
        label={thuisonderwijsTekst.label}
        titel={thuisonderwijsTekst.titel}
        handgeschreven={thuisonderwijsTekst.handgeschreven}
        tekst={thuisonderwijsTekst.tekst}
      />

      <Sectie>
        {/* De lijn van Kim staat bewust bovenaan, voor alle regelgeving. */}
        <div className="rounded-[20px] border border-sage bg-sage-soft p-6">
          {waardenFoto ? (
            <Foto
              bestand={waardenFoto.bestand}
              beschrijving={waardenFoto.beschrijving}
              className="mb-5"
            />
          ) : null}
          {waarden.map((regel) => (
            <p
              key={regel}
              className="mt-2 font-semibold text-green first:mt-0 max-w-[62ch]"
            >
              {regel}
            </p>
          ))}
        </div>

        <div className="mt-5 grid gap-5">
          {blokken.map((blok) => (
            <Kaart key={blok.titel}>
              {blok.foto ? (
                <Foto
                  bestand={blok.foto.bestand}
                  beschrijving={blok.foto.beschrijving}
                  className="mb-5"
                />
              ) : null}
              <h2 className="text-2xl text-green">{blok.titel}</h2>
              {blok.inleiding ? (
                <p className="mt-2 max-w-[62ch] text-ink-dim">
                  {blok.inleiding}
                </p>
              ) : null}
              {blok.punten ? <Punten punten={blok.punten} /> : null}
              {blok.delen?.map((deel) => (
                <div key={deel.titel} className="mt-5">
                  <h3 className="text-lg text-green">{deel.titel}</h3>
                  <Punten punten={deel.punten} />
                </div>
              ))}
              {blok.slot ? (
                <p className="mt-4 max-w-[62ch] text-ink-dim">{blok.slot}</p>
              ) : null}
            </Kaart>
          ))}

          {/* Kims eigen verhaal, in haar eigen stem. */}
          <div className="rounded-[20px] border border-l-[6px] border-purple bg-purple-soft p-6">
            <h2 className="text-2xl text-purple">{verhaal.titel}</h2>
            {verhaal.alineas.map((alinea) => (
              <p key={alinea} className="mt-3 max-w-[62ch] text-ink">
                {alinea}
              </p>
            ))}
            <p className="font-hand mt-3 text-2xl text-purple">
              {verhaal.naam}
            </p>
          </div>

          <Kaart>
            <h2 className="text-2xl text-green">{watWijDoen.titel}</h2>
            {watWijDoen.alineas.map((alinea) => (
              <p key={alinea} className="mt-2 max-w-[62ch] text-ink-dim">
                {alinea}
              </p>
            ))}
          </Kaart>
        </div>

        <p className="mt-6 text-[15px] text-ink-dim">
          {bronnen.tekst}
          <br />
          {bronnen.links.map((link) => (
            <a
              key={link.adres}
              href={link.adres}
              target="_blank"
              rel="noopener noreferrer"
              className="mt-1 block font-bold text-blue underline-offset-4 hover:underline"
            >
              {link.tekst}
            </a>
          ))}
        </p>
      </Sectie>
    </>
  );
}
