from django.contrib import admin

from blogs.models import Blogpost


@admin.register(Blogpost)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    # list_filter = ('product_category',)
    search_fields = ('title',)

# Register your models here.
