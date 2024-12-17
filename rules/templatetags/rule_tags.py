from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def days_since_effective(value):
    """Calculate days since a rule became effective"""
    if not value:
        return "Not specified"
    
    days = (timezone.now().date() - value).days
    return f"{days} days ago"

@register.simple_tag
def severity_color(severity):
    """Return color class based on rule severity"""
    color_map = {
        'low': 'text-green-600',
        'medium': 'text-yellow-600',
        'high': 'text-orange-600',
        'critical': 'text-red-600'
    }
    return color_map.get(severity, 'text-gray-600')

@register.filter
def violation_status_color(status):
    """Return color class based on violation status"""
    color_map = {
        'reported': 'text-yellow-600',
        'under_investigation': 'text-blue-600',
        'resolved': 'text-green-600',
        'dismissed': 'text-red-600'
    }
    return color_map.get(status, 'text-gray-600')