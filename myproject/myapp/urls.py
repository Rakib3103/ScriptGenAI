# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Rename 'login' function if it conflicts with built-in function
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/<int:customer_id>/', views.customer_details, name='customer_details'),
    path('generate_script/<int:customer_id>/', views.generate_script, name='generate_script'),
]
