from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView 
from .models import Ingredient, Purchase, MenuItem, RecipeRequirement
from .forms import IngredientForm
from decimal import *
# Create your views here.

def home(request):
	return render(request, 'inventory/home.html')

class Inventory(ListView):
	model = Ingredient


class PurchaseList(ListView):
	model = Purchase

class Menu_itemList(ListView):
	model = MenuItem


class Results(TemplateView):
	template_name = 'inventory/results.html'

	@property
	def cost(self):
		total_cost = Decimal(0.00)
		recipe = Purchase.objects.all()
		for i in recipe:
			total_cost += i.menuitem.recipe_prices()
		return	total_cost

	@property
	def revenue(self):
		rev = Decimal(0.00)
		purchase_objects = Purchase.objects.all()
		for i in purchase_objects:
			rev += i.menuitem.price
		return rev

	def get_context_data(self):
		context = super().get_context_data()
		context['totalcost'] = self.cost
		context['revenue'] = self.revenue
		context['grossprofit'] = self.revenue - self.cost
		return context

class UpdateIngredient(UpdateView):
	template_name= 'inventory/update_ingredient.html'
	form_class = IngredientForm
	model = Ingredient