from django.contrib import admin

from .models import Product
from .models import Shop

admin.site.register(Product)
admin.site.register(Shop)
# Register your models here.
