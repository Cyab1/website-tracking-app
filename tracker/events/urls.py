from django.urls import path
from .views import track_event,  home # Import the tracking view

urlpatterns = [
    path("api/events/", track_event, name="track_event"),
    path('', home, name='home')
]

