from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('kimAdmin', views.kimAdmin, name = 'kimAdmin'),
    path("ads.txt", serve, {"document_root": settings.STATICFILES_DIRS[0], "path": "ads.txt"}),
    path('apply', views.apply, name = 'apply'),
]