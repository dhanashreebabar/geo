# places_app/urls.py
from django.urls import path
from places.views import PlaceListCreateAPIView, PlaceDeleteAPIView, PlaceSearchAPIView,place_list_view

urlpatterns = [
    path('api/places/', PlaceListCreateAPIView.as_view(), name='place-list-create'),
    path('api/places/<int:pk>/', PlaceDeleteAPIView.as_view(), name='place-delete'),
    path('api/places/search/', PlaceSearchAPIView.as_view(), name='place-search'),
    path('places/', place_list_view, name='place-list'),
]


