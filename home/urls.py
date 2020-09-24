from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('home', views.index),
    path('course',views.course),
    path('blogs', views.blogs),
    path('contact', views.contact),
    path('about', views.about)

]