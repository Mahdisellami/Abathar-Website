'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { getEvents } from '@/lib/api';
import EventCard from '@/components/EventCard';
import type { Event } from '@/lib/types';

export default function HomePage() {
  const [upcomingEvents, setUpcomingEvents] = useState<Event[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchEvents() {
      try {
        const events = await getEvents('upcoming');
        setUpcomingEvents(events.slice(0, 3)); // Get first 3 upcoming events
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load events');
      } finally {
        setLoading(false);
      }
    }

    fetchEvents();
  }, []);

  return (
    <div>
      {/* Hero Section */}
      <section className="relative bg-gradient-to-br from-primary-50 via-secondary-50 to-accent-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900 py-20 md:py-32">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-serif font-bold text-gray-900 dark:text-white mb-6 animate-fade-in">
              Welcome to My Musical World
            </h1>
            <p className="text-xl md:text-2xl text-gray-700 dark:text-gray-300 mb-4 max-w-3xl mx-auto">
              Oud Player | Music Pedagogue | Composer | Transcultural Musician
            </p>
            <p className="text-lg text-gray-600 dark:text-gray-400 max-w-2xl mx-auto mb-8">
              Bridging Eastern and Western musical traditions through the oud, cello, and intercultural collaboration.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                href="/bio"
                className="px-8 py-3 bg-primary-600 hover:bg-primary-700 text-white font-medium rounded-lg transition-colors shadow-lg hover:shadow-xl"
              >
                View Biography
              </Link>
              <Link
                href="/events"
                className="px-8 py-3 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-900 dark:text-white font-medium rounded-lg border border-gray-300 dark:border-gray-600 transition-colors"
              >
                Upcoming Events
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Introduction */}
      <section className="py-16 bg-white dark:bg-gray-900">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl mx-auto text-center">
            <h2 className="text-3xl font-serif font-bold text-gray-900 dark:text-white mb-6">
              About Abathar Kmash
            </h2>
            <p className="text-lg text-gray-700 dark:text-gray-300 mb-4">
              Born in As-Suwaida, Syria in 1987, I am an oud and cello performer with a passion for transcultural music.
              Currently pursuing an M.A. in Music.World at Hildesheim University, I have dedicated my career to bridging
              Eastern and Western musical traditions.
            </p>
            <p className="text-lg text-gray-700 dark:text-gray-300">
              As the founder of <strong>Ogaro Ensemble</strong> and instructor at Hildesheim University, I create
              musical experiences that span from Damascus to Istanbul, from Alexandria to Baghdad.
            </p>
          </div>
        </div>
      </section>

      {/* Featured Events */}
      {!loading && !error && upcomingEvents.length > 0 && (
        <section className="py-16 bg-gray-50 dark:bg-gray-800">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-serif font-bold text-gray-900 dark:text-white mb-4">
                Upcoming Performances
              </h2>
              <p className="text-lg text-gray-600 dark:text-gray-400">
                Join me for these upcoming concerts and events
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {upcomingEvents.map((event) => (
                <EventCard key={event.id} event={event} />
              ))}
            </div>

            <div className="text-center mt-12">
              <Link
                href="/events"
                className="inline-flex items-center px-6 py-3 text-base font-medium text-primary-600 dark:text-primary-400 hover:text-primary-700 dark:hover:text-primary-300 transition-colors"
              >
                View all events
                <svg className="ml-2 w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 8l4 4m0 0l-4 4m4-4H3" />
                </svg>
              </Link>
            </div>
          </div>
        </section>
      )}

      {/* CTA Section */}
      <section className="py-16 bg-gradient-to-r from-primary-600 to-secondary-600">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h2 className="text-3xl font-serif font-bold text-white mb-4">
              Interested in Music Lessons?
            </h2>
            <p className="text-xl text-primary-50 mb-8 max-w-2xl mx-auto">
              I offer instruction in oud, cello, and Arabic music theory. Contact me to learn more about lessons and availability.
            </p>
            <Link
              href="/contact"
              className="inline-block px-8 py-3 bg-white text-primary-600 font-medium rounded-lg hover:bg-primary-50 transition-colors shadow-lg hover:shadow-xl"
            >
              Get in Touch
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}
