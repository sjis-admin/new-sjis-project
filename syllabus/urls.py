# urls.py
from django.urls import path
from . import views

app_name = 'syllabus'

urlpatterns = [
    path('list', views.syllabus_list, name='syllabus_list'),
    path('category/<int:category_id>/', views.syllabus_by_category, name='syllabus_category'),
    path('view/<int:syllabus_id>/', views.syllabus_view, name='syllabus_view'),
    path('download/<int:syllabus_id>/', views.download_syllabus, name='syllabus_download'),
    path('upload/', views.upload_syllabus, name='syllabus_upload'),
]



