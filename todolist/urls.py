from django.urls import path
from .views import (show_task_html, register, login_user, logout_user)

app_name = 'todolist'

urlpatterns = [
    path('', show_task_html, name='show_task_html'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]