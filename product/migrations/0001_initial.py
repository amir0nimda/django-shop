# Generated by Django 3.2.5 on 2021-07-25 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='ادرس دسته بندی')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
                ('status', models.CharField(choices=[('d', 'پیش نویس'), ('p', 'انتشار')], max_length=1, verbose_name='وضعیت')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='product.category', verbose_name='والد')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='ادرس محصول')),
                ('spec', models.TextField(verbose_name='اطلاعات راجب محصول')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیح درباره محصول')),
                ('price', models.DecimalField(decimal_places=1, max_digits=20, verbose_name='قیمت کالا')),
                ('thumbnail', models.ImageField(upload_to='image', verbose_name='عکس')),
                ('product_number', models.IntegerField(verbose_name='تعداد کالا')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('updated', models.DateField(auto_now=True, verbose_name='زمان تغییر')),
                ('status', models.CharField(choices=[('d', 'پیش نویس'), ('p', 'انتشار'), ('f', 'محصولات ویژه')], max_length=1, verbose_name='وضعیت')),
                ('exist', models.BooleanField(default=True, verbose_name='موجود بودن محصول')),
                ('category', models.ManyToManyField(related_name='product', to='product.Category', verbose_name='دسته ها')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='مدیر')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_size', models.CharField(blank=True, max_length=100, null=True, verbose_name='اندازه محصول')),
                ('size', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_size', to='product.product')),
            ],
            options={
                'verbose_name': 'اندازه',
                'verbose_name_plural': 'اندازه ها',
            },
        ),
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='image', verbose_name='عکس')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'عکس',
                'verbose_name_plural': 'عکس ها',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام رنگ')),
                ('code', models.CharField(max_length=30, verbose_name='کد رنگ')),
                ('color', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_color', to='product.product')),
            ],
            options={
                'verbose_name': 'رنگ',
                'verbose_name_plural': 'رنگ ها',
            },
        ),
    ]
