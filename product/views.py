from django.shortcuts import get_object_or_404, render,HttpResponse
from product.models import Product,Category
from django.views.generic import ListView,DetailView
from django.db.models import Q
from cart.forms import CartAddProductFrom
# Create your views here.

class ListProduct(ListView):
    queryset=Product.objects.product_publish()[:20]
    template_name='products/home.html'
    context_object_name='products'

         
class ProductDetail(DetailView):
    template_name='products/detail.html' 
    context_object_name='product'

    def get_object(self):
        global product
        global slug
        slug=self.kwargs.get('slug')
        product=get_object_or_404(Product.objects.product_publish(),slug=slug)
        return product

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        related_product=Product.objects.filter(title__icontains=product.title[:5],).exclude(slug=slug)[:5]
        context['related_products']=related_product
        context['form']=CartAddProductFrom()
        return context   

class SearchResult(ListView):
    template_name='products/search_result.html'
    context_object_name='products'
    model=Product
    paginate_by=5
    def get_queryset(self):
        query=self.request.GET.get('q',"None")
        object_list=Product.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query) | Q(spec__icontains=query))
        return object_list

class CategoryList(ListView):
    template_name='products/category_list.html'
    context_object_name='products'
    paginate_by=5
    def get_queryset(self):
        slug=self.kwargs.get('slug')
        category=get_object_or_404(Category.objects.category_publish(),slug=slug)
        return category.product.product_publish()