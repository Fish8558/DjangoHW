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
- переи меновать файл .env.sample в .env и заполнить поля
```ini
NAME="db_name" - название вашей БД
USER="postgres" - имя пользователя БД
PASSWORD="secret" - пароль пользователя БД
HOST="127.0.0.1" - хост
PORT=5432 - порт
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
```