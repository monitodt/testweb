from django.shortcuts import render,redirect
from . models import Task
from . forms import TaskForm


def index (request):    
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})

def polis (request):    
    return render(request, 'main/polis.html')

def help (request):    
    return render(request, 'main/help.html')

def create (request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
        else:
            error='Досвидания:)'

    form=TaskForm()   
    context={

        'form':form,
        'error': error
    }
    return render(request, 'main/create.html', context)
# Create your views here.
