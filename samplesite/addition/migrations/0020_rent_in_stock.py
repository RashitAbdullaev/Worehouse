# Generated by Django 2.2.24 on 2022-01-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addition', '0019_auto_20220111_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='in_stock',
            field=models.IntegerField(null=True, verbose_name='в наличии'),
        ),
    ]
