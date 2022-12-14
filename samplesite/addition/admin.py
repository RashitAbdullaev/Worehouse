from django.contrib import admin

from .models import *


class –°ategoriesAdmin(admin.ModelAdmin):
    list_display = ('title',)


class Material_typeAdmin(admin.ModelAdmin):
    list_display = ('title_material_type', 'category')
    search_fields = ('title_material_type', 'category')


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('pk','title_material', 'material_type', 'ean','unit','material_type','barcode')


class ComingAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'general_price', 'unit_price', 'currency', 'date', 'warehouse', 'material')


class RentAdmin(admin.ModelAdmin):
    list_display = ('date_of_delivery', 'worker', 'material', 'quantity','date_of_issue')
    readonly_fields = ['date_of_issue','date_of_delivery']


admin.site.register(–°ategories, –°ategoriesAdmin)
admin.site.register(Material_type, Material_typeAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Coming, ComingAdmin)
admin.site.register(Rent, RentAdmin)
