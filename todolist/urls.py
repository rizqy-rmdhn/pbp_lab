from django.urls import path
from .views import (delete_task_json, show_task_html, register, login_user, 
                    logout_user, create_task, update_task_status,
                    delete_task, get_json, show_json, create_task_ajax,
                    delete_task_json, update_task_status_json)

app_name = 'todolist'

urlpatterns = [
    path('', show_task_html, name='show_task_html'),
    path('json/', show_json, name='show_json'),
    path('json/get', get_json, name='get_json'),
    path('json/create-task', create_task_ajax, name='create_task_ajax'),
    path('json/update-status/<int:id>', update_task_status_json, name="update_status_json"),
    path('json/delete-task/<int:id>', delete_task_json, name="delete_task_json"),
    path('json/logout/', logout_user, name='logout_ajax'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('update-status/<int:id>', update_task_status, name="update_status"),
    path('delete-task/<int:id>', delete_task, name="delete_task"),
]