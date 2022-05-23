from django.contrib import admin
from django.urls import path, include, re_path
from django import views

from django.views.static import serve 
from django.conf import settings
# from django.conf.urls.static import static

from shortner import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('calculator/', views.calcPage, name='calc'),
    path('', include('shortner.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]