import Link from "next/link";
import { PRIJS_ACTIE_EUR, PRIJS_STRAKS_EUR } from "@/lib/prijs";

/*
  De Black Friday-banner bovenaan de startpagina (Kim, 24 november 2026:
  "iets met een strik", in onze kleuren). Zelfde stijl als de post op sociale
  media: donkergroen vlak met een fijn ruitje, een oranje lint en een strik.
  Staat er enkel zolang actieLoopt() in lib/prijs.ts waar is.
*/

const patroon = {
  backgroundColor: "#2f4a22",
  backgroundImage:
    "radial-gradient(circle at 50% 50%, rgba(251,246,234,.13) 2px, transparent 3px)," +
    "linear-gradient(45deg, transparent 47%, rgba(251,246,234,.07) 48%, rgba(251,246,234,.07) 52%, transparent 53%)," +
    "linear-gradient(-45deg, transparent 47%, rgba(251,246,234,.07) 48%, rgba(251,246,234,.07) 52%, transparent 53%)",
  backgroundSize: "24px 24px, 80px 80px, 80px 80px",
};

function Strik() {
  return (
    <svg viewBox="0 0 500 380" className="h-full w-full" aria-hidden="true">
      <defs>
        <linearGradient id="bf-g1" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#e4a066" />
          <stop offset=".5" stopColor="#c8752a" />
          <stop offset="1" stopColor="#8f4e17" />
        </linearGradient>
        <linearGradient id="bf-g2" x1="1" y1="0" x2="0" y2="1">
          <stop offset="0" stopColor="#e4a066" />
          <stop offset=".5" stopColor="#c8752a" />
          <stop offset="1" stopColor="#8f4e17" />
        </linearGradient>
        <radialGradient id="bf-k" cx=".4" cy=".35" r=".7">
          <stop offset="0" stopColor="#e9a86e" />
          <stop offset="1" stopColor="#9a5419" />
        </radialGradient>
      </defs>
      <path d="M235 240 L175 345 L205 332 L222 358 L250 255 Z" fill="url(#bf-g1)" stroke="#7a420f" strokeWidth="3" />
      <path d="M265 240 L325 345 L295 332 L278 358 L250 255 Z" fill="url(#bf-g2)" stroke="#7a420f" strokeWidth="3" />
      <path d="M250 225 C190 120 40 70 30 170 C22 250 120 290 250 245 Z" fill="url(#bf-g1)" stroke="#7a420f" strokeWidth="3" />
      <path d="M250 225 C310 120 460 70 470 170 C478 250 380 290 250 245 Z" fill="url(#bf-g2)" stroke="#7a420f" strokeWidth="3" />
      <path d="M215 225 C170 160 90 135 75 175 C70 205 120 230 215 235 Z" fill="#7a420f" opacity=".35" />
      <path d="M285 225 C330 160 410 135 425 175 C430 205 380 230 285 235 Z" fill="#7a420f" opacity=".35" />
      <path d="M70 150 C100 110 160 115 200 150" fill="none" stroke="#fff" strokeOpacity=".45" strokeWidth="7" strokeLinecap="round" />
      <path d="M300 150 C340 115 400 110 430 150" fill="none" stroke="#fff" strokeOpacity=".45" strokeWidth="7" strokeLinecap="round" />
      <rect x="212" y="195" width="76" height="80" rx="22" fill="url(#bf-k)" stroke="#7a420f" strokeWidth="3" />
      <path d="M228 212 C240 205 258 205 270 212" fill="none" stroke="#fff" strokeOpacity=".5" strokeWidth="5" strokeLinecap="round" />
    </svg>
  );
}

export function BlackFridayBanner({ ingelogd }: { ingelogd: boolean }) {
  return (
    <section className="relative mb-8 overflow-hidden rounded-2xl text-[#fbf6ea] shadow-sm" style={patroon}>
      {/* Het lint: verticaal over de rechterkant, met de strik erop. */}
      <div
        className="absolute inset-y-0 right-16 hidden w-12 sm:block"
        style={{ background: "linear-gradient(90deg,#d8894a,#c8752a 45%,#a85e1f)" }}
        aria-hidden="true"
      />
      <div className="absolute right-0 top-1/2 hidden h-28 w-36 -translate-y-1/2 sm:block">
        <Strik />
      </div>

      <div className="relative px-6 py-6 sm:pr-48">
        <p className="text-xs font-extrabold tracking-[0.2em] text-[#e9b77a]">BLACK FRIDAY</p>
        <p className="mt-1 font-display text-2xl font-semibold sm:text-3xl">
          Nog tot vrijdag 27 november, 24u:{" "}
          <span className="whitespace-nowrap">
            €{PRIJS_ACTIE_EUR}{" "}
            <span className="text-lg font-normal text-[#fbf6ea]/60 line-through">€{PRIJS_STRAKS_EUR}</span>
          </span>
        </p>
        <p className="mt-2 max-w-[60ch] text-sm text-[#fbf6ea]/90">
          Een volledig schooljaar voor het hele gezin. Vanaf zaterdag 28 november kost het €{PRIJS_STRAKS_EUR}.
          Wie nu betaalt, heeft toegang tot het einde van dit schooljaar.
        </p>
        <Link
          href={ingelogd ? "/betalen" : "/registreren"}
          className="mt-4 inline-block rounded-full bg-[#c8752a] px-5 py-2 text-sm font-bold text-white transition hover:bg-[#a85e1f]"
        >
          {ingelogd ? "Volledige toegang vrijgeven" : "Account aanmaken"}
        </Link>
      </div>
    </section>
  );
}
