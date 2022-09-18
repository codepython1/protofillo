from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    # path('home',views.vie),
    path('drawing',views.draw),
    path('jarvis',views.jarvis),
    path('weather',views.weather),
]


