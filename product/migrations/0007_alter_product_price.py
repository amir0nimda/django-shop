# Generated by Django 3.2.5 on 2021-08-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210803_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='قیمت کالا'),
        ),
    ]
