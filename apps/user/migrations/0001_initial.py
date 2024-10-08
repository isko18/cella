# Generated by Django 5.1 on 2024-08-10 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='employees/')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='user.employee')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
