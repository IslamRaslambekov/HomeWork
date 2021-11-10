from django.db import models


class Common(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Отчество')
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
    image = models.ImageField(upload_to='RSP', null=True, blank=True, verbose_name='Фото',
                              default='/static/RSP/img/user.png')

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'

    class Meta:
        verbose_name = 'Доктора'
        verbose_name_plural = 'Доктора'

    def get_titles_count(self):
        return len(self.title.all())

    def get_more_than_null(self):
        if len(self.title.all()) > 0:
            return True

    def get_less_than_null(self):
        if len(self.title.all()) < 1:
            return False

    def name_is_null(self):
        return True if self.name is None else False

    def middle_name_is_null(self):
        return True if self.middle_name is None else False
