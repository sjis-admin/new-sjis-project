from django.shortcuts import render
from .models import AcademicYear, Semester, Event, Holiday

def academic_calendar(request):
    academic_years = AcademicYear.objects.all()
    return render(request, 'academic_calendar/academic_calendar.html', {'academic_years': academic_years})

def events_by_semester(request, semester_id):
    semester = Semester.objects.get(id=semester_id)
    events = semester.events.all()
    holidays = Holiday.objects.filter(academic_year=semester.term.academic_year)
    return render(request, 'academic_calendar/events_by_semester.html', {'semester': semester, 'events': events, 'holidays': holidays})

def holidays_by_year(request, year_id):
    academic_year = AcademicYear.objects.get(id=year_id)
    holidays = academic_year.holidays.all()
    return render(request, 'academic_calendar/holidays_by_year.html', {'academic_year': academic_year, 'holidays': holidays})
