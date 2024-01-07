from django.urls import path
from funnel.views import FunnelListAPIView, FunnelDetailAPIView


urlpatterns = [
    path('funnels/', FunnelListAPIView.as_view(), name='funnel-list'),
    path('funnels/<int:pk>/', FunnelDetailAPIView.as_view(), name='funnel-detail'),
]