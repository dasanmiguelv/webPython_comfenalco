from django.contrib import admin
from .models import Menu

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_filter = ('type_dish',)
    search_fields = ('name',)


admin.site.register(Menu, MenuAdmin)
