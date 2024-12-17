# models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)
    reply_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
