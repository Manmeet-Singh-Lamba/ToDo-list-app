from django.urls import path
from . import views


urlpatterns = [
    path('login/sign-up/', views.register, name = 'sign-up')
]
