from django.shortcuts import redirect
import functools
from cart.cart import Cart

def premision_decorator(func):
    functools.wraps(func)
    def wrapper_order_login_required(request):
        if request.user.is_authenticated and request.user.is_not_empty_field() \
            and request.session.get('cart'):
            return func(request)    

        elif not request.user.is_authenticated: 
            return redirect('login')

        elif not request.session.get('cart'):
            return redirect('cart:cart_detail')

        else:
            return redirect('account:address_update')

    return wrapper_order_login_required