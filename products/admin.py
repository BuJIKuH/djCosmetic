from django.contrib import admin

from products.models import ProductsModel, CategoryLineModels

admin.site.register(ProductsModel)
admin.site.register(CategoryLineModels)
