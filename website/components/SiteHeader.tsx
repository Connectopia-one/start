import Link from "next/link";
import { Logo } from "@/components/Logo";
import { MenuMobiel } from "@/components/MenuMobiel";
import { NaarLink } from "@/components/ui";
import { extraLinks, menu, onderdelen } from "@/content/site";

const ouderportaal = onderdelen.find((o) => o.slug === "/ouderportaal");
const extraInMenu = extraLinks.filter((extra) => extra.inMenu);

/* Dezelfde onderdelen als in de balk, voor het uitklapmenu op een gsm. */
const menuLinks = [
  ...menu.map((onderdeel) => ({
    href: onderdeel.extern ?? onderdeel.slug,
    tekst: onderdeel.menuTitel,
  })),
  ...extraInMenu.map((extra) => ({
    href: extra.slug,
    tekst: extra.menuTitel,
  })),
];

export function SiteHeader() {
  return (
    <header className="niet-afdrukken sticky top-0 z-30 border-b border-border bg-cream/95 backdrop-blur">
      <div className="mx-auto flex w-full max-w-5xl flex-wrap items-center gap-3 px-4 py-3 sm:gap-4 sm:px-5">
        <Link href="/" aria-label="Naar de startpagina">
          <Logo />
        </Link>
        <nav className="ml-auto hidden items-center gap-0.5 sm:flex">
          {menu.map((onderdeel) => (
            <NaarLink
              key={onderdeel.slug}
              href={onderdeel.extern ?? onderdeel.slug}
              className="rounded-full px-2.5 py-2 text-[14.5px] font-bold text-ink-dim hover:bg-sage-soft hover:text-green"
            >
              {onderdeel.menuTitel}
            </NaarLink>
          ))}
          {extraInMenu.map((extra) => (
            <NaarLink
              key={extra.slug}
              href={extra.slug}
              className="rounded-full px-2.5 py-2 text-[14.5px] font-bold text-ink-dim hover:bg-sage-soft hover:text-green"
            >
              {extra.menuTitel}
            </NaarLink>
          ))}
          {ouderportaal ? (
            <NaarLink
              href={ouderportaal.extern ?? ouderportaal.slug}
              className="ml-1.5 rounded-full bg-green px-4 py-2 text-[14.5px] font-bold text-cream hover:bg-green-mid"
            >
              Inloggen
            </NaarLink>
          ) : null}
        </nav>

        <MenuMobiel
          links={menuLinks}
          inloggen={
            ouderportaal
              ? {
                  href: ouderportaal.extern ?? ouderportaal.slug,
                  tekst: "Inloggen",
                }
              : undefined
          }
        />
      </div>
    </header>
  );
}
