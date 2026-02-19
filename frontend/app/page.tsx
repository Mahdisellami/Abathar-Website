'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { getEvents, getFeaturedVideos } from '@/lib/api';
import EventCard from '@/components/EventCard';
import VideoGrid from '@/components/VideoGrid';
import VideoModal from '@/components/VideoModal';
import type { Event, Video } from '@/lib/types';

export default function HomePage() {
  const [upcomingEvents, setUpcomingEvents] = useState<Event[]>([]);
  const [featuredVideos, setFeaturedVideos] = useState<Video[]>([]);
  const [selectedVideo, setSelectedVideo] = useState<Video | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const [events, videos] = await Promise.all([
          getEvents('upcoming'),
          getFeaturedVideos(3)
        ]);
        setUpcomingEvents(events.slice(0, 3)); // Get first 3 upcoming events
        setFeaturedVideos(videos);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load data');
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  const handleVideoClick = (video: Video) => {
    setSelectedVideo(video);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setTimeout(() => setSelectedVideo(null), 300);
  };

  return (
    <div>
      {/* Hero Section */}
      <section className="relative overflow-hidden h-[70vh] md:h-[80vh] lg:h-[90vh] min-h-[600px]">
        {/* Background Image */}
        <div className="absolute inset-0">
          <Image
            src="/images/hero-performance.webp"
            alt="Abathar Kmash performing with Ogaro Ensemble"
            fill
            priority
            className="object-cover object-center"
            quality={90}
            placeholder="blur"
            blurDataURL="data:image/webp;base64,UklGRh4AAABXRUJQVlA4IBIAAAAwAQCdASoBAAEAAwA0JaQAA3AA/vuUAAA="
          />
        </div>

        {/* Dark Overlay */}
        <div className="absolute inset-0 bg-black/40"></div>

        {/* Content */}
        <div className="relative z-10 mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 h-full flex items-center justify-center">
          <div className="text-center">
            <h1 className="text-5xl md:text-7xl lg:text-8xl font-script text-white mb-2 animate-fade-in" style={{ fontFamily: 'var(--font-great-vibes)' }}>
              Abathar Kmash
            </h1>
            <h2 className="text-4xl md:text-6xl lg:text-7xl font-amiri font-bold text-white mb-8 animate-fade-in" style={{ fontFamily: 'var(--font-amiri)' }}>
              أباذر قماش
            </h2>
            <p className="text-xl md:text-2xl lg:text-3xl text-white/90 mb-6 max-w-4xl mx-auto font-light">
              Oud Player | Music Pedagogue | Composer | Transcultural Musician
            </p>
            <p className="text-lg md:text-xl text-white/80 max-w-3xl mx-auto mb-10 font-light">
              Bridging Eastern and Western musical traditions through the oud, cello, and intercultural collaboration.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                href="/bio"
                className="px-8 py-3 bg-white hover:bg-gray-100 text-gray-900 font-medium rounded-lg transition-colors shadow-lg hover:shadow-xl"
              >
                View Biography
              </Link>
              <Link
                href="/events"
                className="px-8 py-3 bg-transparent hover:bg-white/10 text-white font-medium rounded-lg border-2 border-white transition-colors"
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
          <div className="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
            {/* Image */}
            <div className="order-2 md:order-1">
              <div className="relative aspect-[4/3] rounded-lg overflow-hidden shadow-xl">
                <Image
                  src="/images/about-performing.webp"
                  alt="Abathar Kmash performing on oud"
                  fill
                  className="object-cover"
                  quality={85}
                  placeholder="blur"
                  blurDataURL="data:image/webp;base64,UklGRh4AAABXRUJQVlA4IBIAAAAwAQCdASoBAAEAAwA0JaQAA3AA/vuUAAA="
                />
              </div>
            </div>

            {/* Text */}
            <div className="order-1 md:order-2">
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

      {/* Featured Videos */}
      {!loading && featuredVideos.length > 0 && (
        <section className="py-16 bg-white dark:bg-gray-900">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-serif font-bold text-gray-900 dark:text-white mb-4">
                Featured Performances
              </h2>
              <p className="text-lg text-gray-600 dark:text-gray-400">
                Watch recent concert recordings and performances
              </p>
            </div>

            <VideoGrid
              videos={featuredVideos}
              columns={3}
              onVideoClick={handleVideoClick}
            />

            <div className="text-center mt-12">
              <Link
                href="/media"
                className="inline-flex items-center px-6 py-3 text-base font-medium text-primary-600 dark:text-primary-400 hover:text-primary-700 dark:hover:text-primary-300 transition-colors"
              >
                View all videos
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

      {/* Video Modal */}
      <VideoModal
        video={selectedVideo}
        isOpen={isModalOpen}
        onClose={handleCloseModal}
      />
    </div>
  );
}
