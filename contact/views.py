# views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save message to the database
            contact_message = ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            # Send email to user
            user_email = form.cleaned_data['email']
            send_mail(
                subject="Thank you for contacting us",
                message="We have received your email. Thank you for contacting us. We'll get back to you as soon as possible.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user_email],
            )

            # Send email to admin
            send_mail(
                subject=f"New contact message from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
            )

            messages.success(request, 'Thank you for contacting us. We will respond soon.')
            return redirect('contact:contact')  # Update this line

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

