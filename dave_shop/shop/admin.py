from django.contrib import admin
from .models import Category, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","price"]
    list_filter =["category"]
    prepopulated_fields = {"slug": ('title',) }

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

