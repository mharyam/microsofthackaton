#from django.contrib.auth.models import User, UserProfileInfo, CooperativeInfo
from django.contrib.auth.models import User
from account.models import UserProfileInfo, CooperativeInfo
from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# class SignUpForm(UserCreationForm):
#     username = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
#     password1=forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
#     password2=forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))


#     class Meta(UserCreationForm.Meta):
#         model = User
#         # I've tried both of these 'fields' declaration, result is the same
#         # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =['username','password','email',]


class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ['first_name', 'last_name', 'phone_number','email','adress', ]

class CooperativeInfoForm(forms.ModelForm):

    class Meta:
        model = CooperativeInfo
        fields = ['name', 'adress', 'email', 'phone_number',]