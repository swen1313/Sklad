# Generated by Django 3.2.6 on 2021-09-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qty', models.PositiveIntegerField(verbose_name='quantity')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('date_of_upload', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('units', models.CharField(choices=[('piece', 'штука'), ('kilo', 'килограмм'), ('litr', 'литр')], default='piece', max_length=10)),
            ],
        ),
    ]
