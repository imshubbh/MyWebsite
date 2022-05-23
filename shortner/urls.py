from django.contrib import admin
from django.urls import path
from shortner import views

urlpatterns = [
    path('<str:pk>/', views.go, name='create'),
    path('calculator/', views.calcPage, name='calc'),
    path('', views.homePage, name='Home' ),
    
]