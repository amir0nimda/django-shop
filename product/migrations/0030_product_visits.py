# Generated by Django 3.2.5 on 2021-09-10 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_auto_20210910_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visits',
            field=models.ManyToManyField(related_name='product', to='product.IpAddress', verbose_name='تعداد بازدید ها'),
        ),
    ]