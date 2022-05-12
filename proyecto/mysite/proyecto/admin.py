from django.contrib import admin
from proyecto.models import Game, Player, GamePlayer


class PlayerAdmin(admin.ModelAdmin):    
    search_fields = ('name',)
    list_display = ('name', 'age')

class Gameadmin(admin.ModelAdmin):
    date_hierarchy = ('fecha')


# Register your models here.
admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, Gameadmin)
admin.site.register(GamePlayer)