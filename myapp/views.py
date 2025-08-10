from django.shortcuts import render, redirect
from .models import  Notebook   
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            User.objects.create_user(username=username, password=password1)
            messages.success(request, 'Account created successfully!')
            return redirect('login') 

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def myfunctioncall(request):
    signup_view(request)
    login_view(request)
    return render(request, 'home.html')

def another_function(request):
    return render(request, 'views.html')

# views.py
from django.shortcuts import render, redirect
from .forms import NotebookForm
from django.shortcuts import get_object_or_404


def add_notebook(request):
    if request.method == 'POST':
        form = NotebookForm(request.POST, request.FILES)
        if form.is_valid():
            notebook = form.save(commit=True)
            notebook.author = request.user  # Set current user as author
            notebook.save()
            return redirect('notebook_detail', pk=notebook.pk)
    else:
        form = NotebookForm()
    return render(request, 'add_notebook.html', {'form': form})

def notebook_detail(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk)
    return render(request, 'notebook_detail.html', {'notebook': notebook})



def notebook_list(request):
    notebooks = Notebook.objects.all()
    return render(request, 'notebook_list.html', {'notebooks': notebooks})
