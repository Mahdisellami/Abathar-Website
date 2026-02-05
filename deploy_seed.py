"""
Deployment Seed Script - Run this once to populate Supabase

Usage:
1. Install psycopg2: pip install psycopg2-binary
2. Replace DATABASE_URL with your Supabase connection string
3. Run: python deploy_seed.py
"""

import psycopg2
from datetime import date

# REPLACE THIS with your Supabase connection string
DATABASE_URL = "postgresql://postgres:[YOUR-PASSWORD]@db.xxx.supabase.co:5432/postgres"

def seed_database():
    print("Connecting to Supabase...")
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    # Check if already seeded
    cur.execute("SELECT COUNT(*) FROM biography")
    if cur.fetchone()[0] > 0:
        print("Database already seeded!")
        return

    print("Seeding biography...")
    cur.execute("""
        INSERT INTO biography (name, title, bio_text, education, achievements, current_roles, discography)
        VALUES (
            'Abathar Kmash',
            'Oud Player | Music Pedagogue | Composer | Transcultural Musician',
            'Born in 1987 in As-Suwaida, Syria, Abathar Kmash is an oud and cello performer who began his musical career self-taught before pursuing formal training.

From 2010 to 2014, he studied oud and cello at the Higher Music Institute in Damascus. Currently, he is pursuing an M.A. in Music.World – Cultural Diversity in Musical Education at Hildesheim University.

As an oud and cello player, composer, and artistic director of intercultural music projects, Abathar has established himself as a significant voice in transcultural music. From 2018 to February 2025, he served as an instructor at the Freien Musikzentrum München, teaching oud, cello, and Arabic music theory. He currently teaches oud at Hildesheim University.

Abathar has founded and co-founded multiple ensembles including Ogaro Ensemble, Jisr, Met in Munich, and A.E.R.A Qualität. His work spans premiere performances, such as "Prayers – Gebete aus der Hölle des Krieges" (2019) in Munich, and collaborations with renowned orchestras including Philharmonie Orchester des Staatstheaters Cottbus and Bayerische Philharmonie.

He has performed at prestigious venues including Gasteig HP8, Konzerthaus Berlin and Wien, and Cuvilliés Theater, working with internationally recognized artists such as Konstantin Wecker and Hani Seblini. His recordings feature collaborations with World.Wide.Wig, Embryo, and other ensembles.',
            '[{"period": "Current", "institution": "Hildesheim University", "degree": "M.A. in Music.World – Cultural Diversity in Musical Education"}, {"period": "2010-2014", "institution": "Higher Music Institute in Damascus", "degree": "Oud and Cello studies"}, {"period": "Before 2010", "institution": "Self-taught", "degree": "Began musical career"}]'::jsonb,
            '["Premiered ''Prayers – Gebete aus der Hölle des Krieges'' (2019) in Munich", "Performed with Philharmonie Orchester des Staatstheaters Cottbus", "Performed with Bayerische Philharmonie", "Performed at Gasteig HP8, Konzerthaus Berlin and Wien, Cuvilliés Theater", "Collaborated with Konstantin Wecker and Hani Seblini", "Former instructor at Freien Musikzentrum München (2018-2025)"]'::jsonb,
            '["Oud instructor at Hildesheim University", "Oud and cello performer", "Composer", "Artistic director of intercultural music projects", "Founder of Ogaro Ensemble"]'::jsonb,
            '["World.Wide.Wig", "Embryo collaborations", "Various ensemble recordings"]'::jsonb
        )
    """)

    print("Seeding events...")
    events = [
        ('Ogaro Ensemble', '2026-01-22', '19:30', 'Stadtstadel Kempten', 'Kempten', None, 'Ogaro Ensemble', 'concert', False),
        ('All that Music (OMOPO)', '2026-02-22', '20:00', 'Freies Musikzentrum München', 'München', None, None, 'concert', False),
        ('Alfulimux, der Wüstenfuchs', '2026-03-15', '16:00', 'Gasteig HP8', 'München', "Children's concert", None, "children's concert", False),
        ('Alfulimux, der Wüstenfuchs', '2026-03-16', '10:00', 'Gasteig HP8', 'München', "Children's concert", None, "children's concert", False),
        ('Alfulimux, der Wüstenfuchs', '2026-03-22', '15:00', 'Schwörsaal im Waaghaus', 'Ravensburg', "Children's concert", None, "children's concert", False),
        ('Alfulimux, der Wüstenfuchs', '2026-03-23', '10:00', 'Schwörsaal im Waaghaus', 'Ravensburg', "Children's concert", None, "children's concert", False),
        ('Met in Munich', '2026-04-10', None, 'Tresor Vinum', 'München', None, 'Met in Munich', 'concert', False),
        ('Ogaro Ensemble with Oriental Dance', '2026-05-17', '20:00', 'Gasteig HP8', 'München', 'Ogaro Ensemble with oriental dance performance', 'Ogaro Ensemble', 'concert', False),
        ('Ogaro Ensemble', '2026-08-01', None, '', 'Graz', None, 'Ogaro Ensemble', 'concert', False),
        ('Met in Munich', '2026-10-17', None, '', 'Kitzingen', None, 'Met in Munich', 'concert', False),
    ]

    for event in events:
        cur.execute("""
            INSERT INTO events (title, date, time, venue, location, description, ensemble_name, event_type, is_past)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, event)

    print("Seeding ensemble...")
    cur.execute("""
        INSERT INTO ensembles (name, description, formation_year, musical_style, vision, contact_email, contact_phone, members, highlights)
        VALUES (
            'Ogaro Ensemble',
            'The Ogaro Ensemble was established in 2017 by Syrian oud player Abathar Kmash in Munich. The group creates a magical combination from different nationalities that produces distinctive music blending traditional and contemporary pieces.

The ensemble performs a fusion of Eastern Mediterranean and Balkan music, drawing influences from regions spanning North Macedonia through the Black Sea to Armenia. Their repertoire includes Greek rembetiko and Turkish dance music, taking audiences on a musical journey from Damascus through Istanbul and Alexandria to Baghdad.

The ensemble has performed at significant venues including the European Championships 2022 in Munich and the Frauenhofer Theater (2023), plus various Munich festivals like Olympiasee and Sound of Munich Now.',
            2017,
            'Eastern Mediterranean and Balkan music fusion, incorporating Greek rembetiko and Turkish dance music. A blend of traditional and contemporary pieces.',
            'A magical combination from different nationalities producing distinctive music that takes audiences on a musical journey from Damascus through Istanbul and Alexandria to Baghdad.',
            'ogaro.ensemble@gmail.com',
            '+4917620360789',
            '[{"name": "Abathar Kmash", "instrument": "Oud, Handpan", "origin": "Syria", "role": "Founder"}, {"name": "Eleanna Pitsikaki", "instrument": "Qanun", "origin": "Greece"}, {"name": "Wilbert Pepper", "instrument": "Contrabass, Electric Bass", "origin": "Venezuela"}, {"name": "Ludwig Himpsl", "instrument": "Darbuka, Riq, Davul", "origin": "Germany"}, {"name": "Stefan Noelle", "instrument": "Frame drums, Riq, Cajon", "origin": "Germany"}]'::jsonb,
            '["European Championships 2022 in Munich", "Frauenhofer Theater (2023)", "Olympiasee Festival", "Sound of Munich Now"]'::jsonb
        )
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Database seeded successfully!")
    print("\nNext steps:")
    print("1. Deploy backend to Render.com")
    print("2. Deploy frontend to Vercel")

if __name__ == "__main__":
    if "[YOUR-PASSWORD]" in DATABASE_URL:
        print("❌ ERROR: Please update DATABASE_URL with your Supabase connection string!")
        print("Find it in Supabase → Settings → Database → Connection string")
    else:
        seed_database()
