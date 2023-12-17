from django.contrib import admin

from accounts.models import *

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category", "description",  "date_created"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "product", "date_created", "status"]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tag)

