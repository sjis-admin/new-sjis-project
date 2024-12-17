from django.contrib import admin
from .models import AcademicYear, Semester, Event, Holiday

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'semester', 'is_holiday')
    search_fields = ('name',)

class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'holiday_date', 'academic_year')
    search_fields = ('name',)

admin.site.register(AcademicYear)
admin.site.register(Semester)
admin.site.register(Event, EventAdmin)
admin.site.register(Holiday, HolidayAdmin)
