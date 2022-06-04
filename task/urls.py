from django.urls import path
from .views import home,login,signup

urlpatterns=[
    path('',home,name="home-page"),
    path('login/',login,name="home-page"),
    path('sign_up/',signup,name="register-page")
]