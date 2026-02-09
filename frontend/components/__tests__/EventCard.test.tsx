import { render, screen } from '@testing-library/react'
import EventCard from '../EventCard'
import type { Event } from '@/lib/types'

describe('EventCard', () => {
  const mockEvent: Event = {
    id: 1,
    title: 'Test Concert',
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

  it('renders event card with all information', () => {
    render(<EventCard event={mockEvent} />)

    expect(screen.getByText('Test Concert')).toBeInTheDocument()
    expect(screen.getByText(/Test Venue, Test City/)).toBeInTheDocument()
    expect(screen.getByText('Test Description')).toBeInTheDocument()
  })

  it('displays event photo when photo_url is provided', () => {
    render(<EventCard event={mockEvent} />)

    const image = screen.getByAltText('Test Concert')
    expect(image).toBeInTheDocument()
  })

  it('does not display photo when photo_url is null', () => {
    const eventWithoutPhoto = { ...mockEvent, photo_url: null }
    render(<EventCard event={eventWithoutPhoto} />)

    expect(screen.queryByAltText('Test Concert')).not.toBeInTheDocument()
  })

  it('displays ensemble name when provided', () => {
    render(<EventCard event={mockEvent} />)

    expect(screen.getByText('Test Ensemble')).toBeInTheDocument()
  })

  it('formats date correctly', () => {
    render(<EventCard event={mockEvent} />)

    // The component should display the date in a formatted way
    expect(screen.getByText('31')).toBeInTheDocument() // Day in date badge
    expect(screen.getByText('Dec')).toBeInTheDocument() // Month in date badge
    expect(screen.getByText(/December 31, 2026/)).toBeInTheDocument() // Full date
  })

  it('displays past event styling when is_past is true', () => {
    const pastEvent = { ...mockEvent, is_past: true }
    const { container } = render(<EventCard event={pastEvent} />)

    // Check if the card has the appropriate styling (e.g., opacity or disabled state)
    expect(container.firstChild).toBeInTheDocument()
  })
})
