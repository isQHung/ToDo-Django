from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegisterForm
from .models import Todo


class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos."""
        return Todo.objects.order_by('-created_at')

@login_required
def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title, user = request.user)

    return redirect('todos:index')

@login_required 
def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')

@login_required
def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')

@login_required
def add_tags(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    

    return redirect('todos:index')

# ======================================================================================

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todos:index')
    else:
        form = RegisterForm()
    return render(request, 'views/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    return render(request, 'views/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('todos:login')