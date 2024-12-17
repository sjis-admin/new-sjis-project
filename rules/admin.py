from django.contrib import admin
from django.utils.html import format_html
from .models import RuleCategory, Rule, Violation, RuleDocument

@admin.register(RuleCategory)
class RuleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'rule_count')
    search_fields = ('name',)

    def rule_count(self, obj):
        return obj.rules.count()
    rule_count.short_description = 'Number of Rules'

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'severity', 'status', 'effective_date', 'applicable_to')
    list_filter = ('category', 'severity', 'status', 'applicable_to')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Violation)
class ViolationAdmin(admin.ModelAdmin):
    list_display = ('rule', 'offender', 'reported_by', 'status', 'reported_at')
    list_filter = ('status', 'reported_at')
    search_fields = ('offender__username', 'rule__title')

@admin.register(RuleDocument)
class RuleDocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rule', 'uploaded_by', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('name', 'rule__title')