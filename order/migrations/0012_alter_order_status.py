# Generated by Django 3.2.5 on 2021-08-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('unpaid', 'پرداخت نشده'), ('delivered', 'تحویل'), ('sending', 'درحال ارسال'), ('paid', 'پرداخت شده')], default='unpaid', max_length=15, verbose_name='وضعیت'),
        ),
    ]
