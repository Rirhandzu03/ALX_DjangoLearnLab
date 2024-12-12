from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.db import models
from .models import User

# Create your models here.
class Notification(models.Model):
    recipicient = models.ForeignKey(User, on_delete=models.CASCADE)
    actor = models.ForeignKey(User, on_delete=models.CASCADE)
    verb = models.CharField(max_length=250)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient.username}: {self.verb}"
    
#Notifications Utility method
def create_notification(recipient, actor, verb, target=None):
    """Creates a notification for a user."""
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target_content_type=ContentType.objects.get_for_model(target) if target else None,
        target_object_id=target.id if target else None,
        target=target
    )