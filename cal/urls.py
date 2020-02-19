from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    url('calendar/', views.CalendarView.as_view(), name='calendar'),
    url('event/new/', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]
