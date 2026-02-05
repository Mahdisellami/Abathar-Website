# Abathar Kmash Website - Frontend

Modern Next.js frontend for the Abathar Kmash music teacher portfolio website.

## Features

- **Next.js 14** with App Router
- **TypeScript** for type safety
- **Tailwind CSS** for styling
- **Dual Theme Support** - Modern & Classic themes with toggle button
- **Responsive Design** - Mobile-first approach
- **Server-Side Rendering** for optimal SEO
- **API Integration** with FastAPI backend

## Pages

- **Home** - Hero section, introduction, featured events
- **Bio** - Complete biography with education and achievements
- **Events** - Upcoming and past events with filtering
- **Ensemble** - Ogaro Ensemble information and members
- **Contact** - Contact information and Impressum

## Prerequisites

- Node.js 18+ and npm
- Backend API running (see backend README)

## Installation

```bash
# Install dependencies
cd frontend
npm install
```

## Configuration

Create a `.env.local` file:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

For production, update the API URL to your deployed backend.

## Development

```bash
# Start development server
npm run dev
```

The frontend will be available at http://localhost:3000

## Build for Production

```bash
# Build optimized production bundle
npm run build

# Start production server
npm start
```

## Theme System

The website includes two themes:

### Modern Theme
- Clean, minimalist design
- Warm color palette (gold, teal, burgundy)
- Large typography
- Smooth animations

### Classic Theme
- Dark background (#1a1a1a)
- Gold accents (#d4af37)
- Traditional look matching original site

Users can toggle between themes using the sun/moon icon in the header. The preference is saved in localStorage.

## Project Structure

```
frontend/
├── app/                  # Next.js 14 App Router
│   ├── layout.tsx        # Root layout
│   ├── page.tsx          # Home page
│   ├── bio/              # Biography page
│   ├── events/           # Events page
│   ├── ensemble/         # Ensemble page
│   └── contact/          # Contact page
├── components/           # React components
│   ├── ThemeProvider.tsx # Theme context provider
│   ├── Header.tsx        # Navigation header
│   ├── Footer.tsx        # Footer component
│   └── EventCard.tsx     # Event display card
├── lib/                  # Utilities
│   ├── api.ts            # API client
│   ├── types.ts          # TypeScript interfaces
│   └── theme.ts          # Theme utilities
├── styles/
│   └── globals.css       # Global styles & Tailwind
└── public/
    └── images/           # Static images
```

## API Integration

The frontend communicates with the FastAPI backend through the API client (`lib/api.ts`):

```typescript
import { getBio, getEvents, getEnsemble, getContactInfo } from '@/lib/api';

// Fetch biography
const bio = await getBio();

// Fetch events (with filter)
const upcomingEvents = await getEvents('upcoming');
const pastEvents = await getEvents('past');

// Fetch ensemble info
const ensemble = await getEnsemble();
```

## Components

### ThemeProvider
Manages theme state and provides theme toggle functionality.

```typescript
import { useTheme } from '@/components/ThemeProvider';

function MyComponent() {
  const { theme, toggleTheme } = useTheme();
  // ...
}
```

### Header
Responsive navigation with mobile menu and theme toggle.

### Footer
Site footer with quick links, contact info, and scroll-to-top button.

### EventCard
Reusable component for displaying event information.

## Styling

Uses Tailwind CSS with custom configuration:

- **Primary colors**: Gold/amber tones
- **Secondary colors**: Teal/cyan
- **Accent colors**: Burgundy/red
- **Fonts**: Inter (sans-serif), Playfair Display (serif)

Custom animations:
- `fade-in` - Fade in effect
- `slide-up` - Slide up with fade

## TypeScript

All components use TypeScript with proper types:

```typescript
interface Bio {
  id: number;
  name: string;
  title: string;
  bio_text: string;
  education: Education[] | null;
  // ...
}
```

See `lib/types.ts` for all type definitions.

## Responsive Design

Breakpoints:
- `sm`: 640px
- `md`: 768px
- `lg`: 1024px
- `xl`: 1280px

Mobile-first approach with responsive utilities:

```tsx
<div className="text-sm md:text-base lg:text-lg">
  Responsive text
</div>
```

## Performance

- **Next.js Image Optimization** for images
- **Server-Side Rendering** for fast initial load
- **Code Splitting** automatic with Next.js
- **Lazy Loading** for below-the-fold content

## SEO

Metadata configured in `app/layout.tsx`:

```typescript
export const metadata = {
  title: 'Abathar Kmash | Oud Player, Music Pedagogue, Composer',
  description: '...',
  keywords: 'oud, music, pedagogue, composer, ...',
  openGraph: { /* ... */ },
}
```

## Deployment

### Vercel (Recommended)

1. Push code to GitHub
2. Import project in Vercel
3. Set environment variable:
   - `NEXT_PUBLIC_API_URL` = your backend URL
4. Deploy

### Other Platforms

```bash
# Build
npm run build

# The output is in .next/ directory
# Deploy .next/ and package.json to your hosting
```

## Troubleshooting

### API Connection Errors

Check that:
1. Backend is running
2. `NEXT_PUBLIC_API_URL` is correct
3. CORS is configured in backend

### Theme Not Persisting

Clear localStorage or check browser console for errors.

### Images Not Loading

Ensure `next.config.js` has correct remote image patterns.

## Future Enhancements

- Contact form implementation
- Image gallery for performances
- Audio/video player for recordings
- Social media integration
- Newsletter signup
- Admin panel for content management

## License

See LICENSE file in project root.
