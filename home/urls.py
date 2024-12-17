from django.urls import path
from . import views
from .views import faculty_list, about_us_view, principal_message_view

app_name = 'home'

urlpatterns = [
    path("", views.home, name="home"),
    # path('about/', views.about_us_detail, name='about_us_detail'),
    path('about/', about_us_view, name='about_us_view'),
    path('news/', views.news_list, name='news_list'),
    path('<int:pk>/', views.news_detail, name='news_detail'),
    path('news-ticker/', views.news_ticker, name='news_ticker'),
    path('news-ticker/<int:pk>/', views.news_ticker_details, name='news_ticker_details'),
    path('faculty/', faculty_list, name='faculty_list'),
    path('principal-message/', principal_message_view, name='principal_message'),
    path('vice-principal-message/', views.vice_principal_message_view, name='vice_principal_message'),

]


