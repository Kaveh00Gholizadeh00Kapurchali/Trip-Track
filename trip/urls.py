
from django.urls import path

#local views
from .views import HomeView
from .views import trips_list
from .views import TripCreateView
from .views import TripDatailView
from .views import NoteDetailView
from .views import NoteListView
from .views import NoteCreateView
from .views import NoteUpdateView
from .views import NoteDeleteView
from .views import TripUpdateView
from .views import TripDeleteView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path("dashboard/", trips_list, name="trip-list"),
    path("dashboard/note/", NoteListView.as_view(), name="note-list"),
    path("dashboard/note/", NoteCreateView.as_view(), name="note-create"),
    path("dashboard/trip/create/", TripCreateView.as_view(), name="trip-create"),
    path("dashboard/trip/<int:pk>/", TripDatailView.as_view(), name="trip-detail"),
    path("dashboard/trip/<int:pk>/update/", TripUpdateView.as_view(), name="trip-update"),
    path("dashboard/trip/<int:pk>/delete/", TripDeleteView.as_view(), name="trip-delete"),
    path("dashboard/note/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),
    path("dashboard/note/<int:pk>/update/", NoteUpdateView.as_view(), name="note-update"),
    path("dashboard/note/<int:pk>/delete/", NoteDeleteView.as_view(), name="note-delete"),
]

# not template requied for delete view
# update uses same template as create view