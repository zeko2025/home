"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main),
    path('karim/', views.karim),
    path('malak/', views.malak),
    path('elias/', views.elias),
    path('abdelrahman/', views.abdelrahman),
    path('ahmed/', views.ahmed),
    path('sief/', views.sief),
    path('ramy/', views.ramy),
    path('sec/', views.second),
    path('articles/', views.all_articles),
    path('details/<n>', views.article_details),
    #path('css/',views.css),
    path('form',views.form),
    path('create',views.add_article),
    path('delete/<n>',views.delete_article),
    path('update/<n>',views.update_article),
    path('home',views.Home),
    #path('home2/',views.Home2),
    #path('category/',views.cate),
    #path('work/',views.WORK),
    #path('about/',views.About),
    #path('home3/',views.Home3),
    #path('around/',views.About2),
    #path('home4/',views.Home4),
#   path('contact/',views.contact),
   #path('team/',views.Team),
   #path('home5/',views.Home5),

]
