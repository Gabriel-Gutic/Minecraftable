# Generated by Django 3.2.5 on 2021-08-15 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Minecraftable', '0009_auto_20210813_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='tag',
            new_name='tags',
        ),
    ]
