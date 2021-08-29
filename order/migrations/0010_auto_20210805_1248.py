# Generated by Django 3.2.5 on 2021-08-05 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_address'),
        ('order', '0009_auto_20210805_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='plaque',
        ),
        migrations.RemoveField(
            model_name='order',
            name='post_code',
        ),
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
        migrations.RemoveField(
            model_name='order',
            name='unit',
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.address', verbose_name='ادرس'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('sending', 'درحال ارسال'), ('delivered', 'تحویل'), ('unpaid', 'پرداخت نشده'), ('paid', 'پرداخت شده')], default='unpaid', max_length=15, verbose_name='وضعیت'),
        ),
    ]
