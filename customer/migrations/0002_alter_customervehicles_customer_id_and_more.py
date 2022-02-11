# Generated by Django 4.0.2 on 2022-02-11 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customervehicles',
            name='customer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='customervehicles',
            name='kind',
            field=models.IntegerField(choices=[(1, 'MOTO'), [2, 'CARRO']], null=True),
        ),
    ]