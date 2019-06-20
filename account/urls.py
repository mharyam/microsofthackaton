from django.urls import path
from .import views

app_name = 'account'

urlpatterns =[
    path('farmer/', views.registerfarmer, name='registerfarmer'),
    path('cooperative/', views.registercooperative, name='registercooperative'),
    path('signin/', views.signin, name="signin"),
]