import { NaarLink } from "@/components/ui";
import { extraLinks, onderdelen, site } from "@/content/site";

export function SiteFooter() {
  return (
    <footer className="niet-afdrukken bg-green text-cream">
      <div className="mx-auto w-full max-w-5xl px-5 py-10">
        <p className="font-hand text-2xl text-[#f3c98a]">{site.afsluiter}</p>

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
      </div>
    </footer>
  );
}
