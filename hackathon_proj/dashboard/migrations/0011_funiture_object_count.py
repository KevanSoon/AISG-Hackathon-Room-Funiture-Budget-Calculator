# Generated by Django 3.2.9 on 2021-12-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20211209_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='funiture',
            name='object_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]