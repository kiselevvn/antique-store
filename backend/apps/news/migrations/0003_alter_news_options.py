# Generated by Django 3.2 on 2021-04-16 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210416_0343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date_created'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
