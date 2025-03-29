from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.response import Response

# start task 3
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')

class UnreadNotificationCountView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        unread_count = Notification.objects.filter(recipient=request.user, read=False).count()
        return Response({'unread_count': unread_count})

class NotificationReadUpdateView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer  # You might want a simpler serializer for this
    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save(read=True, recipient=self.request.user) # Ensure only recipient can mark as read

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)
    #end task 3