'use client';

import React from 'react';
import Link from 'next/link';

export default function Footer() {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer className="bg-gray-50 dark:bg-gray-900 border-t border-gray-200 dark:border-gray-700">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* About */}
          <div>
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
              Abathar Kmash
            </h3>
            <p className="text-sm text-gray-600 dark:text-gray-400">
              Professional oud player, music pedagogue, and composer based in Munich, Germany.
              Specializing in transcultural music that bridges Eastern and Western traditions.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
              Quick Links
            </h3>
            <ul className="space-y-2">
              <li>
                <Link href="/bio" className="text-sm text-gray-600 dark:text-gray-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors">
                  Biography
                </Link>
              </li>
              <li>
                <Link href="/events" className="text-sm text-gray-600 dark:text-gray-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors">
                  Upcoming Events
                </Link>
              </li>
              <li>
                <Link href="/ensemble" className="text-sm text-gray-600 dark:text-gray-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors">
                  Ogaro Ensemble
                </Link>
              </li>
              <li>
                <Link href="/contact" className="text-sm text-gray-600 dark:text-gray-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors">
                  Contact
                </Link>
              </li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
              Contact
            </h3>
            <ul className="space-y-2 text-sm text-gray-600 dark:text-gray-400">
              <li>
                <a href="mailto:abathar.k987@gmail.com" className="hover:text-primary-600 dark:hover:text-primary-400 transition-colors">
                  abathar.k987@gmail.com
                </a>
              </li>
              <li>
                <a href="tel:+4917620360789" className="hover:text-primary-600 dark:hover:text-primary-400 transition-colors">
                  +49 176 20360789
                </a>
              </li>
              <li className="pt-2">
                Haimhauser 15<br />
                80802 München<br />
                Germany
              </li>
            </ul>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="mt-12 pt-8 border-t border-gray-200 dark:border-gray-700">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <p className="text-sm text-gray-600 dark:text-gray-400">
              © {new Date().getFullYear()} Abathar Kmash. All rights reserved.
            </p>

            <button
              onClick={scrollToTop}
              className="mt-4 md:mt-0 px-4 py-2 text-sm font-medium text-gray-700 dark:text-gray-300 hover:text-primary-600 dark:hover:text-primary-400 transition-colors"
              aria-label="Scroll to top"
            >
              ↑ Scroll to top
            </button>
          </div>
        </div>
      </div>
    </footer>
  );
}
