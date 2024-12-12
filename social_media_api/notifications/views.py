from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Notification
from django.shortcuts import render

# Create your views here.
@login_required
def fetch_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    unread_notifications = notifications.filter(is_read=False)
    unread_notifications.update(is_read=True)

    data = [{
        "id": n.id,
        "actor": n.actor.username,
        "verb": n.verb,
        "target": str(n.target) if n.target else None,
        "timestamp": n.timestamp,
        "is_read": n.is_read,
    } for n in notifications]

    return JsonResponse(data, safe=False)