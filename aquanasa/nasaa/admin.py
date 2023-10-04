from django.contrib import admin
from .models import Data

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","age")

admin.site.register(Data, DataAdmin)