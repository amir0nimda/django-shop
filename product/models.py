from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.expressions import Col
from account.models import User
from django.urls import reverse
from django.db.models import Q
from django.utils.html import format_html
from django.db.models import Count
# Create your models here.


class ProductManager(models.Manager):
    def product_publish(self):
        return self.filter(status='p')

    def number_of_visits(self):
        return self.annotate(count=Count('visits'))
    

class CategoryManager(models.Manager):
    def category_publish(self):
        return self.filter(status='p')

class Category(models.Model):
    STATUS_CHOICE={
        ('p','انتشار'),
        ('d','پیش نویس'),
    }
    parent=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True,default=None,related_name='children',verbose_name="والد")
    title=models.CharField(max_length=200,verbose_name='عنوان')
    slug=models.SlugField(max_length=100,unique=True,verbose_name='ادرس دسته بندی')
    position=models.IntegerField(verbose_name='پوزیشن')
    status=models.CharField(max_length=1,choices=STATUS_CHOICE,verbose_name='وضعیت')
 
    def get_absolute_url(self):
        return reverse('product:category_list',args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'
        ordering=["position"]
    objects=CategoryManager()

class Color(models.Model):
    code=models.CharField(max_length=50,verbose_name='کد رنگ')
    name=models.CharField(max_length=50,verbose_name='نام رنگ')
    
    def __str__(self):
        return self.name
    def color_pic(self):
        return format_html(f'<p style="background-color:{self.code};width:200px;">{self.name}</p>')
    class Meta:
        verbose_name='رنگ'
        verbose_name_plural='رنگ ها'
    color_pic.short_description = 'رنگ'



class IpAddress(models.Model):
    ip=models.GenericIPAddressField()

    def __str__(self):
        return str(self.ip)


class Product(models.Model):
    STATUS_CHOICE={
        ('p','انتشار'),
        ('d','پیش نویس'),
    }
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='مدیر')
    title=models.CharField(max_length=100,verbose_name='عنوان')
    slug=models.SlugField(max_length=100,unique=True,verbose_name='ادرس محصول')
    category=models.ManyToManyField(Category,verbose_name='دسته ها',related_name='product')
    color=models.ManyToManyField(Color,verbose_name='رنگ',blank=True)
    spec=models.TextField(verbose_name='اطلاعات راجب محصول')
    description=models.TextField(verbose_name='توضیح درباره محصول', blank=True,null=True)
    price=models.FloatField(verbose_name='قیمت کالا')
    thumbnail=models.ImageField(upload_to='image',verbose_name='عکس',blank=False,null=False)
    created=models.DateTimeField(auto_now_add=True,verbose_name='زمان ساخت')
    updated=models.DateField(auto_now=True,verbose_name='زمان تغییر')
    status=models.CharField(max_length=1,choices=STATUS_CHOICE,verbose_name='وضعیت')
    exist=models.BooleanField(default=True,verbose_name='موجود بودن محصول') 
    visits=models.ManyToManyField(IpAddress,related_name='product',verbose_name='تعداد بازدید ها',blank=True)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('product:product_detail',
                        args=[self.slug])

    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'
        ordering=['-created']
    objects=ProductManager()


class ImageProduct(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول',related_name='product_image')
    image=models.FileField(upload_to='image',verbose_name='عکس')

    class Meta:
        verbose_name='عکس'
        verbose_name_plural='عکس ها'


