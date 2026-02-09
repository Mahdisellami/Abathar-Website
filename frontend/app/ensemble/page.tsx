'use client';

import React, { useEffect, useState } from 'react';
import Image from 'next/image';
import { getEnsemble } from '@/lib/api';
import PhotoGallery from '@/components/PhotoGallery';
import type { Ensemble } from '@/lib/types';

export default function EnsemblePage() {
  const [ensemble, setEnsemble] = useState<Ensemble | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Performance photos
  const performancePhotos = [
    { src: '/images/performances/performance-01.webp', alt: 'Ogaro Ensemble Performance', caption: 'Ogaro Ensemble Performance' },
    { src: '/images/performances/performance-02.webp', alt: 'Ogaro Ensemble Performance', caption: 'Ogaro Ensemble Performance' },
    { src: '/images/performances/performance-03.webp', alt: 'Ogaro Ensemble Performance', caption: 'Ogaro Ensemble Performance' },
    { src: '/images/performances/performance-04.webp', alt: 'Ogaro Ensemble Performance', caption: 'Ogaro Ensemble Performance' },
    { src: '/images/performances/performance-05.webp', alt: 'Ogaro Ensemble Stage Performance', caption: 'Ogaro Ensemble Stage Performance' },
    { src: '/images/performances/performance-06.webp', alt: 'Ogaro Ensemble Stage Performance', caption: 'Ogaro Ensemble Stage Performance' },
    { src: '/images/performances/performance-07.webp', alt: 'Sound of Munich Now 2021', caption: 'Sound of Munich Now 2021 - Photo: Ananda Nefzger' },
    { src: '/images/performances/performance-08.webp', alt: 'European Championships 2022', caption: 'European Championships 2022 - Photo: Axel Heimken' },
    { src: '/images/performances/performance-09.webp', alt: 'European Championships 2022', caption: 'European Championships 2022 - Photo: Axel Heimken' },
    { src: '/images/performances/performance-10.webp', alt: 'European Championships 2022', caption: 'European Championships 2022 - Photo: Axel Heimken' },
    { src: '/images/performances/performance-11.webp', alt: 'European Championships 2022', caption: 'European Championships 2022 - Photo: Axel Heimken' },
    { src: '/images/performances/performance-12.webp', alt: 'Ogaro Ensemble Event', caption: 'Ogaro Ensemble Performance' },
  ];

  useEffect(() => {
    async function fetchEnsemble() {
      try {
        const data = await getEnsemble();
        setEnsemble(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load ensemble information');
      } finally {
        setLoading(false);
      }
    }

    fetchEnsemble();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  if (error || !ensemble) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-600 dark:text-red-400">{error || 'Ensemble information not found'}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-white dark:bg-gray-900">
      {/* Hero Section */}
      <section className="relative overflow-hidden py-16">
        {/* Background Image */}
        <div className="absolute inset-0">
          <Image
            src="/images/ensemble-group.webp"
            alt="Ogaro Ensemble members"
            fill
            priority
            className="object-cover"
            quality={90}
          />
        </div>

        {/* Gradient Overlay */}
        <div className="absolute inset-0 bg-gradient-to-br from-primary-50/90 via-secondary-50/90 to-accent-50/85 dark:from-gray-900/90 dark:via-gray-800/90 dark:to-gray-900/85"></div>

        {/* Content */}
        <div className="relative z-10 mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-4xl md:text-5xl font-serif font-bold text-gray-900 dark:text-white mb-4">
            {ensemble.name}
          </h1>
          {ensemble.formation_year && (
            <p className="text-xl text-gray-700 dark:text-gray-300">
              Established {ensemble.formation_year}
            </p>
          )}
        </div>
      </section>

      {/* Main Content */}
      <section className="py-16">
        <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
          {/* Description */}
          <div className="mb-12">
            <div className="prose prose-lg dark:prose-invert max-w-none">
              {ensemble.description.split('\n\n').map((paragraph, index) => (
                <p key={index} className="text-gray-700 dark:text-gray-300 mb-4">
                  {paragraph}
                </p>
              ))}
            </div>
          </div>

          {/* Musical Style & Vision */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
            {ensemble.musical_style && (
              <div className="bg-gradient-to-br from-primary-50 to-secondary-50 dark:from-gray-800 dark:to-gray-700 rounded-lg p-6">
                <h2 className="text-2xl font-serif font-bold text-gray-900 dark:text-white mb-4">
                  Musical Style
                </h2>
                <p className="text-gray-700 dark:text-gray-300">
                  {ensemble.musical_style}
                </p>
              </div>
            )}

            {ensemble.vision && (
              <div className="bg-gradient-to-br from-secondary-50 to-accent-50 dark:from-gray-800 dark:to-gray-700 rounded-lg p-6">
                <h2 className="text-2xl font-serif font-bold text-gray-900 dark:text-white mb-4">
                  Vision
                </h2>
                <p className="text-gray-700 dark:text-gray-300">
                  {ensemble.vision}
                </p>
              </div>
            )}
          </div>

          {/* Members */}
          {ensemble.members && ensemble.members.length > 0 && (
            <div className="mb-12">
              <h2 className="text-3xl font-serif font-bold text-gray-900 dark:text-white mb-8 text-center">
                Ensemble Members
              </h2>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {ensemble.members.map((member, index) => (
                  <div key={index} className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 border border-gray-200 dark:border-gray-700 hover:shadow-lg transition-shadow">
                    <div className="text-center">
                      <div className="w-16 h-16 bg-gradient-to-br from-primary-500 to-secondary-500 rounded-full mx-auto mb-4 flex items-center justify-center">
                        <span className="text-2xl font-bold text-white">
                          {member.name.split(' ').map(n => n[0]).join('').substring(0, 2)}
                        </span>
                      </div>
                      <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                        {member.name}
                      </h3>
                      <div className="text-sm font-medium text-primary-600 dark:text-primary-400 mb-2">
                        {member.instrument}
                      </div>
                      <div className="text-sm text-gray-600 dark:text-gray-400">
                        {member.bio}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Highlights */}
          {ensemble.highlights && ensemble.highlights.length > 0 && (
            <div className="mb-12">
              <h2 className="text-3xl font-serif font-bold text-gray-900 dark:text-white mb-6 text-center">
                Performance Highlights
              </h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {ensemble.highlights.map((highlight, index) => (
                  <div key={index} className="flex items-start bg-accent-50 dark:bg-accent-900/10 rounded-lg p-4 border border-accent-200 dark:border-accent-800">
                    <svg className="w-6 h-6 text-accent-600 dark:text-accent-400 mr-3 flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
                    </svg>
                    <span className="text-gray-700 dark:text-gray-300">
                      {typeof highlight === 'string' ? highlight : highlight}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Performance Gallery */}
          <div className="mb-12">
            <h2 className="text-3xl font-serif font-bold text-gray-900 dark:text-white mb-6 text-center">
              Performance Gallery
            </h2>
            <p className="text-center text-gray-600 dark:text-gray-400 mb-8 max-w-2xl mx-auto">
              Explore our performances from various concerts and festivals, including Sound of Munich Now 2021 and European Championships 2022.
            </p>
            <PhotoGallery photos={performancePhotos} />
          </div>

          {/* Contact Information */}
          <div className="bg-gradient-to-br from-primary-600 to-secondary-600 rounded-lg p-8 text-white text-center">
            <h2 className="text-2xl font-serif font-bold mb-4">
              Book the {ensemble.name}
            </h2>
            <p className="mb-6 text-primary-50">
              Interested in booking the ensemble for your event?
            </p>
            <div className="space-y-2">
              {ensemble.contact_email && (
                <div>
                  <a href={`mailto:${ensemble.contact_email}`} className="text-white hover:text-primary-100 transition-colors font-medium">
                    {ensemble.contact_email}
                  </a>
                </div>
              )}
              {ensemble.contact_phone && (
                <div>
                  <a href={`tel:${ensemble.contact_phone}`} className="text-white hover:text-primary-100 transition-colors font-medium">
                    {ensemble.contact_phone}
                  </a>
                </div>
              )}
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
