from django.urls import path
from . import views

app_name = "tournaments"
urlpatterns = [
    path('tournois', views.tournois, name = 'tournois')
]