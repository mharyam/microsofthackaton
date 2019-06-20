from django.urls import path
from .import views

app_name = 'farmers'

urlpatterns =[
    path('dashboard/', views.home, name='home'),    
    path('create-a-plan/', views.create_a_plan, name='create_a_plan'),
    path('premium-payment/', views.premium_payment, name='premium_payment'),
    path('claim/', views.claim, name="claim")
]