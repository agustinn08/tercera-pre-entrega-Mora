# Generated by Django 5.0 on 2023-12-24 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_remove_zapatillas_imagen_zapatillas_imagen_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapatillas',
            name='imagen_url',
            field=models.URLField(default='https://ibb.co/qy1DD7Y'),
        ),
    ]
