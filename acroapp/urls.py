from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('news', views.news, name='news'),
    path('ms', views.ms, name='ms'),
    path('calendar', views.calendar, name='calendar'),
    path('wall', views.wall, name='wall'),
    path('coach', views.coach, name='coach'),
    path('contacts', views.contacts, name='contacts'),
    path('article/<str:art>', views.article, name='article'),
    path('groups', views.groups, name='groups'),
]