# Generated by Django 3.2.9 on 2021-12-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_room_funiture_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='uploads/post_photos'),
        ),
    ]