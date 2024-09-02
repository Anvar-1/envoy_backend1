# Generated by Django 5.1 on 2024-08-30 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=50, verbose_name='car name')),
                ('car_number', models.CharField(max_length=20, verbose_name='car number')),
                ('car_type', models.CharField(max_length=50, verbose_name='car type')),
                ('car_case', models.CharField(max_length=50, verbose_name='car case')),
                ('load_weight', models.FloatField(blank=True, null=True, verbose_name='load weight')),
                ('size', models.CharField(max_length=50, verbose_name='size')),
                ('height', models.FloatField(blank=True, null=True, verbose_name='height')),
                ('length', models.FloatField(blank=True, null=True, verbose_name='length')),
                ('width', models.FloatField(blank=True, null=True, verbose_name='width')),
                ('Driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drivers.driver')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
