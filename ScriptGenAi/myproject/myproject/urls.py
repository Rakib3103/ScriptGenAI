# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),  # Redirect root URL to login
    path('register/', include('myapp.urls')),     # Or include your app URLs directly
    path('login/', include('myapp.urls')),
    path('logout/', include('myapp.urls')),
    path('dashboard/', include('myapp.urls')),
    path('customer/<int:customer_id>/', include('myapp.urls')),
    path('generate_script/<int:customer_id>/', include('myapp.urls')),
]
