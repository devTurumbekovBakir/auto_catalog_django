import requests
from bs4 import BeautifulSoup
from celery import shared_task
from django.db import transaction

from .models import Mark, Model


@shared_task
@transaction.atomic
def task_update_autoru_catalog():
    """
    Асинхронная Celery-задача для обновления каталога AutoRu.

    Очищает базу данных перед каждым обновлением. Затем выполняет запрос к XML-файлу каталога,

    парсит его с использованием BeautifulSoup и обновляет базу данных марок и моделей.

    Использует транзакцию для обеспечения атомарности операций базы данных.

    """
    # Очищаем базу данных перед каждым обновлением
    Mark.objects.all().delete()
    Model.objects.all().delete()

    url = "https://auto-export.s3.yandex.net/auto/price-list/catalog/cars.xml"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    for mark_tag in soup.find_all("mark"):
        mark_name = mark_tag["name"]
        mark = Mark.objects.create(name=mark_name)

        for folder_tag in mark_tag.find_all("folder"):
            model_name = folder_tag["name"].split(",")[0].strip()
            Model.objects.create(mark=mark, name=model_name)
