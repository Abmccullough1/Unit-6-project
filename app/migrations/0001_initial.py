# Generated by Django 4.2.6 on 2023-12-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('username', models.TextField(max_length=24)),
                ('password', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('address', models.TextField()),
                ('city', models.TextField()),
                ('zip_code', models.IntegerField()),
                ('size', models.IntegerField()),
                ('available', models.BooleanField()),
            ],
        ),
    ]
