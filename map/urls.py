from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('events_list/', views.EventList.as_view(), name="events_list"),
    path('saved_events/', views.SavedEventList.as_view(), name="saved_events"),
    path('<slug:slug>/', views.EventDetails.as_view(), name="event_details"),
    path(
        'save_event/<slug:slug>/',
        views.SaveEvent.as_view(),
        name='save_event'
    )
]
