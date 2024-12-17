from django.urls import path
from . import views

app_name = 'rules'

urlpatterns = [
    # Dashboard
    path('', views.rule_dashboard, name='rule_dashboard'),
    # Categories
    path('categories/', views.rule_category_list, name='rule_category_list'),
    
    # Rules
    path('rules/', views.rule_list, name='rule_list'),
    path('rules/category/<int:category_id>/', views.rule_list, name='rules_by_category'),
    path('rules/<int:rule_id>/', views.rule_detail, name='rule_detail'),
    
    # Violation Reporting
    path('rules/<int:rule_id>/report/', views.report_violation, name='report_violation'),
]