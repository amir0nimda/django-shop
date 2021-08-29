from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from product.models import Category, Product
from account.models import User

class UserAccessMixin():
    def dispatch(self,request,*args,**kwargs):
        user=get_object_or_404(User,pk=request.user.pk)
        if user==request.user or request.user.is_superuser:
            return super().dispatch(request,*args,**kwargs)            
        else:
            raise Http404("You can't access this page")


