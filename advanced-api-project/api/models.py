from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Author model stores author's information
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book model stores book information and links to an Author
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Custom validation to prevent future publication years
    def clean(self):
        if self.publication_year > date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
