from rest_framework.test import APITestCase
from django.db import IntegrityError, transaction
from .models import Breed

BREED = dict(name='Labrador', size='Large', friendliness=5, trainability=5, sheddingamount=4, exerciseneeds=5)
DOG = dict(name='Buddy', age=3, gender='Male', color='Yellow', favoritefood='Chicken', favoritetoy='Ball')


class DogAPITests(APITestCase):
    def setUp(self):
        self.breed = Breed.objects.create(**BREED)

    def test_ten_required_requests(self):
        response = self.client.post('/api/breeds/', BREED, format='json')
        self.assertEqual(response.status_code, 201)
        breed_id = response.data['id']
        self.assertEqual(self.client.get('/api/breeds/').status_code, 200)
        self.assertEqual(self.client.get(f'/api/breeds/{breed_id}').status_code, 200)
        updated = {**BREED, 'name': 'Golden Retriever'}
        response = self.client.put(f'/api/breeds/{breed_id}', updated, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], updated['name'])
        dog = {**DOG, 'breed': breed_id}
        response = self.client.post('/api/dogs/', dog, format='json')
        self.assertEqual(response.status_code, 201)
        dog_id = response.data['id']
        self.assertEqual(self.client.get('/api/dogs/').status_code, 200)
        self.assertEqual(self.client.get(f'/api/dogs/{dog_id}').data['name'], 'Buddy')
        response = self.client.put(f'/api/dogs/{dog_id}', {**dog, 'age': 4}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['age'], 4)
        self.assertEqual(self.client.delete(f'/api/dogs/{dog_id}').status_code, 204)
        self.assertEqual(self.client.delete(f'/api/breeds/{breed_id}').status_code, 204)
        self.assertEqual(self.client.get(f'/api/dogs/{dog_id}').status_code, 404)
        self.assertEqual(self.client.get(f'/api/breeds/{breed_id}').status_code, 404)

    def test_validation(self):
        for size in ['Tiny', 'Small', 'Medium', 'Large']:
            self.assertEqual(self.client.post('/api/breeds', {**BREED, 'size': size}, format='json').status_code, 201)
        self.assertEqual(self.client.post('/api/breeds', {**BREED, 'size': 'Huge'}, format='json').status_code, 400)
        for field in ['friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']:
            for value in [0, 6, 'invalid']:
                self.assertEqual(self.client.post('/api/breeds', {**BREED, field: value}, format='json').status_code, 400)
        for breed, age in [(999999, 3), (self.breed.pk, -1)]:
            self.assertEqual(self.client.post('/api/dogs', {**DOG, 'breed': breed, 'age': age}, format='json').status_code, 400)
        self.assertEqual(self.client.post('/api/dogs', {}, format='json').status_code, 400)

    def test_protected_breed_and_full_update(self):
        r = self.client.post('/api/dogs', {**DOG, 'breed': self.breed.pk}, format='json')
        self.assertEqual(self.client.delete(f'/api/breeds/{self.breed.pk}').status_code, 409)
        self.assertEqual(self.client.put(f"/api/dogs/{r.data['id']}", {'name': 'Incomplete'}, format='json').status_code, 400)

    def test_missing_and_unsupported_methods(self):
        for resource in ['dogs', 'breeds']:
            for method in ['get', 'put', 'delete']:
                self.assertEqual(getattr(self.client, method)(f'/api/{resource}/99999', {}, format='json').status_code, 404)
            self.assertEqual(self.client.delete(f'/api/{resource}/').status_code, 405)

    def test_database_constraints(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            Breed.objects.create(**{**BREED, 'friendliness': 6})
