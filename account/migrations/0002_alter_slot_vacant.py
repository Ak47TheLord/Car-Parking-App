# Generated by Django 3.2.6 on 2021-08-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='vacant',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=True, max_length=10),
        ),
    ]
