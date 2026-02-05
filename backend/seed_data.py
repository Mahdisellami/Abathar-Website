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
            "World.Wide.Wig",
            "Embryo collaborations",
            "Various ensemble recordings"
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
                "origin": "Syria",
                "role": "Founder"
            },
            {
                "name": "Eleanna Pitsikaki",
                "instrument": "Qanun",
                "origin": "Greece"
            },
            {
                "name": "Wilbert Pepper",
                "instrument": "Contrabass, Electric Bass",
                "origin": "Venezuela"
            },
            {
                "name": "Ludwig Himpsl",
                "instrument": "Darbuka, Riq, Davul",
                "origin": "Germany"
            },
            {
                "name": "Stefan Noelle",
                "instrument": "Frame drums, Riq, Cajon",
                "origin": "Germany"
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


def main():
    """Main seeding function"""
    print("=" * 50)
    print("Starting database seeding...")
    print("=" * 50)

    db = SessionLocal()

    try:
        seed_bio(db)
        seed_events(db)
        seed_ensemble(db)

        print("=" * 50)
        print("Database seeding completed successfully!")
        print("=" * 50)

    except Exception as e:
        print(f"Error during seeding: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
