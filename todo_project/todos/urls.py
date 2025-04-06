from django.urls import path
from .views import TodoListCreate, TodoFetchUpdateDelete
from .views import todo_list
from .views import home
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos/', TodoListCreate.as_view(), name='todo-list-create'),
    path('api/todos/<int:pk>/', TodoFetchUpdateDelete.as_view(), name='todo-retrieve-update-delete'),
    path('api/index/', todo_list, name='todo-list'),
    # path('', home, name='home'),
]
