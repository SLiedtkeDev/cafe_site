from django.contrib import admin
from .models import Menu, Food


class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('title', 'description', 'order', 'active')
    search_fields = ('title', 'order')


class FoodAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('name', 'description', 'cost', 'order',
                    'previous_cost', 'recommended', 'menu')
    search_fields = ('title', 'order', 'menu')


admin.site.register(Menu, MenuAdmin)
admin.site.register(Food, FoodAdmin)
