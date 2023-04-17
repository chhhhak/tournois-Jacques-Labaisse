from django.urls import path
from . import views

app_name = "tournaments"
urlpatterns = [
    path('tournois', views.tournois, name = 'tournois'),
    path('tournoi/<int:id_tournoi>', views.tournoi, name = 'tournoi')
]