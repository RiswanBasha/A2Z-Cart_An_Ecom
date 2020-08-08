from django.contrib import admin
from .models import Products,Order
# Register your models here.
admin.site.site_header="A2Z Cart Admin"
admin.site.site_title= "A2Z Cart"
admin.site.index_title= "Manage A2Z Cart Shopping"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")


    list_display = ('title','price','discount_price','category','description')
    search_fields= ('title',)
    actions= ('change_category_to_default',)
    list_editable=('price','category',)

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)