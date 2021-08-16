from django.urls import path
from . import views

urlpatterns = [
    path('login', views.UAlogin, name="UALogin"),
    path('loginuser', views.loginuser, name="UALoginuser"),
    path('logout', views.UAlogout, name="UALogout"),
    path('signup', views.UAsignup, name="UASignup"),
    path('signupuser', views.signupuser, name="signupuser"),
]