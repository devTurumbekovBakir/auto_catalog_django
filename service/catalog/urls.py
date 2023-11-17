# catalog/urls.py
from django.urls import path
from .views import update_autoru_catalog, home

urlpatterns = [
    path('', home, name='home'),
    path('update_autoru_catalog/', update_autoru_catalog, name='update_autoru_catalog'),

]
