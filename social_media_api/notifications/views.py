from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from notifications.models import Notification
from notifications.serializers import NotificationSerializer
# Create your views here.

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')

