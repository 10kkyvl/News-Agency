from django.contrib.auth.models import AbstractUser
from django.db import models


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING, related_name="articles")
    publishers = models.ManyToManyField(Redactor, related_name="published_articles")

    def __str__(self):
        return self.title
