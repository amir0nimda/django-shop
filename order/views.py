from django.shortcuts import redirect, render
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem,Order
from account.models import User
import functools


def premision_decorator(func):
    functools.wraps(func)
    def wrapper_order_login_required(request):
        if request.user.is_authenticated and request.user.is_empty_field:
            return func(request)
        elif not request.user.is_authenticated: 
            return redirect('login')
        else:
            return redirect('account:profile')
    return wrapper_order_login_required


@premision_decorator
def order_create(request):
        cart=Cart(request)
        get_user=User.objects.get(username=request.user)
        order=Order.objects.filter(user=get_user.id,status='unpaid')
        if request.method=="POST":
            if order.exists():
                get_order=order[0]
                if cart.coupon:
                    get_order.coupon=cart.coupon
                    get_order.discount=cart.coupon.discount
                    get_order.save()
                    del request.session["coupon_id"]
                for item in cart:
                    OrderItem.objects.create(order=get_order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                    color=item['color'],
                    )
                cart.clear()
                return redirect('product:home')                   
            else:
                form_order=OrderCreateForm(request.POST,request.user)
                create=form_order.save(commit=False)
                create.user=request.user
                create.address=get_user.address
                if cart.coupon:
                    create.coupon = cart.coupon
                    create.discount = cart.coupon.discount
                    del request.session["coupon_id"]
                if form_order.is_valid():
                    create.save()
                    for item in cart:
                        OrderItem.objects.create(order=create,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity'],
                        color=item['color'],
                        )
                    cart.clear()
                    return redirect('product:home')
        else:
            form_order=OrderCreateForm()      
        return render(request,'order/create_order.html',{"user":get_user,'form':form_order,"cart":cart})  

