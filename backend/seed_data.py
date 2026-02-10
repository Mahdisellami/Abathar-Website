"""
Database Seed Script

This script populates the database with initial content from the original website.
Run this after creating the database tables.

Usage:
    python seed_data.py
"""

from datetime import date
from app.database import SessionLocal
from app.models.bio import Bio
from app.models.event import Event
from app.models.ensemble import Ensemble
from app.models.video import Video
from app.models.playlist import Playlist


def seed_bio(db):
    """Seed biography data"""
    print("Seeding biography...")

    # Check if bio already exists
    existing_bio = db.query(Bio).first()
    if existing_bio:
        print("Biography already exists. Skipping...")
        return

    bio = Bio(
        name="Abathar Kmash",
        title="Oud Player | Music Pedagogue | Composer | Transcultural Musician",
        bio_text="""Born in 1987 in As-Suwaida, Syria, Abathar Kmash is an oud and cello performer who began his musical career self-taught before pursuing formal training.

From 2010 to 2014, he studied oud and cello at the Higher Music Institute in Damascus. Currently, he is pursuing an M.A. in Music.World – Cultural Diversity in Musical Education at Hildesheim University.

As an oud and cello player, composer, and artistic director of intercultural music projects, Abathar has established himself as a significant voice in transcultural music. From 2018 to February 2025, he served as an instructor at the Freien Musikzentrum München, teaching oud, cello, and Arabic music theory. He currently teaches oud at Hildesheim University.

Abathar has founded and co-founded multiple ensembles including Ogaro Ensemble, Jisr, Met in Munich, and A.E.R.A Qualität. His work spans premiere performances, such as "Prayers – Gebete aus der Hölle des Krieges" (2019) in Munich, and collaborations with renowned orchestras including Philharmonie Orchester des Staatstheaters Cottbus and Bayerische Philharmonie.

He has performed at prestigious venues including Gasteig HP8, Konzerthaus Berlin and Wien, and Cuvilliés Theater, working with internationally recognized artists such as Konstantin Wecker and Hani Seblini. His recordings feature collaborations with World.Wide.Wig, Embryo, and other ensembles.""",
        education=[
            {
                "period": "Current",
                "institution": "Hildesheim University",
                "degree": "M.A. in Music.World – Cultural Diversity in Musical Education"
            },
            {
                "period": "2010-2014",
                "institution": "Higher Music Institute in Damascus",
                "degree": "Oud and Cello studies"
            },
            {
                "period": "Before 2010",
                "institution": "Self-taught",
                "degree": "Began musical career"
            }
        ],
        current_roles=[
            "Oud instructor at Hildesheim University",
            "Oud and cello performer",
            "Composer",
            "Artistic director of intercultural music projects",
            "Founder of Ogaro Ensemble"
        ],
        achievements=[
            "Premiered 'Prayers – Gebete aus der Hölle des Krieges' (2019) in Munich",
            "Performed with Philharmonie Orchester des Staatstheaters Cottbus",
            "Performed with Bayerische Philharmonie",
            "Performed at Gasteig HP8, Konzerthaus Berlin and Wien, Cuvilliés Theater",
            "Collaborated with Konstantin Wecker and Hani Seblini",
            "Former instructor at Freien Musikzentrum München (2018-2025)"
        ],
        discography=[
            {
                "title": "World.Wide.Wig",
                "year": "2023",
                "role": "Oud, Composer"
            },
            {
                "title": "Embryo Collaborations",
                "year": "2022",
                "role": "Oud, Cello"
            },
            {
                "title": "Ogaro Ensemble Recordings",
                "year": "2017-present",
                "role": "Oud, Artistic Director"
            }
        ]
    )

    db.add(bio)
    db.commit()
    print("Biography seeded successfully!")


def seed_events(db):
    """Seed events data"""
    print("Seeding events...")

    # Check if events already exist
    existing_events = db.query(Event).count()
    if existing_events > 0:
        print(f"{existing_events} events already exist. Skipping...")
        return

    events = [
        # Past Events with Photos
        Event(
            title="Sound of Munich Now 2021",
            date=date(2021, 8, 14),
            time="20:00",
            venue="Olympiapark",
            location="München",
            description="Ogaro Ensemble performance at Sound of Munich Now Festival",
            ensemble_name="Ogaro Ensemble",
            event_type="festival",
            photo_url="/images/performances/performance-07.webp",
            is_past=True
        ),
        Event(
            title="European Championships 2022 Opening",
            date=date(2022, 8, 17),
            time="19:00",
            venue="Olympiapark",
            location="München",
            description="Ogaro Ensemble performance at European Championships 2022 opening ceremony",
            ensemble_name="Ogaro Ensemble",
            event_type="festival",
            photo_url="/images/performances/performance-08.webp",
            is_past=True
        ),
        Event(
            title="Sound of Munich Now 2023",
            date=date(2023, 7, 15),
            time="21:00",
            venue="Olympiapark",
            location="München",
            description="Ogaro Ensemble performance at Sound of Munich Now Festival",
            ensemble_name="Ogaro Ensemble",
            event_type="festival",
            photo_url="/images/hero-performance.webp",
            is_past=True
        ),
        # 2026 Upcoming Events
        Event(
            title="Ogaro Ensemble",
            date=date(2026, 1, 22),
            time="19:30",
            venue="Stadtstadel Kempten",
            location="Kempten",
            ensemble_name="Ogaro Ensemble",
            event_type="concert",
            is_past=False
        ),
        Event(
            title="All that Music (OMOPO)",
            date=date(2026, 2, 22),
            time="20:00",
            venue="Freies Musikzentrum München",
            location="München",
            event_type="concert",
            is_past=False
        ),
        Event(
            title="Alfulimux, der Wüstenfuchs",
            date=date(2026, 3, 15),
            time="16:00",
            venue="Gasteig HP8",
            location="München",
            description="Children's concert",
            event_type="children's concert",
            is_past=False
        ),
        Event(
            title="Alfulimux, der Wüstenfuchs",
            date=date(2026, 3, 16),
            time="10:00",
            venue="Gasteig HP8",
            location="München",
            description="Children's concert",
            event_type="children's concert",
            is_past=False
        ),
        Event(
            title="Alfulimux, der Wüstenfuchs",
            date=date(2026, 3, 22),
            time="15:00",
            venue="Schwörsaal im Waaghaus",
            location="Ravensburg",
            description="Children's concert",
            event_type="children's concert",
            is_past=False
        ),
        Event(
            title="Alfulimux, der Wüstenfuchs",
            date=date(2026, 3, 23),
            time="10:00",
            venue="Schwörsaal im Waaghaus",
            location="Ravensburg",
            description="Children's concert",
            event_type="children's concert",
            is_past=False
        ),
        Event(
            title="Met in Munich",
            date=date(2026, 4, 10),
            time="",
            venue="Tresor Vinum",
            location="München",
            ensemble_name="Met in Munich",
            event_type="concert",
            is_past=False
        ),
        Event(
            title="Ogaro Ensemble with Oriental Dance",
            date=date(2026, 5, 17),
            time="20:00",
            venue="Gasteig HP8",
            location="München",
            description="Ogaro Ensemble with oriental dance performance",
            ensemble_name="Ogaro Ensemble",
            event_type="concert",
            is_past=False
        ),
        Event(
            title="Ogaro Ensemble",
            date=date(2026, 8, 1),
            time="",
            venue="",
            location="Graz",
            ensemble_name="Ogaro Ensemble",
            event_type="concert",
            is_past=False
        ),
        Event(
            title="Met in Munich",
            date=date(2026, 10, 17),
            time="",
            venue="",
            location="Kitzingen",
            ensemble_name="Met in Munich",
            event_type="concert",
            is_past=False
        ),
    ]

    db.add_all(events)
    db.commit()
    print(f"Seeded {len(events)} events successfully!")


def seed_ensemble(db):
    """Seed ensemble data"""
    print("Seeding ensemble...")

    # Check if ensemble already exists
    existing_ensemble = db.query(Ensemble).first()
    if existing_ensemble:
        print("Ensemble already exists. Skipping...")
        return

    ensemble = Ensemble(
        name="Ogaro Ensemble",
        description="""The Ogaro Ensemble was established in 2017 by Syrian oud player Abathar Kmash in Munich. The group creates a magical combination from different nationalities that produces distinctive music blending traditional and contemporary pieces.

The ensemble performs a fusion of Eastern Mediterranean and Balkan music, drawing influences from regions spanning North Macedonia through the Black Sea to Armenia. Their repertoire includes Greek rembetiko and Turkish dance music, taking audiences on a musical journey from Damascus through Istanbul and Alexandria to Baghdad.

The ensemble has performed at significant venues including the European Championships 2022 in Munich and the Frauenhofer Theater (2023), plus various Munich festivals like Olympiasee and Sound of Munich Now.""",
        formation_year=2017,
        musical_style="Eastern Mediterranean and Balkan music fusion, incorporating Greek rembetiko and Turkish dance music. A blend of traditional and contemporary pieces.",
        vision="A magical combination from different nationalities producing distinctive music that takes audiences on a musical journey from Damascus through Istanbul and Alexandria to Baghdad.",
        contact_email="ogaro.ensemble@gmail.com",
        contact_phone="+4917620360789",
        members=[
            {
                "name": "Abathar Kmash",
                "instrument": "Oud, Handpan",
                "bio": "Founder from Syria. Oud player and artistic director of the ensemble."
            },
            {
                "name": "Eleanna Pitsikaki",
                "instrument": "Qanun",
                "bio": "Qanun player from Greece, bringing Mediterranean melodies to the ensemble."
            },
            {
                "name": "Wilbert Pepper",
                "instrument": "Contrabass, Electric Bass",
                "bio": "Venezuelan bassist providing the rhythmic foundation."
            },
            {
                "name": "Ludwig Himpsl",
                "instrument": "Darbuka, Riq, Davul",
                "bio": "German percussionist specializing in Middle Eastern rhythms."
            },
            {
                "name": "Stefan Noelle",
                "instrument": "Frame drums, Riq, Cajon",
                "bio": "German percussionist adding diverse rhythmic textures."
            }
        ],
        highlights=[
            "European Championships 2022 in Munich",
            "Frauenhofer Theater (2023)",
            "Olympiasee Festival",
            "Sound of Munich Now"
        ]
    )

    db.add(ensemble)
    db.commit()
    print("Ensemble seeded successfully!")


def seed_videos(db):
    """Seed video data"""
    print("Seeding videos...")

    # Check if videos already exist
    existing_count = db.query(Video).count()
    if existing_count > 0:
        print(f"{existing_count} videos already exist. Skipping...")
        return

    # Real videos from Abathar Kmash's YouTube channel
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
            "title": "Neue Version von meinem Stück \"Serap\" mit Embryo",
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
            "title": "Abathar Kmash \"Warten - إنتظار\"",
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
            "title": "Abathar Kmash Oud \"Bakhtsha kurd No.1\" - Adel Geray",
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
            "title": "Abathar Kmash Oud \"Bakhtsha kurd No.2\" - Adel Geray",
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

    for video_data in videos_data:
        video = Video(**video_data)
        db.add(video)

    db.commit()
    print(f"Seeded {len(videos_data)} videos successfully!")


def seed_playlists(db):
    """Seed playlists data"""
    print("Seeding playlists...")

    # Check if playlists already exist
    existing_count = db.query(Playlist).count()
    if existing_count > 0:
        print(f"{existing_count} playlists already exist. Skipping...")
        return

    # Playlists from Abathar Kmash's YouTube channel
    # Note: Playlist titles need to be manually updated from YouTube
    # Thumbnail URLs use the first video in each playlist for preview
    playlists_data = [
        {
            "title": "Ogaro Ensemble",
            "playlist_id": "PLsEOqTNaP9YIqemlmrUtcyT_4hDVQxYmD",
            "playlist_url": "https://www.youtube.com/playlist?list=PLsEOqTNaP9YIqemlmrUtcyT_4hDVQxYmD",
            "description": "Performances by Ogaro Ensemble featuring Abathar Kmash",
            "video_count": 2,
            "thumbnail_url": "https://img.youtube.com/vi/vQ84dyE5jUY/hqdefault.jpg",  # First video in playlist
            "is_featured": True,
            "display_order": 1,
        },
        {
            "title": "Sufi, Ancient to Balkan",
            "playlist_id": "PLsEOqTNaP9YJECY4kMURaQcgk9oWvsd3z",
            "playlist_url": "https://www.youtube.com/playlist?list=PLsEOqTNaP9YJECY4kMURaQcgk9oWvsd3z",
            "description": "Musical journey from Sufi traditions to Balkan sounds",
            "video_count": 4,
            "thumbnail_url": "https://img.youtube.com/vi/rqRhxFUVSI0/hqdefault.jpg",  # First video in playlist
            "is_featured": True,
            "display_order": 2,
        },
        {
            "title": "European Championships Munich 2022",
            "playlist_id": "PLsEOqTNaP9YJ2DKbwmaFbO3F7EJKJQZ92",
            "playlist_url": "https://www.youtube.com/playlist?list=PLsEOqTNaP9YJ2DKbwmaFbO3F7EJKJQZ92",
            "description": "Performances at European Championships Munich 2022",
            "video_count": 6,
            "thumbnail_url": "https://img.youtube.com/vi/n9bspXnxS_0/hqdefault.jpg",  # First video in playlist
            "is_featured": True,
            "display_order": 3,
        },
        {
            "title": "Met in Munich",
            "playlist_id": "PLsEOqTNaP9YIEtK6UT_zC27PRlWWb83Jo",
            "playlist_url": "https://www.youtube.com/playlist?list=PLsEOqTNaP9YIEtK6UT_zC27PRlWWb83Jo",
            "description": "Musical encounters and collaborations in Munich",
            "video_count": 3,
            "thumbnail_url": "https://img.youtube.com/vi/aRN-OKOo3QA/hqdefault.jpg",  # First video in playlist
            "is_featured": False,
            "display_order": 4,
        },
        {
            "title": "Import Export",
            "playlist_id": "PLsEOqTNaP9YKRehqZhZ6Y8RX_DkVhl54g",
            "playlist_url": "https://www.youtube.com/playlist?list=PLsEOqTNaP9YKRehqZhZ6Y8RX_DkVhl54g",
            "description": "Cross-cultural musical exchanges and performances",
            "video_count": 1,
            "thumbnail_url": "https://img.youtube.com/vi/azewXlAacgs/hqdefault.jpg",  # First video in playlist
            "is_featured": False,
            "display_order": 5,
        },
    ]

    for playlist_data in playlists_data:
        playlist = Playlist(**playlist_data)
        db.add(playlist)

    db.commit()
    print(f"Seeded {len(playlists_data)} playlists successfully!")


def seed_database():
    """Seed database function that can be called from anywhere"""
    print("=" * 50)
    print("Starting database seeding...")
    print("=" * 50)

    db = SessionLocal()

    try:
        seed_bio(db)
        seed_events(db)
        seed_ensemble(db)
        seed_videos(db)
        seed_playlists(db)

        print("=" * 50)
        print("Database seeding completed successfully!")
        print("=" * 50)

    except Exception as e:
        print(f"Error during seeding: {e}")
        db.rollback()
        raise
    finally:
        db.close()


def main():
    """Main entry point when run as script"""
    seed_database()


if __name__ == "__main__":
    main()
