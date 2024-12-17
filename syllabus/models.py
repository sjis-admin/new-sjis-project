# models.py
from django.db import models
from django.core.validators import FileExtensionValidator

class SyllabusCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Syllabus Categories"

class Syllabus(models.Model):
    category = models.ForeignKey(SyllabusCategory, on_delete=models.CASCADE, related_name='syllabuses')
    title = models.CharField(max_length=200)
    file = models.FileField(
        upload_to='syllabi/', 
        validators=[FileExtensionValidator(['pdf'])],
        help_text="Upload only PDF files"
    )
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    download_count = models.PositiveIntegerField(default=0)  # New field to track downloads

    def __str__(self):
        return f"{self.category.name} - {self.title}"

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name_plural = "Syllabi"
