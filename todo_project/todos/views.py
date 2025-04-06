# from django.shortcuts import render

from urllib import response
from rest_framework import generics,status
from .models import Todo
from .serializers import TodoSerializer

class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoFetchUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



from django.shortcuts import render
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todoList.html', {'todos': todos})

def home(request):
    return render(request, 'home.html')



def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return response(
            {"message": "Updated successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )

def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response(
            {"message": "Deleted successfully"},
            status=status.HTTP_200_OK  
        )
