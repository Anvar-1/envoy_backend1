# Generated by Django 5.1 on 2024-08-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(default='Available', max_length=50)),
            ],
        ),
    ]
