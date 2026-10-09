import { NaarLink } from "@/components/ui";
import { extraLinks, onderdelen, site, volgOns } from "@/content/site";

/*
  Kim op 9 oktober 2026 over de voettekst: "kunnen we dit ook op een manier
  overzichtelijker maken? mss ook in kleine knoppen? dus dat er overal een
  kadertje rond staat. nu lijkt het gewoon veel tekst bij elkaar."

  Daarom is elke link een pilletje met een eigen randje, zoals de knoppen
  elders op de site. Zo zie je meteen waar de ene link eindigt en de volgende
  begint, ook op een gsm waar ze over meerdere regels vallen.
*/
const pil =
  "rounded-full border border-cream/30 bg-cream/5 px-3.5 py-1.5 text-[15px] font-bold text-cream/90 transition hover:border-cream/60 hover:bg-cream/15 hover:text-cream";

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

        <nav className="mt-7 flex flex-wrap gap-2">
          {onderdelen.map((onderdeel) => (
            <NaarLink
              key={onderdeel.slug}
              href={onderdeel.extern ?? onderdeel.slug}
              className={pil}
            >
              {onderdeel.menuTitel}
            </NaarLink>
          ))}
          {extraLinks.map((extra) => (
            <NaarLink key={extra.slug} href={extra.slug} className={pil}>
              {extra.menuTitel}
            </NaarLink>
          ))}
        </nav>

        {/*
          Waar we te volgen zijn. De lijst komt uit volgOns in
          content/site.ts; staat daar niets in, dan valt deze regel weg.
        */}
        {volgOns.length > 0 ? (
          <div className="mt-7 flex flex-wrap items-center gap-2 border-t border-cream/15 pt-6">
            <span className="mr-1 text-[15px] text-cream/75">Volg ons op</span>
            {volgOns.map((kanaal) => (
              <a key={kanaal.naam} href={kanaal.adres} className={pil}>
                {kanaal.naam}
              </a>
            ))}
          </div>
        ) : null}

        <p className="mt-6 text-[15px] text-cream/75">
          {site.naam} {site.vzw} · {site.socials} · {site.email}
        </p>
      </div>
    </footer>
  );
}
