# Generated by Django 2.2.24 on 2021-11-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addition', '0006_auto_20211129_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='barcode',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='material',
            name='ean',
            field=models.IntegerField(null=True, unique=True, verbose_name='Значения штрихкода'),
        ),
    ]