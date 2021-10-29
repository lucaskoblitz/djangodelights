from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Ingredient, Purchase, MenuItem, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, PurchaseForm, RecipeRequirementForm
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

class CreateMenuItem(CreateView):
	template_name= 'inventory/add_menu_item.html'
	form_class = MenuItemForm
	model = MenuItem

class CreateIngredient(CreateView):
	template_name= 'inventory/add_ingredient.html'
	form_class = IngredientForm
	model = Ingredient

class CreateRecipeRequirement(CreateView):
	template_name= 'inventory/add_recipe.html'
	form_class = RecipeRequirementForm
	model = RecipeRequirement

class CreatePurchase(CreateView):
	template_name= 'inventory/add_purchase.html'
	form_class = PurchaseForm
	model = Purchase
