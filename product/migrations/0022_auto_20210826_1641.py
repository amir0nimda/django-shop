# Generated by Django 3.2.5 on 2021-08-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20210826_1148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'رنگ', 'verbose_name_plural': 'رنگ ها'},
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('p', 'انتشار'), ('d', 'پیش نویس')], max_length=1, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(to='product.Color', verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('p', 'انتشار'), ('d', 'پیش نویس')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
