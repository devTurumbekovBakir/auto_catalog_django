<h1 align="center">Auto Catalog Web Application</h1>

<p align="center">
    <em>Это веб-приложение позволяет пользователям изучать каталог марок и моделей автомобилей. Он включает 
        функциональность фильтрации моделей на основе выбранных марок и предоставляет пагинированный вид 
        всех доступных моделей.
    </em>
</p>

## Начало работы

Чтобы начать использовать веб-приложение Auto Catalog, следуйте инструкциям ниже.

Необходимые программы
Убедитесь, что у вас установлены следующие программы на вашем компьютере:

Docker
Docker Compose
Установка
Склонируйте репозиторий:

## Установка

1. Клонируйте репозиторий:

bash
Copy code
git clone https://github.com/devTurumbekovBakir/auto_catalog_django.git
cd auto-catalog
Соберите и запустите контейнеры Docker:

bash
Copy code
docker-compose up -d --build

docker-compose run --rm web-app sh -c "python manage.py makemigrations"

docker-compose run --rm web-app sh -c "python manage.py migrate"

docker-compose run --rm web-app sh -c "python manage.py createsuperuser"

Перейдите веб-приложение по адресу http://localhost:8000 в вашем веб-браузере.

Использование
Выберите марку из выпадающего списка на главной странице, чтобы просмотреть связанные модели.

Обновление каталога AutoRu
Каталог AutoRu можно обновлять асинхронно с использованием задачи Celery. Чтобы запустить обновление:

Перейдите к мониторингу задач в интерфейсе Flower по адресу http://localhost:5555.
Отслеживайте ход выполнения фоновой задачи.
Задачу обновления каталога также можно запустить программно, посетив ссылку "Обновить каталог AutoRu" на главной странице.
