# Generated by Django 3.2.7 on 2021-09-27 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(max_length=5)),
                ('unit_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('price', models.FloatField()),
                ('example', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('ingredient', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='inventory.ingredients')),
                ('menu_items', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='inventory.menuitems')),
            ],
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('menu_item', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='inventory.menuitems')),
            ],
        ),
    ]