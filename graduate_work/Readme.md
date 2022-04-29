

# dentistry - вебсайт для записи на прием к врачу

## Тема проекта: создание веб-сайта для записи к врачу, используя Django Framework

## Возможности и функционал
Для пользователя
> Сайт позволяет выбрать удобное пациенту время для записи к врачу (без регистрации).
> 
> Удобство сайта заключется в том, что пациенту нет необходимости регистрироваться на сайте.
> Для записи достаточно выбрать доктора, день и часы приема, указать Ф.И.О. и ввести номер телефона.

Для админа
> Админ может гибко настроить график работы сотрудников(врачей),
> например: выбирать дни в которые нет приема как у одного из сотрудников так и у всех.

Сам процесс записи осуществляется следующим образом:
* Админ устнавливает график приема к врачу
* На основе этих данных создается view, которое отображает данные в определенном шаблоне(странице)
* Переходя по нужному роуту пользователь видит эти данные(расписание) и выбирает удобное для себя время для записи
* Выбрав это время перед пользователем появляется форма записи, куда он вводит требуемые данные и делает запись
* В итоге эти данные, если они прошли валидацию, записываются в базу данных

Сама база данных представлена моделями:

Модель врача
```python
class Doctor(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    title = models.ManyToManyField('Title', verbose_name='Специальность')
    number = models.IntegerField(blank=True, null=True, verbose_name='Телефон')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Фотография')
    created_in = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_in = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_active = models.BooleanField(default=True, verbose_name='Доступно')

class Title(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Специальность')
    created_in = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_in = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
```

Модель пациента
```python
class Patient(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    number = models.IntegerField(verbose_name='Телефон')
    reception_time = models.OneToOneField('Time', unique=True, on_delete=models.CASCADE, verbose_name='Запись')
    created_in = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
```

Модель расписания
```python
class Time(models.Model):
    time = models.TimeField(verbose_name='Время')
    date = models.ManyToManyField('Date', verbose_name='День')
    doctor = models.ManyToManyField('Doctor', verbose_name='Врач')
    is_active = models.BooleanField(default=True, verbose_name='Доступно')

class Date(models.Model):
    day = models.DateField(verbose_name='День')
    is_active = models.BooleanField(default=True, verbose_name='Доступно')
```
## Способы развертывания системы
Данный сайт развернут на сервере "address" на ОС Ubuntu используя nginx и gunicorn.
Для развертывания требуется установка Python, PostgreSQL и некоторые зависимости.
Все зависимости лежат в корневой директории проекта graduate_work/requirements.txt

Для установки зависимостей нужно перейти в директорию проекта
```
cd/graduate_work
```
и ввести в терминале команду
```python
pip install -r requiremets.txt
```
Также сайт развернут на 'address' используя ngrok.
Есть возможность развернуть и в Docker контейнере.

## Интерфейс системы
**dentistry** я решил сделать веб-сайтом, потому что веб-сайты являются одними из основных источников информации.
Каждый человек, даже далекий от IT области умеет пользоваться сайтами, также для многих пользователей удобно зайти 
в браузер и открыть нужную страницу, чем скачивать приложение на свое устройство.

Интерфейс выбран web-сайт по следующим причинам:
* Простая реализация
* Возможности фреймворка Django
* Клиентом может служить любой девайс с браузером и доступом в Интернет

## Стек технологий
* Python
* Django/DjangoDebugToolbar
* PostgreSQL
* HTML/CSS/Bootstrap
* Ngrok
* Nginx
* Gunicorn

## Выводы
В ходе выполнения дипломной работы был получен большой опыт работы как с самим языком Python, так и с фреймворком Django.
Помимо этого получены знания работы с различными СУБД (Postgres, Sqlite) и ORM. Проект создан придерживаясь концепции 
MVC (MTV).

## План дальнейшего развития системы
Создание REST API используя DRF для дальнейшего развития проекта(использовать данные на дргих сайтах или в приложении).