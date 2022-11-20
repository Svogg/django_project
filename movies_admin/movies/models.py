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
        verbose_name = _('Genre_verbose')
        verbose_name_plural = _('Genre_verbose_plural')


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
        verbose_name = _('FilmWork_verbose')
        verbose_name_plural = _('FilmWork_verbose_plural')


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_('full_name'), max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "content\".\"person"
        verbose_name = _('Person_verbose')
        verbose_name_plural = _('Person_verbose_plural')


class GenreFilmWork(UUIDMixin):
    film_work = models.ForeignKey(FilmWork, verbose_name=_('film_work'), on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, verbose_name=_('genre'), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = _('GenreFilmWork_verbose')
        verbose_name_plural = _('GenreFilmWork_verbose_plural')

        constraints = [
            models.UniqueConstraint(fields=[
                'film_work',
                'genre'
            ],
                name='film_work_genre_idx')
        ]


class PersonFilmWork(UUIDMixin):
    class Role(models.TextChoices):
        actor = _('actor')
        screenwriter = _('screenwriter')
        producer = _('producer')
        editor = _('editor')
        director = _('director')

    film_work = models.ForeignKey(FilmWork, verbose_name=_('film_work'), on_delete=models.CASCADE)
    person = models.ForeignKey(Person, verbose_name=_('person'), on_delete=models.CASCADE)

    role = models.ForeignKey(
        'self',
        max_length=100,
        choices=Role.choices,
        default=Role.actor,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = _('PersonFilmWork_verbose')
        verbose_name_plural = _('PersonFilmWork_verbose_plural')

        constraints = [
            models.UniqueConstraint(fields=[
                'film_work',
                'person',
                'role'
            ],
                name='film_work_person_role_idx')
        ]
