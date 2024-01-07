from django.urls import path
from .views import CustomerListAPIView, CustomerDetailAPIView,FunnelAssignmentCreateAPIView

urlpatterns = [
    path('customers/', CustomerListAPIView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
    path('funnel-assignment/', FunnelAssignmentCreateAPIView.as_view(), name='funnel-assignment-create'),

]