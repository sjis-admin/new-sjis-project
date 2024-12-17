from django.urls import path
from . import views

app_name = 'academic_calendar'

urlpatterns = [
    path('', views.academic_calendar, name='academic_calendar'),
    # path('terms/<int:year_id>/', views.terms_by_year, name='terms_by_year'),
    # path('semester/<int:term_id>/', views.semester_by_term, name='semester_by_term'),
    path('events/<int:semester_id>/', views.events_by_semester, name='events_by_semester'),
    path('holidays/<int:year_id>/', views.holidays_by_year, name='holidays_by_year'),
]
