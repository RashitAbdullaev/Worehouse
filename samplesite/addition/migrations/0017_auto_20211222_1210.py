# Generated by Django 2.2.24 on 2021-12-22 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addition', '0016_auto_20211214_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество'),
        ),
    ]