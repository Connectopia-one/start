"use client";

import Link from "next/link";
import { useState } from "react";
import { logout } from "@/app/login/actions";

type Rol = "ouder" | "beheerder" | "leerkracht";

/*
  De menubalk.

  Op een gsm paste alles niet naast elkaar, zeker niet met een terugknop erbij
  en als beheerder. Daarom klapt het menu onder 768 pixels open met een knop,
  en staat het daarboven gewoon naast elkaar. De terugknop blijft altijd
  staan: die hoort bij de pagina waar je bent, niet in een menu.

  Een link bijzetten doe je hieronder in menuLinks; hij verschijnt dan vanzelf
  in allebei de menu's.
*/
function menuLinks(rol: Rol) {
  const lijst = [{ href: "/portaal/kalender", tekst: "Kalender" }];
  if (rol !== "leerkracht") {
    lijst.push({ href: "/portaal/gezin", tekst: "Mijn gezin" });
  }
  if (rol === "leerkracht") {
    lijst.push({ href: "/team", tekst: "Team" });
  }
  if (rol === "beheerder") {
    lijst.push({ href: "/beheer", tekst: "Beheer" });
  }
  return lijst;
}

export function Header({
  naam,
  rol,
  terugHref,
  terugLabel,
}: {
  naam: string;
  rol: Rol;
  terugHref?: string;
  terugLabel?: string;
}) {
  const [open, setOpen] = useState(false);
  const links = menuLinks(rol);

  return (
    <header className="border-b border-border bg-surface">
      <div className="mx-auto flex max-w-4xl items-center justify-between gap-4 px-6 py-4">
        <div className="flex min-w-0 items-center gap-4">
          <Link
            href="/portaal"
            className="font-display text-lg font-semibold text-forest-dark"
          >
            Ouderportaal
          </Link>
          {terugHref && (
            <Link
              href={terugHref}
              className="truncate text-sm text-ink-dim hover:text-ink"
            >
              &larr; {terugLabel ?? "Terug"}
            </Link>
          )}
        </div>

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
          <span className="text-ink-dim">{naam}</span>
          <form action={logout}>
            <button
              type="submit"
              className="text-ink-dim underline-offset-2 hover:text-ink hover:underline"
            >
              Uitloggen
            </button>
          </form>
        </div>

        {/* Gsm: één knop die het menu openklapt. */}
        <button
          type="button"
          onClick={() => setOpen(!open)}
          aria-expanded={open}
          aria-controls="hoofdmenu"
          className="flex flex-none items-center gap-2 rounded-md border border-border px-3 py-2 text-sm font-semibold text-forest-dark md:hidden"
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
                className="border-b border-border py-3 text-forest-dark"
              >
                {link.tekst}
              </Link>
            ))}
            <span className="border-b border-border py-3 text-ink-dim">
              {naam}
            </span>
            <form action={logout}>
              <button
                type="submit"
                className="w-full py-3 text-left text-ink-dim"
              >
                Uitloggen
              </button>
            </form>
          </nav>
        </div>
      ) : null}
    </header>
  );
}
