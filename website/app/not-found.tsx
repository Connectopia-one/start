import Link from "next/link";
import { onderdelen, site } from "@/content/site";

/*
  Wat een bezoeker ziet als een adres niet bestaat.

  Dit doet er vooral toe op de dag dat de site op connectopia.one komt te
  staan. Wie dan nog een link of een bladwijzer van de oude site heeft, of
  iets aanklikt dat Google nog kent, komt hier terecht. Een kale foutmelding
  laat die bezoeker weglopen; een lijstje met waar hij wél naartoe kan, niet.
*/
export default function NietGevonden() {
  return (
    <div className="mx-auto w-full max-w-2xl px-6 py-16">
      <div className="rounded-[24px] bg-surface px-7 py-8 shadow-sm">
        <h1 className="text-[26px] font-extrabold text-green">
          Deze pagina bestaat niet (meer)
        </h1>
        <p className="mt-3 text-[17px] text-ink">
          Onze website is vernieuwd, dus een oude link komt soms nergens meer
          uit. Alles staat er nog, alleen op een ander adres. Kies hieronder
          waar je naartoe wou.
        </p>

        <ul className="mt-6 grid gap-2">
          {onderdelen.map((o) => (
            <li key={o.slug}>
              {o.extern ? (
                <a
                  className="flex items-center gap-3 rounded-2xl bg-cream px-4 py-3 text-[16px] font-bold text-ink transition hover:-translate-y-0.5"
                  href={o.extern}
                >
                  <span aria-hidden>{o.icoon}</span>
                  {o.titel}
                </a>
              ) : (
                <Link
                  className="flex items-center gap-3 rounded-2xl bg-cream px-4 py-3 text-[16px] font-bold text-ink transition hover:-translate-y-0.5"
                  href={o.slug}
                >
                  <span aria-hidden>{o.icoon}</span>
                  {o.titel}
                </Link>
              )}
            </li>
          ))}
        </ul>

        <p className="mt-7 text-[17px] text-ink">
          Vind je niet wat je zocht? Laat het ons gerust weten.
          <br />
          <a className="font-bold text-green underline" href={`mailto:${site.email}`}>
            {site.email}
          </a>
          <br />
          <a className="font-bold text-green underline" href={site.telefoonLink}>
            {site.telefoon}
          </a>
        </p>

        <Link
          href="/"
          className="mt-7 inline-block rounded-full bg-green px-7 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
        >
          Naar de startpagina →
        </Link>
      </div>
    </div>
  );
}
