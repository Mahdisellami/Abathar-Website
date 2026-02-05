'use client';

import React from 'react';
import { format, parseISO } from 'date-fns';
import type { Event } from '@/lib/types';

interface EventCardProps {
  event: Event;
}

export default function EventCard({ event }: EventCardProps) {
  const eventDate = parseISO(event.date);
  const formattedDate = format(eventDate, 'MMMM d, yyyy');
  const dayOfWeek = format(eventDate, 'EEEE');

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-shadow p-6 border border-gray-200 dark:border-gray-700">
      {/* Date Badge */}
      <div className="flex items-start justify-between mb-4">
        <div className="flex-shrink-0 text-center bg-primary-50 dark:bg-primary-900/20 rounded-lg p-3">
          <div className="text-2xl font-bold text-primary-600 dark:text-primary-400">
            {format(eventDate, 'd')}
          </div>
          <div className="text-xs font-medium text-primary-600 dark:text-primary-400">
            {format(eventDate, 'MMM')}
          </div>
        </div>

        {event.is_past && (
          <span className="px-3 py-1 text-xs font-medium bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded-full">
            Past Event
          </span>
        )}
      </div>

      {/* Event Details */}
      <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
        {event.title}
      </h3>

      <div className="space-y-2 text-sm text-gray-600 dark:text-gray-400">
        {/* Date & Time */}
        <div className="flex items-center">
          <svg className="w-4 h-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
          </svg>
          <span>{dayOfWeek}, {formattedDate}</span>
          {event.time && <span className="ml-2">• {event.time}</span>}
        </div>

        {/* Venue */}
        <div className="flex items-center">
          <svg className="w-4 h-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
          <span>
            {event.venue}
            {event.location && `, ${event.location}`}
          </span>
        </div>

        {/* Ensemble */}
        {event.ensemble_name && (
          <div className="flex items-center">
            <svg className="w-4 h-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3" />
            </svg>
            <span>{event.ensemble_name}</span>
          </div>
        )}

        {/* Description */}
        {event.description && (
          <p className="mt-3 text-gray-700 dark:text-gray-300">
            {event.description}
          </p>
        )}

        {/* Event Type Badge */}
        {event.event_type && (
          <div className="pt-2">
            <span className="inline-block px-2 py-1 text-xs font-medium bg-secondary-50 dark:bg-secondary-900/20 text-secondary-600 dark:text-secondary-400 rounded">
              {event.event_type}
            </span>
          </div>
        )}
      </div>
    </div>
  );
}
