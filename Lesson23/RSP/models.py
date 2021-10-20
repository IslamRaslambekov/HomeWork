from django.db import models


class Common(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')

    class Meta:
        abstract = True


class Title(models.Model):
    title = models.CharField(max_length=100, verbose_name='Специальность')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальность'


class Doctor(Common):
    title = models.ManyToManyField(Title)
    image = models.ImageField(upload_to='RSP', verbose_name='Фото')

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'

    class Meta:
        verbose_name = 'Доктора'
        verbose_name_plural = 'Доктора'

