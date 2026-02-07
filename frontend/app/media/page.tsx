'use client';

import { useState, useEffect } from 'react';
import { getVideos, getFeaturedVideos } from '@/lib/api';
import type { Video } from '@/lib/types';
import VideoGrid from '@/components/VideoGrid';
import VideoModal from '@/components/VideoModal';

// YouTube channel URL
const YOUTUBE_CHANNEL_URL = 'https://www.youtube.com/@abatharkmash3453';

export default function MediaPage() {
  const [allVideos, setAllVideos] = useState<Video[]>([]);
  const [featuredVideos, setFeaturedVideos] = useState<Video[]>([]);
  const [filteredVideos, setFilteredVideos] = useState<Video[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [selectedVideo, setSelectedVideo] = useState<Video | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchVideos = async () => {
      try {
        setLoading(true);
        setError(null);

        const [featured, all] = await Promise.all([
          getFeaturedVideos(3),
          getVideos({ limit: 50 })
        ]);

        setFeaturedVideos(featured);
        setAllVideos(all);
        setFilteredVideos(all);
      } catch (err) {
        console.error('Failed to load videos:', err);
        setError('Fehler beim Laden der Videos. Bitte versuchen Sie es später erneut.');
      } finally {
        setLoading(false);
      }
    };

    fetchVideos();
  }, []);

  // Filter videos by category
  useEffect(() => {
    if (selectedCategory === 'all') {
      setFilteredVideos(allVideos);
    } else {
      setFilteredVideos(allVideos.filter(video => video.category === selectedCategory));
    }
  }, [selectedCategory, allVideos]);

  // Get unique categories from all videos
  const categories: string[] = [
    'all',
    ...Array.from(new Set(allVideos.map(v => v.category).filter((c): c is string => Boolean(c))))
  ];

  const handleVideoClick = (video: Video) => {
    setSelectedVideo(video);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    // Delay clearing selected video to allow for closing animation
    setTimeout(() => setSelectedVideo(null), 300);
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative bg-gradient-to-br from-primary-50 via-secondary-50 to-accent-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900 py-16 md:py-24">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-4xl md:text-5xl font-serif font-bold text-gray-900 dark:text-white mb-4">
              Videos & Aufführungen
            </h1>
            <p className="text-xl text-gray-700 dark:text-gray-300 mb-8 max-w-3xl mx-auto">
              Sehen Sie Konzertaufnahmen, Interviews und mehr von Abathar Kmash und dem Ogaro Ensemble
            </p>
            <a
              href={YOUTUBE_CHANNEL_URL}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center px-6 py-3 bg-red-600 hover:bg-red-700 text-white font-medium rounded-lg transition shadow-lg hover:shadow-xl"
            >
              <svg className="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 24 24">
                <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
              </svg>
              YouTube-Kanal abonnieren
            </a>
          </div>
        </div>
      </section>

      {/* Featured Videos Section */}
      {featuredVideos.length > 0 && (
        <section className="py-16 bg-white dark:bg-gray-900">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h2 className="text-3xl font-serif font-bold text-gray-900 dark:text-white mb-8 text-center">
              Ausgewählte Aufführungen
            </h2>
            <VideoGrid
              videos={featuredVideos}
              columns={3}
              onVideoClick={handleVideoClick}
            />
          </div>
        </section>
      )}

      {/* All Videos Section */}
      <section className="py-16 bg-gray-50 dark:bg-gray-800">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row md:items-center md:justify-between mb-8">
            <h2 className="text-3xl font-serif font-bold text-gray-900 dark:text-white mb-4 md:mb-0">
              Alle Videos
            </h2>

            {/* Category Filter */}
            <div className="flex flex-wrap gap-2">
              {categories.map(category => (
                <button
                  key={category}
                  onClick={() => setSelectedCategory(category)}
                  className={`px-4 py-2 rounded-lg font-medium transition capitalize ${
                    selectedCategory === category
                      ? 'bg-primary-600 text-white'
                      : 'bg-white dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-600'
                  }`}
                >
                  {category === 'all' ? 'Alle' : category}
                </button>
              ))}
            </div>
          </div>

          {error ? (
            <div className="text-center py-12">
              <p className="text-red-600 dark:text-red-400">{error}</p>
            </div>
          ) : (
            <VideoGrid
              videos={filteredVideos}
              columns={3}
              onVideoClick={handleVideoClick}
            />
          )}
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
