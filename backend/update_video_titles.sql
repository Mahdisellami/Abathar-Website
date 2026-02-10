-- SQL script to update video titles in production
-- Run this after getting the correct titles

-- Update featured videos (first 3)
UPDATE videos SET title = 'Sona - سونا' WHERE youtube_id = 'epDFxlaZr2E';
UPDATE videos SET title = 'Sham - شام' WHERE youtube_id = 'iWD9gBHF7AM';
UPDATE videos SET title = 'Warren - انتظار' WHERE youtube_id = '1owBIrX_HM8';

-- Update remaining videos with correct titles
-- NOTE: You need to provide the correct titles for these IDs
UPDATE videos SET title = 'Gypsy Dance - رقصة الغجري' WHERE youtube_id = 'Dl_41_lVyC0';
UPDATE videos SET title = 'Ogaro Ensemble - Sufi Ancient' WHERE youtube_id = 'rqRhxFUVSI0';
UPDATE videos SET title = 'Ogaro im Frauenhofer Theater 2023' WHERE youtube_id = 'Dq2Rci_863M';
UPDATE videos SET title = 'Fairouz - Bent El-Shalabya' WHERE youtube_id = 'iPpeWDRrG6g';
UPDATE videos SET title = '#Ogaro_Ensemble live at the Bellevue of Monaco' WHERE youtube_id = 'azewXlAacgs';
UPDATE videos SET title = 'Ogaro Ensemble soundofmunichNow2021' WHERE youtube_id = 'y75WXHucsTU';

-- For remaining videos, use generic titles until we get real ones
-- UPDATE videos SET title = 'Performance Title' WHERE youtube_id = '...';
