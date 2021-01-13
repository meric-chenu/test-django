
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.view_home,name="home"),
    path('contact/',include("contact.urls")),
    path("articles/",include("articles.urls")),
    path("utilisateurs/",include("utilisateurs.urls")),
]
