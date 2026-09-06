import Link from "next/link";

export default function BevestigEmailPage() {
  return (
    <main className="flex flex-1 items-center justify-center bg-paper px-6 py-16">
      <div className="w-full max-w-sm text-center">
        <h1 className="font-display text-2xl font-semibold text-ink">Bijna klaar!</h1>
        <p className="mt-3 text-sm text-ink-dim">
          We stuurden een bevestigingslink naar je e-mailadres. Klik op die link om je account te
          activeren, en log daarna in.
        </p>
        <Link
          href="/login"
          className="mt-6 inline-block rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
        >
          Naar inloggen
        </Link>
      </div>
    </main>
  );
}
