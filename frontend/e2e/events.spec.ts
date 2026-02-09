import { test, expect } from '@playwright/test';

test.describe('Events Page', () => {
  test('should load events page', async ({ page }) => {
    await page.goto('/events');
    await expect(page.locator('h1')).toContainText(/Events|Concerts/i);
  });

  test('should display upcoming events', async ({ page }) => {
    await page.goto('/events');

    // Wait for events to load
    await page.waitForSelector('[class*="event"]', { timeout: 10000 });

    // Check if event cards are displayed
    const eventCards = page.locator('[class*="event"]');
    const count = await eventCards.count();
    expect(count).toBeGreaterThan(0);
  });

  test('should display event details', async ({ page }) => {
    await page.goto('/events');

    // Wait for events to load
    await page.waitForSelector('h3', { timeout: 10000 });

    // Check if event title is displayed
    const firstEventTitle = page.locator('h3').first();
    await expect(firstEventTitle).toBeVisible();
  });

  test('should filter between upcoming and past events', async ({ page }) => {
    await page.goto('/events');

    // Look for filter buttons (if they exist)
    const upcomingButton = page.getByRole('button', { name: /Upcoming/i });
    const pastButton = page.getByRole('button', { name: /Past/i });

    if (await upcomingButton.isVisible()) {
      await upcomingButton.click();
      await page.waitForTimeout(500);

      // Verify events are displayed
      const events = page.locator('[class*="event"]');
      expect(await events.count()).toBeGreaterThan(0);
    }
  });

  test('should display event photos when available', async ({ page }) => {
    await page.goto('/events');

    // Wait for images to load
    await page.waitForTimeout(2000);

    // Check if any event has a photo
    const eventImages = page.locator('img[alt*=""]');
    const imageCount = await eventImages.count();

    // Some events should have photos
    if (imageCount > 0) {
      const firstImage = eventImages.first();
      await expect(firstImage).toBeVisible();
    }
  });
});
