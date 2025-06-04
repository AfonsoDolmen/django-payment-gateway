from django.contrib import admin
from tickets.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ('id', 'name', 'description', 'price', 'created_at')
        list_filter = ('name', 'description')


admin.site.register(Ticket, TicketAdmin)
