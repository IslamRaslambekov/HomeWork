from django.db import models


class Title(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.ManyToManyField(Title)

    def __str__(self):
        return f'{self.last_name}; {self.name}; {self.middle_name}'

