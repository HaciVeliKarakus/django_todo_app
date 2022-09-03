from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from todo.decorators import unauthenticated_user
from todo.forms import TodoModelForm, CreateUserForm
from todo.models import Todo


@method_decorator(login_required, name='dispatch')
class TodoListView(ListView):
    model = Todo
    template_name = 'index.html'
    queryset = Todo.objects.all()


@method_decorator(login_required, name='dispatch')
class TodoDetailView(DetailView):
    model = Todo
    login_required = True
    template_name = 'detail.html'


@method_decorator(login_required, name='dispatch')
class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoModelForm
    success_url = reverse_lazy('index')
    template_name = 'add.html'

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'details']
    template_name = 'edit.html'
    success_url = reverse_lazy('index')


@method_decorator(login_required, name='dispatch')
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


@login_required(login_url='login')
def todo_complete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')


@login_required(login_url='login')
def delete_completed(request):
    Todo.objects.filter(completed=True).delete()

    return redirect('index')


@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}

    return render(request, 'register.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}

    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)

    return redirect('login')
