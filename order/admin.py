from django.contrib import admin
from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['type_of_application', 'exactly_name_application', 'name',
                    'date', 'status', 'relevant']
    list_display_links = ['type_of_application', 'name']
    list_editable = ['status', 'relevant']
    readonly_fields = ['type_of_application', 'exactly_name_application',
                       'name', 'phone', 'email', 'question', 'date']
    list_filter = ['date', 'status', 'relevant', 'type_of_application']
    list_per_page = 15

    fieldsets = (
        (None, {
            'fields': ('type_of_application', 'exactly_name_application',
                       'name', 'phone', 'email')
        }),
        ('Комментарии', {
            'fields': ('question', 'comment')
        }),
        ('Статусы', {
            'fields': ('date', 'status', 'relevant')
        })
    )


