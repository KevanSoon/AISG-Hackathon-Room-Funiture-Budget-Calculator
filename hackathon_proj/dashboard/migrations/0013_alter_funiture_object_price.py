# Generated by Django 3.2.9 on 2021-12-09 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_funiture_object_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funiture',
            name='object_price',
            field=models.FloatField(default=0),
        ),
    ]
