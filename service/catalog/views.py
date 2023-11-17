from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Mark, Model
from .tasks import task_update_autoru_catalog


@csrf_exempt
def home(request):
    if request.method == 'POST':
        mark_id = request.POST.get('mark')
        selected_mark = Mark.objects.get(pk=mark_id)
        models = Model.objects.filter(mark=selected_mark)
        return render(request, 'home.html', {'models': models})

    marks = Mark.objects.all()
    return render(request, 'home.html', {'marks': marks})


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
