from django.db import models
from product.models import Product
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, \
 MaxValueValidator
from account.models import User,Address
from coupon.models import Coupon
# Create your models here.
 

class Order(models.Model):
    STATUS_CHOICE={
        ('unpaid','پرداخت نشده'),
        ('paid','پرداخت شده'),
        ('sending','درحال ارسال'),
        ('delivered','تحویل'),

    }
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    address=models.ForeignKey(Address,on_delete=models.CASCADE,verbose_name="ادرس",blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name='ساخت شده')
    updated=models.DateTimeField(auto_now=True,verbose_name='بروز رسانی شده')
    status = models.CharField(max_length=15,choices=STATUS_CHOICE,verbose_name='وضعیت',default='unpaid')
    discount = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    coupon = models.ForeignKey(Coupon,related_name='orders',null=True,blank=True,on_delete=models.SET_NULL)
    class Meta:
        verbose_name='سفارش'
        verbose_name_plural='سفارشات'

    def __str__(self):
        return str(self.user)    
        
    def update_time(self):
        if self.updated!=self.created:
            return self.updated
        else:
            return "اپدیت نشده است"
    update_time.short_description='زمان اپدیت'

    # def get_total_cost(self):
    #     total_cost = sum(item_product.get_cost() for item_product in self.item.all())
    #     return total_cost - total_cost * \
    #         (self.discount / float(100))
    # get_total_cost.short_description='قیمت کل '


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='item',verbose_name='سفارش')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_item",verbose_name='محصول')
    price=models.FloatField(verbose_name='قیمت')
    total_price=models.FloatField(verbose_name='قیمت کل',default=1)
    color=models.CharField(max_length=50,verbose_name='رنگ',default='سفید')
    quantity=models.IntegerField(default=1,verbose_name='تعداد')

    class Meta:
        verbose_name='کالا'
        verbose_name_plural='کالاها'

    def __str__(self):
        return str(self.product)

    def get_cost(self):
        return self.price * self.quantity
    get_cost.short_description='کل قیمت'

    def save(self,*args,**kwargs):
        self.total_price=self.get_cost()
        super(OrderItem, self).save(*args, **kwargs)
