# Generated by Django 3.2 on 2021-05-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orderposition_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderposition',
            name='count',
            field=models.IntegerField(verbose_name='Количество'),
        ),
    ]