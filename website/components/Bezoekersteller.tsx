"use client";

import { Analytics } from "@vercel/analytics/next";

/*
  De bezoekersteller van Vercel, waar de site toch al draait.

  Wat hij doorgeeft: welke pagina bekeken werd, wanneer, via welke link iemand
  binnenkwam, uit welk land, en op welk soort toestel en browser. Meer niet.
  Er komt geen cookie aan te pas en er wordt geen IP-adres bewaard, dus er is
  ook geen cookiebanner voor nodig.

  Wat hij niet doorgeeft: alles wat achter het vraagteken in een webadres
  staat. Daar kan namen of een mailadres in belanden zodra een formulier ooit
  iets in de link meegeeft, en dat gaat niemand anders aan. We knippen het er
  hier af voor het vertrekt, en niet pas aan de andere kant.

  Tellen begint pas als de teller in het Vercel-scherm van het project
  aangezet is; tot dan gaat er niets weg.
*/
export function Bezoekersteller() {
  return (
    <Analytics
      beforeSend={(gebeurtenis) => {
        const zonderVraagteken = gebeurtenis.url.split("?")[0].split("#")[0];
        return { ...gebeurtenis, url: zonderVraagteken };
      }}
    />
  );
}
