# Generated by Django 4.0.2 on 2022-02-11 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerVehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=10)),
                ('kind', models.IntegerField(blank=True, choices=[(1, 'MOTO'), [2, 'CARRO']])),
                ('customer_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
