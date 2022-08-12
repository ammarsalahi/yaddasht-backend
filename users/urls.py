from django.urls import path
from users.api import *


urlpatterns=[
    path('signin/',UserSignin.as_view()),
    path('logout/',userLogout),
    path('signup/',UserSignup.as_view()),
    path('detailupdate/',UserViewGeneric.as_view()),
    path('device/',get_device),
]

