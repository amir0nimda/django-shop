# Generated by Django 3.2.5 on 2022-07-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('unpaid', 'پرداخت نشده'), ('delivered', 'تحویل'), ('paid', 'پرداخت شده'), ('sending', 'درحال ارسال')], default='unpaid', max_length=15, verbose_name='وضعیت'),
        ),
    ]
