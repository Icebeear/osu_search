from django.contrib import admin
from django.urls import path, include
from beatmaps import views

app_name = "beatmaps"

urlpatterns = [
    path('', views.MapsView.as_view(), name="index"),
    path('search/', views.FilterMapsView.as_view(), name="search"),
]
