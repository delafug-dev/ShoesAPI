# Generated by Django 4.0.4 on 2022-05-12 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('descriptionShoes', models.TextField(default='pendiente', max_length=150)),
                ('priceShoes', models.FloatField(null=True)),
                ('imageUrl', models.TextField(default='inserte URL de la image')),
            ],
        ),
    ]
