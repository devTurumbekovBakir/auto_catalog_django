from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Mark, Model
from .tasks import task_update_autoru_catalog


@csrf_exempt
def home(request):
    """
    Представление для главной страницы, отображающей список марок автомобилей и моделей.

     Данный представитель обрабатывает запросы методом POST и GET.
        - При методе POST извлекается выбранный идентификатор марки, и затем отображаются все связанные с ней модели.
        - При методе GET отображаются все модели с использованием пагинации по 10 моделей на странице.

    Это представление декорировано `csrf_exempt` для отключения защиты от CSRF.

    Параметры:
        request (HttpRequest): Объект HTTP-запроса.

    Возвращает:
        HttpResponse: Отображает шаблон 'home.html' со списком марок автомобилей или моделей.
    """
    if request.method == 'POST':
        mark_id = request.POST.get('mark')
        selected_mark = Mark.objects.get(pk=mark_id)
        models = Model.objects.filter(mark=selected_mark)
        return render(request, 'home.html', {'models': models})

    # Извлекаем все модели
    all_models = Model.objects.all()

    # Создаем объект пагинатора с количеством моделей на странице равным 10
    paginator = Paginator(all_models, 10)

    # Получаем номер текущей страницы из параметров запроса
    page_number = request.GET.get('page')

    # Получаем объект текущей страницы
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})


@csrf_exempt
def update_autoru_catalog(request):
    """
    Представление для запуска асинхронной задачи обновления каталога AutoRu.

    Это представление декорировано `csrf_exempt` для отключения защиты от CSRF.

    Параметры:
        request (HttpRequest): Объект HTTP-запроса.

    Возвращает:
        HttpResponseRedirect: Перенаправляет на страницу 'home' после запуска задачи обновления каталога.
    """
    task_update_autoru_catalog.delay()
    return redirect('home')
