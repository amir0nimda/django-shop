# Generated by Django 3.2.5 on 2021-08-22 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='color',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='total_price',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('delivered', 'تحویل'), ('paid', 'پرداخت شده'), ('unpaid', 'پرداخت نشده'), ('sending', 'درحال ارسال')], default='unpaid', max_length=15, verbose_name='وضعیت'),
        ),
    ]
