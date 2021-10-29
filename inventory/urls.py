from django.urls import path
from . import views
from django.views.generic import ListView

urlpatterns = [
	path('', views.home, name="home"),
	path('inventory/', views.Inventory.as_view(), name='inventory'),
	path('purchase/', views.PurchaseList.as_view(), name='purchase'),
	path('menu/', views.Menu_itemList.as_view(), name='menu'),
	path('menu/<pk>/update', views.UpdateIngredient.as_view(), name='update_ingredient'),
	path('results/', views.Results.as_view(), name='result'),
]