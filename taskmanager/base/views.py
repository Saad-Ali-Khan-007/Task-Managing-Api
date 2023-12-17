from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer


# Create your views here.

@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def task_list(request):
    if request.method == 'GET':
        task = Task.objects.all()
        serializer = TaskSerializer(task,many=True)
        return Response(serializer.data) 

    if request.method == 'POST':
        task = Task.objects.create(
            name = request.data['name'],
            about = request.data['about'], 
            completed = request.data['completed']
        )
        serializer = TaskSerializer(task,many=False)
        return Response(serializer.data)
    if request.method == 'DELETE':
        task_id = request.data['id']
        task_obj = Task.objects.get(pk=task_id)
        task_obj.delete()
        return Response({"message": "Person deleted successfully"})



@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def task_detail(request):
    if request.method == 'GET':
        task = Task.objects.all()
        serializer = TaskSerializer(task,many=True)
        return Response(serializer.data) 
    if request.method == 'PUT':
        task = request.data
        task_id = task['id']
        task_obj = Task.objects.get(pk=task_id)
        serializer = TaskSerializer(task_obj,data=task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    if request.method == 'DELETE':
        task = Task.objects.all()
        task.delete()
        return Response('Task deleted succesfully')