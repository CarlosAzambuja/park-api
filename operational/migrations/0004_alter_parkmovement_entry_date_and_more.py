# Generated by Django 4.0.2 on 2022-02-11 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customervehicles_customer_id_and_more'),
        ('operational', '0003_alter_parkmovement_validate_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkmovement',
            name='entry_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='parkmovement',
            name='vehicle_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='vehicle_id', to='customer.customervehicles'),
        ),
    ]
