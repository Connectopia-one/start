import Link from "next/link";
import { Tegel } from "@/components/Tegel";
import {
  Blad,
  Foto,
  Icoon,
  Knop,
  Label,
  NaarLink,
  Penseel,
  stipKleur,
  tekstKleur,
} from "@/components/ui";
import { home } from "@/content/home";
import { echteLink, onderdeelPerGroep, site } from "@/content/site";
import type { Sponsor } from "@/content/sponsors";
import { sponsorsPerSoort, sponsorsTekst } from "@/content/sponsors";
import { stappen, wegwijzerTekst } from "@/content/wegwijzer";

export default function Startpagina() {
  const watwedoen = onderdeelPerGroep("watwedoen");
  const platform = onderdeelPerGroep("platform");
  const kennis = onderdeelPerGroep("kennis");
  const wegwijzer = onderdeelPerGroep("uitgelicht")[0];

  return (
    <>
      {/* Hero */}
      <section className="relative overflow-hidden">
        <Blad className="-top-5 -left-10 w-44 -rotate-12" />
        <Blad className="-right-8 -bottom-10 w-36 rotate-[150deg]" />

        <div className="relative mx-auto grid w-full max-w-5xl gap-9 px-5 py-14 md:grid-cols-[1.2fr_0.85fr] md:items-center">
          <div>
            <Penseel>{site.baseline}</Penseel>
            <h1 className="mt-4 text-4xl font-black text-green sm:text-5xl">
              {home.hero.titel}{" "}
              <span className="text-purple">{home.hero.titelAccent}</span>.
            </h1>
            <p className="font-hand mt-2 text-2xl text-orange sm:text-3xl">
              {home.hero.handgeschreven}
            </p>
            <p className="mt-4 max-w-[48ch] text-[17px] text-ink-dim">
              {home.hero.tekst}
            </p>
            <div className="mt-7 flex flex-wrap gap-3">
              <Knop href={home.hero.knopPrimair.link}>
                {home.hero.knopPrimair.tekst}
              </Knop>
              <Knop href={home.hero.knopTweede.link} variant="tweede">
                {home.hero.knopTweede.tekst}
              </Knop>
            </div>
          </div>

          <aside className="rounded-[20px] border border-border bg-surface p-6 shadow-[0_2px_10px_rgba(47,74,34,0.07)]">
            <Label>Kies je richting</Label>
            <h2 className="mt-1.5 text-lg text-green">
              {home.kiesJeRichting.titel}
            </h2>
            <ul className="mt-3 grid gap-0.5">
              {home.kiesJeRichting.keuzes.map((keuze) => (
                <li key={keuze.link}>
                  <NaarLink
                    href={echteLink(keuze.link)}
                    className="flex items-center gap-2.5 rounded-xl px-2.5 py-2.5 text-[15px] font-semibold hover:bg-sage-soft hover:text-green"
                  >
                    <span
                      aria-hidden
                      className={`h-2.5 w-2.5 shrink-0 rounded-full ${stipKleur[keuze.kleur]}`}
                    />
                    {keuze.tekst}
                  </NaarLink>
                </li>
              ))}
            </ul>
          </aside>
        </div>
      </section>

      {/* De brede foto onder de hero */}
      {home.foto ? (
        <section className="mx-auto w-full max-w-5xl px-5 pb-12">
          <Foto
            bestand={home.foto.bestand}
            beschrijving={home.foto.beschrijving}
            verhouding="breed"
          />
        </section>
      ) : null}

      {/* Aankondiging */}
      {home.aankondiging ? (
        <section className="bg-green text-cream">
          <div className="mx-auto flex w-full max-w-5xl flex-wrap items-center justify-center gap-x-5 gap-y-2 px-5 py-4 text-center text-[15px] font-bold">
            <span>{home.aankondiging.tekst}</span>
            <span className="font-hand text-2xl text-[#f3c98a]">
              {home.aankondiging.handgeschreven}
            </span>
            <Link
              href={home.aankondiging.link.href}
              className="font-extrabold underline-offset-4 hover:underline"
            >
              {home.aankondiging.link.tekst} →
            </Link>
          </div>
        </section>
      ) : null}

      {/* Wat we doen */}
      <section className="mx-auto w-full max-w-5xl px-5 py-14">
        <Label>{home.blokken.watwedoen.label}</Label>
        <h2 className="mt-1.5 text-3xl text-green">
          {home.blokken.watwedoen.titel}
        </h2>
        <p className="mt-2 max-w-[62ch] text-ink-dim">
          {home.blokken.watwedoen.tekst}
        </p>

        <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {watwedoen.map((onderdeel) => (
            <Tegel key={onderdeel.slug} onderdeel={onderdeel} />
          ))}
        </div>

        {/* De wegwijzer, uitgelicht */}
        {wegwijzer ? (
          <Link
            href={wegwijzer.slug}
            className="mt-4 block rounded-[20px] border border-border bg-surface p-7 shadow-[0_2px_10px_rgba(47,74,34,0.07)] transition hover:-translate-y-1"
          >
            <div className="grid gap-6 md:grid-cols-[1.1fr_0.9fr] md:items-center">
              <div>
                <Penseel>{wegwijzerTekst.label}</Penseel>
                <h3 className="mt-3 text-2xl text-green">
                  {wegwijzerTekst.titel}
                </h3>
                <p className="font-hand mt-1 text-xl text-purple">
                  {wegwijzerTekst.handgeschreven}
                </p>
              </div>
              <p className="text-[15px] text-ink-dim">{wegwijzerTekst.tekst}</p>
            </div>

            <div className="mt-6 grid gap-4 border-t border-dashed border-border pt-5 sm:grid-cols-2 lg:grid-cols-5">
              {stappen.map((stap) => (
                <div
                  key={stap.nummer}
                  className="flex flex-col items-start gap-2"
                >
                  <Icoon kleur={stap.kleur}>{stap.icoon}</Icoon>
                  <h4 className={`text-[15.5px] ${tekstKleur[stap.kleur]}`}>
                    {stap.nummer}. {stap.titel}
                  </h4>
                  <p className="text-[13.5px] text-ink-dim">
                    {stap.samenvatting}
                  </p>
                </div>
              ))}
            </div>
          </Link>
        ) : null}
      </section>

      {/* Direct naar jouw plek */}
      <section className="mx-auto w-full max-w-5xl px-5 pb-14">
        <Label>{home.blokken.platform.label}</Label>
        <h2 className="mt-1.5 text-3xl text-green">
          {home.blokken.platform.titel}
        </h2>
        <p className="mt-2 max-w-[62ch] text-ink-dim">
          {home.blokken.platform.tekst}
        </p>

        <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {platform.map((onderdeel) => (
            <Tegel key={onderdeel.slug} onderdeel={onderdeel} gevuld />
          ))}
        </div>
      </section>

      {/* Lezen en bijleren */}
      <section className="mx-auto w-full max-w-5xl px-5 pb-14">
        <Label>{home.blokken.kennis.label}</Label>
        <h2 className="mt-1.5 text-3xl text-green">
          {home.blokken.kennis.titel}
        </h2>

        <div className="mt-6 grid gap-4 sm:grid-cols-2">
          {kennis.map((onderdeel) => (
            <Tegel key={onderdeel.slug} onderdeel={onderdeel} />
          ))}
          <Link
            href={home.partnerBlok.link}
            className="flex flex-col gap-2.5 rounded-[20px] border border-border bg-surface p-6 shadow-[0_2px_10px_rgba(47,74,34,0.07)] transition hover:-translate-y-1"
          >
            <Icoon kleur="orange">{home.partnerBlok.icoon}</Icoon>
            <h3 className="text-xl text-orange">{home.partnerBlok.titel}</h3>
            <p className="text-[15px] text-ink-dim">
              {home.partnerBlok.omschrijving}
            </p>
            <span className="mt-auto pt-3 text-sm font-extrabold text-orange">
              {home.partnerBlok.linkTekst} →
            </span>
          </Link>
        </div>
      </section>

      {/* Sponsors en samenwerkingen */}
      <section className="bg-sage-soft" id="sponsors">
        <div className="mx-auto w-full max-w-5xl px-5 py-12">
          <Label>{sponsorsTekst.label}</Label>
          <h2 className="mt-1.5 text-3xl text-green">{sponsorsTekst.titel}</h2>
          <p className="mt-2 max-w-[60ch] text-ink-dim">
            {sponsorsTekst.tekst}
          </p>

          <SponsorRij
            kop={sponsorsTekst.kopSponsors}
            lijst={sponsorsPerSoort("sponsor")}
          />
          <SponsorRij
            kop={sponsorsTekst.kopPartners}
            lijst={sponsorsPerSoort("partner")}
          />

          <p className="mt-5 text-[15px] text-ink-dim">
            <Link
              href={sponsorsTekst.oproepLink}
              className="font-extrabold text-green underline-offset-4 hover:underline"
            >
              {sponsorsTekst.oproep}
            </Link>
          </p>
        </div>
      </section>
    </>
  );
}

function SponsorRij({ kop, lijst }: { kop: string; lijst: Sponsor[] }) {
  if (lijst.length === 0) return null;
  return (
    <div className="mt-7">
      <h3 className="text-[13px] font-bold tracking-[0.09em] text-green uppercase">
        {kop}
      </h3>
      {/* Flexibele rij: werkt met twee logo's net zo goed als met twaalf. */}
      <ul className="mt-3 flex flex-wrap gap-3.5">
        {lijst.map((sponsor) => (
          <li key={sponsor.naam} className="w-[calc(50%-0.44rem)] sm:w-48">
            <SponsorVak sponsor={sponsor} />
          </li>
        ))}
      </ul>
    </div>
  );
}

function SponsorVak({ sponsor }: { sponsor: Sponsor }) {
  const inhoud = sponsor.logo ? (
    // eslint-disable-next-line @next/next/no-img-element
    <img
      src={`/sponsors/${sponsor.logo}`}
      alt={sponsor.naam}
      className="max-h-20 w-auto object-contain"
    />
  ) : (
    <span className="px-2 text-center">
      <span className="block text-[14px] font-extrabold text-green">
        {sponsor.naam}
      </span>
      {sponsor.toelichting ? (
        <span className="block text-[12px] text-ink-dim">
          {sponsor.toelichting}
        </span>
      ) : null}
    </span>
  );

  const vak =
    "flex h-28 items-center justify-center rounded-2xl bg-surface p-3 shadow-[0_2px_10px_rgba(47,74,34,0.07)]";

  if (sponsor.link) {
    return (
      <a
        href={sponsor.link}
        target="_blank"
        rel="noopener noreferrer"
        className={`${vak} transition hover:-translate-y-0.5`}
      >
        {inhoud}
      </a>
    );
  }
  return <div className={vak}>{inhoud}</div>;
}
