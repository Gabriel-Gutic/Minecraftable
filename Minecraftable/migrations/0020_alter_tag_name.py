# Generated by Django 3.2.5 on 2021-09-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Minecraftable', '0019_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
