from django.contrib import admin
from catalog.models import Products, Category
from blogs.models import Blogpost


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_category')
    list_filter = ('product_category',)
    search_fields = ('product_name', 'product_description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_description')



class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    # list_filter = ('product_category',)
    search_fields = ('title',)
