import { NaarLink } from "@/components/ui";
import { extraLinks, onderdelen, site, volgOns } from "@/content/site";

/*
  Kim op 9 oktober 2026 over de voettekst: "kunnen we dit ook op een manier
  overzichtelijker maken? mss ook in kleine knoppen? dus dat er overal een
  kadertje rond staat. nu lijkt het gewoon veel tekst bij elkaar."

  Kim op 15 oktober 2026: de knoppen door elkaar "lijkt me nog heel druk,
  mss moet dat toch al mooi uitgelijnd zijn per categorie".

  Daarom staan de links nu in vier kolommen met een kopje, elk met een
  eigen kadertje, netjes onder elkaar. Een nieuwe pagina in content/site.ts
  die hieronder nog in geen enkele groep staat, komt vanzelf bij de laatste
  groep terecht, zodat er nooit een link verdwijnt.
*/
const groepen: { titel: string; links: string[] }[] = [
  {
    titel: "Voor je kind",
    links: [
      "/aanbod",
      "/kijkje",
      "/ouderportaal",
      "/oefenplatform",
      "/meetesten",
    ],
  },
  {
    titel: "Hulp en advies",
    links: [
      "/hulp-en-advies",
      "/wegwijzer",
      "/waar-kan-je-terecht",
      "/observatielijst",
      "/thuisonderwijs",
    ],
  },
  {
    titel: "Lezen en delen",
    links: ["/blog", "/in-de-kijker", "/prikbord"],
  },
  {
    titel: "Over Connectopia",
    links: ["/over-ons", "/professionals", "/steun-ons", "/contact"],
  },
];

const alleLinks = [
  ...onderdelen.map((o) => ({
    slug: o.slug,
    href: o.extern ?? o.slug,
    titel: o.menuTitel,
  })),
  ...extraLinks.map((e) => ({
    slug: e.slug,
    href: e.slug,
    titel: e.menuTitel,
  })),
];

const ingedeeld = new Set(groepen.flatMap((g) => g.links));
const kolommen = groepen.map((groep, i) => ({
  titel: groep.titel,
  links: [
    ...groep.links
      .map((slug) => alleLinks.find((l) => l.slug === slug))
      .filter((l) => l !== undefined),
    ...(i === groepen.length - 1
      ? alleLinks.filter((l) => !ingedeeld.has(l.slug))
      : []),
  ],
}));

const pil =
  "rounded-full border border-cream/30 bg-cream/5 px-3.5 py-1.5 text-[15px] font-bold text-cream/90 transition hover:border-cream/60 hover:bg-cream/15 hover:text-cream";

const kadertje =
  "block rounded-xl border border-cream/25 bg-cream/5 px-3 py-1.5 text-[15px] font-bold text-cream/90 transition hover:border-cream/60 hover:bg-cream/15 hover:text-cream";

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

        <nav className="mt-8 grid grid-cols-2 gap-x-5 gap-y-7 lg:grid-cols-4">
          {kolommen.map((kolom) => (
            <div key={kolom.titel}>
              <h2 className="text-[13px] font-extrabold uppercase tracking-wider text-[#f3c98a]">
                {kolom.titel}
              </h2>
              <ul className="mt-3 grid gap-2">
                {kolom.links.map((link) => (
                  <li key={link.slug}>
                    <NaarLink href={link.href} className={kadertje}>
                      {link.titel}
                    </NaarLink>
                  </li>
                ))}
              </ul>
            </div>
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
