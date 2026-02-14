from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('department',views.department,name='department'),
    path('contact',views.contact,name='contact'),
]

