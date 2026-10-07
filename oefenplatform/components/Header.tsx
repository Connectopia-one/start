"use client";

import Link from "next/link";
import { useState } from "react";
import { logout } from "@/app/login/actions";

type Rol = "ouder" | "beheerder" | "begeleider";

/*
  De menubalk.

  Op een gsm paste alles vroeger niet naast elkaar: wie ingelogd was als
  beheerder kreeg acht items op één rij en moest het hele scherm uitzoomen om
  ze te zien. Daarom klapt het menu onder 768 pixels open met een knop, en
  staat het daarboven gewoon naast elkaar.

  Een link bijzetten doe je hieronder in menuLinks; hij verschijnt dan vanzelf
  in allebei de menu's.
*/
function menuLinks(rol?: Rol) {
  const lijst = [
    { href: "/", tekst: "Vakken" },
    { href: "/tips", tekst: "Tips" },
    { href: "/weetjes", tekst: "Weetjes" },
    { href: "/materiaal", tekst: "Materiaal" },
    { href: "/over-ons", tekst: "Over ons" },
  ];
  if (rol === "beheerder" || rol === "begeleider") {
    lijst.push({ href: "/begeleiding", tekst: "Begeleiding" });
  }
  if (rol === "beheerder") {
    lijst.push({ href: "/beheer", tekst: "Beheer" });
  }
  return lijst;
}

export function Header({ naam, rol }: { naam?: string; rol?: Rol }) {
  const [open, setOpen] = useState(false);
  const links = menuLinks(rol);

  return (
    <header className="border-b border-border bg-surface">
      <div className="mx-auto flex max-w-4xl items-center justify-between gap-4 px-6 py-4">
        <Link
          href="/"
          className="font-display text-lg font-semibold text-forest-dark"
        >
          Oefenplatform
        </Link>

        {/* Breed scherm: alles naast elkaar. */}
        <div className="hidden flex-wrap items-center justify-end gap-4 text-sm md:flex">
          {links.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="text-forest-dark hover:underline"
            >
              {link.tekst}
            </Link>
          ))}
          {naam ? (
            <>
              <Link href="/account" className="text-ink-dim hover:text-ink">
                {naam}
              </Link>
              <form action={logout}>
                <button
                  type="submit"
                  className="text-ink-dim underline-offset-2 hover:text-ink hover:underline"
                >
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

        {/* Gsm: één knop die het menu openklapt. */}
        <button
          type="button"
          onClick={() => setOpen(!open)}
          aria-expanded={open}
          aria-controls="hoofdmenu"
          className="flex items-center gap-2 rounded-md border border-border px-3 py-2 text-sm font-semibold text-forest-dark md:hidden"
        >
          <span aria-hidden>{open ? "✕" : "☰"}</span>
          {open ? "Sluiten" : "Menu"}
        </button>
      </div>

      {open ? (
        <div id="hoofdmenu" className="border-t border-border md:hidden">
          <nav className="mx-auto flex max-w-4xl flex-col px-6 py-2">
            {/* Elke link sluit het menu, zodat je de pagina eronder meteen ziet. */}
            {links.map((link) => (
              <Link
                key={link.href}
                href={link.href}
                onClick={() => setOpen(false)}
                className="border-b border-border py-3 text-forest-dark last:border-0"
              >
                {link.tekst}
              </Link>
            ))}
            {naam ? (
              <>
                <Link
                  href="/account"
                  onClick={() => setOpen(false)}
                  className="border-b border-border py-3 text-ink-dim"
                >
                  {naam}
                </Link>
                <form action={logout}>
                  <button
                    type="submit"
                    className="w-full py-3 text-left text-ink-dim"
                  >
                    Uitloggen
                  </button>
                </form>
              </>
            ) : (
              <>
                <Link
                  href="/login"
                  onClick={() => setOpen(false)}
                  className="border-b border-border py-3 text-forest-dark"
                >
                  Inloggen
                </Link>
                <Link
                  href="/registreren"
                  onClick={() => setOpen(false)}
                  className="my-3 rounded-md bg-forest px-3 py-2.5 text-center text-white"
                >
                  Registreren
                </Link>
              </>
            )}
          </nav>
        </div>
      ) : null}
    </header>
  );
}
