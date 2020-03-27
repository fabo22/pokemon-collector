from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('pokemon/', views.pokemon_index, name='index'),
  path('pokemon/<int:poke_id>/', views.pokemon_detail, name='detail'),
  path('pokemon/create/', views.PokemonCreate.as_view(), name='pokemon_create'),
  path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon_update'),
  path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon_delete'),
  path('pokemon/<int:poke_id>/add_training/', views.add_training, name='add_training'),
  path('pokemon/<int:poke_id>/assoc_item/<int:item_id>/', views.assoc_item, name='assoc_item'),
  path('pokemon/<int:poke_id>/unassoc_item/<int:item_id>/', views.unassoc_item, name='unassoc_item'),
  path('items/', views.ItemList.as_view(), name='items_index'),
  path('items/<int:pk>/', views.ItemDetail.as_view(), name='items_detail'),
  path('items/create/', views.ItemCreate.as_view(), name='items_create'),
  path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='items_update'),
  path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
]