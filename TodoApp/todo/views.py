from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSerializer


class TodoAPIView(APIView):
    def get(self, request):
        todo = Todo.objects.filter(complete=False)
        serializer = TodoSerializer(todo,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
