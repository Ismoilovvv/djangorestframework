from django.urls import path
from .views import expense_detail, expense_list

urlpatterns = [
    path('expenses/', expense_list),
    path('expenses/<int:id>/', expense_detail)
]