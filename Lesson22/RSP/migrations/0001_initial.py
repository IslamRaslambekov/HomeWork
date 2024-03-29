# Generated by Django 3.2 on 2021-09-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('number', models.CharField(max_length=25, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Пациенты',
                'verbose_name_plural': 'Пациенты',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальность',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('image', models.ImageField(blank=True, null=True, upload_to='RSP/doctors/%Y/%m/%d', verbose_name='Фото')),
                ('title', models.ManyToManyField(to='RSP.Title')),
            ],
            options={
                'verbose_name': 'Доктора',
                'verbose_name_plural': 'Доктора',
            },
        ),
    ]
