create schema if not exists content;

create table if not exists content.film_work (
    id uuid primary key,
    title text not null,
    description text,
    creation_date date,
    rating float,
    type text not null,
    created timestamp with time zone,
    modified timestamp with time zone
);

create table if not exists content.genre (
    id uuid primary key,
    name text not null,
    description text,
    created timestamp with time zone,
    modified timestamp with time zone
);

create table if not exists content.person (
    id uuid primary key,
    full_name text not null,
    created timestamp with time zone,
    modified timestamp with time zone
);

create table if not exists content.genre_film_work (
    id uuid primary key,
    genre_id uuid references content.genre,
    film_work_id uuid references content.film_work,
    created timestamp with time zone
);


create table if not exists content.person_film_work (
    id uuid primary key,
    person_id uuid references content.person,
    film_work_id uuid references content.film_work,
    role text not null,
    created timestamp with time zone
);
    
create unique index if not exists film_work_person_role_idx on content.person_film_work(
                                                                     film_work_id,
                                                                     person_id,
                                                                     role
);

create unique index if not exists film_work_genre_idx on content.genre_film_work(
                                                                   film_work_id,
                                                                   genre_id
);

