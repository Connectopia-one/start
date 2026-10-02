import type { Kanaal } from "@/content/inkijker";

/*
  Het teken van het kanaal, groot, als band bovenaan een kaartje zonder beeld.

  Facebook en Instagram geven het beeld van een bericht niet vrij, en wij
  zetten er bewust geen echt venster van hen op de site (dat plaatst cookies
  bij elke bezoeker). Zo'n kaartje is dan enkel tekst, en dat oogde leeg.
  Met deze band ziet een lezer meteen waar het bericht staat.

  De tekens zijn eenvoudig natekend werk in de kleur van het kanaal zelf,
  zodat ze herkenbaar zijn. Het is geen beeld uit het bericht: dat zouden we
  niet mogen overnemen zonder het te vragen.
*/

type Merk = { vlak: string; kleur: string; tekening: React.ReactNode };

const MERKEN: Record<Kanaal, Merk> = {
  facebook: {
    vlak: "bg-[#eef3fb]",
    kleur: "#1877f2",
    tekening: (
      <path d="M13.5 21v-8h2.7l.4-3.1h-3.1V7.8c0-.9.2-1.5 1.5-1.5h1.7V3.5c-.3 0-1.3-.1-2.4-.1-2.4 0-4 1.5-4 4.1v2.4H7.6V13h2.7v8z" />
    ),
  },
  instagram: {
    vlak: "bg-[#fbeef5]",
    kleur: "#c13584",
    tekening: (
      <>
        <rect
          x="3.2"
          y="3.2"
          width="17.6"
          height="17.6"
          rx="5"
          fill="none"
          stroke="currentColor"
          strokeWidth="1.9"
        />
        <circle
          cx="12"
          cy="12"
          r="4.1"
          fill="none"
          stroke="currentColor"
          strokeWidth="1.9"
        />
        <circle cx="17.2" cy="6.8" r="1.3" />
      </>
    ),
  },
  linkedin: {
    vlak: "bg-[#eaf2f8]",
    kleur: "#0a66c2",
    tekening: (
      <path d="M4.5 9h3v11h-3zM6 4a1.8 1.8 0 1 1 0 3.6A1.8 1.8 0 0 1 6 4zm3.8 5h2.9v1.5c.5-.9 1.6-1.7 3.2-1.7 2.5 0 3.6 1.6 3.6 4.4V20h-3v-5.9c0-1.5-.5-2.3-1.7-2.3-1.1 0-1.9.7-1.9 2.3V20h-3z" />
    ),
  },
  tiktok: {
    vlak: "bg-[#f0f0f2]",
    kleur: "#111111",
    tekening: (
      <path d="M16.5 3h-3v11.3a2.6 2.6 0 1 1-2.2-2.6V8.6A6.1 6.1 0 1 0 17 14.6V9.3a6.6 6.6 0 0 0 3.4 1V7A3.9 3.9 0 0 1 16.5 3Z" />
    ),
  },
  youtube: {
    vlak: "bg-[#fdeded]",
    kleur: "#ff0000",
    tekening: (
      <>
        <rect x="2.2" y="5.3" width="19.6" height="13.4" rx="3.6" />
        <path d="M10.3 9.1 15.6 12l-5.3 2.9z" fill="#fff" />
      </>
    ),
  },
  anders: {
    vlak: "bg-sage-soft",
    kleur: "#2f4a22",
    tekening: (
      <path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Zm6.9 6h-2.9a15 15 0 0 0-1.3-3.4A8 8 0 0 1 18.9 8ZM12 4.2c.6.9 1.2 2.2 1.6 3.8h-3.2c.4-1.6 1-2.9 1.6-3.8ZM4.3 14a8 8 0 0 1 0-4h3.3a19 19 0 0 0 0 4Zm.8 2H8a15 15 0 0 0 1.3 3.4A8 8 0 0 1 5.1 16Zm2.9-8H5.1a8 8 0 0 1 4.2-3.4A15 15 0 0 0 8 8Zm4 11.8c-.6-.9-1.2-2.2-1.6-3.8h3.2c-.4 1.6-1 2.9-1.6 3.8Zm2-5.8h-4a17 17 0 0 1 0-4h4a17 17 0 0 1 0 4Zm.7 5.4A15 15 0 0 0 16 16h2.9a8 8 0 0 1-4.2 3.4ZM16.4 14a19 19 0 0 0 0-4h3.3a8 8 0 0 1 0 4Z" />
    ),
  },
};

export function KanaalMerk({
  kanaal,
  naam,
}: {
  kanaal: Kanaal;
  /* Hoe het kanaal heet, voor wie de pagina voorgelezen krijgt. */
  naam: string;
}) {
  const merk = MERKEN[kanaal] ?? MERKEN.anders;

  return (
    <div
      className={`flex aspect-[16/7] w-full items-center justify-center border-b border-border ${merk.vlak}`}
    >
      <svg
        viewBox="0 0 24 24"
        role="img"
        aria-label={naam}
        className="h-11 w-11"
        fill="currentColor"
        style={{ color: merk.kleur }}
      >
        {merk.tekening}
      </svg>
    </div>
  );
}
