from django.contrib import admin
from django.urls import include, path

from .views import UserLogOut, UserLogin


urlpatterns = [
    path('login/',UserLogin.as_view(),name="login"),
    path('logout/',UserLogOut.as_view(),name="logout"),

   
]