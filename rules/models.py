from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class RuleCategory(models.Model):
    """Categorization of rules and regulations"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True, help_text="FontAwesome icon class")
    
    def __str__(self):
        return self.name

class Rule(models.Model):
    """Specific rules within a category"""
    SEVERITY_CHOICES = [
        ('low', 'Low Impact'),
        ('medium', 'Medium Impact'),
        ('high', 'High Impact'),
        ('critical', 'Critical')
    ]
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('archived', 'Archived')
    ]
    
    title = models.CharField(max_length=255)
    category = models.ForeignKey(RuleCategory, on_delete=models.CASCADE, related_name='rules')
    description = models.TextField()
    full_text = models.TextField(blank=True, null=True)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='medium')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
        null=True,
        blank=True
    )
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_rules')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    effective_date = models.DateField(null=True, blank=True)
    applicable_to = models.CharField(max_length=100, help_text="Who this rule applies to (e.g., Students, Staff, All)", default='All')
    
    def __str__(self):
        return self.title

class Violation(models.Model):
    """Tracking of rule violations"""
    STATUS_CHOICES = [
        ('reported', 'Reported'),
        ('under_investigation', 'Under Investigation'),
        ('resolved', 'Resolved'),
        ('dismissed', 'Dismissed')
    ]
    
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='violations')
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reported_violations')
    offender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rule_violations')
    description = models.TextField()
    evidence = models.FileField(upload_to='violation_evidence/', null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='reported')
    reported_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.status == 'resolved' and not self.resolved_at:
            self.resolved_at = timezone.now()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Violation of {self.rule.title} by {self.offender.username}"

class RuleDocument(models.Model):
    """Attachments and supporting documents for rules"""
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='documents')
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='rule_documents/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name