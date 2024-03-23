from django.contrib import admin
from .models import Properties, Contract, PropertiesSale, SaleCart, Sale, StaffProfile

# Register your models here.
admin.site.register(Properties)
admin.site.register(Contract)
admin.site.register(PropertiesSale)
admin.site.register(SaleCart)
admin.site.register(Sale)
admin.site.register(StaffProfile)