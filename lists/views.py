from django.shortcuts import render, redirect
from .models import Lists
from .forms import TodoListForm
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
	todoItems = Lists.objects.order_by('-id')
	form = TodoListForm()
	context = {'todoItems': todoItems, 'form': form}
	return render(request, 'lists/index.html', context)

@require_POST
def addTodoItem(request):
	form = TodoListForm(request.POST)
	if form.is_valid():
		newTodo = Lists(text = request.POST['text'])
		newTodo.save()
	return redirect('index')

def completedTodo(request, todoId):
	todo = Lists.objects.get(pk = todoId)
	todo.completed = True
	todo.save()
	return redirect('index')

def deleteCompletedItems(request):
	completedList = Lists.objects.filter(completed__exact = True).delete()
	return redirect('index')

def deleteAllItems(request):
	deleteList = Lists.objects.all().delete()
	return redirect('index')