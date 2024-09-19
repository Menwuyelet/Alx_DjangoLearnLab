from django.urls import path, include
from .views import NotificationListView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
]