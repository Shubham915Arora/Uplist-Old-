from django.contrib import admin
from .models import cat,loc,ad,message

# Register your models here.
admin.site.register(cat)
admin.site.register(loc)
admin.site.register(ad)
admin.site.register(message)
