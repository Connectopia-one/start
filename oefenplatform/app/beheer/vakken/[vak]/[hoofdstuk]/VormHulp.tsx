/**
 * Hoe je een tabel of een keuzelijst intikt, in het formulier zelf. Die twee
 * vormen (zie lib/vraagvorm.ts) lezen hun velden anders dan de andere types,
 * en dat moet je kunnen zien zonder het ergens op te zoeken.
 */
export function VormHulp() {
  return (
    <details className="rounded-md border border-border bg-paper px-3 py-2 text-xs text-ink-dim">
      <summary className="cursor-pointer text-ink">Hoe tik je een tabel of een keuzelijst in?</summary>
      <p className="mt-2">
        <span className="font-medium text-ink">Tabel, per rij juist of fout.</span> Bij Vraag de opdracht, bijvoorbeeld
        &ldquo;Zijn deze uitspraken over de Romeinen juist of fout?&rdquo;. Bij Opties elke uitspraak op een eigen
        regel. Bij Antwoord per rij het juiste woord, met een komma ertussen: juist, fout, juist. Wil je andere
        kolommen, zet ze dan vooraan met een dubbelpunt erachter: Ja | Nee | Soms: ja, soms, nee.
      </p>
      <p className="mt-2">
        <span className="font-medium text-ink">Keuzelijst in een zin.</span> Zet elke keuzelijst tussen dubbele
        haken, de opties gescheiden door een verticale streep, met een sterretje voor het juiste woord: De raaklijn
        is een [[*stijgende|dalende|horizontale]] rechte. Er mogen meerdere keuzelijsten in één zin staan. Antwoord
        en Opties laat je leeg. In een keuzelijst kan geen formule staan, enkel gewone tekst.
      </p>
      <p className="mt-2">Bij allebei krijgt een kind alleen punten als alles juist is, net als op het examen.</p>
    </details>
  );
}
