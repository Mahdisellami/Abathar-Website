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
    year: string;
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
