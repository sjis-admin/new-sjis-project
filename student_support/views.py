from django.shortcuts import render
from .models import Service, FAQ, Counselor

def home_view(request):
    services = Service.objects.all()
    faqs = FAQ.objects.all()
    counselors = Counselor.objects.all()
    
    context = {
        'services': services,
        'faqs': faqs,
        'counselors': counselors
    }
    return render(request, 'student_support/support_base.html', context)


def contact_view(request):
    return render(request, 'student_support/contact.html')
