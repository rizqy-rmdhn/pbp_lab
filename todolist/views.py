from django.shortcuts import render
from .models import Task
from .forms import TaskForm
import datetime
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_task_html(request):
    user_logged_in = request.user
    task_data = Task.objects.filter(user=user_logged_in).all()
    context = {
                'list_task': task_data,
                'name': 'Muhammad Rizqy Ramadhan',
                'NPM': '2106632182',
                'last_login': request.COOKIES['last_login'],
              }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Account successfully created!')
        return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_task_html")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Incorrect Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if (request.method == 'POST'):
        form = TaskForm(request.POST)
        if (form.is_valid()):
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            messages.success(request, "Succesfully created task!")
        else:
            messages.error(request, "Invalid!")
            
        return HttpResponseRedirect(reverse("todolist:show_task_html"))
    
    context = {'task_form' : TaskForm}
    return render(request, 'create_task.html', context)

def update_task_status(request, id):
    task = Task.objects.get(id=id)
    if task: 
        if task.finished:
            task.finished = 0
            task.save()
            messages.success(request, "Oops, turned you have not finished the task!")
        else:
            task.finished = 1
            task.save()
            messages.success(request, "Yeay, you have finished the task!")
    else:
        messages.error(request, "Oops, the task can not be found")
    return HttpResponseRedirect(reverse("todolist:show_task_html"))

def delete_task(request, id):
    task = Task.objects.get(id=id)
    if task: 
        task.delete()
        messages.success(request, "Successfully deleted the task!")
    else:
        messages.error(request, "Oops, the task can not be found")
    return HttpResponseRedirect(reverse("todolist:show_task_html"))
    
        