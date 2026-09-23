import { site } from "@/content/site";

/* Het logo: de C van verbonden puntjes, met de naam ernaast. */
export function Logo() {
  const punten = [
    [23.8, 8.2],
    [17.9, 5.2],
    [11.4, 6],
    [6.5, 10.5],
    [5, 17],
    [7.6, 23.1],
    [13.2, 26.6],
    [19.8, 26.3],
    [23.8, 23.8],
  ];

  return (
    <span className="flex items-center gap-2.5 text-ink">
      <svg
        viewBox="0 0 32 32"
        aria-hidden
        className="h-8 w-8 shrink-0"
        fill="none"
      >
        <polyline
          points={punten.map(([x, y]) => `${x},${y}`).join(" ")}
          stroke="currentColor"
          strokeWidth="1.4"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <g fill="currentColor">
          {punten.map(([x, y]) => (
            <circle key={`${x}-${y}`} cx={x} cy={y} r="2" />
          ))}
        </g>
      </svg>
      <span className="text-[20px] font-extrabold tracking-tight">
        {site.naam}
      </span>
      <span className="text-[12px] font-extrabold tracking-[0.08em] text-ink-dim uppercase">
        {site.vzw}
      </span>
    </span>
  );
}
