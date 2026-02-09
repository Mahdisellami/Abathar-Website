import type { Event, Bio, Ensemble, Video, Playlist } from '../types'

describe('TypeScript Types', () => {
  describe('Event interface', () => {
    it('should accept valid Event object', () => {
      const event: Event = {
        id: 1,
        title: 'Test Event',
        date: '2026-12-31',
        time: '20:00',
        venue: 'Test Venue',
        location: 'Test City',
        description: 'Test Description',
        ensemble_name: 'Test Ensemble',
        event_type: 'concert',
        photo_url: '/images/test.webp',
        is_past: false,
        created_at: '2024-01-01T00:00:00Z',
        updated_at: '2024-01-01T00:00:00Z',
      }

      expect(event.id).toBe(1)
      expect(event.title).toBe('Test Event')
      expect(event.photo_url).toBe('/images/test.webp')
    })

    it('should accept Event with optional photo_url as undefined', () => {
      const event: Event = {
        id: 1,
        title: 'Test Event',
        date: '2026-12-31',
        venue: 'Test Venue',
        location: 'Test City',
        is_past: false,
        created_at: '2024-01-01T00:00:00Z',
        updated_at: '2024-01-01T00:00:00Z',
      }

      expect(event.photo_url).toBeUndefined()
    })
  })

  describe('Bio interface', () => {
    it('should accept valid Bio object', () => {
      const bio: Bio = {
        id: 1,
        name: 'Test Name',
        title: 'Test Title',
        bio_text: 'Test bio text',
        education: [],
        achievements: [],
        current_roles: [],
        discography: [],
        created_at: '2024-01-01T00:00:00Z',
        updated_at: '2024-01-01T00:00:00Z',
      }

      expect(bio.name).toBe('Test Name')
      expect(bio.title).toBe('Test Title')
    })
  })

  describe('Video interface', () => {
    it('should accept valid Video object', () => {
      const video: Video = {
        id: 1,
        title: 'Test Video',
        youtube_id: 'abc123',
        description: 'Test description',
        thumbnail_url: 'https://example.com/thumb.jpg',
        duration: '3:45',
        view_count: 1000,
        published_at: '2024-01-01',
        created_at: '2024-01-01T00:00:00Z',
        updated_at: '2024-01-01T00:00:00Z',
      }

      expect(video.youtube_id).toBe('abc123')
      expect(video.title).toBe('Test Video')
    })
  })

  describe('Playlist interface', () => {
    it('should accept valid Playlist object', () => {
      const playlist: Playlist = {
        id: 1,
        title: 'Test Playlist',
        youtube_playlist_id: 'PLtest123',
        description: 'Test description',
        thumbnail_url: 'https://example.com/thumb.jpg',
        video_count: 5,
        created_at: '2024-01-01T00:00:00Z',
        updated_at: '2024-01-01T00:00:00Z',
      }

      expect(playlist.youtube_playlist_id).toBe('PLtest123')
      expect(playlist.video_count).toBe(5)
    })
  })
})
