# Generated by Django 4.0.4 on 2022-04-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
