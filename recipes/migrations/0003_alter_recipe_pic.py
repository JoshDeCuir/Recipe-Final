# Generated by Django 4.2.8 on 2023-12-17 20:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0002_recipe_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="pic",
            field=models.ImageField(default="no_picture.jpg", upload_to="recipes"),
        ),
    ]
