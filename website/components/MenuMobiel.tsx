"use client";

import { useState } from "react";
import { NaarLink } from "@/components/ui";

/*
  Het menu voor een gsm.

  Op een breed scherm staan de onderdelen gewoon naast elkaar in de balk. Op
  een smal scherm paste dat niet, en stond er vroeger helemaal geen menu: je
  kon alleen via de startpagina of via de voettekst verder. Nu staat er een
  knop die de lijst openklapt.

  De lijst komt uit SiteHeader, zodat beide menu's dezelfde onderdelen tonen.
*/
export function MenuMobiel({
  links,
  inloggen,
}: {
  links: { href: string; tekst: string }[];
  inloggen?: { href: string; tekst: string };
}) {
  const [open, setOpen] = useState(false);

  return (
    <div className="ml-auto sm:hidden">
      {/*
        Enkel het teken, zonder het woord "menu": met het logo ernaast past
        een bredere knop niet naast elkaar op een smalle gsm, en dan springt
        hij naar een tweede regel. De naam staat er wel voor wie voorleest.
      */}
      <button
        type="button"
        onClick={() => setOpen(!open)}
        aria-expanded={open}
        aria-controls="menu-mobiel"
        aria-label={open ? "Menu sluiten" : "Menu openen"}
        className="flex h-11 w-11 items-center justify-center rounded-full border-2 border-green text-[20px] font-bold text-green"
      >
        <span aria-hidden>{open ? "✕" : "☰"}</span>
      </button>

      {open ? (
        <nav
          id="menu-mobiel"
          /*
            De balk blijft bovenaan staan als je scrolt, dus het menu blijft
            openstaan tot je het sluit. Een klik ergens in de lijst sluit het,
            en daar valt elke link vanzelf onder.
          */
          onClick={() => setOpen(false)}
          className="absolute left-0 right-0 top-full border-b border-border bg-cream px-5 pb-4 shadow-sm"
        >
          {links.map((link) => (
            <NaarLink
              key={link.href}
              href={link.href}
              className="block border-b border-border py-3.5 text-[16px] font-bold text-green"
            >
              {link.tekst}
            </NaarLink>
          ))}
          {inloggen ? (
            <NaarLink
              href={inloggen.href}
              className="mt-4 block rounded-full bg-green px-4 py-3 text-center text-[16px] font-bold text-cream"
            >
              {inloggen.tekst}
            </NaarLink>
          ) : null}
        </nav>
      ) : null}
    </div>
  );
}
