from . import views
from django.urls import path


urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('events_list/', views.EventList.as_view(), name="events"),
    path('saved_events/', views.SavedEventList.as_view(), name="saved"),
]