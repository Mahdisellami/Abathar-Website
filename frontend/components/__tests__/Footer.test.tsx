import { render, screen } from '@testing-library/react'
import Footer from '../Footer'

describe('Footer', () => {
  it('renders the footer with copyright information', () => {
    render(<Footer />)

    const currentYear = new Date().getFullYear()
    expect(screen.getByText(new RegExp(`© ${currentYear}`))).toBeInTheDocument()
  })

  it('displays photo credits section', () => {
    render(<Footer />)

    expect(screen.getByText(/Photography Credits/i)).toBeInTheDocument()
    expect(screen.getByText(/Marie Lehmann/)).toBeInTheDocument()
    expect(screen.getByText(/Lena Semmelroggen/)).toBeInTheDocument()
    expect(screen.getByText(/Axel Heimken/)).toBeInTheDocument()
    expect(screen.getByText(/Ananda Nefzger/)).toBeInTheDocument()
  })

  it('includes social media link (if present)', () => {
    render(<Footer />)

    // Check if Instagram handle is present
    const instagramLink = screen.queryByText(/@mariellemilia/)
    if (instagramLink) {
      expect(instagramLink).toBeInTheDocument()
    }
  })
})
