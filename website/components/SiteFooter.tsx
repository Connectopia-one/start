import Link from "next/link";
import { onderdelen, site } from "@/content/site";

export function SiteFooter() {
  return (
    <footer className="bg-green text-cream">
      <div className="mx-auto w-full max-w-5xl px-5 py-10">
        <p className="font-hand text-2xl text-[#f3c98a]">{site.afsluiter}</p>

        <nav className="mt-6 flex flex-wrap gap-x-5 gap-y-2">
          {onderdelen.map((onderdeel) => (
            <Link
              key={onderdeel.slug}
              href={onderdeel.extern ?? onderdeel.slug}
              className="text-sm font-bold text-cream/90 underline-offset-4 hover:underline"
            >
              {onderdeel.menuTitel}
            </Link>
          ))}
        </nav>

        <p className="mt-6 text-sm text-cream/75">
          {site.naam} {site.vzw} · {site.socials} · {site.email}
        </p>
      </div>
    </footer>
  );
}
