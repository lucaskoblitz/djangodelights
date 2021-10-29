from django.db import models
from decimal import *

# Create your models here.
	
class Ingredient(models.Model):
	name = models.CharField(max_length=35)
	quantity = models.IntegerField()
	unit = models.CharField(max_length=5)
	unit_price = models.DecimalField(max_digits=10, decimal_places=2)

	def get_absolute_url(self):
		return '/ingredient'

	def __str__(self):
		return self.name

class MenuItem(models.Model):
	title = models.CharField(max_length=35)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)

	def recipe_prices(self):
		total_price = Decimal(0.00)
		ingredients_list = self.reciperequirement_set.all()
		for i in ingredients_list:
			total_price += i.ingredient_cost
		return total_price

	def __str__(self):
		return self.title

class RecipeRequirement(models.Model):
	menuitem = models.ForeignKey(MenuItem,  on_delete=models.CASCADE)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, default=0)
	quantity = models.DecimalField(max_digits=3, decimal_places=0, default=1)

	@property
	def ingredient_cost(self):
		return self.ingredient.unit_price * self.quantity
	
	def __str__(self):
		return str(self.menuitem)


class Purchase(models.Model):
	menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
	timestamp = models.DateTimeField()

	def get_absolute_url(self):
		return '/purchase'


	def __str__(self):
		return 'Purchase ' + str(self.menuitem) + str(self.timestamp)