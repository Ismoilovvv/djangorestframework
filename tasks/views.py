from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskDetail(APIView):
    def get_object(self, id):
        try:
            return Task.objects.get(id=id)
        except Task.DoesNotExist:
            return None
        
    def get(self, request, id):
        task = self.get_object(id)
        if task is None:
            return Response({'error': 'Task not found!'}, status=404)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request, id):
        task = self.get_object(id)
        if task is None:
            return Response({'error': 'Task not found!'}, status=404)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, id):
        task = self.get_object(id)
        if task is None:
            return Response({'error': 'Task not found!'}, status=404)
        task.delete()
        return Response(status=204)