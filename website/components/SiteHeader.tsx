import Link from "next/link";
import { Logo } from "@/components/Logo";
import { NaarLink } from "@/components/ui";
import { menu, onderdelen } from "@/content/site";

const ouderportaal = onderdelen.find((o) => o.slug === "/ouderportaal");

export function SiteHeader() {
  return (
    <header className="niet-afdrukken sticky top-0 z-30 border-b border-border bg-cream/95 backdrop-blur">
      <div className="mx-auto flex w-full max-w-5xl flex-wrap items-center gap-4 px-5 py-3">
        <Link href="/" aria-label="Naar de startpagina">
          <Logo />
        </Link>
        <nav className="ml-auto hidden items-center gap-0.5 sm:flex">
          {menu.map((onderdeel) => (
            <NaarLink
              key={onderdeel.slug}
              href={onderdeel.extern ?? onderdeel.slug}
              className="rounded-full px-3 py-2 text-[14.5px] font-bold text-ink-dim hover:bg-sage-soft hover:text-green"
            >
              {onderdeel.menuTitel}
            </NaarLink>
          ))}
          {ouderportaal ? (
            <NaarLink
              href={ouderportaal.extern ?? ouderportaal.slug}
              className="ml-2 rounded-full bg-green px-4 py-2 text-[14.5px] font-bold text-cream hover:bg-green-mid"
            >
              Inloggen
            </NaarLink>
          ) : null}
        </nav>
      </div>
    </header>
  );
}
