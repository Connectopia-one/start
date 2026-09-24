"use client";

import { Analytics } from "@vercel/analytics/next";
import { zonderPersoonlijkeStukken } from "@/lib/bezoekadres";

/*
  De bezoekersteller van Vercel, waar het platform toch al draait. Het scherm
  staat in Vercel bij dit project, onder Analytics.

  Hij telt paginaweergaves: welke hoofdstukken het meest geopend worden, hoe
  druk het platform is, en op welk soort toestel de kinderen oefenen. Geen
  cookie, geen IP-adres, en niets over wie een kind is of hoe het scoorde — dat
  staat allemaal in je eigen databank en blijft daar. De kindnummers die in
  sommige webadressen staan, gaan er eerst uit; zie lib/bezoekadres.ts.

  Tellen begint pas als de teller in het Vercel-scherm aangezet is; tot dan
  gaat er niets weg.
*/
export function Bezoekersteller() {
  return (
    <Analytics
      beforeSend={(gebeurtenis) => ({
        ...gebeurtenis,
        url: zonderPersoonlijkeStukken(gebeurtenis.url),
      })}
    />
  );
}
