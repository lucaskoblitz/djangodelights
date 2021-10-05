from django.shortcuts import render
from django.views.generic import ListView
from .models import Ingredient, Purchase, MenuItem
# Create your views here.

def home(request):
	return render(request, 'inventory/home.html')

class Inventory(ListView):
	model = Ingredient

class PurchaseList(ListView):
	model = Purchase

class Menu_itemList(ListView):
	model = MenuItem