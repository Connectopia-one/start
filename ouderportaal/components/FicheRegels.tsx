import { type Kind, samen } from "@/lib/kind";

/*
  De inlichtingenfiche van één kind, om te lezen.

  Het teamscherm en het beheerscherm tonen allebei dezelfde fiche, dus staat ze
  hier één keer. Een veld dat leeg is, verschijnt niet: op een dag op een kamp
  wil je de drie dingen die écht ingevuld zijn meteen zien, niet een lijst van
  twintig regels waarvan er zeventien leeg zijn.

  De volgorde is die van dringendheid, niet die van het formulier. Medicatie en
  allergieën staan bovenaan, de school onderaan.
*/

function Regel({ kop, waarde }: { kop: string; waarde: string | null }) {
  if (!waarde) return null;
  return (
    <p className="mt-1">
      <strong className="text-ink">{kop}: </strong>
      <span className="text-ink-dim">{waarde}</span>
    </p>
  );
}

export function FicheRegels({ kind }: { kind: Kind }) {
  return (
    <>
      <Regel kop="Allergieën" waarde={kind.allergieen} />
      <Regel kop="Medicatie" waarde={kind.medicatie} />
      <Regel kop="Eten" waarde={kind.eten} />
      <Regel kop="Diagnoses" waarde={kind.diagnoses} />
      <Regel kop="Wat helpt" waarde={kind.wat_helpt} />
      <Regel
        kop="Noodcontact"
        waarde={samen(kind.noodcontact_naam, kind.noodcontact_telefoon) || null}
      />
      <Regel
        kop="Tweede noodcontact"
        waarde={
          samen(kind.noodcontact2_naam, kind.noodcontact2_telefoon) || null
        }
      />
      <Regel
        kop="Huisarts"
        waarde={samen(kind.huisarts_naam, kind.huisarts_telefoon) || null}
      />
      <Regel kop="Mag ophalen" waarde={kind.ophalen} />
      {kind.alleen_naar_huis && (
        <p className="mt-1 text-ink-dim">Mag alleen naar huis.</p>
      )}
      <Regel kop="School" waarde={samen(kind.school, kind.leerjaar) || null} />
    </>
  );
}
