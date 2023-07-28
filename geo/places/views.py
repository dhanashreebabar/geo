from rest_framework import generics
from django.db.models import Q  
from .models import Place
from .serializers import PlaceSerializer
from django.shortcuts import render
from django.contrib.postgres.search import SearchVector, SearchQuery



class PlaceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceDeleteAPIView(generics.DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

# class PlaceSearchAPIView(generics.ListAPIView):
#     queryset = Place.objects.all()
#     serializer_class = PlaceSerializer

#     def get_queryset(self):
#         query = self.request.query_params.get('query', '')
#         return Place.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

class PlaceSearchAPIView(generics.ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('query', '')
        vector = SearchVector('name', 'description')
        query = SearchQuery(search_query)

        return Place.objects.annotate(rank=SearchVector('name', 'description')).filter(rank=query).order_by('-rank')

def place_list_view(request):
    return render(request, 'place_list.html')        
