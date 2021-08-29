from django.urls import path
from .views import (
    ListProduct,
    SearchResult,
    ProductDetail,
    CategoryList,
    )

app_name='product'

urlpatterns=[
    path('',ListProduct.as_view(),name='home'), 
    path('search_result/',SearchResult.as_view(),name='search_result'),
    path('item/<slug:slug>/',ProductDetail.as_view(),name='product_detail'),
    path('products/category/<slug:slug>/',CategoryList.as_view(),name='category_list'),
]