from django.urls import path
from .views import Login_View

urlpatterns = [
    path('',Login_View,name="login"),
]
