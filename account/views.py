from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponse
from django.shortcuts import render
from account.models import User,Address
from django.http.response import HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddressForm, UserForm,SignUpForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils.html import format_html


UserModel = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save() 
            current_site = get_current_site(request)
            mail_subject = 'حساب خود را فعال کنید'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('لطفا ایمیل ادرس خود را تایید کنید تا ساخت حساب کاربری تکمیل شود')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('ممنون از تایید کردن حساب کاربری خود,حالا شما میتوانید وارد حساب خود شود')
    else:
        return HttpResponse('لینک فعال سازی نامعتبر!')



class Profile(LoginRequiredMixin,DetailView):
    model=User
    login_url = 'login'
    template_name='registration/profile.html'
    context_object_name='user'
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)


class UserAddress(LoginRequiredMixin,DetailView):
    model=Address
    login_url = 'login'
    template_name='registration/address.html'
    context_object_name='address'
    def get_object(self):
        return Address.objects.get(pk=self.request.user.address.pk)

class UpdateProfile(LoginRequiredMixin,UpdateView):
    model=User
    form_class=UserForm
    template_name='registration/update_profile.html'
    login_url = 'login'
    success_url=reverse_lazy('account:profile')
    def get_object(self):
        return get_object_or_404(User,pk=self.request.user.pk)

class UpdateAddress(LoginRequiredMixin,UpdateView):
    model=Address
    form_class=AddressForm
    template_name='registration/update_create_address.html'
    success_url=reverse_lazy('account:address')
    def get_object(self):
        return get_object_or_404(Address,pk=self.request.user.pk)



