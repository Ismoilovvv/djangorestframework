from django.urls import path 
from .views import ExpenseList, ExpenseDetail

urlpatterns = [
    path('expenses/', ExpenseList.as_view()),
    path('expenses/<int:id>/', ExpenseDetail.as_view()),
]