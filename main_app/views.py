from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Item
from .forms import TrainingForm

class PokemonCreate(CreateView):
  model = Pokemon
  fields = ['name', 'breed', 'description', 'age']

class PokemonUpdate(UpdateView):
  model = Pokemon
  fields = ['breed', 'description', 'age']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemon/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  pokemon = Pokemon.objects.all()
  return render(request, 'pokemon/index.html', { 'pokemon': pokemon })

def pokemon_detail(request, poke_id):
  poke = Pokemon.objects.get(id=poke_id)
  items_pokemon_doesnt_have = Item.objects.exclude(id__in = poke.items.all().values_list('id'))
  training_form = TrainingForm()
  return render(request, 'pokemon/detail.html', {
    'poke': poke, 'training_form': training_form,
    'items': items_pokemon_doesnt_have
  })

def add_training(request, poke_id):
  form = TrainingForm(request.POST)
  if form.is_valid():
    new_training = form.save(commit=False)
    new_training.poke_id = poke_id
    new_training.save()
  return redirect('detail', poke_id=poke_id)


def assoc_item(request, poke_id, item_id):
  Pokemon.objects.get(id=poke_id).items.add(item_id)
  return redirect('detail', poke_id=poke_id)

def unassoc_item(request, poke_id, item_id):
  Pokemon.objects.get(id=poke_id).items.remove(item_id)
  return redirect('detail', poke_id=poke_id)

class ItemList(ListView):
  model = Item

class ItemDetail(DetailView):
  model = Item

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'

class ItemUpdate(UpdateView):
  model = Item
  fields = ['name', 'type']

class ItemDelete(DeleteView):
  model = Item
  success_url = '/items/'
