# Generated by Django 5.1.1 on 2024-11-15 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_usermodel_alter_customuser_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='newuser',
            fields=[
                ('usern_id', models.IntegerField(primary_key=True, serialize=False)),
                ('usern_name', models.CharField(max_length=100)),
                ('passwordn', models.CharField(max_length=100)),
            ],
        ),
    ]