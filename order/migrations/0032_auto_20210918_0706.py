# Generated by Django 3.2.5 on 2021-09-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0031_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('delivered', 'تحویل'), ('paid', 'پرداخت شده'), ('sending', 'درحال ارسال'), ('unpaid', 'پرداخت نشده')], default='unpaid', max_length=15, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='رنگ'),
        ),
    ]