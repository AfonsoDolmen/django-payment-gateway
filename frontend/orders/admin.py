from django.contrib import admin
from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ('id', 'ticket.name', 'ticket.price', 'status')
        list_filter = ('id')


admin.site.register(Order, OrderAdmin)
