from django.contrib import admin
from .models import *

admin.site.register(category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','detail','price')
admin.site.register(product,ProductAdmin)

# Register your models here.
