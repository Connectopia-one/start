"use client";

/*
  Tekeningen bij een vraag over meetkunde of metend rekenen.

  Waarom dit bestaat: die twee hoofdstukken stonden volledig in woorden, en
  meetkunde in woorden is voor veel kinderen net het moeilijkste. Een hoek van
  130° moet je zien, niet lezen. Kim vroeg daar op 25 september 2026 naar.

  Een tekening komt in de vraag te staan als een markering tussen dubbele
  accolades, net als de breukfiguren in Figuren.tsx:

    {{hoek 130}}              een hoek van 130°, met de graden erbij
    {{hoek 130 ?}}            dezelfde hoek, maar met een vraagteken
    {{driehoek gelijkbenig}}  een gelijkbenige driehoek, met streepjes op de
                              gelijke zijden
    {{driehoek 50-60-?}}      een driehoek met die hoeken; ? blijft open
    {{vierhoek trapezium}}    een trapezium, met pijltjes op de evenwijdige
                              zijden
    {{snijlijn 70}}           twee snijdende rechten, één hoek gegeven
    {{evenwijdig 65}}         twee evenwijdige rechten met een snijlijn
    {{cirkeldeel straal}}     een cirkel met de straal aangeduid
    {{merkwaardig bissectrice}}  een driehoek met die merkwaardige lijn
    {{assen rechthoek}}       een figuur met zijn symmetrieassen in stippellijn
    {{beweging rotatie}}      voor en na de transformatie
    {{maat rechthoek 7x3}}    een rechthoek met 7 cm en 3 cm erbij
    {{maat cirkel straal 5}}  een cirkel met de straal van 5 cm erbij
    {{ruimte balk 5x3x2}}     een balk in schuine projectie, met de ribben erbij
    {{ladder oppervlakte}}    de maatladder, met maal 100 per stap

  De tekening staat altijd ónder de vraag en vervangt de tekst nooit: wie de
  tekening niet ziet (de pagina waar ouders meekijken, een schermlezer), moet
  de vraag nog altijd kunnen oplossen. Schrijf een vraag dus alsof er geen
  tekening bij staat, en zet de markering achteraan.

  Alle berekende punten worden afgerond met n(), zodat de server en de browser
  exact hetzelfde pad tekenen en React niet klaagt over een verschil.
*/

const LIJN = "var(--forest-dark)";
const VUL = "var(--forest)";
const MERK = "var(--amber)";
const TEKST = "var(--ink)";
const FLAUW = "var(--border)";

/** Afronden, zodat server en browser hetzelfde tekenen. */
function n(x: number) {
  return Number(x.toFixed(2));
}

const rad = (graden: number) => (graden * Math.PI) / 180;

function Blad({
  breedte,
  hoogte,
  kader,
  children,
  titel,
}: {
  breedte: number;
  hoogte: number;
  /* Een eigen kader [x, y, breedte, hoogte], voor een tekening die zelf
     uitrekent hoe groot ze wordt. Zonder kader begint de tekening op 0,0. */
  kader?: [number, number, number, number];
  children: React.ReactNode;
  titel: string;
}) {
  const vak = kader ?? [0, 0, breedte, hoogte];
  /* Een smalle, hoge figuur zou anders de hele breedte pakken en loodrecht
     uit de kaart groeien. Daarom houden we de getekende hoogte onder 240. */
  const maxBreedte = Math.min(vak[2], (240 * vak[2]) / vak[3]);
  return (
    <svg
      viewBox={vak.map((v) => n(v)).join(" ")}
      width="100%"
      style={{ maxWidth: n(maxBreedte) }}
      role="img"
      aria-label={titel}
      className="select-none"
    >
      {children}
    </svg>
  );
}

/** Het kader rond een reeks punten, met wat lucht eromheen. */
function kaderRond(punten: { x: number; y: number }[], lucht = 30): [number, number, number, number] {
  const xs = punten.map((p) => p.x);
  const ys = punten.map((p) => p.y);
  const x = Math.min(...xs) - lucht;
  const y = Math.min(...ys) - lucht;
  return [x, y, Math.max(...xs) + lucht - x, Math.max(...ys) + lucht - y];
}

/** Een stukje tekst in de tekening. */
function Label({
  x,
  y,
  children,
  kleur = TEKST,
  groot = false,
  midden = true,
}: {
  x: number;
  y: number;
  children: React.ReactNode;
  kleur?: string;
  groot?: boolean;
  midden?: boolean;
}) {
  return (
    <text
      x={n(x)}
      y={n(y)}
      fill={kleur}
      fontSize={groot ? 15 : 13}
      fontWeight={600}
      textAnchor={midden ? "middle" : "start"}
      dominantBaseline="middle"
    >
      {children}
    </text>
  );
}

/** Een streepje dwars op een zijde, om gelijke zijden aan te duiden. */
function Streepjes({
  x1,
  y1,
  x2,
  y2,
  aantal,
}: {
  x1: number;
  y1: number;
  x2: number;
  y2: number;
  aantal: number;
}) {
  const mx = (x1 + x2) / 2;
  const my = (y1 + y2) / 2;
  const lengte = Math.hypot(x2 - x1, y2 - y1) || 1;
  // Loodrecht op de zijde.
  const dx = ((y2 - y1) / lengte) * 6;
  const dy = (-(x2 - x1) / lengte) * 6;
  // Langs de zijde, om meerdere streepjes uit elkaar te zetten.
  const ex = ((x2 - x1) / lengte) * 4;
  const ey = ((y2 - y1) / lengte) * 4;
  const start = -((aantal - 1) / 2);
  return (
    <>
      {Array.from({ length: aantal }, (_, i) => {
        const v = start + i;
        return (
          <line
            key={i}
            x1={n(mx + v * ex - dx)}
            y1={n(my + v * ey - dy)}
            x2={n(mx + v * ex + dx)}
            y2={n(my + v * ey + dy)}
            stroke={MERK}
            strokeWidth={2}
          />
        );
      })}
    </>
  );
}

/** Het vierkantje dat een rechte hoek aanduidt. */
function RechteHoek({ x, y, dx1, dy1, dx2, dy2 }: { x: number; y: number; dx1: number; dy1: number; dx2: number; dy2: number }) {
  const m = 12;
  const l1 = Math.hypot(dx1, dy1) || 1;
  const l2 = Math.hypot(dx2, dy2) || 1;
  const ax = (dx1 / l1) * m;
  const ay = (dy1 / l1) * m;
  const bx = (dx2 / l2) * m;
  const by = (dy2 / l2) * m;
  return (
    <path
      d={`M ${n(x + ax)} ${n(y + ay)} L ${n(x + ax + bx)} ${n(y + ay + by)} L ${n(x + bx)} ${n(y + by)}`}
      fill="none"
      stroke={LIJN}
      strokeWidth={1.4}
    />
  );
}

/** Een boogje in een hoek, met een opschrift. */
function HoekBoog({
  x,
  y,
  van,
  tot,
  straal = 26,
  opschrift,
  kleur = MERK,
}: {
  x: number;
  y: number;
  /* Graden, tegen de wijzers van de klok gemeten vanaf rechts. */
  van: number;
  tot: number;
  straal?: number;
  opschrift?: string;
  kleur?: string;
}) {
  const p = (hoek: number) => `${n(x + straal * Math.cos(rad(hoek)))} ${n(y - straal * Math.sin(rad(hoek)))}`;
  const groot = Math.abs(tot - van) > 180 ? 1 : 0;
  const midden = (van + tot) / 2;
  const lx = x + (straal + 16) * Math.cos(rad(midden));
  const ly = y - (straal + 16) * Math.sin(rad(midden));
  return (
    <>
      <path d={`M ${p(van)} A ${straal} ${straal} 0 ${groot} 0 ${p(tot)}`} fill="none" stroke={kleur} strokeWidth={2} />
      {opschrift ? (
        <Label x={lx} y={ly} kleur={kleur} groot>
          {opschrift}
        </Label>
      ) : null}
    </>
  );
}

// ---------------------------------------------------------------------------
// Hoeken

function Hoek({ graden, opschrift }: { graden: number; opschrift: string }) {
  const x = 40;
  const y = 130;
  const lengte = 150;
  const bx = x + lengte * Math.cos(rad(graden));
  const by = y - lengte * Math.sin(rad(graden));
  // Een stompe hoek loopt naar links, dus het blad moet breder dan het been.
  const breedte = 230;
  return (
    <Blad breedte={breedte} hoogte={170} titel={`Een hoek van ${graden} graden`}>
      <g transform={graden > 90 ? "translate(60 0)" : ""}>
        <line x1={x} y1={y} x2={n(x + lengte)} y2={y} stroke={LIJN} strokeWidth={2.4} strokeLinecap="round" />
        <line x1={x} y1={y} x2={n(bx)} y2={n(by)} stroke={LIJN} strokeWidth={2.4} strokeLinecap="round" />
        {graden === 90 && opschrift !== "?" ? <RechteHoek x={x} y={y} dx1={1} dy1={0} dx2={0} dy2={-1} /> : null}
        <HoekBoog x={x} y={y} van={0} tot={graden} opschrift={opschrift} straal={graden < 40 ? 42 : 30} />
        <circle cx={x} cy={y} r={3} fill={LIJN} />
      </g>
    </Blad>
  );
}

// ---------------------------------------------------------------------------
// Driehoeken

/** Bouwt een driehoek uit zijn drie hoeken. */
function driehoekPunten(a: number, b: number, basis: number, x0: number, y0: number) {
  const c = 180 - a - b;
  const d = (basis * Math.sin(rad(b))) / Math.sin(rad(c));
  return {
    A: { x: x0, y: y0 },
    B: { x: x0 + basis, y: y0 },
    C: { x: x0 + d * Math.cos(rad(a)), y: y0 - d * Math.sin(rad(a)) },
  };
}

const DRIEHOEKEN: Record<string, { a: number; b: number; gelijk: number[]; recht?: boolean; naam: string }> = {
  gelijkzijdig: { a: 60, b: 60, gelijk: [1, 1, 1], naam: "Een gelijkzijdige driehoek" },
  gelijkbenig: { a: 72, b: 72, gelijk: [0, 1, 1], naam: "Een gelijkbenige driehoek" },
  ongelijkbenig: { a: 64, b: 46, gelijk: [], naam: "Een ongelijkbenige driehoek" },
  rechthoekig: { a: 90, b: 37, gelijk: [], recht: true, naam: "Een rechthoekige driehoek" },
  "rechthoekig-gelijkbenig": { a: 90, b: 45, gelijk: [1, 0, 1], recht: true, naam: "Een rechthoekige gelijkbenige driehoek" },
  /* gelijk: welke zijden een streepje krijgen, in de volgorde AB, BC, CA. */
  stomphoekig: { a: 118, b: 33, gelijk: [], naam: "Een stomphoekige driehoek" },
};

function Driehoek({ soort }: { soort: string }) {
  const vorm = DRIEHOEKEN[soort] ?? DRIEHOEKEN.ongelijkbenig;
  const { A, B, C } = driehoekPunten(vorm.a, vorm.b, 170, 30, 150);
  const kader = kaderRond([A, B, C]);
  return (
    <Blad breedte={n(kader[2])} hoogte={n(kader[3])} kader={kader} titel={vorm.naam}>
      <polygon
        points={`${n(A.x)},${n(A.y)} ${n(B.x)},${n(B.y)} ${n(C.x)},${n(C.y)}`}
        fill="var(--forest)"
        fillOpacity={0.08}
        stroke={LIJN}
        strokeWidth={2.4}
        strokeLinejoin="round"
      />
      {vorm.recht ? <RechteHoek x={A.x} y={A.y} dx1={B.x - A.x} dy1={B.y - A.y} dx2={C.x - A.x} dy2={C.y - A.y} /> : null}
      {/* De drie zijden: AB, BC, CA. Een 1 betekent één streepje. */}
      {vorm.gelijk[0] ? <Streepjes x1={A.x} y1={A.y} x2={B.x} y2={B.y} aantal={1} /> : null}
      {vorm.gelijk[1] ? <Streepjes x1={B.x} y1={B.y} x2={C.x} y2={C.y} aantal={1} /> : null}
      {vorm.gelijk[2] ? <Streepjes x1={C.x} y1={C.y} x2={A.x} y2={A.y} aantal={1} /> : null}
    </Blad>
  );
}

/** Een driehoek met de hoeken erbij, bijvoorbeeld 50-60-? */
function DriehoekHoeken({ opschriften }: { opschriften: string[] }) {
  const getal = (s: string) => (/^\d+$/.test(s) ? Number(s) : null);
  const g = opschriften.map(getal);
  // De ontbrekende hoek halen we uit de hoekensom, alleen om te kunnen tekenen.
  const gekend = g.filter((x): x is number => x !== null);
  const rest = gekend.length === 2 ? 180 - gekend[0] - gekend[1] : 60;
  const hoeken = g.map((x) => x ?? rest);
  const { A, B, C } = driehoekPunten(hoeken[0], hoeken[1], 170, 40, 155);
  const punten = [A, B, C];
  // Naar het midden toe, zodat het opschrift binnen de driehoek valt.
  const mx = (A.x + B.x + C.x) / 3;
  const my = (A.y + B.y + C.y) / 3;
  const kader = kaderRond(punten, 26);
  return (
    <Blad breedte={n(kader[2])} hoogte={n(kader[3])} kader={kader} titel="Een driehoek met zijn hoeken">
      <polygon
        points={punten.map((p) => `${n(p.x)},${n(p.y)}`).join(" ")}
        fill="var(--forest)"
        fillOpacity={0.08}
        stroke={LIJN}
        strokeWidth={2.4}
        strokeLinejoin="round"
      />
      {punten.map((p, i) => {
        const dx = mx - p.x;
        const dy = my - p.y;
        const l = Math.hypot(dx, dy) || 1;
        return (
          <Label key={i} x={p.x + (dx / l) * 36} y={p.y + (dy / l) * 30} kleur={MERK} groot>
            {/^\d+$/.test(opschriften[i]) ? `${opschriften[i]}°` : opschriften[i]}
          </Label>
        );
      })}
    </Blad>
  );
}

// ---------------------------------------------------------------------------
// Vierhoeken

const VIERHOEKEN: Record<string, { punten: number[][]; gelijk?: number[]; evenwijdig?: number[]; recht?: boolean; naam: string }> = {
  vierkant: { punten: [[40, 30], [170, 30], [170, 160], [40, 160]], gelijk: [1, 1, 1, 1], recht: true, naam: "Een vierkant" },
  rechthoek: { punten: [[30, 40], [210, 40], [210, 150], [30, 150]], gelijk: [1, 2, 1, 2], recht: true, naam: "Een rechthoek" },
  parallellogram: { punten: [[70, 40], [230, 40], [180, 150], [20, 150]], evenwijdig: [1, 2, 1, 2], naam: "Een parallellogram" },
  trapezium: { punten: [[75, 40], [185, 40], [230, 150], [30, 150]], evenwijdig: [1, 0, 1, 0], naam: "Een trapezium" },
  ruit: { punten: [[110, 25], [200, 95], [110, 165], [20, 95]], gelijk: [1, 1, 1, 1], naam: "Een ruit" },
};

/** Een pijltje midden op een zijde, om evenwijdige zijden aan te duiden. */
function Pijltjes({ x1, y1, x2, y2, aantal }: { x1: number; y1: number; x2: number; y2: number; aantal: number }) {
  const mx = (x1 + x2) / 2;
  const my = (y1 + y2) / 2;
  const l = Math.hypot(x2 - x1, y2 - y1) || 1;
  const ux = (x2 - x1) / l;
  const uy = (y2 - y1) / l;
  const px = -uy;
  const py = ux;
  return (
    <>
      {Array.from({ length: aantal }, (_, i) => {
        const o = (i - (aantal - 1) / 2) * 11;
        const cx = mx + ux * o;
        const cy = my + uy * o;
        return (
          <path
            key={i}
            d={`M ${n(cx - ux * 5 + px * 5)} ${n(cy - uy * 5 + py * 5)} L ${n(cx + ux * 5)} ${n(cy + uy * 5)} L ${n(cx - ux * 5 - px * 5)} ${n(cy - uy * 5 - py * 5)}`}
            fill="none"
            stroke={MERK}
            strokeWidth={2}
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        );
      })}
    </>
  );
}

function Vierhoek({ soort }: { soort: string }) {
  const vorm = VIERHOEKEN[soort] ?? VIERHOEKEN.rechthoek;
  const p = vorm.punten;
  const zijden = [0, 1, 2, 3].map((i) => [p[i], p[(i + 1) % 4]]);
  return (
    <Blad breedte={250} hoogte={190} titel={vorm.naam}>
      <polygon
        points={p.map((q) => `${q[0]},${q[1]}`).join(" ")}
        fill="var(--forest)"
        fillOpacity={0.08}
        stroke={LIJN}
        strokeWidth={2.4}
        strokeLinejoin="round"
      />
      {vorm.recht ? <RechteHoek x={p[0][0]} y={p[0][1]} dx1={1} dy1={0} dx2={0} dy2={1} /> : null}
      {zijden.map(([a, b], i) => {
        const merk = vorm.gelijk?.[i];
        const pijl = vorm.evenwijdig?.[i];
        if (merk) return <Streepjes key={i} x1={a[0]} y1={a[1]} x2={b[0]} y2={b[1]} aantal={merk} />;
        if (pijl) return <Pijltjes key={i} x1={a[0]} y1={a[1]} x2={b[0]} y2={b[1]} aantal={pijl} />;
        return null;
      })}
    </Blad>
  );
}

// ---------------------------------------------------------------------------
// Twee snijdende rechten, en twee evenwijdige rechten met een snijlijn

function Snijlijn({ graden, neven }: { graden: number; neven: boolean }) {
  const x = 125;
  const y = 95;
  const l = 115;
  const bx = l * Math.cos(rad(graden));
  const by = l * Math.sin(rad(graden));
  return (
    <Blad breedte={260} hoogte={195} titel={`Twee snijdende rechten met een hoek van ${graden} graden`}>
      <line x1={n(x - l)} y1={y} x2={n(x + l)} y2={y} stroke={LIJN} strokeWidth={2.4} strokeLinecap="round" />
      <line x1={n(x - bx)} y1={n(y + by)} x2={n(x + bx)} y2={n(y - by)} stroke={LIJN} strokeWidth={2.4} strokeLinecap="round" />
      <HoekBoog x={x} y={y} van={0} tot={graden} straal={30} opschrift={`${graden}°`} />
      {neven ? (
        <HoekBoog x={x} y={y} van={graden} tot={180} straal={30} opschrift="?" kleur={VUL} />
      ) : (
        <HoekBoog x={x} y={y} van={180} tot={180 + graden} straal={30} opschrift="?" kleur={VUL} />
      )}
      <circle cx={x} cy={y} r={3} fill={LIJN} />
    </Blad>
  );
}

function Evenwijdig({ graden, binnen }: { graden: number; binnen: boolean }) {
  // Twee horizontale rechten, en een snijlijn die er schuin doorloopt.
  const y1 = 45;
  const y2 = 140;
  const helling = rad(graden);
  // x-verplaatsing tussen de twee snijpunten.
  const dx = (y2 - y1) / Math.tan(helling);
  const s1x = 95;
  const s2x = s1x + dx;
  // De snijlijn loopt aan weerszijden een stuk door voorbij de twee rechten.
  const over = 45;
  const lengte = Math.hypot(s2x - s1x, y2 - y1) || 1;
  const ux = (s2x - s1x) / lengte;
  const uy = (y2 - y1) / lengte;
  return (
    <Blad breedte={280} hoogte={200} titel={`Twee evenwijdige rechten met een snijlijn van ${graden} graden`}>
      <line x1={15} y1={y1} x2={265} y2={y1} stroke={LIJN} strokeWidth={2.4} strokeLinecap="round" />
      <line x1={15} y1={y2} x2={265} y2={y2} stroke={LIJN} strokeWidth={2.4} strokeLinecap="round" />
      <Pijltjes x1={15} y1={y1} x2={265} y2={y1} aantal={1} />
      <Pijltjes x1={15} y1={y2} x2={265} y2={y2} aantal={1} />
      <line
        x1={n(s1x - ux * over)}
        y1={n(y1 - uy * over)}
        x2={n(s2x + ux * over)}
        y2={n(y2 + uy * over)}
        stroke={LIJN}
        strokeWidth={2.4}
        strokeLinecap="round"
      />
      <HoekBoog x={s1x} y={y1} van={0} tot={-graden} straal={26} opschrift={`${graden}°`} />
      {binnen ? (
        /* De binnenhoek aan dezelfde kant van de snijlijn: die ligt bóven de
           onderste rechte, en is samen met de gegeven hoek 180°. */
        <HoekBoog x={s2x} y={y2} van={n(180 - graden)} tot={0} straal={26} opschrift="?" kleur={VUL} />
      ) : (
        <HoekBoog x={s2x} y={y2} van={0} tot={-graden} straal={26} opschrift="?" kleur={VUL} />
      )}
      <circle cx={n(s1x)} cy={y1} r={3} fill={LIJN} />
      <circle cx={n(s2x)} cy={y2} r={3} fill={LIJN} />
    </Blad>
  );
}

// ---------------------------------------------------------------------------
// De cirkel en zijn delen

function Cirkeldeel({ soort, stil }: { soort: string; stil: boolean }) {
  const c = 100;
  const r = 72;
  const naam = soort === "diameter" ? "De diameter" : soort === "koorde" ? "Een koorde" : "De straal";
  return (
    <Blad breedte={230} hoogte={205} titel={`Een cirkel met ${naam.toLowerCase()} aangeduid`}>
      <circle cx={c} cy={c} r={r} fill="var(--forest)" fillOpacity={0.06} stroke={LIJN} strokeWidth={2.4} />
      {soort === "straal" ? (
        <>
          <line x1={c} y1={c} x2={n(c + r)} y2={c} stroke={MERK} strokeWidth={2.6} />
          {stil ? null : (
            <Label x={c + r / 2} y={c - 14} kleur={MERK}>
              straal
            </Label>
          )}
          <circle cx={c} cy={c} r={3.5} fill={LIJN} />
        </>
      ) : soort === "diameter" ? (
        <>
          <line x1={n(c - r)} y1={c} x2={n(c + r)} y2={c} stroke={MERK} strokeWidth={2.6} />
          {stil ? null : (
            <Label x={c} y={c - 14} kleur={MERK}>
              diameter
            </Label>
          )}
          <circle cx={c} cy={c} r={3.5} fill={LIJN} />
        </>
      ) : (
        <>
          <line
            x1={n(c + r * Math.cos(rad(210)))}
            y1={n(c - r * Math.sin(rad(210)))}
            x2={n(c + r * Math.cos(rad(330)))}
            y2={n(c - r * Math.sin(rad(330)))}
            stroke={MERK}
            strokeWidth={2.6}
          />
          {stil ? null : (
            <Label x={c} y={c + r / 2 + 30} kleur={MERK}>
              koorde
            </Label>
          )}
        </>
      )}
    </Blad>
  );
}

// ---------------------------------------------------------------------------
// De merkwaardige lijnen in een driehoek

function Merkwaardig({ soort, stil }: { soort: string; stil: boolean }) {
  const { A, B, C } = driehoekPunten(62, 44, 180, 35, 160);
  const naam =
    soort === "hoogtelijn"
      ? "De hoogtelijn"
      : soort === "zwaartelijn"
        ? "De zwaartelijn"
        : soort === "middelloodlijn"
          ? "De middelloodlijn"
          : "De bissectrice";

  // Het midden van AB, en de voet van de loodlijn uit C op AB.
  const mAB = { x: (A.x + B.x) / 2, y: (A.y + B.y) / 2 };
  const voet = { x: C.x, y: A.y };

  let lijn: [number, number, number, number];
  if (soort === "hoogtelijn") lijn = [C.x, C.y, voet.x, voet.y];
  else if (soort === "zwaartelijn") lijn = [C.x, C.y, mAB.x, mAB.y];
  else if (soort === "middelloodlijn") lijn = [mAB.x, mAB.y - 105, mAB.x, mAB.y + 18];
  else {
    // Bissectrice uit C: deelt hoek C middendoor en loopt door tot op AB.
    const hoekA = Math.atan2(A.y - C.y, A.x - C.x);
    const hoekB = Math.atan2(B.y - C.y, B.x - C.x);
    const mid = (hoekA + hoekB) / 2;
    const t = (A.y - C.y) / Math.sin(mid);
    lijn = [C.x, C.y, C.x + t * Math.cos(mid), A.y];
  }

  const kader = kaderRond([A, B, C, { x: lijn[0], y: lijn[1] }, { x: lijn[2], y: lijn[3] }, { x: 125, y: 192 }], 24);
  return (
    <Blad breedte={n(kader[2])} hoogte={n(kader[3])} kader={kader} titel={`${naam} in een driehoek`}>
      <polygon
        points={`${n(A.x)},${n(A.y)} ${n(B.x)},${n(B.y)} ${n(C.x)},${n(C.y)}`}
        fill="var(--forest)"
        fillOpacity={0.08}
        stroke={LIJN}
        strokeWidth={2.4}
        strokeLinejoin="round"
      />
      <line x1={n(lijn[0])} y1={n(lijn[1])} x2={n(lijn[2])} y2={n(lijn[3])} stroke={MERK} strokeWidth={2.6} />
      {soort === "hoogtelijn" ? <RechteHoek x={voet.x} y={voet.y} dx1={-1} dy1={0} dx2={0} dy2={-1} /> : null}
      {soort === "middelloodlijn" ? (
        <>
          <RechteHoek x={mAB.x} y={mAB.y} dx1={1} dy1={0} dx2={0} dy2={-1} />
          <Streepjes x1={A.x} y1={A.y} x2={mAB.x} y2={mAB.y} aantal={1} />
          <Streepjes x1={mAB.x} y1={mAB.y} x2={B.x} y2={B.y} aantal={1} />
        </>
      ) : null}
      {soort === "zwaartelijn" ? (
        <>
          <Streepjes x1={A.x} y1={A.y} x2={mAB.x} y2={mAB.y} aantal={1} />
          <Streepjes x1={mAB.x} y1={mAB.y} x2={B.x} y2={B.y} aantal={1} />
        </>
      ) : null}
      {soort === "bissectrice" ? (
        <>
          <HoekBoog
            x={C.x}
            y={C.y}
            van={n(-(Math.atan2(A.y - C.y, A.x - C.x) * 180) / Math.PI)}
            tot={n(-(((Math.atan2(A.y - C.y, A.x - C.x) + Math.atan2(B.y - C.y, B.x - C.x)) / 2) * 180) / Math.PI)}
            straal={34}
          />
          <HoekBoog
            x={C.x}
            y={C.y}
            van={n(-(((Math.atan2(A.y - C.y, A.x - C.x) + Math.atan2(B.y - C.y, B.x - C.x)) / 2) * 180) / Math.PI)}
            tot={n(-(Math.atan2(B.y - C.y, B.x - C.x) * 180) / Math.PI)}
            straal={34}
          />
        </>
      ) : null}
      {stil ? null : (
        <Label x={125} y={192} kleur={MERK}>
          {naam.toLowerCase().replace("de ", "")}
        </Label>
      )}
    </Blad>
  );
}

// ---------------------------------------------------------------------------
// Symmetrieassen

const ASSEN: Record<string, { punten: number[][]; assen: "geen" | "alle" | "top"; middelpunt: boolean; naam: string }> = {
  vierkant: { punten: [[55, 25], [175, 25], [175, 145], [55, 145]], assen: "alle", middelpunt: true, naam: "Een vierkant met zijn symmetrieassen" },
  rechthoek: { punten: [[25, 40], [205, 40], [205, 130], [25, 130]], assen: "top", middelpunt: true, naam: "Een rechthoek met zijn symmetrieassen" },
  gelijkzijdig: { punten: [[30, 150], [200, 150], [115, 3]], assen: "alle", middelpunt: false, naam: "Een gelijkzijdige driehoek met zijn symmetrieassen" },
  gelijkbenig: { punten: [[40, 150], [190, 150], [115, 20]], assen: "top", middelpunt: false, naam: "Een gelijkbenige driehoek met zijn symmetrieas" },
  parallellogram: { punten: [[70, 35], [225, 35], [175, 145], [20, 145]], assen: "geen", middelpunt: true, naam: "Een parallellogram, zonder symmetrieas" },
  ruit: { punten: [[115, 15], [200, 90], [115, 165], [30, 90]], assen: "alle", middelpunt: true, naam: "Een ruit met zijn symmetrieassen" },
};

/*
  De assen worden uitgerekend uit de figuur zelf, niet met de hand ingetikt.
  Bij een driehoek loopt elke as van een hoekpunt naar het midden van de
  overstaande zijde; bij een vierhoek van het midden van een zijde naar het
  midden van de overstaande zijde, en bij een vierkant of ruit ook langs de
  diagonalen. "top" betekent: alleen de eerste as, voor een figuur die er maar
  één heeft (gelijkbenige driehoek) of twee (rechthoek).
*/
function assenVan(punten: number[][], welke: "geen" | "alle" | "top", ruit: boolean) {
  if (welke === "geen") return [];
  const p = punten.map(([x, y]) => ({ x, y }));
  const mx = p.reduce((s, q) => s + q.x, 0) / p.length;
  const my = p.reduce((s, q) => s + q.y, 0) / p.length;
  /* Trekt de as door tot een eind voorbij de figuur. */
  const door = (ax: number, ay: number, bx: number, by: number) => {
    const l = Math.hypot(bx - ax, by - ay) || 1;
    const ux = (bx - ax) / l;
    const uy = (by - ay) / l;
    return [ax - ux * 16, ay - uy * 16, bx + ux * 16, by + uy * 16];
  };
  const assen: number[][] = [];
  if (p.length === 3) {
    // Uit elk hoekpunt naar het midden van de overstaande zijde.
    for (let i = 0; i < 3; i++) {
      const top = p[(i + 2) % 3];
      const a = p[i];
      const b = p[(i + 1) % 3];
      assen.push(door(top.x, top.y, (a.x + b.x) / 2, (a.y + b.y) / 2));
    }
  } else {
    // Van het midden van een zijde naar het midden van de overstaande zijde.
    for (let i = 0; i < 2; i++) {
      const a = { x: (p[i].x + p[i + 1].x) / 2, y: (p[i].y + p[i + 1].y) / 2 };
      const b = { x: (p[(i + 2) % 4].x + p[(i + 3) % 4].x) / 2, y: (p[(i + 2) % 4].y + p[(i + 3) % 4].y) / 2 };
      assen.push(door(a.x, a.y, b.x, b.y));
    }
    if (welke === "alle") {
      // Bij een vierkant zijn de diagonalen er ook assen; bij een ruit net niet
      // de diagonalen maar de lijnen door de overstaande hoekpunten, en dat is
      // hetzelfde. Bij een ruit vervallen de twee hierboven.
      const d = [door(p[0].x, p[0].y, p[2].x, p[2].y), door(p[1].x, p[1].y, p[3].x, p[3].y)];
      if (ruit) return d;
      assen.push(...d);
    }
  }
  const aantal = welke === "top" ? (p.length === 3 ? 1 : 2) : assen.length;
  void mx;
  void my;
  return assen.slice(0, aantal);
}

function Assen({ soort }: { soort: string }) {
  const vorm = ASSEN[soort] ?? ASSEN.vierkant;
  const assen = assenVan(vorm.punten, vorm.assen, soort === "ruit");
  const mx = vorm.punten.reduce((s, p) => s + p[0], 0) / vorm.punten.length;
  const my = vorm.punten.reduce((s, p) => s + p[1], 0) / vorm.punten.length;
  const kader = kaderRond(
    [...vorm.punten.map(([x, y]) => ({ x, y })), ...assen.flatMap((a) => [{ x: a[0], y: a[1] }, { x: a[2], y: a[3] }])],
    18
  );
  return (
    <Blad breedte={n(kader[2])} hoogte={n(kader[3])} kader={kader} titel={vorm.naam}>
      <polygon
        points={vorm.punten.map((p) => `${p[0]},${p[1]}`).join(" ")}
        fill="var(--forest)"
        fillOpacity={0.08}
        stroke={LIJN}
        strokeWidth={2.4}
        strokeLinejoin="round"
      />
      {assen.map((a, i) => (
        <line key={i} x1={n(a[0])} y1={n(a[1])} x2={n(a[2])} y2={n(a[3])} stroke={MERK} strokeWidth={2} strokeDasharray="7 5" />
      ))}
      {vorm.middelpunt ? <circle cx={n(mx)} cy={n(my)} r={4} fill={MERK} /> : null}
    </Blad>
  );
}

// ---------------------------------------------------------------------------
// Transformaties

function Beweging({ soort }: { soort: string }) {
  // Een vlaggetje, want daaraan zie je meteen of de figuur gedraaid of
  // gespiegeld is. Bij een symmetrische figuur zou je dat niet zien.
  const vlag = (x: number, y: number, schaal: number, draai: number, spiegel: boolean) => {
    const punten = [
      [0, 0],
      [0, -70],
      [45, -55],
      [0, -40],
    ];
    return punten
      .map(([px, py]) => {
        const sx = spiegel ? -px : px;
        const c = Math.cos(rad(draai));
        const s = Math.sin(rad(draai));
        return `${n(x + (sx * c - py * s) * schaal)},${n(y + (sx * s + py * c) * schaal)}`;
      })
      .join(" ");
  };

  const naam = soort === "rotatie" ? "Een rotatie" : soort === "spiegeling" ? "Een spiegeling" : "Een translatie";

  // Bij een rotatie zwaait de vlag naar rechts uit, dus daar is meer plaats nodig.
  const draaipunt = { x: 75, y: 95 };
  return (
    <Blad breedte={280} hoogte={soort === "rotatie" ? 200 : 165} titel={`${naam}: de figuur voor en na`}>
      {/* De figuur zoals ze eerst stond. */}
      {soort === "rotatie" ? null : (
        <polygon points={vlag(60, 130, 1, 0, false)} fill="var(--forest)" fillOpacity={0.12} stroke={LIJN} strokeWidth={2.2} strokeLinejoin="round" />
      )}
      {soort === "translatie" ? (
        <>
          <polygon points={vlag(190, 130, 1, 0, false)} fill={MERK} fillOpacity={0.18} stroke={MERK} strokeWidth={2.2} strokeLinejoin="round" />
          <line x1={75} y1={145} x2={185} y2={145} stroke={MERK} strokeWidth={2} markerEnd="url(#pijl)" />
        </>
      ) : soort === "rotatie" ? (
        <>
          <polygon points={vlag(draaipunt.x, draaipunt.y, 1, 0, false)} fill="var(--forest)" fillOpacity={0.12} stroke={LIJN} strokeWidth={2.2} strokeLinejoin="round" />
          <polygon points={vlag(draaipunt.x, draaipunt.y, 1, 90, false)} fill={MERK} fillOpacity={0.18} stroke={MERK} strokeWidth={2.2} strokeLinejoin="round" />
          <HoekBoog x={draaipunt.x} y={draaipunt.y} van={90} tot={0} straal={46} opschrift="90°" />
          <circle cx={draaipunt.x} cy={draaipunt.y} r={4} fill={MERK} />
        </>
      ) : (
        <>
          <line x1={145} y1={14} x2={145} y2={155} stroke={MERK} strokeWidth={2} strokeDasharray="7 5" />
          <polygon points={vlag(230, 130, 1, 0, true)} fill={MERK} fillOpacity={0.18} stroke={MERK} strokeWidth={2.2} strokeLinejoin="round" />
        </>
      )}
      <defs>
        <marker id="pijl" markerWidth={8} markerHeight={8} refX={6} refY={4} orient="auto">
          <path d="M 0 0 L 8 4 L 0 8 z" fill={MERK} />
        </marker>
      </defs>
    </Blad>
  );
}

// ---------------------------------------------------------------------------
// Figuren met maten erbij (metend rekenen)

/** Een maatlijn met een getal erbij, naast of onder een zijde. */
function Maatlijn({ x1, y1, x2, y2, tekst, kant = 1 }: { x1: number; y1: number; x2: number; y2: number; tekst: string; kant?: number }) {
  const l = Math.hypot(x2 - x1, y2 - y1) || 1;
  const px = (-(y2 - y1) / l) * 16 * kant;
  const py = ((x2 - x1) / l) * 16 * kant;
  return (
    <>
      <line x1={n(x1 + px)} y1={n(y1 + py)} x2={n(x2 + px)} y2={n(y2 + py)} stroke={MERK} strokeWidth={1.6} />
      <line x1={n(x1 + px * 0.3)} y1={n(y1 + py * 0.3)} x2={n(x1 + px * 1.3)} y2={n(y1 + py * 1.3)} stroke={MERK} strokeWidth={1.4} />
      <line x1={n(x2 + px * 0.3)} y1={n(y2 + py * 0.3)} x2={n(x2 + px * 1.3)} y2={n(y2 + py * 1.3)} stroke={MERK} strokeWidth={1.4} />
      <Label x={(x1 + x2) / 2 + px * 2.7} y={(y1 + y2) / 2 + py * 2.2} kleur={MERK}>
        {tekst}
      </Label>
    </>
  );
}

function Maat({ soort, maten }: { soort: string; maten: number[] }) {
  const eenheid = "cm";
  const vlak = { fill: "var(--forest)", fillOpacity: 0.08, stroke: LIJN, strokeWidth: 2.4, strokeLinejoin: "round" as const };

  if (soort === "vierkant" || soort === "rechthoek") {
    const [a, b] = soort === "vierkant" ? [maten[0], maten[0]] : maten;
    // Op schaal, maar nooit te klein of te groot om te tonen.
    const eenh = Math.min(22, 180 / Math.max(a, b));
    const w = a * eenh;
    const h = b * eenh;
    return (
      <Blad breedte={n(w + 90)} hoogte={n(h + 80)} titel={`Een ${soort} van ${a} bij ${b} ${eenheid}`}>
        <rect x={40} y={25} width={n(w)} height={n(h)} {...vlak} />
        <RechteHoek x={40} y={25} dx1={1} dy1={0} dx2={0} dy2={1} />
        <Maatlijn x1={40} y1={n(25 + h)} x2={n(40 + w)} y2={n(25 + h)} tekst={`${a} ${eenheid}`} />
        <Maatlijn x1={n(40 + w)} y1={25} x2={n(40 + w)} y2={n(25 + h)} tekst={`${b} ${eenheid}`} kant={-1} />
      </Blad>
    );
  }

  if (soort === "driehoek") {
    const [basis, hoogte] = maten;
    const eenh = Math.min(22, 170 / Math.max(basis, hoogte));
    const w = basis * eenh;
    const h = hoogte * eenh;
    const top = 40 + w * 0.36;
    return (
      <Blad breedte={n(w + 100)} hoogte={n(h + 80)} titel={`Een driehoek met basis ${basis} en hoogte ${hoogte} ${eenheid}`}>
        <polygon points={`40,${n(25 + h)} ${n(40 + w)},${n(25 + h)} ${n(top)},25`} {...vlak} />
        <line x1={n(top)} y1={25} x2={n(top)} y2={n(25 + h)} stroke={MERK} strokeWidth={1.8} strokeDasharray="6 4" />
        <RechteHoek x={n(top)} y={n(25 + h)} dx1={1} dy1={0} dx2={0} dy2={-1} />
        <Maatlijn x1={40} y1={n(25 + h)} x2={n(40 + w)} y2={n(25 + h)} tekst={`basis ${basis} ${eenheid}`} />
        <Label x={n(top + 42)} y={n(25 + h / 2)} kleur={MERK}>
          {`h ${hoogte} ${eenheid}`}
        </Label>
      </Blad>
    );
  }

  if (soort === "parallellogram") {
    const [basis, hoogte] = maten;
    const eenh = Math.min(20, 160 / Math.max(basis, hoogte));
    const w = basis * eenh;
    const h = hoogte * eenh;
    const schuin = 40;
    return (
      <Blad breedte={n(w + schuin + 100)} hoogte={n(h + 80)} titel={`Een parallellogram met basis ${basis} en hoogte ${hoogte} ${eenheid}`}>
        <polygon points={`40,${n(25 + h)} ${n(40 + w)},${n(25 + h)} ${n(40 + w + schuin)},25 ${n(40 + schuin)},25`} {...vlak} />
        <line x1={n(40 + schuin)} y1={25} x2={n(40 + schuin)} y2={n(25 + h)} stroke={MERK} strokeWidth={1.8} strokeDasharray="6 4" />
        <RechteHoek x={n(40 + schuin)} y={n(25 + h)} dx1={1} dy1={0} dx2={0} dy2={-1} />
        <Maatlijn x1={40} y1={n(25 + h)} x2={n(40 + w)} y2={n(25 + h)} tekst={`basis ${basis} ${eenheid}`} />
        <Label x={n(40 + schuin + 40)} y={n(25 + h / 2)} kleur={MERK}>
          {`h ${hoogte} ${eenheid}`}
        </Label>
      </Blad>
    );
  }

  if (soort === "trapezium") {
    const [boven, onder, hoogte] = maten;
    const eenh = Math.min(18, 170 / Math.max(onder, hoogte));
    const wb = boven * eenh;
    const wo = onder * eenh;
    const h = hoogte * eenh;
    const inspring = (wo - wb) / 2;
    return (
      <Blad breedte={n(wo + 110)} hoogte={n(h + 105)} titel={`Een trapezium met evenwijdige zijden ${boven} en ${onder} en hoogte ${hoogte} ${eenheid}`}>
        <polygon points={`40,${n(35 + h)} ${n(40 + wo)},${n(35 + h)} ${n(40 + inspring + wb)},35 ${n(40 + inspring)},35`} {...vlak} />
        <line x1={n(40 + inspring)} y1={35} x2={n(40 + inspring)} y2={n(35 + h)} stroke={MERK} strokeWidth={1.8} strokeDasharray="6 4" />
        <Maatlijn x1={n(40 + inspring)} y1={35} x2={n(40 + inspring + wb)} y2={35} tekst={`${boven} ${eenheid}`} kant={-1} />
        <Maatlijn x1={40} y1={n(35 + h)} x2={n(40 + wo)} y2={n(35 + h)} tekst={`${onder} ${eenheid}`} />
        <Label x={n(40 + inspring + 32)} y={n(35 + h / 2 + 14)} kleur={MERK}>
          {`h ${hoogte}`}
        </Label>
      </Blad>
    );
  }

  if (soort === "ruit") {
    const [d1, d2] = maten;
    const eenh = Math.min(20, 150 / Math.max(d1, d2));
    const w = d1 * eenh;
    const h = d2 * eenh;
    const cx = 50 + w / 2;
    const cy = 30 + h / 2;
    return (
      <Blad breedte={n(w + 120)} hoogte={n(h + 70)} titel={`Een ruit met diagonalen ${d1} en ${d2} ${eenheid}`}>
        <polygon points={`${n(cx)},30 ${n(50 + w)},${n(cy)} ${n(cx)},${n(30 + h)} 50,${n(cy)}`} {...vlak} />
        <line x1={50} y1={n(cy)} x2={n(50 + w)} y2={n(cy)} stroke={MERK} strokeWidth={1.8} strokeDasharray="6 4" />
        <line x1={n(cx)} y1={30} x2={n(cx)} y2={n(30 + h)} stroke={MERK} strokeWidth={1.8} strokeDasharray="6 4" />
        <RechteHoek x={n(cx)} y={n(cy)} dx1={1} dy1={0} dx2={0} dy2={-1} />
        <Label x={n(cx - w / 4)} y={n(cy - 14)} kleur={MERK}>
          {`${d1} ${eenheid}`}
        </Label>
        <Label x={n(cx + 30)} y={n(cy + h / 4)} kleur={MERK}>
          {`${d2} ${eenheid}`}
        </Label>
      </Blad>
    );
  }

  // cirkel: maten[0] is de maat, en soort is "cirkel-straal" of "cirkel-diameter"
  const diameter = soort.endsWith("diameter");
  const maat = maten[0];
  const r = 72;
  const c = 92;
  return (
    <Blad breedte={230} hoogte={200} titel={`Een cirkel met een ${diameter ? "diameter" : "straal"} van ${maat} ${eenheid}`}>
      <circle cx={c} cy={c} r={r} fill="var(--forest)" fillOpacity={0.06} stroke={LIJN} strokeWidth={2.4} />
      {diameter ? (
        <line x1={n(c - r)} y1={c} x2={n(c + r)} y2={c} stroke={MERK} strokeWidth={2.4} />
      ) : (
        <line x1={c} y1={c} x2={n(c + r)} y2={c} stroke={MERK} strokeWidth={2.4} />
      )}
      <circle cx={c} cy={c} r={3.5} fill={LIJN} />
      <Label x={diameter ? c : n(c + r / 2)} y={n(c - 14)} kleur={MERK}>
        {`${diameter ? "d" : "r"} = ${String(maat).replace(".", ",")} ${eenheid}`}
      </Label>
    </Blad>
  );
}

// ---------------------------------------------------------------------------
// Ruimtefiguren, in schuine projectie

function Ruimte({ soort, maten }: { soort: string; maten: number[] }) {
  const eenheid = "cm";

  if (soort === "cilinder") {
    const [straal, hoogte] = maten;
    const eenh = Math.min(15, 120 / hoogte);
    const rx = n(straal * eenh);
    const h = n(hoogte * eenh);
    const cx = 95;
    const top = 42;
    const ry = n(Math.max(9, rx * 0.34));
    return (
      <Blad breedte={230} hoogte={n(h + top + ry + 46)} titel={`Een cilinder met straal ${straal} en hoogte ${hoogte} ${eenheid}`}>
        <path
          d={`M ${n(cx - rx)} ${top} L ${n(cx - rx)} ${n(top + h)} A ${rx} ${ry} 0 0 0 ${n(cx + rx)} ${n(top + h)} L ${n(cx + rx)} ${top}`}
          fill="var(--forest)"
          fillOpacity={0.08}
          stroke={LIJN}
          strokeWidth={2.2}
        />
        <ellipse cx={cx} cy={top} rx={rx} ry={ry} fill="var(--forest)" fillOpacity={0.14} stroke={LIJN} strokeWidth={2.2} />
        <line x1={cx} y1={top} x2={n(cx + rx)} y2={top} stroke={MERK} strokeWidth={2.2} />
        <Label x={n(cx + rx / 2)} y={n(top - 14)} kleur={MERK}>
          {`r ${straal}`}
        </Label>
        <Maatlijn x1={n(cx + rx)} y1={top} x2={n(cx + rx)} y2={n(top + h)} tekst={`h ${hoogte}`} />
      </Blad>
    );
  }

  // kubus en balk
  const [a, b, c] = soort === "kubus" ? [maten[0], maten[0], maten[0]] : maten;
  const eenh = Math.min(20, 150 / Math.max(a, b, c));
  const w = n(a * eenh);
  const h = n(b * eenh);
  const d = n(c * eenh * 0.55);
  const x = 35;
  const y = n(30 + d);
  return (
    <Blad breedte={n(w + d + 130)} hoogte={n(h + d + 100)} titel={`Een ${soort} van ${maten.join(" bij ")} ${eenheid}`}>
      {/* achterkant */}
      <polygon points={`${n(x + d)},${n(y - d)} ${n(x + w + d)},${n(y - d)} ${n(x + w + d)},${n(y + h - d)} ${n(x + d)},${n(y + h - d)}`} fill="none" stroke={FLAUW} strokeWidth={1.6} strokeDasharray="5 4" />
      <line x1={x} y1={n(y + h)} x2={n(x + d)} y2={n(y + h - d)} stroke={FLAUW} strokeWidth={1.6} strokeDasharray="5 4" />
      {/* bovenvlak en zijvlak */}
      <polygon points={`${x},${y} ${n(x + d)},${n(y - d)} ${n(x + w + d)},${n(y - d)} ${n(x + w)},${y}`} fill="var(--forest)" fillOpacity={0.14} stroke={LIJN} strokeWidth={2.2} strokeLinejoin="round" />
      <polygon points={`${n(x + w)},${y} ${n(x + w + d)},${n(y - d)} ${n(x + w + d)},${n(y + h - d)} ${n(x + w)},${n(y + h)}`} fill="var(--forest)" fillOpacity={0.1} stroke={LIJN} strokeWidth={2.2} strokeLinejoin="round" />
      {/* voorvlak */}
      <rect x={x} y={y} width={w} height={h} fill="var(--forest)" fillOpacity={0.06} stroke={LIJN} strokeWidth={2.4} />
      <Maatlijn x1={x} y1={n(y + h)} x2={n(x + w)} y2={n(y + h)} tekst={`${a}`} />
      <Maatlijn x1={n(x + w)} y1={y} x2={n(x + w)} y2={n(y + h)} tekst={`${b}`} kant={-1} />
      <Label x={n(x + w + d / 2 + 16)} y={n(y - d / 2 - 6)} kleur={MERK}>
        {`${c}`}
      </Label>
      <Label x={n((w + d) / 2 + x)} y={n(y + h + 52)} kleur={TEKST}>
        {`alles in ${eenheid}`}
      </Label>
    </Blad>
  );
}

// ---------------------------------------------------------------------------
// De maatladder

const LADDERS: Record<string, { namen: string[]; stap: string; naam: string }> = {
  lengte: { namen: ["km", "hm", "dam", "m", "dm", "cm", "mm"], stap: "× 10", naam: "De maatladder voor lengte" },
  oppervlakte: { namen: ["km²", "hm²", "dam²", "m²", "dm²", "cm²", "mm²"], stap: "× 100", naam: "De maatladder voor oppervlakte" },
  volume: { namen: ["km³", "hm³", "dam³", "m³", "dm³", "cm³", "mm³"], stap: "× 1000", naam: "De maatladder voor volume" },
  massa: { namen: ["ton", "kg", "hg", "dag", "g", "dg", "cg", "mg"], stap: "× 10", naam: "De maatladder voor massa" },
};

function Ladder({ soort }: { soort: string }) {
  const l = LADDERS[soort] ?? LADDERS.lengte;
  const breed = 46;
  const hoog = 26;
  const stappen = l.namen.length;
  const b = stappen * breed + 60;
  return (
    <Blad breedte={b} hoogte={112} titel={l.naam}>
      {l.namen.map((naam, i) => (
        <g key={naam}>
          <rect
            x={n(30 + i * breed)}
            y={44}
            width={n(breed - 5)}
            height={hoog}
            rx={6}
            fill="var(--forest)"
            fillOpacity={i === Math.floor(stappen / 2) ? 0.18 : 0.06}
            stroke={LIJN}
            strokeWidth={1.6}
          />
          <Label x={n(30 + i * breed + (breed - 5) / 2)} y={57}>
            {naam}
          </Label>
        </g>
      ))}
      {/* Naar rechts is maal, naar links is gedeeld door. */}
      <Label x={n(b / 2)} y={22} kleur={MERK}>
        {`naar rechts ${l.stap}`}
      </Label>
      <Label x={n(b / 2)} y={96} kleur={MERK}>
        {`naar links : ${l.stap.replace("× ", "")}`}
      </Label>
    </Blad>
  );
}

// ---------------------------------------------------------------------------
// Samengestelde figuren

function Samengesteld({ soort, maten }: { soort: string; maten: number[] }) {
  if (soort === "halvecirkel") {
    const zijde = maten[0];
    const eenh = 20;
    const w = n(zijde * eenh);
    const r = n(w / 2);
    return (
      <Blad breedte={n(w + 130)} hoogte={n(w + r + 85)} titel={`Een vierkant van ${zijde} cm met daarop een halve cirkel`}>
        <path
          d={`M 45 ${n(30 + r)} A ${r} ${r} 0 0 1 ${n(45 + w)} ${n(30 + r)} L ${n(45 + w)} ${n(30 + r + w)} L 45 ${n(30 + r + w)} Z`}
          fill="var(--forest)"
          fillOpacity={0.08}
          stroke={LIJN}
          strokeWidth={2.4}
          strokeLinejoin="round"
        />
        <line x1={45} y1={n(30 + r)} x2={n(45 + w)} y2={n(30 + r)} stroke={MERK} strokeWidth={1.8} strokeDasharray="6 4" />
        <Maatlijn x1={45} y1={n(30 + r + w)} x2={n(45 + w)} y2={n(30 + r + w)} tekst={`${zijde} cm`} />
        <Maatlijn x1={n(45 + w)} y1={n(30 + r)} x2={n(45 + w)} y2={n(30 + r + w)} tekst={`${zijde} cm`} kant={-1} />
      </Blad>
    );
  }

  // hoekjes: uit een groot vierkant knip je in elke hoek een vierkantje
  const [groot, klein] = maten;
  const eenh = 16;
  const W = n(groot * eenh);
  const K = n(klein * eenh);
  return (
    <Blad breedte={n(W + 110)} hoogte={n(W + 85)} titel={`Een vierkant van ${groot} cm met in elke hoek een vierkantje van ${klein} cm weg`}>
      <rect x={45} y={25} width={W} height={W} fill="var(--forest)" fillOpacity={0.08} stroke={LIJN} strokeWidth={2.4} />
      {[
        [45, 25],
        [n(45 + W - K), 25],
        [45, n(25 + W - K)],
        [n(45 + W - K), n(25 + W - K)],
      ].map(([hx, hy], i) => (
        <rect key={i} x={hx} y={hy} width={K} height={K} fill="var(--surface)" stroke={MERK} strokeWidth={2} strokeDasharray="5 4" />
      ))}
      <Maatlijn x1={45} y1={n(25 + W)} x2={n(45 + W)} y2={n(25 + W)} tekst={`${groot} cm`} />
      <Label x={n(45 + K / 2)} y={n(25 + K + 16)} kleur={MERK}>
        {`${klein}`}
      </Label>
    </Blad>
  );
}

// ---------------------------------------------------------------------------
// De ene ingang die Figuren.tsx gebruikt

export const TEKENINGEN = [
  "hoek",
  "driehoek",
  "vierhoek",
  "snijlijn",
  "evenwijdig",
  "cirkeldeel",
  "merkwaardig",
  "assen",
  "beweging",
  "maat",
  "ruimte",
  "ladder",
  "samengesteld",
] as const;

export type TekeningNaam = (typeof TEKENINGEN)[number];

/** Zet "7x3" of "6-10x4" om in een lijst getallen. */
function getallen(s: string): number[] {
  return (s ?? "")
    .split(/[x×\-]/)
    .map((d) => Number(d.replace(",", ".")))
    .filter((d) => Number.isFinite(d));
}

export function Tekening({ naam, args }: { naam: string; args: string[] }) {
  switch (naam) {
    case "hoek": {
      const graden = Number(args[0]);
      if (!Number.isFinite(graden)) return null;
      return <Hoek graden={graden} opschrift={args[1] === "?" ? "?" : `${graden}°`} />;
    }
    case "driehoek": {
      // Ofwel een soort ("gelijkbenig"), ofwel drie hoeken ("50-60-?").
      if (args[0]?.includes("-")) return <DriehoekHoeken opschriften={args[0].split("-").slice(0, 3)} />;
      return <Driehoek soort={args[0]} />;
    }
    case "vierhoek":
      return <Vierhoek soort={args[0]} />;
    case "snijlijn": {
      const g = Number(args[0]);
      return Number.isFinite(g) ? <Snijlijn graden={g} neven={args[1] === "neven"} /> : null;
    }
    case "evenwijdig": {
      const g = Number(args[0]);
      return Number.isFinite(g) ? <Evenwijdig graden={g} binnen={args[1] === "binnen"} /> : null;
    }
    case "cirkeldeel":
      return <Cirkeldeel soort={args[0]} stil={args[1] === "stil"} />;
    case "merkwaardig":
      return <Merkwaardig soort={args[0]} stil={args[1] === "stil"} />;
    case "assen":
      return <Assen soort={args[0]} />;
    case "beweging":
      return <Beweging soort={args[0]} />;
    case "maat": {
      // {{maat rechthoek 7x3}} of {{maat cirkel straal 5}}
      if (args[0] === "cirkel") return <Maat soort={`cirkel-${args[1]}`} maten={getallen(args[2])} />;
      const m = getallen(args[1]);
      return m.length ? <Maat soort={args[0]} maten={m} /> : null;
    }
    case "ruimte": {
      const m = getallen(args[1]);
      return m.length ? <Ruimte soort={args[0]} maten={m} /> : null;
    }
    case "ladder":
      return <Ladder soort={args[0]} />;
    case "samengesteld": {
      const m = args.slice(1).flatMap(getallen);
      return m.length ? <Samengesteld soort={args[0]} maten={m} /> : null;
    }
    default:
      return null;
  }
}
