# Generated by Django 5.1.1 on 2025-02-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=15)),
                ('messages', models.CharField(max_length=300)),
                ('time_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
