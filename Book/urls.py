from django.contrib import admin
from django.urls import path
from Book import views

urlpatterns = [
  path('', views.index, name="Book"),
  path('display', views.display, name="Book"),
  path('submit', views.submit, name="Book"),
]