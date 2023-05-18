from django.contrib import admin
# Register your models here.
from .models import *
admin.site.register(Custumer)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Shop)