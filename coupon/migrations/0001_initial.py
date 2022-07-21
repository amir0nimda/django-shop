# Generated by Django 3.2.5 on 2022-07-20 09:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='کد')),
                ('valid_from', models.DateTimeField(verbose_name='اعتبار از')),
                ('valid_to', models.DateTimeField(verbose_name='اعتبار تا')),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='درصد تخفیف')),
                ('active', models.BooleanField(verbose_name='فعال')),
            ],
            options={
                'verbose_name': 'کد تخفیف',
                'verbose_name_plural': 'کد تخفیف ها',
            },
        ),
    ]
