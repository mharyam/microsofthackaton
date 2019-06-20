from django.shortcuts import render
from account.forms import UserForm, UserProfileInfoForm, CooperativeInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.


@login_required
def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'account/signin.html', {})

# def home(request):
#     # return render(request, 'account/index.html')
#     return redirect(reverse('account:choose_profile'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def registerfarmer(request):
    registered = False
    user_form = UserCreationForm
    user_profile_form = UserProfileInfoForm
    #if request is not post initialize an empty string 
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        user_profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user.set_password = (user.password)
            user.save()
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            registered = True
            return redirect('account/signin.html')

        else:
            messages.warning(request, "Invalid Input ")

    return render(request, 'account/farmer_signup.html', {
            'user_form':user_form,
            'user_profile_form':user_profile_form,
           'registered':registered,
        })

def registercooperative(request):
    registered = False
    user_form = UserCreationForm
    user_profile_form = CooperativeInfoForm
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        cooperative_form = CooperativeInfoForm(data=request.POST)
        if user_form.is_valid() and cooperative_form.is_valid():
            user = user_form.save()
            user.set_password = (user.password)
            user.save()
            cooperative_form_profile = cooperative_form.save(commit=False)
            cooperative_form_profile.user = user
            cooperative_form_profile.save()
            registered = True

        else:
            messages.warning(request, "Invalid Input ")
    return render(request, 'account/copeartive_signup.html', {'user_form':user_form, 'user_profile_form':user_profile_form, 'registered':registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

        else:
            return render(request, 'login', {})


@login_required
def choose_profile(request):
    user = request.user
    if not user.is_superuser:
        if user.has_perm("account.coperative"):
            return HttpResponseRedirect(reverse('account:coopeartive'))

        elif user.has_perm("account.outreach_officer"):
            return HttpResponseRedirect(reverse('account:coopeartive'))
        else:   
            return HttpResponseRedirect(reverse('account:admin_dashboard'))

