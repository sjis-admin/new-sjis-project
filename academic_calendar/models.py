from django.db import models
from django.utils import timezone

class AcademicYear(models.Model):
    year_start = models.DateField()
    year_end = models.DateField()
    description = models.CharField(max_length=255, help_text="Example: 2024-2025 Academic Year")

    def __str__(self):
        return f"{self.year_start.year}-{self.year_end.year}"

class Semester(models.Model):
    academic_year = models.ForeignKey(AcademicYear, related_name='semesters', on_delete=models.CASCADE)
    semester_number = models.IntegerField(choices=[(1, '1st Semester'), (2, '2nd Semester')])
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Semester {self.semester_number} - {self.academic_year}"

class Event(models.Model):
    semester = models.ForeignKey(Semester, related_name='events', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    is_holiday = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.event_date}"

    class Meta:
        ordering = ['event_date']

class Holiday(models.Model):
    academic_year = models.ForeignKey(AcademicYear, related_name='holidays', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    holiday_date = models.DateField()
    
    def __str__(self):
        return f"{self.name} - {self.holiday_date}"

    class Meta:
        ordering = ['holiday_date']
