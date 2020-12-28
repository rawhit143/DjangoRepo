from django.urls import path
from JobsApp import views
urlpatterns = [
    path('home/', views.home),
    path('indore/', views.indore),
]
