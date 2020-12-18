from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import ImageForm


def tasks(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('-update_date_time')
    else:
        tasks = {}
    context = {'tasks':tasks}
    return render(request, 'tasks.html',context)


def newTask(request):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            title = request.POST.get('title')
            task = Task.objects.create(user=user, title=title)
            
            if request.POST.get('completed') == 'True':
                task.completed = True
            else:
                task.completed = False
            if 'description' in request.POST:
                task.description = request.POST.get('description')
            if 'task_image' in request.FILES:
                task.image = request.FILES["task_image"]
            task.save()
            return redirect('/')
    
    return render(request, 'new_task.html')

@login_required(login_url='/login_register/')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST.get('title') != "":
            task.title = request.POST.get('title')
            
        if request.POST.get('description') !=  "" :
            task.description = request.POST.get('description')
            
        if request.POST.get('completed') != "" :
            c = request.POST.get('completed')
            if c == 'True':
                task.completed = True
            else:
                task.completed = False
        if 'task_image' in request.FILES:
            task.image = request.FILES["task_image"]
        task.save()
        return redirect('/')
    context = {"task":task}
    return render(request, 'update_task.html',context)

@login_required(login_url='/login_register/')
def deleteTask(request, pk):

    if request.user.is_authenticated:
        if request.method == 'POST':
            task = Task.objects.get(id=pk)
            task.delete()
            return redirect('/')
    task = Task.objects.get(id=pk)
    context = {"task":task}
    return render(request, 'delete_task.html',context)


@login_required(login_url='/login_register/')
def userLogout(request):
    logout(request)
    return redirect('/')


def loginOrRegister(request):
    if request.method == 'POST':
        
        formType = request.POST.get('formType')
        if formType == 'login':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(username=email, password=password)
            if user:
                login(request,user)
                return redirect('/')
            else:
                return render(request,'reglogin.html',{'error_msg':'Invalid login details given.'})
        elif formType == 'register':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            try:
                user = User.objects.get(username=email)
                return render(request,'reglogin.html',{'error_msg_reg':'User already exist, proceed with login or use diffrent email id'})
            except:
                user = User.objects.create(username=email)
                user.set_password(password)
                user.email = email
                user.save()
                return render(request,'reglogin.html',{'error_msg_reg':'Successfully registered, Login Now!'})


    return render(request, 'reglogin.html')