from django.urls import path
from .views import Profile,UserAddress,activate,signup,UpdateProfile,UpdateAddress

app_name='account'
urlpatterns=[
    path("profile/",Profile.as_view(),name="profile"),
    path("address/",UserAddress.as_view(),name="address"),
    # path("update_profile/",update_profile,name="update_profile"),
    path('activate/<uidb64>/<token>/',activate, name='activate'),
    path('signup/',signup,name='signup'),
    path('author/update/', UpdateProfile.as_view(), name='author_update'),
    path('address/update/', UpdateAddress.as_view(), name='address_update'),

]
