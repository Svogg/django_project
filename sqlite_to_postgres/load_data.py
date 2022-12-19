import os
import sqlite3
from contextlib import contextmanager

import psycopg2
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor
from dotenv import load_dotenv, find_dotenv

from pg_saver import PgSaver
from sqlite_extarctor import SqliteExtractor

from data_classes import FilmWork, Genre, Person, GenreFilmWork, PersonFilmWork

load_dotenv(find_dotenv())


@contextmanager
def conn_context(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()


@contextmanager
def pg_conn_context(dsl: dict):
    pg_conn = psycopg2.connect(**dsl, cursor_factory=DictCursor)
    yield pg_conn
    pg_conn.close()


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""

    postgres_saver = PgSaver(pg_conn)
    sqlite_loader = SqliteExtractor(connection)

    for data in sqlite_loader.extract(FilmWork, 'film_work'):

        film_work_record = [record.get_film_work_tuple() for record in data]
        postgres_saver.save_all_film_works(film_work_record)

    for data in sqlite_loader.extract(Genre, 'genre'):

        genre_record = [record.get_genre_tuple() for record in data]
        postgres_saver.save_all_genres(genre_record)

    for data in sqlite_loader.extract(Person, 'person'):

        person_record = [record.get_person_tuple() for record in data]
        postgres_saver.save_all_persons(person_record)

    for data in sqlite_loader.extract(GenreFilmWork, 'genre_film_work'):

        genre_film_work_record = [record.get_genre_film_work_tuple() for record in data]
        postgres_saver.save_all_genre_film_works(genre_film_work_record)

    for data in sqlite_loader.extract(PersonFilmWork, 'person_film_work'):

        person_film_work_record = [record.get_person_film_work_tuple() for record in data]
        postgres_saver.save_all_person_film_works(person_film_work_record)


if __name__ == '__main__':
    dsl = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'options': '-c search_path=content',
    }

    with conn_context('db.sqlite') as sqlite_conn, pg_conn_context(dsl) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
