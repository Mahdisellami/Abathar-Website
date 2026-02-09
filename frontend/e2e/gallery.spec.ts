import { test, expect } from '@playwright/test';

test.describe('Gallery Page', () => {
  test('should load gallery page', async ({ page }) => {
    await page.goto('/gallery');
    await expect(page.locator('h1')).toContainText(/Photo Gallery|Gallery/i);
  });

  test('should display filter buttons', async ({ page }) => {
    await page.goto('/gallery');

    // Check for filter buttons
    const allButton = page.getByRole('button', { name: /All/i });
    const portraitsButton = page.getByRole('button', { name: /Portraits/i });
    const performancesButton = page.getByRole('button', { name: /Performances/i });

    await expect(allButton).toBeVisible();
    await expect(portraitsButton).toBeVisible();
    await expect(performancesButton).toBeVisible();
  });

  test('should filter photos by category', async ({ page }) => {
    await page.goto('/gallery');

    // Click on Portraits filter
    await page.click('button:has-text("Portraits")');

    // Wait for filter to apply
    await page.waitForTimeout(500);

    // Verify that images are displayed
    const images = page.locator('img');
    const count = await images.count();
    expect(count).toBeGreaterThan(0);
  });

  test('should open lightbox on image click', async ({ page }) => {
    await page.goto('/gallery');

    // Click on first image
    const firstImage = page.locator('img').first();
    await firstImage.click();

    // Wait for lightbox to appear
    await page.waitForTimeout(500);

    // Check if lightbox modal is visible
    // This depends on how the lightbox is implemented
    // Adjust selector based on actual implementation
    const lightbox = page.locator('[role="dialog"]').or(page.locator('.lightbox'));
    await expect(lightbox).toBeVisible();
  });

  test('should display photo credits', async ({ page }) => {
    await page.goto('/gallery');

    // Scroll to footer
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));

    // Check for photo credits
    await expect(page.getByText(/Marie Lehmann/i)).toBeVisible();
  });
});
