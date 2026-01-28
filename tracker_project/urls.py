from django.urls import path, include

urlpatterns = [
    path('api/', include('expenses.urls')),
    path('api/', include('tasks.urls')),
]