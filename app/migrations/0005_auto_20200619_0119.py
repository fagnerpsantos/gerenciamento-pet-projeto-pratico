# Generated by Django 3.0.7 on 2020-06-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_consultapet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultapet',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
    ]
