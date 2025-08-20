from django.db import models
from datetime import timedelta
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"

class Tweet(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date of update")
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="tweets", null=True, blank=True)
    
    def published_recently(self):
        return self.published_date >= timezone.now() - timedelta(days=7)
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"


