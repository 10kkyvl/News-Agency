from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_display_name(self):
        return self.username


class Topic(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ManyToManyField(
        Topic,
        related_name="articles"
    )
    publishers = models.ManyToManyField(
        Redactor,
        related_name="published_articles"
    )

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title
