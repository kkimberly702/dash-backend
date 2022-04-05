from django.contrib import admin
from .models.user import User
from .models.item import Item

# Register your models here.
admin.site.register(User)
admin.site.register(Item)