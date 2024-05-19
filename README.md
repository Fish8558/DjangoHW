### Интернет магазин 

##### Технологии:
- Django
- python-dotenv
- psycopg2-binary
- pillow
- ipython
- pytils


#### Инструкция для запуска проекта:
- Клонировать проект
- Создать и активировать виртуального окружения
- Установить зависимости
- Отредактировать файл .env.sample
- Настроить БД
- Запустить проект


##### Клонирование проекта:
- git clone https://github.com/Fish8558/DjangoHW.git

##### Настройка виртуального окружение и установка зависимостей:
- [Инструкция по установке](https://sky.pro/media/kak-sozdat-virtualnoe-okruzhenie-python/)

##### Редактирование файла .env.sample
- переименовать файл .env.sample в .env и заполнить поля
```text
NAME="db_name" - название вашей БД
USER="postgres" - имя пользователя БД
PASSWORD="secret" - пароль пользователя БД
HOST="127.0.0.1" - хост
PORT=5432 - порт

EMAIL_HOST_USER='your_email@yandex.ru' - ваш email yandex
EMAIL_HOST_PASSWORD='your_yandex_smtp_password' - ваш пароль smtp yandex
ADMIN_EMAIL='admin@test.com' - email регистрации администратора сайта
ADMIN_PASSWORD='secret' - пароль регистрации администратора сайта

DEBUG=True - режим дебага
REDIS_HOST=127.0.0.1:6379 - хост и порт редис
CACHE_ENABLED=True - кэш
```
##### Настройка БД
- примените миграции:
```text
python manage.py migrate
```
- примените фикстуры:
```text
python -Xutf8 manage.py loaddata fixtures/*.json
```

##### Запуск проекта
- запустите проект и перейдите по адресу
```text
python manage.py runserver
http://127.0.0.1:8000
```

##### Создание администратора
- для создания административного пользователя используйте команду
```text
python manage.py csu
```
