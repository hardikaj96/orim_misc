from django.urls import path
from . import views

urlpatterns = [
    path("", views.keyword_index, name="keyword_index"),
    path("<str:kw>/", views.keyword_details, name="keyword_details"),
]