from django.contrib import admin
from .models import Category,Product,ImageProduct,Color,IpAddress
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','position','slug','parent']
    list_filter=['title']
    search_fields=['title','slug','description']

admin.site.register(Category,CategoryAdmin)


class ImageProductAdmin(admin.StackedInline):
    model = ImageProduct


class ProductAdmin(admin.ModelAdmin):
    list_display=['title','slug','status']
    list_filter=['slug','category',]
    search_fields=['category','spec','slug']
    ordering=['-updated']
    inlines = [ImageProductAdmin]   
admin.site.register(Product,ProductAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display=["color_pic"]
    list_filter=['name']
    search_fields=['name']

admin.site.register(Color,ColorAdmin)

admin.site.register(IpAddress)
