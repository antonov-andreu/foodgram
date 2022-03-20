![example workflow](https://github.com/Andrey-oss-ai/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

# Foodgram

Foodgram - сервис для публикации рецептов, работающий как web сервис, 
так и через api. Пользователи прошедшие авторизацию могут добавлять 
рецепты других пользователей в избранное, подписываться на понравившихся
авторов и формировать список покупок из рецептов.


[![screen-one.png](https://i.postimg.cc/DyZwM6cv/screen-one.png)](https://postimg.cc/c6pWKQj2)
[![screen-second.png](https://i.postimg.cc/fbK4Znw6/screen-second.png)](https://postimg.cc/bGsVH5ST)
## Подготовка и запуск проекта
### Склонировать репозиторий на локальный пк:
```
git clone https://github.com/Andrey-oss-ai/foodgram-project-react
```
## Для работы с удаленным сервером (на ubuntu):
* Выполнить вход на свой удаленный сервер

* Установить docker на сервер:
```
sudo apt install docker.io 
```
* Установить docker-compose на сервер:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
* Локально отредактировать файл infra/nginx.conf и в строке server_name вписать свой IP
* Скопировать файлы docker-compose.yml и nginx.conf из директории infra на сервер:
```
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp nginx.conf <username>@<host>:/home/<username>/nginx.conf
```
* Cоздать .env файл и добавить в него переменные:
```
SECRET_KEY=<Secret key of Django project>
DB_ENGINE=<django.db.backends.postgresql>
POSTGRES_PASSWORD=<Postgress pass>
DB_NAME=<Database name>
POSTGRES_USER=<Postgress user>
DB_HOST=<Host with Database>
DB_PORT=<Database port>
ALLOWED_HOSTS=<Hosts for connect>
```
* Для работы с Workflow добавить в Secrets GitHub переменные окружения: 
```
    DB_ENGINE=<django.db.backends.postgresql>
    DB_NAME=<имя базы данных postgres>
    DB_USER=<пользователь бд>
    DB_PASSWORD=<пароль>
    DB_HOST=<db>
    DB_PORT=<5432>
    DOCKER_PASSWORD=<пароль от DockerHub>
    DOCKER_USERNAME=<имя пользователя>
    SECRET_KEY=<секретный ключ проекта django>
    USER=<username для подключения к серверу>
    HOST=<IP сервера>
    PASSPHRASE=<пароль для сервера, если он установлен>
    SSH_KEY=<ваш SSH ключ (для получения команда: cat ~/.ssh/id_rsa)>
    ALLOWED_HOSTS=<Hosts for connect>
    TELEGRAM_TO=<ID чата, в который придет сообщение>
    TELEGRAM_TOKEN=<токен вашего бота>
```
    Workflow состоит из четырёх шагов:
     - Проверка кода на соответствие PEP8(flake8)
     - Сборка и публикация образа бекенда на DockerHub.
     - Автоматический деплой на удаленный сервер.
     - Отправка уведомления в телеграм-чат. 

* После успешной сборки на сервере выполнить команды (только после первого деплоя):
    Собрать статические файлы:
    ```
    sudo docker-compose exec backend python manage.py collectstatic --noinput
    ```
    Применить миграции:
    ```
    sudo docker-compose exec backend python manage.py migrate --noinput
    ```
    Загрузить ингридиенты  в базу данных (необязательно):  
    ```
    sudo docker-compose exec backend python manage.py loaddata fixtures/ingredients.json
    ```
    Создать суперпользователя Django:
    ```
    sudo docker-compose exec backend python manage.py createsuperuser
    ```
    Проект будет доступен по вашему IP


### Автор
andreu-antonov@yandex.ru


