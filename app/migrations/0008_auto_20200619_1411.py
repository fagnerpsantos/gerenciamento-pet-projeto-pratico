# Generated by Django 3.0.7 on 2020-06-19 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200619_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultapet',
            name='peso_atual',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
