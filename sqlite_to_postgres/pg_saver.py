from psycopg2.extras import execute_batch
from datetime import datetime


class PgSaver:
    def __init__(self, pg_conn) -> None:
        self.pg_conn = pg_conn

    def save_all_persons(self, data: list, n: int = 16) -> None:
        with self.pg_conn.cursor() as cur:
            query = """INSERT INTO content.person(
                id, full_name,
                created_at, updated_at
            )
            VALUES (
                %s, %s,
                %s, %s
            )
            ON CONFLICT (id) DO NOTHING; """
            insert_data = [
                (
                    person[0], person[1],
                    person[2], datetime.now()
                ) for person in data
            ]
            execute_batch(cur, query, insert_data, page_size=n)
            self.pg_conn.commit()

    def save_all_film_works(self, data: list, n: int = 16) -> None:
        with self.pg_conn.cursor() as cur:
            query = """INSERT INTO content.film_work(
                id, title, description, 
                creation_date, file_path, rating, 
                type, created_at, updated_at
            )
            VALUES (
                %s, %s, %s,
                %s, %s, %s,
                %s, %s, %s
            )
            ON CONFLICT (id) DO NOTHING; """
            insert_data = [
                (
                    film[0], film[1], film[2],
                    film[3], film[4], film[5],
                    film[6], film[7], film[8]
                ) for film in data
            ]
            execute_batch(cur, query, insert_data, page_size=n)
            self.pg_conn.commit()

    def save_all_genres(self, data: list, n: int = 16) -> None:
        with self.pg_conn.cursor() as cur:
            query = """
            INSERT INTO content.genre(
                id, name,
                description, created_at,
                updated_at
            )
            VALUES (
                %s, %s,
                %s, %s,
                %s
            ) 
            ON CONFLICT (id) DO NOTHING; """
            insert_data = [
                (
                    genre[0], genre[1],
                    genre[2], genre[3],
                    datetime.now()
                ) for genre in data
            ]
            execute_batch(cur, query, insert_data, page_size=n)
            self.pg_conn.commit()

    def save_all_genre_film_works(self, data: list, n: int = 16) -> None:
        with self.pg_conn.cursor() as cur:
            query = """INSERT INTO content.genre_film_work(
            id, film_work_id, 
            genre_id, created_at
            )
            VALUES (
            %s, %s,
            %s, %s
            ) 
            ON CONFLICT (id) DO NOTHING; """
            insert_data = [
                (
                    g[0], g[1],
                    g[2], datetime.now()
                ) for g in data
            ]
            execute_batch(cur, query, insert_data, page_size=n)
            self.pg_conn.commit()

    def save_all_person_film_works(self, data: list, n: int = 16) -> None:
        with self.pg_conn.cursor() as cur:
            query = """INSERT INTO content.person_film_work(
            id, film_work_id, 
            person_id, role,
            created_at
            )
            VALUES (
            %s, %s,
            %s, %s,
            %s
            ) 
            ON CONFLICT (id) DO NOTHING;"""
            insert_data = [
                (
                    p[0], p[1],
                    p[2], p[3],
                    datetime.now()
                ) for p in data
            ]
            execute_batch(cur, query, insert_data, page_size=n)
            self.pg_conn.commit()