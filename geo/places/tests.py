from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Place
from .serializers import PlaceSerializer

class PlaceListViewTest(APITestCase):
    def setUp(self):
        Place.objects.create(name="Place 1", description="Description 1", latitude=40.7128, longitude=-74.0060)
        Place.objects.create(name="Place 2", description="Description 2", latitude=34.0522, longitude=-118.2437)

    def test_list_places(self):
        url = '/api/places/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  
        self.assertEqual(response.data[0]['name'], "Place 1")
        self.assertEqual(response.data[1]['description'], "Description 2")


class PlaceSearchViewTest(APITestCase):
    def setUp(self):
        Place.objects.create(name="New York City", description="The city that never sleeps.", latitude=40.7128, longitude=-74.0060)
        Place.objects.create(name="Los Angeles", description="The entertainment capital of the world.", latitude=34.0522, longitude=-118.2437)

    def test_search_places(self):
        url = '/api/places/search/'
        response = self.client.get(url, {'query': 'New York'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "New York City")

        response = self.client.get(url, {'query': 'city'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['description'], "The city that never sleeps.")

