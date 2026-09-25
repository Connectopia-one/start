import Link from "next/link";
import { verder } from "@/content/verder";

/**
 * Drie kaarten naar de rest van de site. Zie content/verder.ts voor het waarom
 * en voor de teksten.
 */
export function OntdekVerder({ titel, tekst }: { titel: string; tekst: string }) {
  return (
    <>
      <h2 className="text-2xl text-green">{titel}</h2>
      <p className="mt-2 text-[16px] text-ink-dim">{tekst}</p>
      <div className="mt-4 grid gap-4 md:grid-cols-3">
        {verder.kaarten.map((kaart) => (
          <div
            key={kaart.link}
            className="flex flex-col rounded-[20px] border border-border bg-cream p-5"
          >
            <h3 className="text-xl text-green">{kaart.titel}</h3>
            <p className="mt-2 grow text-[16px] text-ink-dim">{kaart.tekst}</p>
            <Link
              href={kaart.link}
              className="mt-4 inline-block self-start rounded-full bg-green px-5 py-2 text-[15px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
            >
              {kaart.knop} &rarr;
            </Link>
          </div>
        ))}
      </div>
    </>
  );
}
