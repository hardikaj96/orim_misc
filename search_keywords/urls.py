from django.urls import path
from search_keywords import views

urlpatterns = [
    path('', views.search_keywords, name='search_keywords'),
]