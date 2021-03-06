# Generated by Django 3.2.5 on 2021-08-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Minecraftable', '0004_alter_datapack_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('tag', models.ManyToManyField(to='Minecraftable.Tag')),
            ],
        ),
    ]
