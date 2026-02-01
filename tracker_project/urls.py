from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('expenses.urls')),
    path('api/', include('tasks.urls')),
]