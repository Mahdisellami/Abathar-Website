import { test, expect } from '@playwright/test';

test.describe('Homepage', () => {
  test('should load successfully', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/Abathar/);
  });

  test('should display navigation menu', async ({ page }) => {
    await page.goto('/');

    // Check main navigation items
    await expect(page.getByRole('link', { name: 'Home' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Bio' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Events' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Media' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Gallery' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Contact' })).toBeVisible();
  });

  test('should display hero section', async ({ page }) => {
    await page.goto('/');

    // Check for hero image or main content
    const heroSection = page.locator('section').first();
    await expect(heroSection).toBeVisible();
  });

  test('should navigate to Events page', async ({ page }) => {
    await page.goto('/');

    await page.click('a[href="/events"]');
    await expect(page).toHaveURL('/events');
  });

  test('should navigate to Gallery page', async ({ page }) => {
    await page.goto('/');

    await page.click('a[href="/gallery"]');
    await expect(page).toHaveURL('/gallery');
  });
});
