import { NaarLink } from "@/components/ui";
import { extraLinks, onderdelen, site, volgOns } from "@/content/site";

export function SiteFooter() {
  return (
    <footer className="niet-afdrukken bg-green text-cream">
      <div className="mx-auto w-full max-w-5xl px-5 py-10">
        <div className="flex flex-wrap items-center justify-between gap-6">
          <p className="font-hand text-2xl text-[#f3c98a]">{site.afsluiter}</p>
          {/* Het logo. Vervang public/beeldmerk.png om het te veranderen. */}
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src="/beeldmerk.png"
            alt={`Het logo van ${site.naam} ${site.vzw}`}
            width={512}
            height={512}
            className="h-20 w-20 shrink-0 rounded-2xl"
          />
        </div>

        <nav className="mt-6 flex flex-wrap gap-x-5 gap-y-2">
          {onderdelen.map((onderdeel) => (
            <NaarLink
              key={onderdeel.slug}
              href={onderdeel.extern ?? onderdeel.slug}
              className="text-[15px] font-bold text-cream/90 underline-offset-4 hover:underline"
            >
              {onderdeel.menuTitel}
            </NaarLink>
          ))}
          {extraLinks.map((extra) => (
            <NaarLink
              key={extra.slug}
              href={extra.slug}
              className="text-[15px] font-bold text-cream/90 underline-offset-4 hover:underline"
            >
              {extra.menuTitel}
            </NaarLink>
          ))}
        </nav>

        <p className="mt-6 text-[15px] text-cream/75">
          {site.naam} {site.vzw} · {site.socials} · {site.email}
        </p>

        {/*
          Waar we te volgen zijn. De lijst komt uit volgOns in
          content/site.ts; staat daar niets in, dan valt deze regel weg.
        */}
        {volgOns.length > 0 ? (
          <p className="mt-2 flex flex-wrap gap-x-4 gap-y-1 text-[15px] text-cream/75">
            <span>Volg ons op</span>
            {volgOns.map((kanaal) => (
              <a
                key={kanaal.naam}
                href={kanaal.adres}
                className="font-bold text-cream underline-offset-4 hover:underline"
              >
                {kanaal.naam}
              </a>
            ))}
          </p>
        ) : null}
      </div>
    </footer>
  );
}
