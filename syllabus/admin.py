from django.contrib import admin
from .models import SyllabusCategory, Syllabus

@admin.register(SyllabusCategory)
class SyllabusCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_active', 'uploaded_at']
    list_filter = ['is_active', 'category']
    search_fields = ['title']
