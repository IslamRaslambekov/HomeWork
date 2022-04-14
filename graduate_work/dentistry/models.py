from django.db import models


# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.ManyToManyField('Title')
    number = models.IntegerField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    created_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)


class Title(models.Model):
    name = models.CharField(max_length=50)
    created_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField(max_length=25)
    email = models.EmailField(blank=True, null=True)
    reception_time = models.OneToOneField('Schedule', unique=True, on_delete=models.CASCADE)
    created_in = models.DateTimeField(auto_now_add=True)


class Schedule(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    stop_at = models.DateTimeField()
    created_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)
