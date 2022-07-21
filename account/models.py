from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.http import request
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin,Group


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError('User must have a phone number')
        user=self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email
        """
        user = self.create_user(
            phone=phone,
            password=password,
        )
        user.is_admin = True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class AddressManger(models.Manager):
    def active_address(self,pk,user):
        objects=self.filter(user=user).update(activeـaddress=False)
        requested_object=self.get(pk=pk,user=user)
        requested_object.activeـaddress=True
        requested_object.save()
        return 


class User(AbstractBaseUser,PermissionsMixin):
    groups = models.ManyToManyField(Group)
    name = models.CharField(max_length=128, null=True)
    email = models.EmailField(verbose_name='email field', max_length=60, unique=True,null=True,blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='date joined', auto_now=True)    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone_regex=RegexValidator(regex=r'09(\d{9})$', 
    message='Enter a valid mobile number. This value may contain only numbers.')
    phone = models.CharField(verbose_name='phone field', max_length=11, unique=True,
    validators=[phone_regex])
    
    objects = UserManager()
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS = []

    def empty_field_address(self):
        '''
        It checks if any field of the address model is empty and returns a false value.
        '''
        get_address=self.address_set.get(activeـaddress=True)
        for field in get_address._meta.fields:
            if not getattr(get_address,field.name):
                return False
        else:
            return True


class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    state=models.CharField(max_length=20,verbose_name='استان')
    city=models.CharField(max_length=50,verbose_name='شهر')
    address=models.TextField(verbose_name='ادرس')
    post_code=models.CharField(max_length=10,verbose_name='کد پستی')
    plaque=models.CharField(max_length=10,verbose_name='پلاک')
    unit=models.CharField(max_length=10,verbose_name='واحد')
    phone_number=models.CharField(max_length=11,verbose_name='شماره تلفن')
    activeـaddress=models.BooleanField(default=False)

    objects=AddressManger()

    class Meta:
        verbose_name='ادرس'
        verbose_name_plural='ادرس ها'
    
    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        address=Address(user=instance)
        address.activeـaddress=True
        address.save()
