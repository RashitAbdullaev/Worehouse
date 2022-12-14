# Generated by Django 2.2.24 on 2021-11-30 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addition', '0007_auto_20211129_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='coming',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rates_coming', to='addition.Coming', verbose_name='Приход'),
        ),
        migrations.AlterField(
            model_name='coming',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rates_material', to='addition.Material', verbose_name='Материал'),
        ),
    ]
