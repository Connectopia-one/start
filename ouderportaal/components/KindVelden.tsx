import { type Kind } from "@/lib/kind";

/*
  De vakjes van één inlichtingenfiche, om in te vullen.

  Dit formulier stond eerst alleen op /portaal/gezin. Sinds 12 oktober 2026
  staat het ook op /beheer/gezinnen/<id>, want Kim keek daar naar de fiche van
  een gezin en kon ze niet aanpassen; de enige weg was eerst meekijken met dat
  gezin. Zie connectopia-kim-twee-accounts in het geheugen: dat is precies hoe
  de fiche van haar eigen zoon op het verkeerde profiel belandde.

  Het formulier weet zelf niet bij welk gezin het hoort. Dat beslist de actie
  die het meekrijgt: op het ouderscherm het gezin van wie ingelogd is, op het
  beheerscherm het gezin dat in gezinId staat.
*/
export function KindVelden({
  action,
  kind,
  gezinId,
  submitLabel,
}: {
  action: (formData: FormData) => void | Promise<void>;
  kind?: Kind;
  /* Enkel op het beheerscherm: bij welk gezin deze fiche hoort. */
  gezinId?: string;
  submitLabel: string;
}) {
  return (
    <form action={action} className="mt-4 space-y-4">
      {kind && <input type="hidden" name="kind_id" value={kind.id} />}
      {gezinId && <input type="hidden" name="gezin_id" value={gezinId} />}

      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">Naam kind</label>
          <input
            name="naam"
            required
            defaultValue={kind?.naam ?? ""}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">Geboortedatum</label>
          <input
            name="geboortedatum"
            type="date"
            defaultValue={kind?.geboortedatum ?? ""}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">School</label>
          <input
            name="school"
            defaultValue={kind?.school ?? ""}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">Leerjaar</label>
          <input
            name="leerjaar"
            defaultValue={kind?.leerjaar ?? ""}
            placeholder="Bv. 4de leerjaar, 1A"
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">Allergieën</label>
        <textarea
          name="allergieen"
          rows={2}
          defaultValue={kind?.allergieen ?? ""}
          placeholder="Bv. noten, penicilline — of laat leeg indien niet van toepassing"
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">
          Eten — buiten een allergie
        </label>
        <input
          name="eten"
          defaultValue={kind?.eten ?? ""}
          placeholder="Bv. vegetarisch, geen varkensvlees, eet weinig warm"
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">
          Medicatie tijdens de dag
        </label>
        <textarea
          name="medicatie"
          rows={2}
          defaultValue={kind?.medicatie ?? ""}
          placeholder="Wat, hoeveel en op welk moment. Laat leeg als er niets moet gegeven worden."
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">
          Diagnoses / aandachtspunten
        </label>
        <textarea
          name="diagnoses"
          rows={2}
          defaultValue={kind?.diagnoses ?? ""}
          placeholder="Bv. ADHD, ASS, HB — wat wij als begeleiders goed zouden moeten weten"
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">
          Wat helpt als het je kind te veel wordt?
        </label>
        <textarea
          name="wat_helpt"
          rows={2}
          defaultValue={kind?.wat_helpt ?? ""}
          placeholder="Bv. even apart zitten, niet aanraken, een vaste knuffel, buiten gaan"
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">
            Huisarts — naam
          </label>
          <input
            name="huisarts_naam"
            defaultValue={kind?.huisarts_naam ?? ""}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">
            Huisarts — telefoon
          </label>
          <input
            name="huisarts_telefoon"
            type="tel"
            defaultValue={kind?.huisarts_telefoon ?? ""}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">
            Noodcontact — naam
          </label>
          <input
            name="noodcontact_naam"
            defaultValue={kind?.noodcontact_naam ?? ""}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">
            Noodcontact — telefoon
          </label>
          <input
            name="noodcontact_telefoon"
            type="tel"
            defaultValue={kind?.noodcontact_telefoon ?? ""}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">
            Tweede noodcontact — naam
          </label>
          <input
            name="noodcontact2_naam"
            defaultValue={kind?.noodcontact2_naam ?? ""}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-ink">
            Tweede noodcontact — telefoon
          </label>
          <input
            name="noodcontact2_telefoon"
            type="tel"
            defaultValue={kind?.noodcontact2_telefoon ?? ""}
            placeholder="Voor als het eerste nummer niet opneemt"
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">
          Wie mag je kind ophalen?
        </label>
        <input
          name="ophalen"
          defaultValue={kind?.ophalen ?? ""}
          placeholder="De namen van wie het kind mag meenemen, naast jezelf"
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      <div className="space-y-2 rounded-md bg-paper p-3">
        <label className="flex items-start gap-2 text-sm">
          <input
            type="checkbox"
            name="alleen_naar_huis"
            defaultChecked={kind?.alleen_naar_huis ?? false}
            className="mt-0.5"
          />
          <span>
            Mijn kind mag op het einde van de dag alleen naar huis gaan.
          </span>
        </label>
      </div>

      <div className="space-y-2 rounded-md bg-paper p-3">
        <label className="flex items-start gap-2 text-sm">
          <input
            type="checkbox"
            name="toestemming_fotos"
            defaultChecked={kind?.toestemming_fotos ?? false}
            className="mt-0.5"
          />
          <span>
            Ik geef toestemming om foto&apos;s van mijn kind te maken en te
            delen binnen het ouderportaal (klasje, kamp).
          </span>
        </label>
        <label className="flex items-start gap-2 text-sm">
          <input
            type="checkbox"
            name="toestemming_social_media"
            defaultChecked={kind?.toestemming_social_media ?? false}
            className="mt-0.5"
          />
          <span>
            Ik geef toestemming om foto&apos;s van mijn kind te gebruiken op de
            publieke website of social media van Connectopia.
          </span>
        </label>
      </div>

      <button
        type="submit"
        className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
      >
        {submitLabel}
      </button>
    </form>
  );
}
