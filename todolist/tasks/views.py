from django.shortcuts import render,redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login,logout

# Create your views here.


def index(request):
    return render(request,"index.html",{})

@login_required
def task_lists(request):
    tasks = Task.objects.all().order_by('-created')
    return render(request, "task_list.html", {"Tasks":tasks})

# if the file is not html  u use Http response
# return HttpResponse(request, 'welcome')

def create_new(request):
    if request.method == 'POST':
        task = Task(
            title = request.POST.get('title'),
            complete = request.POST.get('status', 'off') == 'on',
            due_date = request.POST.get('datetime')
        )
        task.save()
        return redirect('task_list')
    return render(request, 'create_task.html')

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    # task = get_object_or_404(Task,id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('tittle')
        task.complete = request.POST.get('completee','off' )== 'on'
        task.due_date = request.POST.get('date')
        task.save()
        return redirect('task_list')
    return render(request, 'update.html', {'task': task})# i do not undastand this task :task
#the context as in a dictionary holds the value from the views function to be represented by the key in the html.


def delete_task(request, task_pk):
    task = Task.objects.get(pk=task_pk)
    task.delete()
    return redirect('task_list')

def login_task(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        userr = authenticate(request,username=username,password = password)
        if userr is not None:
            login(request,userr)
            return redirect(task_lists)
        else:
            error_message = 'Invalid Password or Username'
            return render(request,'registration/login.html',{'error_message':error_message})


    return render(request, 'registration/login.html')

def signup_task(request):
    if request.method == 'POST':
        username = request.POST['username']
        email =request.POST['email']
        password =request.POST['password']
        repeatpassword =request.POST['repeatpassword']
        if password == repeatpassword:
             try:
                user = User.objects.create_user(username,email,password)
                user.save()
                login(request,user)
                return redirect('task_list')
             except:
                 error_message = 'Error creating account'
                 return render(request, 'registration/signin.html', {'error_message':error_message}) 
        else:
            error_message  = 'password do not match'
            return render(request, 'registration/signin.html', {'error_message':error_message})    
    return render(request, 'registration/signin.html')


def logout_task(request):
    logout(request)
    return redirect('/')
