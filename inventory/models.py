from django.db import models

# Create your models here.
	
class Ingredient(models.Model):
	name = models.CharField(max_length=35)
	quantity = models.IntegerField()
	unit = models.CharField(max_length=5)
	unit_price = models.FloatField()

	def __str__(self):
		return self.name

class MenuItem(models.Model):
	title = models.CharField(max_length=35)
	price = models.FloatField()
	example = models.ImageField()

	def __str__(self):
		return self.title

class RecipeRequirement(models.Model):
	menu_items = models.ForeignKey(MenuItem, default = 1,  on_delete=models.SET_DEFAULT)
	ingredient = models.CharField(max_length=35)
	quantity = models.FloatField()

	def __str__(self):
		return str(self.menu_items)


class Purchase(models.Model):
	menu_item = models.ForeignKey(MenuItem, default=1, on_delete=models.SET_DEFAULT)
	timestamp = models.DateTimeField()

	def __str__(self):
		return 'Purchase ' + str(self.menu_item) + str(self.timestamp)