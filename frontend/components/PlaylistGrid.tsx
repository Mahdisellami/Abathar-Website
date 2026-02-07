import React from 'react';
import type { Playlist } from '@/lib/types';
import PlaylistCard from './PlaylistCard';

interface PlaylistGridProps {
  playlists: Playlist[];
  columns?: 2 | 3 | 4;
  onPlaylistClick?: (playlist: Playlist) => void;
}

export default function PlaylistGrid({ playlists, columns = 3, onPlaylistClick }: PlaylistGridProps) {
  const gridCols = {
    2: 'grid-cols-1 md:grid-cols-2',
    3: 'grid-cols-1 md:grid-cols-2 lg:grid-cols-3',
    4: 'grid-cols-1 md:grid-cols-2 lg:grid-cols-4',
  };

  if (playlists.length === 0) {
    return (
      <div className="text-center py-12">
        <svg className="mx-auto h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
        </svg>
        <p className="mt-4 text-gray-500 dark:text-gray-400">
          Keine Playlists verfügbar
        </p>
      </div>
    );
  }

  return (
    <div className={`grid ${gridCols[columns]} gap-6`}>
      {playlists.map((playlist) => (
        <PlaylistCard
          key={playlist.id}
          playlist={playlist}
          onClick={() => onPlaylistClick?.(playlist)}
        />
      ))}
    </div>
  );
}
