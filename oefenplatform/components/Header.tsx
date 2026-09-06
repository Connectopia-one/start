import Link from "next/link";
import { logout } from "@/app/login/actions";

export function Header({
  naam,
  rol,
}: {
  naam?: string;
  rol?: "ouder" | "beheerder";
}) {
  return (
    <header className="border-b border-border bg-surface">
      <div className="mx-auto flex max-w-4xl items-center justify-between gap-4 px-6 py-4">
        <Link href="/" className="font-display text-lg font-semibold text-forest-dark">
          Oefenplatform
        </Link>
        <div className="flex items-center gap-4 text-sm">
          <Link href="/" className="text-forest-dark hover:underline">
            Vakken
          </Link>
          {rol === "beheerder" && (
            <Link href="/beheer" className="text-forest-dark hover:underline">
              Beheer
            </Link>
          )}
          {naam ? (
            <>
              <Link href="/account" className="text-ink-dim hover:text-ink">
                {naam}
              </Link>
              <form action={logout}>
                <button type="submit" className="text-ink-dim underline-offset-2 hover:text-ink hover:underline">
                  Uitloggen
                </button>
              </form>
            </>
          ) : (
            <>
              <Link href="/login" className="text-forest-dark hover:underline">
                Inloggen
              </Link>
              <Link
                href="/registreren"
                className="rounded-md bg-forest px-3 py-1.5 text-white transition hover:bg-forest-dark"
              >
                Registreren
              </Link>
            </>
          )}
        </div>
      </div>
    </header>
  );
}
