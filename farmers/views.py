from django.shortcuts import render

# Create your views here.

def home(request):
    #create model and put it here and caall it 
    return render(request, 'farmers/user_dashboard.html', {})


def create_a_plan(request):
    return render(request, 'farmers/create-plan.html', {})

def premium_payment(request):
    return render(request, 'farmers/payment-page.html', {})

def claim(request):
    return render(request, 'farmers/claims.html', {})