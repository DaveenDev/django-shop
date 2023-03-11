from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderItems

admin.site.site_header="E-commerce Site"
admin.site.site_title="Dave Shop"
admin.site.index_title="Manage " + admin.site.site_title

# Register your models here.



class ProductAdmin(admin.ModelAdmin):
     
    def change_category_to_default(self,request,queryset):
        queryset.update(category='default')

    list_display = ["title","price", 'discounted_price', 'category']
    list_filter =["category"]
    list_editable=['category']
    prepopulated_fields = {"slug": ('title',) }
    search_fields=["title"]
    actions = ('change_category_to_default')

class OrderItemsList(admin.TabularInline):
    model=OrderItems
    #prepopulated_fields = {"item_price": ('price',)}

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','order_date','customer','ordered_items','order_total']
    inlines =[
        OrderItemsList
    ]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)

