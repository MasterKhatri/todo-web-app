from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodoItem, name='add'),
    path('deletecompleted', views.deleteCompletedItems, name='deletecompleted'),
    path('deleteall', views.deleteAllItems, name='deleteall'),
    path('completed/<todoId>', views.completedTodo, name='completed'),
]
