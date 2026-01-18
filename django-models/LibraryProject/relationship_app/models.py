from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        related_name='books'  # <-- No clash now, Library.books refers to all books in that library
    )
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author.name}"


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name='librarian'
    )

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Signal to automatically create UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, role='Member')  # default role
