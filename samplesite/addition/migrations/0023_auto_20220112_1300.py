# Generated by Django 2.2.24 on 2022-01-12 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addition', '0022_auto_20220112_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='addition.Material', verbose_name='материал'),
        ),
    ]