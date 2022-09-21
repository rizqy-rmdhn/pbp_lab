from django.urls import path
from .views import show_catalog

app_name = 'katalog'

urlpatterns = [
    path('', show_catalog, name='show_catalog'),
]