# Generated by Django 3.2.7 on 2021-09-27 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
        migrations.RenameModel(
            old_name='MenuItems',
            new_name='MenuItem',
        ),
        migrations.RenameModel(
            old_name='Purchases',
            new_name='Purchase',
        ),
        migrations.RenameModel(
            old_name='RecipeRequirements',
            new_name='RecipeRequirement',
        ),
    ]
