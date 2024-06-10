from django.contrib import admin

# Register your models here.
from .models import *


class ImagesTublerinline(admin.TabularInline):
    model = Images

class TagTublerinline(admin.TabularInline):
    model = Tag

class Productadmin(admin.ModelAdmin):
    inlines = [ImagesTublerinline,TagTublerinline]

class OrderItemTubleinline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTubleinline]
    list_display = ['firstname','phone','email','payment_id','paid','date']
    search_fields = ['firstname','email','payment_id']


admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product,Productadmin)
admin.site.register(Contact_us)

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)

