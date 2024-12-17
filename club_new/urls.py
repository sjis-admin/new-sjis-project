from django.urls import path
from . import views
app_name = 'club_new'
urlpatterns = [
    # Route for the club list page
    path('', views.club_list, name='club_list'),
    
    # Route for the specific club detail page
    path('club/<int:club_id>/', views.club_detail, name='club_detail'),
]
