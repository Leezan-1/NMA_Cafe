from django.contrib import admin
from cafeapp.models import Customer, Order, MobileNumber, Food, FoodCategory

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'f_slug':('item_name','price')}
    list_display = ('item_name', 'price')
    

admin.site.register(Food, FoodAdmin)
admin.site.register(FoodCategory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(MobileNumber)