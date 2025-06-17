from django.contrib import admin
from payments.models import Payment


class PaymentAdmin(admin.ModelAdmin):
    class Meta:
        list_filter = ('id', 'status', 'total_amount', 'total_paid_amount',)


admin.site.register(Payment, PaymentAdmin)
