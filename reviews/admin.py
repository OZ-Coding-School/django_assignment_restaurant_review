from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'restaurant',
        'title',
        'comment',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'created_at',
    )
    search_fields = (
        'user__nickname',
        'user__email',
        'restaurant__name',
        'title',
        'comment',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    fieldsets = (
        (
            'Review',
            {
                'fields': (
                    'user',
                    'restaurant',
                    'title',
                    'comment',
                )
            },
        ),
        (
            'Timestamps',
            {
                'fields': (
                    'created_at',
                    'updated_at',
                )
            },
        ),
    )
    ordering = (
        'created_at',
    )

