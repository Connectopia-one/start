import Link from "next/link";
import type { Onderdeel } from "@/content/site";
import { Icoon, tekstKleur, vlakKleur } from "@/components/ui";

/*
  Eén klikbaar blok op de startpagina.
  "gevuld" geeft het blok een zachte achtergrondkleur in plaats van wit.
*/
export function Tegel({
  onderdeel,
  gevuld = false,
  children,
}: {
  onderdeel: Onderdeel;
  gevuld?: boolean;
  children?: React.ReactNode;
}) {
  const achtergrond = gevuld
    ? `${vlakKleur[onderdeel.kleur]} border-transparent`
    : "bg-surface border-border";

  return (
    <Link
      href={onderdeel.extern ?? onderdeel.slug}
      className={`flex flex-col gap-2.5 rounded-[20px] border p-6 shadow-[0_2px_10px_rgba(47,74,34,0.07)] transition hover:-translate-y-1 hover:shadow-[0_8px_20px_rgba(47,74,34,0.12)] ${achtergrond}`}
    >
      {onderdeel.label ? (
        <span className="self-start rounded-full bg-surface px-3 py-1 text-[11.5px] font-extrabold tracking-[0.07em] text-ink-dim uppercase">
          {onderdeel.label}
        </span>
      ) : null}

      <Icoon kleur={onderdeel.kleur}>{onderdeel.icoon}</Icoon>

      <h3 className={`text-xl ${tekstKleur[onderdeel.kleur]}`}>{onderdeel.titel}</h3>
      <p className="text-[15px] text-ink-dim">{onderdeel.omschrijving}</p>

      {children}

      <span className={`mt-auto pt-3 text-sm font-extrabold ${tekstKleur[onderdeel.kleur]}`}>
        Bekijken →
      </span>
    </Link>
  );
}
