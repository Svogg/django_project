import os
from dotenv import load_dotenv, find_dotenv

import sqlite3
from data_classes import FilmWork, Genre, Person, GenreFilmWork, PersonFilmWork
from pg_saver import PgSaver
from sqlite_extarctor import SqliteExtractor
import psycopg2
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor

load_dotenv(find_dotenv())


def load_from_sqlite(sqlite3_conn: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""

    postgres_saver = PgSaver(pg_conn)

    sqlite3_conn.row_factory = sqlite3.Row
    curs = sqlite3_conn.cursor()
    sqlite_extractor = SqliteExtractor(sqlite3_conn, curs)

    dt_film_work = sqlite_extractor.extract_all(
        'film_work',
        'id, title, description, '
        'creation_date, file_path, rating, '
        'type, created_at, updated_at',
        FilmWork,
    )
    dt_genre = sqlite_extractor.extract_all(
        'genre',
        'id, name, description, '
        'created_at, updated_at',
        Genre
    )
    dt_person = sqlite_extractor.extract_all(
        'person',
        'id, full_name, '
        'created_at, updated_at',
        Person
    )
    dt_genre_film_work = sqlite_extractor.extract_all(
        'genre_film_work',
        'id, film_work_id, '
        'genre_id, created_at',
        GenreFilmWork
    )
    dt_person_film_work = sqlite_extractor.extract_all(
        'person_film_work',
        'id, film_work_id, '
        'person_id, role, '
        'created_at',
        PersonFilmWork
    )

    film_work_record = [record.get_film_work_tuple() for record in dt_film_work]
    genre_record = [record.get_genre_tuple() for record in dt_genre]
    person_record = [record.get_person_tuple() for record in dt_person]
    genre_film_work_record = [record.get_genre_film_work_tuple() for record in dt_genre_film_work]
    person_film_work_record = [record.get_person_film_work_tuple() for record in dt_person_film_work]

    postgres_saver.save_all('film_work',
                            FilmWork.film_work_column,
                            FilmWork.film_work_value,
                            film_work_record)

    postgres_saver.save_all('genre',
                            Genre.genre_column,
                            Genre.genre_value,
                            genre_record)

    postgres_saver.save_all('person',
                            Person.person_column,
                            Person.person_value,
                            person_record)

    postgres_saver.save_all('genre_film_work',
                            GenreFilmWork.genre_film_work_column,
                            GenreFilmWork.genre_film_work_value,
                            genre_film_work_record)

    postgres_saver.save_all('person_film_work',
                            PersonFilmWork.person_film_work_column,
                            PersonFilmWork.person_film_work_value,
                            person_film_work_record)


if __name__ == '__main__':
    dsl = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'options': '-c search_path=content',
    }
    with sqlite3.connect('db.sqlite') as sqlite_conn, psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
