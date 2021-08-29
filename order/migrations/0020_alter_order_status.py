# Generated by Django 3.2.5 on 2021-08-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('sending', 'درحال ارسال'), ('paid', 'پرداخت شده'), ('unpaid', 'پرداخت نشده'), ('delivered', 'تحویل')], default='unpaid', max_length=15, verbose_name='وضعیت'),
        ),
    ]
