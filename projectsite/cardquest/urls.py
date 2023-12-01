from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list', views.TrainerList.as_view(), name='trainer-list'),
    path('pokemon_card', views.PokemonCardList.as_view(), name='pokemon-card'),
    path('collection', views.CollectionList.as_view(), name='collection'),
]