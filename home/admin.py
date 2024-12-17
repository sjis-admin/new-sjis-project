# home/admin.py
from django.contrib import admin
from .models import CarouselImage, AboutUs, NewsArticle, NewsTicker, FacultyMember, PrincipalMessage, AboutUsSection
from tinymce.widgets import TinyMCE
from django.db import models

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['alt_text', 'image']


class AboutUsSectionInline(admin.TabularInline):
    model = AboutUsSection
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 20})},
    }

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsSectionInline]
    list_display = ['title']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 20})},
    }


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title',)


@admin.register(NewsTicker)
class NewsScrollAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)



class FacultyMemberAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('name', 'designation', 'category')
    
    # Add search functionality
    search_fields = ('name', 'designation')
    
    # Add filters for categories
    list_filter = ('category',)
    
    # Customize fields to be displayed in the detail view
    fields = ('name', 'designation', 'image', 'category')

# Register the FacultyMember model with the custom admin class
admin.site.register(FacultyMember, FacultyMemberAdmin)



class PrincipalMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'is_active')  # Display title, type, and active status
    list_filter = ('type', 'is_active')  # Filter by type and active status
    search_fields = ('title', 'message')  # Add search functionality for title and message
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }
    fieldsets = (
        (None, {
            'fields': ('type', 'title', 'message', 'image', 'is_active')
        }),
    )

admin.site.register(PrincipalMessage, PrincipalMessageAdmin)
