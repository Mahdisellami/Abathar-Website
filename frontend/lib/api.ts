import axios from 'axios';
import type { Event, Bio, Ensemble, ContactInfo } from './types';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export async function getEvents(filterType: 'all' | 'upcoming' | 'past' = 'all'): Promise<Event[]> {
  const response = await api.get('/api/events', {
    params: { filter_type: filterType },
  });
  return response.data;
}

export async function getEvent(id: number): Promise<Event> {
  const response = await api.get(`/api/events/${id}`);
  return response.data;
}

export async function getBio(): Promise<Bio> {
  const response = await api.get('/api/bio');
  return response.data;
}

export async function getEnsemble(): Promise<Ensemble> {
  const response = await api.get('/api/ensemble');
  return response.data;
}

export async function getContactInfo(): Promise<ContactInfo> {
  const response = await api.get('/api/contact-info');
  return response.data;
}

export async function sendContactMessage(data: {
  name: string;
  email: string;
  message: string;
}): Promise<{ message: string }> {
  const response = await api.post('/api/contact', data);
  return response.data;
}
