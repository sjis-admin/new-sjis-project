
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "St. Joseph International School"
admin.site.site_title = "SJIS Admin Portal"
admin.site.index_title = "Welcome to SJIS Portal"

urlpatterns =[
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('notice-board2/', include('notice_board2.urls', namespace='notice_board2')),
    # path('notice-board2/', include('notice_board2.urls', namespace='notice_board2')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('club_new/', include('club_new.urls', namespace='club_new')),
    path('syllabus/', include('syllabus.urls', namespace='syllabus')),
    path('rules/', include('rules.urls', namespace='rules')),
    path('tinymce/', include('tinymce.urls')),
    path('academic_calendar/', include('academic_calendar.urls', namespace='academic_calendar')),
    path('student_support/', include('student_support.urls', namespace='student_support')),
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    
