# Generated by Django 3.2.6 on 2021-08-23 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_slot_vacant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='vacant',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=True, max_length=10),
        ),
    ]
