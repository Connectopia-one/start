import Link from "next/link";
import type { ReactNode } from "react";

export type Kleur = "green" | "orange" | "purple" | "blue";

/* Kleurcombinaties staan voluit, zodat Tailwind ze terugvindt in de code. */
export const icoonKleur: Record<Kleur, string> = {
  green: "bg-sage-soft text-green",
  orange: "bg-orange-soft text-orange",
  purple: "bg-purple-soft text-purple",
  blue: "bg-blue-soft text-blue",
};

export const tekstKleur: Record<Kleur, string> = {
  green: "text-green",
  orange: "text-orange",
  purple: "text-purple",
  blue: "text-blue",
};

export const vlakKleur: Record<Kleur, string> = {
  green: "bg-sage-soft",
  orange: "bg-orange-soft",
  purple: "bg-purple-soft",
  blue: "bg-blue-soft",
};

/* Een volle knop in de kleur van het blok, met crèmekleurige letters. */
export const knopKleur: Record<Kleur, string> = {
  green: "bg-green hover:bg-green-mid",
  orange: "bg-orange hover:bg-green-mid",
  purple: "bg-purple hover:bg-green-mid",
  blue: "bg-blue hover:bg-green-mid",
};

export const stipKleur: Record<Kleur, string> = {
  green: "bg-green",
  orange: "bg-orange",
  purple: "bg-purple",
  blue: "bg-blue",
};

export function Icoon({
  kleur,
  children,
}: {
  kleur: Kleur;
  children: ReactNode;
}) {
  return (
    <span
      aria-hidden
      className={`flex h-12 w-12 shrink-0 items-center justify-center rounded-full text-2xl ${icoonKleur[kleur]}`}
    >
      {children}
    </span>
  );
}

export function Label({ children }: { children: ReactNode }) {
  return <span className="text-[14px] font-bold text-sage">{children}</span>;
}

export function Penseel({ children }: { children: ReactNode }) {
  return (
    <span className="inline-block rounded-full bg-sage-soft px-4 py-1.5 text-[15px] font-extrabold text-green">
      {children}
    </span>
  );
}

export function Knop({
  href,
  variant = "primair",
  children,
}: {
  href: string;
  variant?: "primair" | "tweede";
  children: ReactNode;
}) {
  const stijl =
    variant === "primair"
      ? "bg-green text-cream border-green hover:bg-green-mid hover:border-green-mid"
      : "border-green text-green hover:bg-sage-soft";
  return (
    <Link
      href={href}
      className={`inline-block rounded-full border-2 px-6 py-3 text-[16px] font-extrabold transition hover:-translate-y-0.5 ${stijl}`}
    >
      {children}
    </Link>
  );
}

export function PaginaKop({
  label,
  titel,
  handgeschreven,
  tekst,
}: {
  label: string;
  titel: string;
  handgeschreven?: string;
  tekst?: string;
}) {
  return (
    <header className="mx-auto w-full max-w-5xl px-5 pt-14 pb-2">
      <Label>{label}</Label>
      <h1 className="mt-2 text-3xl text-green sm:text-4xl">{titel}</h1>
      {handgeschreven ? (
        <p className="font-hand mt-2 text-2xl text-orange">{handgeschreven}</p>
      ) : null}
      {tekst ? <p className="mt-4 max-w-[62ch] text-ink-dim">{tekst}</p> : null}
    </header>
  );
}

export function Sectie({
  children,
  className = "",
  id,
}: {
  children: ReactNode;
  className?: string;
  /* Een eigen anker, zodat een link als /in-de-kijker#insturen hier landt. */
  id?: string;
}) {
  return (
    <section
      id={id}
      className={`mx-auto w-full max-w-5xl px-5 py-10 ${className}`}
    >
      {children}
    </section>
  );
}

export function Kaart({
  children,
  className = "",
  id,
}: {
  children: ReactNode;
  className?: string;
  id?: string;
}) {
  return (
    <div
      id={id}
      className={`rounded-[20px] border border-border bg-surface p-6 shadow-[0_2px_10px_rgba(47,74,34,0.07)] ${className}`}
    >
      {children}
    </div>
  );
}

export function Blad({ className = "" }: { className?: string }) {
  return (
    <svg
      aria-hidden
      viewBox="0 0 100 100"
      className={`pointer-events-none absolute text-sage opacity-25 ${className}`}
    >
      <path
        d="M90 10C55 12 26 30 16 58c-4 12-4 22-2 32 8-30 28-52 58-66-24 16-40 36-47 60 26-4 48-24 58-50 5-12 7-18 7-24z"
        fill="currentColor"
      />
    </svg>
  );
}

/*
  Twee handjes rond een hartje, bij de vrijgehouden plaatsen op /aanbod.
  Kim op 21 oktober 2026: "een leuke tekening van helpende handjes of zoiets ?
  of handen rond een hartje".
*/
export function Handjes({ className = "" }: { className?: string }) {
  return (
    <svg aria-hidden viewBox="0 0 160 140" className={className}>
      <path
        d="M80 94C54 78 48 52 62 44c9-5 16 1 18 8 2-7 9-13 18-8 14 8 8 34-18 50z"
        fill="var(--orange)"
        stroke="var(--green)"
        strokeWidth="2.5"
        strokeLinejoin="round"
      />
      <path
        d="M66 53c-3 4-3 10 0 14"
        fill="none"
        stroke="var(--cream)"
        strokeWidth="3"
        strokeLinecap="round"
        opacity=".8"
      />
      {[false, true].map((rechts) => (
        <g
          key={String(rechts)}
          transform={rechts ? "translate(160 0) scale(-1 1)" : undefined}
          fill="var(--sage-soft)"
          stroke="var(--green)"
          strokeWidth="2.5"
          strokeLinejoin="round"
          strokeLinecap="round"
        >
          <path d="M26 136c-6-24 0-52 16-72 3-4 9-3 8 2-2 8 0 22 10 30 6 4 12 5 19 5-5 11-17 23-23 35z" />
          <path
            d="M33 92c1-10 5-18 10-24M30 106c1-10 4-18 8-24"
            fill="none"
            strokeWidth="1.8"
            opacity=".6"
          />
        </g>
      ))}
      <g fill="var(--orange)" opacity=".7">
        <path d="m24 30 2 6 6 2-6 2-2 6-2-6-6-2 6-2z" />
        <path d="m132 22 1.5 4.5 4.5 1.5-4.5 1.5-1.5 4.5-1.5-4.5-4.5-1.5 4.5-1.5z" />
      </g>
      <g fill="var(--sage)">
        <path d="M136 58c-5-4-6-9-3-10 2-1 3 1 3 2 0-1 1-3 3-2 3 1 2 6-3 10z" />
        <path d="M80 26c-4-3-5-7-2.5-8 1.5-.6 2.5.8 2.5 1.6 0-.8 1-2.2 2.5-1.6 2.5 1 1.5 5-2.5 8z" />
      </g>
    </svg>
  );
}

/*
  Eén link die zowel naar een pagina van deze site als naar een ander
  webadres kan wijzen. Externe adressen openen in een nieuw tabblad.
*/
export function NaarLink({
  href,
  className,
  children,
}: {
  href: string;
  className?: string;
  children: ReactNode;
}) {
  if (href.startsWith("http")) {
    return (
      <a
        href={href}
        target="_blank"
        rel="noopener noreferrer"
        className={className}
      >
        {children}
      </a>
    );
  }
  return (
    <Link href={href} className={className}>
      {children}
    </Link>
  );
}

/*
  Een foto met ronde hoeken, die de hele breedte vult.
  Zet het bestand in  public/fotos/  en geef alleen de bestandsnaam mee.
    verhouding  "breed" voor een brede band, "kaart" voor boven een kaart,
                "vrij" toont de foto zoals ze is, zonder bij te snijden
*/
export function Foto({
  bestand,
  beschrijving,
  verhouding = "kaart",
  className = "",
}: {
  bestand: string;
  beschrijving: string;
  verhouding?: "breed" | "kaart" | "vrij";
  className?: string;
}) {
  const hoogte =
    verhouding === "breed"
      ? "aspect-[8/3] object-cover"
      : verhouding === "vrij"
        ? "h-auto"
        : "aspect-[16/9] object-cover";
  return (
    // eslint-disable-next-line @next/next/no-img-element
    <img
      src={`/fotos/${bestand}`}
      alt={beschrijving}
      className={`${hoogte} w-full rounded-[20px] border border-border ${className}`}
    />
  );
}
