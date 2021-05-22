from django.urls import path
from .views import HomePage_views

urlpatterns = [
    path('',HomePage_views,name="home"),
]