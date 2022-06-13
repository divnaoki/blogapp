from django.db import models
from django.utils import timezone
class Blog(models.Model):
  title = models.CharField(null=False, max_length=120)
  content = models.TextField(null=False)
  create_at = models.DateTimeField(default=timezone.now)
  update_at = models.DateTimeField(default=timezone.now)
