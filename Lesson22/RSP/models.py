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
    image = models.ImageField(upload_to='RSP', null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'

