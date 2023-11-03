from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.location_summary, name='location_summary'),
    path('index', views.header, name='index'),
    path('analysis', views.race_filter_view, name='analysis'),
    path('about', views.about, name='about'),
    path('location/<int:location_id>/', views.event_summary, name='event_summary'),
    path('locations/<int:location_id>/events/<int:event_id>/', views.event_details, name='event_details'),
    path('locations/<int:location_id>/events/<int:event_id>/visual', views.event_visual, name='event_visual'),
    path('runner/<int:runner_id>', views.runner_details, name='runner_details'),
    path('get_events/', views.get_events, name='get_events'),
    path('participation', views.participation, name='participation'),
    path('time', views.time_visual, name='time_visual'),
]
