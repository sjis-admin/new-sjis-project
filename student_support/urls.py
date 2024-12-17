from django.urls import path
from . import views

app_name = 'student_support'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
]
