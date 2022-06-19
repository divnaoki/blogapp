from django.db import models
from django.utils import timezone
from category.models import Category
class Blog(models.Model):
  title = models.CharField(null=False, max_length=120)
  content = models.TextField(null=False)
  create_at = models.DateTimeField(default=timezone.now)
  update_at = models.DateTimeField(default=timezone.now)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
