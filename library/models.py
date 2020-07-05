from django.db import models
from django.utils import timezone

# Create your models here.


class Library(models.Model):

    name = models.CharField(max_length=128)

    updated_at = models.DateTimeField(null=True)
    archived = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Library, self).save(*args, **kwargs)


class Book(models.Model):

    title = models.CharField(max_length=512)
    publisher = models.CharField(max_length=128)
    library = models.ForeignKey('Library', on_delete=models.DO_NOTHING)

    updated_at = models.DateTimeField(null=True)
    archived = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Book, self).save(*args, **kwargs)


# Possibile features that can be added


# class Location

    # name
    # state - choice field
    # country - choice field


# class LibraryLocations

    # - Library (FKey)
    # - Location (FKey)
