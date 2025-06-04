from django.urls import path
from tickets.views import TicketListView, TicketDetailView

urlpatterns = [
    path('', TicketListView.as_view(), name='ticket-list'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
]
