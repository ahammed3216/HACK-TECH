from django.urls import path
from .views import home,login_view,signup,complaint

urlpatterns=[
    path('',home,name="home-page"),
    path('login/',login_view,name="home-page"),
    path('sign_up/',signup,name="register-page"),
    path('complaint/',complaint,name="compaint-page"),

]