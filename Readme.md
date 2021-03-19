# where_to_go

Карта с самыми интересными местами в Москве.

[сайт на pythonanywhere](https://wenny171.pythonanywhere.com/).

## Как запустить

* Скачайте код
* Перейдите в каталог проекта с файлом `manage.py`
* В корне проекта создать файл .env

* Положить внутрь переменную SECRET_KEY

* Установить зависимости
```bash
pip install -r requirements.txt
```
Сделать миграции
```bash
python manage.py migrate
```
* Запустите веб-сервер командой 
```bash
$ python manage.py runserver
```
* Откройте в браузере

Админка сайта находится по адресу http://127.0.0.1:8000/admin/
Для входа в админку создайте суперпользователя командой
```bash
$ python manage.py createsuperuser
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
