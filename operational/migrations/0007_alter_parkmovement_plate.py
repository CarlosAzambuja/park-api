# Generated by Django 4.0.2 on 2022-02-14 18:05

from django.db import migrations
import operational.models


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0006_parkmovement_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkmovement',
            name='plate',
            field=operational.models.UpperCaseCharField(max_length=255, null=True),
        ),
    ]