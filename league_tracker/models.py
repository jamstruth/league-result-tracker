from django.db import models

# Create your models here.

from django.db import models


class League(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Division(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateTimeField('Date and Time of Event')


class Result(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    position = models.IntegerField
    driver_name = models.CharField(max_length=100)

