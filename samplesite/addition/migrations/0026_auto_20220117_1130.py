# Generated by Django 2.2.24 on 2022-01-17 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addition', '0025_auto_20220117_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество'),
        ),
    ]
