# Generated by Django 3.2.5 on 2021-08-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Minecraftable', '0003_auto_20210811_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapack',
            name='version',
            field=models.PositiveSmallIntegerField(choices=[(4, '1.13 - 1.14.4'), (5, '1.15 - 1.16.1'), (6, '1.16.2 - 1.16.5'), (7, '1.17')], default=7),
        ),
    ]