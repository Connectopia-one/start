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

export const stipKleur: Record<Kleur, string> = {
  green: "bg-green",
  orange: "bg-orange",
  purple: "bg-purple",
  blue: "bg-blue",
};

export function Icoon({ kleur, children }: { kleur: Kleur; children: ReactNode }) {
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
  return (
    <span className="text-[13px] font-bold tracking-[0.09em] text-sage uppercase">
      {children}
    </span>
  );
}

export function Penseel({ children }: { children: ReactNode }) {
  return (
    <span className="inline-block rounded-full bg-sage-soft px-4 py-1.5 text-sm font-extrabold text-green">
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
      className={`inline-block rounded-full border-2 px-6 py-3 text-[15px] font-extrabold transition hover:-translate-y-0.5 ${stijl}`}
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
}: {
  children: ReactNode;
  className?: string;
}) {
  return (
    <section className={`mx-auto w-full max-w-5xl px-5 py-10 ${className}`}>{children}</section>
  );
}

export function Kaart({
  children,
  className = "",
}: {
  children: ReactNode;
  className?: string;
}) {
  return (
    <div
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
