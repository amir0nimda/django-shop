from django import template
from ..models import Category
from django.http import request

register = template.Library()

@register.inclusion_tag("products/partials/navbar.html",takes_context=True)
def navbar(context):
    request=context['request']
    return{
        'categorys':Category.objects.category_publish(),
        'request':request
    }


