from django.contrib import admin
from .models import NoticeBoard, Grade
from .forms import NoticeBoardAdminForm
from django.utils.html import format_html
from django.utils import timezone
from tinymce.widgets import TinyMCE
from django.db import models

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Grade model
    """
    list_display = ('name', 'notices_count')
    search_fields = ('name',)

    def notices_count(self, obj):
        """
        Display the number of notices for each grade
        """
        return obj.notices_for_grade.count()
    notices_count.short_description = 'Number of Notices'

@admin.register(NoticeBoard)
class NoticeBoardAdmin(admin.ModelAdmin):
    form = NoticeBoardAdminForm

    list_display = (
        'title',
        'created_by',
        'created_at',
        'display_target_grades',
    )
    list_filter = (
        'created_at',
        'target_grades',
        'created_by',
        ('attachment', admin.BooleanFieldListFilter),
    )
    search_fields = (
        'title',
        'content',
        'created_by__username',
        'created_by__email'
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'attachment_preview',
        'view_hit_count'
    )
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'target_grades', 'attachment', 'created_by')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at', 'view_hit_count'),
            'classes': ('collapse',)
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

    # Adding custom actions for bulk updates
    actions = [
        'mark_as_new', 
        'clear_attachment', 
        'bulk_set_target_grades'
    ]

    def mark_as_new(self, request, queryset):
        """
        Bulk action to mark notices as 'new' (e.g., today)
        """
        updated_count = queryset.update(created_at=timezone.now())
        self.message_user(request, f"{updated_count} notices marked as new.")
    mark_as_new.short_description = 'Mark selected notices as New'

    def clear_attachment(self, request, queryset):
        """
        Bulk action to clear attachments
        """
        updated_count = queryset.update(attachment=None)
        self.message_user(request, f"{updated_count} attachments cleared.")
    clear_attachment.short_description = 'Clear Attachments'

    def bulk_set_target_grades(self, request, queryset):
        """
        Bulk action to set target grades
        """
        # Placeholder for implementing a custom form for bulk grade selection
        pass
    bulk_set_target_grades.short_description = 'Set Target Grades in Bulk'

    def display_target_grades(self, obj):
        """
        Display formatted target grades in the admin list view
        """
        return obj.formatted_target_grades
    display_target_grades.short_description = 'Target Grades'

    def is_new_notice(self, obj):
        """
        Boolean column for 'new' status in the list display
        """
        today = timezone.now().date()
        return obj.created_at.date() == today
    is_new_notice.boolean = True
    is_new_notice.short_description = 'New Notice'

    def attachment_status(self, obj):
        """
        Display attachment status
        """
        return 'Yes' if obj.attachment else 'No'
    attachment_status.short_description = 'Attachment'

    def attachment_preview(self, obj):
        """
        Preview of attachments (e.g., image or file download)
        """
        if obj.attachment:
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" width="100" /></a>',
                obj.attachment.url,
                obj.attachment.url
            )
        return "No Attachment"
    attachment_preview.short_description = 'Attachment Preview'

    def view_hit_count(self, obj):
        """
        Display the hit count for the notice
        """
        return obj.hit_count_generic.count if obj.hit_count_generic else 0
    view_hit_count.short_description = 'Hit Count'

    def days_since_creation(self, obj):
        """
        Calculate and display days since notice creation
        """
        days = (timezone.now().date() - obj.created_at.date()).days
        return f"{days} days ago"
    days_since_creation.short_description = 'Created'

    def get_queryset(self, request):
        """
        Enhance performance by prefetching related fields
        """
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related(
            'target_grades', 
            'created_by', 
            'hit_count_generic'
        )
        return queryset
