import type { Metadata } from 'next';
import { Inter, Playfair_Display, Amiri, Great_Vibes } from 'next/font/google';
import { SpeedInsights } from '@vercel/speed-insights/next';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import { ThemeProvider } from '@/components/ThemeProvider';
import '@/styles/globals.css';

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'optional',
  preload: true,
});

const playfair = Playfair_Display({
  subsets: ['latin'],
  variable: '--font-playfair',
  display: 'optional',
});

const amiri = Amiri({
  subsets: ['arabic', 'latin'],
  weight: ['400', '700'],
  variable: '--font-amiri',
  display: 'swap',
  preload: true,
});

const greatVibes = Great_Vibes({
  subsets: ['latin'],
  weight: '400',
  variable: '--font-great-vibes',
  display: 'swap',
  preload: true,
});

// Force dynamic rendering for all pages
export const dynamic = 'force-dynamic';

export const metadata: Metadata = {
  title: 'Abathar Kmash | Oud Player, Music Pedagogue, Composer',
  description: 'Professional oud player, music pedagogue, and composer based in Munich, Germany. Specializing in transcultural music that bridges Eastern and Western traditions.',
  keywords: 'oud, music, pedagogue, composer, transcultural music, Munich, Ogaro Ensemble, Arabic music, concerts',
  authors: [{ name: 'Abathar Kmash' }],
  openGraph: {
    title: 'Abathar Kmash | Oud Player & Composer',
    description: 'Professional oud player and music pedagogue in Munich. Founder of Ogaro Ensemble.',
    type: 'website',
    locale: 'de_DE',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="de" className={`${inter.variable} ${playfair.variable} ${amiri.variable} ${greatVibes.variable}`} suppressHydrationWarning>
      <body className="min-h-screen flex flex-col bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
        <ThemeProvider>
          <Header />
          <main className="flex-1">
            {children}
          </main>
          <Footer />
        </ThemeProvider>
        <SpeedInsights />
      </body>
    </html>
  );
}
