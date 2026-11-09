import { redirect } from "next/navigation";

/*
  "Handig materiaal" staat sinds 9 november 2026 onder de Leuke extra's: de
  links op /extras/links, de documenten op /extras/documenten en de filmpjes
  op /extras/filmpjes. Wie het oude adres nog heeft, komt op /extras terecht.
*/
export default function MateriaalPage() {
  redirect("/extras");
}
