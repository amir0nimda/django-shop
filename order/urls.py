from django.urls import path
from .views import order_create,show_session

app_name='orders'
urlpatterns=[
    path('create/',order_create,name="order_create"),
    path('show_session/',show_session,name="show_session"),

    
]