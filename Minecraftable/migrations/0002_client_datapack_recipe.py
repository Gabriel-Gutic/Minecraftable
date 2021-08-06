# Generated by Django 3.2.5 on 2021-08-06 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Minecraftable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Minecraftable.user')),
            ],
        ),
        migrations.CreateModel(
            name='Datapack',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Minecraftable.client')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('json_data', models.TextField(blank=True)),
                ('datapack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Minecraftable.datapack')),
            ],
        ),
    ]