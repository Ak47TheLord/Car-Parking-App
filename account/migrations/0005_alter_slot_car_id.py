# Generated by Django 3.2.6 on 2021-08-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_slot_vacant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='car_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
