'use client';

import React, { useState } from 'react';
import Image from 'next/image';
import PhotoGallery from '@/components/PhotoGallery';

export default function GalleryPage() {
  const [selectedCategory, setSelectedCategory] = useState<'all' | 'performances' | 'portraits'>('all');

  // All performance photos
  const performancePhotos = [
    { src: '/images/performances/performance-01.webp', alt: 'Ogaro Ensemble Performance', caption: 'Ogaro Ensemble Performance', category: 'performances' },
    { src: '/images/performances/performance-02.webp', alt: 'Ogaro Ensemble Performance', caption: 'Ogaro Ensemble Performance', category: 'performances' },
    { src: '/images/performances/performance-03.webp', alt: 'Ogaro Ensemble Performance', caption: 'Ogaro Ensemble Performance', category: 'performances' },
    { src: '/images/performances/performance-04.webp', alt: 'Ogaro Ensemble Performance', caption: 'Ogaro Ensemble Performance', category: 'performances' },
    { src: '/images/performances/performance-05.webp', alt: 'Ogaro Ensemble Stage Performance', caption: 'Ogaro Ensemble Stage Performance', category: 'performances' },
    { src: '/images/performances/performance-06.webp', alt: 'Ogaro Ensemble Stage Performance', caption: 'Ogaro Ensemble Stage Performance', category: 'performances' },
    { src: '/images/performances/performance-07.webp', alt: 'Sound of Munich Now 2021', caption: 'Sound of Munich Now 2021 - Photo: Ananda Nefzger', category: 'performances' },
    { src: '/images/performances/performance-08.webp', alt: 'European Championships 2022', caption: 'European Championships 2022 - Photo: Axel Heimken', category: 'performances' },
    { src: '/images/performances/performance-09.webp', alt: 'European Championships 2022', caption: 'European Championships 2022 - Photo: Axel Heimken', category: 'performances' },
    { src: '/images/performances/performance-10.webp', alt: 'European Championships 2022', caption: 'European Championships 2022 - Photo: Axel Heimken', category: 'performances' },
    { src: '/images/performances/performance-11.webp', alt: 'European Championships 2022', caption: 'European Championships 2022 - Photo: Axel Heimken', category: 'performances' },
    { src: '/images/performances/performance-12.webp', alt: 'Ogaro Ensemble Event', caption: 'Ogaro Ensemble Performance', category: 'performances' },
  ];

  // Portrait and featured photos
  const portraitPhotos = [
    { src: '/images/hero-performance.webp', alt: 'Ogaro Ensemble at Sound of Munich Now', caption: 'Ogaro Ensemble - Sound of Munich Now 2023 - Photo: Marie Lehmann (@mariellemilia)', category: 'portraits' },
    { src: '/images/profile-abathar.webp', alt: 'Abathar Kmash Portrait', caption: 'Abathar Kmash - Photo: Lena Semmelroggen', category: 'portraits' },
    { src: '/images/ensemble-group.webp', alt: 'Ogaro Ensemble Group Photo', caption: 'Ogaro Ensemble Group Photo', category: 'portraits' },
    { src: '/images/about-performing.webp', alt: 'Abathar Performing', caption: 'Abathar Kmash performing on oud', category: 'portraits' },
  ];

  const allPhotos = [...portraitPhotos, ...performancePhotos];

  const filteredPhotos = selectedCategory === 'all'
    ? allPhotos
    : selectedCategory === 'portraits'
      ? portraitPhotos
      : performancePhotos;

  return (
    <div className="min-h-screen bg-white dark:bg-gray-900">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-primary-50 via-secondary-50 to-accent-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900 py-16">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-4xl md:text-5xl font-serif font-bold text-gray-900 dark:text-white mb-4">
            Photo Gallery
          </h1>
          <p className="text-xl text-gray-700 dark:text-gray-300 max-w-3xl mx-auto">
            Explore moments from concerts, festivals, and performances featuring Abathar Kmash and Ogaro Ensemble
          </p>
        </div>
      </section>

      {/* Gallery Content */}
      <section className="py-16">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          {/* Category Filter */}
          <div className="flex flex-wrap justify-center gap-4 mb-12">
            <button
              onClick={() => setSelectedCategory('all')}
              className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                selectedCategory === 'all'
                  ? 'bg-primary-600 text-white'
                  : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600'
              }`}
            >
              All Photos ({allPhotos.length})
            </button>
            <button
              onClick={() => setSelectedCategory('portraits')}
              className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                selectedCategory === 'portraits'
                  ? 'bg-primary-600 text-white'
                  : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600'
              }`}
            >
              Portraits & Featured ({portraitPhotos.length})
            </button>
            <button
              onClick={() => setSelectedCategory('performances')}
              className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                selectedCategory === 'performances'
                  ? 'bg-primary-600 text-white'
                  : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600'
              }`}
            >
              Performances ({performancePhotos.length})
            </button>
          </div>

          {/* Photo Gallery */}
          <PhotoGallery photos={filteredPhotos} />

          {/* Photo Credits */}
          <div className="mt-16 pt-8 border-t border-gray-200 dark:border-gray-700">
            <h2 className="text-2xl font-serif font-bold text-gray-900 dark:text-white mb-6 text-center">
              Photography Credits
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
              <div className="text-center">
                <div className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
                  Marie Lehmann
                </div>
                <p className="text-sm text-gray-600 dark:text-gray-400">
                  Instagram: <a href="https://instagram.com/mariellemilia" target="_blank" rel="noopener noreferrer" className="text-primary-600 dark:text-primary-400 hover:underline">@mariellemilia</a>
                </p>
                <p className="text-xs text-gray-500 dark:text-gray-500 mt-1">
                  Sound of Munich Now 2023
                </p>
              </div>
              <div className="text-center">
                <div className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
                  Lena Semmelroggen
                </div>
                <p className="text-xs text-gray-500 dark:text-gray-500 mt-1">
                  Portrait Photography
                </p>
              </div>
              <div className="text-center">
                <div className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
                  Axel Heimken
                </div>
                <p className="text-xs text-gray-500 dark:text-gray-500 mt-1">
                  European Championships 2022
                </p>
              </div>
              <div className="text-center">
                <div className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
                  Ananda Nefzger
                </div>
                <p className="text-xs text-gray-500 dark:text-gray-500 mt-1">
                  Sound of Munich Now 2021
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
