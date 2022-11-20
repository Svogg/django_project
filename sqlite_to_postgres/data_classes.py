import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class FilmWork:
    id: uuid.UUID
    title: str
    description: str
    creation_date: str
    file_path: str
    rating: float
    type: str
    created_at: field(default=datetime.utcnow())
    updated_at: field(default=datetime.utcnow())

    film_work_column: str = '(' \
                            'id, title, description, ' \
                            'creation_date, file_path, rating, ' \
                            'type, created_at, updated_at' \
                            ')'

    film_work_value: str = '(' \
                           '%s, %s, %s, ' \
                           '%s, %s, %s, ' \
                           '%s, %s, %s' \
                           ')'

    def get_film_work_tuple(self):
        if self.description is not None:
            description = self.description
        else:
            description = self.description

        title = self.title

        if self.creation_date is None:
            creation_date = datetime.utcnow()
        else:
            creation_date = self.creation_date

        if self.rating is None:
            rating = 0.0
        else:
            rating = self.rating

        if self.type is None:
            type = 'no type'
        else:
            type = self.type

        return (self.id, str(title), str(description),
                str(creation_date), str(self.file_path), rating,
                type, str(self.created_at), str(self.updated_at),)



@dataclass
class Genre:
    id: uuid.UUID
    name: str
    description: str
    created_at: field(default=datetime.utcnow())
    updated_at: field(default=datetime.utcnow())

    genre_column: str = '(' \
                        'id, name, ' \
                        'description, created_at, ' \
                        'updated_at' \
                        ')'

    genre_value: str = '(' \
                       '%s, %s, ' \
                       '%s, %s, ' \
                       '%s' \
                       ')'

    def get_genre_tuple(self):
        if self.description is not None:
            description = self.description.replace("'", '"')
        else:
            description = self.description

        name = self.name.replace("'", '"')

        return (self.id, name,
                str(description), str(self.created_at),
                str(self.updated_at),)


@dataclass
class Person:
    id: uuid.UUID
    full_name: str
    created_at: field(default=datetime.utcnow())
    updated_at: field(default=datetime.utcnow())

    person_column: str = '(' \
                         'id, full_name, ' \
                         'created_at, updated_at' \
                         ')'

    person_value: str = '(' \
                        '%s, %s, ' \
                        '%s, %s' \
                        ')'

    def get_person_tuple(self):
        full_name = self.full_name.replace("'", '"')

        return (self.id, full_name,
                str(self.created_at), str(self.updated_at),)


@dataclass
class GenreFilmWork:
    id: uuid.UUID
    film_work_id: str
    genre_id: str
    created_at: field(default=datetime.utcnow())

    genre_film_work_column: str = '(' \
                                  'id, film_work_id, ' \
                                  'genre_id, created_at' \
                                  ')'

    genre_film_work_value: str = '(' \
                                 '%s, %s, ' \
                                 '%s, %s' \
                                 ')'

    def get_genre_film_work_tuple(self):
        return (self.id, self.film_work_id,
                self.genre_id, str(self.created_at),)


@dataclass
class PersonFilmWork:
    id: uuid.UUID
    film_work_id: str
    person_id: str
    role: str
    created_at: field(default=datetime.utcnow())

    person_film_work_column: str = '(' \
                                   'id, film_work_id, ' \
                                   'person_id, role, ' \
                                   'created_at' \
                                   ')'

    person_film_work_value: str = '(' \
                                  '%s, %s, ' \
                                  '%s, %s, ' \
                                  '%s' \
                                  ')'

    def get_person_film_work_tuple(self):
        return (self.id, self.film_work_id,
                self.person_id, str(self.role),
                str(self.created_at),)
