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
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('car_type', models.CharField(max_length=100)),
                ('car_case', models.CharField(max_length=100)),
                ('load_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.CharField(max_length=50)),
                ('height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start', models.CharField(max_length=200)),
                ('finish', models.CharField(max_length=200)),
                ('current_time', models.DateTimeField(auto_now=True)),
                ('load_time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('plastic_card', models.DecimalField(decimal_places=2, max_digits=20)),
                ('price_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_type', models.CharField(choices=[('naqd pul', 'Naqd pul'), ('card', 'Card'), ('humo_card', 'Humo_Card'), ('uzcard', 'Uzcard')], default='cash', max_length=50)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drivers.driver')),
            ],
        ),
    ]
