from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,UpdateView,ListView,DeleteView
from .models import Todo
from .forms import TodoForm

def home(request):
    return render(request,"todoapp/base.html")

class TodoListView(ListView):
    model=Todo

class TodoCreateView(CreateView):
    form_class = TodoForm
    template_name = "todoapp/todo_form.html"

    def get_success_url(self):
        return reverse_lazy("todo_detail",kwargs={'pk': self.object.pk})

class TodoDetailView(DetailView):
    model = Todo

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todoapp/update_todo.html"

    def get_success_url(self):
        return reverse_lazy("todo_detail",kwargs={'pk': self.object.pk})

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todoapp/todo_detail.html"
    success_url = reverse_lazy("todo_list")

def completetodo(request,pk):
    todo = get_object_or_404(Todo,pk=pk)
    if request.method=="POST":
        todo.is_completed = True
        todo.save()
        return redirect("todo_list")

def incompletetodo(request,pk):
    todo = get_object_or_404(Todo,pk=pk)
    if request.method=="POST":
        todo.is_completed = False
        todo.save()
        return redirect("todo_detail",pk)
