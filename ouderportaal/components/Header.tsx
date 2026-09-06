import Link from "next/link";
import { logout } from "@/app/login/actions";

export function Header({
  naam,
  rol,
  terugHref,
  terugLabel,
}: {
  naam: string;
  rol: "ouder" | "beheerder" | "leerkracht";
  terugHref?: string;
  terugLabel?: string;
}) {
  return (
    <header className="border-b border-border bg-surface">
      <div className="mx-auto flex max-w-4xl items-center justify-between gap-4 px-6 py-4">
        <div className="flex items-center gap-4">
          <Link href="/portaal" className="font-display text-lg font-semibold text-forest-dark">
            Ouderportaal
          </Link>
          {terugHref && (
            <Link href={terugHref} className="text-sm text-ink-dim hover:text-ink">
              &larr; {terugLabel ?? "Terug"}
            </Link>
          )}
        </div>
        <div className="flex items-center gap-4 text-sm">
          <Link href="/portaal/kalender" className="text-forest-dark hover:underline">
            Kalender
          </Link>
          {rol !== "leerkracht" && (
            <Link href="/portaal/gezin" className="text-forest-dark hover:underline">
              Mijn gezin
            </Link>
          )}
          {rol === "leerkracht" && (
            <Link href="/team" className="text-forest-dark hover:underline">
              Team
            </Link>
          )}
          {rol === "beheerder" && (
            <Link href="/beheer" className="text-forest-dark hover:underline">
              Beheer
            </Link>
          )}
          <span className="text-ink-dim">{naam}</span>
          <form action={logout}>
            <button type="submit" className="text-ink-dim underline-offset-2 hover:text-ink hover:underline">
              Uitloggen
            </button>
          </form>
        </div>
      </div>
    </header>
  );
}
