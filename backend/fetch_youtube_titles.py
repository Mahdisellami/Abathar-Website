"""
Fetch real YouTube video titles using YouTube Data API

Requirements:
pip install google-api-python-client

Usage:
export YOUTUBE_API_KEY="your_api_key_here"
python fetch_youtube_titles.py
"""

import os
from googleapiclient.discovery import build

# YouTube video IDs from seed_data.py
VIDEO_IDS = [
    "epDFxlaZr2E",  # Performance 1
    "iWD9gBHF7AM",  # Performance 2
    "1owBIrX_HM8",  # Performance 3
    "Dl_41_lVyC0",  # Performance 4
    "rqRhxFUVSI0",  # Performance 5
    "Dq2Rci_863M",  # Performance 6
    "iPpeWDRrG6g",  # Performance 7
    "azewXlAacgs",  # Performance 8
    "y75WXHucsTU",  # Performance 9
    "n9bspXnxS_0",  # Performance 10
    "aRN-OKOo3QA",  # Performance 11
    "XUkGC5VL1nk",  # Performance 12
    "ot5v9oB6p10",  # Performance 13
    "KEtNJXYVb4E",  # Performance 14
    "Cwe87O0d1Pk",  # Performance 15
    "oVkXFRFCm8A",  # Performance 16
    "KQzSVmO3Ubk",  # Performance 17
    "HYPPuBZg5RY",  # Performance 18
    "ikvQWJN-ysE",  # Performance 19
    "OvZUq_6X2NU",  # Performance 20
    "B68UAWuT_cU",  # Performance 21
    "07Y4GA-RdRM",  # Performance 22
    "qJxQii397wM",  # Performance 23
    "vQ84dyE5jUY",  # Performance 24
]


def fetch_video_titles():
    """Fetch video titles from YouTube Data API"""
    api_key = os.getenv("YOUTUBE_API_KEY")

    if not api_key:
        print("ERROR: YOUTUBE_API_KEY environment variable not set")
        print("\nTo get an API key:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create a new project or select existing")
        print("3. Enable YouTube Data API v3")
        print("4. Create credentials (API key)")
        print("5. Export: export YOUTUBE_API_KEY='your_key_here'")
        return

    youtube = build('youtube', 'v3', developerKey=api_key)

    # Fetch video details in batches (max 50 per request)
    batch_size = 50
    all_videos = []

    for i in range(0, len(VIDEO_IDS), batch_size):
        batch = VIDEO_IDS[i:i + batch_size]

        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=','.join(batch)
        )
        response = request.execute()
        all_videos.extend(response.get('items', []))

    # Print results
    print("=" * 80)
    print("YouTube Video Titles")
    print("=" * 80)
    print()

    for idx, video in enumerate(all_videos, 1):
        video_id = video['id']
        snippet = video['snippet']
        title = snippet['title']
        description = snippet.get('description', '')[:100]  # First 100 chars
        published_at = snippet['publishedAt'][:10]  # Date only

        print(f"{idx}. {title}")
        print(f"   ID: {video_id}")
        print(f"   Published: {published_at}")
        print(f"   Description: {description}...")
        print()

    print("=" * 80)
    print("\nPython dict format for seed_data.py:")
    print("=" * 80)
    print()

    for idx, video in enumerate(all_videos, 1):
        video_id = video['id']
        snippet = video['snippet']
        title = snippet['title'].replace('"', '\\"')  # Escape quotes
        description = snippet.get('description', '').split('\n')[0][:200].replace('"', '\\"')
        published_at = snippet['publishedAt'][:10]

        print(f'    {{')
        print(f'        "title": "{title}",')
        print(f'        "youtube_id": "{video_id}",')
        print(f'        "youtube_url": "https://www.youtube.com/watch?v={video_id}",')
        print(f'        "description": "{description}",')
        print(f'        "category": "performance",')
        print(f'        "is_featured": {str(idx <= 3).lower()},')
        print(f'        "display_order": {idx},')
        print(f'        "published_date": date({published_at[:4]}, {int(published_at[5:7])}, {int(published_at[8:10])})')
        print(f'    }},')


if __name__ == "__main__":
    fetch_video_titles()
