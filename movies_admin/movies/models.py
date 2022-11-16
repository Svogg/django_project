import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(_('created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('modified'), auto_now_add=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class FilmWork(UUIDMixin, TimeStampedMixin):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    creation_date = models.DateField(_('creation date'), blank=True)
    file_path = models.FileField(_('file path'), blank=True)
    rating = models.FloatField(_('rating'), default=0.0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    type = models.TextField(_('type'), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = 'Кинопроизведение'
        verbose_name_plural = 'Кинопроизведения'


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_('full_name'), max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "content\".\"person"
        verbose_name = 'Над фильмом работал'
        verbose_name_plural = 'Над фильмом работали'


class GenreFilmWork(UUIDMixin):
    film_work = models.ForeignKey('FilmWork', verbose_name=_('film_work'), on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', verbose_name=_('genre'), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = 'жанр относящийся к фильму'
        verbose_name_plural = 'жанры относящиеся к фильму'


class PersonFilmWork(UUIDMixin):
    film_work = models.ForeignKey('FilmWork', verbose_name=_('film_work'), on_delete=models.CASCADE)
    person = models.ForeignKey('Person', verbose_name=_('person'), on_delete=models.CASCADE)
    role = models.TextField(_('role'), null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = 'человек работавший над фильмом'
        verbose_name_plural = 'люди работавшие над фильмом'
