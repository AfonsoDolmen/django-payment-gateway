from django.urls import path
from orders.views import OrderListView, OrderCreateView, OrderDeleteView

urlpatterns = [
    path('', OrderListView.as_view(), name='list-orders'),
    path('new/', OrderCreateView.as_view(), name='create-order'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='delete-order'),
]
