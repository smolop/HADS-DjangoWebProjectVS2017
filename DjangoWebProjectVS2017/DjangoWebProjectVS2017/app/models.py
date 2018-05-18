"""
Definition of models.
"""

from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Topic(models.Model):
    """A poll object for use in the application views and repository."""
    text = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """Returns a string representation of a poll."""
        return self.text

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)

class User(models.Model):
    email = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)