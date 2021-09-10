from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.http import request
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
    #check if any fields in address is empty
    def is_empty_field(self):
        for field in self.address._meta.fields:
            fname=field.name
            if not getattr(self.address,fname):
                return False
        else:
            return True



class Address(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='کاربر')
    state=models.CharField(max_length=20,verbose_name='استان')
    city=models.CharField(max_length=50,verbose_name='شهر')
    address=models.TextField(verbose_name='ادرس')
    post_code=models.CharField(max_length=10,verbose_name='کد پستی')
    plaque=models.CharField(max_length=10,verbose_name='پلاک')
    unit=models.CharField(max_length=10,verbose_name='واحد')
    phone_number=models.CharField(max_length=11,verbose_name='شماره تلفن')

    class Meta:
        verbose_name='ادرس'
        verbose_name_plural='ادرس ها'
    
    def __str__(self):
        return str(self.user)

    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Address.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.address.save()