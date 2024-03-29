# Generated by Django 3.0.7 on 2020-06-12 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nascimento', models.DateField()),
                ('categoria', models.CharField(choices=[('Ca', 'Cachorro'), ('Ga', 'Gato'), ('Co', 'Coelho')], max_length=2)),
                ('cor', models.CharField(choices=[('Pr', 'Preto'), ('Br', 'Branco'), ('Ci', 'Cinza'), ('Ma', 'Marrom')], max_length=2)),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Cliente')),
            ],
        ),
    ]
