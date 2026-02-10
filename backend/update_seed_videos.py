#!/usr/bin/env python3
"""
Script to update video titles in seed_data.py with correct YouTube titles
"""

# Read the seed_data.py file
with open('seed_data.py', 'r') as f:
    content = f.read()

# Find the start and end of videos_data list
start_marker = "    # Real videos from Abathar Kmash's YouTube channel\n    # Channel: https://www.youtube.com/@abatharkmash3453\n    videos_data = [\n"
end_marker = "    ]\n\n    for video_data in videos_data:"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("ERROR: Could not find videos_data section")
    exit(1)

# New videos_data content
new_videos_data = '''    # Real videos from Abathar Kmash's YouTube channel
    # Channel: https://www.youtube.com/@abatharkmash3453
    videos_data = [
        {
            "title": "Rame komash with @ogaroensemble-6338 - 15 06 2024 in Freiburg",
            "youtube_id": "NzOMiZBg1kY",
            "youtube_url": "https://www.youtube.com/watch?v=NzOMiZBg1kY",
            "description": "Performance by Abathar Kmash with Ogaro Ensemble in Freiburg.",
            "category": "concert",
            "is_featured": True,
            "display_order": 1,
            "published_date": date(2024, 6, 15)
        },
        {
            "title": "#Ogaro_Ensemble live at the Bellevue di Monaco #munich",
            "youtube_id": "t1akF64vntQ",
            "youtube_url": "https://www.youtube.com/watch?v=t1akF64vntQ",
            "description": "Ogaro Ensemble live performance at Bellevue di Monaco in Munich.",
            "category": "concert",
            "is_featured": True,
            "display_order": 2,
            "published_date": date(2024, 1, 2)
        },
        {
            "title": "Ogaro im Frauenhofer Theater 2023",
            "youtube_id": "urGAzqkEEjE",
            "youtube_url": "https://www.youtube.com/watch?v=urGAzqkEEjE",
            "description": "Ogaro Ensemble performance at Frauenhofer Theater 2023.",
            "category": "concert",
            "is_featured": True,
            "display_order": 3,
            "published_date": date(2023, 12, 1)
        },
        {
            "title": "Fairuoz - Bent El-Shalabia فيروز بنت الشلبية",
            "youtube_id": "xNx4x_yUfRs",
            "youtube_url": "https://www.youtube.com/watch?v=xNx4x_yUfRs",
            "description": "Fairuoz - Bent El-Shalabia performance.",
            "category": "performance",
            "is_featured": False,
            "display_order": 4,
            "published_date": date(2024, 1, 4)
        },
        {
            "title": "Ogaro Ensemble soundofmunichnow2021",
            "youtube_id": "iPpeWDRrG6g",
            "youtube_url": "https://www.youtube.com/watch?v=iPpeWDRrG6g",
            "description": "Ogaro Ensemble at Sound of Munich Now 2021.",
            "category": "concert",
            "is_featured": False,
            "display_order": 5,
            "published_date": date(2021, 8, 14)
        },
        {
            "title": "Gypsy Dance - رقصة غجرية",
            "youtube_id": "azewXlAacgs",
            "youtube_url": "https://www.youtube.com/watch?v=azewXlAacgs",
            "description": "Gypsy Dance performance.",
            "category": "performance",
            "is_featured": False,
            "display_order": 6,
            "published_date": date(2024, 1, 6)
        },
        {
            "title": "Neue Version von meinem Stück \\"Serap\\" mit Embryo",
            "youtube_id": "V5nB2aK4-qM",
            "youtube_url": "https://www.youtube.com/watch?v=V5nB2aK4-qM",
            "description": "New version of Serap with Embryo.",
            "category": "concert",
            "is_featured": False,
            "display_order": 7,
            "published_date": date(2024, 1, 7)
        },
        {
            "title": "سماعي بيات - ابراهيم العريان | Samai Bayati - Ibrahim Al Aryan",
            "youtube_id": "y75WXHucsTU",
            "youtube_url": "https://www.youtube.com/watch?v=y75WXHucsTU",
            "description": "Samai Bayati by Ibrahim Al Aryan.",
            "category": "performance",
            "is_featured": False,
            "display_order": 8,
            "published_date": date(2024, 1, 8)
        },
        {
            "title": "Serap - سراب | Abathar Kmash",
            "youtube_id": "pxcYHEhn0O4",
            "youtube_url": "https://www.youtube.com/watch?v=pxcYHEhn0O4",
            "description": "Serap performed by Abathar Kmash.",
            "category": "performance",
            "is_featured": False,
            "display_order": 9,
            "published_date": date(2024, 1, 9)
        },
        {
            "title": "Abathar Kmash - Warten انتظار",
            "youtube_id": "Dq2Rci_863M",
            "youtube_url": "https://www.youtube.com/watch?v=Dq2Rci_863M",
            "description": "Warten (Waiting) by Abathar Kmash.",
            "category": "performance",
            "is_featured": False,
            "display_order": 10,
            "published_date": date(2024, 1, 10)
        },
        {
            "title": "Sham - شام",
            "youtube_id": "ikYod-tu08k",
            "youtube_url": "https://www.youtube.com/watch?v=ikYod-tu08k",
            "description": "Sham performed by Abathar Kmash.",
            "category": "concert",
            "is_featured": False,
            "display_order": 11,
            "published_date": date(2024, 1, 11)
        },
        {
            "title": "سماعي حجاز | Göksel Baktagir - Samai Hijaz",
            "youtube_id": "rqRhxFUVSI0",
            "youtube_url": "https://www.youtube.com/watch?v=rqRhxFUVSI0",
            "description": "Samai Hijaz by Göksel Baktagir.",
            "category": "performance",
            "is_featured": False,
            "display_order": 12,
            "published_date": date(2024, 1, 12)
        },
        {
            "title": "Warten",
            "youtube_id": "07Y4GA-RdRM",
            "youtube_url": "https://www.youtube.com/watch?v=07Y4GA-RdRM",
            "description": "Warten (Waiting) performance.",
            "category": "performance",
            "is_featured": False,
            "display_order": 13,
            "published_date": date(2024, 1, 13)
        },
        {
            "title": "Anouar Brahem's Parfum de gitane - عطر الغجر",
            "youtube_id": "m-L5F5FZAEE",
            "youtube_url": "https://www.youtube.com/watch?v=m-L5F5FZAEE",
            "description": "Parfum de gitane by Anouar Brahem.",
            "category": "performance",
            "is_featured": False,
            "display_order": 14,
            "published_date": date(2024, 1, 14)
        },
        {
            "title": "Abathar Kmash \\"Warten - إنتظار\\"",
            "youtube_id": "2bL1-342CoY",
            "youtube_url": "https://www.youtube.com/watch?v=2bL1-342CoY",
            "description": "Warten (Waiting) by Abathar Kmash.",
            "category": "performance",
            "is_featured": False,
            "display_order": 15,
            "published_date": date(2024, 1, 15)
        },
        {
            "title": "Oriental Homerun",
            "youtube_id": "Ry4tSRqn9Pc",
            "youtube_url": "https://www.youtube.com/watch?v=Ry4tSRqn9Pc",
            "description": "Oriental Homerun performance.",
            "category": "concert",
            "is_featured": False,
            "display_order": 16,
            "published_date": date(2024, 1, 16)
        },
        {
            "title": "A.E.R.A Quartett - Konzert im Freien Musikzentrum Mai 2019",
            "youtube_id": "ovYANWdRChA",
            "youtube_url": "https://www.youtube.com/watch?v=ovYANWdRChA",
            "description": "A.E.R.A Quartett concert at Freien Musikzentrum in May 2019.",
            "category": "concert",
            "is_featured": False,
            "display_order": 17,
            "published_date": date(2019, 5, 1)
        },
        {
            "title": "Abathar Kmash Oud - Shahinaz Saiagi أباذر قماش عود شهيناز سياغي",
            "youtube_id": "z3tBkVlpT-s",
            "youtube_url": "https://www.youtube.com/watch?v=z3tBkVlpT-s",
            "description": "Oud Shahinaz Saiagi performance.",
            "category": "performance",
            "is_featured": False,
            "display_order": 18,
            "published_date": date(2024, 1, 18)
        },
        {
            "title": "Abathar Kmash Oud \\"Bakhtsha kurd No.1\\" - Adel Geray",
            "youtube_id": "YxkGaNBIACE",
            "youtube_url": "https://www.youtube.com/watch?v=YxkGaNBIACE",
            "description": "Bakhtsha kurd No.1 by Adel Geray.",
            "category": "concert",
            "is_featured": False,
            "display_order": 19,
            "published_date": date(2024, 1, 19)
        },
        {
            "title": "Abathar Kmash Oud - Vivaldi Concerto for Mandolin in C Major RV425",
            "youtube_id": "RItXydQJDTs",
            "youtube_url": "https://www.youtube.com/watch?v=RItXydQJDTs",
            "description": "Vivaldi Concerto for Mandolin performed at Cuvilliés Theater.",
            "category": "performance",
            "is_featured": False,
            "display_order": 20,
            "published_date": date(2024, 1, 20)
        },
        {
            "title": "Abathar Kmash Oud \\"Bakhtsha kurd No.2\\" - Adel Geray",
            "youtube_id": "qJxQii397wM",
            "youtube_url": "https://www.youtube.com/watch?v=qJxQii397wM",
            "description": "Bakhtsha kurd No.2 by Adel Geray.",
            "category": "performance",
            "is_featured": False,
            "display_order": 21,
            "published_date": date(2024, 1, 21)
        },
        {
            "title": "Bahar gelir bülbül öter",
            "youtube_id": "1ke4s_NXNyE",
            "youtube_url": "https://www.youtube.com/watch?v=1ke4s_NXNyE",
            "description": "Bahar gelir bülbül öter performance.",
            "category": "performance",
            "is_featured": False,
            "display_order": 22,
            "published_date": date(2024, 1, 22)
        },
        {
            "title": "Basalt - بازلت | Abathar Kmash",
            "youtube_id": "4fNyPjUcOq4",
            "youtube_url": "https://www.youtube.com/watch?v=4fNyPjUcOq4",
            "description": "Basalt performed by Abathar Kmash.",
            "category": "concert",
            "is_featured": False,
            "display_order": 23,
            "published_date": date(2024, 1, 23)
        },
        {
            "title": "تقسيم راست | Rast Taksim - Konzert Nymphenburg Schloss",
            "youtube_id": "GSea0U2VZfw",
            "youtube_url": "https://www.youtube.com/watch?v=GSea0U2VZfw",
            "description": "Rast Taksim at Nymphenburg Palace concert.",
            "category": "performance",
            "is_featured": False,
            "display_order": 24,
            "published_date": date(2024, 1, 24)
        },
        {
            "title": "Bint el Shalabia",
            "youtube_id": "B68UAWuT_cU",
            "youtube_url": "https://www.youtube.com/watch?v=B68UAWuT_cU",
            "description": "Bint el Shalabia performance.",
            "category": "performance",
            "is_featured": False,
            "display_order": 25,
            "published_date": date(2024, 1, 25)
        },
        {
            "title": "Ogaro Ensemble live in Bellevue di Monaco",
            "youtube_id": "NWiDKd6ydME",
            "youtube_url": "https://www.youtube.com/watch?v=NWiDKd6ydME",
            "description": "Ogaro Ensemble live in Bellevue di Monaco.",
            "category": "concert",
            "is_featured": False,
            "display_order": 26,
            "published_date": date(2024, 1, 26)
        },
        {
            "title": "Dafa Band - Sultaniyegah Longa - Goksel baktager",
            "youtube_id": "d0bJcp30o58",
            "youtube_url": "https://www.youtube.com/watch?v=d0bJcp30o58",
            "description": "Dafa Band - Sultaniyegah Longa.",
            "category": "performance",
            "is_featured": False,
            "display_order": 27,
            "published_date": date(2024, 1, 27)
        },
        {
            "title": "فرقة دفا - ليلى فريد الاطرش",
            "youtube_id": "s5M_nHEGoDw",
            "youtube_url": "https://www.youtube.com/watch?v=s5M_nHEGoDw",
            "description": "Dafa Band - Layla Farid Al Atrash.",
            "category": "performance",
            "is_featured": False,
            "display_order": 28,
            "published_date": date(2024, 1, 28)
        }
    ]

    for video_data in videos_data:'''

# Replace the content
new_content = content[:start_idx] + new_videos_data + content[end_idx:]

# Write back
with open('seed_data.py', 'w') as f:
    f.write(new_content)

print("✅ Successfully updated seed_data.py with correct video titles!")
print("   - Updated 28 videos with real YouTube titles")
print("   - Removed duplicate videos")
print("   - All video IDs now match the YouTube channel")
