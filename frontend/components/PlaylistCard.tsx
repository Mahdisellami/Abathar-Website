import React from 'react';
import type { Playlist } from '@/lib/types';

interface PlaylistCardProps {
  playlist: Playlist;
  onClick?: () => void;
}

export default function PlaylistCard({ playlist, onClick }: PlaylistCardProps) {
  // YouTube playlists don't have direct thumbnail URLs
  // Use custom thumbnail if provided, otherwise show gradient background with playlist icon
  const hasCustomThumbnail = playlist.thumbnail_url && playlist.thumbnail_url.length > 0;

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
      <div className="relative aspect-video group cursor-pointer" onClick={onClick}>
        {hasCustomThumbnail ? (
          <img
            src={playlist.thumbnail_url}
            alt={playlist.title}
            className="w-full h-full object-cover"
            onError={(e) => {
              // Hide image on error and show gradient background
              const target = e.target as HTMLImageElement;
              target.style.display = 'none';
            }}
          />
        ) : null}

        {/* Gradient background for playlists without custom thumbnails */}
        {!hasCustomThumbnail && (
          <div className="absolute inset-0 bg-gradient-to-br from-primary-600 via-secondary-600 to-accent-600 dark:from-primary-700 dark:via-secondary-700 dark:to-accent-700" />
        )}

        {/* Playlist overlay icon */}
        <div className="absolute inset-0 bg-black bg-opacity-40 group-hover:bg-opacity-50 transition-opacity flex items-center justify-center">
          <div className="flex items-center space-x-2">
            {/* Play button */}
            <svg className="w-16 h-16 text-white" fill="currentColor" viewBox="0 0 24 24">
              <path d="M8 5v14l11-7z" />
            </svg>

            {/* Playlist icon */}
            <div className="flex flex-col space-y-1">
              <div className="w-1 h-1 bg-white rounded-full"></div>
              <div className="w-1 h-1 bg-white rounded-full"></div>
              <div className="w-1 h-1 bg-white rounded-full"></div>
            </div>
          </div>
        </div>

        {/* Video count badge */}
        {playlist.video_count && (
          <div className="absolute top-2 right-2 bg-black bg-opacity-75 text-white text-sm px-3 py-1 rounded">
            {playlist.video_count} Videos
          </div>
        )}
      </div>

      <div className="p-4">
        <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2 line-clamp-2">
          {playlist.title}
        </h3>

        {playlist.description && (
          <p className="text-sm text-gray-600 dark:text-gray-400 line-clamp-2 mb-2">
            {playlist.description}
          </p>
        )}

        <a
          href={playlist.playlist_url}
          target="_blank"
          rel="noopener noreferrer"
          onClick={(e) => e.stopPropagation()}
          className="inline-flex items-center text-sm text-primary-600 dark:text-primary-400 hover:text-primary-700 dark:hover:text-primary-300 transition-colors"
        >
          Playlist ansehen
          <svg className="w-4 h-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
          </svg>
        </a>
      </div>
    </div>
  );
}
