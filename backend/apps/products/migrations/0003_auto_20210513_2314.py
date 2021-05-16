# Generated by Django 3.2 on 2021-05-13 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210511_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='group_tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='products.Tag', verbose_name='Группа тегов'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.category', verbose_name='Категория'),
        ),
        migrations.DeleteModel(
            name='GroupTags',
        ),
    ]
