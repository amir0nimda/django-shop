# Generated by Django 3.2.5 on 2022-07-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('delivered', 'تحویل'), ('unpaid', 'پرداخت نشده'), ('sending', 'درحال ارسال'), ('paid', 'پرداخت شده')], default='unpaid', max_length=15, verbose_name='وضعیت'),
        ),
    ]
