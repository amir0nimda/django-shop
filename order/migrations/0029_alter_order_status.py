# Generated by Django 3.2.5 on 2021-09-10 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0028_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('delivered', 'تحویل'), ('sending', 'درحال ارسال'), ('unpaid', 'پرداخت نشده'), ('paid', 'پرداخت شده')], default='unpaid', max_length=15, verbose_name='وضعیت'),
        ),
    ]
