"""
Update existing video records with real YouTube IDs

Run this script on Render to update placeholder videos with real IDs
"""

from datetime import date
from app.database import SessionLocal
from app.models.video import Video


def update_videos():
    """Update placeholder video IDs with real ones"""
    db = SessionLocal()

    # Mapping of old placeholder IDs to new real IDs
    video_updates = {
        "PLACEHOLDER_ID_1": "epDFxlaZr2E",
        "PLACEHOLDER_ID_2": "iWD9gBHF7AM",
        "PLACEHOLDER_ID_3": "1owBIrX_HM8",
        "PLACEHOLDER_ID_4": "Dl_41_lVyC0",
    }

    try:
        print("Updating videos with real YouTube IDs...")

        for old_id, new_id in video_updates.items():
            video = db.query(Video).filter(Video.youtube_id == old_id).first()
            if video:
                video.youtube_id = new_id
                video.youtube_url = f"https://www.youtube.com/watch?v={new_id}"
                print(f"✓ Updated {old_id} -> {new_id}")
            else:
                print(f"✗ Video with ID {old_id} not found")

        db.commit()
        print("\n✅ All videos updated successfully!")

    except Exception as e:
        print(f"❌ Error updating videos: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    update_videos()
