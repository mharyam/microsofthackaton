from django.shortcuts import render

# Create your views here.

def home(request):
    #create model and put it here and caall it 
    return render(request, 'insurance/farminsure.html', {})