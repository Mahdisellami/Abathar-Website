'use client';

import React from 'react';
import type { Video } from '@/lib/types';

interface VideoCardProps {
  video: Video;
  onClick?: () => void;
}

export default function VideoCard({ video, onClick }: VideoCardProps) {
  // Use YouTube thumbnail if no custom thumbnail provided
  const thumbnailUrl = video.thumbnail_url ||
    `https://img.youtube.com/vi/${video.youtube_id}/maxresdefault.jpg`;

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow cursor-pointer">
      <div className="relative aspect-video" onClick={onClick}>
        <img
          src={thumbnailUrl}
          alt={video.title}
          className="w-full h-full object-cover"
          onError={(e) => {
            // Fallback to standard quality thumbnail if maxres fails
            const target = e.target as HTMLImageElement;
            target.src = `https://img.youtube.com/vi/${video.youtube_id}/hqdefault.jpg`;
          }}
        />
        <button
          className="absolute inset-0 flex items-center justify-center bg-black bg-opacity-30 hover:bg-opacity-50 transition"
          aria-label={`Play ${video.title}`}
        >
          {/* Play Icon */}
          <svg
            className="w-16 h-16 text-white"
            fill="currentColor"
            viewBox="0 0 24 24"
          >
            <path d="M8 5v14l11-7z" />
          </svg>
        </button>
        {video.duration && (
          <span className="absolute bottom-2 right-2 bg-black bg-opacity-75 text-white text-sm px-2 py-1 rounded">
            {video.duration}
          </span>
        )}
      </div>

      <div className="p-4">
        <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2 line-clamp-2">
          {video.title}
        </h3>
        {video.category && (
          <span className="inline-block px-2 py-1 text-xs bg-primary-100 dark:bg-primary-900 text-primary-600 dark:text-primary-300 rounded capitalize">
            {video.category}
          </span>
        )}
        {video.description && (
          <p className="mt-2 text-sm text-gray-600 dark:text-gray-400 line-clamp-2">
            {video.description}
          </p>
        )}
        {video.published_date && (
          <p className="mt-2 text-xs text-gray-500 dark:text-gray-500">
            {new Date(video.published_date).toLocaleDateString('de-DE', {
              year: 'numeric',
              month: 'long',
              day: 'numeric'
            })}
          </p>
        )}
      </div>
    </div>
  );
}
