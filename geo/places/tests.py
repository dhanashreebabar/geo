from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Place

class PlaceAPITests(APITestCase):
    def setUp(self):
        self.place_data = {
            'name': 'Test Place',
            'description': 'This is a test place.',
            'latitude': 40.7128,
            'longitude': -74.0060,
        }
        self.place = Place.objects.create(**self.place_data)

    def test_create_place(self):
        url = reverse('place-list')
        response = self.client.post(url, self.place_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Place.objects.count(), 2)

    def test_retrieve_place(self):
        url = reverse('place-detail', args=[self.place.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.place_data['name'])

class PlaceAPITests(APITestCase):
    def setUp(self):
        self.place_data = {
            'name': 'Test Place',
            'description': 'This is a test place.',
            'latitude': 40.7128,
            'longitude': -74.0060,
        }
        self.place = Place.objects.create(**self.place_data)

    def test_create_place(self):
        url = reverse('place-list')
        response = self.client.post(url, self.place_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Place.objects.count(), 2)

    def test_retrieve_place(self):
        url = reverse('place-detail', args=[self.place.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.place_data['name'])

class PlaceSearchTests(APITestCase):
    def setUp(self):
        self.place1 = Place.objects.create(name='Place 1', description='Test description 1', latitude=40.0, longitude=-74.0)
        self.place2 = Place.objects.create(name='Place 2', description='Test description 2', latitude=41.0, longitude=-75.0)
        self.place3 = Place.objects.create(name='Place 3', description='Another test description', latitude=42.0, longitude=-76.0)

    def test_search_by_name(self):
        url = reverse('place-search')
        response = self.client.get(url, {'query': 'Place'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3) 
    def test_search_by_description(self):
        url = reverse('place-search')
        response = self.client.get(url, {'query': 'test description'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  

