from django.contrib import admin
from restaurants.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'address',
        'contact',
        'open_time',
        'close_time',
        'last_order',
        'regular_holiday',
    )
    list_filter = ('regular_holiday',)
    search_fields = ('name', 'address', 'contact')
    ordering = ('id',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Restaurant Info', {
            'fields': ('name', 'address', 'contact', 'open_time', 'close_time', 'last_order', 'regular_holiday')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
