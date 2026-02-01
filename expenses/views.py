from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseList(APIView):
    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ExpenseDetail(APIView):
    def get_object(self, id):
        try:
            return Expense.objects.get(id=id)
        except Expense.DoesNotExist:
            return None
        
    def get(self, request, id):
        expense = self.get_object(id)
        if expense is None:
            return Response({'error': 'Expense not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)
    
    def put(self, request, id):
        expense = self.get_object(id)
        if expense is None:
            return Response({'error': 'Expense not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
        
    def delete(self, id):
        expense = self.get_object(id)
        if expense is None:
            return Response({'error': 'Expense not found!'}, status=status.HTTP_404_NOT_FOUND)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)