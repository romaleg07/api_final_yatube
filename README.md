# API Yatube

Апи для сервиса Yatube.
Сервиса для шеринга своих историй и рассказов

## Возможности

- Получение постов для любых пользователей
- Написание постов для авторизированных пользователей
- Разбиение постов на группы
- Получение и работа с комментариями к постам
- Подписка на авторов

## Технологии

Для создания были использованы:
- [Python 3.7.0](https://www.python.org)
- [Django 3.2.14](https://www.djangoproject.com)
- [djangorestframework 3.12.4](https://www.django-rest-framework.org)

и многое другое, со списком всех зависимостей можете ознакомиться в файле [requirements.txt](https://github.com/romaleg07/api_final_yatube/blob/master/requirements.txt)

## Установка

Скопируйте репозиторий в свою папку:
```sh
$git clone https://github.com/romaleg07/api_final_yatube.git
```

Установите виртуальное окружение:
```sh
$python3 -m venv <myenvname>
```

После установки запустите его:
```sh
$source <myenvname>/scripts/activate
```

Установите зависимости из requirements.txt:
```sh
$pip install -r reqiurements.txt
```

Выполните миграции:
```sh
$cd yatube_api
$python3 manage.py makemigrations
$python3 manage.py migrate
```

Запустите сервер:
```sh
$python3 manage.py runserver
```

Апи доступен по адресу http://127.0.0.1:8000/api/v1/

## Документация

Вся документация доступна по ссылке: http://127.0.0.1:8000/redoc/#tag/api

