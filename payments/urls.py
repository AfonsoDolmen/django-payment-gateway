from django.urls import path
from payments.views import PaymentRedirectView

urlpatterns = [
    path('new/', PaymentRedirectView.as_view(), name='new-payment'),
]
