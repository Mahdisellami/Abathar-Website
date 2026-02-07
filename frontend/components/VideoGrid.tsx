'use client';

import React from 'react';
import VideoCard from './VideoCard';
import type { Video } from '@/lib/types';

interface VideoGridProps {
  videos: Video[];
  columns?: 2 | 3 | 4;
  onVideoClick?: (video: Video) => void;
}

export default function VideoGrid({ videos, columns = 3, onVideoClick }: VideoGridProps) {
  const gridCols = {
    2: 'grid-cols-1 md:grid-cols-2',
    3: 'grid-cols-1 md:grid-cols-2 lg:grid-cols-3',
    4: 'grid-cols-1 md:grid-cols-2 lg:grid-cols-4',
  };

  if (videos.length === 0) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-600 dark:text-gray-400 text-lg">
          Keine Videos gefunden.
        </p>
      </div>
    );
  }

  return (
    <div className={`grid ${gridCols[columns]} gap-6`}>
      {videos.map(video => (
        <VideoCard
          key={video.id}
          video={video}
          onClick={() => onVideoClick?.(video)}
        />
      ))}
    </div>
  );
}
