# Generated by Django 4.1.2 on 2022-11-08 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
