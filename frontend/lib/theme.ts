export type Theme = 'modern' | 'classic';

const THEME_KEY = 'abathar-theme';

export function getStoredTheme(): Theme {
  if (typeof window === 'undefined') {
    return 'modern';
  }

  const stored = localStorage.getItem(THEME_KEY);
  return (stored === 'classic' || stored === 'modern') ? stored : 'modern';
}

export function setStoredTheme(theme: Theme): void {
  if (typeof window !== 'undefined') {
    localStorage.setItem(THEME_KEY, theme);
  }
}

export function applyTheme(theme: Theme): void {
  if (typeof window === 'undefined') {
    return;
  }

  if (theme === 'classic') {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
}

export function toggleTheme(currentTheme: Theme): Theme {
  return currentTheme === 'modern' ? 'classic' : 'modern';
}
