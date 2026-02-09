export interface Event {
  id: number;
  title: string;
  date: string;
  time?: string;
  venue: string;
  location: string;
  description?: string;
  ensemble_name?: string;
  event_type?: string;
  photo_url?: string;
  is_past: boolean;
}

export interface Bio {
  id: number;
  name: string;
  title: string;
  bio_text: string;
  education: Array<{
    degree: string;
    institution: string;
    period: string;
  }>;
  achievements: string[];
  current_roles: string[];
  discography: Array<{
    title: string;
    year: string;
    role: string;
  }>;
}

export interface Ensemble {
  id: number;
  name: string;
  description: string;
  formation_year: number;
  musical_style: string;
  vision: string;
  contact_email?: string;
  contact_phone?: string;
  members: Array<{
    name: string;
    instrument: string;
    bio: string;
  }>;
  highlights: string[];
}

export interface ContactInfo {
  name: string;
  email: string;
  phone: string;
  address: string;
  ensemble_email: string;
}

export interface Video {
  id: number;
  title: string;
  youtube_id: string;
  youtube_url: string;
  description?: string;
  thumbnail_url?: string;
  duration?: string;
  published_date?: string;
  category?: string;
  event_id?: number;
  is_featured: boolean;
  display_order: number;
  is_visible: boolean;
  created_at: string;
  updated_at?: string;
}

export interface Playlist {
  id: number;
  title: string;
  playlist_id: string;
  playlist_url: string;
  description?: string;
  thumbnail_url?: string;
  video_count?: number;
  is_featured: boolean;
  display_order: number;
  is_visible: boolean;
  created_at: string;
  updated_at?: string;
}
