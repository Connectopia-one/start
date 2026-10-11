import { zetAanwezig } from "@/app/beheer/activiteiten/actions";

/*
  De twee knopjes waarmee een begeleider aanduidt of een kind er was.

  Ze staan op twee schermen: bij de activiteit in het beheer, en op
  /team/aanwezigheden voor de begeleiders. Daarom één component, zodat de
  betekenis van de knopjes niet op de ene plek anders wordt dan op de andere.

  Niets aangeduid is een echte derde stand, niet hetzelfde als aanwezig: op de
  factuur telt die mee, maar het overzicht zegt er wel bij hoeveel er nog open
  staan. Klik je op de knop die al aan staat, dan gaat ze weer uit; zo kan je
  een vergissing terugnemen zonder een derde knopje.
*/
export function Aanwezigheid({
  activiteitId,
  kindId,
  waarde,
  terug,
}: {
  activiteitId: string;
  kindId: string;
  waarde: boolean | null;
  terug: string;
}) {
  return (
    <div className="flex gap-1.5 print:hidden">
      <Knop
        activiteitId={activiteitId}
        kindId={kindId}
        terug={terug}
        naar={waarde === true ? "" : "ja"}
        label="Was er"
        aan={waarde === true}
        kleur="forest"
      />
      <Knop
        activiteitId={activiteitId}
        kindId={kindId}
        terug={terug}
        naar={waarde === false ? "" : "nee"}
        label="Afwezig"
        aan={waarde === false}
        kleur="danger"
      />
    </div>
  );
}

function Knop({
  activiteitId,
  kindId,
  terug,
  naar,
  label,
  aan,
  kleur,
}: {
  activiteitId: string;
  kindId: string;
  terug: string;
  naar: string;
  label: string;
  aan: boolean;
  kleur: "forest" | "danger";
}) {
  const stijl = aan
    ? kleur === "forest"
      ? "bg-forest text-white"
      : "bg-danger text-white"
    : "border border-border text-ink-dim hover:border-forest hover:text-forest-dark";

  return (
    <form action={zetAanwezig}>
      <input type="hidden" name="activiteit_id" value={activiteitId} />
      <input type="hidden" name="kind_id" value={kindId} />
      <input type="hidden" name="waarde" value={naar} />
      <input type="hidden" name="terug" value={terug} />
      <button
        type="submit"
        className={`rounded-md px-2.5 py-1 text-xs font-medium transition ${stijl}`}
      >
        {label}
      </button>
    </form>
  );
}

/* Het regeltje dat zegt hoe ver het aanduiden staat. Een lijst waar niets is
   aangeduid ziet er anders precies hetzelfde uit als een volle lijst. */
export function AanwezigheidStand({
  aanwezigen,
  nietAangeduid,
}: {
  aanwezigen: number;
  nietAangeduid: number;
}) {
  if (nietAangeduid === 0) {
    return (
      <span>
        {aanwezigen} {aanwezigen === 1 ? "kind was" : "kinderen waren"} er
      </span>
    );
  }
  return (
    <span>
      {nietAangeduid} nog niet aangeduid
      {aanwezigen > nietAangeduid && ` van de ${aanwezigen}`}
    </span>
  );
}
