from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import RegisterForm
import openai

# Registration View
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

# Logout View
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('login')

# Dashboard View
@login_required
def dashboard(request):
    customers = Customer.objects.all()
    return render(request, 'dashboard.html', {'customers': customers})

# Customer Details View
@login_required
def customer_details(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'customer_details.html', {'customer': customer})

# Script Generation View
@login_required
def generate_script(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    # Mock script generation with OpenAI
    script = f"Generating script for {customer.name} based on portfolio: {customer.portfolio} and persona: {customer.persona}."
    messages.info(request, script)
    return redirect('customer_details', customer_id=customer_id)
