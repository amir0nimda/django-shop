# Generated by Django 3.2.5 on 2021-09-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0026_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('sending', 'درحال ارسال'), ('delivered', 'تحویل'), ('paid', 'پرداخت شده'), ('unpaid', 'پرداخت نشده')], default='unpaid', max_length=15, verbose_name='وضعیت'),
        ),
    ]
