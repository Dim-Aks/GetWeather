from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/city_searches/', views.CitySearchList.as_view(), name='city-search-list'),
]