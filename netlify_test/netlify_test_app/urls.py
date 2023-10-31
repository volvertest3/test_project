from django.urls import path
from .import views

urlpatterns = [
    path("",views.home),
    path("say-hello",views.say_hello),
]