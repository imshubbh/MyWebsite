from django.contrib import admin
from django.urls import path
from shortner import views

urlpatterns = [
    path('<str:pk>/', views.go, name='create'),
    path('', views.homePage, name='Home' ),
    path('calculator', views.calcPage, name='Calculator')
]