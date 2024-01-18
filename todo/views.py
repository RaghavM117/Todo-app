from django.shortcuts import render,redirect
from .forms import UserRegistrationForm, TodoForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from .models import TodoItem
from django.urls import reverse

# Create your views here.

def register(request):
    
    form = UserRegistrationForm()
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form=UserRegistrationForm()
    context = {'form':form}
    return render(request, 'todo/register.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    if request.method == 'POST':
        todo_name = request.POST.get("new-todo")
        todo = TodoItem.objects.create(name=todo_name, user=request.user)
        return redirect(reverse("home"))

    todos = TodoItem.objects.filter(user=request.user, is_completed=False).order_by("-id")

    paginator = Paginator(todos, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"todos": todos, "page_obj": page_obj}

    return render(request, "todo/crud.html", context)

def update_todo(request, pk):
    
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)
    todo.name=request.POST.get(f'todo_{pk}')
    todo.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def complete_todo(request, pk):
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_todo(request, pk):
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)
    todo.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



    
    




    
