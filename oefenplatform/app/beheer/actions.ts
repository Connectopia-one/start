"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { slugify } from "@/lib/slug";
import { NIVEAUS, vindNiveau, heeftProefhoofdstuk } from "@/lib/niveaus";
import { volgendVolgnummer, vrijeVolgnummers } from "@/lib/volgnummer";

/**
 * Waar een knop van de vakkenpagina naar terugkeert.
 *
 * Die pagina toont sinds 29 september 2026 één categorie van één vak tegelijk
 * in plaats van alles onder elkaar. "Terug naar /beheer/vakken" zou je dan
 * telkens weer helemaal vooraan zetten, dus elk formulier stuurt in
 * "terug_niveau" en "terug_vak" mee waar het stond.
 */
function vakkenPagina(formData: FormData, sleutel?: string, waarde?: string) {
  const params = new URLSearchParams();
  const niveau = String(formData.get("terug_niveau") || "").trim();
  const vak = String(formData.get("terug_vak") || "").trim();
  if (niveau) params.set("niveau", niveau);
  if (vak) params.set("vak", vak);
  if (sleutel && waarde !== undefined) params.set(sleutel, waarde);
  const vraag = params.toString();
  return "/beheer/vakken" + (vraag ? "?" + vraag : "");
}

/**
 * Een nieuw vak aanmaken.
 *
 * Het formulier staat bij de vakken van een categorie, dus zetten we je daarna
 * meteen in dat nieuwe vak: anders valt het terug in het klapje "vakken zonder
 * hoofdstukken in deze categorie" en moet je het gaan zoeken.
 */
export async function maakVak(formData: FormData) {
  await requireBeheerder();
  const naam = String(formData.get("naam") || "").trim();
  const rekenmachine = formData.get("rekenmachine") === "on";
  if (!naam)
    redirect(vakkenPagina(formData, "fout", "Geef een naam op voor het vak."));

  const admin = createAdminClient();
  const { count } = await admin
    .from("vakken")
    .select("id", { count: "exact", head: true });
  const { data: nieuw, error } = await admin
    .from("vakken")
    .insert({ naam, slug: slugify(naam), volgorde: count ?? 0, rekenmachine })
    .select("slug")
    .maybeSingle();
  if (error || !nieuw)
    redirect(
      vakkenPagina(
        formData,
        "fout",
        "Kon het vak niet aanmaken. Bestaat er al een vak met die naam?",
      ),
    );

  formData.set("terug_vak", nieuw.slug);
  revalidatePath("/beheer/vakken");
  revalidatePath("/");
  redirect(vakkenPagina(formData, "melding", `${naam} staat er.`));
}

/**
 * De naam van een vak aanpassen, bijvoorbeeld na een typfout.
 *
 * De slug staat in het webadres van het vak. Die passen we mee aan zolang ze
 * nog de automatische vorm van de oude naam is — dan is het adres immers ook
 * fout getypt. Koos je de slug ooit zelf anders, dan blijft het adres staan,
 * zodat bestaande links blijven werken.
 */
export async function hernoemVak(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const naam = String(formData.get("naam") || "").trim();
  if (!id) redirect(vakkenPagina(formData));
  if (!naam)
    redirect(vakkenPagina(formData, "fout", "Geef een naam op voor het vak."));

  const admin = createAdminClient();
  const { data: vak } = await admin
    .from("vakken")
    .select("naam, slug")
    .eq("id", id)
    .maybeSingle();
  if (!vak)
    redirect(vakkenPagina(formData, "fout", "Dit vak bestaat niet meer."));

  const nieuweSlug = slugify(naam);
  const slugVolgdeDeNaam = vak.slug === slugify(vak.naam);
  const wijziging: { naam: string; slug?: string } = { naam };
  if (slugVolgdeDeNaam && nieuweSlug && nieuweSlug !== vak.slug) {
    wijziging.slug = nieuweSlug;
  }

  const { error } = await admin.from("vakken").update(wijziging).eq("id", id);
  if (error) {
    redirect(
      vakkenPagina(
        formData,
        "fout",
        "Kon de naam niet aanpassen. Bestaat er al een vak met die naam?",
      ),
    );
  }

  revalidatePath("/beheer/vakken");
  revalidatePath("/");
  redirect(vakkenPagina(formData));
}

/**
 * De titel van een hoofdstuk aanpassen, bijvoorbeeld na een typfout.
 *
 * Anders dan bij een vak zit hier geen slug aan vast: een hoofdstuk staat in
 * het webadres als zijn volgnummer. Een nieuwe titel breekt dus geen links.
 *
 * Let wel: de bulk-import zoekt een hoofdstuk op zijn categorie en zijn titel.
 * Hernoem je er een, dan moet een JSON-bestand dat je daarna importeert de
 * nieuwe titel gebruiken, anders wordt het oude hoofdstuk opnieuw aangemaakt.
 */
export async function hernoemHoofdstuk(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const titel = String(formData.get("titel") || "").trim();
  if (!id) redirect(vakkenPagina(formData));
  if (!titel) {
    redirect(
      vakkenPagina(formData, "fout", "Geef een titel op voor het hoofdstuk."),
    );
  }

  const admin = createAdminClient();
  const { error } = await admin
    .from("hoofdstukken")
    .update({ titel })
    .eq("id", id);
  if (error) {
    redirect(
      vakkenPagina(
        formData,
        "fout",
        "Kon de titel van het hoofdstuk niet aanpassen.",
      ),
    );
  }

  revalidatePath("/beheer/vakken");
  revalidatePath("/");
  redirect(vakkenPagina(formData));
}

export async function wisselRekenmachine(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const rekenmachine = formData.get("rekenmachine") === "true";
  const admin = createAdminClient();
  await admin
    .from("vakken")
    .update({ rekenmachine: !rekenmachine })
    .eq("id", id);
  revalidatePath("/beheer/vakken");
  redirect(vakkenPagina(formData));
}

export async function verwijderVak(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const admin = createAdminClient();
  await admin.from("vakken").delete().eq("id", id);
  revalidatePath("/beheer/vakken");
  // Niet terug naar het vak zelf: dat bestaat nu niet meer. Wel naar de
  // categorie waar je stond, zodat je de andere vakken weer voor je hebt.
  formData.delete("terug_vak");
  redirect(vakkenPagina(formData));
}

export async function maakHoofdstuk(formData: FormData) {
  await requireBeheerder();
  const vakId = String(formData.get("vak_id") || "");
  const titel = String(formData.get("titel") || "").trim();
  const gratis = formData.get("gratis") === "on";
  const niveau = String(formData.get("niveau") || "start");
  if (!vakId || !titel)
    redirect(
      vakkenPagina(formData, "fout", "Geef een titel op voor het hoofdstuk."),
    );
  if (!NIVEAUS.some((n) => n.slug === niveau))
    redirect(vakkenPagina(formData, "fout", "Ongeldige categorie."));

  const admin = createAdminClient();

  const { error } = await admin.from("hoofdstukken").insert({
    vak_id: vakId,
    titel,
    volgnummer: await volgendVolgnummer(admin, "hoofdstukken", "vak_id", vakId),
    gratis: gratis || (await isEersteVanNiveau(admin, vakId, niveau)),
    niveau,
  });
  if (error) {
    redirect(
      vakkenPagina(
        formData,
        "fout",
        `Hoofdstuk "${titel}" aanmaken mislukt: ${error.message}`,
      ),
    );
  }

  revalidatePath("/beheer/vakken");
  redirect(vakkenPagina(formData));
}

/** Het eerste hoofdstuk van elke categorie (niveau) binnen een vak is altijd
 * gratis om uit te proberen — zo geeft elk vak een gratis staaltje op elk
 * niveau, niet enkel op het allereerste (start-)niveau. */
async function isEersteVanNiveau(
  admin: ReturnType<typeof createAdminClient>,
  vakId: string,
  niveau: string,
): Promise<boolean> {
  const { count } = await admin
    .from("hoofdstukken")
    .select("id", { count: "exact", head: true })
    .eq("vak_id", vakId)
    .eq("niveau", niveau);
  return (count ?? 0) === 0;
}

export async function wisselGratis(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const gratis = formData.get("gratis") === "true";
  const admin = createAdminClient();
  const { error } = await admin
    .from("hoofdstukken")
    .update({ gratis: !gratis })
    .eq("id", id);
  if (error) {
    redirect(
      vakkenPagina(
        formData,
        "fout",
        `Het hoofdstuk omzetten lukte niet: ${error.message}`,
      ),
    );
  }
  revalidatePath("/beheer/vakken");
  redirect(vakkenPagina(formData));
}

/*
  Een heel niveau van een vak in één keer gratis zetten of weer op slot.

  Kim vroeg op 25 september 2026 om 🧱 Basis van wiskunde helemaal open te
  zetten. Dat zijn veertien hoofdstukken, en die één voor één aanklikken is
  vragen om er eentje te vergeten.
*/
export async function zetNiveauGratis(formData: FormData) {
  await requireBeheerder();
  const vakId = String(formData.get("vak_id") || "");
  const niveau = String(formData.get("niveau") || "");
  const gratis = formData.get("gratis") === "ja";
  if (!vakId || !niveau) redirect(vakkenPagina(formData));
  const admin = createAdminClient();
  const { data, error } = await admin
    .from("hoofdstukken")
    .update({ gratis })
    .eq("vak_id", vakId)
    .eq("niveau", niveau)
    .select("id");
  if (error) {
    redirect(
      vakkenPagina(
        formData,
        "fout",
        `Het niveau omzetten lukte niet: ${error.message}`,
      ),
    );
  }
  // Zeg hoeveel hoofdstukken mee zijn. Zonder die bevestiging is het na het
  // klikken niet te zien of er iets gebeurd is.
  const aantal = data?.length ?? 0;
  const naam = vindNiveau(niveau)?.naam ?? niveau;
  revalidatePath("/beheer/vakken");
  redirect(
    vakkenPagina(
      formData,
      "melding",
      `${aantal} ${aantal === 1 ? "hoofdstuk" : "hoofdstukken"} van ${naam} ${
        aantal === 1 ? "staat" : "staan"
      } nu ${gratis ? "gratis" : "op slot"}.`,
    ),
  );
}

/*
  Overal een gratis proefhoofdstuk openzetten.

  Kim op 29 september 2026: "bij spark nederlands staat er geen enkel hoofdstuk
  gratis ... want zo kunnen mensen buitenaf niet testen."

  De bedoeling was altijd al dat het eerste hoofdstuk van elke categorie binnen
  een vak gratis openstaat (zie isEersteVanNiveau hierboven), maar dat geldt
  enkel voor een hoofdstuk op het moment dat het aangemaakt wordt. Wie daarna
  hoofdstukken hernoemt, verhuist, verwijdert of met de hand op slot zet, kan
  een vak zonder enkel open hoofdstuk overhouden. Dan ziet een bezoeker zonder
  account daar niets.

  Deze knop loopt alle vakken af en zet in elke categorie waar niets openstaat
  het eerste hoofdstuk gratis. Ze raakt nooit iets aan dat al gratis is en zet
  nooit iets op slot. 🔭 De uitdagingshoek blijft buiten schot: Kim wou die
  uitdrukkelijk achter een account.
*/
export async function herstelProefhoofdstukken(formData: FormData) {
  await requireBeheerder();
  const admin = createAdminClient();
  const { data, error } = await admin
    .from("hoofdstukken")
    .select("id, vak_id, niveau, volgnummer, gratis");
  if (error) {
    redirect(
      vakkenPagina(
        formData,
        "fout",
        `De hoofdstukken ophalen lukte niet: ${error.message}`,
      ),
    );
  }

  // Per vak en categorie: staat er al iets open, en wat is anders het eerste?
  const eerste = new Map<string, { id: string; volgnummer: number }>();
  const alOpen = new Set<string>();
  for (const h of data ?? []) {
    if (!heeftProefhoofdstuk(h.niveau)) continue;
    const sleutel = `${h.vak_id}|${h.niveau}`;
    if (h.gratis) {
      alOpen.add(sleutel);
      continue;
    }
    const staand = eerste.get(sleutel);
    if (!staand || h.volgnummer < staand.volgnummer) {
      eerste.set(sleutel, { id: h.id, volgnummer: h.volgnummer });
    }
  }

  const openTeZetten = [...eerste.entries()]
    .filter(([sleutel]) => !alOpen.has(sleutel))
    .map(([, h]) => h.id);

  if (openTeZetten.length === 0) {
    redirect(
      vakkenPagina(
        formData,
        "melding",
        "Overal staat al een hoofdstuk gratis. Er was niets te doen.",
      ),
    );
  }

  const { error: zetFout } = await admin
    .from("hoofdstukken")
    .update({ gratis: true })
    .in("id", openTeZetten);
  if (zetFout) {
    redirect(
      vakkenPagina(
        formData,
        "fout",
        `Het openzetten lukte niet: ${zetFout.message}`,
      ),
    );
  }

  revalidatePath("/beheer/vakken");
  revalidatePath("/niveaus");
  const n = openTeZetten.length;
  redirect(
    vakkenPagina(
      formData,
      "melding",
      `${n} ${n === 1 ? "hoofdstuk staat" : "hoofdstukken staan"} nu gratis: ` +
        `in elk vak en elke categorie waar niets openstond, is het eerste ` +
        `hoofdstuk opengezet.`,
    ),
  );
}

export async function verwijderHoofdstuk(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const admin = createAdminClient();
  await admin.from("hoofdstukken").delete().eq("id", id);
  revalidatePath("/beheer/vakken");
  redirect(vakkenPagina(formData));
}

type BulkVraag = {
  type: "meerkeuze" | "invultekst" | "waarofniet";
  vraag: string;
  opties?: string[] | null;
  /**
   * Bij meerkeuze het nummer van de juiste optie, of een lijstje nummers als
   * er meer dan één juist is (zie lib/antwoord.ts). Bij waarofniet true of
   * false, bij invultekst de tekst.
   */
  antwoord: number | string | boolean | number[] | string[];
  uitleg?: string | null;
  /**
   * Wisselende woorden, enkel bij spelling: een lijstje met per beurt de velden
   * die anders zijn dan hierboven. Zie lib/spellingvariant.ts.
   */
  varianten?:
    | {
        vraag?: string;
        opties?: string[] | null;
        antwoord?: number | string | boolean | number[] | string[];
        uitleg?: string | null;
      }[]
    | null;
};

/**
 * De twee velden voor begrijpend lezen uit een importbestand, alleen als ze
 * er echt in staan. Zo laat een bestand zonder leestekst een bestaande tekst
 * met rust, en wist `"leestekst": ""` hem wel.
 */
function leesVelden(hfst: BulkHoofdstuk) {
  const velden: { leestekst?: string | null; woordenlijst?: unknown } = {};
  if (hfst.leestekst !== undefined) {
    const tekst = String(hfst.leestekst ?? "").trim();
    velden.leestekst = tekst || null;
  }
  if (hfst.woordenlijst !== undefined) {
    const lijst = Array.isArray(hfst.woordenlijst)
      ? hfst.woordenlijst
          .map((w) => ({
            woord: String(w?.woord ?? "").trim(),
            uitleg: String(w?.uitleg ?? "").trim(),
          }))
          .filter((w) => w.woord && w.uitleg)
      : [];
    velden.woordenlijst = lijst.length ? lijst : null;
  }
  return velden;
}

type BulkHoofdstuk = {
  titel: string;
  /**
   * De titel die dit hoofdstuk nú in de databank heeft, als die verschilt van
   * `titel`. Staat die er, dan wordt het bestaande hoofdstuk hernoemd in plaats
   * van dat er een tweede naast komt. Zo kan je een hoofdstuk opsplitsen in een
   * deel 1 en een deel 2 zonder de leerbundel, de stickers of de voortgang van
   * de kinderen kwijt te spelen, en zonder alles met de hand te hernoemen.
   */
  hernoemVan?: string;
  niveau?: string;
  /**
   * De categorie waarin dit hoofdstuk nú staat, als die verschilt van
   * `niveau`. Staat die er, dan wordt het bestaande hoofdstuk verhuisd in
   * plaats van dat er een tweede naast komt. Alleen nodig om een hoofdstuk
   * dat ooit in de verkeerde categorie belandde recht te zetten; een gewoon
   * bestand laat dit weg.
   */
  stondIn?: string;
  /**
   * Begrijpend lezen: de tekst die boven de vragen blijft staan. Een lege
   * regel begint een nieuwe alinea, een woord tussen sterretjes krijgt de
   * uitleg uit de woordenlijst.
   */
  leestekst?: string | null;
  woordenlijst?: { woord: string; uitleg: string }[] | null;
  gratis?: boolean;
  vragen: BulkVraag[];
};

/**
 * Twee titels vergelijken zonder te struikelen over een streepje of een spatie
 * te veel. Een titel die je uit een bestand kopieert, heeft soms een lang
 * streepje (—) waar in de databank een kort streepje (-) staat, of een dubbele
 * spatie. Zonder deze opkuis ziet de import zo'n titel als nieuw en maakt ze
 * het hoofdstuk een tweede keer aan.
 */
function titelSleutel(titel: string) {
  return titel
    .replace(/[\u2010-\u2015]/g, "-")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}

/**
 * De sleutel waarmee de import een hoofdstuk terugvindt: de categorie én de
 * titel, want een titel hoeft binnen een vak niet uniek te zijn.
 *
 * Ontdekt op 29 september 2026. "Uitdaging - alles door elkaar" bestaat bij
 * wiskunde, Nederlands en geschiedenis zowel bij Start als bij Spark. Op de
 * titel alleen vond de import van het Spark-bestand het Start-hoofdstuk terug,
 * verhuisde dat naar Spark en zette er de Spark-vragen in. Zo bleef er van de
 * twee hoofdstukken maar een over.
 */
function hoofdstukSleutel(niveau: string, titel: string) {
  return niveau + "\u0000" + titelSleutel(titel);
}

/**
 * Importeert in één keer meerdere hoofdstukken (met hun vragen) voor een vak.
 * Een hoofdstuk met een titel die al bestaat binnen dit vak krijgt de nieuwe
 * vragen erbij toegevoegd; een onbekende titel wordt als nieuw hoofdstuk
 * aangemaakt, op het eerste volgnummer dat nog vrij is. Verwijderde je net een
 * hoofdstuk, dan komt het nieuwe dus op die vrijgekomen plek te staan; anders
 * achteraan de lijst.
 *
 * Staat "vervang" aan, dan gaan de vragen die al bij zo'n hoofdstuk stonden
 * eerst weg en blijven alleen die uit dit bestand over. Zo kan je een
 * verouderd hoofdstuk bijwerken zonder het eerst te verwijderen — het houdt
 * dan ook zijn plek, zijn webadres, zijn leerbundel en de voortgang die de
 * kinderen er al op hebben.
 */
export async function bulkImportVakInhoud(formData: FormData) {
  await requireBeheerder();
  const vakId = String(formData.get("vak_id") || "");
  const json = String(formData.get("json") || "").trim();
  const vervang = formData.get("vervang") === "on";
  if (!vakId) redirect(vakkenPagina(formData, "fout", "Onbekend vak."));

  let payload: { hoofdstukken: BulkHoofdstuk[] };
  try {
    payload = JSON.parse(json);
    if (!payload || !Array.isArray(payload.hoofdstukken)) {
      throw new Error('Verwacht een object met een "hoofdstukken"-lijst.');
    }
  } catch (e) {
    redirect(
      vakkenPagina(
        formData,
        "fout",
        "Ongeldige JSON: " +
          (e instanceof Error ? e.message : "onbekende fout"),
      ),
    );
  }

  const admin = createAdminClient();

  const { data: bestaande } = await admin
    .from("hoofdstukken")
    .select("id, titel, niveau, gratis")
    .eq("vak_id", vakId);

  const neemVolgnummer = await vrijeVolgnummers(
    admin,
    "hoofdstukken",
    "vak_id",
    vakId,
  );
  const hoofdstukNaarId = new Map<string, string>();
  const gratisVanId = new Map<string, boolean>();
  (bestaande ?? []).forEach((h) => {
    hoofdstukNaarId.set(hoofdstukSleutel(h.niveau, h.titel), h.id);
    gratisVanId.set(h.id, !!h.gratis);
  });
  // Het eerste hoofdstuk van elke categorie (niveau) binnen dit vak is altijd
  // gratis om uit te proberen — zowel al bestaande als in deze import zelf.
  const niveausMetHoofdstuk = new Set<string>(
    (bestaande ?? []).map((h) => h.niveau),
  );

  for (const hfst of payload!.hoofdstukken) {
    const titel = String(hfst.titel || "").trim();
    if (!titel) continue;
    // Een categorie die we niet kennen is een fout in het bestand, geen reden
    // om er stilletjes "start" van te maken. Dat laatste deed dit vroeger, en
    // dan belandde een hoofdstuk zonder één waarschuwing onder 🌱 Start.
    const niveau = String(hfst.niveau || "start");
    if (!NIVEAUS.some((n) => n.slug === niveau)) {
      redirect(
        vakkenPagina(
          formData,
          "fout",
          `"${titel}" draagt de onbekende categorie "${niveau}". Er is niets ingelezen.`,
        ),
      );
    }

    let hoofdstukId = hoofdstukNaarId.get(hoofdstukSleutel(niveau, titel));

    // Staat het hoofdstuk nog onder zijn oude naam in de databank, hernoem het
    // dan eerst. Bestaat de nieuwe titel al, dan is dit blijkbaar een tweede
    // import en laten we alles ongemoeid.
    const oudeTitel = String(hfst.hernoemVan || "").trim();
    if (!hoofdstukId && oudeTitel) {
      const oudeSleutel = hoofdstukSleutel(niveau, oudeTitel);
      const teHernoemen = hoofdstukNaarId.get(oudeSleutel);
      if (teHernoemen) {
        const { error: hernoemFout } = await admin
          .from("hoofdstukken")
          .update({ titel })
          .eq("id", teHernoemen);
        if (hernoemFout) {
          redirect(
            vakkenPagina(
              formData,
              "fout",
              `"${oudeTitel}" hernoemen naar "${titel}" mislukt: ${hernoemFout.message}`,
            ),
          );
        }
        hoofdstukNaarId.delete(oudeSleutel);
        hoofdstukNaarId.set(hoofdstukSleutel(niveau, titel), teHernoemen);
        hoofdstukId = teHernoemen;
      }
    }

    // Staat het hoofdstuk in een andere categorie dan waar het hoort, en zegt
    // het bestand uitdrukkelijk in welke, verhuis het dan. Dit gebeurt nooit
    // vanzelf: een hoofdstuk met dezelfde titel in een andere categorie is
    // meestal een ander hoofdstuk (zie hoofdstukSleutel).
    const oudNiveau = String(hfst.stondIn || "").trim();
    if (oudNiveau && !NIVEAUS.some((n) => n.slug === oudNiveau)) {
      redirect(
        vakkenPagina(
          formData,
          "fout",
          `"${titel}" zegt te verhuizen uit de onbekende categorie "${oudNiveau}". Er is niets ingelezen.`,
        ),
      );
    }
    if (!hoofdstukId && oudNiveau && oudNiveau !== niveau) {
      const vanSleutel = hoofdstukSleutel(oudNiveau, titel);
      const teVerhuizen = hoofdstukNaarId.get(vanSleutel);
      if (teVerhuizen) {
        const { error: verhuisFout } = await admin
          .from("hoofdstukken")
          .update({ niveau })
          .eq("id", teVerhuizen);
        if (verhuisFout) {
          redirect(
            vakkenPagina(
              formData,
              "fout",
              `"${titel}" naar de juiste categorie verplaatsen mislukt: ${verhuisFout.message}`,
            ),
          );
        }
        hoofdstukNaarId.delete(vanSleutel);
        hoofdstukNaarId.set(hoofdstukSleutel(niveau, titel), teVerhuizen);
        hoofdstukId = teVerhuizen;
      }
    }

    const bestondAl = !!hoofdstukId;
    const bestaandGratis = bestondAl
      ? (gratisVanId.get(hoofdstukId!) ?? false)
      : false;

    if (!hoofdstukId) {
      const eersteVanNiveau =
        heeftProefhoofdstuk(niveau) && !niveausMetHoofdstuk.has(niveau);
      niveausMetHoofdstuk.add(niveau);
      const rij = {
        vak_id: vakId,
        titel,
        gratis: !!hfst.gratis || eersteVanNiveau,
        niveau,
        ...leesVelden(hfst),
      };
      let { data: nieuw, error: hoofdstukFout } = await admin
        .from("hoofdstukken")
        .insert({ ...rij, volgnummer: neemVolgnummer() })
        .select("id")
        .single();
      // Botst het nummer toch nog (bijvoorbeeld omdat iemand anders tegelijk
      // iets toevoegde), kijk dan opnieuw welke nummers vrij zijn en probeer
      // het nog één keer.
      if (hoofdstukFout?.code === "23505") {
        const opnieuw = await vrijeVolgnummers(
          admin,
          "hoofdstukken",
          "vak_id",
          vakId,
        );
        ({ data: nieuw, error: hoofdstukFout } = await admin
          .from("hoofdstukken")
          .insert({ ...rij, volgnummer: opnieuw() })
          .select("id")
          .single());
      }
      if (hoofdstukFout || !nieuw) {
        redirect(
          vakkenPagina(
            formData,
            "fout",
            `Hoofdstuk "${titel}" aanmaken mislukt: ${hoofdstukFout?.message ?? "onbekende fout"}`,
          ),
        );
      }
      hoofdstukId = nieuw!.id as string;
      hoofdstukNaarId.set(hoofdstukSleutel(niveau, titel), hoofdstukId);
    }

    // Zegt het bestand uitdrukkelijk dat dit hoofdstuk gratis is, zet het dan
    // ook open als het er al stond. Zo kan het gratis proefhoofdstuk achteraf
    // nog verlegd worden naar een ander hoofdstuk.
    //
    // Omgekeerd niet: een import zet nooit iets op slot dat met de hand open
    // gezet is. Bijna elk bestand draagt "gratis": false mee, dus anders ging
    // een hoofdstuk dat in Beheer gratis gezet was weer dicht bij de volgende
    // import van datzelfde bestand. Op slot zetten gebeurt met de knop.
    if (bestondAl && hfst.gratis === true && !bestaandGratis) {
      const { error: gratisFout } = await admin
        .from("hoofdstukken")
        .update({ gratis: true })
        .eq("id", hoofdstukId);
      if (gratisFout) {
        redirect(
          vakkenPagina(
            formData,
            "fout",
            `"${titel}" op gratis zetten mislukt: ${gratisFout.message}`,
          ),
        );
      }
    }

    // Draagt het bestand een leestekst mee, zet die dan ook op een hoofdstuk
    // dat er al stond. Zo kan een tekst bijgewerkt worden met een nieuwe
    // import, zonder het hoofdstuk weg te gooien.
    const lees = leesVelden(hfst);
    if (bestondAl && Object.keys(lees).length > 0) {
      const { error: leesFout } = await admin
        .from("hoofdstukken")
        .update(lees)
        .eq("id", hoofdstukId);
      if (leesFout) {
        redirect(
          vakkenPagina(
            formData,
            "fout",
            `De leestekst van "${titel}" bewaren mislukt: ${leesFout.message}`,
          ),
        );
      }
    }

    const vragen = Array.isArray(hfst.vragen) ? hfst.vragen : [];
    if (!vragen.length) continue;

    // Bij "vervangen" gaan de oude vragen van dit hoofdstuk eerst weg, zodat je
    // een bijgewerkt bestand kan importeren zonder alles dubbel te krijgen.
    //
    // De voortgang van de kinderen overleeft dat sinds 27 september 2026: in
    // "voortgang" staat het hoofdstuk apart naast de vraag, en de band met de
    // vraag is "on delete set null" in plaats van "cascade". Daarvoor wiste
    // deze regel stilletjes ook elk antwoord dat aan zo'n vraag hing. Zet die
    // band dus nooit terug op cascade; zie supabase/voortgang-blijft.sql.
    if (vervang) {
      const { error: wisFout } = await admin
        .from("vragen")
        .delete()
        .eq("hoofdstuk_id", hoofdstukId);
      if (wisFout) {
        redirect(
          vakkenPagina(
            formData,
            "fout",
            `Oude vragen van "${titel}" verwijderen mislukt: ${wisFout.message}`,
          ),
        );
      }
    }

    const neemVraagnummer = await vrijeVolgnummers(
      admin,
      "vragen",
      "hoofdstuk_id",
      hoofdstukId,
    );

    const rijen = vragen.map((v) => ({
      hoofdstuk_id: hoofdstukId,
      volgnummer: neemVraagnummer(),
      type: v.type,
      vraag: v.vraag,
      opties: v.opties ?? null,
      antwoord: v.antwoord,
      uitleg: v.uitleg ?? null,
      varianten:
        Array.isArray(v.varianten) && v.varianten.length ? v.varianten : null,
    }));

    let { error: vragenFout } = await admin.from("vragen").insert(rijen);
    // Zolang supabase/spellingvarianten.sql nog niet gedraaid is, bestaat de
    // kolom "varianten" niet. Dan gaat de import er zonder in, zodat een
    // bestand met wisselende woorden nooit een heel hoofdstuk tegenhoudt.
    if (vragenFout && rijen.some((r) => r.varianten)) {
      const zonder = rijen.map(({ varianten: _weg, ...rest }) => {
        void _weg;
        return rest;
      });
      ({ error: vragenFout } = await admin.from("vragen").insert(zonder));
    }
    if (vragenFout) {
      redirect(
        vakkenPagina(
          formData,
          "fout",
          `Vragen voor "${titel}" importeren mislukt: ${vragenFout.message}`,
        ),
      );
    }
  }

  revalidatePath("/beheer/vakken");
  redirect(vakkenPagina(formData));
}
