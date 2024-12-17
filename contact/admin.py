# admin.py
from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'replied')
    search_fields = ('name', 'email')
    actions = ['send_reply']

    def send_reply(self, request, queryset):
        for message in queryset:
            if not message.replied:
                send_mail(
                    subject="Reply to your message",
                    message=message.reply_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[message.email],
                )
                message.replied = True
                message.save()
                self.message_user(request, f"Replied to {message.email}")
    send_reply.short_description = "Send reply to selected messages"
