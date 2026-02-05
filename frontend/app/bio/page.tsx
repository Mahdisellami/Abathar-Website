'use client';

import React, { useEffect, useState } from 'react';
import { getBio } from '@/lib/api';
import type { Bio } from '@/lib/types';

export default function BioPage() {
  const [bio, setBio] = useState<Bio | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchBio() {
      try {
        const data = await getBio();
        setBio(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load biography');
      } finally {
        setLoading(false);
      }
    }

    fetchBio();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  if (error || !bio) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-600 dark:text-red-400">{error || 'Biography not found'}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-white dark:bg-gray-900">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-primary-50 via-secondary-50 to-accent-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900 py-16">
        <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-4xl md:text-5xl font-serif font-bold text-gray-900 dark:text-white mb-4">
            {bio.name}
          </h1>
          <p className="text-xl md:text-2xl text-gray-700 dark:text-gray-300">
            {bio.title}
          </p>
        </div>
      </section>

      {/* Biography Content */}
      <section className="py-16">
        <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
          {/* Main Bio Text */}
          <div className="prose prose-lg dark:prose-invert max-w-none mb-12">
            {bio.bio_text.split('\n\n').map((paragraph, index) => (
              <p key={index} className="text-gray-700 dark:text-gray-300 mb-4">
                {paragraph}
              </p>
            ))}
          </div>

          {/* Education */}
          {bio.education && bio.education.length > 0 && (
            <div className="mb-12">
              <h2 className="text-2xl font-serif font-bold text-gray-900 dark:text-white mb-6">
                Education
              </h2>
              <div className="space-y-4">
                {bio.education.map((edu, index) => (
                  <div key={index} className="border-l-4 border-primary-600 dark:border-primary-400 pl-4">
                    <div className="font-semibold text-gray-900 dark:text-white">
                      {edu.degree}
                    </div>
                    <div className="text-gray-700 dark:text-gray-300">
                      {edu.institution}
                    </div>
                    <div className="text-sm text-gray-600 dark:text-gray-400">
                      {edu.period}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Current Roles */}
          {bio.current_roles && bio.current_roles.length > 0 && (
            <div className="mb-12">
              <h2 className="text-2xl font-serif font-bold text-gray-900 dark:text-white mb-6">
                Current Roles
              </h2>
              <ul className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {bio.current_roles.map((role, index) => (
                  <li key={index} className="flex items-start">
                    <svg className="w-6 h-6 text-primary-600 dark:text-primary-400 mr-2 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                    <span className="text-gray-700 dark:text-gray-300">{role}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Notable Achievements */}
          {bio.achievements && bio.achievements.length > 0 && (
            <div className="mb-12">
              <h2 className="text-2xl font-serif font-bold text-gray-900 dark:text-white mb-6">
                Notable Achievements
              </h2>
              <ul className="space-y-3">
                {bio.achievements.map((achievement, index) => (
                  <li key={index} className="flex items-start">
                    <svg className="w-6 h-6 text-accent-600 dark:text-accent-400 mr-3 flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
                    </svg>
                    <span className="text-gray-700 dark:text-gray-300">
                      {achievement}
                    </span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Discography */}
          {bio.discography && bio.discography.length > 0 && (
            <div>
              <h2 className="text-2xl font-serif font-bold text-gray-900 dark:text-white mb-6">
                Discography
              </h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {bio.discography.map((item, index) => (
                  <div key={index} className="bg-gray-50 dark:bg-gray-800 rounded-lg p-4 border border-gray-200 dark:border-gray-700">
                    <div className="flex items-start">
                      <svg className="w-5 h-5 text-secondary-600 dark:text-secondary-400 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3" />
                      </svg>
                      <div>
                        <div className="text-gray-900 dark:text-white font-medium">{item.title}</div>
                        <div className="text-sm text-gray-600 dark:text-gray-400">{item.role} ({item.year})</div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </section>
    </div>
  );
}
