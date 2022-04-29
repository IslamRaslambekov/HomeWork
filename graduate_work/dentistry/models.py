from django.db import models


# Create your models here.
class ReceptionTime(models.Model):
    datetime = models.DateTimeField()
    doctor = models.ManyToManyField('Doctor')

    def __str__(self):
        dr = ", ".join(str(dr) for dr in self.doctor.all())
        return f'{self.datetime} - {dr}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'


class Doctor(models.Model):
    full_name = models.CharField(max_length=150)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Appointment(models.Model):
    reception_time = models.OneToOneField('ReceptionTime', on_delete=models.DO_NOTHING)
    full_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.full_name} - {self.reception_time}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
# class Doctor(models.Model):
#     first_name = models.CharField(max_length=50, verbose_name='Имя')
#     middle_name = models.CharField(max_length=50, verbose_name='Отчество')
#     last_name = models.CharField(max_length=50, verbose_name='Фамилия')
#     title = models.ManyToManyField('Title', verbose_name='Специальность')
#     description = models.TextField(blank=True, verbose_name='О враче')
#     image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Фотография')
#     is_active = models.BooleanField(default=True, verbose_name='Доступно')
#
#     def __str__(self):
#         return f'{self.last_name} {self.first_name} {self.title.name}'
#
#     class Meta:
#         verbose_name = 'Врач'
#         verbose_name_plural = 'Врачи'
#
#
# class Title(models.Model):
#     name = models.CharField(max_length=50, unique=True, verbose_name='Специальность')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Специальность'
#         verbose_name_plural = 'Специальности'
#
#
# class Appointment(models.Model):
#     first_name = models.CharField(max_length=50, verbose_name='Имя')
#     middle_name = models.CharField(max_length=50, verbose_name='Отчество')
#     last_name = models.CharField(max_length=50, verbose_name='Фамилия')
#     number = models.IntegerField(verbose_name='Телефон')
#     appointment = models.OneToOneField('Time', unique=True, on_delete=models.CASCADE, verbose_name='Запись')
#     created_in = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
#
#     def __str__(self):
#         return f'{self.last_name} {self.first_name} {self.middle_name}'
#
#     class Meta:
#         verbose_name = 'Запись'
#         verbose_name_plural = 'Записи'
#
#
# class Date(models.Model):
#     day = models.DateField(verbose_name='День')
#     is_active = models.BooleanField(default=True, verbose_name='Доступно')
#
#     def __str__(self):
#         return f'{self.day}'
#
#     class Meta:
#         verbose_name = 'День'
#         verbose_name_plural = 'Дни'
#
#
# class Time(models.Model):
#     time = models.TimeField(verbose_name='Время')
#     date = models.ManyToManyField('Date', verbose_name='День')
#     doctor = models.ManyToManyField('Doctor', verbose_name='Врач')
#     is_active = models.BooleanField(default=True, verbose_name='Доступно')
#
#     def __str__(self):
#         return f'{self.time} {self.date} {self.doctor}'
#
#     class Meta:
#         verbose_name = 'Расписание'
#         verbose_name_plural = 'Расписание'
#
#
# # Test models ################################################################
#
# class TestTime(models.Model):
#     time = models.TimeField(verbose_name='Время')
#     day = models.ManyToManyField('Week', verbose_name='День')
#     doctor = models.ManyToManyField('TestDr', verbose_name='Врач')
#
#     def __str__(self):
#         return f'{self.time}'
#
#
# class Week(models.Model):
#     day = models.CharField(max_length=20, verbose_name='День')
#
#     def __str__(self):
#         return f'{self.day}'
#
#
# class TestDr(models.Model):
#     name = models.CharField(max_length=50, verbose_name='Врач')
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# class Schedule(models.Model):
#     date = models.DateField(verbose_name='Число')
#     day = models.ManyToManyField('Week', verbose_name='День')
#     doctor = models.ManyToManyField('TestDr', verbose_name='Врач')
#     time = models.ManyToManyField('TestTime', verbose_name='Время')
#
#     def __str__(self):
#         return f'{self.date}'
