import Link from "next/link";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";

export default async function BetalenVoltooidPage() {
  const session = await getSessionProfile();

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-md flex-1 px-6 py-16 text-center">
        <h1 className="font-display text-2xl font-semibold text-ink">Bedankt!</h1>
        <p className="mt-3 text-sm text-ink-dim">
          We verwerken je betaling — dit duurt meestal maar enkele seconden. Ververs je account
          zodra je toegang niet meteen zichtbaar is.
        </p>
        <Link
          href="/account"
          className="mt-6 inline-block rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
        >
          Naar mijn account
        </Link>
      </main>
    </>
  );
}
